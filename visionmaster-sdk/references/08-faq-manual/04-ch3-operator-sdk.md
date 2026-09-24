<!-- source: 05-ch3-operator-sdk.md  pages 598-702 -->
# VM 算子SDK 开发 FAQ（第3章）

> 适用范围：MVDAlgorithm SDK 3.4 及以上 + Visual Studio 2013 及以上（WinForm / WPF，C# 与 C++）。
> 本文档提炼自《VM 4.x（算子SDK 和算法模块开发）》第 3 章「算子SDK 开发」，覆盖 3.1 环境配置类、3.2 公用工具类、3.3 模块工具类、3.4 控件嵌入类。
> 说明：原始输入文件在章节 3 之前还包含 2.5.1「全局相机」条目（pages 589–596），属于第 2 章「全工具类」内容，但因其对算子SDK 调用全局相机模块有参考价值，作为「附录 A」一并收录。

## 本章速览

1. **环境配置**：WinForm 下需引用 `Algorithms`、`Common`、`Control` 三目录下的 dll；渲染控件 `MvRenderActiveX.Net.dll` 需手动加入工具箱。
2. **C++ 封装**：可用虚函数把算子抽象为 `IVisionTool`（Initialize/ImportData/ExportData/Train/Run/GetResult），注意指针内存释放。
3. **托管调试助手中断**：在 VS 异常设置中取消勾选 `ContextSwitchDeadlock`、`DisconnectedContext`。
4. **深度学习 GPU StackOverFlow**：须用 x64 平台，必要时调大堆栈提交大小。
5. **图像载入**：`CMvdImage.InitImage(path, MVD_PIXEL_FORMAT)`，彩色用 `MVD_PIXEL_RGB_RGB24_C3`，灰度用 `MVD_PIXELMONO_08`。
6. **相机取流**：通过 `VisionDesigner.Camera.CCameraTool` 或 `mvdCameraEdit` 控件取流。
7. **内存图像输入**：通过 `MVD_IMAGE_DATA_INFO` + `InitImage(w,h,pixelFormat,data)` 注入，不能用 `SetPrivateData/SetPixel`。
8. **卡尺 ROI**：算子SDK 默认不支持直线/圆卡尺 ROI，需自行生成「卡尺框列表 + 最小外接矩形」，运行时 `RunningMode = MVD_RUNNING_MODE_ONLY_FIND`。
9. **DL 算子唤醒**：长时间空闲显卡休眠导致首次运行变慢，需用 CUDA 周期 memcpy 唤醒。
10. **位置修正/图像修正**：基于基准点 `BasePoint` 与运行点 `RunningPoint` 的仿射/平移变换（`MVD_POSFIX_MODE_HVA` / `MVD_IMGFIX_MODE_HVA`）。
11. **模板匹配**：`ImportPattern/ExportPattern` 实现模板自动加载；训练完成以 `GetPatternResult()!=null` 判断。
12. **Blob**：`SetRunParam` 设极性/阈值/面积，`Result.BlobInfo` 取结果，常配合位置修正绘制。
13. **掩膜**：`CPreproMaskTool` 生成掩模图像，`BlobFindTool.RegionImage` 接收，`Tuple<CMvdShape,bool>` 第二参数为 `true` 表示屏蔽区。
14. **字符识别**：`CNNOCRTool` 用 `lpr_ocr.bin`，`CNNCharRecogTool` 用 `mvb_ocr.bin`；多线程需深拷贝模型后 `LoadModelData`。
15. **控件嵌入**：`mvdRenderActivex1.SaveImage` 存渲染图；`AddShape` + `Display` 叠加图形；WPF 用 `WindowsFormsHost` 承载 WinForm 控件。
16. 所有算子工具均为「`xxxTool` 对象 → 设 `InputImage`/`ROI` → `Run()` → 取 `Result`」的统一调用范式。
17. 多数参数既可用强类型属性（如 `BasicParam.*`），也可用字符串 `SetRunParam("Key","Value")` 形式设置。
18. 错误处理统一抛 `MvdException` / `VmException`（C#）或 `IMVDException` / `CVmException`（C++）。

---

## 3.1 环境配置类

### 3.1.1 环境配置：CSharp 算子SDK 开发环境配置方法

**适用场景 / 问题现象**
在 WinForm 下进行算子SDK 开发，不知道如何配置项目环境（缺少引用或缺少控件，导致编译/工具箱不可用）。

**原理 / 关键概念**
算子SDK 通过一组托管 dll 提供算法模块与控件，需把 `Algorithms`、`Common` 目录的引用加入项目，并把预置控件加入工具箱。渲染控件 `MvRenderActiveX.Net.dll` 不在 `Algorithms`/`Common` 常规集合中，需单独处理。

**实现步骤**
1. 用 VS 新建一个 Windows 窗体（WinForm）类项目。
2. 添加 dll 引用：
   - 将 `C:\Program Files (x86)\MVDAlgorithmSDK\ReferencedAssemblies\Algorithms` 下的**所有 dll** 加入项目引用；
   - 将 `C:\Program Files (x86)\MVDAlgorithmSDK\ReferencedAssemblies\Common` 下的引用加入项目，但**第一个和第二个不能添加**（否则引用报错），其余全部引用。
3. 此时工具箱会出现已封装好的控件，拖到窗体上即可生成并启动。控件基本都在 `...\ReferencedAssemblies\Control` 文件夹下；只有一个在 `Common` 文件夹下：**`MvRenderActiveX.Net.dll`**（图形处理渲染控件），需单独将其添加到工具箱。

**关键代码**
（本条目为配置说明，无核心代码片段；要点见上。）

**关键 API / 接口名 / 枚举 / 参数**
- 引用目录：`Algorithms`、`Common`、`Control`（均在 `C:\Program Files (x86)\MVDAlgorithmSDK\ReferencedAssemblies\` 下）
- 渲染控件 dll：`MvRenderActiveX.Net.dll`

**注意事项 / 坑**
- `Common` 目录下**前两个 dll 不能添加**引用，否则会报引用冲突错误。
- 渲染控件 `MvRenderActiveX.Net.dll` 只有一个，位于 `Common` 目录，必须单独加入工具箱，否则无法在界面上做图像渲染。

---

### 3.1.2 算子封装：使用C++封装算子SDK的方法

**适用场景 / 问题现象**
希望把不同算子工具抽象出统一接口（`Initialize` 初始化、`LoadConfiguration` 加载配置、`Train` 训练模型、`LoadModel` 加载模型、`Run` 执行算法），便于统一调度。

**原理 / 关键概念**
算子SDK 已高度面向对象，直接操作对象的方法/属性即可完成算法流程。进一步抽象可用 C++ 虚函数把算子共性抽成 `IVisionTool` 接口，再由具体工具类（如直线查找 `FindLineTool`）继承实现。每个算子工具的创建/销毁遵循 `CreateXxxToolInstance` / `DestroyXxxToolInstance` 工厂函数约定。

**实现步骤**
1. 定义抽象基类 `IVisionTool`，声明纯虚接口。
2. 具体工具类（以 `FindLineTool` 为例）继承 `IVisionTool` 并实现各接口。
3. 构造函数中用 `CreateLineFindToolInstance` 创建实例；析构函数中 `DestroyLineFindToolInstance` 释放。
4. `Initilize` 中读取参数文件并调用 `LoadConfiguration`；`Run` 中按顺序 `SetInputImage` → `SetROI` → `ClearMasks`/`AddMask` → `Run`。

**关键代码**
```cpp
class IVisionTool
{
public:
    IVisionTool() = default;
    virtual ~IVisionTool() = default;

    //使用参数文件初始化配置
    virtual int Initilize(std::string& paramFilePath = "") = 0;

    //导入数据，数据可以是训练好的模型文件、标定文件、参数配置文件等等
    virtual int ImportData(int &fileType,const std::string &inputPath) = 0;

    //导出数据，数据可以是训练的模型文件、标定文件、参数配置文件等等
    virtual int ExportData(int &fileType,const std::string &inputPath) = 0;

    //训练模型
    virtual int Train(IMVdImage& image,IMvdShape* roi,IMvdShape* mask) = 0;

    //执行算法工具
    virtual int Run(IMVdImage &image,IMvdShape* roi,IMvdShape* mask[],int maskCount) = 0;
    //获取算法工具运行结果
    virtual int GetResult(AlgToolResult &result) = 0;
};
```

```cpp
class FindLineTool:public IVisionTool
{
public:
    FindLineTool();
    ~FindLineTool();

    int Initilize(const std::string& paramFilePath = "") override;
    int ImportData(const int &fileType,const std::string &inputPath) override;
    int ExportData(const int &fileType,const std::string &inputPath) override;
    int Train(const IMVdImage& image,IMvdShape* roi,IMvdShape* mask) override;
    int Run(const IMVdImage &image,IMvdShape* roi,IMvdShape* mask[],int maskCount) override;
    int GetResult(AlgToolResult &result) override;
private:
    ILineFindTool* pLineFindTool;
};
```

```cpp
//构造函数
FindLineTool::FindLineTool()
{
    try
    {
        int nRet = CreateLineFindToolInstance(&pLineFindTool);
        if (nRet != 0)
        {
            throw std::exception("Create FindLineTool instance failed");
        }
    }
    catch (IMVDException& ex)
    {
        throw std::exception(ex);
    }
}
```

```cpp
//析构函数
FindLineTool::~FindLineTool()
{
    if (pLineFindTool != nullptr)
    {
        DestroyLineFindToolInstance(pLineFindTool);
    }
}
```

```cpp
//初始化
int FindLineTool::Initilize(const std::string& paramFilePath = "")
{
    //加载参数文件
    unsigned char* paramBuffer = new unsigned char[1024 * 100];
    try
    {
        FILE* pFile;
        errno_t err = fopen_s(&pFile, inputPath.c_str(), "rb");
        fseek(pFile, 0, SEEK_END);
        long bytes = ftell(pFile);
        fseek(pFile, 0, SEEK_SET);
        fread(paramBuffer, 1, bytes, pFile);
        pLineFindTool->LoadConfiguration(paramBuffer, bytes);
        fclose(pFile);
        delete[] paramBuffer;
        paramBuffer = nullptr;
        return 0;
    }
    catch (IMVDException&ex)
    {
        if (paramBuffer != nullptr)
            delete[] paramBuffer;
        return ex.GetErrorCode();
    }
}
```

```cpp
//运行一次
int Run(const IMVdImage &image, IMvdShape* roi, IMvdShape* mask[], int maskCount)
{
    try
    {
        //1.设置输入图像
        pLineFindTool->SetInputImage(image);
        //2.设置ROI
        pLineFindTool->SetROI(roi);
        //3.设置屏蔽区
        //设置屏蔽区之前先移除vMaskShapes 所有元素
        pLineFindTool->ClearMasks();
        for (int i = 0; i < maskCount; i++)
        {
            pLineFindTool->AddMask(mask[i]);
        }
        //4.运行算子
        pLineFindTool->Run();
        return 0;
    }
    catch (IMVDException&ex)
    {
        return ex.GetErrorCode();
    }
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 抽象接口：`IVisionTool`、`Initilize`、`ImportData`、`ExportData`、`Train`、`Run`、`GetResult`（返回值约定为 `int`，0 表示成功，异常时返回 `IMVDException::GetErrorCode()`）
- 直线查找工具：`ILineFindTool`、`CreateLineFindToolInstance`、`DestroyLineFindToolInstance`
- 实例方法：`LoadConfiguration`、`SetInputImage`、`SetROI`、`ClearMasks`、`AddMask`、`Run`
- 图像/形状类型：`IMVdImage`、`IMvdShape`

**注意事项 / 坑**
- 算子SDK 大部分输入都是**指针**，一定要记得释放指针占用的内存，否则会内存泄漏。本例指针的释放在调用层，由调用者负责释放。
- 调用结束后需显式调用 `DestroyImageInstance`、`DestroyShapeInstance` 等 API 函数释放传入的 `IMvdImage*`、`IMvdShape*` 等指针。
- `Initilize` 中 `new unsigned char[1024*100]` 的缓冲区在任何异常路径都要 `delete[]`，否则泄漏。

---

### 3.1.3 异常中断：算子SDK 软件运行报错"托管调试助手"中断的解决方法

**适用场景 / 问题现象**
运行算子SDK 软件 Demo 时，Visual Studio 弹出"托管调试助手（Managed Debugging Assistant）"中断，程序无法继续。

**原理 / 关键概念**
这是 VS 调试器对 COM 互操作/线程切换死锁等场景的托管调试助手告警，并非算子SDK 逻辑错误。

**实现步骤**
1. 在 VS 中打开「异常设置」（Exception Settings）。
2. 取消勾选 `ContextSwitchDeadlock` 和 `DisconnectedContext` 两项。

**关键代码**
（本条目为 VS 配置操作，无代码。）

**关键 API / 接口名 / 枚举 / 参数**
- 需取消的托管调试助手：`ContextSwitchDeadlock`、`DisconnectedContext`

**注意事项 / 坑**
- 这是 Visual Studio 异常设置不熟悉导致的中断，取消对应助手后即可正常运行 Demo。

---

### 3.1.4 深度学习：GPU 运行深度学习算子引发 StackOverFlow 异常的方法

**适用场景 / 问题现象**
深度学习算子运行时报 `StackOverFlow` 异常，如何处理？

**原理 / 关键概念**
深度学习算子依赖 CUDA，需在 x64 平台运行；默认线程栈提交大小不足时可能溢出。

**实现步骤**
1. 深度学习算子必须在 **x64** 平台下运行；若当前为 Win32，需改为 x64。
2. 改平台后仍报 `StackOverFlow`，则需调大**堆栈提交大小**（项目属性 → 链接器 → 系统 → 堆栈保留/提交大小）。

**关键代码**
（本条目为工程配置，无核心代码。）

**关键 API / 接口名 / 枚举 / 参数**
- 平台：x64（x86/Win32 不支持）
- 链接器设置项：堆栈提交大小（Stack Commit Size）

**注意事项 / 坑**
- 不熟悉内存环境配置时易踩此坑；深度学习算子对平台与栈大小敏感。

---

## 3.2 公用工具类

### 3.2.1 图像载入：本地图像的载入方法

**适用场景 / 问题现象**
彩色/灰度本地图像如何载入为 `CMvdImage`？

**原理 / 关键概念**
`CMvdImage` 是算子SDK 统一图像容器；通过 `InitImage(path, pixelFormat)` 指定文件路径与像素格式载入。

**实现步骤**
1. 彩色图像：`InitImage(ImagePathStr, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3)`。
2. 灰度图像：`InitImage(ImagePathStr, MVD_PIXEL_FORMAT.MVD_PIXELMONO_08)`。

**关键代码**
```csharp
// 一、彩色图像的载入
CMvdImage cMvdImage = new CMvdImage();
cMvdImage.InitImage(ImagePathStr, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3);

// 二、灰度图像的载入
CMvdImage cMvdImage = new CMvdImage();
cMvdImage.InitImage(ImagePathStr, MVD_PIXEL_FORMAT.MVD_PIXELMONO_08);
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CMvdImage`
- 方法：`InitImage(string, MVD_PIXEL_FORMAT)`
- 像素格式枚举：`MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3`、`MVD_PIXEL_FORMAT.MVD_PIXELMONO_08`

**注意事项 / 坑**
- 若原图像素格式为 BGR，需先转换通道灰度值再调用上述像素格式；`MVD_PIXEL_RGB_BGR24_C3` 等不可使用。
- 不熟悉彩色图像像素格式会误用枚举导致载入异常。

---

### 3.2.2 相机取流：相机SDK 取流的方法

**适用场景 / 问题现象**
如何使用相机SDK 截帧并取流？

**原理 / 关键概念**
通过 `VisionDesigner.Camera.CCameraTool` 操作相机设备：枚举设备 → 选择设备 → 打开 → 设采集/触发参数 → 开始取图 → 线程中 `GetOneFrameTimeout` 取帧。`CameraGrabResult` 提供单帧结果。

**实现步骤**
1. 创建 `CCameraTool` 实例，`SelectDevice` + `OpenDevice`。
2. `SetEnumValue` 设置 `AcquisitionMode`（连续）、`TriggerMode`（关闭）、`TriggerSource`（软触发）。
3. `StartGrab` 开始取图；另起线程循环 `CameraGrabResult.GetOneFrameTimeout(ref img)` 取帧。
4. 将 `CMvdImage` 转成业务所需 `ImageData`（示例提供 `CMvdImageToImageData`）。

**关键代码**
```csharp
//相机相关变量
private VisionDesigner.Camera.CCameraTool m_cMyCameraToolObj = null;

/// <summary>
/// 打开相机并开始取图
/// </summary>
public int OpenCamera(int cameraindex = 0)
{
    try
    {
        //DeviceListAcq();//获取相机列表方法
        //创建相机算子实例
        if (null == m_cMyCameraToolObj)
        {
            m_cMyCameraToolObj = new VisionDesigner.Camera.CCameraTool();
            if (null == m_cMyCameraToolObj)
            {
                return -1;
            }
        }
        //设置连续采集模式
        m_cMyCameraToolObj.SelectDevice(cameraindex);//默认选择索引为0 的相机
        m_cMyCameraToolObj.OpenDevice();
        m_cMyCameraToolObj.SetEnumValue("AcquisitionMode", (uint)MVD_CAM_ACQUISITION_MODE.MVD_ACQ_MODE_CONTINUOUS);
        m_cMyCameraToolObj.SetEnumValue("TriggerMode", (uint)MVD_CAM_TRIGGER_MODE.MVD_TRIGGER_MODE_OFF);
        m_cMyCameraToolObj.SetEnumValue("TriggerSource", (uint)MVD_CAM_TRIGGER_SOURCE.MVD_TRIGGER_SOURCE_SOFTWARE);
        m_cMyCameraToolObj.StartGrab();//开始取图
        return 0;
    }
    catch (Exception ex)
    {
        return -1;
    }
}

/// <summary>
/// 从相机获取一帧图像
/// </summary>
private void GetStreamThreadProc()
{
    int nRet = 0;
    CMvdImage imgtemp = null;
    nRet = 0;
    nRet = m_cMyCameraToolObj.CameraGrabResult.GetOneFrameTimeout(ref imgtemp);
    if (0 == nRet && imgtemp != null)
    {
        ImageData imageshow1 = CMvdImageToImageData(imgtemp);
    }
}

/// <summary>
/// CMvdImage 格式的图像转为imagedata 图像
/// </summary>
public ImageData CMvdImageToImageData(CMvdImage image)
{
    if (image != null)
    {
        ImageData imageData = new ImageData();
        imageData.Width = (int)image.Width;
        imageData.Height = (int)image.Height;
        imageData.PixelFormat = PixelFormats.Gray8;
        imageData.ImageBuffer = new byte[image.GetImageData(0).arrDataBytes.Length];
        Array.Copy(image.GetImageData(0).arrDataBytes, imageData.ImageBuffer, imageData.ImageBuffer.Length);
        return imageData;
    }
    else
    {
        return null;
    }
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.Camera.CCameraTool`
- 方法：`SelectDevice`、`OpenDevice`、`SetEnumValue`、`StartGrab`、`CameraGrabResult.GetOneFrameTimeout`
- 枚举：`MVD_CAM_ACQUISITION_MODE.MVD_ACQ_MODE_CONTINUOUS`、`MVD_CAM_TRIGGER_MODE.MVD_TRIGGER_MODE_OFF`、`MVD_CAM_TRIGGER_SOURCE.MVD_TRIGGER_SOURCE_SOFTWARE`

**注意事项 / 坑**
- 不熟悉相机SDK 及其接口会导致取流失败；注意 `GetOneFrameTimeout` 用 `ref` 返回图像。

---

### 3.2.3 输入图像：给算子模块输入图像数据的方法

**适用场景 / 问题现象**
如何把内存中的图像数据（而非文件）直接作为算子模块的输入图像？

**原理 / 关键概念**
算子模块接收 `CMvdImage` / `IMvdImage*` 作为输入。内存数据需包成 `MVD_IMAGE_DATA_INFO`（含 `stDataChannel[0].pData/arrDataBytes`、`nRowStep`、`nSize`、`nLen`），再用 `InitImage(width,height,pixelFormat,dataInfo)` 构造图像。

**实现步骤**
1. 准备 `width/height`、像素格式、数据缓冲区。
2. 填充 `MVD_IMAGE_DATA_INFO.stDataChannel[0]`。
3. `CreateImageInstance` / `new CMvdImage()` 后用 `InitImage` 注入。
4. 用 `SetInputImage` / `InputImage` 赋给具体算子（以字符识别 `OCR` 为例）。

**关键代码**
```cpp
//C++
//设置输入图像
int width = 2048;   //图像宽度
int height = 2024;  //图像高度
unsigned char* data = new unsigned char[2048*2024];
memset(data, '0', 2048 * 2024);//内存中图像数据

MVD_IMAGE_DATA_INFO stImageData;
stImageData.stDataChannel[0].pData = data;
stImageData.stDataChannel[0].nRowStep = width;
stImageData.stDataChannel[0].nSize = width * height;
stImageData.stDataChannel[0].nLen = width * height;

MVD_PIXEL_FORMAT pixelFormat = MVD_PIXEL_MONO_08;   //灰度图

IMvdImage* pInputImage = NULL;
CreateImageInstance(&pInputImage);
pInputImage->InitImage(width, height , pixelFormat, stImageData); //加载内存图像的唯一方法，SetPrivateData/SetPixel 均不能使用
//字符识别算子
IOCRSegmenter* pOCRSegmentTool = NULL;
CreateOCRSegmenterInstance(&pOCRSegmentTool);
pOCRSegmentTool->SetInputImage(pInputImage);
```

```csharp
//c#
//设置输入图像
uint width = 2048;
uint height = 2024;
byte[] data = new byte[2048 * 2024];
MVD_IMAGE_DATA_INFO stImageData = new MVD_IMAGE_DATA_INFO();
stImageData.stDataChannel[0].arrDataBytes = data;
stImageData.stDataChannel[0].nRowStep = width;
stImageData.stDataChannel[0].nSize = width * height;
stImageData.stDataChannel[0].nLen = width * height;
MVD_PIXEL_FORMAT pixelFormat = MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08;
VisionDesigner.CMvdImage cInputImg = new CMvdImage();
cInputImg.InitImage(width, height , pixelFormat, stImageData);
//字符识别算子
VisionDesigner.OCR.COCRTool cOCRToolObj = new VisionDesigner.OCR.COCRTool ();
cOCRToolObj.InputImage = cInputImg;
```

**关键 API / 接口名 / 枚举 / 参数**
- 结构：`MVD_IMAGE_DATA_INFO`、`stDataChannel[0]`（`pData`/`arrDataBytes`、`nRowStep`、`nSize`、`nLen`）
- 方法：`CreateImageInstance`、`CMvdImage.InitImage(int,int,MVD_PIXEL_FORMAT,MVD_IMAGE_DATA_INFO)`、`SetInputImage`
- 像素格式：`MVD_PIXEL_MONO_08` / `MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08`
- 字符识别算子：`IOCRSegmenter`、`CreateOCRSegmenterInstance`、`COCRTool`（命名空间 `VisionDesigner.OCR`）

**注意事项 / 坑**
- `InitImage(w,h,pixelFormat,dataInfo)` 是**加载内存图像的唯一方法**，`SetPrivateData`/`SetPixel` 均不能使用。
- C++ 侧 `data` 由 `new[]` 分配，需调用方负责释放。

---

### 3.2.4 实时取流：实时取流的实现方法

**适用场景 / 问题现象**
算子SDK 开发中如何实现相机实时取流（含设备枚举、可达性判断、渲染到控件）？

**原理 / 关键概念**
实时取流标准流程：枚举设备（`EnumDevices`，按 `MVD_TRANSFER_LAYER_TYPE`）→ 选设备（`SelectDevice`）→ 判可达（`IsDeviceAccessible`）→ 开设备（`OpenDevice`）→ 设参数 → `StartGrab` → 线程循环 `GetOneFrameTimeout` → 渲染 → `StopGrab`/`CloseDevice`/`Dispose` 释放。也可直接用 `mvdCameraEdit` 相机控件。

**实现步骤**
1. `CCameraTool.EnumDevices` 用 `MVD_TRANSFER_LAYER_TYPE` 枚举（USB + GIGE）。
2. `SelectDevice` + `IsDeviceAccessible(1)` 校验。
3. `OpenDevice` 并 `SetEnumValue` 设采集模式/触发/像素格式。
4. `StartGrab` 并在新线程 `GetStreamThreadProc` 中循环取帧，渲染到 `mvdRenderActivex1`。
5. 停止时 `StopGrab` → `CloseDevice` → `Dispose`，并 `Abort` 线程。

**关键代码**
```csharp
using VisionDesigner.Camera; //引用命名空间
private CCameraTool m_cMyCameraToolObj = null;//定义一个设备对象
Thread m_hReceiveThread = null;//定义取流线程
private bool _bGrabbing = false;

// 打开相机并开始取图方法
public int OpenCamera(int cameraIndex = 0)
{
    try
    {
        if (null == m_cMyCameraToolObj)
        {
            m_cMyCameraToolObj = new CCameraTool();
            if (null == m_cMyCameraToolObj)
            {
                return -1;
            }
        }
        //1、通过MVD_TRANSFER_LAYER_TYPE 类型枚举设备，返回设备个数
        int nRet = CCameraTool.EnumDevices((uint)MVD_TRANSFER_LAYER_TYPE.MVD_USB_DEVICE | (uint)MVD_TRANSFER_LAYER_TYPE.MVD_GIGE_DEVICE);
        if (0 == nRet)
        {
            return -1;
        }
        //2、选择索引的设备并判断是否可达
        m_cMyCameraToolObj.SelectDevice(cameraIndex);
        if (!m_cMyCameraToolObj.IsDeviceAccessible(1))
            return -1;
        //3、打开设备，并设置相机参数(相机参数根据实际需求进行设置)
        m_cMyCameraToolObj.OpenDevice();
        m_cMyCameraToolObj.SetEnumValue("AcquisitionMode", (uint)MVD_CAM_ACQUISITION_MODE.MVD_ACQ_MODE_CONTINUOUS);
        m_cMyCameraToolObj.SetEnumValue("TriggerMode", (uint)MVD_CAM_TRIGGER_MODE.MVD_TRIGGER_MODE_OFF);
        m_cMyCameraToolObj.SetEnumValue("PixelFormat", (uint)MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3);
        //4、开始取图
        m_cMyCameraToolObj.StartGrab();
        _bGrabbing = true;
        m_hReceiveThread = new Thread(GetStreamThreadProc);
        m_hReceiveThread.Start();//启动线程主动取流
        return 0;
    }
    catch (Exception)
    {
        return -1;
    }
}

// 取流线程
private void GetStreamThreadProc()
{
    CMvdImage cFrameImage = new CMvdImage();
    while (_bGrabbing)
    {
        //5、获取一帧图像
        m_cMyCameraToolObj.CameraGrabResult.GetOneFrameTimeout(ref cFrameImage);
        //判断图像格式，将图像加载到UI 界面的控件mvdRenderActivex1上
        if ((VisionDesigner.MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == imgtemp.PixelFormat) || (VisionDesigner.MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == imgtemp.PixelFormat))
        {
            mvdRenderActivex1.LoadImageFromObject(cFrameImage);
            mvdRenderActivex1.Display();
        }
    }
}

// 停止抓图
private void StopGrab()
{
    try
    {
        _bGrabbing = false;
        if (null != m_hReceiveThread)
        {
            m_hReceiveThread.Abort();
            m_hReceiveThread = null;
        }
        //6、停止抓图、关闭设备、释放资源
        m_cMyCameraToolObj.StopGrab();
        m_cMyCameraToolObj.CloseDevice();
        m_cMyCameraToolObj.Dispose();
    }
    catch (Exception ex)
    { }
}
```

**关键 API / 接口名 / 枚举 / 参数**
- `CCameraTool.EnumDevices(uint MVD_TRANSFER_LAYER_TYPE)`、`SelectDevice`、`IsDeviceAccessible`、`OpenDevice`、`SetEnumValue`、`StartGrab`、`StopGrab`、`CloseDevice`、`Dispose`
- `MVD_TRANSFER_LAYER_TYPE.MVD_USB_DEVICE`、`MVD_TRANSFER_LAYER_TYPE.MVD_GIGE_DEVICE`
- `CameraGrabResult.GetOneFrameTimeout(ref CMvdImage)`
- 渲染控件方法：`mvdRenderActivex1.LoadImageFromObject(...)`、`mvdRenderActivex1.Display()`
- 相机控件替代方案：`mvdCameraEdit.GetSubject()` 取得 `CCameraTool` 后调 `GetOneFrameTimeout()`（参考 `Samples\CSharp\ControlSamples\CameraControlDemo`）

**注意事项 / 坑**
- 不熟悉 VM 算子SDK 中相机取流的步骤会出错；注意用 `ref` 取帧、停止时务必释放设备与线程。

---

### 3.2.5 卡尺ROI：卡尺型ROI 的生成方法

**适用场景 / 问题现象**
算子SDK 默认支持的 ROI 类型不包含**直线卡尺 ROI**和**圆卡尺 ROI**，如何生成这两种 ROI 并正确传给算子（直线查找、圆查找）？

**原理 / 关键概念**
- **直线卡尺 ROI**：由「线段（起点+终点）、卡尺数量、卡尺宽、卡尺高」组合生成，产出「卡尺框列表 `List<CMvdRectangleF>` + 最小外接矩形 `CMvdRectangleF`」。
- **圆卡尺 ROI**：由「圆心、半径、卡尺数量、卡尺宽、卡尺高」组合生成，同样产出卡尺框列表 + 最小外接矩形。
- 使用时：算子 `ROI` = 最小外接矩形；`BasicParam.RunningMode = MVD_RUNNING_MODE_ONLY_FIND`；`BasicParam.CaliperList` = 卡尺框列表。

**实现步骤（直线）**
1. `GenLineCaliperROIAlg` 按 `caliperCount` 在起终点连线上等距生成卡尺框，并计算最小外接矩形。
2. 实例化 `CLineFindTool`，设 `InputImage`、`ROI=minRect`、`RunningMode=ONLY_FIND`、`CaliperList`。
3. `SetRunParam("LineFindMode","Best")`、`SetRunParam("EdgePolarity","Both")`，`Run()` 后取 `Result` 绘制。

**关键代码（直线卡尺 ROI 生成）**
```csharp
private void GenLineCaliperROIAlg(MVD_POINT_F startPoint, MVD_POINT_F endPoint, float angle, int caliperCount, float caliperWidth, float caliperHeight, ref List<CMvdRectangleF> cMvdRectangleFList, ref CMvdRectangleF minRect)
{
    CaliperCenters.Clear();

    float fLineHeight = endPoint.fY - startPoint.fY;
    float fLineWidth = endPoint.fX - startPoint.fX;
    float xOffset = fLineWidth / (caliperCount + 1);
    float yOffset = fLineHeight / (caliperCount + 1);

    float fRotateAngle = angle;
    MVD_POINT_F stCenter = new MVD_POINT_F();
    CMvdRectangleF rectangleF;
    // 生成卡尺框列表
    for (int i = 1; i < caliperCount + 1; i++)
    {
        stCenter.fX = startPoint.fX + xOffset * i;
        stCenter.fY = startPoint.fY + yOffset * i;
        CaliperCenters.Add(stCenter);
        rectangleF = new CMvdRectangleF(stCenter.fX, stCenter.fY, caliperWidth, caliperHeight);
        rectangleF.Angle = fRotateAngle;
        rectangleF.BorderColor = blue;
        cMvdRectangleFList.Add(rectangleF);
    }

    // 生成最小外接矩形
    float LineMidX = (float)(0.5 * (endPoint.fX + startPoint.fX));
    float LineMidY = (float)(0.5 * (endPoint.fY + startPoint.fY));
    minRect = new CMvdRectangleF(LineMidX, LineMidY, fLineWidth, caliperHeight);
    minRect.Angle = fRotateAngle;
}
```

**关键代码（直线卡尺 ROI 使用）**
```csharp
private List<CMvdRectangleF> cMvdRectangleFs = new List<CMvdRectangleF>();
cMvdRectangleFs.Clear();

CMvdRectangleF minRect = new CMvdRectangleF(cMvdImage.Width / 2, cMvdImage.Height / 2, cMvdImage.Width / 4, cMvdImage.Height / 4);
MVD_POINT_F lineStartPoint = new MVD_POINT_F(1700, 1122);
MVD_POINT_F lineEndPoint = new MVD_POINT_F(2286, 1122);
float angleRad = (float)Math.Atan2((lineEndPoint.fY - lineStartPoint.fY), (lineEndPoint.fX - lineStartPoint.fX));
float angle = (float)(angleRad / Math.PI * 180.0);
GenLineCaliperROIAlg(lineStartPoint, lineEndPoint, angle, caliperCount, caliperWidth, caliperHeight, ref cMvdRectangleFs, ref minRect);

// 直线查找
CLineFindTool cLineFindTool = new CLineFindTool();
cLineFindTool.InputImage = cMvdImage;
cLineFindTool.ROI = minRect;
cLineFindTool.BasicParam.RunningMode = VisionDesigner.LineFind.MVD_RUNNING_MODE.MVD_RUNNING_MODE_ONLY_FIND; // 查找结果受ROI 和CaliperList 影响
cLineFindTool.BasicParam.CaliperList = cMvdRectangleFs;
cLineFindTool.SetRunParam("LineFindMode", "Best");
cLineFindTool.SetRunParam("EdgePolarity", "Both");
cLineFindTool.Run();

CLineFindResult cLineFindRes = cLineFindTool.Result;
List<CLineFindEdgePointInfo> cLineFindEdgePointInfos = cLineFindRes.EdgePointInfo;

// 直线轮廓点
CMvdPointSetF lineEdgePoint = new CMvdPointSetF();
lineEdgePoint.BorderColor = green;
for (int i = 0; i < cLineFindEdgePointInfos.Count; i++)
{
    lineEdgePoint.AddPoint(cLineFindEdgePointInfos[i].EdgePoint.fX, cLineFindEdgePointInfos[i].EdgePoint.fY, i);
}
mvdRenderActivex1.AddShape(lineEdgePoint);

// 输出直线
CMvdLineSegmentF line = new CMvdLineSegmentF(new MVD_POINT_F(cLineFindRes.LineStartPoint.fX, cLineFindRes.LineStartPoint.fY), new MVD_POINT_F(cLineFindRes.LineEndPoint.fX, cLineFindRes.LineEndPoint.fY));
line.BorderColor = green;
mvdRenderActivex1.AddShape(line);

// 直线卡尺框
for (int i = 0; i < caliperCount; i++)
{
    mvdRenderActivex1.AddShape(cMvdRectangleFs[i]);
}

// 直线检测区域
minRect.BorderColor = blue;
mvdRenderActivex1.AddShape(minRect);
mvdRenderActivex1.Display();
```

**关键代码（圆卡尺 ROI 生成）**
```csharp
private void GenCircleCaliperROIAlg(MVD_POINT_F centerPoint, float radius, int caliperCount, float caliperWidth, float caliperHeight, ref List<CMvdRectangleF> cMvdRectangleFList, ref CMvdRectangleF minRect)
{
    CaliperCenters.Clear();

    float angleOffset = 360.0f / caliperCount;
    float angleStart = 180.0f / caliperCount;

    MVD_POINT_F stCenter = new MVD_POINT_F();
    CMvdRectangleF rectangleF;
    // 生成卡尺框列表
    for (int i = 0; i < caliperCount; i++)
    {
        float fRotateAngle = angleStart + angleOffset * i;
        if (fRotateAngle > 180.0f)
        {
            fRotateAngle -= 360.0f;
        }
        stCenter.fX = (float)(radius * Math.Cos(fRotateAngle / 180.0f * Math.PI) + centerPoint.fX);
        stCenter.fY = (float)(radius * Math.Sin(fRotateAngle / 180.0f * Math.PI) + centerPoint.fY);
        CaliperCenters.Add(stCenter);
        rectangleF = new CMvdRectangleF(stCenter.fX, stCenter.fY, caliperHeight, caliperWidth);
        rectangleF.Angle = fRotateAngle;
        rectangleF.BorderColor = blue;
        cMvdRectangleFList.Add(rectangleF);
    }

    // 生成最小外接矩形
    float CircleMidX = centerPoint.fX;
    float CircleMidY = centerPoint.fY;
    minRect = new CMvdRectangleF(CircleMidX, CircleMidY, (float)(2 * radius + caliperHeight), (float)(2 * radius + caliperHeight));
    minRect.Angle = 0.0f;
}
```

**关键代码（圆卡尺 ROI 使用）**
```csharp
private List<CMvdRectangleF> cMvdRectangleFs = new List<CMvdRectangleF>();
cMvdRectangleFs.Clear();

CMvdRectangleF minRect = new CMvdRectangleF(cMvdImage.Width / 2, cMvdImage.Height / 2, cMvdImage.Width / 4, cMvdImage.Height / 4);
MVD_POINT_F circleCenter = new MVD_POINT_F(2258, 1961);
float circleRadius = 357;
GenCircleCaliperROIAlg(circleCenter, circleRadius, caliperCount, caliperWidth, caliperHeight, ref cMvdRectangleFs, ref minRect);

// 圆查找
CCircleFindTool cCircleFindTool = new CCircleFindTool();
cCircleFindTool.InputImage = cMvdImage;
cCircleFindTool.ROI = minRect;
cCircleFindTool.BasicParam.RunningMode = VisionDesigner.CircleFind.MVD_RUNNING_MODE.MVD_RUNNING_MODE_ONLY_FIND; // 查找结果受ROI 和CaliperList 影响
cCircleFindTool.BasicParam.CaliperList = cMvdRectangleFs;
float fMinRadius = (float)(circleRadius - 0.5 * caliperHeight);
float fMaxRadius = (float)(circleRadius + 0.5 * caliperHeight);
cCircleFindTool.SetRunParam("MinRadius", Convert.ToInt32(fMinRadius).ToString());
cCircleFindTool.SetRunParam("MaxRadius", Convert.ToInt32(fMaxRadius).ToString());
cCircleFindTool.SetRunParam("EdgeThresh", "15");
cCircleFindTool.SetRunParam("CircleFindMode", "Best");
cCircleFindTool.SetRunParam("EdgePolarity", "WhiteToBlack");
cCircleFindTool.SetRunParam("RejectNum", "0");
cCircleFindTool.SetRunParam("RejectDist", "5");
cCircleFindTool.Run();

CCircleFindResult cCircleFindRes = cCircleFindTool.Result;
List<CCircleFindEdgePointInfo> cCircleFindEdgePointInfos = cCircleFindRes.EdgePointInfo;

// 圆轮廓点
CMvdPointSetF circleEdgePoint = new CMvdPointSetF();
circleEdgePoint.BorderColor = green;
for (int i = 0; i < cCircleFindEdgePointInfos.Count; i++)
{
    circleEdgePoint.AddPoint(cCircleFindEdgePointInfos[i].EdgePoint.fX, cCircleFindEdgePointInfos[i].EdgePoint.fY, i);
}
mvdRenderActivex1.AddShape(circleEdgePoint);

// 输出圆环
CMvdCircleF circle = new CMvdCircleF(cCircleFindRes.Circle.Center, cCircleFindRes.Circle.Radius);
circle.BorderColor = green;
mvdRenderActivex1.AddShape(circle);

// 输出ROI 圆弧
CMvdAnnularSectorF circleAnnu = new CMvdAnnularSectorF(circleCenter, fMinRadius, fMaxRadius, 0.0f, 360.0f);
circleAnnu.BorderColor = blue;
mvdRenderActivex1.AddShape(circleAnnu);

// 圆卡尺框
for (int i = 0; i < caliperCount; i++)
{
    mvdRenderActivex1.AddShape(cMvdRectangleFs[i]);
}

// 圆检测区域
minRect.BorderColor = blue;
mvdRenderActivex1.AddShape(minRect);
mvdRenderActivex1.Display();
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CLineFindTool`（`VisionDesigner.LineFind`）、`CCircleFindTool`（`VisionDesigner.CircleFind`）
- 运行模式枚举：`MVD_RUNNING_MODE.MVD_RUNNING_MODE_ONLY_FIND`
- 卡尺相关：`BasicParam.CaliperList`（`List<CMvdRectangleF>`）、ROI 即最小外接矩形
- 形类型：`CMvdRectangleF`、`CMvdPointSetF`、`CMvdLineSegmentF`、`CMvdCircleF`、`CMvdAnnularSectorF`、`MVD_POINT_F`
- 字符串运行参数：`LineFindMode`/`EdgePolarity`（直线）、`MinRadius`/`MaxRadius`/`EdgeThresh`/`CircleFindMode`/`EdgePolarity`/`RejectNum`/`RejectDist`（圆）

**注意事项 / 坑**
- 默认 ROI 类型不包含卡尺型，必须自行生成卡尺框列表与最小外接矩形。
- 运行模式必须设为 `ONLY_FIND`，否则结果不受 `ROI` 与 `CaliperList` 影响。

---

### 3.2.6 DL 算子耗时：深度学习算子长时间停止再运行耗时变长问题的解决方法

**适用场景 / 问题现象**
深度学习算子长时间停止后再运行，第一次运行耗时明显变长，如何解决？

**原理 / 关键概念**
原因是显卡休眠：深度学习算子运行前需初始化 CUDA 资源，首次耗时长；长时间停止导致显卡休眠，再次运行需重新唤醒。需周期性用 CUDA 操作唤醒显卡防止休眠。

**实现步骤**
1. 启动一个独立进程/线程，周期性（如每 10s）执行一次 CUDA `cudaMemcpy` 主机→设备拷贝。
2. 进程持续运行即可防止软件空闲时显卡休眠。

**关键代码**
```cpp
int main()
{
    printf("====================Awake Gpu start=======================\n");

    // 覆盖写入文件，不必删除文件
    std::ofstream outFile("AwakenGPUToolLog.txt");
    outFile << "Awake Gpu start" << std::endl;

    //开启线程进行防GPU 空闲
    int       data_c[2] = { 0 };
    int      *data_g = NULL;
    int                        gpu_count = 0;
    cudaError_t                    err = cudaSuccess;
    struct cudaDeviceProp          prop = { 0 };

    do
    {
        err = cudaGetDeviceCount(&gpu_count);
        if ((cudaSuccess != err) || (1 > gpu_count))
        {
            printf("Have no cuda device.err = %d\n", err);
            outFile << "Have no cuda device, err = " << err << std::endl;
            break;
        }

        err = cudaMalloc((void**)&data_g, sizeof(int));
        if (cudaSuccess != err)
        {
            printf("Cuda malloc error. err = %d\n", err);
            outFile << "Cuda malloc error, err = " << err << std::endl;
            break;
        }

        outFile << "GPU OK." << std::endl;

        while (1)
        {
            Sleep(10000);

            err = cudaMemcpy(data_g, data_c, sizeof(int), cudaMemcpyHostToDevice);
            if (cudaSuccess != err)
            {
                printf("Cuda memcpy error.\n");
                outFile << "Cuda memcpy error, err = " << err << std::endl;
                continue;
            }

            printf("GPU OK.\n");
        }
    } while (false);

    outFile << "Awake Gpu end." << std::endl;
    if (NULL != data_g)
    {
        cudaFree(data_g);
        data_g = NULL;
    }
    outFile.close();

    //system("Pause");
    return 0;
}
```

**关键 API / 接口名 / 枚举 / 参数**
- CUDA Runtime API：`cudaGetDeviceCount`、`cudaMalloc`、`cudaMemcpy`（方向 `cudaMemcpyHostToDevice`）、`cudaFree`、`cudaDeviceProp`
- 唤醒周期：示例 `Sleep(10000)`（10 秒）

**注意事项 / 坑**
- 不熟悉显卡唤醒方法会误以为算子性能问题；本质为显卡休眠，需常驻轻量 CUDA 操作保活。

---

## 3.3 模块工具类

### 3.3.1 位置修正：位置修正算子工具的使用方法

**适用场景 / 问题现象**
如何使用位置修正（`CPositionFixTool`）工具，根据基准点与运行点把源 ROI 修正到新位置？

**原理 / 关键概念**
位置修正基于「基准点 `BasePoint`（模板匹配得到的基准位置/角度）+ 运行点 `RunningPoint`（当前图像中的实际位置/角度）」，以 `FixMode`（如 `MVD_POSFIX_MODE_HVA`，平移+旋转+缩放）计算仿射变换，输出 `Result.CorrectedShape`。

**实现步骤**
1. 实例化 `CPositionFixTool`，取 `BasicParam`。
2. 设 `BasePoint`（基准点，含 `stPosition.fX/fY`、`fAngle`）。
3. 设 `RunningPoint`（运行点）。
4. 设 `RunImageSize`、`FixMode`、`InitialShape`（待修正的源 ROI `SrcRegionROI`）。
5. `Run()` 后从 `Result.CorrectedShape` 取修正后的 ROI。

**关键代码**
```csharp
bool re = true;
//位置修正基准参数
CPositionFixTool PosFixToolObj = new CPositionFixTool();
CPositionFixBasicParam BasicParam = PosFixToolObj.BasicParam;
VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F stBasinInit = new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F();
stBasinInit.stPosition.fX = MatchPoint.X;
stBasinInit.stPosition.fY = MatchPoint.Y;
stBasinInit.fAngle = Angle;
BasicParam.BasePoint = stBasinInit;//设置基准点
//位置修正运行参数
VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F stBasicRun = new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F();
stBasicRun.stPosition.fX = stPositionfX;
stBasicRun.stPosition.fY = stPositionfY;
stBasicRun.fAngle = stPositionAngle;
BasicParam.RunningPoint = stBasicRun;//设置运行点
//获取工具位置修正后Roi
MVD_SIZE_I stImageSize = new MVD_SIZE_I();
stImageSize.nWidth = ImageWidth;
stImageSize.nHeight = ImageHeight;
BasicParam.RunImageSize = stImageSize;
BasicParam.FixMode = MVD_POSFIX_MODE.MVD_POSFIX_MODE_HVA;
PosFixToolObj.BasicParam.InitialShape = SrcRegionROI;
PosFixToolObj.Run();
DesRegionROI = PosFixToolObj.Result.CorrectedShape;
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CPositionFixTool`、`CPositionFixBasicParam`
- 结构：`MVD_FIDUCIAL_POINT_F`（`stPosition.fX/fY`、`fAngle`）、`MVD_SIZE_I`（`nWidth/nHeight`）
- 属性：`BasePoint`、`RunningPoint`、`RunImageSize`、`FixMode`、`InitialShape`
- 修正模式枚举：`MVD_POSFIX_MODE.MVD_POSFIX_MODE_HVA`
- 结果：`PosFixToolObj.Result.CorrectedShape`

**注意事项 / 坑**
- 不熟悉位置修正算子工具使用方法会导致 ROI 不随物体位置变化而更新。

---

### 3.3.2 模板保存：实现模板自动加载的方法

**适用场景 / 问题现象**
模板匹配功能希望在程序运行时自动加载之前训练过的模板，如何实现？

**原理 / 关键概念**
模板支持导入/导出：`ImportPattern(path)` 加载模板文件，`ExportPattern(path)` 保存模板文件。配合训练窗口 `mvdAlmightyPatternEdit1.SetSubject(pattern)` 绑定同一个 `pattern` 对象。

**实现步骤**
1. 程序初始化（`FrmMain` 构造）：若模板文件存在，`pattern.ImportPattern(savePatternPath)`。
2. 训练窗口加载（`FrmTempleteMatch_Load`）：`mvdAlmightyPatternEdit1.SetSubject(savePattern)` 绑定。
3. 关闭训练窗口（`FrmTempleteMatch_FormClosing`）：`savePattern.ExportPattern(savePatternPath)` 导出。

**关键代码**
```csharp
// 第一步：程序初始化时导入模板
public FrmMain()
{
    InitializeComponent();
    if (File.Exists(savePatternPath))//判断文件是否存在
    {
        pattern.ImportPattern(savePatternPath);
    }
}

// 第二步：加载模板训练窗口时进行赋值
private void FrmTempleteMatch_Load(object sender, EventArgs e)
{
    mvdAlmightyPatternEdit1.SetSubject(savePattern);
}

// 第三步：在关闭训练窗口时导出模板
private void FrmTempleteMatch_FormClosing(object sender, FormClosingEventArgs e)
{
    savePattern.ExportPattern(savePatternPath);
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 模板方法：`ImportPattern(string)`、`ExportPattern(string)`
- 训练控件：`mvdAlmightyPatternEdit1.SetSubject(pattern)`

**注意事项 / 坑**
- 不熟悉 SDK 算子的相关方法会无法实现模板持久化。

---

### 3.3.3 模板匹配：获取模板匹配框和轮廓点的方法

**适用场景 / 问题现象**
如何获取模板匹配的匹配框（`MatchBox`）与轮廓点（`OutlineList`）并渲染？

**原理 / 关键概念**
模板匹配工具 `CHPFeaturePatMatchTool` 设 `Pattern`、`ROI`、`ShowOutlineStatus=true` 后 `Run()`；结果 `Result.MatchInfoList` 含各匹配项的 `MatchBox`，`Result.OutlineList` 含轮廓点（`EdgePointList`，按 `Score` 区分绿/黄/红）。

**实现步骤**
1. 实例化 `CHPFeaturePattern`、设 `InputImage`、`Pattern`、`ROI`、`ShowOutlineStatus=true`。
2. `Run()` 后遍历 `MatchInfoList` 画匹配框。
3. 若开启轮廓显示，遍历 `OutlineList` 的 `EdgePointList`，按 `Score` 收集绿/黄/红点集并 `AddShape`。

**关键代码**
```csharp
cHPFeaturePattern = new CHPFeaturePattern();
cHPFeaturePatMatchTool.InputImage = cMvdImage;
cHPFeaturePatMatchTool.Pattern = cHPFeaturePattern;
cHPFeaturePatMatchTool.ROI = cROI;
cHPFeaturePatMatchTool.BasicParam.ShowOutlineStatus = true; // 显示轮廓
cHPFeaturePatMatchTool.Run();
CHPFeaturePatMatchResult cHPFeaturePatMatchResult = cHPFeaturePatMatchTool.Result;
var OutlineList = cHPFeaturePatMatchResult.OutlineList;
foreach (var item in cHPFeaturePatMatchResult.MatchInfoList)
{
    var matchBox = new CMvdRectangleF(item.MatchBox.CenterX, item.MatchBox.CenterY, item.MatchBox.Width, item.MatchBox.Height);
    matchBox.Angle = item.MatchBox.Angle;
    matchBox.BorderColor = new MVD_COLOR(255, 0, 0, 255);
    mvdRenderActivex1.AddShape(matchBox);
}
if (cHPFeaturePatMatchTool.BasicParam.ShowOutlineStatus)
{
    foreach (var item in cHPFeaturePatMatchResult.OutlineList)
    {
        CMvdPointSetF pointSetG = new CMvdPointSetF();
        CMvdPointSetF pointSetY = new CMvdPointSetF();
        CMvdPointSetF pointSetR = new CMvdPointSetF();
        foreach (var point in item.EdgePointList)
        {
            if (0 == point.Score)
            {
                pointSetG.AddPoint(point.Position.fX, point.Position.fY);
            }
            else if (1 == point.Score)
            {
                pointSetY.AddPoint(point.Position.fX, point.Position.fY);
            }
            else if (2 == point.Score)
            {
                pointSetR.AddPoint(point.Position.fX, point.Position.fY);
            }
        }
        pointSetG.BorderColor = new MVD_COLOR(0, 255, 0, 255);//绿色得分高的点
        pointSetY.BorderColor = new MVD_COLOR(255, 255, 0, 255);//黄色得分低的点
        pointSetR.BorderColor = new MVD_COLOR(255, 0, 0, 255);//红色丢弃的点

        if (0 != pointSetG.PointsList.Count)
        {
            mvdRenderActivex1.AddShape(pointSetG);
            matchOutlineList.Add(pointSetG);
        }

        if (0 != pointSetY.PointsList.Count)
        {
            mvdRenderActivex1.AddShape(pointSetY);
            matchOutlineList.Add(pointSetY);
        }

        if (0 != pointSetR.PointsList.Count)
        {
            mvdRenderActivex1.AddShape(pointSetR);
            matchOutlineList.Add(pointSetR);
        }
    }
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CHPFeaturePatMatchTool`、`CHPFeaturePattern`、`CHPFeaturePatMatchResult`
- 属性/方法：`Pattern`、`ROI`、`BasicParam.ShowOutlineStatus`、`Result.MatchInfoList`（每项 `MatchBox.CenterX/CenterY/Width/Height/Angle`）、`Result.OutlineList`（每项 `EdgePointList`，点含 `Position.fX/fY`、`Score`）
- 渲染：`CMvdRectangleF`、`CMvdPointSetF`、`MVD_COLOR`

**注意事项 / 坑**
- 不熟悉如何获取匹配框和匹配点会导致无法渲染匹配结果。

---

### 3.3.4 模板训练：模板训练执行完成的判断方法

**适用场景 / 问题现象**
打开模板匹配后未训练模板，但模板状态不为 `null`，如何判断模板训练是否真正完成？

**原理 / 关键概念**
模板是否训练**不应以是否为 `null` 判断**；应以模板结果是否为空判断。

**实现步骤**
使用以下三个判断（任一即可表征训练状态）：
- `pattern != null`：判断是否创建了模板对象；
- `pattern.ReginList.Count != 0`：判断训练区域个数是否大于 0；
- `pattern1.GetPatternResult() != null`：判断模板是否训练成功。

**关键代码**
```csharp
if(pattern != null){}//判断模板是否为空
if(pattern.ReginList.Count != 0){}//判断模板训练的区域个数是否为0
if( pattern1.GetPatternResult() != null){}//判断模板是否训练成功
```

**关键 API / 接口名 / 枚举 / 参数**
- 模板属性/方法：`ReginList`、`GetPatternResult()`

**注意事项 / 坑**
- 不熟悉 SDK 算子的相关方法会误用 `null` 判断训练完成，导致逻辑错误。

---

### 3.3.5 图像相减：算子SDK 开发图像相减的方法

**适用场景 / 问题现象**
WinForm 下如何对两幅同尺寸图像做差（`image1` 基准图，`image2` 图像修正后的图）？

**原理 / 关键概念**
逐像素取绝对值差：`diff = |image1 - image2|`，要求两图 `Width/Height/PixelFormat` 一致，结果写入新 `CMvdImage` 的 `arrDataBytes`。

**实现步骤**
1. 判定两图尺寸/格式一致。
2. 新建 `diffImage` 并 `InitImage(w,h,pixelFormat)`。
3. 按 `nRowStep` 遍历像素，`diffImage` 像素 = `Math.Abs(image1 - image2)`。

**关键代码**
```csharp
if (image1.Width == image2.Width && image1.Height == image2.Height && image1.PixelFormat == image2.PixelFormat)
{
    CMvdImage diffImage = new CMvdImage();
    diffImage.InitImage(image1.Width, image1.Height, image1.PixelFormat);
    for (uint row = 0; row < image1.Height; row++)
    {
        uint nStep = image1.GetImageData(0).nRowStep;
        for (uint col = 0; col < nStep; col++)
        {
            diffImage.GetImageData(0).arrDataBytes[row * nStep + col] = (byte)Math.Abs(image1.GetImageData(0).arrDataBytes[row * nStep + col] - image2.GetImageData(0).arrDataBytes[row * nStep + col]);
        }
    }
    return diffImage;
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CMvdImage`
- 方法/属性：`InitImage(int,int,MVD_PIXEL_FORMAT)`、`GetImageData(0).nRowStep`、`GetImageData(0).arrDataBytes`

**注意事项 / 坑**
- 不熟悉 SDK 算子的相关方法会导致像素访问越界或格式不一致错误。

---

### 3.3.6 图像修正：图像修正工具的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用图像修正（`CImageFixtureTool`）工具？

**原理 / 关键概念**
图像修正与位置修正同源：基于基准点 `BasePoint` 与运行点 `RunningPoint`，按 `FixMode`（`MVD_IMGFIX_MODE_HVA`）对整幅图像做仿射变换。

**实现步骤**
1. 实例化 `CImageFixtureTool`，设 `InputImage`。
2. 设 `BasicParam.FixMode`、`BasePoint`、`RunningPoint`。
3. `Run()`。

**关键代码**
```csharp
CImageFixtureTool tool = new CImageFixtureTool();
tool.InputImage = inputImage;
tool.BasicParam.FixMode = MVD_IMGFIX_MODE.MVD_IMGFIX_MODE_HVA;
tool.BasicParam.BasePoint = new VisionDesigner.ImageFixture.MVD_FIDUCIAL_POINT_F(basePoint, baseAngle);//基准点
tool.BasicParam.RunningPoint = new VisionDesigner.ImageFixture.MVD_FIDUCIAL_POINT_F(runPoint, runAngle);//运行点
tool.Run();
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CImageFixtureTool`
- 结构：`VisionDesigner.ImageFixture.MVD_FIDUCIAL_POINT_F`
- 枚举：`MVD_IMGFIX_MODE.MVD_IMGFIX_MODE_HVA`
- 属性：`BasicParam.FixMode`、`BasePoint`、`RunningPoint`

**注意事项 / 坑**
- 不熟悉 SDK 算子的相关方法会参数配置错误。

---

### 3.3.7 Blob 工具：Blob 工具的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用 Blob 分析（`CBlobFindTool`）工具，并配合位置修正绘制 Blob 框？

**原理 / 关键概念**
Blob 工具设输入图像、ROI（可选）、极性/阈值/面积等运行参数后 `Run()`；`Result.BlobInfo` 为各连通域信息（含 `BoxInfo` 外接矩形）。常配合 `CPositionFixTool` 把 Blob 框修正到基准坐标系。

**实现步骤**
1. 实例化 `CBlobFindTool`，开 `ShowOutlineStatus`/`ShowBlobImageStatus`。
2. 设 `InputImage`、`ROI`（可选）、`SetRunParam` 极性/阈值/面积。
3. `Run()` 取 `Result.BlobInfo`。
4. 对每个 `BlobInfo.BoxInfo` 用位置修正工具修正后 `AddShape` 渲染。

**关键代码**
```csharp
CBlobFindTool tool = new CBlobFindTool();
tool.BasicParam.ShowOutlineStatus = true;
tool.BasicParam.ShowBlobImageStatus = true;
tool.InputImage = inputImage;
if (BlobRoi != null){  tool.ROI = BlobRoi;}
tool.SetRunParam("Polarity", "BrightObject");//Blob 工具参数设置
tool.SetRunParam("LowThreshold", "180");
tool.SetRunParam("HightThreshold", "255");
tool.SetRunParam("MinArea", "5");
tool.SetRunParam("MaxArea", "5000");
tool.Run();
List<CBlobInfo> blobInfoList = tool.Result.BlobInfo;
CPositionFixTool fixTool = new CPositionFixTool();//位置修正
fixTool.BasicParam.BasePoint = new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F(basePoint, baseAngle);
fixTool.BasicParam.RunImageSize = new MVD_SIZE_I((int)inputImage.Width, (int)inputImage.Height);
mvdRenderActivex1.ClearShapes();
foreach (var blobInfo in blobInfoList)//绘制blob 框数据
{
    CMvdRectangleF rectangleF = blobInfo.BoxInfo;
    rectangleF.BorderColor = new MVD_COLOR(0xFF, 0x00, 0x00);
    rectangleF.BorderWidth = 2;
    fixTool.BasicParam.InitialShape = rectangleF;
    fixTool.BasicParam.RunningPoint = new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F(runPoint, runAngle);
    fixTool.BasicParam.FixMode = MVD_POSFIX_MODE.MVD_POSFIX_MODE_HVA;
    fixTool.Run();
    mvdRenderActivex1.AddShape(fixTool.Result.CorrectedShape);
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CBlobFindTool`、`CBlobInfo`、`CPositionFixTool`
- Blob 运行参数（字符串）：`Polarity`（`BrightObject`）、`LowThreshold`、`HightThreshold`、`MinArea`、`MaxArea`
- 结果属性：`Result.BlobInfo`（每项 `BoxInfo` 为 `CMvdRectangleF`）、`ShowOutlineStatus`、`ShowBlobImageStatus`
- 位置修正：`MVD_POSFIX_MODE.MVD_POSFIX_MODE_HVA`、`MVD_SIZE_I`、`Result.CorrectedShape`

**注意事项 / 坑**
- 不熟悉相关接口的使用会导致 Blob 框不渲染或修正失败。

---

### 3.3.8 点点测量：点点测量工具的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用点点测量（`CP2PMeasureTool`）工具？示例：测量两个圆的圆心距。

**原理 / 关键概念**
点点测量设两个 `Point`（来自其他工具结果），`Run()` 后 `Result.Dist()` 返回两点距离。

**实现步骤**
1. 实例化 `CP2PMeasureTool`。
2. 设 `BasicParam.Point1`、`Point2`（如 `CCircleFindTool.Result.CircleCenter`）。
3. `Run()`，`distance = Result.Dist()`。

**关键代码**
```csharp
float distance;
VisionDesigner.P2PMeasure.CP2PMeasureTool cP2PMeasureTool = new VisionDesigner.P2PMeasure.CP2PMeasureTool();
cP2PMeasureTool.BasicParam.Point1 = cCirFindTool1.Result.CircleCenter;
cP2PMeasureTool.BasicParam.Point2 = cCirFindTool2.Result.CircleCenter;
cP2PMeasureTool.Run();
distance = cP2PMeasureTool.Result.Dist();
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.P2PMeasure.CP2PMeasureTool`
- 属性：`BasicParam.Point1`、`BasicParam.Point2`
- 结果方法：`Result.Dist()`

**注意事项 / 坑**
- 不熟悉相关接口的使用会导致坐标取错。

---

### 3.3.9 亮度测量：亮度测量工具的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用亮度测量（`CIntensityToolTool`）工具？

**原理 / 关键概念**
亮度测量需设输入图像与 ROI，结果包含 ROI 内亮度统计（均值等）。

**实现步骤**
1. 实例化 `CIntensityToolTool`，`InitImage` 载入输入图。
2. 设 `InputImage`、`ROI`（中心矩形）。
3. `Run()`。

**关键代码**
```csharp
VisionDesigner.IntensityTool.CIntensityToolTool cIntensityToolTool = new VisionDesigner.IntensityTool.CIntensityToolTool();
VisionDesigner.CMvdImage InputImg = new CMvdImage();
InputImg.InitImage("Input.bmp");
cIntensityToolTool.InputImage = InputImg;
cIntensityToolTool.ROI = new VisionDesigner.CMvdRectangleF(InputImg.Width / 2, InputImg.Height / 2, InputImg.Width / 4, InputImg.Height / 4);
cIntensityToolToolObj.Run();
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.IntensityTool.CIntensityToolTool`
- 属性：`InputImage`、`ROI`

**注意事项 / 坑**
- 不熟悉相关接口的使用会导致 ROI 未设置或运行失败。

---

### 3.3.10 圆查找：圆查找的方法

**适用场景 / 问题现象**
WinForm 下如何使用圆查找（`CCircleFindTool`）算子？

**原理 / 关键概念**
圆查找标准流程：初始化参数（含 `SaveConfiguration` 保存参数）→ 加载图像设 ROI → `Run()` → 取 `CCircleFindResult`。

**实现步骤**
1. 初始化：实例化 `CCircleFindTool`，`InitImage` 载入，`Set ROI`（可选），`SaveConfiguration` 保存参数（缓冲区不足时按返回长度扩容重试）。
2. 加载图片并 `Run()`。
3. 取 `CCircleFindResult`（`m_CircleFindTool.Result`）。

**关键代码**
```csharp
//第一步，初始化参数
try
{
    VisionDesigner.CircleFind.CCircleFindTool m_cCircleFindToolObj = new VisionDesigner.CircleFind.CCircleFindTool();
    //Set input image
    VisionDesigner.CMvdImage cInputImg = new CMvdImage();
    cInputImg.InitImage("InputTest.bmp");
    m_cCircleFindToolObj.InputImage = cInputImg;
    // Set ROI region (optional)
    m_cCircleFindToolObj.ROI = new VisionDesigner.CMvdRectangleF(cInputImg.Width / 2, cInputImg.Height / 2, cInputImg.Width / 4, cInputImg.Height / 4);
    //保存参数设置
    byte[] fileBytes = new byte[256];
    uint nConfigDataSize = 256;
    uint nConfigDataLen = 0;
    try
    {
        m_cCircleFindToolObj.SaveConfiguration(fileBytes, nConfigDataSize, ref nConfigDataLen);
    }
    catch (MvdException ex)
    {
        if (MVD_ERROR_CODE.MVD_E_NOENOUGH_BUF == ex.ErrorCode)
        {
            fileBytes = new byte[nConfigDataLen];
            nConfigDataSize = nConfigDataLen;
            m_cCircleFindToolObj.SaveConfiguration(fileBytes, nConfigDataSize, ref nConfigDataLen);
        }
        else
        {
            throw ex;
        }
    }
}
//第二步，加载图片并运行
m_cCircleFindToolObj.Run();
//输出结果
CCircleFindResult circleFindResult = m_CircleFindTool.Result;
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.CircleFind.CCircleFindTool`、`CCircleFindResult`
- 方法：`InitImage`、`SaveConfiguration(byte[], uint, ref uint)`、`Run`
- 错误码枚举：`MVD_ERROR_CODE.MVD_E_NOENOUGH_BUF`
- 属性：`InputImage`、`ROI`

**注意事项 / 坑**
- 问题原因多为参数设置错误；`SaveConfiguration` 缓冲不足需按 `nConfigDataLen` 扩容。

---

### 3.3.11 仿射变换：图像仿射变换的使用方法

**适用场景 / 问题现象**
WinForm 下如何使用图像仿射变换（`CImageAffineTransformTool`）工具？

**原理 / 关键概念**
仿射变换设 `Aspect`（纵横比）、`InputImage`、`ROIShape` 后 `Run()`，`Result.OutputImage` 为变换后图像。

**实现步骤**
1. 初始化：实例化 `CImageAffineTransformTool`，`SaveConfiguration` 保存参数。
2. 设运行参数（`BasicParam.Aspect`）、`InputImage`、`ROIShape`。
3. `Run()`，取 `Result.OutputImage`。

**关键代码**
```csharp
//第一步，设置参数
//定义仿射变换工具对象
m_stImageAffineTransformToolObj = new CImageAffineTransformTool();
//可修改参数
byte[] fileBytes = new byte[256];
uint nConfigDataSize = 256;
uint nConfigDataLen = 0;
//保存参数
m_stImageAffineTransformToolObj.SaveConfiguration(fileBytes, nConfigDataSize, ref nConfigDataLen);
//设置运行参数，输入图像，ROI 面积等，运行
m_stImageAffineTransformToolObj.BasicParam.Aspect = fAspectValue;
m_stImageAffineTransformToolObj.InputImage = m_stInputImage;
m_stImageAffineTransformToolObj.ROIShape = cDefaultRect;
m_stImageAffineTransformToolObj.Run();
//输出结果
CMvdImage stOutputImage = m_stImageAffineTransformToolObj.Result.OutputImage;
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CImageAffineTransformTool`
- 属性：`BasicParam.Aspect`、`InputImage`、`ROIShape`
- 结果：`Result.OutputImage`

**注意事项 / 坑**
- 问题原因多为参数设置错误或缺少参数设置。

---

### 3.3.12 直线查找：直线查找工具的使用方法

**适用场景 / 问题现象**
如何进行直线查找？工具入口是 `CEdgeFindTool`（原文指出直线查找工具入口为 `xxxTool`，直线查找即 `CEdgeFindTool`）。

**原理 / 关键概念**
创建 `CEdgeFindTool` 对象 → 设 `InputImage` → 设 `ROI` → `Run()` → 从 `Result.SingleEdgeInfo` 取边缘点及得分。

**实现步骤**
1. 创建 `CEdgeFindTool` 对象。
2. `InitImage` 载入输入图，`InputImage` 赋值。
3. 设 `ROI`（中心矩形）。
4. `Run()`，取 `Result.SingleEdgeInfo` 遍历得分。

**关键代码**
```csharp
// 创建对象
VisionDesigner.EdgeFind.CEdgeFindTool cEdgeFindToolObj = new VisionDesigner.EdgeFind.CEdgeFindTool();
// 给定输入图片
VisionDesigner.CMvdImage cInputImg = new CMvdImage();
cInputImg.InitImage("..\\InputTest.bmp");
cEdgeFindToolObj.InputImage = cInputImg;
// 设置ROI
cEdgeFindToolObj.ROI = new VisionDesigner.CMvdRectangleF(cInputImg.Width / 2, cInputImg.Height / 2, cInputImg.Width / 4, cInputImg.Height / 4);
// 运行
cEdgeFindToolObj.Run();
// 获取结果
VisionDesigner.EdgeFind.CEdgeFindResult cEdgeFindRes = cEdgeFindToolObj.Result;
Console.WriteLine("The number of edge: {0}", cEdgeFindRes.SingleEdgeInfo.Count);
List<CEdgeFindSingleEdgeInfo> lstEdgePtInfo = cEdgeFindRes.SingleEdgeInfo;
foreach (CEdgeFindSingleEdgeInfo cCurEdgePt in lstEdgePtInfo)
{
    Console.WriteLine("EdgePoint: {0}, Sore={1}", cCurEdgePt.Score);
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.EdgeFind.CEdgeFindTool`、`CEdgeFindResult`、`CEdgeFindSingleEdgeInfo`
- 属性：`InputImage`、`ROI`、`Result.SingleEdgeInfo`（每项 `Score`）

**注意事项 / 坑**
- 不熟悉直线查找工具的使用会导致 ROI 或结果取错。

---

### 3.3.13 缺陷检测：直线边缘缺陷检测工具的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用直线边缘缺陷检测（`CLineEdgeFlawInspTool`）工具？

**原理 / 关键概念**
实例化缺陷检测工具 → 设 `InputImage` → 设 `ROI` → `Run()` → 取 `Result.FlawInfoList`（缺陷列表）。

**实现步骤**
1. 实例化 `CLineEdgeFlawInspTool`。
2. `InitImage` 载入，`InputImage` 赋值，`ROI` 设中心矩形。
3. `Run()`，取 `Result.FlawInfoList.Count` 得缺陷数。

**关键代码**
```csharp
VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspTool cLineEdgeFlawInspToolObj = new VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspTool();//工具实例化
VisionDesigner.CMvdImage InputImg = new CMvdImage();
InputImg.InitImage("InputTest.bmp");//设置输入图片
cLineEdgeFlawInspToolObj.InputImage = InputImg;
cLineEdgeFlawInspToolObj.ROI = new VisionDesigner.CMvdRectangleF(InputImg.Width / 2, InputImg.Height / 2, InputImg.Width / 4, InputImg.Height / 4);//选择ROI 区域；
cLineEdgeFlawInspToolObj.Run();//工具执行
VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspResult cLineEdgeFlawInspRes = cLineEdgeFlawInspToolObj.Result;//获取结果
String message = "缺陷数:" + cLineEdgeFlawInspRes.FlawInfoList.Count.ToString();
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspTool`、`CLineEdgeFlawInspResult`
- 属性：`InputImage`、`ROI`、`Result.FlawInfoList`

**注意事项 / 坑**
- 不熟悉相关接口的使用会导致 ROI 未设或结果误读。

---

### 3.3.14 N 点标定：N 点标定的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用 N 点标定（`CNPointCalibTool`）工具？需记录图像点(a,b)与物理点(c,d)，最少 4 组。

**原理 / 关键概念**
N 点标定通过若干「图像坐标 ↔ 世界坐标」点对估计单应矩阵（`HomoEstStatus` 表示估计状态）。点≥4 且触发 `CalibRun` 时 `Run()`，成功后 `ExportCalibFile` 导出 `.iccal` 标定文件。

**实现步骤**
1. 实例化 `CNPointCalibTool`，设 `BasicParam.CameraMode`（`MVD_CAMERA_MODE_MOVE`）。
2. 构造 `MVD_CALIB_POINT_F`（图像点 + 物理点），加入 `OffsetPointList`。
3. 当 `OffsetPointList.Count >= 4 && CalibRun == true`：`Run()`，若 `HomoEstStatus != 0` 则 `ExportCalibFile("...calib.iccal")`。

**关键代码**
```csharp
VisionDesigner.NPointCalib.CNPointCalibTool cNPointCalibToolObj = new VisionDesigner.NPointCalib.CNPointCalibTool();//工具实例化
cNPointCalibToolObj.BasicParam.CameraMode = VisionDesigner.NPointCalib.MVD_CAMERA_MODE.MVD_CAMERA_MODE_MOVE;//基本参数设置
MVD_CALIB_POINT_F stCalibPoint = new MVD_CALIB_POINT_F();
stCalibPoint.stImageCoordinate.fX = a;
stCalibPoint.stImageCoordinate.fY = b;//图像点
stCalibPoint.stWorldCoordinate.fX = c;
stCalibPoint.stWorldCoordinate.fY = d;//物理点
cNPointCalibToolObj.BasicParam.OffsetPointList.Add(stCalibPoint);
//至少需要4 组点
if (cNPointCalibToolObj.BasicParam.OffsetPointList.Count >= 4 && CalibRun == true)
{
    cNPointCalibToolObj.Run();//执行
    VisionDesigner.NPointCalib.CNPointCalibResult cNPointCalibRes = cNPointCalibToolObj.Result;//获取标定结果
    CalibRun = false;
    if(cNPointCalibRes.OffsetPointCalibInfo.HomoEstStatus != 0)
    {
        cNPointCalibToolObj.ExportCalibFile("E://新建文件夹//calib.iccal");
    }
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.NPointCalib.CNPointCalibTool`、`CNPointCalibResult`
- 结构：`MVD_CALIB_POINT_F`（`stImageCoordinate.fX/fY`、`stWorldCoordinate.fX/fY`）
- 枚举：`MVD_CAMERA_MODE.MVD_CAMERA_MODE_MOVE`
- 方法/属性：`BasicParam.OffsetPointList`、`Result.OffsetPointCalibInfo.HomoEstStatus`、`ExportCalibFile(string)`

**注意事项 / 坑**
- 最少需要 4 组点；`HomoEstStatus == 0` 表示估计失败，不应导出标定文件。

---

### 3.3.15 畸变校正：畸变校正的使用方法

**适用场景 / 问题现象**
算子SDK 开发如何使用畸变校正（`CImageCorrectCalibTool`）工具？

**原理 / 关键概念**
畸变校正需先有 N 点标定生成的 `.iccal` 标定文件，工具导入该文件后对图像做去畸变。

**实现步骤**
1. 实例化 `CImageCorrectCalibTool`，`InitImage` 载入。
2. `ImportCalibFile("calib.iccal")` 导入标定文件。
3. `Run()`，取 `CImageCorrectCalibResult`。

**关键代码**
```csharp
VisionDesigner.ImageCorrectCalib.CImageCorrectCalibTool cImageCorrectCalibToolObj = new VisionDesigner.ImageCorrectCalib.CImageCorrectCalibTool();
VisionDesigner.CMvdImage cInputImg = new CMvdImage();
cInputImg.InitImage("InputTest.bmp");
cImageCorrectCalibToolObj.InputImage = cInputImg;
cImageCorrectCalibToolObj.ImportCalibFile("calib.iccal");//选择标定文件
cImageCorrectCalibToolObj.Run();
VisionDesigner.ImageCorrectCalib.CImageCorrectCalibResult cImageCorrectCalibRes = cImageCorrectCalibToolObj.Result;
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`VisionDesigner.ImageCorrectCalib.CImageCorrectCalibTool`、`CImageCorrectCalibResult`
- 方法：`ImportCalibFile(string)`、`InitImage`、`Run`

**注意事项 / 坑**
- 不熟悉相关接口的使用会导致标定文件未导入或校正失败。

---

### 3.3.16 字符识别：多线程同时读取同一个本地模型的方法

**适用场景 / 问题现象**
多线程如何同时调用本地同一个字符识别模型，而不互相干扰？

**原理 / 关键概念**
每个线程读取本地模型文件字节流，做**深拷贝**后通过 `LoadModelData` 接口加载到各自的 `CNNOCRTool` 实例，互不影响。

**实现步骤**
1. 每个线程 `FileStream` 读模型文件到 `byte[]`。
2. 深拷贝一份 `ModelArray`。
3. 创建 `CNNOCRTool`（`MVD_ALGORITHM_PLATFORM_CPU`），`BasicParam.LoadModelData(ModelArray, len)`。
4. 设图片参数后 `Run()`。

**关键代码**
```csharp
for (int i = 0; i < 3; i++)
{
    int temp = i;
    Task.Factory.StartNew(new Action<object>(t =>
    {
        FileStream fs = new FileStream(modelpath, FileMode.Open);
        long size = fs.Length;
        byte[] array = new byte[size];
        fs.Read(array, 0, array.Length);
        CNNOCRTool tool = new CNNOCRTool(MVD_ALGORITHM_PLATFORM_TYPE.MVD_ALGORITHM_PLATFORM_CPU);
        byte[] ModelArray = new byte[array.Length];
        Array.Copy(array, ModelArray, array.Length);
        tool.BasicParam.LoadModelData(ModelArray, ModelArray.Length);
        //设置图片等参数
        tool.Run();
    }), temp);
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CNNOCRTool`
- 平台枚举：`MVD_ALGORITHM_PLATFORM_TYPE.MVD_ALGORITHM_PLATFORM_CPU`
- 方法：`BasicParam.LoadModelData(byte[], int)`

**注意事项 / 坑**
- 不熟悉多线程同时读取同一个本地模型会导致模型数据共享冲突；必须深拷贝后各自 `LoadModelData`。

---

### 3.3.17 字符识别：VM 自带字符识别模型的区分

**适用场景 / 问题现象**
VM 安装路径下字符识别模块有两个模型：`lpr_ocr.bin` 和 `mvb_ocr.bin`，分别对应哪个算子？

**原理 / 关键概念**
VM 自带两个已训练模型：`lpr_ocr.bin` 与 `mvb_ocr.bin`，分别对应训练平台-字符识别的模型类型「文本行识别」与「文本行识别（拓展）」。

**实现步骤**
（无需代码，为模型/算子对应关系说明）
- 在 VM 中使用字符识别模块，两个模型都可调用；
- 在算子SDK 开发中：
  - `CNNOCRTool` 算子调用模型 **`lpr_ocr.bin`**；
  - `CNNCharRecogTool` 算子调用模型 **`mvb_ocr.bin`**。

**关键代码**
（本条目为说明，无代码。）

**关键 API / 接口名 / 枚举 / 参数**
- 算子：`CNNOCRTool`（对应 `lpr_ocr.bin`）、`CNNCharRecogTool`（对应 `mvb_ocr.bin`）
- 模型文件：`lpr_ocr.bin`、`mvb_ocr.bin`

**注意事项 / 坑**
- 不熟悉字符识别模型对应关系会调错算子与模型。

---

### 3.3.18 设置掩膜：给模块设置掩膜的方法

**适用场景 / 问题现象**
如何给模块设置掩膜（针对多感兴趣区域及屏蔽区域场景，可通过掩膜设置）？

**原理 / 关键概念**
通过掩膜算子 `CPreproMaskTool` 生成掩模图像：构造 `List<Tuple<CMvdShape, bool>>`（`bool` 为 `true` 表示屏蔽区，`false` 表示感兴趣区域），运行后输出 `OutputImage` 作为掩模；下游工具（如 Blob）用 `RegionImage` 接收该掩模图像。

**实现步骤**
1. 实例化 `CPreproMaskTool`，构造矩形/多边形区域列表（`Tuple<CMvdShape,bool>`）。
2. 设 `InputImage`、`RegionList`，`Run()`。
3. 实例化 `CBlobFindTool`，`RegionImage = cPrepromaskTool.OutputImage`，设阈值/极性后 `Run()`。

**关键代码**
```csharp
public void SetBlobMask()
{
    //实例掩膜工具
    CPreproMaskTool cPrepromaskTool = new CPreproMaskTool();
    //创建Shape链表
    List<Tuple<CMvdShape, bool>> maskList = new List<Tuple<CMvdShape, bool>>();
    var rect1 = new CMvdRectangleF(rect.CenterX, rect.CenterY, rect.Width - 200, rect.Height - 200);
    //添加矩形感兴趣区域
    maskList.Add(new Tuple<CMvdShape, bool>(rect1, false));
    var poly1 = new CMvdPolygonF();
    poly1.AddVertex(rect.CenterX - rect.Height / 2, rect.CenterY - rect.Width / 2);
    poly1.AddVertex(rect.CenterX - rect.Height / 2, rect.CenterY - rect.Width / 2 + 200);
    poly1.AddVertex(rect.CenterX - rect.Height / 2 + 200, rect.CenterY - rect.Width / 2);
    //添加多边形感兴趣区域
    maskList.Add(new Tuple<CMvdShape, bool>(poly1, false));
    var poly2 = new CMvdPolygonF();
    poly2.AddVertex(rect.CenterX - rect.Height / 2, rect.CenterY + rect.Width / 2);
    poly2.AddVertex(rect.CenterX - rect.Height / 2, rect.CenterY + rect.Width / 2 - 200);
    poly2.AddVertex(rect.CenterX - rect.Height / 2 + 200, rect.CenterY + rect.Width / 2);
    //添加多边形屏蔽区域
    maskList.Add(new Tuple<CMvdShape, bool>(poly2, true));
    //设置掩膜工具参数
    cPrepromaskTool.InputImage = runImage;
    cPrepromaskTool.RegionList = maskList;
    //运行掩膜工具
    cPrepromaskTool.Run();
    //实例化Blob分析工具
    CBlobFindTool blobTool = new VisionDesigner.BlobFind.CBlobFindTool();
    blobTool.InputImage = runImage;
    //设置掩膜图像
    blobTool.RegionImage = cPrepromaskTool.OutputImage;
    blobTool.SetRunParam("LowThreshold", "60");
    blobTool.SetRunParam("Polarity", "BrightObject");
    blobTool.BasicParam.ShowBlobImageStatus = true;
    //执行Blob算子
    blobTool.Run();
}
```

**关键 API / 接口名 / 枚举 / 参数**
- 掩膜类：`CPreproMaskTool`，属性 `RegionList`（`List<Tuple<CMvdShape,bool>>`，`true`=屏蔽区）、`OutputImage`
- 形状类：`CMvdRectangleF`、`CMvdPolygonF`（`AddVertex`）
- Blob 类：`VisionDesigner.BlobFind.CBlobFindTool`，属性 `RegionImage`（接收掩模图像）、`SetRunParam("LowThreshold"/"Polarity")`

**注意事项 / 坑**
- 不熟悉掩膜工具的使用会导致掩膜区域语义错误（`Tuple` 第二参数 `true` 才是屏蔽区）。

---

## 3.4 控件嵌入类

### 3.4.1 图片存储：图片保存的方法

**适用场景 / 问题现象**
算子SDK 开发如何存储图片（原图与渲染图）？

**原理 / 关键概念**
- 原图：`CMvdImage.SaveImage(path)`。
- 渲染图：`mvdRenderActivex1.SaveImage(path, format, quality, saveType)`，其中 `quality` 取 0–100。

**实现步骤**
1. 确定保存路径文件夹已创建。
2. 原图 `runImage.SaveImage(...)`。
3. 渲染图 `mvdRenderActivex1.SaveImage(path, MVD_FILE_FORMAT, 100, MVD_SAVE_RESULT_IMAGE)`。

**关键代码**
```csharp
string imageName = "a";
MVD_FILE_FORMAT ms = MVD_FILE_FORMAT.MVD_FILE_BMP;//图片格式
//保存原图
runImage.SaveImage("E:\\" + imageName + "_origin.bmp");
//保存渲染图，参数分别为图片路径，图片格式，图片质量（0-100）
mvdRenderActivex1.SaveImage("E:\\" + imageName + "_render.bmp", ms, 100, MVD_SAVE_TYPE.MVD_SAVE_RESULT_IMAGE);
```

**关键 API / 接口名 / 枚举 / 参数**
- 方法：`CMvdImage.SaveImage(string)`、`mvdRenderActivex1.SaveImage(string, MVD_FILE_FORMAT, int, MVD_SAVE_TYPE)`
- 枚举：`MVD_FILE_FORMAT.MVD_FILE_BMP`、`MVD_SAVE_TYPE.MVD_SAVE_RESULT_IMAGE`

**注意事项 / 坑**
- 保存前需确保路径中的文件夹已创建，否则保存失败。

---

### 3.4.2 辅助十字线：给图像添加辅助十字线的方法

**适用场景 / 问题现象**
希望在图像上显示辅助十字线（便于定位中心），如何实现？

**原理 / 关键概念**
用两条 `CMvdLineSegmentF`（竖线 + 横线）表示十字线，`AddShape` 后 `Display` 渲染；可设线型 `MVD_DASH_STYLE` 与颜色 `MVD_COLOR`。

**实现步骤**
1. 构造两条贯穿图像中心的线段 `CMvdLineSegmentF`。
2. 设 `BorderStyle`、`BorderColor`。
3. `AddShape(line1/line2)`，`Display()`。

**关键代码**
```csharp
CMvdLineSegmentF line1 = new CMvdLineSegmentF(new MVD_POINT_F(mvdimage.Width / 2, 0), new MVD_POINT_F(mvdimage.Width / 2, mvdimage.Height));//定义线段
CMvdLineSegmentF line2 = new CMvdLineSegmentF(new MVD_POINT_F(0, mvdimage.Height / 2), new MVD_POINT_F(mvdimage.Width, mvdimage.Height / 2));//定义线段
line1.BorderStyle = MVD_DASH_STYLE.MvDashStyleDashDot;//设置线型
line1.BorderColor = new MVD_COLOR(250, 0, 0);//设置线的颜色
line2.BorderStyle = MVD_DASH_STYLE.MvDashStyleDashDot;//设置线型
line2.BorderColor = new MVD_COLOR(250, 0, 0);//设置线的颜色
mvdRenderActivex1.AddShape(line1);//添加线段1
mvdRenderActivex1.AddShape(line2);//添加线段2
mvdRenderActivex1.Display();//渲染
```

**关键 API / 接口名 / 枚举 / 参数**
- 类：`CMvdLineSegmentF`、`MVD_POINT_F`、`MVD_COLOR`
- 枚举/属性：`BorderStyle = MVD_DASH_STYLE.MvDashStyleDashDot`、`BorderColor`
- 渲染：`mvdRenderActivex1.AddShape(...)`、`mvdRenderActivex1.Display()`

**注意事项 / 坑**
- 不了解算子SDK 的相关接口会无法叠加图形。

---

### 3.4.3 控件调用：在WPF 中使用Winform 控件的方法

**适用场景 / 问题现象**
在算子SDK 开发（WPF）中，如何使用封装好的 WinForm 模板匹配等控件（以及渲染控件）？

**原理 / 关键概念**
WPF 不能直接承载 WinForm 控件，需通过 `WindowsFormsHost` 宿主容器桥接；并引用 `WindowsFormsIntegration.dll` 与 `System.Windows.Forms.dll`。

**实现步骤**
1. 添加引用：`WindowsFormsIntegration.dll`、`System.Windows.Forms.dll`。
2. 在 WPF 窗体 XAML 添加命名空间引用 `wf` 与 `wfi`。
3. 在 WPF 容器（如 `StackPanel`）内放 `<wfi:WindowsFormsHost x:Name="host"/>` 作为宿主。
4. 代码中 `UserControl1 user = new UserControl1(); this.host.Child = user;`（UserControl1 为自定义 WinForm 用户控件）。
5. 渲染控件在 WPF 中调用时同样添加渲染控件 dll，通过 `WindowsFormsHost` 承载。

**关键代码**
```csharp
// 1. 添加引用：WindowsFormsIntegration.dll，System.Windows.Forms.dll

// 2. WPF 窗体 XAML 添加命名空间引用
// xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"
// xmlns:wfi="clr-namespace:System.Windows.Forms.Integration;assembly=WindowsFormsIntegration"

// 3. 在 WPF 容器控件（如 StackPanel）内添加 WinForm 控件宿主容器
// <StackPanel>
//     <wfi:WindowsFormsHost x:Name="host" Margin="0,0,0,0" />
// </StackPanel>

// 4. 代码中定义用户控件并放入宿主
UserControl1 user = new UserControl1();
this.host.Child = user; //使 XAML 文件中的 host 中的内容为用户控件 user

// 5. 如算子SDK 中渲染控件在 WPF 中的调用，添加渲染控件 dll
```

**关键 API / 接口名 / 枚举 / 参数**
- 引用 dll：`WindowsFormsIntegration.dll`、`System.Windows.Forms.dll`
- XAML 命名空间：`wf`（`System.Windows.Forms`）、`wfi`（`System.Windows.Forms.Integration`）
- 宿主控件：`WindowsFormsHost`（XAML 元素 `<wfi:WindowsFormsHost x:Name="host"/>`）
- 承载方式：`this.host.Child = userControlInstance`

**注意事项 / 坑**
- 必须添加 `WindowsFormsIntegration` 与 `System.Windows.Forms` 两个引用，并在 XAML 声明命名空间；否则 WPF 无法承载 WinForm 控件。

---

## 附录 A（输入文件前置条目，原 2.5.1 全局相机，非第3章内容）

### 2.5.1 全局相机：获取全局相机列表和设置相机参数的方法

**适用场景 / 问题现象**
- 问题1：如何获取方案中所有的全局相机的连接状态，并在流程运行时监控全局相机1/2 的连接状态？
- 问题2：如何设置全局相机的基本参数（如曝光、增益）？

**原理 / 关键概念**
VM4.2.1 起，`GlobalCameraTool` 类提供 `bIsCameraConnect()` 获取相机连接状态；相机参数通过 `GlobalCameraParam` 类属性设置。需在 VM SDK 中引用 `GlobalCameraModuleCs.dll`。

**实现步骤（问题1：监控连接状态）**
1. 通过 `VmSolution.Instance.GetAllModule` 遍历所有模块，筛出 `GlobalCameraModuleTool`。
2. 启动后台线程 `CameraConnectionWatchDog` 每 2s 检查 `bIsCameraConnect()`。

**关键代码（获取全局相机模块列表）**
```csharp
//获取流程中所有全局相机模块
List<GlobalCameraModuleTool> glCameralist = new List<GlobalCameraModuleTool>();
List<VmModule> vmModules = new List<VmModule>();
VmSolution.Instance.GetAllModule(vmModules);
foreach(VmModule module in vmModules)
{
    if(module.GetType() == typeof(GlobalCameraModuleTool))
    {
        glCameralist.Add((GlobalCameraModuleTool) module);
    }
}
//启动全局相机连接状态监控线程
Thread watchThread = new Thread(new ParameterizedThreadStart(CameraConnectionWatchDog));
watchThread.IsBackground = true;
watchThread.Start(glCameralist);
```

**关键代码（监控线程）**
```csharp
public void CameraConnectionWatchDog(object obj)
{
    List<GlobalCameraModuleTool> globalCameraToolList = (List<GlobalCameraModuleTool>)obj;
    bool[] isCameraConected = new bool[globalCameraToolList.Count];
    while (true)
    {
        try
        {
            //获取流程中所有已配置的连接状态
            foreach (var cameraTool in globalCameraToolList)
            {
                if (cameraTool.bIsCameraConnect() == false)
                {
                    Debug.WriteLine(string.Format($"警告: {cameraTool.Name} 已经离线！"));
                }
            }
        }
        catch (VmException ex)
        {
            Debug.WriteLine("发生致命错误，错误码:" + ex.errorCode);
        }
        Thread.Sleep(2000);
    }
}
```

**关键代码（问题2：设置曝光与增益）**
```csharp
GlobalCameraModuleTool cameraModuleTool = VmSolution.Instance["全局相机1"] as GlobalCameraModuleTool;
GlobalCameraParam globalCameraParam = cameraModuleTool.ModuParams;
globalCameraParam.ExposureTime = 5000;
globalCameraParam.Gain = 5.0;
```

**关键 API / 接口名 / 枚举 / 参数**
- 类/接口：`VmSolution.Instance`、`VmModule`、`GlobalCameraModuleTool`、`GlobalCameraParam`
- 方法/属性：`GetAllModule(List<VmModule>)`、`bIsCameraConnect()`、`ModuParams`、`GlobalCameraParam.ExposureTime`、`GlobalCameraParam.Gain`
- 引用 dll：`GlobalCameraModuleCs.dll`（需手动添加引用，且「复制到本地」设为 False），并 `using GlobalCameraModuleCs;`

**注意事项 / 坑**
- 不了解 VM SDK 中全局相机模块的使用、不知道如何访问其方法和属性会导致无法取状态/设参数。
- 手动添加 `GlobalCameraModuleCs.dll` 引用时，「复制到本地」必须设为 False。

---

## 条目索引

**3.1 环境配置类（4）**
- 3.1.1 环境配置：CSharp 算子SDK 开发环境配置方法
- 3.1.2 算子封装：使用C++封装算子SDK的方法
- 3.1.3 异常中断：算子SDK 软件运行报错"托管调试助手"中断的解决方法
- 3.1.4 深度学习：GPU 运行深度学习算子引发StackOverFlow 异常的方法

**3.2 公用工具类（6）**
- 3.2.1 图像载入：本地图像的载入方法
- 3.2.2 相机取流：相机SDK 取流的方法
- 3.2.3 输入图像：给算子模块输入图像数据的方法
- 3.2.4 实时取流：实时取流的实现方法
- 3.2.5 卡尺ROI：卡尺型ROI 的生成方法
- 3.2.6 DL 算子耗时：深度学习算子长时间停止再运行耗时变长问题的解决方法

**3.3 模块工具类（18）**
- 3.3.1 位置修正：位置修正算子工具的使用方法
- 3.3.2 模板保存：实现模板自动加载的方法
- 3.3.3 模板匹配：获取模板匹配框和轮廓点的方法
- 3.3.4 模板训练：模板训练执行完成的判断方法
- 3.3.5 图像相减：算子SDK 开发图像相减的方法
- 3.3.6 图像修正：图像修正工具的使用方法
- 3.3.7 Blob 工具：Blob 工具的使用方法
- 3.3.8 点点测量：点点测量工具的使用方法
- 3.3.9 亮度测量：亮度测量工具的使用方法
- 3.3.10 圆查找：圆查找的方法
- 3.3.11 仿射变换：图像仿射变换的使用方法
- 3.3.12 直线查找：直线查找工具的使用方法
- 3.3.13 缺陷检测：直线边缘缺陷检测工具的使用方法
- 3.3.14 N 点标定：N 点标定的使用方法
- 3.3.15 畸变校正：畸变校正的使用方法
- 3.3.16 字符识别：多线程同时读取同一个本地模型的方法
- 3.3.17 字符识别：VM 自带字符识别模型的区分
- 3.3.18 设置掩膜：给模块设置掩膜的方法

**3.4 控件嵌入类（3）**
- 3.4.1 图片存储：图片保存的方法
- 3.4.2 辅助十字线：给图像添加辅助十字线的方法
- 3.4.3 控件调用：在WPF 中使用Winform 控件的方法

**附录 A（输入文件前置，非第3章）**
- 2.5.1 全局相机：获取全局相机列表和设置相机参数的方法

> 合计：第3章 31 条 + 附录 1 条 = 32 个条目。
