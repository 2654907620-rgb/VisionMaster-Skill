<!-- source: chm_core.md (常见问题) -->
# VM .NET SDK 官方常见问题

本文档汇集 VisionMaster .NET SDK 官方常见问题，共 12 条，覆盖环境配置、模块/图像源/渲染/控件/全局模块/通信/异常捕获等典型场景。每条包含问题、解答、关键代码与关键 API。

## 速览

1. 如何排查程序启动后报错的原因？
2. 如何设置模块输入图像、参数和 ROI 区域？
3. 如何通过图像源模块接口设置输入图像？
4. 如何获取渲染图像的数据？
5. 如何在渲染控件上自定义图形？
6. 如何设置控件语言为英文？
7. 如何通过流程输出或者模块输出获取数据结果？
8. 如何通过绑定流程或模块获取渲染结果？
9. 如何获取全局相机列表和设置相机参数？
10. 全局模块控件中的通信管理如何接收和发送数据？
11. 如何捕获控件操作过程中抛出的异常？
12. 如何理解设置输入接口的"仅当次执行起效"逻辑？

---

### 问题：如何排查程序启动后报错的原因？

**问题描述：** VM4.3 SDK 程序启动后，出现 Vm.Core.Solution 或 VM.PlatformSDKCS 等相关内容。

**解答：**
1. 确保 VM 软件能正常运行，且能打开和运行方案。
2. 确认环境已完成配置：是否插好加密狗，是否以管理员身份运行 VS 再打开项目，框架是否选择 .NET Framework 4.6.1 且取消勾选【首选 32 位】，二次开发程序启动前是否已关闭 VM 软件。
3. （可选）若 VM 版本为 4.0 或 4.1，SDK 开发时重新拷贝 `Development\V4.0.0\ComControls\bin\x64` 下所有的文件到二次开发 exe 所在目录下。
4. 若 PC 存在多个版本的 VM，请确认方案和程序升级后，是否适配当前的 VM 版本。
5. 如以上操作仍无法解决，可使用 `try{ }catch(VmException ex){ }` 捕获异常码，并在手册中查找异常码对应的内容。

**关键代码：**
```csharp
try
{
    // 加载方案、执行等操作
}
catch (VmException ex)
{
    // 在手册中查找异常码 ex.errorCode 对应的内容
}
```

**关键 API：** `VmException`（异常类，含 `errorCode` 错误码属性）。

---

### 问题：如何设置模块输入图像、参数和 ROI 区域？

**问题描述：** 如何设置模块的输入图像、模块参数及 ROI 区域？

**解答：** VM 模块的输入主要包含两部分：基本参数（图像输入、ROI 区域）和运行参数。除图像源模块以及无输入图像的模块以外，在 SDK 二次开发时可通过代码修改模块的输入参数。以下内容以圆查找模块为例。

1. 设置模块输入图像，添加命名空间 `IMVSCircleFindModuCs`。
2. 通过 `ModuParams` 的属性设置模块运行参数。
3. 设置指定模块的 ROI 区域。

**注意：**
- 设置【基本参数】，参数配置窗口界面不会显示所设置的参数。此时若模块运行，则参数永久有效；若流程运行，则参数一次有效。
- 设置【运行参数】，参数配置窗口界面会显示所设置的参数。此时模块和流程运行，参数均永久有效。

**关键代码：**
```csharp
// 1. 设置模块输入图像
Mat matImagee = Cv2.ImRead("D:\\3.ProjectCode\\VM4.3\\1.bmp", ImreadModes.Grayscale);
IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["流程3.圆查找1"] as IMVSCircleFindModuTool;  //实例化指定的模块工具
ImageBaseData StImgbase = new ImageBaseData(matImagee.Data, (uint)(matImagee.Width * matImagee.Height), matImagee.Width, matImagee.Height, VMPixelFormat.VM_PIXEL_MONO_08);
circleFindModuTool.ModuParams.InputImage = StImgbase;

// 2. 设置模块运行参数
IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["流程1.圆查找1"] as IMVSCircleFindModuTool;  //实例化指定的模块工具
circleFindModuTool.ModuParams.EdgeThresh = 30;  //设置边缘阈值为30

// 3. 设置指定模块的ROI区域
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
RectBox rectBox = new RectBox(new VM.PlatformSDKCS.PointF(1000, 1000), 500, 500, 0);
tool.ModuParams.ModuRoiManager.RoiRectangle = rectBox;      //代码设置ROI
```

**关键 API：** `IMVSCircleFindModuTool`、`ModuParams.InputImage`、`ModuParams.EdgeThresh`、`ModuParams.ModuRoiManager.RoiRectangle`、`ImageBaseData`、`RectBox`、`VM.PlatformSDKCS.PointF`。

---

### 问题：如何通过图像源模块接口设置输入图像？

**问题描述：** 如何通过图像源模块接口设置输入图像？

**知识点：** 图像源模块的图像分为 8 位灰度图和 24 位彩色图，可输出两层图像，分别为【图像源.图像】和【图像源.灰度图像】。其他模块基本只能处理 8 位图。
- 图像源类型为 SDK 且接口传入的图像为灰度图时：未开启输出 Mono8 使能，则【图像源.图像】有灰度图数据；开启输出 Mono8 使能，则【图像源.图像】和【图像源.灰度图像】均为灰度图。
- 图像源类型为 SDK 且接口传入的图像为彩色图时：未开启输出 Mono8 使能，则【图像源.图像】为彩色图；开启输出 Mono8 使能，则前者为彩色图、后者为灰度图。
- 后续连接模块图像输入源默认【图像源.图像】；若为彩色图需将输入源设为【图像源.灰度图像】，否则后续模块将运行失败。

**解答：** 图像源选择不同的类型，操作方法有所差别。
- SDK 类型：使用 `SetImagePath` 接口或 `SetImageData` 接口（`SetImageData` 参数类型为 `ImageBaseData`，像素格式使用枚举类 `VMPixelFormat`）。
- 本地（LocalImage）类型：可实现添加单个图像，使用 `AddInputImageByPath`；批量添加图片文件夹则遍历调用 `AddInputImageByPath`。

**关键代码：**
```csharp
// SDK 类型
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.SDK;
imageSourcTool.SetImagePath("E:\\VSVM4.0\\1.bmp");
imageSourcTool.SetImageData(imageBaseData);             //参数类型为ImageBaseData

// 本地（LocalImage）类型
ImageSourceModuleTool imageSourcTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.LocalImage;

//添加图片
imageSourceTool.AddInputImageByPath("D:\\3.ProjectCode\\VM4.3\\1.bmp");

//删除图片
imageSourceTool.DeleteInputImageByPath("D:\\1.bmp");

//清空图片
imageSourceTool.ClearAllInputImage();

//加载文件夹中所有图片
DirectoryInfo dir = new DirectoryInfo("E:\\VSVM4.2\\图像\\新建文件夹");
FileInfo[] dirinfo = dir.GetFiles();
for (int i = 0; i < dirinfo.Length; i++)
{
    string str = dirinfo[i].FullName;
    imageSourceTool.AddInputImageByPath(str);
}
```

**关键 API：** `ImageSourceModuleTool`、`ImageSourceParam.ImageSourceTypeEnum.SDK`/`LocalImage`、`SetImagePath`、`SetImageData`、`AddInputImageByPath`、`DeleteInputImageByPath`、`ClearAllInputImage`、`VMPixelFormat`。

---

### 问题：如何获取渲染图像的数据？

**问题描述：** 如何获取渲染图像的数据？

**解答：**
1. 存图到本地：在输出图像模块的【基本参数】中选择【像素格式】（RGB24 或 MONO8）；通过【渲染设置】中的【前项存储设置】订阅相应模块数据；开启【基本参数】的【存图使能】并设置存图路径，方案运行时即可保存渲染图。
2. 获取渲染图像数据，可通过流程获取，也可通过模块输出。

**关键代码：**
```csharp
// 通过模块输出获取（像素格式为RGB24且前项存储设置已订阅相应模块数据）
SaveImageTool saveImage = (SaveImageTool)VmSolution.Instance["流程1.输出图像1"];    // 实例化输出图像模块
var saveImageResult = saveIamge.ModuResult.OutputImage;
byte[] imageData = saveImageResult.ImageData;
int imagePixelformat = saveImageResult.Pixelformat;                              // 17301505为MONO8灰度图，35127316为彩色图
```

**关键 API：** `SaveImageTool`、`ModuResult.OutputImage`（含 `ImageData`、`Pixelformat` 属性；`17301505`=MONO8，`35127316`=彩色图）。

---

### 问题：如何在渲染控件上自定义图形？

**问题描述：** 如何在渲染控件上自定义图形？

**解答：**
1. 手动添加引用 `VMControls.WPF.dll`、`WindowsBase.dll`，引用属性【复制本地】改为 false。
2. 渲染控件绑定图像再绘制图形。
3. 流程运行结束后，在回调函数中调用渲染控件的 `AddShape` 绘图接口，支持直线、圆形、矩形、文本等。以绘制直线和文本为例：

**关键代码：**
```csharp
//绘制直线
VMControls.WPF.LineEx line = new VMControls.WPF.LineEx(new System.Windows.Point(100, 100), new System.Windows.Point(600, 600), stroke: "#FF0000", strokeThickness: 10);
vmRenderControl1.AddShape(line);

//绘制文本
VMControls.WPF.TextEx text = new VMControls.WPF.TextEx("欢迎使用VM4.2二次开发！", new System.Windows.Point(1000, 1000), fontSize: 20, stroke: "#FF0000");
vmRenderControl1.AddShape(text);
```

**关键 API：** `VMControls.WPF.LineEx`、`VMControls.WPF.TextEx`、`VmRenderControl.AddShape`。

---

### 问题：如何设置控件语言为英文？

**问题描述：** 如何设置控件语言为英文？

**解答：**
- VM4.0 及 VM4.1 的二次开发，控件语言设置的相关配置文件在 debug 路径下的 `LangCFG` 文件夹中，修改配置文件 `LanguageSet.cfg` 即可。
- VM4.2 及 VM4.3 的二次开发，因 debug 中未进行拷贝操作，修改配置文件路径：`..\Development\V4.x\ComControls\Assembly\LangCFG\LanguageSet.cfg`。`zh-cn` 表示中文，英文则修改为 `en-us`。

**关键代码：** （配置项，非代码逻辑）
```
; LanguageSet.cfg
zh-cn   ; 中文
en-us   ; 英文
```

**关键 API：** 配置文件 `LanguageSet.cfg`（语言值 `zh-cn` / `en-us`）。

---

### 问题：如何通过流程输出或者模块输出获取数据结果？

**问题描述：** 如何通过二次开发获取流程输出或模块输出中的数据结果？

**解答：** 获取数据结果可通过流程输出或模块输出两种方式，推荐使用流程输出，更符合高内聚低耦合的思想。

**关键代码：**
```csharp
// 通过流程输出获取（整型、浮点型、字符串型）
VmProcedure vmprocess = (VmProcedure)VmSolution.Instance["流程1"];
var moduResult = vmprocess.ModuResult;
string str = moduResult.GetOutputInt("out").pIntVal[0].ToString();
string str1 = moduResult.GetOutputFloat("out0").pFloatVal[0].ToString();
string str2 = moduResult.GetOutputString("out1").astStringVal[0].strValue;

//获取流程结果列表，str3与str2结果一致
List<VmDynamicIODefine.IoNameInfo> ioNameInfos = VmProcess.ModuResult.GetAllOutputNameInfo();
string str3 = VmProcess.ModuResult.GetOutputString(ioNameInfos[2].Name).astStringVal[0].strValue;

//通过流程输出获取图像数据
ImageBaseData processImageData = VmProcess1.ModuResult.GetOutputImageV2("ImageD");
int width = processImageData.Width;                         //宽
int height = processImageData.Height;                       //高
IntPtr imageByte = processImageData.ImageData;              //数据
VMPixelFormat pixelformat = processImageData.Pixelformat;   //格式

//通过模块输出获取浮点型数据
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
var moduResult = tool.ModuResult;
string circleX = moduResult.OutputCircle.CenterPoint.X.ToString();
string circleY = moduResult.OutputCircle.CenterPoint.Y.ToString();
string circleR = moduResult.OutputCircle.Radius.ToString();

//通过模块输出获取图像数据
SaveImageTool saveImage = (SaveImageTool)VmSolution.Instance["流程1.输出图像1"];
var saveImageResult = saveImage.ModuResult.OutputImage;
byte[] imageData = saveImageResult.ImageData;
int imagePixelformat = saveImageResult.Pixelformat;           // 17301505为MONO8灰度图，35127316为彩色图
```

**关键 API：** `VmProcedure.ModuResult`（`GetOutputInt`/`GetOutputFloat`/`GetOutputString`/`GetOutputImageV2`/`GetAllOutputNameInfo`）、`VmDynamicIODefine.IoNameInfo`、`IMVSCircleFindModuTool.ModuResult.OutputCircle`、`SaveImageTool.ModuResult.OutputImage`。

---

### 问题：如何通过绑定流程或模块获取渲染结果？

**问题描述：** 如何通过绑定流程或模块获取渲染结果？

**解答：** 渲染结果的显示可通过渲染控件绑定流程或模块实现，推荐使用绑定流程方式，更符合高内聚低耦合思想，绑定流程可实现单个渲染控件绑定多个算法模块渲染结果。
- 绑定流程：一个渲染控件只能同时绑定一个流程，如需绑定多个流程需分时绑定或使用多个渲染控件。
- 绑定模块：只能渲染某个模块的渲染结果。

**关键代码：**
```csharp
// 通过绑定流程显示渲染结果
VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//实例化流程1
vmRenderControl.ModuleSource = VmProcess;

// 通过绑定模块显示渲染结果
IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool = (IMVSCircleFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
vmRenderControl.ModuleSource = circleTool;
```

**关键 API：** `VmRenderControl.ModuleSource`、`VmProcedure`、`IMVSCircleFindModuTool`。

---

### 问题：如何获取全局相机列表和设置相机参数？

**问题描述：** 如何获取方案中所有全局相机的连接状态，并设置全局相机的基本参数？例如：在流程运行时查看全局相机1和2的连接状态，并设置全局相机1的曝光和增益。

**解答：**
1. 获取方案中所有全局相机的连接状态：V4.2.1 版本新增获取相机连接状态的 API，通过 `GlobalCameraTool` 类中的 `bIsCameraConnect()` 获取连接状态。可遍历所有模块筛选 `GlobalCameraModuleTool` 并启动监控线程。
2. 设置全局相机的参数：通过 `GlobalCameraParam` 类的方法和属性设置。

**注意：** 全局相机使用时若没有添加引用的工具，需手动添加 `GlobalCameraModuleCs.dll` 引用，将"复制到本地"设为 False，并添加命名空间 `using GlobalCameraModuleCsl;`。

**关键代码：**
```csharp
// 获取流程中所有全局相机模块
List<GlobalCameraModuleTool> glCameralist = new List<GlobalCameraModuleTool>();
List<VmModule> vmModules = new List<VmModule>();
VmSolution.Instance.GetAllModule(vmModules);
foreach (VmModule module in vmModules)
{
    if (module.GetType() == typeof(GlobalCameraModuleTool))
    {
        glCameralist.Add((GlobalCameraModuleTool)module);
    }
}

// 启动全局相机连接状态监控线程
Thread watchThread = new Thread(new ParameterizedThreadStart(CameraConnectionWatchDog));
watchThread.IsBackground = true;
watchThread.Start(glCameralist);

// 查看相机连接状态的线程函数
public void CameraConnectionWatchDog(object obj)
{
    List<GlobalCameraModuleTool> globalCameraToolList = (List<GlobalCameraModuleTool>)obj;
    bool[] isCameraConected = new bool[globalCameraToolList.Count];
    while (true)
    {
        try
        {
            foreach (var cameraTool in globalCameraToolList)
            {
                if (cameraTool.bIsCameraConnect() == false)
                {
                    MessageBox.Show(string.Format($"警告: {cameraTool.Name} 已经离线！"));
                }
            }
        }
        catch (VmException ex)
        {
            MessageBox.Show("发生致命错误，错误码:" + ex.errorCode);
        }
        Thread.Sleep(2000);
    }
}

// 设置全局相机1的曝光和增益
GlobalCameraModuleTool cameraModuleTool = VmSolution.Instance["全局相机1"] as GlobalCameraModuleTool;
GlobalCameraParam globalCameraParam = cameraModuleTool.ModuParams;
globalCameraParam.ExposureTime = 5000;
globalCameraParam.Gain = 5.0;
```

**关键 API：** `GlobalCameraModuleTool`、`GetAllModule`、`bIsCameraConnect()`、`GlobalCameraParam.ExposureTime`/`Gain`、`VmSolution.Instance["全局相机1"]`、`GlobalCameraModuleCs.dll`。

---

### 问题：全局模块控件中的通信管理如何接收和发送数据？

**问题描述：** 二次开发中，全局模块控件中的通信管理如何接收和发送数据？

**解答：**
- 通过 `GetReadData()` 接口接收数据，通过 `SetInt()` 或 `SetString()` 接口发送整型或字符串数据。
- 通过回调接收数据：需添加 `HikExternalCall.dll` 引用（复制到本地= false），注册 `VmSolution.OnCommunicationRecvCallBackEvent` 回调。

**关键代码：**
```csharp
// 直接发送/接收
CommManagerModuleTool commTool = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];   //“通信管理1”是指当前运行的通信设备
if (null != null)
{
    commTool.SetString(2, "abcd");                  //发送字符串型数据，接口函数SetString中的设备号2为通信管理中自动生成的设备序号
    int[] aIntVal = new int[3];
    aIntVal[0] = 10;
    aIntVal[1] = 11;
    aIntVal[2] = 12;
    commTool.SetInt(1, aIntVal, 0);                 //发送整型数据
    byte[] btData = null;
    commTool.GetReadData(2, ref btData);            //接收数据
}

// 通过回调接收数据
//添加HikExternalCall.dll引用，引用属性【复制到本地】改为false
using HikExternalCall.Common;

//注册回调函数，通讯接受事件回调
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
    }
    catch (VmException ex)
    {
        strMsg = "读取通信数据失败. Error Code: " + Convert.ToString(ex.errorCode, 16);
    }
}

//发送字符串数据
public void SendCommDeviceData(int Num, string SendMessage)
{
    CommManagerModuleTool commManagerModule = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];
    string strMsg;
    try
    {
        if (commManagerModule.bIsDeviceConnect(Num))
        {
            commManagerModule.SetString(Num, SendMessage);
            strMsg = "发送信号：" + SendMessage + "给" + Num + "号通讯设备";
        }
        else
        {
            strMsg = Num + "号通讯设备未打开";
        }
    }
    catch (Exception ex)
    {
        strMsg = "发送信号失败";
        return;
    }
}
```

**关键 API：** `CommManagerModuleTool`、`SetString`、`SetInt`、`GetReadData`、`bIsDeviceConnect`、`VmSolution.OnCommunicationRecvCallBackEvent`、`ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO`、`HikExternalCall.Common`、`ExternalCallHelper.IntPtr2Bytes`。

---

### 问题：如何捕获控件操作过程中抛出的异常？

**问题描述：** 二次开发程序操作控件的过程中，一般异常会在内部进行捕获，并以弹窗、日志等方式提示，部分特殊异常会抛出到外部（例如加密狗断开等）。若未妥善捕获该类异常，可能会导致程序闪退。

**解答：** 建议在程序中增加全局捕获异常逻辑。

**关键代码：**
```csharp
// 对于Winform程序：
// 指示应用程序如何响应未经处理的异常
Application.SetUnhandledExceptionMode(UnhandledExceptionMode.CatchException);
// 处理UI线程异常
Application.ThreadException += Application_ThreadException;
// 处理非UI线程异常
AppDomain.CurrentDomain.UnhandledException += CurrentDomain_UnhandledException;

Application.EnableVisualStyles();
Application.SetCompatibleTextRenderingDefault(false);
Application.Run(new Form1());

// 对于WPF程序：
// 处理UI线程异常
this.DispatcherUnhandledException += App_DispatcherUnhandledException;
// 处理非UI线程异常
AppDomain.CurrentDomain.UnhandledException += CurrentDomain_UnhandledException;
```

**关键 API：** `Application.SetUnhandledExceptionMode`、`Application.ThreadException`、`AppDomain.CurrentDomain.UnhandledException`、`DispatcherUnhandledException`。

---

### 问题：如何理解设置输入接口的"仅当次执行起效"逻辑？

**问题描述：** 设置输入类型的接口（包括参数类的输入图像、ROI 管理类的矩形/掩膜图像等接口）在配合流程执行接口或模块执行接口时，逻辑存在不一致的情况。

**解答：** "仅当次执行起效"逻辑主要针对流程执行。在调用设置输入接口后，两种情况执行逻辑不同：
- 如果接着调用**流程执行接口**，流程使用设置数据执行一次并清空设置数据，下一次流程执行则按照流程配置执行；
- 如果接着调用**模块执行接口**，模块使用设置数据执行一次但不清空设置数据，下一次模块或流程执行则继续使用设置数据执行。

**关键代码：** （逻辑说明，无独立代码块）

**关键 API：** 设置输入类接口（输入图像、ROI 矩形/掩膜图像等）、流程执行接口（`VmSolution.SyncRun` / `VmProcedure.Run`）、模块执行接口（`Module.Run`）。

---

## 条目索引

1. 如何排查程序启动后报错的原因？
2. 如何设置模块输入图像、参数和 ROI 区域？
3. 如何通过图像源模块接口设置输入图像？
4. 如何获取渲染图像的数据？
5. 如何在渲染控件上自定义图形？
6. 如何设置控件语言为英文？
7. 如何通过流程输出或者模块输出获取数据结果？
8. 如何通过绑定流程或模块获取渲染结果？
9. 如何获取全局相机列表和设置相机参数？
10. 全局模块控件中的通信管理如何接收和发送数据？
11. 如何捕获控件操作过程中抛出的异常？
12. 如何理解设置输入接口的"仅当次执行起效"逻辑？
