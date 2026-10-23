---
doc_type: knowledge_dependency
chapter: 全局
knowledge_ids: all
difficulty: mixed
figure_required: false
---

# 离散数学知识点前置-后继关系表

> 本表用于智能体规划学习路径：当用户某知识点正确率未达标时，主动建议先复习其前置知识点。
>
> **ID编码规则（三级）**：
> - 知识大点：`CH{章号}-{两位序号}`，如 `CH1-03` 表示第1章第3个知识大点（对应知识点md的`##`标题）
> - 知识小点：`CH{章号}-{两位序号}-{两位序号}`，如 `CH1-03-02` 表示第1章第3个知识大点下的第2个知识小点（对应知识点md的`###`标题）
> - 题目：`KP-CH{章号}-{两位序号}`（基础）/ `KP-CH{章号}-A{两位序号}`（综合提升），如 `KP-CH1-03` 表示第1章第3题
> - 跨章引用：如 `CH1-06` 表示第1章的推理理论
>
> **解锁条件**：前置知识点正确率 ≥ 70% 后解锁；无前置者默认解锁。

---

## 第1章 命题逻辑

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH1-01 | 命题与联结词 | 无 | basic | 默认解锁 |
| CH1-02 | 命题公式与赋值 | CH1-01 | basic | CH1-01正确率≥70% |
| CH1-03 | 等值演算 | CH1-01, CH1-02 | basic | CH1-01、CH1-02正确率≥70% |
| CH1-04 | 范式（主析取/主合取） | CH1-03 | basic | CH1-03正确率≥70% |
| CH1-05 | 联结词完备集 | CH1-03 | basic | CH1-03正确率≥70% |
| CH1-06 | 推理理论 | CH1-03 | basic | CH1-03正确率≥70% |
| KP-CH1-A01 | 多公式等值演算综合 | CH1-03, CH1-04 | comprehensive | CH1-03、CH1-04正确率≥70% |
| KP-CH1-A02 | 主范式推导证明 | CH1-04, CH1-03 | comprehensive | CH1-03、CH1-04正确率≥70% |
| KP-CH1-A03 | 复杂推理证明 | CH1-06, CH1-03 | comprehensive | CH1-03、CH1-06正确率≥70% |
| KP-CH1-A04 | 实际问题符号化推理 | CH1-01, CH1-06 | comprehensive | CH1-01、CH1-06正确率≥70% |
| KP-CH1-A05 | 等价与异或综合 | CH1-03, CH1-05 | comprehensive | CH1-03、CH1-05正确率≥70% |
| KP-CH1-A06 | 主范式求解综合 | CH1-04, CH1-03 | comprehensive | CH1-03、CH1-04正确率≥70% |
| KP-CH1-A07 | 归谬法证明 | CH1-06, CH1-03 | comprehensive | CH1-03、CH1-06正确率≥70% |
| KP-CH1-A08 | 可满足性分析推理 | CH1-01, CH1-06 | comprehensive | CH1-01、CH1-06正确率≥70% |
| KP-CH1-A09 | 吸收律与公式类型判定 | CH1-03, CH1-02 | comprehensive | CH1-02、CH1-03正确率≥70% |
| KP-CH1-A10 | 双向推理与等价引入 | CH1-06, CH1-03 | comprehensive | CH1-03、CH1-06正确率≥70% |

---

## 第2章 谓词逻辑

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH2-01 | 谓词与量词基本概念 | CH1-01 | basic | CH1-01正确率≥70% |
| CH2-02 | 谓词公式与解释 | CH2-01, CH1-02 | basic | CH2-01、CH1-02正确率≥70% |
| CH2-03 | 谓词等值演算 | CH2-01, CH1-03 | basic | CH2-01、CH1-03正确率≥70% |
| CH2-04 | 前束范式 | CH2-03, CH1-04 | basic | CH2-03、CH1-04正确率≥70% |
| CH2-05 | 谓词推理理论 | CH2-03, CH1-06 | basic | CH2-03、CH1-06正确率≥70% |
| KP-CH2-A01 | 多重量词等值演算 | CH2-03, CH2-01 | comprehensive | CH2-01、CH2-03正确率≥70% |
| KP-CH2-A02 | 复杂前束范式化简 | CH2-04, CH2-03 | comprehensive | CH2-03、CH2-04正确率≥70% |
| KP-CH2-A03 | 谓词推理综合证明 | CH2-05, CH2-03 | comprehensive | CH2-03、CH2-05正确率≥70% |
| KP-CH2-A04 | 实际场景符号化推理 | CH2-01, CH2-05 | comprehensive | CH2-01、CH2-05正确率≥70% |
| KP-CH2-A05 | 量词分配与反例构造 | CH2-03, CH2-02 | comprehensive | CH2-02、CH2-03正确率≥70% |
| KP-CH2-A06 | 约束变元改名综合 | CH2-04, CH2-03 | comprehensive | CH2-03、CH2-04正确率≥70% |
| KP-CH2-A07 | 归谬法与UG规则 | CH2-05, KP-CH1-A07 | comprehensive | CH2-05、KP-CH1-A07正确率≥70% |
| KP-CH2-A08 | 化简规则与EG规则 | CH2-05, CH2-01 | comprehensive | CH2-01、CH2-05正确率≥70% |
| KP-CH2-A09 | 量词辖域扩张综合 | CH2-03, CH2-04 | comprehensive | CH2-03、CH2-04正确率≥70% |
| KP-CH2-A10 | 推理有效性分析 | CH2-05, CH2-03 | comprehensive | CH2-03、CH2-05正确率≥70% |

---

## 第3章 集合论

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH3-01 | 集合基本概念 | 无 | basic | 默认解锁 |
| CH3-02 | 集合运算 | CH3-01 | basic | CH3-01正确率≥70% |
| CH3-03 | 有穷集合计数（容斥原理） | CH3-02 | basic | CH3-02正确率≥70% |
| CH3-04 | 二元关系基础 | CH3-02 | basic | CH3-02正确率≥70% |
| CH3-05 | 等价关系与偏序关系 | CH3-04, CH3-02 | basic | CH3-02、CH3-04正确率≥70% |
| CH3-06 | 函数基础 | CH3-04 | basic | CH3-04正确率≥70% |
| KP-CH3-A01 | 集合恒等式综合证明 | CH3-02, CH3-05 | comprehensive | CH3-02、CH3-05正确率≥70% |
| KP-CH3-A02 | 三集合容斥应用题 | CH3-03, CH3-02 | comprehensive | CH3-02、CH3-03正确率≥70% |
| KP-CH3-A03 | 幂集与集合运算结合 | CH3-01, CH3-02 | comprehensive | CH3-01、CH3-02正确率≥70% |
| KP-CH3-A04 | 集合基数综合计算 | CH3-02, CH3-03 | comprehensive | CH3-02、CH3-03正确率≥70% |
| KP-CH3-A05 | 分配律与吸收律证明 | CH3-02, CH3-05 | comprehensive | CH3-02、CH3-05正确率≥70% |
| KP-CH3-A06 | 数论与容斥综合 | CH3-03, CH3-02 | comprehensive | CH3-02、CH3-03正确率≥70% |
| KP-CH3-A07 | 幂集的幂集与归纳法 | CH3-01, CH3-03 | comprehensive | CH3-01、CH3-03正确率≥70% |
| KP-CH3-A08 | 区域计数与恰选两门 | CH3-03, CH3-02 | comprehensive | CH3-02、CH3-03正确率≥70% |
| KP-CH3-A09 | 对称差与特征函数法 | CH3-02, CH3-05 | comprehensive | CH3-02、CH3-05正确率≥70% |
| KP-CH3-A10 | 集合基数最值分析 | CH3-03, CH3-02 | comprehensive | CH3-02、CH3-03正确率≥70% |

---

## 第4章 二元关系

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH4-01 | 有序对与笛卡尔积 | CH3-02 | basic | CH3-02正确率≥70% |
| CH4-02 | 二元关系基本概念 | CH4-01, CH3-04 | basic | CH3-04、CH4-01正确率≥70% |
| CH4-03 | 关系运算（复合/逆/幂） | CH4-02, CH3-02 | basic | CH3-02、CH4-02正确率≥70% |
| CH4-04 | 关系性质（自反/对称/传递） | CH4-02, CH4-03 | basic | CH4-02、CH4-03正确率≥70% |
| CH4-05 | 关系闭包 | CH4-03, CH4-04 | basic | CH4-03、CH4-04正确率≥70% |
| CH4-06 | 等价关系与划分 | CH4-04, CH4-05 | basic | CH4-04、CH4-05正确率≥70% |
| CH4-07 | 偏序关系与哈斯图 | CH4-04, CH4-05 | basic | CH4-04、CH4-05正确率≥70% |
| KP-CH4-A01 | 复合关系与性质综合 | CH4-03, CH4-04 | comprehensive | CH4-03、CH4-04正确率≥70% |
| KP-CH4-A02 | 三种闭包与幂运算 | CH4-05, CH4-03 | comprehensive | CH4-03、CH4-05正确率≥70% |
| KP-CH4-A03 | 等价关系与划分综合 | CH4-06, CH4-02 | comprehensive | CH4-02、CH4-06正确率≥70% |
| KP-CH4-A04 | 偏序集极值与上下界 | CH4-07, CH4-06 | comprehensive | CH4-06、CH4-07正确率≥70% |
| KP-CH4-A05 | 等价关系交并运算 | CH4-06, CH4-04 | comprehensive | CH4-04、CH4-06正确率≥70% |
| KP-CH4-A06 | 闭包单调性证明 | CH4-05, CH4-03 | comprehensive | CH4-03、CH4-05正确率≥70% |
| KP-CH4-A07 | 划分诱导与关系矩阵 | CH4-06, CH4-02 | comprehensive | CH4-02、CH4-06正确率≥70% |
| KP-CH4-A08 | 哈斯图文字描述与确界 | CH4-07, CH4-04 | comprehensive | CH4-04、CH4-07正确率≥70% |
| KP-CH4-A09 | 逆关系与对称反对称 | CH4-03, CH4-04 | comprehensive | CH4-03、CH4-04正确率≥70% |
| KP-CH4-A10 | 等价关系与传递闭包 | CH4-06, CH4-05 | comprehensive | CH4-05、CH4-06正确率≥70% |

---

## 第5章 函数

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH5-01 | 函数基本概念 | CH4-02, CH3-06 | basic | CH3-06、CH4-02正确率≥70% |
| CH5-02 | 单射/满射/双射 | CH5-01, CH4-04 | basic | CH4-04、CH5-01正确率≥70% |
| CH5-03 | 复合函数与反函数 | CH5-01, CH4-03 | basic | CH4-03、CH5-01正确率≥70% |
| CH5-04 | 集合基数 | CH5-02, CH3-01 | basic | CH3-01、CH5-02正确率≥70% |
| CH5-05 | 鸽巢原理与置换 | CH5-02, CH4-03 | basic | CH4-03、CH5-02正确率≥70% |
| KP-CH5-A01 | 函数性质综合证明 | CH5-02, CH5-03 | comprehensive | CH5-02、CH5-03正确率≥70% |
| KP-CH5-A02 | 复合函数与反函数计算 | CH5-03, CH5-02 | comprehensive | CH5-02、CH5-03正确率≥70% |
| KP-CH5-A03 | 双射构造与等势证明 | CH5-02, CH5-04 | comprehensive | CH5-02、CH5-04正确率≥70% |
| KP-CH5-A04 | 像集原像集集合等式 | CH5-02, CH3-02 | comprehensive | CH3-02、CH5-02正确率≥70% |
| KP-CH5-A05 | 有限集函数性质 | CH5-02, CH5-05 | comprehensive | CH5-02、CH5-05正确率≥70% |
| KP-CH5-A06 | 双射复合与反函数 | CH5-03, CH5-02 | comprehensive | CH5-02、CH5-03正确率≥70% |
| KP-CH5-A07 | 可数集与基数比较 | CH5-04, CH5-02 | comprehensive | CH5-02、CH5-04正确率≥70% |
| KP-CH5-A08 | 单射性质与像集交集 | CH5-02, CH3-02 | comprehensive | CH3-02、CH5-02正确率≥70% |
| KP-CH5-A09 | 函数诱导等价关系 | CH5-02, CH4-06 | comprehensive | CH4-06、CH5-02正确率≥70% |
| KP-CH5-A10 | 函数计数与满射计数 | CH5-02, CH3-03 | comprehensive | CH3-03、CH5-02正确率≥70% |

---

## 第6章 代数系统基础

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH6-01 | 二元运算与代数系统 | CH3-02 | basic | CH3-02正确率≥70% |
| CH6-02 | 半群与独异点 | CH6-01 | basic | CH6-01正确率≥70% |
| CH6-03 | 群的基本性质 | CH6-02 | basic | CH6-02正确率≥70% |
| CH6-04 | 环与域 | CH6-03, CH3-02 | basic | CH3-02、CH6-03正确率≥70% |
| CH6-05 | 格与布尔代数 | CH6-01, CH3-05 | basic | CH3-05、CH6-01正确率≥70% |
| KP-CH6-A01 | 运算性质综合判定 | CH6-01, CH6-03 | comprehensive | CH6-01、CH6-03正确率≥70% |
| KP-CH6-A02 | 逆元唯一性与交换群证明 | CH6-03, CH6-02 | comprehensive | CH6-02、CH6-03正确率≥70% |
| KP-CH6-A03 | 子群判定与验证 | CH6-03, CH6-02 | comprehensive | CH6-02、CH6-03正确率≥70% |
| KP-CH6-A04 | 模运算群与元素阶 | CH6-03, CH6-01 | comprehensive | CH6-01、CH6-03正确率≥70% |
| KP-CH6-A05 | 单位元逆元公式综合 | CH6-01, CH6-03 | comprehensive | CH6-01、CH6-03正确率≥70% |
| KP-CH6-A06 | 元素阶与鸽巢原理 | CH6-03, CH5-05 | comprehensive | CH5-05、CH6-03正确率≥70% |
| KP-CH6-A07 | 循环子群与生成元 | CH6-03, CH6-02 | comprehensive | CH6-02、CH6-03正确率≥70% |
| KP-CH6-A08 | Klein四元群与循环群 | CH6-03, CH6-02 | comprehensive | CH6-02、CH6-03正确率≥70% |
| KP-CH6-A09 | 幂集交运算代数判定 | CH6-01, CH3-02 | comprehensive | CH3-02、CH6-01正确率≥70% |
| KP-CH6-A10 | 拉格朗日定理与陪集 | CH6-03, CH4-06 | comprehensive | CH4-06、CH6-03正确率≥70% |

---

## 第7章 图论基础

| 知识点ID | 知识点名称 | 前置知识点ID | 难度层级 | 解锁条件 |
|---------|-----------|-------------|---------|---------|
| CH7-01 | 图的基本概念（握手定理） | CH3-01 | basic | CH3-01正确率≥70% |
| CH7-02 | 路与连通性 | CH7-01, CH4-03 | basic | CH4-03、CH7-01正确率≥70% |
| CH7-03 | 图的矩阵表示 | CH7-01, CH4-02 | basic | CH4-02、CH7-01正确率≥70% |
| CH7-04 | 欧拉图与哈密顿图 | CH7-02, CH7-01 | basic | CH7-01、CH7-02正确率≥70% |
| CH7-05 | 树的性质 | CH7-02, CH3-03 | basic | CH3-03、CH7-02正确率≥70% |
| CH7-06 | 平面图与欧拉公式 | CH7-02, CH7-01 | basic | CH7-01、CH7-02正确率≥70% |
| CH7-07 | 图的着色 | CH7-06, CH7-04 | basic | CH7-04、CH7-06正确率≥70% |
| KP-CH7-A01 | 握手定理与度数序列 | CH7-01, CH7-05 | comprehensive | CH7-01、CH7-05正确率≥70% |
| KP-CH7-A02 | 连通性与度数条件证明 | CH7-02, CH7-04 | comprehensive | CH7-02、CH7-04正确率≥70% |
| KP-CH7-A03 | 欧拉图与哈密顿图综合 | CH7-04, CH7-01 | comprehensive | CH7-01、CH7-04正确率≥70% |
| KP-CH7-A04 | 树性质与方程求解 | CH7-05, CH7-01 | comprehensive | CH7-01、CH7-05正确率≥70% |
| KP-CH7-A05 | 邻接矩阵与通路计数 | CH7-03, CH7-02 | comprehensive | CH7-02、CH7-03正确率≥70% |
| KP-CH7-A06 | 可图化判定与Havel-Hakimi | CH7-01, CH7-02 | comprehensive | CH7-01、CH7-02正确率≥70% |
| KP-CH7-A07 | 欧拉定理证明与对比 | CH7-04, CH7-05 | comprehensive | CH7-04、CH7-05正确率≥70% |
| KP-CH7-A08 | 树的充要条件与圈秩 | CH7-05, CH7-02 | comprehensive | CH7-02、CH7-05正确率≥70% |
| KP-CH7-A09 | 矩阵幂与强连通判定 | CH7-03, CH7-02 | comprehensive | CH7-02、CH7-03正确率≥70% |
| KP-CH7-A10 | 树等价定义与判定 | CH7-05, CH7-01 | comprehensive | CH7-01、CH7-05正确率≥70% |

---

## 跨章依赖总览

```
命题逻辑 (CH1)
  └→ 谓词逻辑 (CH2)          [CH1-01, CH1-03, CH1-06]
集合论 (CH3)
  ├→ 二元关系 (CH4)          [CH3-02, CH3-04]
  ├→ 函数 (CH5)              [CH3-06, CH4-02]
  └→ 代数系统 (CH6)          [CH3-02, CH3-05]
二元关系 (CH4)
  ├→ 函数 (CH5)              [CH4-02, CH4-03, CH4-04]
  └→ 图论矩阵表示 (CH7-03)   [CH4-02, CH4-03]
图论基础 (CH7)               [CH3-01, CH4-03]
```

## 智能体使用规则

1. **解锁检查**：用户请求某知识点时，先查本表前置ID；若前置正确率 < 70%，提示用户先复习前置知识点
2. **学习路径推荐**：按章节顺序 CH1→CH2→CH3→CH4→CH5→CH6→CH7 推进，同章内按ID序号学习
3. **综合提升题**：标注 comprehensive 的题目需先完成对应基础知识点（basic）且正确率≥70%
4. **跨章依赖**：如学 CH2 前需先掌握 CH1 的命题逻辑；学 CH4 前需先掌握 CH3 的集合运算
5. **默认解锁**：CH1-01、CH3-01 无前置知识点，为默认解锁的起点
