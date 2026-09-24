# VisionMaster-Skill

海康机器人 **VisionMaster（VM）** 机器视觉软件知识库 Skill —— 基于三套官方文档全量结构化构建，可直接作为 WorkBuddy / Claude Code 类 Agent 的技能包使用。

## 这是什么

一个面向 **VM 二次开发与使用** 的本地知识库技能：把官方 SDK 指南、FAQ 手册、应用帮助三套文档全量拆解成可检索的结构化 Markdown，让 Agent 在回答 VM 相关问题时能直接命中官方原文与 API 签名，而不是靠记忆编。

## 覆盖范围

| 维度 | 内容 |
|---|---|
| 开发模式 | VM 应用 / VM SDK 二次开发（.NET）/ 算子 SDK 开发 / 算法模块开发（C++）四种模式选型 |
| 对象模型 | `VmSolution` / `VmProcedure` / `ModuParams` / `ModuResult` 等核心对象与调用范式 |
| API 参考 | 19 大类约 200 个算法模块的 API 签名、枚举数值 |
| 状态码 | **2873 条**状态码（`MVALG_STS_ERR` / `IMVS_EC` 等） |
| 模块参数 | **163 个模块 · 1691 个参数 · 3290 个结果**（含义 / 取值范围 / 默认值） |
| 图形界面 | 方案搭建、调试运行、通信管理、全局脚本、相机管理 |
| FAQ | 环境配置、控件嵌入、结果获取、图像类型互转、标定定位、版本升级 |

## 目录结构

```
visionmaster-sdk/
├── SKILL.md                    # 技能主入口（含工作流程与核心事实卡）
├── build/                      # 构建脚本（46 个）：CHM→md、PDF 抽取分片、API/状态码/参数提取
└── references/
    ├── 00-INDEX.md             # 总索引
    ├── 01-overview-and-modes.md            # 四种开发模式选型
    ├── 02-quickstart.md                    # 快速开始
    ├── 03-core-objects.md                  # 核心对象模型
    ├── 04-modules-catalog.md               # 模块总目录
    ├── 05-api/                             # API 参考（按大类分文件）
    ├── 06-status-codes/                    # 状态码（前缀族分文件）
    ├── 07-faq-sdk.md                       # SDK FAQ 提炼
    ├── 08-faq-manual/                      # FAQ 手册结构化
    ├── 09-code-patterns.md                 # 任务 → 范式 → 跳转速查
    ├── 10-app-manual/                      # 应用帮助（GUI 操作 + 模块参数）
    ├── 11-modules-params/                  # 模块参数手册（全量结构化）
    └── fulltext/                           # 官方原文全量层
        ├── sdk-guide/                      # SDK 开发指南 CHM 全量
        ├── faq/                            # VM FAQ 手册（1414 页）全量
        ├── app-help/                       # VM 应用帮助 WebHelp 全量
        └── bundles/                        # 核心章节合并包
```

## 数据来源

三套海康机器人官方文档，全量学习后结构化：

1. 《VisionMaster 算法开发平台 SDK 开发指南 V4.4.3（.NET）》CHM —— 2186 页
2. 《VM FAQ 手册 V1.8.1》PDF —— 1414 页，303 条目录项
3. 《VM 应用帮助》WebHelp —— 296 页，GUI 操作 + 全模块参数手册

厂商：杭州海康机器人股份有限公司 · 机器人业务中心 · 视觉应用解决方案一部

## 使用方式

把 `visionmaster-sdk/` 整个目录放进 Agent 的技能目录即可：

```bash
# 用户级技能目录
cp -r visionmaster-sdk ~/.workbuddy/skills/
# 或项目级
cp -r visionmaster-sdk <项目>/.workbuddy/skills/
```

之后提问诸如「VM 二次开发怎么取流程输出」「报 MVALG_STS_ERR 怎么排查」「DL 字符定位有哪些参数」时，Agent 会按 `SKILL.md` 描述自动加载本技能。

## 注意事项

- 本库是**软件侧**知识库（SDK / API / 模块参数 / GUI 操作），**不含**相机、镜头、光源等硬件型号选型手册。
- 各参数给出的是官方定义与取值范围，不代替现场工艺调优经验。
- 仅覆盖海康 VisionMaster，非海康平台（HALCON / VisionPro 等）仅在"联合开发"章节涉及互转。
- 文档版权归杭州海康机器人股份有限公司所有，本仓库仅作结构化的学习检索用途。

## 规模

2632 个文件 / 约 19 MB
