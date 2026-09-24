---
name: visionmaster-sdk
description: 海康机器人 VisionMaster（VM）机器视觉软件知识库 —— 基于《VisionMaster算法开发平台SDK开发指南V4.4.3（.NET）》CHM 全量文档 + 《VM FAQ 手册 V1.8.1》1414 页 PDF + 《VM 应用帮助》WebHelp（D:\VisionMaster4.4.0\Applications\Help\CH）三套官方文档构建。涵盖四种开发模式选型（VM应用/VM SDK二次开发/算子SDK开发/算法模块开发）、.NET SDK 对象模型与调用范式、19 大类约 200 个算法模块的 API 参考（含枚举数值）、2873 条状态码、编程引导与官方常见问题、VM 图形界面操作与模块参数手册（每个模块的输入/输出/参数/取值范围/默认值）、以及环境配置/控件嵌入/结果获取/图像类型互转/标定定位/算子SDK/算法模块/版本升级等全专题 FAQ。当用户提到 VisionMaster、VM、VM4.x、VM SDK、IMVS、VmSolution、VmProcedure、ModuParams、ModuResult、VM二次开发、算子SDK、算法模块开发、视觉软件开发、图像源模块、渲染控件、参数配置控件、VisionMaster报错码、MVALG_STS_ERR、IMVS_EC，或询问机器视觉软件的二次开发/API/模块选型/模块参数怎么配/界面怎么操作/环境配置/控件嵌入/错误码时使用本 skill。
agent_created: true
---

# VisionMaster（VM）机器视觉软件知识库

> **来源**（三套官方资料，全量学习后结构化）：
> 1. 《VisionMaster 算法开发平台SDK 开发指南 V4.4.3（.NET）》CHM — 2186 页，全量转 Markdown
> 2. 《VM FAQ 手册 V1.8.1》PDF — 1414 页，303 条目录项，全量提炼
> 3. 《VM 应用帮助》WebHelp（`D:\VisionMaster4.4.0\Applications\Help\CH\index.html`）— 296 页，VM 图形界面操作 + 全模块参数手册，全量提炼
>
> 厂商：杭州海康机器人股份有限公司 | 机器人业务中心·视觉应用解决方案一部·生态建设组

---

## 0. 这个 skill 是什么 / 不是什么

**✅ 是**
- VisionMaster **.NET SDK（VM 二次开发）** 的权威知识库：对象模型、调用范式、完整 API 签名、枚举值、状态码
- VM 软件**使用/配置/排错**的实战知识库：环境配置、控件嵌入、结果获取、图像互转、标定定位、版本升级
- **VM 图形界面操作 + 模块参数手册**：方案搭建、调试运行、通信管理、全局脚本、以及**每个模块的输入/输出/参数含义/取值范围/默认值**（应用帮助层 `10-app-manual/`）
- **算子SDK 开发**与**算法模块开发（C++）**的入门与专题知识
- 四种开发模式的**选型决策依据**

**❌ 不是**
- 相机/镜头/光源等**硬件的型号选型手册**（只覆盖软件侧的相机调用接口）
- 现场业务**调参经验/工艺 know-how**（本库给的是每个参数的官方定义与取值范围，不代替现场工艺调优）
- 非海康的其他视觉平台（HALCON/VisionPro 等）—— 只在"联合开发"章节涉及互转

---

## 1. 工作流程（按顺序走）

1. **判断用户是哪一种角色**（决定回答的技术路线）：
   - 只想跑检测、调参数 → **VM 应用**（无开发）
   - 要写 C# 程序、定制界面、把 VM 嵌进自己的软件 → **VM SDK 二次开发**（本库主线）
   - 要用海康算法库自己做全部界面 → **算子SDK 开发**
   - 要写自己的算法并当 VM 模块用 → **算法模块开发（C++）**
   → 详见 `references/01-overview-and-modes.md` §1
2. **读 `references/03-core-objects.md`**（对象模型与调用范式）—— 几乎任何 SDK 问题都先看这一页，它给出了 80% 的答案骨架。
3. **拿到具体任务**（比如"取流程输出""把 Bitmap 传给 VM""控件不显示"）→ 直接查 `references/09-code-patterns.md`（任务→范式→跳转的速查表）。
4. **需要具体 API 名/签名/枚举** → 查 `references/05-api/<大类>.md`。
5. **需要"该用哪个模块"** → 查 `references/04-modules-catalog.md`（一句话职责）。
6. **需要某个模块的完整参数表 / 默认值 / 取值范围 / 输出结果类型** → 查 `references/11-modules-params/<大类>.md`（官方用户手册第 13 章全量结构化，1691 参数 / 3290 结果）。
7. **遇到报错** → 查 `references/06-status-codes/00-INDEX.md` 定位前缀族，再打开对应文件。
8. **需要官方逐字原文** → 用 Grep 检索 `references/fulltext/sdk-guide/`（CHM 全量）或 `references/fulltext/faq/`（PDF 全量）。每个页面都带 `<!-- path:接口函数 > 定位 > 快速匹配 > ... -->` 可还原官方目录位置。
9. **回答时优先给出**：结论 → 关键代码 → 具体 API 名/路径 → 指向本库文件（如"详见 `11-modules-params/定位.md` 13.2.3"），方便用户对照。

---

## 2. 核心事实卡（速记）

| 项目 | 内容 |
|---|---|
| 厂商 | 杭州海康机器人股份有限公司 |
| 简称 | VM（VisionMaster） |
| 当前主流版本线 | VM4.0 / VM4.2 / VM4.3 / **VM4.4.0**（SDK 指南版本 V4.4.3） |
| 二次开发语言 | C# / .NET Framework；也支持 Qt、MFC、VB.Net、LabView |
| 框架要求 | **.NET Framework 4.6.1+**，**不支持 .NET Core** |
| 平台目标 | `Any CPU` 时**必须去掉「首选 32 位」** |
| 入口单例 | `VmSolution.Instance` |
| 对象取法 | `VmSolution.Instance["流程1.图像源1"]`（流程内用 `流程名.模块名`；全局模块直接用模块名） |
| 模块三件套 | `ModuParams`（参数/输入）、`ModuResult`（结果）、`Run()`（自执行） |
| 核心 DLL | `VM.Core.dll`、`VM.PlatformSDKCS.dll`（+ 控件库 `VMControls.*.dll`） |
| 控件库 | `VMControls.Winform.Release.dll` / `VMControls.WPF.Release.dll` |
| 加引用工具 | `..\Development\V4.x\ComControls\Tool\ImportRef.exe` |
| 环境检测工具 | `..\Applications\Tools\VMCollector\VMCollector.exe` |
| 异常收集工具 | `..\Applications\Tools\AbnormalInfoCollectTool\AbnormalInfoCollectTool.exe` |
| 激活工具 | `..\Applications\Tools\ActivationTool\ActivationTool.exe` |
| **最高频坑** | 输入类接口（`SetImageData`/`SetInputXxx`）**"仅当次执行起效"**；`ModuResult` 每次执行后要重新获取 |
| 性能开关 | `VmSolution.Instance.DisableModulesCallback()` 可大幅降 CPU，但要取结果的对象需单独 `EnableResultCallback()` |

---

## 3. 知识库文件地图

```
references/
├── 00-INDEX.md                ← 总索引 / 按问题类型找文件（先看这个）
├── 01-overview-and-modes.md   ← 四种开发模式选型、发版要点、环境、激活、许可、工具、示例
├── 02-quickstart.md           ← 编程引导全文（方案/流程/模块/Group/全局模块/控件/事件 示例代码）
├── 03-core-objects.md         ← ★ 核心对象模型与调用范式（最重要的一页）
├── 04-modules-catalog.md      ← 19 大类 ~200 个算法模块职责一句话
├── 05-api/                    ← 22 个分类 API 参考（类 + 成员签名 + 说明 + 枚举值）
├── 06-status-codes/           ← 2873 条状态码（SDK / 算子 / 算法 / 相机）+ 前缀族索引
├── 07-faq-sdk.md              ← CHM 官方常见问题 12 条（含完整代码）
├── 08-faq-manual/             ← FAQ 手册 V1.8.1 全篇提炼（8 个分册，400+ 条目）
├── 09-code-patterns.md        ← ★ 任务导向速查表 + 十大高频坑 + 性能清单
├── 10-app-manual/             ← ★ VM 应用手册提炼（11 个分册：界面操作 + 全模块参数概览）
├── 11-modules-params/         ← ★★ 全模块参数与结果全表（1691 参数 / 3290 结果，含默认值与取值范围）
│   ├── 00-INDEX.md            ← 15 大类 · 163 模块总索引（参数数/结果数/手册页）
│   └── <大类>.md              ← 采集/定位/测量/识别/缺陷检测/边缘学习/深度学习/标定/运算/
│                                图像处理/颜色处理/拆分组合/图形生成/逻辑工具/通信
└── fulltext/
    ├── sdk-guide/             ← CHM 2186 页全量 Markdown（含目录路径标记）
    ├── faq/                   ← FAQ 手册全文 + 11 个章节分片 + 目录 JSON
    ├── app-help/              ← 应用帮助 WebHelp 296 页全量 Markdown（含目录路径标记 + _index.json）
    └── bundles/               ← 合订本：core-chapters.md（编程引导/示例/常见问题/工具等 50 页连读）+ status-codes-raw.md（状态码章节原文 7 页）
```

---

## 4. 高频问题 → 直达路径

| 问题 | 去哪 |
|---|---|
| 该选哪种开发方式？ | `01-overview-and-modes.md` §1 |
| 环境怎么配？（DLL/引用/首选32位/复制本地） | `09-code-patterns.md` §1；`08-faq-manual/02` 2.1 |
| 怎么加载方案、跑流程、取结果？ | `03-core-objects.md` §3 §4 |
| 怎么给图像源/流程/Group/模块设输入图像？ | `09-code-patterns.md` §3.1 |
| 怎么设 ROI / 参数？ | `09-code-patterns.md` §3.2 |
| ModuResult 拿不到数据？ | `03-core-objects.md` §4（"仅当次执行起效" + 重新获取结果对象） |
| 控件绑定 / 不显示 / 不刷新？ | `03-core-objects.md` §6；`09-code-patterns.md` §3.4 |
| Bitmap/Mat/Halcon/相机图 怎么转成 VM 图像？ | `08-faq-manual/07-image-conversion.md`；`09-code-patterns.md` §3.5 |
| 要做 XX 检测，用哪个模块？ | `04-modules-catalog.md`；选型对比见 `10-app-manual/03a..06d` 各篇末尾对比表 |
| XX 模块有哪些 API / 枚举值？ | `05-api/<大类>.md` |
| XX 模块的参数是什么意思 / 取值范围 / 默认值？ | **`11-modules-params/<大类>.md`**（权威全表，含默认值与取值范围）；概念性说明见 `10-app-manual/`（03a 定位 / 03b 图像处理 / 03c 图形生成 / 04 采集通信逻辑 / 05 测量标定运算 / 06a 识别 / 06b 缺陷 / 06c 边缘学习 / 06d 深度学习） |
| XX 模块有哪些输出结果 / 结果是什么类型？ | `11-modules-params/<大类>.md`（结果名 + 类型 + 说明）；API 侧见 `05-api/<大类>.md` |
| VM 界面上怎么操作（搭方案/连流程/调试/看结果）？ | `10-app-manual/01-setup.md`、`02-debug-tools-troubleshoot.md` |
| 相机管理 / 通信管理 / 全局脚本 / 数据队列怎么配？ | `10-app-manual/01-setup.md` §3 §6 |
| 脚本 / Python脚本 模块怎么用？ | `10-app-manual/04-mod-logic-comm-acq.md` §3.2 |
| 标定怎么选（N点/N图像/标定板/映射）？ | `10-app-manual/05-mod-measure-calc-calib.md` §2.9 对比表 |
| 单点抓取/纠偏/对位的输入输出与前提？ | `10-app-manual/05-mod-measure-calc-calib.md` §三 |
| 报错码 0xE000…… / MVALG_STS_ERR…… 是什么意思？ | `06-status-codes/00-INDEX.md` |
| 算子SDK 怎么开发？ | `08-faq-manual/04-ch3-operator-sdk.md` |
| 自定义算法模块（C++）怎么开发？ | `08-faq-manual/05-ch4-algo-module.md` |
| 标定 / 定位引导 / 抓取纠偏怎么做？ | `08-faq-manual/06-cases-and-tutorials.md`；`05-api/标定.md`、`05-api/运算.md` |
| 版本升级 / 多版本共存注意什么？ | `01-overview-and-modes.md` §4.2；`08-faq-manual/08-version-and-tools.md` |
| 有官方示例程序吗？ | `01-overview-and-modes.md` §7；`02-quickstart.md` §10 |
| 试用版有什么限制？ | `01-overview-and-modes.md` §4.1 |

---

## 5. 回答规范（重要）

1. **结论先行**，直接给做法。默认简洁；用户说"详细介绍"再展开。
2. **给代码就给完整可跑的形式**（含 `using`、判空、异常处理、`Dispose`），不要只给孤零零一行 API 名。
3. **API 名/枚举名/路径/DLL 名一律原样**，不要意译或改写。注意官方原文中的拼写（如 `ImagePixelFormate`、`Heigth`）**保持原样**并提示这是官方拼写。
4. **区分版本**：同一接口在不同版本有差异（如 `ImageBaseData_V2` 是 VM4.2 引入，4.3 起流程输出统一为 `ImageBaseData`；`ImportProcess`/`ExportProcess` 在 V4.4.0 弃用改 `Load`/`SaveAs`）。回答时**明确标注版本**，不确定就问用户用的版本。
5. **不要编造**。FAQ 手册中大量内容原文是截图，抽取后标注了 `（原文为图示，文字缺失）` —— 遇到这种条目要**如实说明**"该部分原文为图，无法给出准确步骤"，绝不臆造。
6. **指路而不是倒垃圾**：给出关键片段后指向本库具体文件（如 `references/05-api/定位.md`），让用户能自己往下查。
7. **优先官方示例**：能引用官方 Demo（`SolutionControl` / `ProcessControl` / `GetResultControl` / `OCRDemoCs` / `LocateDemoCs` / `DeepLearningDemoCs`）时优先引用，比自造示例更可信。

---

## 6. 维护说明

- 知识库由官方 CHM（GB2312，Doxygen）+ PDF FAQ 手册全量转换/提炼而来；CHM 全量原文已固化在 `references/fulltext/sdk-guide/`。
- **构建脚本已归档在本 skill `build/` 目录**（46 个 Python 脚本：CHM 解包→GB18030 转 Markdown、PDF 抽取/目录/分片、API/状态码/模块参数提取、app-help 转换、verify_kb.py 验收），可复用于新版本文档重建；生成时的临时工作目录 `VisionMaster\.workbuddy\vmkb\` 保留有全部中间产物。
- 若用户提供了**新版本**的 SDK 指南 CHM 或 FAQ 手册 PDF，可复用同一流程：`hh.exe -decompile` 解包 → GB18030 解码转 Markdown（`div.fragment` 需按 `div.line` 拼行，否则代码会逐 token 断行）→ Doxygen `memberdecls` 表格解析出 API 参考 → PDF 按 `印刷页码 = PDF页码 - 9` 分片 → 分派提炼。
- ⚠️ CHM 是 **GB2312** 编码，用 UTF-8 读会全部乱码；必须显式 `gb18030` 解码。
