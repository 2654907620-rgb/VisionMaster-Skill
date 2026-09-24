<!-- 综合提炼自：VM FAQ 手册 V1.8.1 全篇 + SDK 开发指南 常见问题 -->
# VM .NET SDK 高频编码范式（任务导向速查）

> 用途：拿到一个需求，先来这里找对应范式，再跳转详细章节。
> 「→」指向本知识库内的详细位置。

---

## 1. 环境与引用（90% 的"控件不显示/报错"都出在这里）

| 步骤 | 做法 | 详细 |
|---|---|---|
| 框架 | .NET Framework **4.6.1**，**不支持 .NET Core** | → `01` §3 / `02` §1 |
| 平台目标 | `Any CPU` 时**必须去掉「首选 32 位」** | → `08-faq-manual/02` 2.1.1 |
| 加引用 | 用 `..\Development\V4.x\ComControls\Tool\ImportRef.exe`，**一个项目只用一次** | → `08-faq-manual/02` 2.1.1 |
| 复制本地 | 手动加引用后必须改 **CopyLocal = False** | → `03` §9 |
| 缺 mfc120u.dll | 运行 `MSVBCRT.AIO_v2020.05.20.exe` | → `08-faq-manual/02` 2.1.2/2.1.3 |
| `Vm.Core.Solution` 报错 | 排查顺序：加密狗 → 管理员权限 → 首选32位 → 版本与补丁 → 关掉 VM 双开 → `EnvironmentDetectionTool.exe` | → `08-faq-manual/02` 2.1.5 |
| 控件不刷新 | 确认 `bin\x64` 是最新；调 `vmRenderControl1.UpdateVMResultShow()` | → `08-faq-manual/02` 2.1.9 |
| 流程不显示 | `CreateSolutionInstance()` 必须在 `VmMainView` / `GetObjectPointer()` **之前**调用一次 | → `08-faq-manual/02` 2.1.9 |

**四语言/框架配置**：C#/WinForm、Qt、MFC、VB.Net，核心都是「拷贝 `ComControls\bin\x64` 下 DLL + `ImportRef.exe` 导引用」。→ `08-faq-manual/02` 2.1.1–2.1.4

---

## 2. 最小可运行骨架（C# WinForm）

```csharp
using System;
using VM.Core;
using VM.PlatformSDKCS;

public partial class MainForm : Form
{
    public MainForm()
    {
        InitializeComponent();
        VmSolution.Load(@"D:\Test.sol", "");   // 绝对路径 + UTF-8
        VmSolution.Instance.DisableModulesCallback();       // 关全部回调省 CPU
        var ps = (VmProcedure)VmSolution.Instance["流程1"];
        ps.EnableResultCallback();                          // 只为需要的对象开回调
    }

    private void btnRun_Click(object sender, EventArgs e)
    {
        VmSolution.Instance.SyncRun();          // 同步跑一次
    }

    private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
    {
        VmSolution.Instance?.Dispose();         // 退出前释放
    }
}
```

---

## 3. 任务 → 范式 速查表

### 3.1 图像输入

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| 用文件喂图给图像源模块 | `imgModu.ModuParams.ImageSourceType = ImageSourceTypeEnum.SDK;` + `imgModu.SetImagePath(path)` | → `02` §5 |
| 用内存喂图 | `new ImageBaseData(bytes, len, w, h, VMPixelFormat.VM_PIXEL_MONO_08)` → `SetImageData` | → `02` §5 |
| 给流程 / Group 设输入图像 | `procedure.ModuParams.SetInputImage_V2("ImageData", img)` / `groupParam.SetInputImage_V2(...)` | → `08-faq-manual/02` 2.2.2 |
| 给普通模块设输入图像 | 填 `InputImageData`（`Names` 固定 `InImage`/`InImageWidth`/`InImageHeight`/`InImagePixelFormat`，**不可改名**）→ `ModuParams.SetInputImage(...)` | → `08-faq-manual/07` |
| 相机直接喂给 VM | 相机回调拿 `MV_FRAME_OUT` → 构造 `ImageBaseData` → `SetImageData` | → `08-faq-manual/07` §3.2 |
| 图像源 SDK 模式 | `ModuParams.ImageSourceType = ImageSourceTypeEnum.SDK`（否则设图无效） | → `05-api/采集.md` |

> ⚠️ **所有输入类接口「仅当次执行起效」**：流程执行后清空需重设；模块自执行 `Run()` 不清空。→ `03` §4

### 3.2 ROI 与参数

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| 设 ROI / 几何形状 | `SetBinaryData("RoiType", ptr, size)` / `SetBinaryData("GeometryType", ...)`，坐标按图像宽高**归一化** | → `08-faq-manual/02` 2.2.3 |
| 用接口设矩形/圆环/点/线 ROI | `SetInputBox` / `SetInputAnnulus` / `SetInputCircle` / `SetInputLine` / `SetInputPoint` / `SetInputRect` / `SetInputPolygon` / `SetInputPosture` / `SetInputEllipse` | → `05-api/逻辑工具.md` |
| 读/写模块参数 | `modu.ModuParams.XxxParam = value`（强类型属性，最稳）或 `GetParamValue/SetParamValue(name, str)` | → `05-api/` |
| 隐藏某个参数 | 改模块 xml 的 `<CustomVisible>False</CustomVisible>` | → `08-faq-manual/02` 2.3.7 |
| 多个不连续 ROI 同时检测 | 用 BlindPolygon / 多 ROI 接口 | → `08-faq-manual/01` 1.2.24 |
| **ROI 生效优先级**（V4.4.0 已知） | **矩形 ROI > 圆形 ROI > 多边形 ROI** | → `01` §2 |

### 3.3 取结果（最容易踩坑的一段）

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| 取单模块结果 | `var r = modu.ModuResult;`（**每次执行后要重新获取**以刷新数据） | → `03` §4 |
| 取流程输出结果 | `GetIntOutputResult` / `GetFloatOutputResult` / `GetStringOutputResult` / `GetImageOutputResult` | → `08-faq-manual/02` 2.4.1 |
| 取 Group 输出图像 | `groupResult.GetOutputImageV2("ImageData0")` | → `03` §5.2 |
| 图像输出字段名 | `Imageout0` / `ImageWidthout0` / `ImageHeightout0` / `ImagePixelFormatout0`（固定） | → `08-faq-manual/02` 2.4.1 |
| 像素格式数值 | `17301505` = MONO8；`35127316` = RGB24 | → `08-faq-manual/02` 2.4.1 |
| 取耗时 | `ProcessTime` / `ModuleTime` / `AlgorithmTime`（回调结构里也有 `fProcessTime`/`fModuleTime`/`fAlgorithmTime`） | → `03` §7.2 |
| **推荐做法** | 结果/状态**写进回调**，不要在按钮里轮询 | → `03` §7 |

**常用回调映射**：流程结束 `OnWorkStatusEvent`；模块结束 `OnModuleResultCallbackEvent`；方案加载完成 `OnSolutionLoadEndEvent`；加密狗 `OnDongleEvent`；通讯收数 `OnCommunicationRecvCallBackEvent`。

### 3.4 渲染与控件

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| 渲染控件绑定 | **推荐绑定流程**（`ModuleSource = VmProcedure`）—— 高内聚低耦合，一个控件可显示多模块 | → `08-faq-manual/02` 2.3.1 |
| 控件上画自定义图形 | `ctrl.DrawShape(shape)` / `ctrl.AddShape(shape)`（AddShape 仅当次执行有效） | → `03` §6 |
| 渲染控件加载本地图 | `ctrl.ImageSource = imageBaseData` | → `03` §6 |
| 渲染控件存图 | **必须放在按钮事件里**；回调 / `Run()` 之后立即存会拿到未渲染完成的图。更推荐用**输出图像模块** | → `08-faq-manual/02` 2.3.11 |
| 参数控件绑定模块 | `paramCtrl.ModuleSource = modu` | → `03` §6 |
| 隐藏某些参数页 | `ctrl.SetParamTabVisible(tabName, false)` | → `03` §6 |
| 控件颜色 | `AppColorService.CurColorDefine` | → `08-faq-manual/02` 2.3.5 |
| 控件语言切英文 | 改 `..\ComControls\Assembly\LangCFG\LanguageSet.cfg` 为 `en-us` | → `03` §10 |
| 前端界面控件大小自适应 | 绑定后按容器 DPI/尺寸处理 | → `08-faq-manual/02` 2.3.10 |
| 鼠标点取像素坐标 | 渲染控件鼠标事件 + 坐标映射 | → `08-faq-manual/01` / `02` 2.3.8 |
| **嵌入整个 VM 软件** | `SetParent` + `MoveWindow` 把 `VisionMaster.exe` 主窗口挂到自己 Panel | → `08-faq-manual/02` 2.3.6 |
| 子窗口放主界面控件报错 | 见专题 | → `08-faq-manual/03` 2.3.8 |

### 3.5 图像类型互转（跨 SDK 联用必看）

> 完整转换矩阵与逐类型代码 → `08-faq-manual/07-image-conversion.md`

**三个致命细节**

1. **通道顺序**：`Bitmap` / `Mat` 三通道是 **BGR**；VM 的 `ImageBaseData`、`ImageData`、`CMvdImage/IMvdImage` 是 **RGB**。互转**必须交换 R/B**。
   C# 侧：`Cv2.CvtColor(mat, mat, ColorConversionCodes.BGR2RGB)`
2. **C++ 例外**：C++ 算子图像像素格式是 `MVD_PIXEL_BGR_BGR24_C3`（BGR），而 VM 图像是 `MVD_PIXEL_RGB_RGB24_C3`（RGB）—— 与 C# 习惯相反，**核对 SDK 版本**。
3. **内存所有权**：`ImageBaseData_V2` 用 `IntPtr` 构造是**浅拷贝**，用完要 `Marshal.FreeHGlobal`；`InputImageData.Data` 需 `Marshal.AllocHGlobal` 申请并自行释放。`HKA_IMAGE.data[0]` 需 `malloc`。
   → 性能敏感场景用指针浅传递，别每帧 `new byte[]` 深拷贝，但要严守释放责任。

**其它高频点**

- `Bitmap` 要求 4 字节行对齐（`Stride`），VM/MVD 图像不要求 —— 转换时要按 Stride 去冗余位。
- Halcon：灰度 `GetImagePointer1`/`GenImage1`；彩色 `GetImagePointer3`/`GenImage3`（RGB 三通道分别取指针）。
- QImage：`(void*)qImage.constBits()` 直接取指针；`Format_Grayscale8` 灰度，`Format_RGB888` 彩色（已是 RGB）。
- 流程图像 ↔ 算子图像互转是 **VM SDK 与算子SDK 联用的核心**。
- 脚本图像类型 `ImageData`，注意原文属性拼写为 `Heigth`、枚举为 `ImagePixelFormate`（官方原文如此）。
- 流程/Group 输入类型：VM4.2 为 `ImageBaseData_V2`；VM4.3 起流程/Group/模块输出统一为 `ImageBaseData`。

### 3.6 标定与定位引导

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| N 点标定 | 收 N（≥4）组像素↔物理点，输出标定文件 | → `04` 标定 |
| 清空标定点 / 生成标定文件 / 渲染轨迹 | 走 `N点标定` 模块的参数字段 | → `08-faq-manual/02` 2.2.7 |
| 单相机抓取 | 标定流程 + 生产流程；`单点抓取` 输出相对/绝对坐标 | → `08-faq-manual/06` |
| 单相机纠偏 / 上下相机映射对位 | `单点纠偏` / `单点映射对位` | → `08-faq-manual/06` |
| 定位精度与误差分析 | 见定位引导专题 + 定位精度评估助手工具 | → `08-faq-manual/06` / `08` |
| 模板导入/导出 | 匹配模板 + `ImportModelData`/`ExportModelData`（V4.4.0 新增 `GetModelNum()`/`ExportModelData()`） | → `08-faq-manual/01` 1.2.26 |

### 3.7 换型、调试与运维

| 我要做的事 | 范式 | 详细 |
|---|---|---|
| 通讯触发快速匹配换型 | 全局脚本 + 通讯 | → `08-faq-manual/01` 1.3.11 |
| 分支字符控制调试模式 | `分支字符` 模块 | → `08-faq-manual/02` 2.2.14 |
| 模块禁用 | `DisableXxx` / 模块使能参数 | → `08-faq-manual/02` 2.2.15 |
| 条件检测设范围 | 参数范围配置 | → `08-faq-manual/02` 2.2.10 |
| 方案高速保存 | 见方案保存专题 | → `08-faq-manual/02` 2.2.1 |
| 多版本间切换与程序升级 | `DevelopProcedureUpgradeTool.exe` + `ImportRef.exe` | → `01` §4.2 |
| 程序启动报错通用排查 | `OnModelLoadWarnEvent` + `EnvironmentDetectionTool.exe` | → `08-faq-manual/03` 2.1.5 |
| 用户日志打印 | 见用户日志专题 | → `08-faq-manual/03` 2.1.9 |
| 通过注册表取 VM 安装路径 | 读注册表 | → `08-faq-manual/03` 2.1.6 |
| 普通用户权限以 EXE 启动 Server | `xxx.exe.config` 的 `AppSettings` 加 `ServerPath` 等 | → `08-faq-manual/02` 2.1.13 |

---

## 4. 十大高频坑（先怀疑这些）

1. **输入类接口"仅当次执行起效"** —— 第二次跑没图，八成是没重设输入。→ `03` §4
2. **`ModuResult` 没重新获取** —— 拿到的是旧数据。→ `03` §4
3. **忘记 `DisableModulesCallback()`** —— 大量模块回调把 CPU 吃满。→ `03` §3
4. **忘记 `Dispose()` / 在析构函数里调接口** —— 崩溃或资源泄漏。→ `03` §8
5. **BGR/RGB 搞反** —— 彩色图整体颜色错乱。→ §3.5
6. **`CopyLocal = True`** —— DLL 冲突，控件失效。→ §1
7. **没去掉"首选 32 位"** —— 控件异常/崩溃。→ §1
8. **渲染控件存图时机太早** —— 存到未渲染完成的图。→ §3.4
9. **独立 Group 当普通 Group 用** —— 它不隶属方案，取不到，且非线程安全。→ `03` §1
10. **中英文方案名混用** —— 中文 VM 建方案用中文名取对象，英文 VM 用英文名。→ `03` §2

---

## 5. 错误码怎么查

| 前缀 | 含义 | 文件 |
|---|---|---|
| `IMVS_EC_*` | SDK 层错误（版本/参数/内存/句柄/方案状态/通信/加密狗） | `06-status-codes/01-sdk-status.md` |
| `MVALG_STS_ERR_*`（算法通用） | 算法库通用错误（能力检查/内存/图像格式/参数/文件/模型版本/GPU） | `06-status-codes/04a-算法通用状态码.md` |
| `MVALG_STS_ERR_MVBPATMATCH*` 等 | 具体算法模块错误（匹配/Blob/边缘/标定/OCR/测距/颜色/CNN…） | `06-status-codes/04a-2D算法模块.md`、`04a-深度学习模块.md` |
| `MVD_CAM_E_*`、`MVD_E_*` | 相机 / 渲染相关 | `06-status-codes/05-camera-status.md` |

> 共收录 **2873 条**状态码，按前缀族索引见 `06-status-codes/00-INDEX.md`。
> 排查套路：先看 `IMVS_EC_*` 判断是 SDK 层还是算法层；算法层错误说明通常已写明"需检查输入/调节参数"。

---

## 6. 性能与稳定性清单

- [ ] 关掉不需要的回调（`DisableModulesCallback` + 按需 `EnableResultCallback`）
- [ ] 图像传递用指针浅拷贝，避免每帧深拷贝
- [ ] 图像用完及时释放（`FreeHGlobal`），注意**谁申请谁释放**
- [ ] 长时间连续运行：关注虚拟内存（见 FAQ 1.1.10）、流程运行间隔（`SetRunInterval`）
- [ ] 规避流程运行时卡死：见 `08-faq-manual/03` 1.1.3
- [ ] 深度学习：GPU 长期停再跑耗时变长、StackOverFlow 等见 `08-faq-manual/05`
- [ ] 退出前统一 `Dispose`，并把 `Dispose` 放在 `FormClosing` 而不是析构函数
