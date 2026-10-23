# -*- coding: utf-8 -*-
"""将智能体专项项目计划书.md 渲染为 PDF（纯文本符号，无 LaTeX）"""
import re, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

import sys
base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) >= 3:
    src = sys.argv[1]
    out = sys.argv[2]
else:
    src = os.path.join(base, "参赛材料", "智能体专项项目计划书.md")
    out = os.path.join(base, "参赛材料", "智能体专项项目计划书.pdf")

# 注册中文字体
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def inline_md(s):
    s = esc(s)
    # 加粗 **x**
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    # 行内代码 `x`
    s = re.sub(r'`([^`]+)`', r'<font face="Courier" size="8">\1</font>', s)
    return s

styles = getSampleStyleSheet()
h1 = ParagraphStyle('h1', parent=styles['Heading1'], fontName='STSong-Light', fontSize=18, leading=24, spaceAfter=8, spaceBefore=6, textColor=colors.HexColor('#1a3c6e'))
h2 = ParagraphStyle('h2', parent=styles['Heading2'], fontName='STSong-Light', fontSize=14, leading=20, spaceAfter=6, spaceBefore=10, textColor=colors.HexColor('#1a3c6e'))
h3 = ParagraphStyle('h3', parent=styles['Heading3'], fontName='STSong-Light', fontSize=12, leading=17, spaceAfter=4, spaceBefore=8)
body = ParagraphStyle('body', parent=styles['Normal'], fontName='STSong-Light', fontSize=10.5, leading=16, spaceAfter=4, alignment=TA_LEFT)
quote = ParagraphStyle('quote', parent=body, leftIndent=12, textColor=colors.HexColor('#555555'))
li = ParagraphStyle('li', parent=body, leftIndent=14, bulletIndent=4, spaceAfter=2)

story = []

def parse_blocks(lines):
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i].rstrip('\n')
        if not line.strip():
            i += 1
            continue
        # 代码块
        if line.strip().startswith('```'):
            buf = []
            i += 1
            while i < n and not lines[i].strip().startswith('```'):
                buf.append(lines[i].rstrip('\n'))
                i += 1
            i += 1
            for b in buf:
                story.append(Paragraph(esc(b), ParagraphStyle('code', parent=body, fontName='Courier', fontSize=7.5, leading=10, leftIndent=8, textColor=colors.HexColor('#333333'))))
            story.append(Spacer(1, 4))
            continue
        s = line.strip()
        if s.startswith('# '):
            story.append(Paragraph(inline_md(s[2:]), h1)); i += 1
        elif s.startswith('## '):
            story.append(Paragraph(inline_md(s[3:]), h2)); i += 1
        elif s.startswith('### '):
            story.append(Paragraph(inline_md(s[4:]), h3)); i += 1
        elif s.startswith('> '):
            story.append(Paragraph(inline_md(s[2:]), quote)); i += 1
        elif s.startswith('- ') or re.match(r'^\d+\.\s', s):
            # 收集连续列表项
            items = []
            while i < n and (lines[i].strip().startswith('- ') or re.match(r'^\d+\.\s', lines[i].strip())):
                t = lines[i].strip()
                if t.startswith('- '):
                    t = t[2:]
                else:
                    t = re.sub(r'^\d+\.\s', '', t)
                items.append(t)
                i += 1
            for it in items:
                story.append(Paragraph('• ' + inline_md(it), li))
        elif s.startswith('|'):
            # 表格
            tbl = []
            while i < n and lines[i].strip().startswith('|'):
                row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                tbl.append(row)
                i += 1
            if len(tbl) >= 2:
                # 去掉分隔行
                if re.match(r'^[\s\-:|]+$', tbl[1][0]) or all(re.match(r'^:?-{2,}:?$', c) for c in tbl[1]):
                    tbl.pop(1)
                data = [[Paragraph(inline_md(c), ParagraphStyle('c', parent=body, fontSize=8.5, leading=12)) for c in row] for row in tbl]
                t = Table(data, repeatRows=1)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#eef3fa')),
                    ('GRID', (0,0), (-1,-1), 0.4, colors.HexColor('#bbbbbb')),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                    ('LEFTPADDING', (0,0), (-1,-1), 4),
                    ('RIGHTPADDING', (0,0), (-1,-1), 4),
                    ('TOPPADDING', (0,0), (-1,-1), 3),
                    ('BOTTOMPADDING', (0,0), (-1,-1), 3),
                ]))
                story.append(t)
                story.append(Spacer(1, 6))
        else:
            story.append(Paragraph(inline_md(s), body)); i += 1

with open(src, encoding='utf-8') as f:
    lines = f.readlines()

parse_blocks(lines)

doc = SimpleDocTemplate(out, pagesize=A4, topMargin=20*mm, bottomMargin=18*mm, leftMargin=18*mm, rightMargin=18*mm)
doc.build(story)
print("PDF 已生成:", out)
