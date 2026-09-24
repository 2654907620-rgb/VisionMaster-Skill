<!-- source: 03-ch2-sdk-dev-v40.md  pages 218-386 -->
# VM 二次开发 FAQ（第2章 · VM4.0）

> 本文件提炼自《VM 二次开发》PDF 分片（第 218–386 页，VM4.0）。
> 内容覆盖 5 大类共 53 个 FAQ 条目：环境配置类（2.1）、模块 API 类（2.2）、控件嵌入类（2.3）、结果获取类（2.4）、全局工具（2.5）。
> 代码块原则上逐字保留原文（仅修正 PDF 抽取造成的单词断行与多余空格，未改写逻辑）。

## 本章速览

1. 二次开发支持 C#/WinForm、Qt、MFC、VB.Net 四种语言/框架，环境核心都是「拷贝 `ComControls\bin\x64` 下的 DLL + 用 `ImportRef.exe` 导入引用」。
2. VM4.0 引用采用**相对路径**方式；从安装目录手动加引用后必须把「复制本地」改为 `False`，否则 DLL 冲突导致控件失效。
3. `.NET Framework` 工程框架固定 **4.6.1**，且必须**取消勾选「首选 32 位」**。
4. 一个项目 `ImportRef.exe` **只使用一次**；报 `mfc120u.dll` 缺失时运行 `MSVBCRT.AIO_v2020.05.20.exe`。
5. `Vm.Core.Solution` 报错排查顺序：加密狗/管理员权限/首选32位 → 版本与补丁 → 关闭 VM 双开进程 → `EnvironmentDetectionTool.exe`。
6. 图像输入通用套路：`OpenCvSharp` 读图 → 填充 `InputImageData`（默认名 `InImage`）→ `ModuParams.SetInputImage(...)`。
7. ROI/几何形状用二进制数据 `SetBinaryData("RoiType", ptr, size)` / `SetBinaryData("GeometryType", ...)`，坐标按图像宽高**归一化**。
8. 渲染控件推荐**绑定流程**（`ModuleSource = VmProcedure`），符合高内聚低耦合，可一个控件显示多模块。
9. 结果获取推荐走**流程输出**（`GetIntOutputResult` / `GetFloatOutputResult` / `GetStringOutputResult` / `GetImageOutputResult`）。
10. 所有结果/状态建议写进**回调函数**：`OnWorkStatusEvent`（流程结束）、`OnModuleResultCallbackEvent`（模块结束）、`OnSolutionLoadEndEvent`（方案加载）、`OnDongleCallBack`（加密狗）、`OnCommunicationRecvCallBackEvent`（通讯）。
11. 图像输出名称固定为 `Imageout0 / ImageWidthout0 / ImageHeightout0 / ImagePixelFormatout0`；像素格式 `17301505`=MONO8，`35127316`=RGB24。
12. 资源释放用 `VmSolution.Instance.Dispose()`（窗体 `FormClosing`）。
13. 控件不显示/不刷新：检查 bin\x64 是否最新 + `vmRenderControl1.UpdateVMResultShow()`。
14. 嵌入整个 VM 软件用 `SetParent`+`MoveWindow` 将 `VisionMaster.exe` 主窗口挂到 Panel。
15. 隐藏参数改模块 xml 的 `<CustomVisible>False</CustomVisible>`；改控件颜色用 `AppColorService.CurColorDefine`。
16. `CreateSolutionInstance()` 必须在 `VmMainView`/`GetObjectPointer()` 之前调用一次，否则流程不显示。
17. 全局相机/通信部分接口在 VM4.0 尚未对外开放，VM4.2 才开放（见 2.5.2/2.5.3）。
18. 渲染控件存图要在 `button` 事件里做，回调/Run 后立即存会得到未渲染完成的图。
19. 流程/模块耗时：`ProcessTime` / `ModuleTime` / `AlgorithmTime`；运行间隔 `SetRunInterval` / `SetContinousRunInterval`。
20. 普通用户权限要以 EXE 方式启动 Server：在 `xxx.exe.config` 的 `AppSettings` 增加 `ServerPath` 等配置。

---

## 2.1 环境配置类

### 2.1.1 环境配置：CSharp 二次开发环境配置方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：C#（以 WinForm 为例）二次开发环境的配置方法。

**原因 / 原理**
- 不熟悉 C# 二次开发环境配置。VM 二次开发依赖一组托管 DLL 与 ActiveX/控件 DLL，需要把 `ComControls\bin\x64` 整体放进调试目录，并通过导入工具把模块 DLL 以相对路径加入引用。

**解决步骤**
1. 新建 `.NET Framework 4.6.1` 工程，**取消勾选「首选 32 位」**，重新生成解决方案，保证 Debug 下存在 exe，然后关闭工程。
2. 将 VM 安装目录下 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64` 整体拷贝到新建工程的 `Debug` 下。
3. 启动二次开发导入工具 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\Tool\ImportRef.exe`：
   - `Module(sp)` 路径 = 生成工程 `Debug` 下的 `Module(sp)` 文件夹；
   - 项目所在路径 = `bin` 文件的上一层；
   - 选择需要引用的模块 DLL，选择是否相对路径，点击确定。
4. 首次配置时工具箱里没有 VM 控件，需手动添加：
   - 右击所有窗体 → 「选择项」；
   - 浏览当前项目 `debug` 路径，**WinForm** 选 `VMControls.Winform.Release.dll`，**WPF** 选 `VMControls.WPF.Release.dll`。

**关键代码**
```csharp
// （本条为配置步骤，原文无代码；关键操作是拷贝 bin\x64 与运行 ImportRef.exe）
```

**关键 API / 类名 / 命名空间 / 属性**
- 目录：`\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64`
- 工具：`ImportRef.exe`（路径 `…\ComControls\Tool\ImportRef.exe`）
- DLL：`VMControls.Winform.Release.dll`、`VMControls.WPF.Release.dll`
- 框架：`.NET Framework 4.6.1`，取消「首选 32 位」

**注意事项 / 坑**
- `ImportRef.exe` 对一个项目**只使用一次**。
- 引用务必使用相对路径，避免从安装目录直接引用导致后续部署问题。

---

### 2.1.2 环境配置：Qt 二次开发环境配置方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2019 + Qt5.12.3。
- 现象：Qt + VS 二次开发环境如何配置。

**原因 / 原理**
- 不熟悉 Qt 二次开发环境配置。Qt 通过 `QAxWidget` 包装 VM 已注册的 ActiveX 控件。

**解决步骤**
1. 新建 Qt 工程，添加 Qt 模块：`Core`、`GUI`、`Active Qt`、`Container Widgets`。
2. 拷贝 DLL：将 `VM\VisionMaster4.0.0\Development\V4.0.0\ComControl\bin\x64` 下的所有文件拷贝到项目工程输出目录（示例输出路径为 `Dll` 文件夹）。
3. 方法一（拷贝 include/lib 到工程）：
   - 3.1 拷贝 `\VisionMaster4.0.0\Development\V4.0.0\includes` 头文件。
   - 3.2 拷贝 `\VisionMaster4.0.0\Development\V4.0.0\ComControl\includes\QT` 头文件。
   - 3.3 拷贝 `\VisionMaster4.0.0\Development\V4.0.0\libraries\win64\C` 下所有库文件。
4. 方法二（配置 VC++ 目录和链接器）：
   - 4.1 包含目录添加：`\VisionMaster4.0.0\Development\V4.0.0\includes` 与 `\VisionMaster4.0.0\Development\V4.0.0\ComControl\includes\QT`。
   - 4.2 库目录添加：`\VisionMaster4.0.0\Development\V4.0.0\libraries\win64\C`。
   - 4.3 链接器附加依赖项写入：`iMVS-6000PlatformSDK.lib`。
5. 配置完成：`#include` 能索引到 VM 模块 `.h` 文件。
6. 第一个 VM 界面：
   - 6.1 添加容器控件 `QAxWidget`（包装 ActiveX 控件，VM 控件安装时已注册到 Windows 组件）。
   - 6.2 创建方案句柄并初始化控件。

**关键代码**
```cpp
CreateSolutionInstance();
ui.axWidget->dynamicCall("GetObjectPointer()");
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件容器：`QAxWidget`（Qt ActiveX 包装）
- 库：`iMVS-6000PlatformSDK.lib`
- 目录：`includes`、`ComControl\includes\QT`、`libraries\win64\C`
- 接口：`CreateSolutionInstance()`、`dynamicCall("GetObjectPointer()")`

**注意事项 / 坑**
- Qt 工程中 `QAxWidget` 绑定 VM 控件前需先创建方案句柄。

---

### 2.1.3 环境配置：MFC 二次开发环境配置方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：MFC 二次开发环境如何配置。

**原因 / 原理**
- 不熟悉 MFC 二次开发环境配置。MFC 通过 `DDX_Control` 绑定 ActiveX 控件变量，控件在安装时已注册。

**解决步骤**
1. 新建 MFC 工程，拷贝 DLL：`VM\VisionMaster4.0.0\Development\V4.0.0\ComControl\bin\x64` 全部到工程输出目录。
2. 配置 C++ 目录和链接器：
   - 2.1 附加包含目录：`.\Includes`。
   - 2.2 库目录：`.\Libraries\win64\C`。
   - 2.3 链接器输入附加依赖项：`iMVS-6000PlatformSDK.lib`。
3. 添加控件源文件：复制 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\Includes\VS2017`（按 VS 版本选）下的控件源文件到工程目录并引入。
4. 配置完成：`#include` 能索引到模块 `.h` 文件。
5. 第一个 VM 界面：
   - 5.1 添加 ActiveX 控件（VM 控件安装时已注册，可直接选）。
   - 5.2 控件绑定与初始化。

**关键代码**
```cpp
protected:
    CVmProcedureControlInterface m_ctrlProcedure;

void CVMMFCApplication1Dlg::DoDataExchange(CDataExchange* pDX)
{
    CDialogEx::DoDataExchange(pDX);
    DDX_Control(pDX, IDC_VMUSERCONTROL1, m_ctrlProcedure);
}

BOOL CVMMFCApplication1Dlg::OnInitDialog()
{
    CDialogEx::OnInitDialog();
    // 将“关于...”菜单项添加到系统菜单中。
    … 
    // TODO: 在此添加额外的初始化代码
    try
    {
        m_ctrlProcedure.GetObjectPointer();
    }
    catch (CVmException e)
    {}
    return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件类：`CVmProcedureControlInterface`
- 宏：`DDX_Control`、`CDialogEx::DoDataExchange`、`OnInitDialog`
- 库：`iMVS-6000PlatformSDK.lib`
- 接口：`GetObjectPointer()`、`CVmException`

**注意事项 / 坑**
- 控件源文件目录按 VS 版本选择（`VS2017` 等）。

---

### 2.1.4 环境配置：VB.Net 二次开发环境配置方法

**问题现象 / 适用场景**
- 环境：VM4.0 + VS2015 及以上。
- 现象：使用 Visual Basic 语言进行 VM 二次开发的环境搭建。

**原因 / 原理**
- 二次开发环境配置功能不熟悉。VB.Net 与 C# 类似，但需手动引用并配置 `APP.Config` 的 `privatePath`。

**解决步骤**
1. 第一步：新建 `.NET Framework 4.6.1` 工程，**去勾选「首选 32 位」**，重新生成，保证 Debug 下存在 exe，关闭工程。
2. 第二步：将 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64` 整体复制到新建工程 `Debug` 下。
3. 第三步：添加工程引用，手动引用基本库和相关模块工具的 DLL。
4. 第四步：修改 `APP.Config`，在 `privatePath` 上指明 DLL 位置（添加相应配置代码），完成整体环境配置。

**关键代码**
```vb
' （本条原文无独立代码；核心是在 APP.Config 的 privatePath 指明 VM DLL 所在相对路径）
```

**关键 API / 类名 / 命名空间 / 属性**
- 框架：`.NET Framework 4.6.1`
- 配置：`APP.Config` 的 `privatePath`
- DLL：`ComControls\bin\x64` 下基本库与模块工具 DLL

**注意事项 / 坑**
- 引用需手动添加，且 `privatePath` 必须与实际 DLL 相对路径一致。

---

### 2.1.5 环境配置：运行出现 Vm.Core.Solution 报错的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：VM4.0.0 环境配置运行出现 `Vm.Core.Solution` 报错。

**原因 / 原理**
- 不熟悉如何排查报错原因。常见根因：加密狗/权限/首选32位、版本过旧、VM 双开、依赖库未替换完整。

**解决步骤**
1. 检查：加密狗是否插好？是否以管理员权限启动程序？「首选 32 位」是否取消勾选？
2. 查看 VM4.0 版本是否为最新（版本信息 20220415 以上；截至 20220505 最新补丁为 20220505）。若打过最新补丁，需把补丁后 `VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64` 下**所有文件**替换到二次开发项目 EXE 生成路径（Debug）下。
3. 关闭所有 VM 相关程序（防止 VM 双开），可用以下代码代替手动关闭。
4. 检查 VM 安装环境是否正常：运行 `VisionMaster4.0.0\Applications\Tools` 下的 `EnvironmentDetectionTool.exe`。
5. 若打开过多个版本的 VM，重启电脑或打开相应版本的 VM 来拉起相应版本的服务。
6. 是否严格按环境步骤配置？`ImportRef` 工具针对一个项目只使用一次。

**关键代码**
```csharp
KillProcess("VisionMasterServerApp");
KillProcess("VisionMaster");
void KillProcess(string strKillName)
{
    foreach(System.Diagnostics.Process p in System.Diagnostics.Process.GetProcesses())
    {
        if (p.ProcessName == strKillName)
        {
            try
            {
                p.Kill();
                p.WaitForExit();
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message.ToString());
            }
        }
    }           
}
```
补充：
- VM 启动时拉起 4 个进程：`VisionMaster.exe`、`VisionMasterServer.exe`、`VisionMasterServerAPP.exe`、`VmModuleProxy.exe`；
- VM SDK 程序启动时拉起 2 个进程：`VisionMasterServer.exe`、`VmModuleProxy.exe`；
- 因此只需结束 `VisionMaster.exe` 和 `VisionMasterServerAPP.exe` 进程即可。

**关键 API / 类名 / 命名空间 / 属性**
- 进程：`VisionMaster.exe`、`VisionMasterServer.exe`、`VisionMasterServerAPP.exe`、`VmModuleProxy.exe`
- 工具：`EnvironmentDetectionTool.exe`
- 版本节点：20220415、补丁 20220505
- 命名空间：`System.Diagnostics.Process`

**注意事项 / 坑**
- 打补丁后务必整体替换 `bin\x64`，否则版本不一致会报 `Vm.Core.Solution`。

---

### 2.1.6 模块索引：MFC 模块索引异常解决办法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：文件编码格式为 UTF-8 不带签名编码格式时，模块索引会出现「模块无法找到」异常。

**原因 / 原理**
- 不熟悉引用库环境配置。MFC 源码文件若用 UTF-8 无 BOM 编码，编译器/索引解析异常。

**解决步骤**
1. 将文件类型更改为 **UTF-8 带签名**（BOM）格式，或改为 VS 默认的 **GBK/GB2312** 编码格式。

**关键代码**
```csharp
// （本条原文无代码；仅修改文件编码格式）
```

**关键 API / 类名 / 命名空间 / 属性**
- 编码：UTF-8 带签名 / GB2312（GBK）

**注意事项 / 坑**
- 源文件编码建议统一为带签名 UTF-8 或 GB2312。

---

### 2.1.7 环境配置：报错序列不包含任何元素的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：配置环境后，获取线线测量模块结果，报错「序列不包含任何元素」。

**原因 / 原理**
- 相关依赖库未拷贝完整。`ComControls\bin\x64` 缺失部分依赖导致结果集合为空。

**解决步骤**
1. 将 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64` 下整体**重新拷贝**到项目 Debug 目录。

**关键代码**
```csharp
// （本条原文无代码；操作为重新拷贝 bin\x64 目录）
```

**关键 API / 类名 / 命名空间 / 属性**
- 目录：`\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64`

**注意事项 / 坑**
- 「序列不包含任何元素」多为依赖 DLL 缺失或版本不匹配。

---

### 2.1.8 环境配置：提示未注册 ActiveX 控件的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 问题：MFC 插入 VM 的控件时，报错「未注册 ActiveX 控件」。

**原因 / 原理**
- 不了解如何注册 VM 控件。VM 控件以 ActiveX 形式注册到系统，需以管理员身份运行注册批处理。

**解决步骤**
1. 关闭 VS 后重新注册 VM 控件：
   - 1）解注册：找到 `win64` 路径，右键以管理员权限运行 `ComUnRegister.bat`。
   - 2）注册：找到 `win64` 路径，右键以管理员权限运行 `ComRegister.bat`。
   - 3）对 `win32` 文件夹下的两个文件重复上述操作。

**关键代码**
```csharp
// （本条原文无代码；操作为运行 ComRegister.bat / ComUnRegister.bat）
```

**关键 API / 类名 / 命名空间 / 属性**
- 批处理：`ComRegister.bat`、`ComUnRegister.bat`
- 路径：`win64`、`win32`

**注意事项 / 坑**
- 必须以**管理员权限**运行批处理，且先关 VS。

---

### 2.1.9 控件失效：VM 控件运行时不显示的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：编译成功、无报错，但运行后 VM 控件是黑色的，不显示任何内容。

**原因 / 原理**
- 环境配置错误（原文根因描述为「不熟悉全局变量工具及其接口」，此处按原文保留）。本地 VM 不是最新版本或 bin\x64 文件未同步。

**解决步骤**
1. 确认本地 VM 是否为最新版本，然后将本地 VM 路径（如 `D:\VM4.0\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64`）下的**所有文件**复制到项目路径的 `Debug` 文件夹下。

**关键代码**
```csharp
// （本条原文无代码；操作为复制 bin\x64 到 Debug）
```

**关键 API / 类名 / 命名空间 / 属性**
- 目录：`\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64`

**注意事项 / 坑**
- 控件黑屏通常是 bin\x64 与 VM 版本不一致所致。

---

### 2.1.10 环境配置：Qt 开发环境出现 rc.exe 无法启动报错解决办法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 + Qt5.9.9。
- 现象：编译出现 `rc.exe` 无法启动。

**原因 / 原理**
- 系统问题。Windows SDK 的 `rc.exe` / `rcdll.dll` 不在 VS bin 路径下。

**解决步骤**
1. 找到 Windows SDK 的 `x86` 目录下的 `rc.exe` 以及 `rcdll.dll` 文件。
2. 复制到 VS 的 `bin` 目录下。

**关键代码**
```csharp
// （本条原文无代码；操作为拷贝 rc.exe / rcdll.dll）
```

**关键 API / 类名 / 命名空间 / 属性**
- 文件：`rc.exe`、`rcdll.dll`（Windows SDK x86 目录）

**注意事项 / 坑**
- 属于系统/SDK 环境缺失，与 VM 本身无关。

---

### 2.1.11 控件失效：添加引用后导致控件失效的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：有些引用需手动添加（如引用 `VMControls.WPF.dll` 在渲染控件上绘图）。添加之后运行项目，界面上的 VM 控件区失效（`vmProcedureConfigControl`、`vmRenderControl`、`vmGlobalToolControl`）。

**原因 / 原理**
- 不熟悉 VM 二次开发中的引用。VM 的引用采用相对路径方式；若从安装路径添加引用，会导致调试目录下的控件 DLL 被覆盖/冲突。

**解决步骤**
1. 因为 VM 的引用都是采用相对路径方式，如果此时是从 VM 的安装路径中添加引用，则需要打开当前引用 DLL 的属性，将「复制本地」改为 **False**。

**关键代码**
```csharp
// （本条原文无代码；操作为将手动添加引用的「复制本地」改为 False）
```

**关键 API / 类名 / 命名空间 / 属性**
- DLL：`VMControls.WPF.dll`
- 控件：`vmProcedureConfigControl`、`vmRenderControl`、`vmGlobalToolControl`
- 属性：「复制本地 = False」

**注意事项 / 坑**
- 从安装目录手动加引用后务必改「复制本地 = False」，否则控件失效。

---

### 2.1.12 添加引用：在原有项目中新配置深度学习环境的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：VM 没装深度学习模块时搭建了二次开发项目，后来项目中需要应用深度学习，如何在原有项目中配置深度学习模块的 DLL。

**原因 / 原理**
- 不熟悉环境配置。深度学习 DLL 需单独拷贝并手动引用，且「复制本地」必须改 False。

**解决步骤**
1. VM 中安装好深度学习模块后，将本地 VM 路径下 `\VM4.0\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64` 的 DLL 全部拷贝到项目的 `debug` 下。
2. 手动添加引用项目 `debug` 下 `Module(sp)\x64\DeepLearning` 相应文件里的 DLL（`C` 代表 CPU）。
3. 手动添加后，引用的属性**立刻修改**（复制本地路径为 false）；为 true 时 debug 会有刚复制过来的 DLL，debug\Module(sp)\x64 下也有，代码会找不到；若 debug 下已经有了就删除掉。
4. 修改 `app.config`，在 `<probing privatePath=>` 后面添加深度学习相对路径：`Module(sp)\x64\DeepLearning\ IMVSCnnClassifyModuC`。
5. 其他模块手动添加步骤类似，但因步骤复杂且模块外 DLL 很难加全，**推荐使用引用工具** `ImportRef.exe`，且一个项目只使用一次。

**关键代码**
```csharp
// （本条原文无代码；操作为拷贝 DLL + 改“复制本地”=False + 修改 app.config 的 probing privatePath）
```

**关键 API / 类名 / 命名空间 / 属性**
- 目录：`Module(sp)\x64\DeepLearning`（C = CPU）
- 工具：`ImportRef.exe`（路径 `…\ComControls\Tool\ImportRef.exe`）
- 配置：`app.config` 的 `<probing privatePath=>`
- DLL：`IMVSCnnClassifyModuC`

**注意事项 / 坑**
- 手动引用后「复制本地」必须为 False，否则 DLL 冲突。
- 优先用 `ImportRef.exe` 添加深度学习等复杂模块引用。

---

### 2.1.13 用户权限：普通用户权限以 EXE 方式启动 Server 的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：客户二次开发程序需要以 Windows 普通用户权限调用 Vm 做视觉处理，需将 Server 以 EXE 方式启动。

**原因 / 原理**
- 不熟悉普通用户权限二次开发的配置。需通过 exe.config 指定 Server 路径，让程序以普通权限拉起 Server。

**解决步骤**
1. 安装 VM20220415 安装包 + 补丁（截至 20220505 最新补丁为 20220505）；若 VM4.0 维护版 2022 年 5 月之后有完整包，直接安装即可，不用装补丁包。
2. 修改二次开发程序的 `xxx.exe.config` 配置文件，在 `AppSettings` 里增加以下两条信息（`ServerPath` 为该电脑上 Server 的绝对路径，需填正确）。

**关键代码**
```xml
<!-- 在 xxx.exe.config 的 <AppSettings> 中增加（原文为图示，文字缺失具体键值）
     至少需包含 ServerPath（Server 的绝对路径）等两项配置 -->
```

**关键 API / 类名 / 命名空间 / 属性**
- 配置：`xxx.exe.config` → `AppSettings` → `ServerPath`
- 版本：VM20220415 / 补丁 20220505

**注意事项 / 坑**
- `ServerPath` 必须是本机 Server 的真实绝对路径。

---

### 2.1.14 引用工具：使用引用工具添加引用报错的解决方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：`ImportRef` 可以帮助用户为项目自动添加引用，但有时会报错缺少 `mfc120u.dll`。

**原因 / 原理**
- 不熟悉 VM 自带的驱动。系统缺失 VC++ 运行库。

**解决步骤**
1. 直接运行 VM 安装路径下的驱动 `MSVBCRT.AIO_v2020.05.20.exe` 解决。

**关键代码**
```csharp
// （本条原文无代码；操作为运行 MSVBCRT.AIO_v2020.05.20.exe）
```

**关键 API / 类名 / 命名空间 / 属性**
- 驱动：`MSVBCRT.AIO_v2020.05.20.exe`
- 缺失文件：`mfc120u.dll`

**注意事项 / 坑**
- 报 `mfc120u.dll` 缺失即运行 VM 自带 VC++ 运行库合集驱动。

---

### 2.1.15 环境配置：句柄创建失败解决问题排查方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：VM 二次开发执行 `CreateSolutionInstance()` 出现句柄错误问题。

**原因 / 原理**
- 不熟悉 VM 二次开发流程。句柄创建失败通常为 VM 已占用、无管理员权限、无加密狗驱动。

**解决步骤**
1. VM 平台软件如果开启，需要关闭退出。
2. VS 未开启管理员权限（需以管理员身份运行）。
3. 加密狗未插上，或未安装驱动。

**关键代码**
```csharp
// （本条原文无代码；排查项如上）
```

**关键 API / 类名 / 命名空间 / 属性**
- 接口：`CreateSolutionInstance()`

**注意事项 / 坑**
- `CreateSolutionInstance()` 前必须保证 VM 主程序未运行、有管理员权限、加密狗就绪。

---

## 2.2 模块 API 类

### 2.2.1 方案保存：方案高速保存的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：二次开发软件调用 `VmSolution.Export(string Path)` 接口保存方案，保存时间较长。

**原因 / 原理**
- 不熟悉方案的相关接口。`Export` 默认会显示进度对话框并阻塞，导致耗时明显。

**解决步骤**
1. 将 `Export` 接口的 `bDisplayProgress` 参数置为 `false`，或将保存操作放在线程里调用。

**关键代码**
```csharp
VmSolution.Export(tb_SolPath.Text, "", false);
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmSolution`
- 方法：`Export(string Path, string, bool bDisplayProgress)`

**注意事项 / 坑**
- 第三个参数 `false` 表示不显示进度，可显著加快保存。

---

### 2.2.2 Group 模块：Group 输入输出图像数据的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：Group 模块可以设置输入和输出，如何进行图像数据的输入和输出。

**原因 / 原理**
- 不熟悉针对 Group 模块如何输入输出图像数据。Group 相当于一个模块，可独立加载 `.gro` 或流程内实例化，通过接口设置/获取图像。

**解决步骤**
1. 设置图像数据的输入（以独立 Group 为例，导入后缀为 `.gro` 的独立 Group）：
   - 用 OpenCV 读图，构造 `InputImageData`，调用 `group.ModuParams.SetInputImage(StImg)`；
   - 绑定渲染源：`vmRenderControl1.ModuleSource = group`；
   - 也可将流程中的 Group 实例化，再用流程的 `SetInputImage` 接口。
2. 获取输出的图像数据：
   - 参考 2.4.1，给 Group 中添加一个「输出图像模块」获取输出图像 `byte`；
   - 或配置 Group 的显示设置，订阅输出图像模块，再按 2.4.1 方法取流程图像数据，`Imageout` 才是真正的图像名称；像素格式 `17301505` 为 MONO8 灰度图，`35127316` 为 RGB24 彩色图。

**关键代码**
```csharp
IMVSGroupTool group=null;
//加载group模块
group = IMVSGroupTool.LoadGroup(@"C:\Users\zhouyigen\Desktop\LackImage.gro", "");
//利用OpenCV的读图方法，读取图像
Mat matImage = Cv2.ImRead(@"C:\Users\zhouyigen\Desktop\Demo(2)\smile.png",ImreadModes.Grayscale);
//实例化VM接口可接收的图像类型
InputImageData StImg = new InputImageData();
//设置图像参数
StImg.Names.DataName = "Imagein";
StImg.Names.HeightName = "ImageHeightin";
StImg.Names.WidthName = "ImageWidthin";
StImg.Names.PixelFormatName = "ImagePixelFormatin";
StImg.Height = matImage.Rows;
StImg.Width = matImage.Cols;
StImg.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;
StImg.DataLen = (uint)(matImage.Width * matImage.Height);
StImg.Data = new byte[matImage.Width * matImage.Height];

//将读取到的图像拷贝给StImg
Marshal.Copy(matImage.Data, StImg.Data, 0, matImage.Width * matImage.Height);
// 设置图像数据
group.ModuParams.SetInputImage(StImg);

//绑定渲染源
vmRenderControl1.ModuleSource = group;
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`IMVSGroupTool`
- 方法：`LoadGroup`、`ModuParams.SetInputImage`
- 结构：`InputImageData`、`InputImageData.Names`（DataName/HeightName/WidthName/PixelFormatName）
- 枚举：`ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8`
- 控件：`vmRenderControl1.ModuleSource`
- DLL：`OpenCvSharp.dll`（位于 `ComControls\bin\x64`）

**注意事项 / 坑**
- Group 内若无图像源模块，需提前建立图像输入联系。
- 输出图像名用 `Imageout`（非 `ImageData`）。

---

### 2.2.3 模块操作类：设置输入图像、参数和 ROI 的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：每个模块类型命名不同，但拥有部分共同的相关操作（输入图像、参数、ROI）。

**原因 / 原理**
- 不熟悉如何对模块进行一些操作。输入图像统一用 `InputImageData` + `SetInputImage`；参数用 `ModuParams` 属性；ROI/屏蔽区用二进制数据 `SetBinaryData("RoiType"/"ExternRoiType", ptr, size)`。

**解决步骤**
1. 给模块设置输入图像（以圆查找为例）。注意：
   - **基本参数**（输入参数）：参数配置窗口**不显示**所设参数，模块运行参数永久有效，流程运行一次有效；
   - **运行参数**：窗口**会显示**所设参数，模块和流程运行都永久有效。
2. 配置参数：实例化模块为 `tool`，设置 `tool.ModuParams` 的属性（以圆查找 `RadNum` 卡尺数量为例）。
3. 设置 ROI（以 DL 字符识别 CPU 模块为例，坐标按图像归一化，0.5f 表示居中比例）。
4. C++ 中获取 ROI / 设置 ROI / 设置多个 ROI / 设置屏蔽区 / 设置多个屏蔽区（见代码）。

**关键代码**
```csharp
//VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64 中包含OpenCvSharp.dll

Mat matImage = Cv2.ImRead(path, ImreadModes.Grayscale);//使用opencv读图，也可以使用BitMap读图
InputImageData StImg = new InputImageData();
StImg.Names.DataName = "InImage";//只能使用默认名称InImage
StImg.Names.HeightName = "InImageHeight";//默认InImageHeight
StImg.Names.WidthName = "InImageWidth";//默认InImageWidth
StImg.Names.PixelFormatName = "InImagePixelFormat";//默认InImagePixelFormat
StImg.Height = matImage.Rows;
StImg.Width = matImage.Cols;
StImg.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;
StImg.DataLen = (uint)(matImage.Width * matImage.Height);
StImg.DataLen = (uint)(matImage.Width * matImage.Height);
Marshal.Copy(matImage.Data,StImg.Data,0,matImage.Width*matImage.Height);
IMVSCircleFindModuTool Circle = (IMVSCircleFindModuTool)process["圆查找1"];
Circle.ModuParams.SetInputImage(StImg);
```
```csharp
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
tool.ModuParams.RadNum=10；// 卡尺数量
```
```csharp
public void OCRROISetFunc(ref VMControls.WPF.Release.VmRenderControl vmRenderControl1)
{
    /////////OCRROISET
    MVSOcrDlModuCTool iMVSOcrDlModuCTool = (IMVSOcrDlModuCTool)VmSolution.Instance["流程1.DL 字符识别C1"];

    RoiBox roiBox = new RoiBox();
    roiBox.bRoiType = (byte)RoiType.ROI_TYPE_BOX;
    roiBox.fCenterX = 0.5f;
    roiBox.fCenterY = 0.68f;
    roiBox.fWidth = 0.5f;
    roiBox.fHeight = 0.1f;

    IntPtr ptr = Marshal.AllocHGlobal(Marshal.SizeOf(roiBox));
    Marshal.StructureToPtr(roiBox, ptr, false);
    iMVSOcrDlModuCTool.ModuParams.SetBinaryData("RoiType", ptr, (uint)Marshal.SizeOf(roiBox));
    vmRenderControl1.ModuleSource = iMVSOcrDlModuCTool;
}
```
```cpp
// 1）拿到指向圆查找模块的指针
IMVSCircleFindModuTool *CircleFindModu=static_cast<IMVSCircleFindModuTool*>((*m_pVmSol)["流程1.圆查找1"]);
ROI_BOX roiBox = { 0 };
unsigned int nLen=0;
//获取ROI
CircleFindModu->GetParamObj()->GetBinaryData("RoiType",&roiBox,sizeof(roiBox), nLen);

// 2）圆卡尺类型ROI
ROI_CIRCLECALIPER RoiCircle = { 0 ,0,0 ,0 ,0 ,0,0,0,0,0};
unsigned int nLen ;
RoiCircle.bRoiType = ROI_TYPE_CIRCLECALIPER;
RoiCircle.bVersion = 0;
RoiCircle.fCenterX = 0.635;//圆心X/图像宽
RoiCircle.fCenterY = 0.59;//圆心Y/图像高
RoiCircle.fOutterRadius = 0.035;//半径/图像宽
RoiCircle.fStartAngle = 0;
RoiCircle.fEndAngle = 0;
RoiCircle.fWidth = 0.0408;//卡尺高/图像宽
RoiCircle.fHeight = 0.0132;//卡尺宽/图像高
RoiCircle.nNum = 60;//卡尺数
//设置ROI
CircleFindModu->GetParamObj()->SetBinaryData("RoiType",&RoiCircle,sizeof(RoiCircle));

// 3）获取指向BLOB分析模块的指针
IMVSBlobFindModuTool *blobFindMou=static_cast<IMVSBlobFindModuTool*>((*m_pVmSol)["流程1.BLOB 分析1"]);
//设置ROI数据
ROI_BOX roiBox[2] = { 0 };
roiBox[0].bRoiType = ROI_TYPE_BOX;
roiBox[0].bVersion = 0;
roiBox[0].fAngle = 0;
roiBox[0].fCenterX = 0.2;
roiBox[0].fCenterY = 0.3;
roiBox[0].fHeight = 0.1;
roiBox[0].fWidth = 0.15;
roiBox[1].bRoiType = ROI_TYPE_BOX;
roiBox[1].bVersion = 0;
roiBox[1].fAngle = 0;
roiBox[1].fCenterX = 0.4;
roiBox[1].fCenterY = 0.6;
roiBox[1].fHeight = 0.2;
roiBox[1].fWidth = 0.3;
//拷贝整合
char *temp = new char[sizeof(ROI_BOX) * 2]{0};
memcpy(temp, &roiBox[0], sizeof(ROI_BOX));
memcpy(temp + sizeof(ROI_BOX), &roiBox[1], sizeof(ROI_BOX));
//设置多个ROI
blobFindMou->GetParamObj()->SetBinaryData("RoiType",temp,sizeof(ROI_BOX) * 2);

// 4）设置屏蔽区
ROI_POLYGON polygon = { 0 };
polygon.bRoiType = ROI_TYPE_POLYGON;
polygon.bVersion = 0;
polygon.nVertexNum = 4;
//设置屏蔽区的4个点
polygon.stVertexPoints[0] = { 0.3,0.125 };
polygon.stVertexPoints[1] = { 0.575,0.087 };
polygon.stVertexPoints[2] = { 0.712,0.799 };
polygon.stVertexPoints[3] = { 0.31,0.8 };
//设置屏蔽区
blobFindMou->GetParamObj()->SetBinaryData("ExternRoiType",&polygon,38);

// 5）设置多个屏蔽区
polygon[1].bRoiType = ROI_TYPE_POLYGON;
polygon[1].bVersion = 0;
polygon[1].nVertexNum = 4;
polygon[1].stVertexPoints[0] = { 0.6f,0.125f };
polygon[1].stVertexPoints[1] = { 0.8f,0.087f };
polygon[1].stVertexPoints[2] = { 0.4f,0.799f };
polygon[1].stVertexPoints[3] = { 0.3f,0.8f };
char* temp=new char[76];
memcpy(temp,&polygon[0],38);
memcpy(temp+38,&polygon[1],38);
//设置多个屏蔽区
blobFindMou->GetParamObj()->SetBinaryData("ExternRoiType",temp,76);
// 其中38根据结构体内容计算字节数 1+1+4+（4+4）*2
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`IMVSCircleFindModuTool`、`MVSOcrDlModuCTool`、`IMVSBlobFindModuTool`
- 结构：`InputImageData`、`RoiBox`、`ROI_BOX`、`ROI_CIRCLECALIPER`、`ROI_POLYGON`
- 枚举：`RoiType.ROI_TYPE_BOX`、`ROI_TYPE_CIRCLECALIPER`、`ROI_TYPE_POLYGON`
- 方法：`ModuParams.SetInputImage`、`ModuParams.SetBinaryData`、`GetParamObj()->GetBinaryData/SetBinaryData`
- 属性：`ModuParams.RadNum`
- DLL：`OpenCvSharp.dll`

**注意事项 / 坑**
- 输入图像名必须用默认名称 `InImage` / `InImageHeight` / `InImageWidth` / `InImagePixelFormat`。
- 基本参数与运行参数在「是否窗口显示 / 是否永久有效」上行为不同。
- ROI 坐标全部按图像宽高归一化（0~1）。
- 多 ROI / 多屏蔽区的字节数需按结构体实际大小计算（如 38 = 1+1+4+(4+4)*2）。

---

### 2.2.4 图像源：通过图像源模块接口设置图像输入的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：在 VM 中可通过界面给图像源模块输入本地图像，如何通过代码给图像源模块设置图像输入。

**原因 / 原理**
- 不熟悉如何通过图像源模块接口设置输入图像。图像源输入分 8 位图和 24 位图，但图像算子只能处理 8 位图（24 位图需转 MONO8 或开启输出 Mono8 使能）。

**解决步骤**
1. 当图像源输入为 24 位图：像素格式选 `MONO8`，运行时输出 8 位图，圆查找的图像输入源选「图像源的图像数据」；或像素格式选 `RGB24` 并打开「输出 Mono8 使能」，输出多一个灰度图像数据，圆查找选「图像源的灰度图像数据」。
2. 图像源类型为 `LocalImage`：用 `AddImage` / `DeleteImage` / `ClearImage` 遍历文件夹。
3. 图像源类型为 `SDK`：用 `SetImagePath` 或 `SetImageData`（注意 `ImageBaseData` 的像素格式）。

**关键代码**
```csharp
ImageSourceModuleTool imageSourcTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.LocalImage;
//给本地图增加图像
imageSourcTool.ModuParams.SetParamValue("AddImage", "E:\\VSVM4.0\\1.bmp");
//给本地图删除图像
imageSource.ModuParams.SetParamValue("DeleteImage","C:\\Users\\zhouyigen\\Desktop\\2.jpg");
//给本地图清空图像
imageSource.ModuParams.SetParamValue("ClearImage", "");

DirectoryInfo dir = new DirectoryInfo("E:\\VSVM4.2\\图像\\新建文件夹");
FileInfo[] dirinfo = dir.GetFiles();
for (int i = 0; i < dirinfo.Length; i++)
{
    string str= dirinfo[i].FullName;
    imageSourcTool.ModuParams.SetParamValue("AddImage", str);
}
```
```csharp
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.SDK;
imageSourcTool.SetImagePath("E:\\VSVM4.0\\1.bmp");
imageSourcTool.SetImageData(imageBaseData);//参数类型为ImageBaseData
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`ImageSourceModuleTool`、`ImageSourceParam`
- 枚举：`ImageSourceParam.ImageSourceTypeEnum.LocalImage` / `.SDK`
- 方法：`ModuParams.SetParamValue("AddImage"/"DeleteImage"/"ClearImage")`、`SetImagePath`、`SetImageData`
- 类型：`ImageBaseData`
- 像素格式：`ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8` / `IMAGE_PIXEL_FORMAT_RGB24`

**注意事项 / 坑**
- 图像算子只能处理 8 位图；24 位图需转 MONO8 或开 Mono8 输出使能。
- `SetImageData` 的参数类型为 `ImageBaseData`。

---

### 2.2.5 图像源：通过 SDK 传入相机图像的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：图像源类型为 SDK 时，可用 `SetImagePath` 或 `SetImageData` 输入图像；如何用 `SetImageData` 传入相机图像。

**原因 / 原理**
- 不熟悉如何通过图像源模块接口 `SetImageData` 传入相机图像。先用海康相机 SDK 取流得到 `byte[]`，再封装为 `ImageBaseData` 喂给图像源模块。

**解决步骤**
1. 手动或代码将图像源类型设为 `SDK`（`ImageSourceType = SDK`）。
2. 使用海康相机 SDK 取流，将帧数据转为 `ImageBaseData`，调用 `SetImageData` 并 `Run()`。

**关键代码**
```csharp
private void SetImageTest()
{
    MyCamera m_MyCamera = new MyCamera();

    try
    {
        // ch:开始采集 | en:Start Grabbing
        int nRet=m_MyCamera.MV_CC_StartGrabbing_NET();
        if (MyCamera.MV_OK != nRet){return;}

        //1.海康相机SDK截取帧
        MyCamera.MV_FRAME_OUT stFrameOut = new MyCamera.MV_FRAME_OUT();
        nRet = m_MyCamera.MV_CC_GetImageBuffer_NET(ref stFrameOut, 1000);
        if (nRet == MyCamera.MV_OK)
        {
            //2.申请byte[]
            byte[] m_BufForDriver1 = new byte[stFrameOut.stFrameInfo.nFrameLen];

            //3.海康相机取流 指针转byte[]
            Marshal.Copy(stFrameOut.pBufAddr, m_BufForDriver1, 0, ((int)stFrameOut.stFrameInfo.nFrameLen));

            //4.byte[]转ImageBaseData，其中1也可以写成ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8
            ImageBaseData stInputImageInfo = new ImageBaseData(m_BufForDriver1, stFrameOut.stFrameInfo.nFrameLen, stFrameOut.stFrameInfo.nWidth, stFrameOut.stFrameInfo.nHeight, 1);

            //5.图像源设置ImageBaseData图像数据
            ImageSourceModuleTool imageSourceModuleTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
            imageSourceModuleTool.SetImageData(stInputImageInfo);

            //流程执行
            process.Run();
        }

        // ch:停止采集 | en:Stop Grabbing
        nRet = m_MyCamera.MV_CC_StopGrabbing_NET();
        if (nRet != MyCamera.MV_OK)
    }
    catch (VmException ex)
    {
        return;
    }
}
```
```cpp
MV_FRAME_OUT_INFO_EX stImageInfo = { 0 };
//相机获取一帧图像
nRet = m_pcMyCamera->GetOneFrameTimeout(m_pGrabBuf, m_nGrabBufSize, &stImageInfo, 1000);
ImageSourceModuleTool * pObject = (ImageSourceModuleTool *)(*m_pVmSol)["流程1.图像源1"];
if (NULL == pObject) return;
ImageBaseData pstImgData = { 0 };
pstImgData.ImageData = m_pGrabBuf;
pstImgData.DataLen = stImageInfo.nWidth * stImageInfo.nHeight;
pstImgData.Width = stImageInfo.nWidth;
pstImgData.Height = stImageInfo.nHeight;
pstImgData.Pixelformat = PIXEL_FORMAT_MONO8;
pObject->SetImageData(&pstImgData);
m_pVmSol->Run();
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`MyCamera`、`ImageSourceModuleTool`
- 结构：`MyCamera.MV_FRAME_OUT`、`MV_FRAME_OUT_INFO_EX`、`ImageBaseData`
- 方法：`MV_CC_StartGrabbing_NET`、`MV_CC_GetImageBuffer_NET`、`MV_CC_StopGrabbing_NET`、`GetOneFrameTimeout`、`SetImageData`、`Run`
- 常量：`MyCamera.MV_OK`、`PIXEL_FORMAT_MONO8`

**注意事项 / 坑**
- `ImageBaseData` 第 5 个参数 `1` 即 MONO8（也可写 `IMAGE_PIXEL_FORMAT_MONO8`）。
- 取流后需 `Run()` 触发流程执行。

---

### 2.2.6 输出图像：获取渲染图像数据的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何获取渲染图像的数据。

**原因 / 原理**
- 不熟悉如何获取渲染图像数据。两种方式：① 输出图像模块存图到本地（开存图使能）；② 实例化输出图像模块取 `byte`。

**解决步骤**
1. 存图到本地：输出图像模块像素格式选 `RGB24` 或 `MONO8`，渲染设置页订阅模块；开启「存图使能」选路径与命名。渲染控件也有存图接口（VM4.0 渲染控件存图为 24 位图）。
2. 获取渲染图像数据：实例化输出图像模块取 `byte`，或流程输出设置订阅输出图像模块取 `byte`（以模块输出为例，见代码；像素格式 `17301505`=MONO8，`35127316`=RGB24）。

**关键代码**
```csharp
SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance["流程1.输出图像1"];//实例化输出图像模块
Var saveImageResult=saveIamge.ModuResult.OutputImage;
byte[] imageData= saveImageResult.ImageData;
int imagePixelformat= saveImageResult.Pixelformat;// 35127316 为彩色图
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`SaveImageTool`
- 属性：`ModuResult.OutputImage`（含 `ImageData`、`Pixelformat`）
- 像素格式：`17301505`=MONO8，`35127316`=RGB24

**注意事项 / 坑**
- 输出图像模块像素格式默认 RGB24（即 `35127316`）。

---

### 2.2.7 N 点标定：清空标定点、生成标定文件和渲染轨迹的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：通过代码清空 N 点标定模块中标定点数据，通过代码生成标定文件。

**原因 / 原理**
- 不熟悉 VM 二次开发接口。`Clear` 清空标定点，`SaveCalibPath` 生成标定文件，渲染时需额外设置背景图像。

**解决步骤**
1. 清空标定点：设 `ModuParams.SetParamValue("Clear","")`；生成标定文件：设 `SetParamValue("SaveCalibPath", path)`。注意保存前需判断标定状态（`ModuResult.ModuStatus == 1` 表示标定完成），否则会报错保存失败。
2. 渲染控件渲染 N 点标定轨迹：除把模块赋值给渲染控件外，还需设置背景图像（图像源的 `ImageData`）。

**关键代码**
```csharp
IMVSNPointCalibModuTool iMVSNPoint = (IMVSNPointCalibModuTool)VmSolution.Instance["流程1.N 点标定1"];
//清空标定点
iMVSNPoint.ModuParams.SetParamValue("Clear" , "");
//生成标定文件
iMVSNPoint.ModuParams.SetParamValue("SaveCalibPath" , path);
```
```csharp
//获取标定状态
IMVSNPointCalibModuTool iMVSNPoint = (IMVSNPointCalibModuTool)VmSolution.Instance["流程1.N 点标定1"];
int i = too.ModuResult.ModuStatus;
if(i ==1){ }
```
```csharp
vmRenderControl1.ModuleSource = N 点标定模块;
VmIO CalibIO = VmSolution.Instance["流程名.图像源名.ImageData"] as VmIO;
vmRenderControl1.SetBackgroundImage(CalibIO);
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`IMVSNPointCalibModuTool`、`VmIO`
- 方法/参数：`ModuParams.SetParamValue("Clear"/"SaveCalibPath")`、`ModuResult.ModuStatus`、`vmRenderControl1.SetBackgroundImage`

**注意事项 / 坑**
- 未标定完成就保存标定文件会报错，需先判断 `ModuStatus == 1`。
- N 点标定渲染必须额外 `SetBackgroundImage`。

---

### 2.2.8 耗时统计：流程与模块运行耗时的获取方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：为计算总耗时，需要了解如何获取流程或某个模块的运行时间。

**原因 / 原理**
- 不熟悉相关接口的使用。耗时通过 `ProcessTime` / `ModuleTime` / `AlgorithmTime` 获取。

**解决步骤**
1. 实例化流程/模块/算法，调用 `ProcessTime`（流程耗时）、`ModuleTime`（模块耗时）、`AlgorithmTime`（算法耗时）。

**关键代码**
```csharp
VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
IMVSCircleFindModuTool circleFind = (IMVSCircleFindModuTool)VmSolution.Instance ["流程1.圆查找1"];
float processtime = vmProcedure .ProcessTime;//流程运行时间
float moduletime = circleFind.ModuleTime;//模块运行时间
```
```csharp
// 在回调函数里获取流程耗时，两种方法如下：
Task.Run(() =>
{
    float processtime = vmProcedure .ProcessTime;//流程运行时间
});

// 或者
float time = workStatusInfo.fProcessTime;
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmProcedure`、`IMVSCircleFindModuTool`
- 属性：`ProcessTime`、`ModuleTime`、`AlgorithmTime`、`workStatusInfo.fProcessTime`

**注意事项 / 坑**
- 回调中获取流程耗时建议用 `Task.Run` 或取 `workStatusInfo.fProcessTime`。

---

### 2.2.9 资源释放：方案资源释放的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何释放资源。

**原因 / 原理**
- 不熟悉相关接口的使用。关闭程序时推荐用 `Dispose` 释放 VM 资源。

**解决步骤**
1. 在窗体 `FormClosing` 事件中调用 `VmSolution.Instance.Dispose()`。

**关键代码**
```csharp
private void Form1_FormClosing(object sender, FormClosingEventArgs e)
{
    VmSolution.Instance.Dispose();
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmSolution`
- 方法：`Instance.Dispose()`

**注意事项 / 坑**
- 务必在程序退出时释放，避免资源泄漏/VM 进程残留。

---

### 2.2.10 条件检测：条件检测模块设置范围的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何用编程实现条件检测模块所订阅的相关模块结果进行范围的设置。

**原因 / 原理**
- 不熟悉条件检测的相关接口。条件检测接口类为 `IfModuleTool`，`int0` 为所订阅的变量名。

**解决步骤**
1. 用 `IfModuleTool`，通过 `GetDynamicParam("int0_Max"/"int0_Min").SetIntValue(...)` 设置范围。

**关键代码**
```csharp
IfModuleTool ifModuleTool = (IfModuleTool)VmSolution.Instance["流程1.条件检测1"];
ifModuleTool.ModuParams.GetDynamicParam("int0_Max").SetIntValue(1000);
ifModuleTool.ModuParams.GetDynamicParam("int0_Min").SetIntValue(1);
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`IfModuleTool`
- 方法：`ModuParams.GetDynamicParam(...).SetIntValue(...)`

**注意事项 / 坑**
- 变量名形如 `int0_Max` / `int0_Min`，`int0` 为订阅变量名。

---

### 2.2.11 流程ID：通过流程名获取流程ID 的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + vs2015 及以上。
- 现象：怎么获取流程 ID。

**原因 / 原理**
- 不熟悉流程接口功能编写。通过 `GetAllProcedureList()` 遍历流程列表匹配流程名。

**解决步骤**
1. 调用 `VmSolution.Instance.GetAllProcedureList()` 获取所有流程，遍历 `astProcessInfo` 匹配 `strProcessName`，取出 `nProcessID`。

**关键代码**
```csharp
public static bool GetProcessID(string ProcessName, ref int ProcessID, ref string ErrorMessage)
{
    bool findIDResult = false;
    try
    {
        ProcessInfoList stProcList = VmSolution.Instance.GetAllProcedureList(); // 获取所有流程列表

        for (int i = 0; i < stProcList.nNum; i++)
        {
            string _ProcessName = stProcList.astProcessInfo[i].strProcessName;
            if (ProcessName == _ProcessName)
            {
                ProcessID = (int)stProcList.astProcessInfo[i].nProcessID;
                findIDResult = true;
                break;
            }
        }
    }
    catch (Exception ex)
    {
        findIDResult = false;
        ErrorMessage = "获取流程ID 异常：" + ex.Message;
    }
    return findIDResult;
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 类/结构：`ProcessInfoList`、`ProcessInfoList.astProcessInfo`
- 方法：`VmSolution.Instance.GetAllProcedureList()`
- 字段：`strProcessName`、`nProcessID`、`nNum`

**注意事项 / 坑**
- 流程 ID 为整型，常用于回调中判断 `nProcessID == 10000`（流程1）。

---

### 2.2.12 几何创建：绘制形状的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：在几何创建模块中，VM 二次开发如何通过代码绘制形状。

**原因 / 原理**
- 不熟悉几何创建模块的接口。几何创建绘制形状与设置 ROI 相关，需组装二进制数据通过 `SetBinaryData("GeometryType", ptr, size)` 传入。

**解决步骤**
1. 实例化几何创建模块，构造形状结构（如 `Geo1line`），归一化坐标（除以图像宽高），用 `Marshal` 转为指针后 `SetBinaryData`。

**关键代码**
```csharp
private void button6_Click(object sender, EventArgs e)
{
    GeometryCreateTool tool = (GeometryCreateTool)VmSolution.Instance["流程1.几何创建1"];
    Geo1line linetool = new Geo1line();
    linetool.nType = (byte)8;
    linetool.fStartX = 123.0f / 5472; //由于归一化，所以要除以图像的高和宽
    linetool.fStartY = 100.0f / 3648;
    linetool.fEndX = 2000.0f / 5472;
    linetool.fEndY = 2000.0f / 3648;

    int size = Marshal.SizeOf(linetool);
    IntPtr intpt = Marshal.AllocHGlobal(Marshal.SizeOf(linetool));
    Marshal.StructureToPtr(linetool, intpt, true);
    //SetBinaryData接口的参数分别为GeometryType，地址指针，内存大小
    tool.ModuParams.SetBinaryData("GeometryType", intpt, (uint)size);//接口函数
}

//结构体序列化
[StructLayout(LayoutKind.Sequential, Pack = 1)]
public struct Geo1line
{
    public byte nType;      //7 是点，8 是线，9 是圆
    public byte nVersion;   //填0
    public float fStartX;   //
    public float fStartY;   //
    public float fEndX;     //
    public float fEndY;    //
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`GeometryCreateTool`
- 结构：`Geo1line`（`nType` 7=点/8=线/9=圆，`Pack=1`）
- 方法：`ModuParams.SetBinaryData("GeometryType", ptr, size)`
- 特性：`[StructLayout(LayoutKind.Sequential, Pack = 1)]`

**注意事项 / 坑**
- 坐标需按图像宽高归一化；`nType` 决定形状类型。

---

### 2.2.13 运行间隔：设置和获取流程运行间隔的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：VM 二次开发如何设置和获取流程运行间隔。

**原因 / 原理**
- 不熟悉二次开发设置与获取流程运行间隔的接口。方案级与流程级分别有 `SetRunInterval` / `SetContinousRunInterval`。

**解决步骤**
1. 设置方案运行间隔：`VmSolution.Instance.SetRunInterval(500)`。
2. 设置流程运行间隔：流程实例化后 `SetContinousRunInterval(500)`。
3. 获取流程运行间隔：`ServerSDKManager...GetContinousRunInterval(流程ID, ref time)`。

**关键代码**
```csharp
//设置方案运行间隔
VmSolution.Instance.SetRunInterval(500);

//设置流程运行间隔
VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//流程实例化
VmProcess.SetContinousRunInterval(500);

//获取流程运行间隔
uint time = 0;
ServerSDKManager.serverSDKManager.mProcessManager.GetContinousRunInterval(10000, ref time); //第一个参数为流程ID，第二个参数为间隔时间
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmSolution`、`VmProcedure`、`ServerSDKManager`
- 方法：`SetRunInterval`、`SetContinousRunInterval`、`GetContinousRunInterval`

**注意事项 / 坑**
- 获取间隔的第一个参数为流程 ID（如 10000 表示流程1）。

---

### 2.2.14 分支字符：控制调试模式开关的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何控制分支字符调试模式的开关。

**原因 / 原理**
- 不熟悉分支字符模块的调试模式参数名及协议格式。通过 `GetParamValue` 读取 `ModuleInfoList`，其值为形如 `4#1#0$10#0#0$` 的协议串。

**解决步骤**
1. 用 `GetParamValue` 函数读取调试模式相关参数 `ModuleInfoList`，其值如 `4#1#0$10#0#0$`：其中 `4` 表示模块 id，`1` 表示这个分支的条件输入值，`0` 代表是否打开调试模式（按 `$` 分隔的各段）。

**关键代码**
```csharp
// （本条原文无独立代码示例；通过 GetParamValue("ModuleInfoList") 读取协议串，格式：模块id#条件输入值#是否打开调试模式$...）
```

**关键 API / 类名 / 命名空间 / 属性**
- 参数：`ModuleInfoList`
- 协议：`4#1#0$10#0#0$`（模块id#条件输入值#调试模式开关）

**注意事项 / 坑**
- 协议串按 `$` 分段，每段 `模块id#条件输入值#调试模式开关`。

---

### 2.2.15 模块禁用：模块禁用的方法

**问题现象 / 适用场景**
- 环境：VM4.0 + VS2015 及以上。
- 现象：如何将模块通过代码控制是否禁用与启用（类似 VM 中的操作）。

**原因 / 原理**
- 不熟悉模块接口使用。可用模块的 `IsForbidden` 属性禁用模块，但 Group 模块禁用后无法开启（该接口未推荐对外使用）。

**解决步骤**
1. 使用模块的 `IsForbidden` 属性控制禁用/启用（`true` 为禁用）。

**关键代码**
```csharp
using IMVSCircleFindModuCs;
IMVSCircleFindModuTool circleTool=( IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
moduleTool.IsForbidden = true;
```

**关键 API / 类名 / 命名空间 / 属性**
- 命名空间：`IMVSCircleFindModuCs`
- 类：`IMVSCircleFindModuTool`
- 属性：`IsForbidden`

**注意事项 / 坑**
- Group 模块禁用后**无法开启**，`IsForbidden` 接口未推荐对外使用，慎用。

---

### 2.2.16 Group 循环：获取 Group 循环数据结果的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + 2015 及以上。
- 现象：如何获取 Group 循环的所有数据结果。

**原因 / 原理**
- 不熟悉如何获取 Group 循环数据结果。需要在 Group 中用「数据集合」模块，并在 Group 输出设置订阅数据集合模块结果。

**解决步骤**
1. 在 Group 中使用数据集合模块，然后在 Group 的输出设置订阅数据集合模块相关结果，最后在二次开发中获取 Group 的数据结果（`out1` 为 Group 订阅的数据集合，代码中可获取数据数组；界面显示 `out1` 中有重复值，后续会改进）。

**关键代码**
```csharp
// （本条原文无独立代码；通过 Group 输出设置订阅「数据集合」模块结果，再按 2.4.1 流程输出方式读取 out1 数组）
```

**关键 API / 类名 / 命名空间 / 属性**
- 模块：Group 内的「数据集合」模块
- 输出：`out1`（Group 订阅的数据集合结果数组）

**注意事项 / 坑**
- 界面显示 `out1` 会有重复值（已知问题，后续版本改进）。

---

## 2.3 控件嵌入类

### 2.3.1 渲染结果：通过绑定流程或模块获取渲染结果的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：方案或流程运行执行之后，可通过渲染结果（绑定渲染控件显示）获取数据结果。

**原因 / 原理**
- 不熟悉如何获取渲染结果。渲染控件可绑定流程或模块，推荐绑定流程（高内聚低耦合，单控件可显示多模块渲染）。

**解决步骤**
1. 通过绑定流程显示渲染结果（一个渲染控件同时只能绑定一个流程，多流程需分时绑定或多个控件）。
2. 通过绑定模块显示渲染结果（只能渲染某模块的渲染结果）。
3. 环境配置没问题但渲染控件不显示时，用刷新接口 `UpdateVMResultShow()`。

**关键代码**
```csharp
// 1.2 绑定流程
VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//实例化流程1
vmRenderControl.ModuleSource=VmProcess;
```
```cpp
// C++ MFC 绑定流程
IVmProcedure *vmprc = (IVmProcedure*)(*m_pVmSol)["流程1"];
m_ctrlRender.SetParamsInfo(vmprc ->GetControlInfo());
```
```cpp
// C++ Qt 绑定流程
IVmProcedure *vmprc = (IVmProcedure*)(*m_pVmSol)["流程1"];
ui.axWidget_Cam1->dynamicCall("SetParamsInfo(qlongqlong)",(qlonglong)(vmprc->GetControlInfo()));
```
```csharp
// 2 绑定模块
IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool=(IMVSCircleFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
vmRenderControl.ModuleSource= circleTool;
```
```cpp
// C++ MFC 绑定模块
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTool *)(*m_pVmSol)["流程1.圆查找1"];
m_ctrlRender.SetParamsInfo(pCirFindObject ->GetControlInfo());
```
```cpp
// C++ Qt 绑定模块
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTool *)(*m_pVmSol)["流程1.圆查找1"];
ui.axWidget_Cam1->dynamicCall("SetParamsInfo(qlongqlong)",(qlonglong)(pCirFindObject ->GetControlInfo()));
```
```csharp
// 3 刷新
vmRenderControl1.UpdateVMResultShow();
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`vmRenderControl`（`VmRenderControl`）
- 属性：`ModuleSource`
- 方法：`UpdateVMResultShow()`、`GetControlInfo()`、`SetParamsInfo()`
- 接口：`dynamicCall("SetParamsInfo(qlongqlong)", ...)`

**注意事项 / 坑**
- 推荐绑定流程，单控件可显示多模块渲染。
- 不显示时先尝试 `UpdateVMResultShow()`。

---

### 2.3.2 渲染控件：渲染控件加载本地图像的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：渲染控件如何显示本地图像。

**原因 / 原理**
- 不熟悉如何使用渲染控件显示本地图像。思路：图像源模块加本地图像（或接口获取，见 2.2.4），渲染控件绑定图像源模块或绑定流程（流程中提前配置显示设置订阅图像源模块）。

**解决步骤**
1. 在 VM 软件平台给图像源模块添加本地图像，或通过图像源模块接口获取本地图像（参考 2.2.4）。
2. 渲染控件绑定图像源模块或绑定流程（流程中提前配置显示设置订阅图像源模块）。

**关键代码**
```csharp
//使用VM软件平台已经给图像源模块添加本地图像，再使用渲染控件绑定模块
ImageSourceModuleTool testImage = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
vmRenderControl.ModuleSource= testImage;
```
```csharp
// MFC / Qt 绑定方式（原文为图示，文字缺失具体代码，参考 2.3.1 的 SetParamsInfo 写法）
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`ImageSourceModuleTool`、`VmRenderControl`
- 属性：`ModuleSource`

**注意事项 / 坑**
- 必须先让图像源模块有本地图像（平台添加或代码添加），再绑定渲染。

---

### 2.3.3 渲染控件：渲染控件上自定义图形的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何在渲染控件上绘图。

**原因 / 原理**
- 不熟悉如何使用渲染控件显示本地图像（原文根因描述如此）。需引用 `VMControls.WPF.dll`，创建 `LineEx`/`RectangleEx`/`TextEx`/`CircleEx` 等 shape 对象，调用 `DrawShape()`。

**解决步骤**
1. 引用 `VMControls.WPF.dll`（路径 `\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64`），手动添加后「复制到本地」改为 false。
2. 创建所需 shape 对象并赋值，调用 `vmRenderControl.DrawShape()`。
3. 模块渲染效果和自定义图形建议放不同线程；连续运行时若自定义图形跟不上，渲染前加延时（如 `Thread.Sleep(50)`）。

**关键代码**
```csharp
Task.Run(()=>
{
    System.Threading.Thread.Sleep(50);

    This.BeginInvoke(new Action(()=>
    {
        //画线
        VMControls.WPF.LineEx line = new VMControls.WPF.LineEx();
        line.StartPointX = 10;
        line.StartPointY = 10;
        line.EndPointX = 1000;
        line.EndPointY = 1000;
        line.Opacity = 1;
        int nArgb = 0;
        nArgb += 100 << 16;
        nArgb += 200 << 8;
        nArgb += 150;
        line.Color = nArgb;
        line.FillColor = nArgb;
        line.StrokeThickness = 10;
        vmRenderControl.DrawShape(line);

        //画矩形
        VMControls.WPF.RectangleEx rect = new VMControls.WPF.RectangleEx();
        rect.CenterX = 1000;
        rect.CenterX = 1000;
        rect.Width = 500;
        rect.Height = 500;
        vmRenderControl1.DrawShape(rect);

        //画文本
        VMControls.WPF.TextEx text = new VMControls.WPF.TextEx();
        text.Content = "1111111111111111";
        text.FontSize = 30;
        text.PositionX = 500;
        text.PositionY = 500;
        text.Opacity = 2;
        text.Color = nArgb;
        text.FillColor = nArgb;
        text.StrokeThickness = 10;
        vmRenderControl1.DrawShape(text);

        //画圆
        VMControls.WPF.CircleEx circle = new VMControls.WPF.CircleEx();
        circle.CenterX = 2000;
        circle.CenterY = 2000;
        circle.Color = nArgb;
        circle.FillColor = nArgb;
        circle.MajorRadius = 50;//外半径和内半径不等时，则是椭圆
        circle.MinorRadius = 50;
        circle.Opacity = 2;
        circle.StrokeThickness = 3;
        vmRenderControl1.DrawShape(circle);
    }),null);
});
```
```cpp
// Qt 绘制矩形
int nArgb = 0;
nArgb += 255 << 16;
nArgb += 0 << 8;
nArgb += 0;
RectangleEx rectangle = { 0 };
rectangle.CenterX = 550;
rectangle.CenterY = 550;
rectangle.Width = 250;
rectangle.Height = 200;
rectangle.Angle = 25;
rectangle.Opacity = 0.5;
rectangle.SkewAngle = 0;
rectangle.Color = nArgb;
rectangle.FillColor = nArgb;
rectangle.StrokeThickness = 3;
//绘制矩形
ui->axWidget_render->dynamicCall("SetRectangle(qlonglong)", reinterpret_cast(&rectangle));
```

**关键 API / 类名 / 命名空间 / 属性**
- 命名空间：`VMControls.WPF`
- 类：`LineEx`、`RectangleEx`、`TextEx`、`CircleEx`
- 方法：`vmRenderControl.DrawShape(...)`、`dynamicCall("SetRectangle(qlonglong)", ...)`
- DLL：`VMControls.WPF.dll`

**注意事项 / 坑**
- 手动加 `VMControls.WPF.dll` 后「复制本地」必须 false。
- 自定义图形与模块渲染建议分线程，且连续运行前加延时。

---

### 2.3.4 参数控件：参数配置控件绑定模块的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：参数控件如何设定参数。

**原因 / 原理**
- 不熟悉参数配置控件的使用。参数配置控件需绑定模块参数（普通控件绑 `Params`，带渲染控件绑 `ModuleSource`）。

**解决步骤**
1. C# 中：普通参数配置控件绑 `circleFindModule.Params`；带渲染的参数配置控件绑 `ModuleSource`；不确定模块时用 `IVmModule`。
2. MFC 中：取模块参数对象 `GetParamObj()`，调 `SetParamsInfo(...)`。
3. Qt 中：取参数指针，构造 `ParamBaseEx`，`dynamicCall("SetParamsInfo(qlonglong)", ...)`。

**关键代码**
```csharp
// 1) C# 中
IMVSCircleFindModuTool circleFindModule = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
//普通的参数配置控件
vmParamsConfigControl1.ParamsConfig = circleFindModule.Params;
//带渲染的参数配置控件
vmParamsConfigWithRenderControl1.ModuleSource = circleFindModule;

//当不确定具体是哪一个模块时，使用IVmModule类
IVmModule module = (VmModule)VmSolution.Instance[ "流程名.模块名"];
vmParamsConfigWithRenderControl1.ModuleSource = module;
```
```cpp
// 2) MFC 中
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTool *)(*m_pVmSol)["流程1.圆查找1"];
if (NULL == pCirFindObject) return;
CircleFindParams * pCirFindParam = pCirFindObject->GetParamObj();
if (NULL == pCirFindParam) return;
CCircleFindDlg::GetExeFilePath();
m_ctrlParamRender.SetParamsInfo(pCirFindParam->GetControlInfo(), m_strFilePath.c_str());
```
```cpp
// 3) Qt 中
IMVSCircleFindModuTool *circleFindMou=static_cast<IMVSCircleFindModuTool*>((*m_pVmSol)["流程1.圆查找1"]);
ParamCtrlInput *param=reinterpret_cast<ParamCtrlInput*>(circleFindMou ->GetParamObj());
ParamBaseEx stParamData={0};
stParamData.Handle=param->Handle;
stParamData.ModuId=param->ModuId;
stParamData.TimeOut=0;
//绑定参数渲染控件
ui->axWidget_3->dynamicCall("SetParamsInfo(qlonglong)",reinterpret_cast<qlonglong>(&stParamData));
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`vmParamsConfigControl`（ParamsConfig）、`vmParamsConfigWithRenderControl`（ModuleSource）
- 类：`IVmModule`、`VmModule`、`CircleFindParams`、`ParamCtrlInput`、`ParamBaseEx`
- 方法：`GetParamObj()`、`GetControlInfo()`、`SetParamsInfo()`

**注意事项 / 坑**
- 不确定具体模块时用 `IVmModule` 通用绑定。

---

### 2.3.5 控件颜色：控件颜色修改的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：简易修改 VM 控件的颜色。

**原因 / 原理**
- 不了解 VM 控件颜色可以改变。颜色由 `ColorStyle` 文件夹下的 XAML 定义，通过 `AppColorService.CurColorDefine` 切换。

**解决步骤**
1. 代码中设置 `AppColorService.CurColorDefine = "ColorStyle3"`（`ColorStyle3` 文件在 VM 安装路径的 `ColorStyle` 文件夹下）。
2. 客户可自行编辑 XAML 文件修改控件颜色，即可生效。

**关键代码**
```csharp
string colorinfo = "ColorStyle3";
AppColorService.CurColorDefine = colorinfo;
```

**关键 API / 类名 / 命名空间 / 属性**
- 类/属性：`AppColorService.CurColorDefine`
- 资源：`ColorStyle` 文件夹下的 XAML（如 `ColorStyle3`）

**注意事项 / 坑**
- 颜色文件为 XAML，可自定义编辑。

---

### 2.3.6 VM 嵌入：嵌入用户软件界面的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：将 VM 整体嵌入到客户软件界面中。

**原因 / 原理**
- 不了解 Panel 控件用法、如何嵌入第三方程序。利用 Windows API `SetParent` + `MoveWindow` 把 `VisionMaster.exe` 主窗口挂到 Panel。

**解决步骤**
1. 利用 `Panel` 控件，先启动 VM 软件（`Process.Start`），待其空闲后取主窗口句柄，再 `SetParent` 到 Panel 并 `MoveWindow` 适应大小。

**关键代码**
```csharp
[DllImport("User32.dll", EntryPoint = "SetParent")]
public static extern int SetParent(IntPtr hWndChild, IntPtr hWndNewParent);

[DllImport("user32.dll", CharSet = CharSet.Auto)]
public static extern int MoveWindow(IntPtr hWnd, int x, int y, int nWidth, int nHeight, bool BRePaint);

// Start the process
p = System.Diagnostics.Process.Start(@"D: \VisionMaster4.0.0\Applications\VisionMaster.exe");
// Wait for process to be created and enter idle condition
p.WaitForInputIdle();
// Get the main handle
appWin = p.MainWindowHandle;
//需要等待p启动，可自行判断，可加上Thread.Sleep(10000);
SetParent(appWin, panel1.Handle);//this在这里是Panel控件
MoveWindow(appWin, 0, 0, this.panel1.Width, this.panel1.Height, true);
```

**关键 API / 类名 / 命名空间 / 属性**
- API：`SetParent`、`MoveWindow`（user32.dll）
- 类：`System.Diagnostics.Process`、`Process.Start`、`WaitForInputIdle`
- 控件：`Panel`（panel1）
- 路径：`VisionMaster4.0.0\Applications\VisionMaster.exe`

**注意事项 / 坑**
- 需等待 VM 启动（`WaitForInputIdle` 或 `Thread.Sleep(10000)`）后再 `SetParent`。

---

### 2.3.7 参数控件：隐藏参数设置控件上某些参数的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何隐藏参数设置控件上的某些参数。

**原因 / 原理**
- 不熟悉配置文件修改方式。通过修改模块 XML 配置中的可见性属性实现隐藏。

**解决步骤**
1. 隐藏前，绑定圆查找模块参数控件，运行参数如下（可见）。
2. 在二次开发程序找到圆查找模块配置路径 `\VMTest\VMTest\bin\Debug\Module(sp)\x64\Location\IMVSCircleFindModu\IMVSCircleFindModuAlgorithmTab.xml`，双击打开。
3. 找到运行参数中卡尺数量处，定位 `<Visibility>Beginner</Visibility>`。
4. 修改为 `<CustomVisible> False </CustomVisible>`。
5. 隐藏后的绑定参数控件运行参数即不再显示该项。
6. 同理：VM 中隐藏模块某些参数，打开 VM 安装路径 `VM4.0.0\VisionMaster4.0.0\Applications\Module(sp)\x64\Location\IMVSCircleFindModu` 下的同名 XML。

**关键代码**
```xml
<!-- 修改前 -->
<Visibility>Beginner</Visibility>
<!-- 修改后 -->
<CustomVisible> False </CustomVisible>
```

**关键 API / 类名 / 命名空间 / 属性**
- 文件：`IMVSCircleFindModuAlgorithmTab.xml`
- 路径：`Module(sp)\x64\Location\IMVSCircleFindModu`
- 属性：`Visibility` → `CustomVisible`

**注意事项 / 坑**
- 修改的是模块算法 Tab 的 XML 配置文件，二次开发与 VM 本体路径不同（Debug 内 vs 安装目录内）。

---

### 2.3.8 渲染控件：通过鼠标点击获取渲染控件像素坐标的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何通过鼠标事件获取渲染控件上的图像坐标。

**原因 / 原理**
- 不熟悉控件事件。通过订阅 `OnMouseLeftButtonDownPixelChanged` 事件获取像素坐标。

**解决步骤**
1. 注册鼠标左键按下像素变化事件，在回调中取得 `(x, y)` 图像坐标。

**关键代码**
```csharp
// 注册鼠标点击事件
public OneWindowUserControl(MainWindow mainWindow)
{
    InitializeComponent();
    RenderImage1.OnMouseLeftButtonDownPixelChanged += RenderImage_OnMouseLeftButtonDownPixelChanged1;
}

// 获取锚点事件
private void RenderImage_OnMouseLeftButtonDownPixelChanged1(int x, int y)
{
    try
    {
        var pointX = x;
        var pointY = y;
        MessageBox.Show("锚点获取成功");
    }
    catch (Exception ex)
    {
        MessageBox.Show("获取锚点失败" + ex.ToString());
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`RenderImage1`（渲染图像控件）
- 事件：`OnMouseLeftButtonDownPixelChanged`（回调参数 `int x, int y`）

**注意事项 / 坑**
- 回调直接给出图像像素坐标，无需自行换算。

---

### 2.3.9 控件显示：控件显示所加载的流程的方法

**问题现象 / 适用场景**
- 环境：VM4.0 + VS2015 及以上。
- 问题：基于对话框的 MFC 程序，主窗口放置了 `VmMainView` 控件，程序初始化时可显示，但加载方案完成时不会显示已加载的流程。

**原因 / 原理**
- `CreateSolutionInstance()` 需要在控件初始化时调用一次，用来提前绑定 `VmMainView` 控件关联的方案。

**解决步骤**
1. 在使用带流程显示的控件（如 `VmMainView`）时，需在控件的初始化代码 `GetObjectPointer()` 之前，调用一次 `CreateSolutionInstance()`。

**关键代码**
```cpp
CreateSolutionInstance();
mainViewControl.GetObjectPointer();
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`VmMainView`（mainViewControl）
- 方法：`CreateSolutionInstance()`、`GetObjectPointer()`

**注意事项 / 坑**
- 必须在 `GetObjectPointer()` 之前调用 `CreateSolutionInstance()`，否则加载方案后流程不显示。

---

### 2.3.10 前端界面控件：前端界面控件大小自适应的方法

**问题现象 / 适用场景**
- 环境：VM4.0 + VS2015 及以上。
- 现象：WinForm 中使用前端界面控件，设置 Anchor/Dock 属性后控件内元素不随界面放缩，如何实现前端界面大小自适应。

**原因 / 原理**
- 不熟悉控件内容放缩接口的调用时机。需手动调用 `AutoChangeSize()`。

**解决步骤**
1. 在界面上拖拽 `vmFrontendControl` 控件（专用于显示 VM 方案前端界面）并设置 Anchor/Dock。
2. 方案加载完成后加载前端界面资源（`LoadFrontendSource()`）。
3. 给控件添加大小变化事件，在 `SizeChanged` 中调用 `AutoChangeSize()`。

**关键代码**
```csharp
private void button16_Click(object sender, EventArgs e)
{
    vmFrontendControl.LoadFrontendSource();
}
```
```csharp
private void vmFrontendControl_SizeChanged(object sender, EventArgs e)
{
    vmFrontendControl.AutoChangeSize();
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`vmFrontendControl`
- 方法：`LoadFrontendSource()`、`AutoChangeSize()`
- 事件：`SizeChanged`

**注意事项 / 坑**
- 必须在 `SizeChanged` 事件中调用 `AutoChangeSize()` 才会随窗体放缩。

---

### 2.3.11 渲染控件：渲染控件存图的方法

**问题现象 / 适用场景**
- 环境：VM4.0 + VS2015 及以上。
- 现象：常见存图方法有输出图像模块以及渲染控件存图，渲染控件存图的方法如何实现。

**原因 / 原理**
- 不熟悉渲染控件存图接口。渲染时机在回调结束之后，因此回调中存图会得到未渲染完成的图；必须在 `button` 事件中存图。

**解决步骤**
1. 使用 `SaveOriginalImage` / `SaveRenderedImage`；但推荐使用输出图像模块存图。在 `button` 事件中调用才能正常存图。

**关键代码**
```csharp
vmRenderControl1.SaveOriginalImage("E:\\VSVM4.2\\VMTestB\\original.bmp");
vmRenderControl1.SaveRenderedImage("E:\\VSVM4.2\\VMTestB\\RenderImage.bmp");
```

**关键 API / 类名 / 命名空间 / 属性**
- 控件：`vmRenderControl1`
- 方法：`SaveOriginalImage(path)`、`SaveRenderedImage(path)`

**注意事项 / 坑**
- 渲染时机在回调之后，回调/`Run` 后立即存图会是空白或未渲染完成；必须在 button 事件中存图。
- 优先用「输出图像模块」存图。

---

## 2.4 结果获取类

### 2.4.1 数据结果：通过流程输出或模块输出获取数据结果的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：方案或流程运行执行之后即可获取结果（建议写在回调函数里）。数据结果分整型、浮点型、字符串型和图像型等，如何获取数据结果。

**原因 / 原理**
- 不熟悉如何获取数据结果。推荐通过流程输出（高内聚低耦合），也可通过模块输出。

**解决步骤**
1. 通过流程的输出获取数据结果：
   - 整型/浮点型/字符串型用 `GetIntOutputResult` / `GetFloatOutputResult` / `GetStringOutputResult`；
   - 图像型需通过 `Imageout0` / `ImageWidthout0` / `ImageHeightout0` / `ImagePixelFormatout0` 四个参数获取。
2. 通过模块的输出获取数据结果：
   - 浮点型直接读 `ModuResult.OutputCircle...`；
   - 图像数据读 `ModuResult.ImageData` / `ModuResult.OutputImage`。

**关键代码**
```csharp
// 1.2 获取整型、浮点型、字符串型数据
VmProcedure vmprocess = (VmProcedure)VmSolution.Instance["流程1"];
string str = vmprocess.GetIntOutputResult("out").pIntValue[0].ToString();
string str1 = vmprocess.GetFloatOutputResult("out0").pFloatValue[0].ToString();
string str2 = vmprocess.GetStringOutputResult("out1").astStringValue[0].strValue;

// 流程拿结果，c从界面层获取的方法，适用于高内存场景
string str2 = ((ImvsSdkDefine.IMVS_MODULE_STRING_VALUE_EX)(vmProcess["out1.Value"] as Array).GetValue(0)).strValue.ToString();//字符串型结果
string str1 = ((vmProcess["out0.Value"] as Array).GetValue(0)).ToString();//浮点型结果
```
```csharp
// 1.3 获取图像数据
VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//实例化流程1
ImageResultInfo resultInfo0 =VmProcess.GetImageOutputResult("Imageout0");
IntResultInfo resultInfo1 =VmProcess.GetIntOutputResult("ImageWidthout0");
IntResultInfo resultInfo2 =VmProcess.GetIntOutputResult("ImageHeightout0");
IntResultInfo resultInfo3 =VmProcess.GetIntOutputResult("ImagePixelFormatout0");
byte[] imageData=resultInfo0.pstImageValue[0].pData;
```
```csharp
// 2.1 获取模块的浮点型数据
IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool=(IMVSCircleFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
//只调用一次circleTool.ModuResult表示只从底层拿一次结果，适用于高内存场景
var circleToolResult = circleTool.ModuResult;
string circleX = circleToolResult.OutputCircle.CenterPoint.X.ToString();
string circleY = circleToolResult.OutputCircle.CenterPoint.Y.ToString();
string circleR = circleToolResult.OutputCircle.Radius.ToString();
```
```csharp
// 2.2 获取图像数据，针对有图像输出的模块
//图像源模块
Using ImageSourceModuleCs;
ImageSourceModuleTool sourceImage=(ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];//实例化输出图形模块
Var sourceImageResult=sourceIamge.ModuResult.ImageData;//只需要调用一次ModuResult,适用于高内存场景
byte[] imageData= sourceImageResult.ImageData;
int imagePixelformat= sourceImageResult.Pixelformat;

//输出图像模块
Using SaveImageCs;
SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance["流程1.输出图像1"];//实例化输出图像模块
Var saveImageResult=saveIamge.ModuResult.OutputImage;//只需要调用一次ModuResult,适用于高内存场景
byte[] imageData= saveImageResult.ImageData;
int imagePixelformat= saveImageResult.Pixelformat;
```
像素格式 `17301505` 为 MONO8 灰度图，像素格式 `35127316` 为 RGB24 彩色图；输出图像模块像素格式默认是 RGB24（即 `35127316`）。

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmProcedure`、`IMVSCircleFindModuTool`、`ImageSourceModuleTool`、`SaveImageTool`
- 方法：`GetIntOutputResult` / `GetFloatOutputResult` / `GetStringOutputResult` / `GetImageOutputResult`
- 结构：`ImageResultInfo`、`IntResultInfo`、`ImvsSdkDefine.IMVS_MODULE_STRING_VALUE_EX`
- 属性：`ModuResult.OutputCircle.CenterPoint.X/Y`、`ModuResult.OutputCircle.Radius`、`ModuResult.ImageData`、`ModuResult.OutputImage`
- 像素格式：`17301505`=MONO8，`35127316`=RGB24
- 输出名：`Imageout0` / `ImageWidthout0` / `ImageHeightout0` / `ImagePixelFormatout0`

**注意事项 / 坑**
- 图像输出必须用 `Imageout0` 等四个参数名，不能用自定义 image 名。
- 高内存场景只调用一次 `ModuResult` 拿结果。

---

### 2.4.2 流程运行：所有流程运行结束的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：流程运行的触发方式有多种，无论哪种方式都会进入回调函数，因此建议在回调函数中获取结果。

**原因 / 原理**
- 不熟悉流程运行结束的回调函数。注册 `OnWorkStatusEvent`（C#）或 `RegisterCallBack`（C++），在 `nWorkStatus==0` 且 `nProcessID==10000` 时表示流程1执行完毕。

**解决步骤**
1. 注册回调函数（C# 用事件 `OnWorkStatusEvent`；C++ 用 `RegisterCallBack`）。
2. 在回调中判断 `nWorkStatus==0`（执行完毕）与 `nProcessID`（流程 ID），获取结果/渲染结果。

**关键代码**
```csharp
public Form1()
{
    InitializeComponent();
    //注册回调函数，流程运行状态回调
    VmSolution.OnWorkStatusEvent += VmSolution_OnWorkStatusEvent;
}
private void VmSolution_OnWorkStatusEvent(ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo)
{
    if (workStatusInfo.nWorkStatus == 0 && workStatusInfo.nProcessID == 10000)//为0表示执行完毕，为1表示正在执行；10000表示流程1
    {
        //获取结果
    }
}
```
```cpp
//类中声明变量和函数
IVmSolution* m_pVmSol;
IVmProcedure* m_pVmPrc;
static int __stdcall SolutionCallback(IN OutputPlatformInfo * const pstInputPlatformInfo, IN void * const pUser);
int SolutionCallbackFunc(IN OutputPlatformInfo * const pstInputPlatformInfo);

//在初始化时用方案注册回调函数，这是所有流程运行结束都会自动进的回调函数
m_pVmSol->RegisterCallBack(SolutionCallback, this);

//回调函数的实现方法,Demo为项目类名
int __stdcall Demo::SolutionCallback(IN OutputPlatformInfo * const pstInputPlatformInfo, IN void * const pUser)
{
    auto *pCtrlDemoThis = static_cast<Demo*>(pUser);
    int nRet = IMVS_EC_UNKNOWN;
    if (pCtrlDemoThis)
    {
        nRet = pCtrlDemoThis->SolutionCallbackFunc(pstInputPlatformInfo);
        if (IMVS_EC_OK != nRet)
        {
            return nRet;
        }
    }
    return IMVS_EC_OK;
}
int Demo::SolutionCallbackFunc(IN OutputPlatformInfo * const pstInputPlatformInfo)
{
    if (pstInputPlatformInfo->nInfoType == IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_WORK_STATE)
    {
        try {
            auto workstateInfo = static_cast<IMVS_PF_MODULE_WORK_STAUS*>(pstInputPlatformInfo->pData);
            if (workstateInfo->nWorkStatus == 0 && workstateInfo->nProcessID == 10000)//判断流程执行状态和流程ID
            {
                auto m_pVmPro = (IVmProcedure*)(*m_pVmSol)["流程1"];
                float info = m_pVmPro->GetResult()->GetOutputFloat("out").pFloatVal[0];
            }
        }
        catch (exception *e)
        {
            TRACE(e->what());
        }
    }
    return 0;
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`VmSolution.OnWorkStatusEvent`
- 结构：`ImvsSdkDefine.IMVS_MODULE_WORK_STAUS`
- 字段：`nWorkStatus`（0=完毕/1=执行中）、`nProcessID`
- C++：`IVmSolution`、`RegisterCallBack`、`OutputPlatformInfo`、`IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_WORK_STATE`、`IMVS_PF_MODULE_WORK_STAUS`、`GetResult()->GetOutputFloat`
- 常量：`IMVS_EC_OK`、`IMVS_EC_UNKNOWN`

**注意事项 / 坑**
- C# 回调中获取渲染结果需用委托 `this.BeginInvoke` 操作控件。

---

### 2.4.3 模块回调：所有模块运行结束的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：所有模块运行结束就会进入的回调函数。

**原因 / 原理**
- 不熟悉所有模块运行结束的回调。注册 `OnModuleResultCallbackEvent`，在 `nStatus==1` 且 `nModuleID` 匹配时获取结果。

**解决步骤**
1. 注册 `OnModuleResultCallbackEvent`，判断 `nModuleID` 与 `nStatus==1`（模块运行成功）后获取结果。

**关键代码**
```csharp
//注册回调函数
VmSolution.OnModuleResultCallbackEvent += VmSolution_OnModuleResultCallbackEvent;
private void VmSolution_OnModuleResultCallbackEvent (ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data moduleResultExInfo)
{
    if (moduleResultExInfo.nModuleID == moduleID )//判断模块Id
    {
        if (moduleResultExInfo.nStatus == 1)//判断模块状态，1表示模块运行成功
        {
            //获取结果
        }
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`VmSolution.OnModuleResultCallbackEvent`
- 结构：`ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data`
- 字段：`nModuleID`、`nStatus`（1=成功）

**注意事项 / 坑**
- `nStatus==1` 表示模块运行成功。

---

### 2.4.4 加密狗回调：获取加密狗状态的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何获取加密狗编号。

**原因 / 原理**
- 不熟悉如何获取加密狗编号，从而判断是否插了加密狗。通过 `OnDongleCallBack` 事件，`nDongleStatus==0` 表示正常，`strDongleType` 为编号。

**解决步骤**
1. 建立 `ServerSDKManager...OnDongleCallBack` 事件，处理 `moduleInfo`：`nDongleStatus==0` 正常，否则提示未检测到加密狗；`strDongleType` 为加密狗编号。

**关键代码**
```csharp
ServerSDKManager.serverSDKManager.mSolutionManager.OnDongleCallBack += MSolutionManager_OnDongleCallBack;
private void MSolutionManager_OnDongleCallBack(ImvsSdkDefine.IMVS_DONGLE_INFO moduleInfo)
{
    if(moduleInfo.nDongleStatus == 0)//获取加密狗状态
    {
       string dogNum = System.Text.Encoding.Default.GetString(moduleInfo.strDongleType);//获取加密狗型号
    }
    else
    {
        MessageBox.Show("未检测到加密狗！");
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`ServerSDKManager.serverSDKManager.mSolutionManager.OnDongleCallBack`
- 结构：`ImvsSdkDefine.IMVS_DONGLE_INFO`
- 字段：`nDongleStatus`（0=正常）、`strDongleType`（编号）

**注意事项 / 坑**
- 用 `Encoding.Default.GetString` 解析 `strDongleType` 得到加密狗型号/编号。

---

### 2.4.5 方案加载：方案加载结束的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：方案加载结束进入的回调函数。

**原因 / 原理**
- 不熟悉方案加载结束的回调。建立 `OnSolutionLoadEndEvent`，`nStatus==0` 表示加载成功。

**解决步骤**
1. 建立 `VmSolution.OnSolutionLoadEndEvent`，判断 `nStatus==0`（方案空闲/加载成功）后插入相关函数。
2. 提示：方案含脚本/深度学习模块时第一次执行耗时长，可在加载成功后静默执行：`VmSolution.Instance.SilentExecute(true)`。

**关键代码**
```csharp
VmSolution.OnSolutionLoadEndEvent += VmSolution_OnSolutionLoadEndEvent;
//方案加载成功

private void VmSolution_OnSolutionLoadEndEvent
(ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO solutionLoadEndInfo)
{
    if (solutionLoadEndInfo.nStatus == 0)//0为方案加载成功
    {
       //这里可以插入相关函数
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`VmSolution.OnSolutionLoadEndEvent`
- 结构：`ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO`
- 字段：`nStatus`（0=成功/空闲，1=忙碌）
- 方法：`VmSolution.Instance.SilentExecute(true)`

**注意事项 / 坑**
- 含脚本/深度学习模块的方案，建议在加载成功后静默执行一次以预热。

---

### 2.4.6 模块回调：指定模块运行结束的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：指定模块，在运行结束后进入回调函数。

**原因 / 原理**
- 不熟悉指定模块运行结束的回调。对具体模块注册 `ModuleResultCallBackArrived`，模块每次执行都会进该回调（注意：目前模块回调非事件，无法快捷键补全）。

**解决步骤**
1. 注册 `module.ModuleResultCallBackArrived += ...`。
2. 在回调中 `sender` 即是模块实例，直接取 `ModuResult`。

**关键代码**
```csharp
IVmModule module = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
module.ModuleResultCallBackArrived += ModuleResultCallBackArrived;
```
```csharp
private void ModuleResultCallBackArrived(object sender ,EventArgs e)
{
   IMVSCircleFindModuTool circleFind = (IMVSCircleFindModuTool)sender;
   float x = circleFind.ModuResult.OutputCircle.Radius;
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 接口：`IVmModule`
- 事件：`ModuleResultCallBackArrived`
- 属性：`ModuResult.OutputCircle.Radius`

**注意事项 / 坑**
- 当前模块回调不是事件，无法快捷键自动补全，需手写函数签名。

---

### 2.4.7 模块回调：禁用模块结果回调的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：为了提高内存利用率，禁用不必要的模块结果回调。

**原因 / 原理**
- 不熟悉相关接口的使用。可全局禁用/启用模块回调，或按模块 ID 控制。

**解决步骤**
1. 禁用所有模块回调：`VmSolution.Instance.DisableModulesCallback()`。
2. 按模块 ID 控制：`CtrlCallBackModuResult(ID, 0)`（0=禁用，1=启用）。
3. 启用所有回调：`VmSolution.Instance.EnableModulesCallback()`。

**关键代码**
```csharp
//禁用所有模块的回调
VmSolution.Instance.DisableModulesCallback();
//控制方案中回调，ID指模块ID，0是禁用，1是启用
ServerSDKManager.serverSDKManager.mModuleManager.CtrlCallBackModuResult(ID,0);
//启用所有回调
VmSolution.Instance.EnableModulesCallback();
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`VmSolution`、`ServerSDKManager`
- 方法：`DisableModulesCallback()`、`EnableModulesCallback()`、`mModuleManager.CtrlCallBackModuResult(ID, 0/1)`

**注意事项 / 坑**
- 禁用后将无法获取该模块结果，按需启用。

---

### 2.4.8 通讯回调：通讯设备状态和接收数据的回调方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何获取通讯设备的状态是开启还是关闭？如何获取通讯数据。

**原因 / 原理**
- 不熟悉通讯相关的回调方法。通过 `OnCommunicationStatusCallBackEvent`（状态）与 `OnCommunicationRecvCallBackEvent`（接收数据）获取。

**解决步骤**
1. 获取通讯设备状态：注册 `OnCommunicationStatusCallBackEvent`，`btarr[0]` 为开关状态（1=开/0=关），`btarr[1]` 为设备 ID。
2. 获取通讯数据：注册 `OnCommunicationRecvCallBackEvent`，`btarr[0]` 为设备 ID，从 `btarr[2]` 开始为有效数据。

**关键代码**
```csharp
// 1. 获取通讯设备的状态
//注册回调
VmSolution.OnCommunicationStatusCallBackEvent += VmSolution_OnCommunicationStatusCallBackEvent;

private void VmSolution_OnCommunicationStatusCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
{
    int nType = reportDataInfo.nType;
    byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pData, reportDataInfo.nLen);
    int len = btarr.Length;
    string ID = btarr[1].ToString();//通讯设备ID
    string Open = btarr[0].ToString();//开关状态，1表示开，0表示关
}
```
```csharp
// 2. 获取通讯数据
//注册回调
VmSolution.OnCommunicationRecvCallBackEvent += VmSolution_OnCommunicationRecvCallBackEvent;
private void VmSolution_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
{
    string strMsg;
    try
    {
        int nType = reportDataInfo.nType;
        byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pData, reportDataInfo.nLen);
        int len = btarr.Length;
        string ID = btarr[0].ToString();
        byte[] vs = new byte[len - 2];
        Array.Copy(btarr, 2, vs, 0, len - 2);
        string ReceiveData = System.Text.Encoding.Default.GetString(vs);
        strMsg = ID + "号设备接受到：" + ReceiveData;
        Logger.WriteLog(LogLevel.INFO, strMsg);
    }
    catch (VmException ex)
    {
        strMsg = "读取通信数据失败. Error Code: " + Convert.ToString(ex.errorCode, 16);
        Logger.WriteLog(LogLevel.ERROR, strMsg);
        return;
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`VmSolution.OnCommunicationStatusCallBackEvent`、`VmSolution.OnCommunicationRecvCallBackEvent`
- 结构：`ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO`
- 字段：`nType`、`pData`、`nLen`
- 辅助：`ExternalCallHelper.IntPtr2Bytes`
- 日志：`Logger.WriteLog`、`LogLevel.INFO/ERROR`
- 异常：`VmException`（含 `errorCode`）

**注意事项 / 坑**
- 状态回调中 `btarr[0]`=开关、`btarr[1]`=设备ID；数据回调中 `btarr[0]`=设备ID，有效数据从索引 2 开始。

---

## 2.5 全局工具

### 2.5.1 全局相机：全局相机设置参数的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：全局相机一些参数如何设置或获取。

**原因 / 原理**
- 不熟悉全局相机的一些参数配置。连接状态需从图像源 `CameraName` 按 `$` 解析；触发源、曝光用 `GetParamValue` / `SetParamValue`。

**解决步骤**
1. 获取相机连接状态：只有图像源绑定相机里全局相机才可获取状态；读 `CameraName` 的 Value（如 `0$0$$$$Close`），按 `$` 分割取第一个，>0 已连接，=0 未连接。
2. 触发源获取/设置：枚举值 0=LINE0、1=LINE1、2=LINE2、3=LINE3、7=SOFTWARE。
3. 曝光获取/设置：`ExposureTime`。

**关键代码**
```csharp
ImageSourceModuleTool imageSourceModule = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
tring i = null;
imageSourceModule.ModuParams.GetParamValue("CameraName", ref i);
```
```csharp
GlobalCameraModuleTool globalTool = VmSolution.Instance["全局相机1"] as GlobalCameraModuleTool;
//获取
string strVal11 = "";
globalTool.ModuParams.GetParamValue("TriggerSource", ref strVal11);
//设置
globalTool.ModuParams.SetParamValue("TriggerSource", "7");
```
```csharp
GlobalCameraModuleTool tool = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"];
//获取
string strValue = "";
tool.ModuParams.GetParamValue("ExposureTime", ref strValue);
//设置
tool.ModuParams.SetParamValue("ExposureTime", "5000");
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`GlobalCameraModuleTool`、`ImageSourceModuleTool`
- 参数：`CameraName`（连接状态）、`TriggerSource`（0/1/2/3/7）、`ExposureTime`
- 方法：`ModuParams.GetParamValue` / `SetParamValue`

**注意事项 / 坑**
- 连接状态需按 `$` 拆分 `CameraName` 取首段判断。
- 触发源 `7` = SOFTWARE（软触发）。

---

### 2.5.2 全局相机：获取全局相机列表的方法

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：如何获取全局相机列表并给图像源设置指定相机。

**原因 / 原理**
- 相关接口在 VM4.0 尚未对外开放，后续版本（VM4.2）会开放出来。但仍可通过 `GetAllModuleList()` 过滤 `nModuleType==6` 获取相机列表。

**解决步骤**
1. 获取全局相机列表：通过 `ServerSDKManager...GetAllModuleList()`，遍历 `astModuleInfo`，`nModuleType==6` 即相机，取 `nNodeID` + `strDisplayName`。
2. 图像源模块设置相机：`SetParamValue("CameraID", "1")`。

**关键代码**
```csharp
// 全局相机下拉列表
private void vmGalobalCameraCombBox_DropDownOpened(object sender, EventArgs e)
{
    try
    {
        var moduleList = ServerSDKManager.serverSDKManager.mSolutionManager.GetAllModuleList();

        vmGalobalCameraCombBox.Items.Clear();
        if (moduleList.HasValue)
        {
            foreach (var item in moduleList.Value.astModuleInfo)
            {
                if (item.nModuleType == 6)
                {
                    string str = Encoding.UTF8.GetString(item.strDisplayName);
                    vmGalobalCameraCombBox.Items.Add(item.nNodeID.ToString() + " " + str);
                }
            }
        }
    }
    catch (VmException ex)
    {
        System.Windows.MessageBox.Show("获取相机列表失败！" + ex.ToString());
    }
}
```
```csharp
// 图像源绑定相机
private void BindingCamera_Click_1(object sender, RoutedEventArgs e)
{
    try
    {
        var imageSourceModuleTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
        imageSourceModuleTool.ModuParams.SetParamValue("CameraID","1");
        System.Windows.MessageBox.Show("绑定成功！");
    }
    catch (Exception ex)
    {
        System.Windows.MessageBox.Show("绑定失败！");
    }
}
```

**关键 API / 类名 / 命名空间 / 属性**
- 类：`ServerSDKManager`、`ImageSourceModuleTool`
- 方法：`mSolutionManager.GetAllModuleList()`
- 结构：`astModuleInfo`（字段 `nModuleType`、`nNodeID`、`strDisplayName`）
- 参数：`CameraID`
- 常量：`nModuleType == 6` 表示相机

**注意事项 / 坑**
- 原文注明：相关接口在 VM4.0 未对外开放，VM4.2 才开放。

---

### 2.5.3 全局通信：通信管理中设备开启状态管理

**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上。
- 现象：通信管理中设备开启状态和如何通过代码设置，如何通过回调获取开启状态。

**原因 / 原理**
- （原文在「解答」处结束，PDF 分片截断，文字/图示缺失）通信管理设备开启状态可通过代码设置，并通过回调获取开启状态（参见 2.4.8 的 `OnCommunicationStatusCallBackEvent`）。

**解决步骤**
1. （原文解答缺失）可参考 2.4.8 通讯状态回调 `OnCommunicationStatusCallBackEvent` 获取设备开关状态；通过方案/通信管理相关接口设置设备开启状态。

**关键代码**
```csharp
// （原文为图示，文字缺失；PDF 分片在解答处结束）
// 参考 2.4.8：VmSolution.OnCommunicationStatusCallBackEvent 获取设备开关（btarr[0]: 1=开/0=关）
```

**关键 API / 类名 / 命名空间 / 属性**
- 事件：`VmSolution.OnCommunicationStatusCallBackEvent`（参考 2.4.8）
- 结构：`ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO`

**注意事项 / 坑**
- 本条解答在源 PDF 分片中被截断（页 386 结束），原文图示与文字缺失，建议以 2.4.8 通讯回调方案为准。

---

## 条目索引

2.1.1 环境配置：CSharp 二次开发环境配置方法
2.1.2 环境配置：Qt 二次开发环境配置方法
2.1.3 环境配置：MFC 二次开发环境配置方法
2.1.4 环境配置：VB.Net 二次开发环境配置方法
2.1.5 环境配置：运行出现 Vm.Core.Solution 报错的解决方法
2.1.6 模块索引：MFC 模块索引异常解决办法
2.1.7 环境配置：报错序列不包含任何元素的解决方法
2.1.8 环境配置：提示未注册 ActiveX 控件的解决方法
2.1.9 控件失效：VM 控件运行时不显示的解决方法
2.1.10 环境配置：Qt 开发环境出现 rc.exe 无法启动报错解决办法
2.1.11 控件失效：添加引用后导致控件失效的解决方法
2.1.12 添加引用：在原有项目中新配置深度学习环境的方法
2.1.13 用户权限：普通用户权限以 EXE 方式启动 Server 的方法
2.1.14 引用工具：使用引用工具添加引用报错的解决方法
2.1.15 环境配置：句柄创建失败解决问题排查方法
2.2.1 方案保存：方案高速保存的方法
2.2.2 Group 模块：Group 输入输出图像数据的方法
2.2.3 模块操作类：设置输入图像、参数和 ROI 的方法
2.2.4 图像源：通过图像源模块接口设置图像输入的方法
2.2.5 图像源：通过 SDK 传入相机图像的方法
2.2.6 输出图像：获取渲染图像数据的方法
2.2.7 N 点标定：清空标定点、生成标定文件和渲染轨迹的方法
2.2.8 耗时统计：流程与模块运行耗时的获取方法
2.2.9 资源释放：方案资源释放的方法
2.2.10 条件检测：条件检测模块设置范围的方法
2.2.11 流程ID：通过流程名获取流程ID 的方法
2.2.12 几何创建：绘制形状的方法
2.2.13 运行间隔：设置和获取流程运行间隔的方法
2.2.14 分支字符：控制调试模式开关的方法
2.2.15 模块禁用：模块禁用的方法
2.2.16 Group 循环：获取 Group 循环数据结果的方法
2.3.1 渲染结果：通过绑定流程或模块获取渲染结果的方法
2.3.2 渲染控件：渲染控件加载本地图像的方法
2.3.3 渲染控件：渲染控件上自定义图形的方法
2.3.4 参数控件：参数配置控件绑定模块的方法
2.3.5 控件颜色：控件颜色修改的方法
2.3.6 VM 嵌入：嵌入用户软件界面的方法
2.3.7 参数控件：隐藏参数设置控件上某些参数的方法
2.3.8 渲染控件：通过鼠标点击获取渲染控件像素坐标的方法
2.3.9 控件显示：控件显示所加载的流程的方法
2.3.10 前端界面控件：前端界面控件大小自适应的方法
2.3.11 渲染控件：渲染控件存图的方法
2.4.1 数据结果：通过流程输出或模块输出获取数据结果的方法
2.4.2 流程运行：所有流程运行结束的回调方法
2.4.3 模块回调：所有模块运行结束的回调方法
2.4.4 加密狗回调：获取加密狗状态的回调方法
2.4.5 方案加载：方案加载结束的回调方法
2.4.6 模块回调：指定模块运行结束的回调方法
2.4.7 模块回调：禁用模块结果回调的方法
2.4.8 通讯回调：通讯设备状态和接收数据的回调方法
2.5.1 全局相机：全局相机设置参数的方法
2.5.2 全局相机：获取全局相机列表的方法
2.5.3 全局通信：通信管理中设备开启状态管理
