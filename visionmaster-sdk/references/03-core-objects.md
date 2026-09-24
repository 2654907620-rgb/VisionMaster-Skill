<!-- 来源：《VisionMaster算法开发平台SDK开发指南V4.4.3（.NET）》编程引导（方案/流程/模块/Group/全局模块/控件/事件）+ 接口函数参考 -->
# VM .NET SDK 核心对象模型与调用范式

> 这是本知识库**最重要的一页**。掌握这一页，80% 的 VM 二次开发问题都能自行推导。
> 完整可运行示例代码见 `02-quickstart.md`；每个类的完整成员见 `05-api/`。

---

## 1. 对象层级

```
VmSolution（方案，单例）
├── VmProcedure（流程）× N            ← 流程是执行单位，有独立触发/运行
│   ├── 算法模块（VmModule 派生，如 IMVSCircleFindModuTool）
│   └── IMVSGroupTool（组合模块 / Group）
│       └── 子模块（含深层嵌套）
└── 全局模块（GlobalVariable / CommManager / DataQueue / GlobalCamera / LightControl …）
    ※ 全局模块与流程并列，通过 VmSolution.Instance["全局变量1"] 直接取，不经流程

**独立 Group**：`IMVSGroupTool.LoadIndependentGroup("D:\\TestGro.gro")`
   ※ 与方案**并列**，不是所属关系，**无法用方案对象获取或操作**；非线程安全，不支持多线程调用。
```

**布局-运行两套坐标**：方案（Solution）是所有流程/全局模块的容器，`VmSolution.Instance` 是**单例**，所有获取对象的入口。

---

## 2. 对象获取方式（最常用的一句）

```csharp
// 加载方案：仅支持绝对路径，编码格式 UTF-8
VmSolution.Load("D:\\Test.sol", "");

// 用「限定全名称」取任意对象（流程 / 模块 / Group / 全局模块）
VmProcedure  vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
ImageSourceModuleTool imageModu = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
IMVSCircleFindModuTool circleModu = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];

// 全局模块：直接用全局模块名，不带流程前缀
GlobalVariableModuleTool globalVar = (GlobalVariableModuleTool)VmSolution.Instance["全局变量1"];
```

| 关键点 | 说明 |
|---|---|
| 名称格式 | 流程内对象用 **`流程名.模块名`**；全局模块用 **`全局模块名`** |
| 中英文 | 中文 VM 下搭建的方案用**中文名**（`"全局变量1"`）；英文 VM 下用**英文名**（`"Global Variable1"`、`"CommManagerModule1"`、`"Data Queue1"`、`"Global Camera1"`、`"Light Control1"`） |
| 判空 | 取到后**必须判空**再调用（`if (null != globalVar) { … }`） |
| 批量获取 | `VmSolution.Instance.GetAllProcedureObjects(ref procedureList)`、`GetAllProcedureList()`、`GetAllModuleList()` |

---

## 3. 标准调用范式（方案级）

```csharp
using System;
using System.Collections.Generic;
using VM.Core;
using VM.PlatformSDKCS;

namespace VM.Test
{
    public class SolutionTest
    {
        static void Main()
        {
            try
            {
                // 1) 方案信息（可选）
                string strVersion = VmSolution.Instance.GetSolutionVersion("D:\\Test.sol", "");
                bool bPassword = VmSolution.Instance.HasPassword("D:\\Test.sol");

                // 2) 加载方案（仅绝对路径，UTF-8）
                VmSolution.Load("D:\\Test.sol", "");
                string strPath = VmSolution.Instance.SolutionPath;

                // 3) 取流程对象
                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
                List<VmProcedure> procedureList = new List<VmProcedure>();
                VmSolution.Instance.GetAllProcedureObjects(ref procedureList);

                // 4) 流程/模块控制
                VmSolution.Instance.DisableProcedure("流程1");   // 禁用后不参与方案运行
                VmSolution.Instance.EnableProcedure("流程1");
                VmSolution.Instance.DeleteOneProcedure("流程2");

                // 5) 性能优化：禁用全部回调（可显著降低 CPU 占用）
                VmSolution.Instance.DisableModulesCallback();
                vmProcedure.EnableResultCallback();              // 只启用需要取结果的
                VmSolution.Instance.EnableModulesCallback();

                // 6) 执行
                VmSolution.Instance.SyncRun();                   // 方案同步执行一次
                VmSolution.Instance.SetRunInterval(500);         // 连续执行间隔 (ms)
                VmSolution.Instance.ContinuousRunEnable = true;  // 开始连续执行
                VmSolution.Instance.ContinuousRunEnable = false; // 停止连续执行

                // 7) 保存 / 关闭
                VmSolution.Save();
                VmSolution.SaveAs("D:\\Test1.sol", "");
                VmSolution.Instance.CloseSolution();

                // 8) 退出前释放资源（避免在析构函数中调用）
                VmSolution.Instance?.Dispose();
            }
            catch (VmException vmex) { throw vmex; }
            catch (Exception ex) { throw ex; }
        }
    }
}
```

> ⚠️ **性能提示**：`DisableModulesCallback()` 会同时禁掉流程/Group/模块回调，可提高运行效率、降低 CPU 资源依赖。但**若要获取流程/Group/模块输出，必须单独启用对应对象的回调**。

---

## 4. 标准调用范式（模块级）

```csharp
using VM.Core;
using VM.PlatformSDKCS;
using ImageSourceModuleCs;
using IMVSFastFeatureMatchModuCs;

// 取模块对象
ImageSourceModuleTool imageModu = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
IMVSFastFeatureMatchModuTool fastMatchModu = (IMVSFastFeatureMatchModuTool)VmSolution.Instance["流程1.快速匹配1"];

// 1) 设参数：走 ModuParams（模块参数对象）
imageModu.ModuParams.ImageSourceType = ImageSourceTypeEnum.SDK;   // 图像源切到 SDK 模式

// 2) 设输入（两种通道）
imageModu.SetImagePath("D:\\test.jpg");                          // 方式一：文件路径
int nWidth = 64, nHeight = 64, nDataLen = nWidth * nHeight;
ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen,
                                             nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
imageModu.SetImageData(inputImage);                              // 方式二：内存图像

// 3) 执行
VmSolution.Instance.SyncRun();

// 4) 取结果：走 ModuResult（模块结果对象）
//    注意：每次执行后需【重新获取】结果对象以刷新其中数据；该操作有耗时，
//         建议拿到结果对象后直接用它取具体输出字段。
ImageSourceResult imageSourceResult = imageModu.ModuResult;
```

**模块对象三件套（所有算法模块统一）**

| 成员 | 类型 | 用途 |
|---|---|---|
| `ModuParams` | 模块对应 `XxxParam` | **读/写模块参数**、设置输入（图像/ROI/数据） |
| `ModuResult` | 模块对应 `XxxResult` | **读模块输出结果**（每次执行后重新获取） |
| `ModuResultMemType` | `ModuResultMemoryTypeEnum` | 模块结果内存管理类型 |
| `Run()` | `void` | 模块**自执行**一次（不影响其他模块） |
| `EnableResultCallback()` | `void` | 开启模块结果回调 |

> **`"仅当次执行起效"` 规则（高频坑）**：`SetImagePath` / `SetImageData` / `SetInputXxx` 这类**输入类接口**设置的数据**仅当次执行有效**，执行完成后被清空，**再次执行需再次设置**。
> - 配合**流程执行**：执行后清空（需重设）
> - 配合**模块自执行**（`Run()`）：不清空

---

## 5. 流程 / Group / 全局模块范式

### 5.1 流程（VmProcedure）

| 接口 | 说明 |
|---|---|
| `Run()` | 流程自执行一次 |
| `EnableResultCallback()` | 开启流程结果回调（取流程前需确保回调开启） |
| `Dispose()` | 删除流程 |
| `OnWorkBeginStatusCallBack` / `OnWorkEndStatusCallBack` | 流程开始/结束执行状态回调事件 |

### 5.2 Group（IMVSGroupTool）

```csharp
using IMVSGroupCs;

IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];

groupTool.DisableGroup();                       // 禁用 Group
groupTool.EnableGroup();                        // 启用 Group
groupTool.GetAllModuleList();                   // 取 Group 所有模块信息

GroupParam groupParam = groupTool.ModuParams;   // 参数对象
groupParam.SetInputImage_V2("ImageData", inputImage);   // 设输入（仅当次执行有效）
groupTool.Run();                                // Group 同步执行一次
GroupResult groupResult = groupTool.ModuResult;         // 结果对象（执行后重新获取）
ImageBaseData outputImage = groupResult.GetOutputImageV2("ImageData0");

groupTool.SaveAs("D:\\TestGro1.gro");
groupTool.DestroyGroup();

// 独立 Group（与方案并列，非线程安全）
IMVSGroupTool indep = IMVSGroupTool.LoadIndependentGroup("D:\\TestGro.gro");
```
Group 事件：`OnModuleIONameChanged`（IO 重命名）、`OnModuleDisplayParamNameChanged`（显示 IO 重命名）。

### 5.3 全局模块

| 全局模块 | Tool 类 | 典型用法 |
|---|---|---|
| 全局变量 | `GlobalVariableModuleTool` | `SetGlobalVar("var0","100")` / `GetGlobalVar("var0")` |
| 通信管理 | `CommManagerModuleTool` | `SetString(0,"abcd")` / `SetInt(1,int[],0)` / `GetReadData(1, ref byte[])` / `bIsDeviceConnect(1)` |
| 数据队列 | `DataQueueModuleTool` | `SetStringData(StringValue)` / `GetStringData(0)` / `GetIntData(1)` / `GetFloatData(2)` |
| 全局相机 | `GlobalCameraModuleTool` | `ModuParams.TriggerSource` / `GetCameraInfoList()` / `GetChosenCameraSN()` / `SetChosenCameraSN(sn)` |
| 全局光源 | `LightControlTool` | `SetGlobalLightParam(GlobalLightParam)`（含 `nDeviceIndex`、`nDeviceType`、`nTriggerTime`、`stLightConfig.stChannel1..4` 的使能/亮度/状态/触发边沿/时长） |

> 数据队列取数常需配合 `VmSolution.Instance.Run()` 逐次推进。

---

## 6. 控件体系

**两类框架，接口相似**：`VMControls.Winform.Release` / `VMControls.WPF.Release`（示例代码以 WinForm 为准）。

| 控件 | 类名 | 用途 | 绑定 |
|---|---|---|---|
| 流程配置控件 | `VmProcedureConfigControl` | 配置方案/流程 | `BindSingleProcedure("流程1")` / `BindMultiProcedure()` / `LockWorkArea()` / `UnlockWorkArea()` |
| 主界面控件 | `VmMainViewConfigControl` | 绑定 VM 主界面显示 | 同上 + `SetParamTabEditable(bool)` |
| 参数配置控件 | `VmParamsConfigControl` | 配置模块参数 | `ModuleSource = 对象` |
| 参数配置带渲染控件 | `VmParamsConfigWithRenderControl` | 参数配置 + 渲染/绘制 ROI | `ModuleSource = 流程 / Group / 模块` |
| 参数配置带渲染弹出控件 | `VmParamsWithRenderForm` | 同上，窗口式，**仅支持 Winform** | — |
| 综合配置控件 | `VmComprehensiveConfigWithRenderControl` | 绑定 **`VmSolution.Instance`** 显示综合配置界面 | `ModuleSource = VmSolution.Instance` |
| 渲染控件 | `VmRenderControl` | 绑定流程/模块渲染 | — |
| 全局工具控件 | `VmGlobalToolControl` | 显示全局配置工具 | — |
| 全局相机控件 | — | 显示全局相机模块实时取流图像 | — |
| 独立 Group 控件 | `VmSingleModuleSetConfigControl` | 显示/配置独立 Group | `ModuleSource = IMVSGroupTool.LoadIndependentGroup(...)` |
| 实时取流控件 | `VmRealTimeAcqControl` | 实时取流，**仅支持全局相机模块** | `ModuleSource = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"]`；`StartGrabbing()` / `StopGrabbing()` / `ShowButton(true)` |
| 前端运行界面控件 | `VmFrontendControl` | 显示方案运行界面信息 | — |

**渲染/参数控件通用能力（V4.4.0）**

```csharp
ctrl.ModuleSource = 对象;                 // 绑定对象（流程/Group/模块/方案）
ctrl.SetParamTabEditable(true|false);     // 参数配置页可编辑开关
ctrl.MultiImageButtonVisible = true;      // 单/双画面切换按钮
ctrl.ImageSource = imageBaseData;         // 绘制图像
ctrl.DrawShape(textEx);                   // 绘制图形
ctrl.AddShape(textEx);                    // 添加图形（仅当次执行有效）
ctrl.ClearDisplayView();                  // 清空显示
ctrl.SetBackground("D:\\background.bmp"); // 背景图（或 "#FF00FF" 背景色）
ctrl.SaveOriginalImage("D:\\save.bmp");   // 保存原始图（建议改用输出图像模块）
ctrl.SaveRenderedImage("D:\\save.bmp");   // 保存渲染图
ctrl.GetParamTabNames();                  // 取参数页 Tab 名称
ctrl.SetParamTabVisible(tabName, false);  // 隐藏/显示指定 Tab
ctrl.ChangeImageComboBoxVisibility(false);// 隐藏/显示图层选择控件
ctrl.SetRenderToolbarVisible(false);      // 隐藏/显示渲染工具栏
ctrl.GetDisplayableImageNameList();       // 可显示图像名列表
ctrl.SetSelectedImage(name);              // 设置显示图像
ctrl.AddStackImage(name);                 // 堆叠显示
ctrl.RemoveStackImage(name);
ctrl.SwitchBackgroundImage(name);
ctrl.SetParamConfigUIWidth(500);          // 参数配置页宽度
ctrl.Dispose();                           // 释放控件资源
```

> **控件绑定的执行语义**：点击带渲染控件的执行按钮时，**仅绑定的对象自执行一次**，其余模块无动作。自执行前须用流程执行/接口设置把该对象的**输入数据填充完毕**，否则会执行出错。
> **控件显示是异步刷新**，不能保证与执行前后严格时序配合。

---

## 7. 事件与回调机制

### 7.1 订阅方式

| 层级 | 订阅入口 | 典型事件 |
|---|---|---|
| **方案** | `VmSolution.OnXxxEvent += Handler` | `OnWorkStatusEvent`（流程工作状态）、`OnDongleEvent`（加密狗状态）、`OnSolutionLoadBeginEvent` / `OnSolutionLoadEndEvent` / `OnSolutionLoadProgressEvent`、`OnProcedureUnRegisterEvent`、`OnModelLoadWarnEvent`（模块加载错误警告）、`OnProcessStatusStartEvent` / `OnProcessStatusStopEvent`（连续执行起停）、`OnServerStatusEvent`、`OnProxyCrashEvent`、`OnModuleResultCallbackEvent`、`OnCommunicationRecvCallBackEvent`、`OnCommunicationStatusCallBackEvent`、`OnCameraCollectCallBackEvent` / `OnCameraCollectStartCallBackEvent`、`OnCommuConnectCallBackEvent`、`OnCameraConnectStatusCallBackEvent`、`OnGlobalCameraModuleAddedEvent` / `OnGlobalCameraModuleDeletedEvent` |
| **流程** | `vmProcedure.OnXxx += Handler` | `OnWorkBeginStatusCallBack`、`OnWorkEndStatusCallBack` |
| **Group** | `groupTool.OnXxx += Handler` | `OnModuleIONameChanged`、`OnModuleDisplayParamNameChanged` |
| **模块** | `vmModule.OnXxx += Handler` | `ModuleResultCallBackArrived`（模块结果回调） |

### 7.2 常用回调数据结构（`VM.PlatformSDKCS.ImvsSdkDefine`）

| 回调 | 结构体 | 可取字段 |
|---|---|---|
| `OnWorkStatusEvent` | `IMVS_MODULE_WORK_STAUS` | `nProcessID`（流程ID）、`nWorkStatus`（1 开始 / 0 结束）、`fProcessTime`（耗时，仅结束时有效） |
| `OnDongleEvent` | `IMVS_DONGLE_INFO` | `nDongleStatus`（0 正常，否则错误码）、`strDongleType` |
| `OnSolutionLoadEndEvent` | `IMVS_SOLUTION_LOAD_END_INFO` | `nStatus`（0 正常）、`strSolPath` |
| `OnSolutionLoadProgressEvent` | `IMVS_SOLUTION_LOAD_PROCESS_INFO` | `nProcess`（0~100） |
| `OnModelLoadWarnEvent` | `IMVS_LOAD_MODULE_ERROR_INFO_LIST` | `nModuleNum`、`astLoadModuErrInfo[]`（模块ID/名称等） |
| `OnModuleResultCallbackEvent` | `IMVS_MODULE_RESULT_INFO_LIST_EX_Data` | `nErrorCode`、`nModuleID`、`fModuleTime`、`fAlgorithmTime`、`nResultNum`、`pInfo[]`（`strParamName` 等） |
| `OnCommunicationRecvCallBackEvent` | `IMVS_COMMU_REPORT_DATA_INFO` | `nType`、`pData`(IntPtr)、`nLen` |
| `OnCameraConnectStatusCallBackEvent` | `IMVS_CAMERA_CONNECT_STATUS_INFO` | `nCameraID`、`nConnectStatus`、`strCameraSN` |

> 字节数组字符串统一这样解：`Encoding.UTF8.GetString(bytes).TrimEnd('\0')`
> `OnCommunicationStatusCallBackEvent` 使用较复杂，**建议改用 `OnCommuConnectCallBackEvent`**。

---

## 8. 异常与资源释放

```csharp
try { … }
catch (VmException vmex) { throw vmex; }   // VM 自定义异常，优先捕获
catch (Exception ex)     { throw ex; }
finally { VmSolution.Instance?.Dispose(); } // 退出程序前释放全部资源
```

- **必须**在程序退出前释放 VM 资源；**避免在析构函数中调用接口**。
- 控件各自 `Dispose()`。
- 4.3+ 提供独立的资源释放接口（见 `05-api/`）。

---

## 9. 依赖 DLL 清单（按开发方式）

| 开发方式 | 需要引用的 DLL |
|---|---|
| 纯调接口（无控件） | `VM.Core.dll`、`VM.PlatformSDKCS.dll` |
| WinForm 控件 | 上面 2 个 + `VMControls.Interface.dll`、`VMControls.BaseInterface.dll`、`VMControls.RenderInterface.dll`、`VMControls.Winform.Release.dll` |
| WPF 控件 | 上面 2 个 + `VMControls.Interface.dll`、`VMControls.BaseInterface.dll`、`VMControls.RenderInterface.dll`、`VMControls.WPF.Release.dll` |

**各库职责**

- `VM.Core.dll`：所有方案、流程的对外接口
- `VM.PlatformSDKCS.dll`：对外接口的底层实现，所有对外接口的基础库
- `VMControls.Interface.dll`、`VMControls.BaseInterface.dll`：控件对外接口基础库
- `VMControls.RenderInterface.dll`：带渲染功能控件的基础库（ROI、图形显示等）
- `VMControls.Winform.Release.dll` / `VMControls.WPF.Release.dll`：WinForm / WPF 控件对外接口

**添加引用**：推荐用自动工具 `..\Development\V4.x\ComControls\Tool\ImportRef.exe`；手动添加后需把库属性中**复制本地设为 False**。

---

## 10. 配置流程注意事项（WPF / WinForm 通用）

- 仅支持 **.NET Framework 4.6.1+**，**不支持 .NET Core**。
- 平台目标选 `Any CPU` 时，需**去掉"首选 32 位"勾选**。
- 手动添加 VM 动态库引用后，库属性**复制本地 = False**。
- 程序退出前调用接口释放资源，**避免在析构函数中调用**。
- 参数控件与参数渲染控件**暂不支持记忆**参数订阅框的默认显示方式。
- 独立 Group 控件**暂不支持执行和耗时显示**。
- 控件中英文切换：改 `..\Development\V4.x\ComControls\Assembly\LangCFG\LanguageSet.cfg`（zh-cn 中文 / en-us 英文）。
