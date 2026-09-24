<!-- source: 06-ch4-algo-module.md  pages 703-800 -->
# VM 算法模块开发 FAQ（第4章）

> 本文件提炼自 VisionMaster 官方 FAQ 文档第 4 章「算法模块开发」（PDF 第 703–800 页）。
> 覆盖：4.1 开发配置类（15 条）、4.2 联合 OpenCV 开发（2 条）、4.3 联合 Halcon 开发（1 条）。
> 说明：源片段到第 800 页的 4.3.1 末尾截止，**4.4 异常处理** 不在本输入文件内，故未编造，相关说明见文末「条目索引」。

## 本章速览

1. **算法模块标准开发流程**：算子生成器配置 → 生成 XML/C#/C++ 工程 → Release/x64 编译 → 拷贝到 `Module(sp)\x64\XX` 工具箱目录。
2. **参数分两类**：基本参数（输入/输出，界面可见/结果可见）用 `VM_M_Getxxxx / VM_M_Setxxxx`；运行参数（算法参数）用 `GetParam / SetParam`。
3. **参数类型** 6 种：int、float、string、byte、image、pointset。
4. **文件交互**：在 `***AlgorithmTab.xml` 的 `Tab_Basic Params` 中加 `OpenFileForCalibDialog`，底层用 `SetParam/GetParam` 读写路径；加 `Boolean RefreshFileEnable` 实现每次执行同步最新文件。
5. **输出显示**：在 `xxxxModu.xml` 配置输出参数（Visible=false 则不显示），C++ 用 `VM_M_Setxxxx` 赋值，`xxxxDisplay.xml` 配渲染 Mapping。
6. **模板配置界面**：算法模块生成器 → 数据源类 → `AlgorithmTab.xml` → 自定义控件 → DataTemplate → 弹出窗口 → 界面/底层 `IUserStringData / IUserBytesData` 数据交互。
7. **中文名**：用 `VisionMaster4.X.0\Applications\Lang\LanguageTool` 增加中英文资源（Key 查找 → 增/编辑）。
8. **无图像源**：注释 `xxxxModu.xml` 图像输入段，重载 `Process(IN void* hInput, IN void* hOutput)`（两参）。
9. **多图像源**：`xxxxModu.xml` + `xxxxAlgorithmTab.xml` 增 `ImageSource2` 枚举；重写 `GetInputImage` 用 `VmModule_GetInputImageByName` 取双图。
10. **断点调试**：VS「显示所有用户的进程」勾选，附加 `VmModuleProxy.exe`，代码类型选「本机」。
11. **点集参数**：输入/输出 pointset 子元素 float；`VM_M_GetFloat` 遍历获取，`VmModule_OutputVector_32f` 输出。
12. **直线参数**：输入直线起点/终点 float，用 `VM_M_GetFloat` 逐项获取。
13. **矩形参数**：输出 `RectCenterX/Y`、`RectWidth/Height`、`RectAngle`；图形显示依赖输出图像 + `Display.xml` Mapping。
14. **多 ROI**：`AlgorithmTab.xml` 的 `ROISelecter` 加 `DoubleBox`；`Process` 中 `dynamic_cast<IMvdRectangleF*>`；`ResetDefaultRoi` 屏蔽原码改多 Box。
15. **日志打印**：`MLOG_ERROR`/`LOG_ERROR`（VM4.3+），等级 ERROR>WARN>INFO>DEBUG>TRACE；日志落 `Applications\log\Module\对应模块名.log`。
16. **参数自执行**：`AlgorithmTab.xml` 的 `Tab_ROI Area` 节点加 `CanTriggerRun="TRUE"`。
17. **联合 OpenCV**：版本与 VS 工具集对应（VS2013→VC=120→OpenCV 3.1.0）；HKA_IMAGE ↔ Mat 互转。
18. **联合 Halcon**：用 `AlgorithmXMLGenerator` 生成 XML/C#/C++ 工程，C++ 工程 `Proj_<模块名>` 配 Halcon 包含/库/依赖项，封装 `DynThreshold` 等第三方算子入工具箱。

---

## 4.1 开发配置类

### 4.1.1 算法开发：算法模块的开发流程

**适用场景 / 目标**
图像类自定义算子模块从「算子生成器」到嵌入 VisionMaster 工具箱的完整标准流程，确保自研算法可作为标准工具拖拽使用。

**关键概念**
- **算子生成器**（AlgorithmXMLGenerator）：配置模块名、自定义输入/输出参数，生成 XML、C++ 工程、C# 工程。
- **三类产物**：XML 配置文件夹、C# 界面工程（编译出 `xxxcs.dll`）、C++ 算法工程（编译出算法 `dll`）。
- **部署目录**：`VisionMaster4.0.0\Applications\Module(sp)\x64\XX`（XX 为工具箱名，如 `Measurement`）。
- **编译选项**：C# 用 Release；C++ 用 Release、x64、禁用优化。

**实现步骤**
1. 打开算子生成器，配置算法模块名称、自定义输入输出参数，单击「下一步」。
2. 配置算法模块基本参数和运行参数，依次生成 XML、C++ 工程、C# 工程。
3. 打开生成的 C# 工程，选择 Release，编译生成 dll 并拷贝到 XML 文件夹。
4. 打开生成的 C++ 工程，选择 Release、x64，禁用优化。
5. 在 C++ 工程的 `AlgorithmModule.cpp` 的 `Process()` 函数中实现自定义算法。
6. 编译 C++ 工程，生成的 dll 拷贝到 XML 文件夹。
7. 将 XML 文件夹拷贝到 `VisionMaster4.0.0\Applications\Module(sp)\x64\XX`，即完成图像类算子模块的开发与嵌入。

**关键代码**
本条目为流程说明，无代码片段。

**关键 API / 接口 / 配置项 / 文件路径**
- 算子生成器（界面工具，VM 软件「工具」菜单下）。
- 部署路径：`VisionMaster4.0.0\Applications\Module(sp)\x64\XX`（例：`Measurement`）。
- 核心实现文件：`AlgorithmModule.cpp` → `Process()`。

**注意事项 / 坑**
- C++ 工程必须选 **Release + x64 + 禁用优化**，否则易与 VM 宿主运行环境不兼容或触发异常。
- XML 文件夹需同时包含 C# 生成的 `xxxcs.dll` 与 C++ 生成的算法 `dll`，缺一不可，否则模块无法加载或运行。

---

### 4.1.2 参数操作：获取与设置模块参数的方法

**适用场景 / 目标**
在算法模块开发中正确读写「基本参数」与「运行参数」两类参数，理解二者接口差异。

**关键概念**
- **基本参数**：含输入/输出参数。输入参数一般通过订阅方式获取；输出参数不在参数配置界面、而在 VM 右侧结果区显示。
- **运行参数**：即算法参数。
- **参数类型**：int、float、string、byte、image、pointset 六种。
- **接口差异**：
  - 基本参数：`VM_M_Getxxxx()` 获取，`VM_M_Setxxxx()` 输出。
  - 浮点数组可遍历，或一次性调用 `VmModule_GetInputVectorIndex_32f()` / `VmModule_OutputVector_32f()`。
  - 运行参数：在 `GetParam()` / `SetParam()` 中读写。
- **参数名来源**：`xxxxAlgorithmTab.xml`（参数配置界面）与 `xxxxModu.xml`（输入输出参数定义）。

**实现步骤**
1. 基本参数（输入/输出）用 `VM_M_Getxxxx / VM_M_Setxxxx`，索引 0 表示数组首元素。
2. 运行参数在 `Process()` 内（或 `GetParam/SetParam` 内）用 `GetParam/SetParam` 读写。
3. 参数名取自 `xxxxAlgorithmTab.xml` / `xxxxModu.xml`。

**关键代码**

```cpp
//运行函数
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput, IN MVDSDK_BASE_MODU_INPUT* modu_input)
{
    HKA_F32 fValue = 0;
    int nArrayCount = 0;
    int nRet = IMVS_EC_UNKNOWN;

    //从模块界面中拿到名为ImagePointA的数组中索引为0的浮点值
    nRet = VM_M_GetFloat(hInput, "ImagePointA", 0, &fValue, &nArrayCount);

    //将模块输出中名为ModuStatus的整型数组中索引为0的值设置为1
    VM_M_SetInt(hOutput, "ModuStatus", 0, 1);
}
```

```cpp
//运行函数
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput, IN MVDSDK_BASE_MODU_INPUT* modu_input)
{
    char pBuff[1024] = {1024};
    int pDataLen = 1024;

    //获取模块界面中名为threshold的运行参数的值
    GetParam("threshold", pBuff, sizeof(pBuff), &pDataLen);

    //获取到的值做转换
    int thresh = atoi(pBuff);

    //将模块中名为threshold的运行参数设置为240
    SetParam("threshold", "240", pDataLen);
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- `VM_M_GetFloat / VM_M_SetInt / VM_M_GetInt / VM_M_SetFloat …`
- `VmModule_GetInputVectorIndex_32f()`、`VmModule_OutputVector_32f()`
- `GetParam(name, pBuff, buffSize, &dataLen)`、`SetParam(name, pData, dataLen)`
- 参数名定义文件：`xxxxAlgorithmTab.xml`、`xxxxModu.xml`

**注意事项 / 坑**
- 基本参数与运行参数使用**不同**接口，混用会取不到值或写入无效。
- 数组型参数需先用索引 0 取得 `nArrayCount`（数组长度），再遍历读写。
- 参数名必须与对应 XML 文件中的 `Name` 严格一致（区分大小写）。

---

### 4.1.3 文件交互：文件交互操作的配置方法

**适用场景 / 目标**
自定义算子模块需要「在界面选择文件并加载」（如标定文件 `.xml/.iwcal`），并支持每次执行同步最新文件。

**关键概念**
- **配置文件**：`***AlgorithmTab.xml`（模块参数配置界面），在 `Name="Tab_Basic Params"` 的 Tab 内添加控件。
- **文件选择控件**：`<OpenFileForCalibDialog>`（含 `FileOption` 过滤、`IsMultiselect`）。
- **刷新使能**：`<Boolean Name="RefreshFileEnable">` 标志位，控制是否每次执行重新加载文件。
- **底层接口**：`SetParam` 取路径→`LoadFile` 读文件；`GetParam` 回传路径；`Process` 中据 `m_bRefreshFileEnable` 触发刷新。

**实现步骤**
1. 在 `***AlgorithmTab.xml` 的 `Tab_Basic Params` 添加 `OpenFileForCalibDialog` 控件（名称如 `CalibPathName`）。
2. 在 C++ 工程 `SetParam` 中 `strcmp("CalibPathName", szParamName)` 分支获取路径、`malloc(MAX_FILE_PATH)`、`memcpy_s` 拷贝、`LoadFile` 读取；`GetParam` 中 `sprintf_s` 回传路径。
3. 在 `Tab_Basic Params` 添加 `Boolean RefreshFileEnable` 控件；`SetParam` 据 `True/False` 置 `m_bRefreshFileEnable`，`GetParam` 回传状态。
4. 在 `Process` 中 `if (m_bRefreshFileEnable)` 触发重新 `SetParam("CalibPathName", ...)` 以同步最新文件。

**关键代码**

```xml
<OpenFileForCalibDialog Name="CalibPathName" NameSpace="Standard">
    <Description>Load Calib File Path</Description>
    <DisplayName>RunParam_Load Calibration File</DisplayName>
    <Visibility>Beginner</Visibility>
    <AccessMode>RW</AccessMode>
    <CurValue></CurValue>
    <DefaultValue></DefaultValue>
    <FileOption>
        <IsMultiselect>false</IsMultiselect>
        <FilterName>.xml|*.xml;*.iwcal</FilterName>
    </FileOption>
</OpenFileForCalibDialog>
```

```cpp
//SetParam 函数中加入以下代码来获取文件路径并设置到底层，选择路径时触发读取文件函数
else if (0 == strcmp("CalibPathName", szParamName))
{
    // m_chSaveCalibPathName 为char 型指针
    if (m_chSaveCalibPathName != NULL)
    {
        free(m_chSaveCalibPathName);
        m_chSaveCalibPathName = NULL;
    }
    //获取文件路径
    m_chSaveCalibPathName = (char*)malloc(MAX_FILE_PATH);
    memcpy_s(m_chSaveCalibPathName, MAX_FILE_PATH, pData, strlen(pData));
    //读取文件操作
    nErrCode = LoadFile(m_chSaveCalibPathName);
}
//GetParam 函数中加入以下代码来获取底层文件路径信息
else if (0 == strcmp("CalibPathName", szParamName))
{
    sprintf_s(pBuff, nBuffSize, "%s", m_chSaveCalibPathName);
}
```

```xml
<Boolean Name="RefreshFileEnable" NameSpace="Standard">
    <CurValue>False</CurValue>
    <DefaultValue>False</DefaultValue>
    <Description>RefreshFileEnable</Description>
    <DisplayName>RefreshFileEnable</DisplayName>
    <Visibility>Beginner</Visibility>
    <AccessMode>RW</AccessMode>
</Boolean>
```

```cpp
//SetParam 函数中加入以下代码来将更新文件使能设置到底层，更改状态时触发
else if (0 == strcmp("RefreshFileEnable", szParamName))
{
    if (0 == strncmp(pData, "True", strlen("True")))
    {
        m_bRefreshFileEnable = true;
    }
    else
    {
        m_bRefreshFileEnable = false;
    }
}
//GetParam 函数中加入以下代码来获取底层使能状态反馈给界面
else if (0 == strcmp("RefreshFileEnable", szParamName))
{
    if (m_bRefreshFileEnable)
    {
        sprintf_s(pBuff, nBuffSize, "%s", "True");
    }
    else
    {
        sprintf_s(pBuff, nBuffSize, "%s", "False");
    }
}
```

```cpp
//process 函数中添加触发代码
if (m_bRefreshFileEnable)
{
    m_calibPathName = m_chSaveCalibPathName;
    SetParam("CalibPathName", m_calibPathName.c_str(), m_calibPathName.length());
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- 控件：`OpenFileForCalibDialog`、`Boolean`、`Tab_Basic Params`。
- 属性：`NameSpace="Standard"`、`Visibility="Beginner"`、`AccessMode="RW"`、`FileOption/IsMultiselect`、`FilterName`。
- C++：`SetParam`、`GetParam`、`LoadFile`、`malloc(MAX_FILE_PATH)`、`memcpy_s`、`sprintf_s`、`m_bRefreshFileEnable`。

**注意事项 / 坑**
- 仅配置 `OpenFileForCalibDialog` 只能选路径；若不加重 `RefreshFileEnable` + `Process` 触发逻辑，每次执行**不会**自动同步最新文件。
- 路径指针 `m_chSaveCalibPathName` 需先 `free` 再 `malloc`，避免内存泄漏/悬垂指针。
- 界面示意（原文为图示，文字缺失）；`FilterName` 决定文件选择对话框过滤类型。

---

### 4.1.4 输出显示：设置输出并显示在VM 界面的方法

**适用场景 / 目标**
将模块计算结果数值与图形（直线、卡尺框、ROI、文本等）渲染显示在 VM 图像窗口与结果区。

**关键概念**
- **`xxxxModu.xml`**：定义输出参数名称与类型，一一对应 VM 运行后数据结果；属性 `Visible="false"` 或注释该参数 → 不在界面显示。
- **`VM_M_Setxxxx`**：在 `Process` 中设置输出值。
- **`xxxxDisplay.xml`**：配置渲染 Mapping，每项 `Mapping` 映射到某输出值；支持「Show Text」在图像区显示文本。
- 直线查找模块典型 Display 项：`InputImage`(图像)、`Line Result`/`Through Line`(直线/贯穿线)、`Contour Point`(边缘点)、`CaliperBox`/`DetectCaliperBox`(卡尺框)、`ROI`(检测区)、`Fixtured Point`(基准点)、`Unfixtured Point`(运行点)、`Data Record`(历史)、`Result List`(当前)、`ExternROI`(屏蔽区)。

**实现步骤**
1. 在 `xxxxModu.xml` 配置要输出的参数名称和类型；不需要显示的设 `Visible="false"` 或注释。
2. 在 C++ 工程 `Process` 中用 `VM_M_Setxxxx()` 设置输出参数值。
3. 通过 `xxxxDisplay.xml` 的 `Mapping` 将输出渲染到图像（文本用 `<Show Text>`）。
4. 修改 `Display.xml` 后需重新拖拽模块到流程（否则不生效）。

**关键代码**

```cpp
//c++设置模块状态
VM_M_SetInt(hOutput, "ModuStatus", 0, 1);
```

**关键 API / 接口 / 配置项 / 文件路径**
- 配置：`xxxxModu.xml`（`Visible` 属性）、`xxxxDisplay.xml`（`Mapping`、`Show Text`）。
- 接口：`VM_M_SetInt / VM_M_SetFloat …`
- 提示：界面显示内容可参考已有模块的同名 XML 配置。

**注意事项 / 坑**
- 修改 `Display.xml` 后**必须重新拖拽模块**到流程并执行，原流程实例不会自动生效。
- 图形显示（如文本、检测框）依赖模块**输出图像**；若模块无图像输出，需在 `Display.xml` 中先做图像输出映射。

---

### 4.1.5 模板配置：模板配置界面的实现方法

**适用场景 / 目标**
开发模板匹配等需要「建模配置界面」的模块，实现自定义弹出窗口与底层数据双向交互。

**关键概念**
- **算法模块生成器**：配置建模参数（速度尺度、特征尺度等）。
- **数据源类**：`IUserStringData` / `IUserBytesData` 用于界面<->底层数据交换。
- **`AlgorithmTab.xml`**：配置参数界面。
- **WPF 控件**：新建参数配置界面模板控件 → 应用到 `DataTemplate` → 新建模板配置弹出窗口。
- **底层接口**：`AlgorithmModule.cpp` 的 `GetParam`（取界面参数）、`SetParam`（建模及参数处理）。

**实现步骤**
1. 在算法模块生成器中配置建模配置参数（速度尺度、特征尺度等）。
2. 定义数据源类。
3. 配置 `AlgorithmTab.xml`。
4. 新建参数配置界面模板控件。
5. 将新建控件应用于 `DataTemplate`。
6. 新建模板配置弹出窗口。
7. 实现建模界面与算法底层数据交互。
   - 界面数据传给底层：通过 `(paramsConfig as IUserStringData)[...]` / `(paramsConfig as IUserBytesData)[...]`。
   - 底层数据传给界面：同样经 `IUserStringData` / `IUserBytesData` 读回。
   - 底层获取界面数据：在 `GetParam` 中获取；建模处理在 `SetParam` 中。

**关键代码**

```csharp
//1)界面数据传给底层
(paramsConfig as IUserStringData)["SetImageWidth"] = model.ImageWidth.ToString(); //int
(paramsConfig as IUserStringData)["TextBoxMsg"] = textMsg; //string
(paramsConfig as IUserBytesData)["SetImageData"] = model.ImageBuffer; //byte[]

//2)底层数据传给界面
int ImageWidth = int.Parse((paramsConfig as IUserStringData)["GetImageWidth"]); //int
byte[] ImageBuffer = (paramsConfig as IUserBytesData)["GetImageData"]; //byte[]
byte[] roiBuffer = (paramsConfig as IUserBytesData)["GetRoiData"]; //byte[]

//3)底层获取界面数据并处理
//在AlgorithmModule.cpp 的GetParam 函数中获取界面参数。
//在AlgorithmModule.cpp 的SetParam 函数中进行建模及参数处理。
```

**关键 API / 接口 / 配置项 / 文件路径**
- 接口：`IUserStringData`、`IUserBytesData`、`GetParam`、`SetParam`。
- 配置：`AlgorithmTab.xml`、`DataTemplate`、参数配置界面模板控件、模板配置弹出窗口。
- 运行效果（原文为图示，文字缺失）。

**注意事项 / 坑**
- 界面与底层数据交互必须成对实现「界面→底层」与「底层→界面」，否则建模参数不回显或算法读不到配置。
- 自定义 WPF 控件需正确挂到 `DataTemplate`，并注意 VM 宿主为 WPF，自定义控件若用 WinForm 需了解 `WindowsFormsHost` 嵌入方式（详见 3.4 图形/鼠标事件章节）。

---

### 4.1.6 命名翻译：自定义模块在VM 界面显示中文的方法

**适用场景 / 目标**
为自定义算法模块添加中/英文名称资源，使模块在 VM 工具箱中显示中文。

**关键概念**
- **LanguageTool**：位于 `VisionMaster4.X.0\Applications\Lang`，用于管理中英文资源。
- 通过「Key 查找资源」输入模块名称，添加中文值、英文值，点「增加/编辑」。

**实现步骤**
1. 使用 `VisionMaster4.X.0\Applications\Lang` 中 `LanguageTool` 工具，给算法模块增加中英文资源：在「通过 Key 查找资源」中输入模块名称，下方分别添加模块中文值（中文名称）和英文值（英文名称），最后点「增加/编辑」按钮。
2. 重新打开 VM，模块中文名添加成功。

**关键代码**
本条目为工具操作，无代码片段。

**关键 API / 接口 / 配置项 / 文件路径**
- 工具：`VisionMaster4.X.0\Applications\Lang\LanguageTool`
- 资源键：模块名称（Key）；值：中文名称、英文名称。

**注意事项 / 坑**
- 修改语言资源后需**重启 VM** 才生效。
- 模块名称（Key）需与 `xxxxModu.xml` / `xxxxAlgorithmTab.xml` 中的模块名一致，否则匹配不到。

---

### 4.1.7 无图像源：算法模块无输入图像的方法

**适用场景 / 目标**
算法模块不需要图像输入（如纯数值/逻辑运算模块）时的改造方法。

**关键概念**
- **XML 注释**：注释 `xxxxModu.xml` 中图像输入部分，参数配置窗口即无图像输入项。
- **Process 重载**：去掉 `modu_input` 第三参，仅保留 `(hInput, hOutput)` 两参。

**实现步骤**
1. 修改 `xxxxModu.xml`，注释图像输入部分，使界面无输入图像项。
2. 修改 C++ 代码，重载 `Process` 函数（两参版本）。

**关键代码**

```cpp
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput) //模块无输入图片时
{
    int nRet = IMVS_EC_OK;
    //......
    //......
    //......
    return IMVS_EC_OK;
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- 配置：`xxxxModu.xml`（图像输入段注释）。
- 接口：`Process(IN void* hInput, IN void* hOutput)`。

**注意事项 / 坑**
- `Process` 重载签名必须与 XML 是否含图像输入保持一致；若 XML 仍声明图像输入却用两参 `Process`，会导致加载/运行异常。

---

### 4.1.8 多图像源：算法模块输入多幅图像的方法

**适用场景 / 目标**
默认模块仅支持单幅图像输入；本条目说明如何扩展到双目（多幅）图像输入，例如双目视觉算法。

**关键概念**
- **界面 XML 修改**：在 `模块名.xml` 图像输入部分增加「图像输入源2」（图像名、宽、高、像素格式均需重命名）；`模块名AlgorithmTab.xml` 的「图像输入」Category 增加 `ImageSource2` 枚举。
- **OperationParams 一致性**：`AlgorithmTab.xml` 中 `OperationParams` 必须与 `模块名.xml` 中 `Filter Name` 一致（源1=`InputImage`，源2=`InputImage2`）。
- **底层取图**：标准 Demo 的 `GenerateImage` 取单图，需重写为 `GetInputImage`（取两幅），调用 `VmModule_GetInputImageByName`。

**实现步骤**
1. 界面区别：单目视图与双目视图基本参数界面不同（原文为图示，文字缺失）。
2. 界面 XML 修改：
   - `模块名.xml` 图像输入部分增图像输入源2（名自定义，图像名/宽/高/像素格式重命名）。
   - `模块名AlgorithmTab.xml` 将「图像输入」Category 改为含 `ImageSource` 与 `ImageSource2` 两个 `EnumerationG`（见下代码）。
3. 底层算法代码修改：重写 `GetInputImage` 取两幅 `HKA_IMAGE`，在 `Process` 调用；若基类无 `VmModule_GetInputImageByName`，将其复制到 `VmModule_IO.cpp`。

**关键代码**

```xml
<Category Name="图像输入">
    <Items>
        <EnumerationG Name="ImageSource">
            <Description>Input Source 1</Description>
            <DisplayName>RunParam_Input Source 1</DisplayName>
            <Visibility>Beginner</Visibility>
            <AccessMode>O</AccessMode>
            <Triggers>
                <Trigger>
                    <Property>CurValue</Property>
                    <Setters>
                        <Setter>
                            <OperationName>SetCombinationSourceOperation</OperationName>
                            <OperationParams>InputImage</OperationParams>
                        </Setter>
                    </Setters>
                </Trigger>
            </Triggers>
            <Initers>
                <Setter>
                    <TargetName>EnumEntrys</TargetName>
                    <OperationName>GetFrontParamItemsOperation</OperationName>
                    <OperationParams>IMAGE</OperationParams>
                </Setter>
                <Setter>
                    <TargetName>CurValue</TargetName>
                    <OperationName>GetSelectedCombinationOperation</OperationName>
                    <OperationParams>InputImage</OperationParams>
                </Setter>
            </Initers>
        </EnumerationG>
        <EnumerationG Name="ImageSource2">
            <Description>Input Source 2</Description>
            <DisplayName>RunParam_Input Source 2</DisplayName>
            <Visibility>Beginner</Visibility>
            <AccessMode>O</AccessMode>
            <Triggers>
                <Trigger>
                    <Property>CurValue</Property>
                    <Setters>
                        <Setter>
                            <OperationName>SetCombinationSourceOperation</OperationName>
                            <OperationParams>InputImage2</OperationParams>
                        </Setter>
                    </Setters>
                </Trigger>
            </Triggers>
            <Initers>
                <Setter>
                    <TargetName>EnumEntrys</TargetName>
                    <OperationName>GetFrontParamItemsOperation</OperationName>
                    <OperationParams>IMAGE</OperationParams>
                </Setter>
                <Setter>
                    <TargetName>CurValue</TargetName>
                    <OperationName>GetSelectedCombinationOperation</OperationName>
                    <OperationParams>InputImage2</OperationParams>
                </Setter>
            </Initers>
        </EnumerationG>
    </Items>
</Category>
```

```cpp
/// <summary>
/// 获取两幅输入图像(HKA_IMAGE)
/// </summary>
/// <param name="hInput">输入体指针</param>
/// <returns></returns>
int CAlgorithmModule::GetInputImage(IN void* hInput, bool &bCamera1, bool &bCamera2, HKA_IMAGE struInputImg[2])
{
    HKA_S32             nRet = IMVS_EC_UNKNOWN;
    HKA_U32             nImageStatus = 0;

    do
    {
        nRet = VmModule_GetInputImageByName(hInput,
            "InImage",
            "InImageWidth",
            "InImageHeight",
            "InImagePixelFormat",
            &struInputImg[0],
            &nImageStatus);
        HKA_CHECK_BREAK(IMVS_EC_OK != nRet);
        bCamera1 = true;
    } while (0);

    do
    {
        nRet = VmModule_GetInputImageByName(hInput,
            "InImage2",
            "InImage2Width",
            "InImage2Height",
            "InImage2PixelFormat",
            &struInputImg[1],
            &nImageStatus);
        HKA_CHECK_BREAK(IMVS_EC_OK != nRet);
        bCamera2 = true;
    } while (0);

    return nRet;
}
```

```cpp
//获取输入的两张图片
bool bCamera1 = false;
bool bCamera2 = false;
HKA_IMAGE struInputImg[2];
int nRet = GetInputImage(hInput, bCamera1, bCamera2, struInputImg);
if (!bCamera1 && !bCamera2)
{
    //两个图片都没有,返回错误
    return IMVS_EC_MODULE_SUB_RST_NOT_FOUND;
}
if (IMVS_EC_OK != nRet)
{
    return IMVS_EC_MODULE_INPUT_NOT_FOUND;
}
```

```cpp
HKA_S32 VmModule_GetInputImageByName(IN const void * const hInput,
                                     char          *strImage,
                                     char          *strWidth,
                                     char          *strHeight,
                                     char          *strFormat,
                                     HKA_IMAGE     *image,
                                     HKA_U32       *imageStatus)
{
    HKA_S32          nRet          = IMVS_EC_UNKNOWN;
    HKA_S32          format        = 0;
    HKA_IMAGE_FORMAT formatAlg     = HKA_IMG_MONO_08;
    HKA_U32          nStatusImage  = IMVS_MODU_ENUM_STATUS_ERROR;
    HKA_U32          nStatusWidth  = IMVS_MODU_ENUM_STATUS_ERROR;
    HKA_U32          nStatusHeight = IMVS_MODU_ENUM_STATUS_ERROR;
    HKA_U32          nStatusFormat = IMVS_MODU_ENUM_STATUS_ERROR;
    char*            addr          = 0;

    HKA_CHECK_ERROR(HKA_NULL == hInput,      IMVS_EC_PARAM);
    HKA_CHECK_ERROR(HKA_NULL == image,       IMVS_EC_PARAM);
    HKA_CHECK_ERROR(HKA_NULL == imageStatus, IMVS_EC_PARAM);

    nRet = VmModule_GetInputImageAddress(hInput, strImage, &addr, &nStatusImage);
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

    nRet = VmModule_GetInputScalar_32i(hInput, strWidth, &(image->width), &nStatusWidth);
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

    nRet = VmModule_GetInputScalar_32i(hInput, strHeight, &(image->height), &nStatusHeight);
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

    nRet = VmModule_GetInputScalar_32i(hInput, strFormat, &format, &nStatusFormat);
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

    if(image->height <= 0)
    {
        nStatusHeight = IMVS_MODU_ENUM_STATUS_INPUT_INVALID;
    }

    if(image->width <= 0)
    {
        nStatusWidth = IMVS_MODU_ENUM_STATUS_INPUT_INVALID;
    }

    *imageStatus =   (IMVS_MODU_ENUM_STATUS_OK == nStatusImage)
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusWidth)
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusHeight)
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusFormat);

    nRet = VmModule_iMVSFormatToAlgFormat(format, &formatAlg);
    HKA_CHECK_ERROR(HKA_TRUE != nRet, nRet);

    image->format  = formatAlg;
    image->data[0] = addr;
    image->step[0] = (HKA_IMG_RGB_RGB24_C3 == formatAlg) ? (3 * image->width) : image->width;

    return IMVS_EC_OK;
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- XML：`EnumerationG`、`SetCombinationSourceOperation`、`GetFrontParamItemsOperation`、`GetSelectedCombinationOperation`、`OperationParams=IMAGE`。
- C++：`VmModule_GetInputImageByName`、`VmModule_GetInputImageAddress`、`VmModule_GetInputScalar_32i`、`VmModule_iMVSFormatToAlgFormat`、`HKA_CHECK_BREAK`、`HKA_CHECK_ERROR`、`IMVS_MODU_ENUM_STATUS_*`、`HKA_IMAGE`、`HKA_IMAGE_FORMAT`。
- 文件：`VmModule_IO.cpp`（基类取图实现位置）。

**注意事项 / 坑**
- `OperationParams` 必须与 `模块名.xml` 中 `Filter Name` 严格一致，否则图像源下拉为空或取图失败。
- 第二幅图命名（`InImage2/InImage2Width/...`）需与 XML 中 `ImageSource2` 的 `OperationParams` 对应。
- 若基类未提供 `VmModule_GetInputImageByName`，需手动把该函数复制到 `VmModule_IO.cpp` 并确认 `HKA_IMAGE` 字段（`width/height/format/data[0]/step[0]`）正确赋值。

---

### 4.1.9 断点调试：附加断点调试的注意事项

**适用场景 / 目标**
对自定义算法模块 C++ 工程进行 VS 附加进程断点调试，定位运行期问题。

**关键概念**
- **调试进程**：`VmModuleProxy.exe`（VM 加载自定义模块的实际宿主进程）。
- **附加选项**：勾选「显示所有用户的进程」，代码类型选「本机」。

**实现步骤**
1. 勾选「显示所有用户的进程」，进程选择 `VmModuleProxy.exe`。
2. 附加代码类型选择「本机」。

**关键代码**
本条目为调试配置，无代码片段。

**关键 API / 接口 / 配置项 / 文件路径**
- 进程：`VmModuleProxy.exe`
- VS 附加设置：「显示所有用户的进程」、代码类型「本机」。

**注意事项 / 坑**
- 必须勾选「显示所有用户的进程」，否则在进程列表里看不到 `VmModuleProxy.exe`。
- 代码类型选「本机」（Native），不可选托管/仅托管，否则断点不命中（C++ 算法工程为 native 编译）。
- 环境兼容：VM4.0 及 VM4.2 + VS2013。

---

### 4.1.10 点集参数：点集输入、输出实现方法

**适用场景 / 目标**
自定义模块获取输入点集、输出点集，扩展到几何基元拟合等算法领域（pointset 类型）。

**关键概念**
- **参数类型**：pointset，子元素类型均为 float（如 `ImagePointPointX/Y`、`WorldPointPointX/Y`）。
- **数组容量宏**：`MVBCALIBTRANS_MAX_POINT_NUM` 定义点集最大点数。
- **接口**：`VM_M_GetFloat` 遍历获取；`VmModule_OutputVector_32f` 一次性输出 float 数组。

**实现步骤**
1. 在算法模块生成器的自定义输入输出中配置输入点集、输出点集参数（编译并拷贝到工具箱，效果原文为图示，文字缺失）。
2. 在 `AlgorithmModule.h` 定义输入/输出点集数组变量（X/Y 像素、X/Y 物理）。
3. 在 `Process()` 中用 `VM_M_GetFloat` 遍历获取输入点集（先索引0取 `nArrayCount`，再逐点取 X、Y，校验 X/Y 数量一致）。
4. 对输入点集处理，给输出点集数组赋值。
5. 用 `VmModule_OutputVector_32f` 设置点集输出（配合 `VM_M_SetInt("ModuStatus",0,1)`）。

**关键代码**

```cpp
// AlgorithmModule.h 中定义输入、输出点集数组变量
#define MVBCALIBTRANS_MAX_POINT_NUM                         (100000)

HKA_F32  m_fImagePointX[MVBCALIBTRANS_MAX_POINT_NUM];    // 像素坐标X
HKA_F32  m_fImagePointY[MVBCALIBTRANS_MAX_POINT_NUM];    // 像素坐标Y
HKA_F32  m_fWorldPointX[MVBCALIBTRANS_MAX_POINT_NUM];    // 物理坐标X
HKA_F32  m_fWorldPointY[MVBCALIBTRANS_MAX_POINT_NUM];    // 物理坐标Y
```

```cpp
// AlgorithmModule.cpp 的 Process() 中获取输入点集
int nRet = IMVS_EC_UNKNOWN;
HKA_CHECK_ERROR((IMVS_NULL == hInput || IMVS_NULL == hOutput), IMVS_EC_PARAM);

HKA_F32 fValue = 0;
int nCount = 0;
int nArrayCount = 0;        // 数组大小
int pointXCount = 0;        // X 坐标数组大小
int pointYCount = 0;        // Y 坐标数组大小

// 获取输入点集
nRet = VM_M_GetFloat(hInput, "ImagePointPointX", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    for (int i = 0; i<nArrayCount; ++i)
    {
        nRet = VM_M_GetFloat(hInput, "ImagePointPointX", i, &fValue, &nArrayCount);
        if (IMVS_EC_OK != nRet)
        {
            break;
        }
        m_fImagePointX[i] = fValue;
    }
    pointXCount = nArrayCount;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

nRet = VM_M_GetFloat(hInput, "ImagePointPointY", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    for (int i = 0; i<nArrayCount; ++i)
    {
        nRet = VM_M_GetFloat(hInput, "ImagePointPointY", i, &fValue, &nArrayCount);
        if (IMVS_EC_OK != nRet)
        {
            break;
        }
        m_fImagePointY[i] = fValue;
    }
    pointYCount = nArrayCount;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

HKA_MODU_CHECK_ERROR((pointXCount != pointYCount), IMVS_EC_PARAM);
```

```cpp
// 输出物理点
for (int i = 0; i < pointXCount; ++i)
{
   m_fWorldPointX[i] = m_fImagePointX[i] + 400;
   m_fWorldPointY[i] = m_fImagePointY[i] + 500;
}
```

```cpp
// 设置点集输出
if (IMVS_EC_OK == nRet)
{
    VM_M_SetInt(hOutput, "ModuStatus", 0, 1);        // 模块状态
    int nProcessStatus = 1;                            // 1 表示模块正常，0 表示模块异常
    nRet = VmModule_OutputVector_32f(hOutput, nProcessStatus, m_fWorldPointX, "WorldPointPointX", nArrayCount);
    HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

    nRet = VmModule_OutputVector_32f(hOutput, nProcessStatus, m_fWorldPointY, "WorldPointPointY", nArrayCount);
    HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);
}
else
{
    VM_M_SetInt(hOutput, "ModuStatus", 0, 0);
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- 接口：`VM_M_GetFloat`、`VM_M_SetInt`、`VmModule_OutputVector_32f`、`HKA_MODU_CHECK_ERROR`、`HKA_CHECK_ERROR`。
- 参数名：`ImagePointPointX/Y`、`WorldPointPointX/Y`、`ModuStatus`。

**注意事项 / 坑**
- 必须先以索引 0 调用 `VM_M_GetFloat` 取得 `nArrayCount`（实际数组长度），再遍历；不要直接按 `#define` 上限遍历，否则越界。
- X、Y 坐标数组长度必须一致（`pointXCount != pointYCount` 视为参数错误）。
- 输出数组名（`WorldPointPointX/Y`）需与 `xxxxModu.xml` 中输出 pointset 子元素名一致。

---

### 4.1.11 直线参数：获取输入直线的方法

**适用场景 / 目标**
自定义模块获取输入直线（起点/终点），扩展到直线边缘缺陷检测等算法领域（环境 VM4.2+）。

**关键概念**
- 输入直线参数类型 float，子元素为 `lineStartPX/PY`、`lineEndPX/PY`（起点X/Y、终点X/Y）。
- 参数名从 `模块.xml` 查看。

**实现步骤**
1. 在算法模块生成器的自定义输入输出中配置输入直线参数（编译拷贝到工具箱后，模块界面原文为图示，文字缺失）。
2. 在 `AlgorithmModule.h` 定义直线起点/终点变量。
3. 在 `Process()` 中用 `VM_M_GetFloat` 逐项获取 `lineStartPX/PY`、`lineEndPX/PY`。

**关键代码**

```cpp
// AlgorithmModule.h 中定义输入直线的起点、终点变量
float lineStartPX;
float lineStartPY;
float lineEndPX;
float lineEndPY;
```

```cpp
// AlgorithmModule.cpp 的 Process() 中获取输入直线数据
int nRet = IMVS_EC_UNKNOWN;
HKA_CHECK_ERROR((IMVS_NULL == hInput || IMVS_NULL == hOutput), IMVS_EC_PARAM);

HKA_F32 fValue = 0;
int nArrayCount = 0;

nRet = VM_M_GetFloat(hInput, "lineStartPX", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    lineStartPX = fValue;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

VM_M_GetFloat(hInput, "lineStartPY", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    lineStartPY = fValue;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

VM_M_GetFloat(hInput, "lineEndPX", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    lineEndPX = fValue;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);

VM_M_GetFloat(hInput, "lineEndPY", 0, &fValue, &nArrayCount);
if (IMVS_EC_OK == nRet && nArrayCount > 0)
{
    lineEndPY = fValue;
}
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet);
```

**关键 API / 接口 / 配置项 / 文件路径**
- 接口：`VM_M_GetFloat`、`HKA_MODU_CHECK_ERROR`、`HKA_CHECK_ERROR`。
- 参数名：`lineStartPX`、`lineStartPY`、`lineEndPX`、`lineEndPY`。

**注意事项 / 坑**
- 直线参数子元素均为 float，参数名必须与 `模块.xml` 中一致。
- 每次 `VM_M_GetFloat` 后建议 `HKA_MODU_CHECK_ERROR` 校验，避免后续逻辑用脏值。

---

### 4.1.12 矩形参数：输出和显示矩形检测框的方法

**适用场景 / 目标**
自定义模块输出并图形显示矩形检测框，扩展到深度学习目标检测等算法领域（环境 VM4.2+）。

**关键概念**
- 输出矩形参数类型 float：`RectCenterX/Y`、`RectWidth/Height`、`RectAngle`（中心X/Y、宽、高、角度）。
- 图形显示依赖模块**输出图像**，需配 `Display.xml` 的 `Mapping`。

**实现步骤**
1. 在算法模块生成器自定义输入输出中配置矩形框输出参数（编译拷贝到工具箱，界面原文为图示，文字缺失）。
2. 在 `Process()` 中用 `VM_M_SetFloat` 输出单个或多个矩形框（索引区分）。
3. 若需在图像图层显示，先让模块输出图像（参见 4.1.4 / FAQ 专题篇 1.4）。
4. 打开 `Display.xml` 添加矩形框输出并设 `Mapping`（运行效果原文为图示，文字缺失）。

**关键代码**

```cpp
//输出矩形框1
VM_M_SetFloat(hOutput, "RectCenterX", 0, 50);
VM_M_SetFloat(hOutput, "RectCenterY", 0, 50);
VM_M_SetFloat(hOutput, "RectWidth",   0, 50);
VM_M_SetFloat(hOutput, "RectHeight",  0, 50);
VM_M_SetFloat(hOutput, "RectAngle",   0, 10);

//输出矩形框2
VM_M_SetFloat(hOutput, "RectCenterX", 1, 150);
VM_M_SetFloat(hOutput, "RectCenterY", 1, 150);
VM_M_SetFloat(hOutput, "RectWidth",   1, 150);
VM_M_SetFloat(hOutput, "RectHeight",  1, 150);
VM_M_SetFloat(hOutput, "RectAngle",   1, 20);
```

**关键 API / 接口 / 配置项 / 文件路径**
- 接口：`VM_M_SetFloat`。
- 配置：`xxxxModu.xml`（矩形框输出参数）、`xxxxDisplay.xml`（矩形框 `Mapping`）。
- 参数名：`RectCenterX/Y`、`RectWidth`、`RectHeight`、`RectAngle`。

**注意事项 / 坑**
- 矩形图形显示**依赖模块输出图像**；纯数值输出不会在图像上画框，需按 4.1.4 同时输出图像并在 `Display.xml` 做 `Mapping`。
- 多矩形框用索引（0、1…）区分，索引需与 `Display.xml` 中 `Mapping` 对应。

---

### 4.1.13 多ROI：获取多个ROI 的方法

**适用场景 / 目标**
自研模块获取多个 ROI（如双矩形框），封装类似 BLOB、边缘交点、矩形查找等模块（环境 VM4.0.0+）。

**关键概念**
- **ROISelecter 节点**：在 `模块名AlgorithmTab.xml` 的 `ROISelecter` 的 `ROISelection` 属性添加 ROI 类型（如 `DoubleBox` 双矩形框）。
- **`modu_input->vtFixRoiShapeObj`**：界面绘制 ROI 的几何对象容器，用 `dynamic_cast<IMvdRectangleF*>` 取矩形。
- **`ResetDefaultRoi`**：在 `VmAlgModuBase.cpp` 中屏蔽原码，改设定默认多 ROI（`IMVS_ROI_BOX`、`IMVS_ROI_TYPE_BOX`）。

**实现步骤**
1. 在 `模块名AlgorithmTab.xml` 的 `ROISelecter` 节点，`ROISelection` 属性添加 `DoubleBox`（双矩形框）；拖拽模块到流程区效果原文为图示，文字缺失。
2. 在 `AlgorithmModule.cpp` 的 `Process()` 中获取界面绘制的多 ROI（`vtFixRoiShapeObj.size()==2` 时逐个 `dynamic_cast`）。
3. 在 `VmAlgModuBase.cpp` 的 `ResetDefaultRoi()` 屏蔽原有代码，改为写入两个 `IMVS_ROI_BOX`（含角度），并设 `iRoiTypeIndex = IMVS_ROI_TYPE_BOX`。

**关键代码**

```cpp
// 获取界面绘制的多ROI
if (modu_input->vtFixRoiShapeObj.size() == 2)
{
    IMvdRectangleF *rectangleRoi = dynamic_cast<IMvdRectangleF*>(modu_input->vtFixRoiShapeObj[0]);
    width = rectangleRoi->GetWidth();
    height = rectangleRoi->GetHeight();
    centerX = rectangleRoi->GetCenterX();
    centerY = rectangleRoi->GetCenterY();

    IMvdRectangleF *rectangleRoi2 = dynamic_cast<IMvdRectangleF*>(modu_input->vtFixRoiShapeObj[1]);
    width2 = rectangleRoi2->GetWidth();
    height2 = rectangleRoi2->GetHeight();
    centerX2 = rectangleRoi2->GetCenterX();
    centerY2 = rectangleRoi2->GetCenterY();
}
```

```cpp
// VmAlgModuBase.cpp 的 ResetDefaultRoi()
int CVmAlgModuleBase::ResetDefaultRoi(OUT BASE_MODU_ROI_DATA* stBaseModuROIData)
{
    int nRet = IMVS_EC_OK;
    stBaseModuROIData->stRoiBox.clear();
    IMVS_ROI_BOX roiBox = { 0.0f };

    // 第一个0度Box
    roiBox.fRoiCenterX = 0.375f;
    roiBox.fRoiCenterY = 0.375f;
    roiBox.fRoiHeight = 0.5f;
    roiBox.fRoiWidth = 0.5f;
    roiBox.fRoiAngle = 0.0f;
    stBaseModuROIData->stRoiBox.push_back(roiBox);

    // 第二个90度Box
    roiBox.fRoiCenterX = 0.7f;
    roiBox.fRoiCenterY = 0.7f;
    roiBox.fRoiHeight = 0.5f;
    roiBox.fRoiWidth = 0.5f;
    roiBox.fRoiAngle = 90.0f;
    stBaseModuROIData->stRoiBox.push_back(roiBox);

    stBaseModuROIData->iRoiTypeIndex = IMVS_ROI_TYPE_BOX;

    return nRet;
}
```

**关键 API / 接口 / 配置项 / 文件路径**
- 配置：`模块名AlgorithmTab.xml` → `ROISelecter` / `ROISelection`（值 `DoubleBox`）。
- 接口：`IMvdRectangleF`、`GetWidth/GetHeight/GetCenterX/GetCenterY`、`dynamic_cast`、`CVmAlgModuleBase::ResetDefaultRoi`、`BASE_MODU_ROI_DATA`、`IMVS_ROI_BOX`、`IMVS_ROI_TYPE_BOX`。

**注意事项 / 坑**
- `ROISelection` 添加的 ROI 类型（如 `DoubleBox`）决定 `vtFixRoiShapeObj` 的元素数量与类型；`dynamic_cast` 失败会得到 `nullptr`，需判空。
- `ResetDefaultRoi` 必须屏蔽原所有代码再写入自定义 Box，否则默认 ROI 不生效或被覆盖。
- ROI 坐标用归一化比例（0~1）而非像素，注意 `0.375/0.5` 等取值含义。

---

### 4.1.14 日志打印：日志打印的方法

**适用场景 / 目标**
自研模块打印日志，协助定位问题（环境 VM4.0.0+）。

**关键概念**
- **日志接口**：`MLOG_ERROR`（VM4.3 前），`MLOG_ERROR`/`LOG_ERROR`（VM4.3 及之后）；等级从高到低：ERROR、WARN、INFO、DEBUG、TRACE。
- **VM4.2 特殊要求**：需向海康技术/研发获取 `spdlog` 文件夹放到 C++ 工程 `src` 目录；初始化 `Spdlog_Init4Module(moduName)`；获取模块 Id `VM_M_GetModuleId(m_hModule, &m_nModuleId)`。
- **日志路径**：`Applications\log\Module\对应模块名.log`。

**实现步骤**
1. VM4.3 之前：在 `AlgorithmModule.cpp` 需打印处调用 `MLOG_ERROR`（调用示例原文为图示，文字缺失）；VM4.2 还需 `spdlog` + 初始化 `Spdlog_Init4Module` + `VM_M_GetModuleId`。
2. VM4.3 及之后：调用 `MLOG_ERROR` 或 `LOG_ERROR`（调用示例原文为图示，文字缺失）。
3. 日志写入 `Applications\log\Module\对应模块名.log`。

**关键代码**
本条目以接口调用为主，调用示例原文为图示（文字缺失）；接口签名示例：

```cpp
// VM4.3 之前
MLOG_ERROR("your log message");

// VM4.3 及之后
MLOG_ERROR("your log message");
LOG_ERROR("your log message");

// VM4.2 额外初始化（spdlog）
Spdlog_Init4Module(moduName);
VM_M_GetModuleId(m_hModule, &m_nModuleId);
```

**关键 API / 接口 / 配置项 / 文件路径**
- 接口：`MLOG_ERROR`、`LOG_ERROR`（等级 ERROR/WARN/INFO/DEBUG/TRACE）、`Spdlog_Init4Module`、`VM_M_GetModuleId`。
- 依赖：VM4.2 需 `spdlog` 文件夹（置于 C++ 工程 `src` 目录）。
- 日志路径：`Applications\log\Module`、`Applications\log\Module\对应模块名.log`。

**注意事项 / 坑**
- VM4.2 必须额外获取并部署 `spdlog` 且完成 `Spdlog_Init4Module` 初始化，否则日志接口不可用/不输出。
- 日志等级按需选择，生产环境避免过多 TRACE/DEBUG 影响性能。
- 不同版本接口名不同（VM4.3 起支持 `LOG_ERROR`），注意与所用 VM 版本匹配。

---

### 4.1.15 参数自执行：参数自执行的方法

**适用场景 / 目标**
自研模块实现「参数自执行」，调整参数时实时看到模块结果（环境 VM4.3.0+）。

**关键概念**
- **`CanTriggerRun`**：在 `模块名AlgorithmTab.xml` 的 `Tab_ROI Area` 节点增加 `CanTriggerRun="TRUE"`，使参数变更触发自动运行。

**实现步骤**
1. 在 `模块名AlgorithmTab.xml` 中找到 `Tab_ROI Area` 节点，增加 `CanTriggerRun="TRUE"`（配置示意原文为图示，文字缺失）。

**关键代码**

```xml
<!-- 在 模块名AlgorithmTab.xml 的 Tab_ROI Area 节点增加 -->
<Tab Name="Tab_ROI Area" CanTriggerRun="TRUE">
    ...
</Tab>
```

**关键 API / 接口 / 配置项 / 文件路径**
- 配置项：`Tab_ROI Area` → `CanTriggerRun="TRUE"`。
- 文件：`模块名AlgorithmTab.xml`。

**注意事项 / 坑**
- 仅 VM4.3.0 及以上支持 `CanTriggerRun`；低版本无此特性。
- 需放在正确的 `Tab`（ROI Area）节点，否则不触发自动运行。

---

## 4.2 联合 OpenCV 开发

### 4.2.1 环境配置：使用OpenCV 开发的环境配置

**适用场景 / 目标**
使用第三方库 OpenCV 开发自定义算法模块时的 VS 环境配置（环境 VM4.0.0+）。

**关键概念**
- **版本对应**：OpenCV 版本须与 VS 集成环境（生成工具）对应。VS2013 对应 VC=120，需 OpenCV 包含 VC=120 构建，如 OpenCV 3.1.0。
- **系统 Path**：加入 `opencv\build\x64\vc12\bin`。
- **VS 工程属性**：包含目录（3 个）、库目录（1 个）、链接器附加依赖项 `opencv_world310.lib`（Debug 为 `opencv_world310d.lib`，后缀随版本变）。

**实现步骤**
1. 下载对应 OpenCV（VS2013/VC=120 → OpenCV 3.1.0）。
2. 解压并在系统 Path 添加 `D:\OpenCV3.1.0\opencv\build\x64\vc12\bin`。
3. VS 项目属性页：
   - VC++ 目录 → 包含目录：添加 3 个 OpenCV 相关路径（原文为图示，文字缺失）。
   - VC++ 目录 → 库目录：添加 1 个 OpenCV 相关路径（原文为图示，文字缺失）。
   - 链接器 → 库目录/附加依赖项：添加 `opencv_world310.lib`（Debug 为 `opencv_world310d.lib`）。

**关键代码**
本条目为工程配置，无代码片段。

**关键 API / 接口 / 配置项 / 文件路径**
- 路径示例：`D:\OpenCV3.1.0\opencv\build\x64\vc12\bin`。
- 库文件：`opencv_world310.lib`（Release）、`opencv_world310d.lib`（Debug）。
- 版本映射：VS2013 ↔ VC=120 ↔ `vc12` ↔ OpenCV 3.1.0。

**注意事项 / 坑**
- OpenCV 版本与 VS 工具集必须匹配（VC 主版本号对应），否则链接/运行报错。
- Debug/Release 的 lib 后缀不同（`d` 后缀），混用导致链接失败。
- 路径中 `vc12` 对应 VS2013；若用更高 VS 需对应 `vc14/vc15` 等。

---

### 4.2.2 图像类算法：使用OpenCV 开发算法模块的方法

**适用场景 / 目标**
用 OpenCV 开源库处理图像并作为 VM 自定义算法模块（环境 VM4.0+）。

**关键概念**
- **格式互转**：VM 内部图像为 `HKA_IMAGE`，需转 OpenCV `cv::Mat` 处理，再转回 `HKA_IMAGE` 输出。

**实现步骤**
1. 输入图像格式由 `HKA_IMAGE` 转 `Mat`。
2. 调用 OpenCV 算子 API 处理图像。
3. 输出图像格式由 `Mat` 转 `HKA_IMAGE`。
4. 输出图像。

**关键代码**
本条目为流程说明，无具体互转代码片段（互转时需按 `HKA_IMAGE` 的 `data[0]/width/height/format/step[0]` 构造 `cv::Mat`，可参考 4.1.8 的 `VmModule_GetInputImageByName` 取值逻辑）。

**关键 API / 接口 / 配置项 / 文件路径**
- 类型：`HKA_IMAGE`、`cv::Mat`。
- 流程：`HKA_IMAGE → Mat → OpenCV API → Mat → HKA_IMAGE → 输出`。

**注意事项 / 坑**
- `cv::Mat` 构造需注意像素格式（Mono8 / RGB24_C3 步长不同，`step[0] = 3*width` for RGB），否则图像错位或崩溃。
- 转回 `HKA_IMAGE` 后要正确回填 `format/data[0]/step[0]`，供 VM 渲染与下游订阅。

---

## 4.3 联合 Halcon 开发

### 4.3.1 联合开发：集成HALCON 第三方算子到VM 工具箱的方法

**适用场景 / 目标**
将 HALCON、OpenCV 等第三方视觉算法库封装成 VM 工具箱中的自定义算法模块（可弹窗配置运行参数、连线订阅、设 ROI、查看渲染），以封装 HALCON `DynThreshold` 动态阈值算子为例（环境 VM4.0+）。

**关键概念**
- **XML 驱动界面**：VM 所有模块的参数调试界面依赖 XML；VM 启动时按 `Module(sp)` 内 XML 呈现界面。每个模块 XML 在 `VisionMaster4.0.0\Applications\Module(sp)\x64\<工具箱>\XXXModu`，如定位组的 `IMVSHPFeatureMatchModu`；选中模块按 `Ctrl+m` 打开 XML 文件夹。
- **参数组成**：Int/Float/string/bool/enum 等基本类型，由 XML 树形节点描述；运行参数位于 `XXXAlgorithmTab.xml` 的 `Tab_Run_Params`。
- **ROI 输入**：是否接受 ROI、位置修正由 XML 决定（如 Blob 模块的 `IMVSBlobFindModuAlrorithemTab.xml` 中 Item）。
- **便捷工具**：VM「工具」菜单下的算法模块生成器（AlgorithmXMLGenerator）配置输入输出，免手写全部 XML。
- **集成三件事**：① 生成界面（XML）；② C# DLL（界面资源）；③ C++ DLL（算法流程）。
- **生成产物**：以模块名前缀的 3 个文件夹；其中 `DynThreshold` 文件夹最终拷到 `Applications\Module(sp)\x64\<类别>`；`Cs` 开头为 C# 工程，仅编译「以模块名命名的工程」（Release，不编译 `+Control` 工程）；C++ 工程名 `Proj_<模块名>`（本例 `Proj_DynThreshold`），用 VS2013（msvc2013），Release/x64/禁用优化，并配置 Halcon 包含/库/依赖项。

**实现步骤**
1. 准备工作（概念）：
   1.1 确认模块 XML 位于 `Module(sp)` 目录（例：`C:\Program Files\VisionMaster4.0.0\Applications\Module(sp)\x64\Location\IMVSHPFeatureMatchModu`）。
   1.2 输入输出由基本类型组成，在 `XXXAlgorithmTab.xml` 的 `Tab_Run_Params` 描述。
   1.3 ROI 输入由 XML 配置决定。
   1.4 集成需完成 3 项：生成界面 / C# DLL / C++ DLL。
2. 举例（封装 `DynThreshold`）：
   - `DynThreshold(HObject inputImage, HTuple darkLight, HTuple maskWidth, HTuple maskHeight, HTuple offset, HTuple minArea, HTuple maxArea, HTuple *area)`。
   - 输入图像订阅 VM 图像源；ROI 由界面交互获得。
   - 第一步：用 `AlgorithmXMLGenerator` 生成 XML 文件夹；再生成 C# 工程与 C++ 工程；得 3 个以模块名前缀文件夹，`DynThreshold` 文件夹最终拷到 `Applications\Module(sp)\x64\<类别>`；编译 `Cs` 工程「以模块名命名工程」（Release），将 `模块名+cs.dll` 与 `模块名.pdb` 拷到 `DynThreshold` 文件夹。
   - 第二步：编写 C++ 工程 `Proj_DynThreshold`（VS2013，Release/x64/禁用优化），配置 Halcon 环境（附加包含目录、附加库目录、附加依赖项）。

**关键代码**
本条目以工程/配置为主，无独立算法代码片段（具体算法在 `Process()` 中调用 HALCON `DynThreshold` 等算子，图像与参数通过前述 `VM_M_Getxxxx/GetParam` 接口获取，经 `HKA_IMAGE` 与 HALCON `HObject` 互转后调用 HALCON API，结果经 `VM_M_Setxxxx` 输出）。

**关键 API / 接口 / 配置项 / 文件路径**
- 工具：`AlgorithmXMLGenerator`（VM「工具」菜单）。
- 模块 XML 目录：`VisionMaster4.0.0\Applications\Module(sp)\x64\<工具箱>\XXXModu`（快捷键 `Ctrl+m` 打开）。
- 配置：`XXXAlgorithmTab.xml` 的 `Tab_Run_Params`、`ROISelection`（ROI 类型）。
- C++ 工程：`Proj_<模块名>`（例 `Proj_DynThreshold`），编译器 msvc2013，Release/x64/禁用优化。
- Halcon 配置：附加包含目录、附加库目录、附加依赖项。
- 产物拷贝：`模块名+cs.dll`、`模块名.pdb` → `DynThreshold` 文件夹；`DynThreshold` 文件夹 → `Applications\Module(sp)\x64\<类别>`。

**注意事项 / 坑**
- C# 工程仅编译「以模块名命名的工程」，不要编译 `+Control` 工程，否则易出错或多余。
- C++ 工程必须用 VS2013 / msvc2013 编译器，且 Release + x64 + 禁用优化，与 VM 宿主一致。
- Halcon 环境（包含/库/依赖项）须在 C++ 工程中正确配置，否则 `DynThreshold` 等算子链接失败。
- 图像在 VM（`HKA_IMAGE`）与 HALCON（`HObject`）间需正确互转（像素格式/步长）。
- 本条目在源片段（PDF 第 800 页）处截止，后续「第二步编写 C++ 工程」细节及可能的 4.3.2 等未在本次输入内。

---

## 条目索引

> 本章输入文件（PDF 703–800 页）实际包含以下 **18** 个条目（编号与标题原样保留）：

**4.1 开发配置类**
1. 4.1.1 算法开发：算法模块的开发流程
2. 4.1.2 参数操作：获取与设置模块参数的方法
3. 4.1.3 文件交互：文件交互操作的配置方法
4. 4.1.4 输出显示：设置输出并显示在VM 界面的方法
5. 4.1.5 模板配置：模板配置界面的实现方法
6. 4.1.6 命名翻译：自定义模块在VM 界面显示中文的方法
7. 4.1.7 无图像源：算法模块无输入图像的方法
8. 4.1.8 多图像源：算法模块输入多幅图像的方法
9. 4.1.9 断点调试：附加断点调试的注意事项
10. 4.1.10 点集参数：点集输入、输出实现方法
11. 4.1.11 直线参数：获取输入直线的方法
12. 4.1.12 矩形参数：输出和显示矩形检测框的方法
13. 4.1.13 多ROI：获取多个ROI 的方法
14. 4.1.14 日志打印：日志打印的方法
15. 4.1.15 参数自执行：参数自执行的方法

**4.2 联合 OpenCV 开发**
16. 4.2.1 环境配置：使用OpenCV 开发的环境配置
17. 4.2.2 图像类算法：使用OpenCV 开发算法模块的方法

**4.3 联合 Halcon 开发**
18. 4.3.1 联合开发：集成HALCON 第三方算子到VM 工具箱的方法

**未覆盖说明**
- **4.4 异常处理**：不在本输入文件（PDF 703–800 页）内，源片段于第 800 页 4.3.1 处截止，故未提炼、未编造。如后续取得 4.4 章节原文，应另行补充。
