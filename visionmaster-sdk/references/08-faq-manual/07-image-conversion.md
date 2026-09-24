<!-- source: 09-image-conversion.md  PDF 1122-1297 -->
# VM 图像转换专题（C# / C++）

> 素材来源：VM 官方 FAQ 专题·图像转换（PDF 1122–1297 页），环境 VM4.2 + VS2013 及以上。
> 本文档将各图像载体之间的转换函数逐字保留，仅对 PDF 抽取产生的断行/页眉页脚做重组，不增删任何类名、方法名、属性名、命名空间、DLL 名、枚举名。
> 涉及内存释放、通道顺序（BGR↔RGB）、位深、指针/句柄、性能等"坑"均在每节末尾标注。

## 速览

1. VM 二次开发涉及三类：VM SDK 开发、算子 SDK 开发、自定义算法模块开发（C++）。
2. C# 侧流程/Group 输入类型在 VM4.2 为 `ImageBaseData_V2`，VM4.3 起流程/Group/模块输出统一为 `ImageBaseData`。
3. C# 侧相机取流用 `MyCamera.MV_FRAME_OUT`（来自 `MvCameraControl.Net.dll`）；算子 SDK 的 `MVDCamera.Net.dll` 取流类型为 `CMvdImage`。
4. 三通道 Bitmap、Mat 按 **BGR** 存储；三通道 VM / 二次开发（ImageBaseData、ImageData、CMvdImage/IMvdImage）按 **RGB** 存储。互转时务必交换 R/B。
5. `ImageBaseData_V2` 用 `IntPtr` 构造时为**浅拷贝**，使用结束后需 `Marshal.FreeHGlobal` 手动释放。
6. `InputImageData.Data` 需 `Marshal.AllocHGlobal` 申请，使用完 `Marshal.FreeHGlobal` 释放。
7. Halcon 灰度图用 `GetImagePointer1` / `GenImage1`，彩色图用 `GetImagePointer3` / `GenImage3`（RGB 三通道分别取指针）。
8. C++ 侧流程图像类型为 `IoImage`，图像源/模块输入为 `ImageBaseData`；算子图像为 `IMvdImage`（需用 `CreateImageInstance` 创建）。
9. C++ 算子图像像素格式枚举用的是 `MVD_PIXEL_BGR_BGR24_C3`（BGR），而 VM 图像用 `MVD_PIXEL_RGB_RGB24_C3`（RGB），与 C# 习惯不同，注意核对 SDK 版本。
10. C++ 算法模块图像类型为 `HKA_IMAGE`，含 `format`/`width`/`height`/`step[0]`/`data[0]`，`data[0]` 需 `malloc` 申请。
11. Bitmap 要求 4 字节对齐（行步长），VM/MVD 图像不要求，转换灰度/彩色图需按 `Stride` 去掉冗余位。
12. 相机采图转算子图像（C++）时，RGB8_Packed 对应 `MVD_PIXEL_BGR_BGR24_C3`，转 VM 图像则对应 `MVD_PIXEL_RGB_RGB24_C3`。
13. Mat 转 VM 图像用 `Mat.Ptr(0)` 直接取首地址（OpenCvSharp）；彩色需 `Cv2.CvtColor(..., ColorConversionCodes.BGR2RGB)`。
14. `CMvdImage` 通过 `InitImage(w, h, MVD_PIXEL_FORMAT, MVD_IMAGE_DATA_INFO)` 初始化；`MVD_IMAGE_DATA_INFO.stDataChannel[0].arrDataBytes` 承载字节。
15. QImage 转 VM：直接 `(void*)qImage.constBits()` 取数据指针，灰度 `Format_Indexed8`/`Format_Grayscale8`，彩色 `Format_RGB888`（已是 RGB）。
16. Halcon 彩色转 MVD/VM 需把 R/G/B 三块拼成交错 RGB 或 BGR 一块，注意顺序。
17. 流程图像 ↔ 算子图像互转是 VM SDK 与算子 SDK 联用的核心（3.6 / 3.12）。
18. 脚本图像类型为 `ImageData`（属性 `Buffer`/`Width`/`Heigth`/`PixelFormat`），`PixelFormat` 用 `ImagePixelFormate.MONO8` / `RGB24`。
19. 模块输入 `InputImageData` 的 `Names` 固定为 `InImage` / `InImageWidth` / `InImageHeight` / `InImagePixelFormat`，不可改名。
20. 性能敏感场景尽量用指针/首地址浅传递，避免每帧 `new byte[]` 深拷贝；但要严守各自的释放责任。

---

## 图像类型对照与转换矩阵

### C# 关键类型

| 载体 | 类型 / 命名空间 | 备注 |
|---|---|---|
| 相机采图 | `MyCamera.MV_FRAME_OUT`（`MvCameraControl.Net.dll`） | `stFrameInfo.enPixelType` / `pBufAddr` / `nFrameLen` |
| 脚本图像 | `ImageData` | `Buffer` / `Width` / `Heigth` / `PixelFormat`（`ImagePixelFormate`） |
| 流程/Group 输入 | `ImageBaseData_V2`（`VM.PlatformSDKCS`） | VM4.2 新增；`IntPtr ImageData` 浅拷贝 |
| 图像源 SDK 输入 | `ImageBaseData` | `byte[] ImageData` / `Pixelformat`(`VMPixelFormat`) |
| 模块输入 | `InputImageData` | `Data` 为 `IntPtr`，需 `AllocHGlobal`；`Names` 固定 |
| 流程输出 | `ImageBaseData_V2`（VM4.2）/ `ImageBaseData`（VM4.3） | 见 3.3.5 |
| 算子图像 | `CMvdImage`（`VisionDesigner`） | `InitImage` + `MVD_IMAGE_DATA_INFO` |
| Bitmap | `System.Drawing.Bitmap` | `PixelFormat.Format8bppIndexed` / `Format24bppRgb` |
| Mat | `OpenCvSharp.Mat` | `Cv2`、`MatType`、`ColorConversionCodes` |
| Halcon | `HObject` / `HOperatorSet`（`HalconDotNet`） | `GetImagePointer1/3`、`GenImage1/3` |

### C++ 关键类型

| 载体 | 类型 / 命名空间 | 备注 |
|---|---|---|
| 相机采图 | `MV_FRAME_OUT`（`MvCameraControl`） | `stFrameInfo.enPixelType` / `pBufAddr` |
| 流程/Group 输入 | `IoImage`（`VisionMasterSDK`） | 内含 `stImage`（Width/Height/DataLen/Pixelformat/ImageData） |
| 图像源/模块输入 | `ImageBaseData`（`VisionMasterSDK`） | `ImageData` 为 `void*` |
| 算子图像 | `IMvdImage`（`VisionDesigner`） | `CreateImageInstance` 创建；`GetImageData(0)->pData` |
| QImage | `QImage`（`Qt`） | `constBits()` / `Format_Indexed8` / `Format_RGB888` / `Format_Grayscale8` |
| Mat | `cv::Mat`（`OpenCV`） | `CV_8UC1` / `CV_8UC3` / `cvtColor` |
| Halcon | `HImage` / `Hobject`（`HalconCpp`） | `get_image_pointer1/3` / `gen_image1/3` |
| 算法模块图像 | `HKA_IMAGE` | `format` / `width` / `height` / `step[0]` / `data[0]`（`HKA_IMG_MONO_08` / `HKA_IMG_RGB_RGB24_C3`） |

### C# 转换矩阵（源类型 → 目标类型 → 小节）

| 源 \ 目标 | 流程输入 `ImageBaseData_V2` | Group 输入 | 图像源 SDK `ImageBaseData` | 模块输入 `InputImageData` | 算子输入 `CMvdImage` | 脚本图像 `ImageData` | 反转为 Bitmap / Mat / Halcon |
|---|---|---|---|---|---|---|---|
| 相机采图 `MV_FRAME_OUT` | 3.2.1 | 3.2.1 | 3.2.2 | 3.2.3 | 3.2.4 | — | — |
| Bitmap | 3.3.1 | 3.3.1 | 3.3.2 | 3.3.3 | 3.3.4 | — | 3.3.5(→Bitmap) |
| Mat | 3.4.1 | 3.4.1 | 3.4.2 | 3.4.3 | 3.4.4 | 3.4.6 | 3.4.5(→Mat) |
| Halcon `HObject` | 3.5.1 | 3.5.1 | 3.5.2 | 3.5.3 | 3.5.4 | 3.5.6 | 3.5.5(→Halcon) |
| 流程图像 `ImageBaseData_V2` | — | — | — | — | 3.6.1(→算子) | — | 3.6.2(算子→流程) |
| 算子图像 `CMvdImage` | 3.6.2 | — | — | — | — | 3.3.4 / 3.4.4 / 3.5.4 | — |

### C++ 转换矩阵（源类型 → 目标类型 → 小节）

| 源 \ 目标 | 流程输入 `IoImage` | Group 输入 | 图像源/模块 `ImageBaseData` | 算子输入 `IMvdImage` | 流程输出反转为 QImage/Mat/Halcon | HKA_IMAGE |
|---|---|---|---|---|---|---|
| 相机采图 `MV_FRAME_OUT` | 3.8.1 | 3.8.1 | 3.8.2 | 3.8.3 | — | — |
| QImage | 3.9.1 | 3.9.1 | 3.9.2 | 3.9.3 | 3.9.4(→QImage) | — |
| Mat | 3.10.1 | 3.10.1 | 3.10.2 | 3.10.3 | 3.10.4(→Mat) | — |
| Halcon `HImage` | 3.11.1 | 3.11.1 | 3.11.2 | 3.11.3 | 3.11.4(→Halcon) | — |
| 流程图像 `IoImage` | — | — | — | 3.12.1(→算子) | 3.12.2(算子→流程) | — |
| 算法模块 `HKA_IMAGE` | — | — | — | 3.13.3 | — | 3.13.1 / 3.13.2 |
| 算子图像 `IMvdImage` | 3.12.2 | — | — | — | 3.12.1(流程→算子) | 3.13.3 |

---

# C# 篇

## 命名空间与引用（原文出现的命名空间，非编造）

- `using VM.PlatformSDKCS;` —— `ImageBaseData_V2` / `ImageBaseData` / `InputImageData` / `VmSolution` / `ImageSourceModuleTool` / `IMVSGroupTool` / `IMVSImageEnhanceModuCs.IMVSImageEnhanceModuTool` / `VMPixelFormat`
- `using VisionDesigner;` —— `CMvdImage` / `MVD_IMAGE_DATA_INFO` / `MVD_PIXEL_FORMAT` / `MvdException` / `MVD_MODULE_TYPE` / `MVD_ERROR_CODE`
- `using MvCameraControl;` —— `MyCamera.MV_FRAME_OUT` / `MyCamera.MvGvspPixelType`
- `using HalconDotNet;` —— `HObject` / `HOperatorSet` / `HTuple`
- `using OpenCvSharp;` —— `Mat` / `MatType` / `Cv2` / `ColorConversionCodes`（Mat 相关示例所用 OpenCV 封装）
- `using System.Drawing;` / `using System.Drawing.Imaging;` / `using System.Runtime.InteropServices;`

---

### 3.1 图像转换扫盲篇（CSharp）

**适用场景**：了解 VM 各开发形态下"图像"究竟是什么类型，建立转换全景。

**关键类型 / 类名**：`MyCamera.MV_FRAME_OUT`、`CMvdImage`、`ImageData`、`ImageBaseData_V2`、`ImageBaseData`、`InputImageData`、`CMvdImage`、`HKA_IMAGE`。

**图像格式一览**（原文转录）：

- 相机：图像数据流类型 `MyCamera.MV_FRAME_OUT`（来自海康机器人工业相机 SDK `MvCameraControl.Net.dll`）；算子 SDK 的 `MVDCamera.Net.dll` 取流时图像数据流类型是 `CMvdImage`；`MvCameraControl.Net.dll` 取流时类型是 `MyCamera.MV_FRAME_OUT`。
- VM：脚本输入图像，类型是 `ImageData`。
- VM SDK：
  - 流程输入图像 `ImageBaseData_V2`（VM4.2 SDK 新增）
  - Group 输入图像 `ImageBaseData_V2`（VM4.2 SDK 新增）
  - 图像源 SDK 输入图像 `ImageBaseData`
  - 模块输入图像 `InputImageData`
  - 流程输出图像（VM4.0 与 VM4.2 获取方式不同；VM4.2 获取类型为 `ImageBaseData_V2`）
  - 提示：VM4.3 SDK 中，流程、Group、模块输出图像类型统一为 `ImageBaseData`
- 算子 SDK：输入图像 `CMvdImage`
- 算法模块：输入图像 `HKA_IMAGE`（C++ 中图像类型）

**转换说明**：

- 三通道的 Bitmap、Mat 为 **BGR**；三通道的 VM 和二次开发为 **RGB**。
- 单通道 / 三通道图像的常用转换场景见 3.2 ~ 3.6。
- 每种转换用函数表达：函数输入某种图像类型，返回另一种图像类型。

**注意事项 / 坑**：

- 所有函数仅处理 8bit 单通道（Mono8）与 8bit 三通道（RGB/BGR Packed）；其他位深（如 16bit）需自行扩展。
- 通道顺序错位是第一大病：Bitmap/Mat 是 BGR，VM/算子图像是 RGB，互转必须交换 R 与 B。
- 跨 4 字节对齐（Bitmap `Stride`）与无对齐（VM/MVD）的差异，决定灰度/彩色拷贝要逐行去冗余位。

---

### 3.2 相机采图转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入图像

**适用场景**：`MyCamera.MV_FRAME_OUT` → 流程输入 / Group 输入 / 图像源 SDK 输入 / 模块输入 / 算子输入。

**关键类型 / 类名**：`MyCamera.MV_FRAME_OUT`、`MyCamera.MvGvspPixelType`（`PixelType_Gvsp_Mono8` / `PixelType_Gvsp_RGB8_Packed`）、`ImageBaseData_V2`、`ImageBaseData`、`InputImageData`、`CMvdImage`、`MVD_IMAGE_DATA_INFO`、`MVD_PIXEL_FORMAT`、`VmSolution`、`ImageSourceModuleTool`、`IMVSGroupTool`、`IMVSImageEnhanceModuTool`。

#### 3.2.1 相机采图转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V2）

```csharp
public ImageBaseData_V2 CCDToImageBaseDataV2(MyCamera.MV_FRAME_OUT frameOut)
{
    ImageBaseData_V2 imageBaseDataV2 = new ImageBaseData_V2();
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_Mono8)
    {
        imageBaseDataV2 = new ImageBaseData_V2(frameOut.pBufAddr, frameOut.stFrameInfo.nFrameLen, frameOut.stFrameInfo.nWidth, frameOut.stFrameInfo.nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
    }
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_RGB8_Packed)
    {
        imageBaseDataV2 = new ImageBaseData_V2(frameOut.pBufAddr, frameOut.stFrameInfo.nFrameLen, frameOut.stFrameInfo.nWidth, frameOut.stFrameInfo.nHeight, VMPixelFormat.VM_PIXEL_RGB24_C3);
    }

    return imageBaseDataV2;
}
```

```csharp
var image = CCDToImageBaseDataV2(stFrameOut);
//设置到流程
var procedure = VmSolution.Instance["流程1"] as VmProcedure;
procedure.ModuParams.SetInputImage_V2("ImageData", image);
//设置到Group
var group = VmSolution.Instance["流程1.组合模块1"] as IMVSGroupTool;
group.ModuParams.SetInputImage_V2("ImageData", image);
```

**注意事项 / 坑**：`ImageBaseData_V2(IntPtr, ...)` 为浅拷贝，引用相机缓冲区；`image` 使用结束后需 `Marshal.FreeHGlobal` 释放（此处 `pBufAddr` 由相机 SDK 管理，转换出的 `ImageBaseData_V2` 若独立持有需自管内存）。

#### 3.2.2 相机采图转图像源 SDK 输入（ImageBaseData）

```csharp
public ImageBaseData CCDToImageBaseData(MyCamera.MV_FRAME_OUT frameOut)
{
    ImageBaseData imageBaseData = new ImageBaseData();
    imageBaseData.Width = frameOut.stFrameInfo.nWidth;
    imageBaseData.Height = frameOut.stFrameInfo.nHeight;
    imageBaseData.DataLen = frameOut.stFrameInfo.nFrameLen;
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_Mono8)
    {
        imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_MONO_08;
    }
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_RGB8_Packed)
    {
        imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_RGB24_C3;
    }
    imageBaseData.ImageData = new byte[frameOut.stFrameInfo.nFrameLen];
    Marshal.Copy(frameOut.pBufAddr, imageBaseData.ImageData, 0, (int)frameOut.stFrameInfo.nFrameLen);
    return imageBaseData;
}
```

```csharp
var image = CCDToImageBaseData(stFrameOut);
//设置到图像源
ImageSourceModuleTool imageSourceModuleTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
imageSourceModuleTool.SetImageData(image);
```

**注意事项 / 坑**：`ImageBaseData.ImageData` 为 `byte[]`，已深拷贝相机缓冲，随对象 GC 释放；像素格式枚举需强转 `(int)`。

#### 3.2.3 相机采图转模块输入（InputImageData）

```csharp
public InputImageData CCDToInputImageData(MyCamera.MV_FRAME_OUT frameOut)
{
    InputImageData inputImageData = new InputImageData();
    inputImageData.Names.DataName = "InImage";//只能使用默认名称InImage
    inputImageData.Names.HeightName = "InImageHeight";//默认InImageHeight
    inputImageData.Names.WidthName = "InImageWidth";//默认InImageWidth
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";//默认InImagePixelFormat
    inputImageData.Width = frameOut.stFrameInfo.nWidth;
    inputImageData.Height = frameOut.stFrameInfo.nHeight;
    inputImageData.DataLen = frameOut.stFrameInfo.nFrameLen;

    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_Mono8)
    {
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;

    }
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_RGB8_Packed)
    {
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_RGB24;
    }
    //申请内存，记得inputImageData 使用完成后，手动释放内存，Marshal.FreeHGlobal
    inputImageData.Data = Marshal.AllocHGlobal((int)frameOut.stFrameInfo.nFrameLen);
    byte[] imagedataBuffer = new byte[(int)frameOut.stFrameInfo.nFrameLen];
    Marshal.Copy(frameOut.pBufAddr, imagedataBuffer, 0, (int)frameOut.stFrameInfo.nFrameLen);
    Marshal.Copy(imagedataBuffer, 0, inputImageData.Data, (int)frameOut.stFrameInfo.nFrameLen);
    return inputImageData;
}
```

```csharp
var image = CCDToInputImageData(stFrameOut);
//设置到模块
var circlefindTool = VmSolution.Instance["流程1.圆查找1"] as IMVSImageEnhanceModuCs.IMVSImageEnhanceModuTool;
circlefindTool.ModuParams.SetInputImage(image);
```

**注意事项 / 坑**：`InputImageData.Data` 是 `IntPtr`，`AllocHGlobal` 后必须手动 `Marshal.FreeHGlobal`；`Names` 四个字段只能使用默认名称（InImage / InImageWidth / InImageHeight / InImagePixelFormat）。

#### 3.2.4 相机采图转算子输入（CmvdImage）

```csharp
public CMvdImage CCDToCMvdImage(MyCamera.MV_FRAME_OUT frameOut)
{
    VisionDesigner.CMvdImage cMvdImage = new VisionDesigner.CMvdImage();
    VisionDesigner.MVD_IMAGE_DATA_INFO stImageData = new VisionDesigner.MVD_IMAGE_DATA_INFO();
    stImageData.stDataChannel[0].nLen = (uint)(frameOut.stFrameInfo.nFrameLen);
    stImageData.stDataChannel[0].nSize = (uint)(frameOut.stFrameInfo.nFrameLen);
    byte[] m_BufForDriver1 = new byte[frameOut.stFrameInfo.nFrameLen];
    //数据Copy
    Marshal.Copy(frameOut.pBufAddr, m_BufForDriver1, 0, (int)frameOut.stFrameInfo.nFrameLen);
    stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver1;
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_Mono8)
    {
        stImageData.stDataChannel[0].nRowStep = (uint)frameOut.stFrameInfo.nWidth;
        //初始化CMvdImage
        cMvdImage.InitImage((uint)frameOut.stFrameInfo.nWidth, (uint)frameOut.stFrameInfo.nHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08, stImageData);
    }
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelType.PixelType_Gvsp_RGB8_Packed)
    {
        stImageData.stDataChannel[0].nRowStep = (uint)frameOut.stFrameInfo.nWidth * 3;
        //初始化CMvdImage
        cMvdImage.InitImage((uint)frameOut.stFrameInfo.nWidth, (uint)frameOut.stFrameInfo.nHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3, stImageData);
    }
    return cMvdImage;
}
```

**注意事项 / 坑**：相机 RGB8_Packed 在 C# 算子侧映射为 `MVD_PIXEL_RGB_RGB24_C3`（RGB）；`stImageData` 与 `byte[]` 为托管对象，注意生命周期。

**问题根因**：不熟悉相机采图转换为其它类型。

---

### 3.3 Bitmap 转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、算子输出、流程输出图像

**适用场景**：`Bitmap` → 流程输入 / Group 输入 / 图像源 SDK 输入 / 模块输入 / 算子输入；以及流程输出 `ImageBaseData_V2` / `ImageBaseData` → `Bitmap`。

**关键类型 / 类名**：`System.Drawing.Bitmap`、`BitmapData`、`PixelFormat.Format8bppIndexed` / `Format24bppRgb`、`ImageBaseData_V2`、`ImageBaseData`、`InputImageData`、`CMvdImage`、`MvdException`、`MVD_MODULE_TYPE`、`MVD_ERROR_CODE`、`VMPixelFormat`、`ImagePixelFormat`。

#### 3.3.1 Bitmap 转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V2）

```csharp
public ImageBaseData_V2 BitmapToImageBaseData_V2(Bitmap bmpInputImg)
{
    ImageBaseData_V2 imageBaseData_V2 = new ImageBaseData_V2();
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputImg.PixelFormat;
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0, bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnly, bitPixelFormat);//锁定

    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height;//imageBaseData_V2 图像真正的缓存长度
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex++];
            }
            bitmapIndex += offset;//删除冗余数据
        }
        IntPtr _ImageBaseDataIntptr = Marshal.AllocHGlobal(ImageBaseDataSize);
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, _ImageBaseDataIntptr, ImageBaseDataSize);
        imageBaseData_V2 = new ImageBaseData_V2(_ImageBaseDataIntptr, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, VMPixelFormat.VM_PIXEL_MONO_08);

        // 上面new imageBaseData_V2 是浅拷贝，imageBaseData_V2使用结束后需要手动释放
        //Marshal.FreeHGlobal(_ImageBaseDataIntptr);
    }
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format24bppRgb)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width * 3;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height * 3;//imageBaseData_V2 图像真正的缓存长度
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 2];//bitmap 为BGR，imageBaseData_V2 为RGB
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 1];
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex];
                bitmapIndex += 3;
            }
            bitmapIndex += offset;
        }
        IntPtr _ImageBaseDataIntptr = Marshal.AllocHGlobal(ImageBaseDataSize);
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, _ImageBaseDataIntptr, ImageBaseDataSize);
        imageBaseData_V2 = new ImageBaseData_V2(_ImageBaseDataIntptr, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, VMPixelFormat.VM_PIXEL_RGB24_C3);
        // 上面new imageBaseData_V2 是浅拷贝，使用结束后需要手动释放
        //Marshal.FreeHGlobal(_ImageBaseDataIntptr);
    }
    bmpInputImg.UnlockBits(bmData);  // 解除锁定
    return imageBaseData_V2;
}
```

**注意事项 / 坑**：灰度需按 `Stride` 去冗余位；彩色不仅要去 `Stride` 冗余位，还要 BGR→RGB 交换；`ImageBaseData_V2(IntPtr)` 是浅拷贝，需 `Marshal.FreeHGlobal` 释放。

#### 3.3.2 Bitmap 转图像源 SDK 输入（ImageBaseData）

```csharp
public ImageBaseData BitmapToImageBaseData(Bitmap bmpInputImg)
{
    ImageBaseData imageBaseData = new ImageBaseData();
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputImg.PixelFormat;
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0, bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnly, bitPixelFormat);//锁定

    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height;
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex++];
            }
            bitmapIndex += offset;
        }
        imageBaseData = new ImageBaseData(_ImageBaseDataBufferBytes, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, (int)VMPixelFormat.VM_PIXEL_MONO_08);
    }
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format24bppRgb)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width * 3;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height * 3;
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 2];
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 1];
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex];
                bitmapIndex += 3;
            }
            bitmapIndex += offset;
        }
        imageBaseData = new ImageBaseData(_ImageBaseDataBufferBytes, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, (int)VMPixelFormat.VM_PIXEL_RGB24_C3);
    }
    bmpInputImg.UnlockBits(bmData);  // 解除锁定
    return imageBaseData;
}
```

#### 3.3.3 Bitmap 转模块输入（InputImageData）

```csharp
public InputImageData BitmapToInputImageData(Bitmap bmpInputImg)
{
    InputImageData inputImageData = new InputImageData();
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputImg.PixelFormat;
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0, bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnly, bitPixelFormat);//锁定

    inputImageData.Names.DataName = "InImage";//只能使用默认名称InImage
    inputImageData.Names.HeightName = "InImageHeight";//默认InImageHeight
    inputImageData.Names.WidthName = "InImageWidth";//默认InImageWidth
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";//默认InImagePixelFormat
    inputImageData.Width = bmData.Width;
    inputImageData.Height = bmData.Height;

    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format8bppIndexed)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height;
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex++];
            }
            bitmapIndex += offset;
        }
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;
        inputImageData.DataLen = (uint)ImageBaseDataSize;
        inputImageData.Data = Marshal.AllocHGlobal(ImageBaseDataSize);//inputImageData.Data 需要申请内存; 记得inputImageData 使用完成后，手动释放内存，Marshal.FreeHGlobal
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, inputImageData.Data, _ImageBaseDataBufferBytes.Length);
    }
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format24bppRgb)
    {
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bitmap 图像缓存长度
        int offset = bmData.Stride - bmData.Width * 3;
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height * 3;
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize];
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDataSize];
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmapDataSize);
        int bitmapIndex = 0;
        int ImageBaseDataIndex = 0;
        for (int i = 0; i < bmData.Height; i++)
        {
            for (int j = 0; j < bmData.Width; j++)
            {
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 2];
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex + 1];
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] = _BitImageBufferBytes[bitmapIndex];
                bitmapIndex += 3;
            }
            bitmapIndex += offset;
        }
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_RGB24;
        inputImageData.DataLen = (uint)ImageBaseDataSize;
        inputImageData.Data = Marshal.AllocHGlobal(ImageBaseDataSize);// //inputImageData.Data 需要申请内存; 记得inputImageData 使用完成后，手动释放内存，Marshal.FreeHGlobal
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, inputImageData.Data, _ImageBaseDataBufferBytes.Length);
    }
    bmpInputImg.UnlockBits(bmData);  // 解除锁定
    return inputImageData;
}
```

**注意事项 / 坑**：`InputImageData.Data` 必须 `AllocHGlobal`，用后 `FreeHGlobal`；彩色做了 BGR→RGB 交换。

#### 3.3.4 Bitmap 与算子（CmvdImage）互转

```csharp
private static void ConvertBitmap2MVDImage(Bitmap cBitmapImg, CMvdImage cMvdImg)
{
    // 参数合法性判断
    if (null == cBitmapImg || null == cMvdImg)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL);
    }

    // 判断像素格式
    if (PixelFormat.Format8bppIndexed != cBitmapImg.PixelFormat && PixelFormat.Format24bppRgb != cBitmapImg.PixelFormat)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    Int32 nImageWidth = cBitmapImg.Width;
    Int32 nImageHeight = cBitmapImg.Height;
    Int32 nChannelNum = 0;
    BitmapData bitmapData = null;

    try
    {
        // 获取图像信息
        if (PixelFormat.Format8bppIndexed == cBitmapImg.PixelFormat) // 灰度图
        {
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, nImageWidth, nImageHeight)
                                                            , ImageLockMode.ReadOnly
                                                            , PixelFormat.Format8bppIndexed);
            cMvdImg.InitImage(Convert.ToUInt32(nImageWidth), Convert.ToUInt32(nImageHeight), MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08);
            nChannelNum = 1;
        }
        else if (PixelFormat.Format24bppRgb == cBitmapImg.PixelFormat) // 彩色图
        {
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, nImageWidth, nImageHeight)
                                                        , ImageLockMode.ReadOnly
                                                        , PixelFormat.Format24bppRgb);
            cMvdImg.InitImage(Convert.ToUInt32(nImageWidth), Convert.ToUInt32(nImageHeight), MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3);
            nChannelNum = 3;
        }

        // 考虑图像是否4 字节对齐，bitmap 要求4 字节对齐，而mvdimage 不要求对齐
        if (0 == nImageWidth % 4) // 4 字节对齐时，直接拷贝
        {
            Marshal.Copy(bitmapData.Scan0, cMvdImg.GetImageData().stDataChannel[0].arrDataBytes, 0, nImageWidth * nImageHeight * nChannelNum);
        }
        else // 按步长逐行拷贝
        {
            // 每行实际占用字节数
            Int32 nRowPixelByteNum = nImageWidth * nChannelNum + 4 - (nImageWidth * nChannelNum % 4);
            // 每行首字节首地址
            IntPtr bitmapDataRowPos = IntPtr.Zero;
            for (int i = 0; i < nImageHeight; i++)
            {
                // 获取每行第一个像素值的首地址
                bitmapDataRowPos = new IntPtr(bitmapData.Scan0.ToInt64() + nRowPixelByteNum * i);
                Marshal.Copy(bitmapDataRowPos, cMvdImg.GetImageData().stDataChannel[0].arrDataBytes, i * nImageWidth * nChannelNum, nImageWidth * nChannelNum);
            }
        }

        // bitmap 彩色图按BGR 存储，而MVDimg 按RGB 存储，改变存储顺序
        // 交换R 和B
        if (PixelFormat.Format24bppRgb == cBitmapImg.PixelFormat)
        {
            byte bTemp;
            byte[] bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
            for (int i = 0; i < nImageWidth * nImageHeight; i++)
            {
                bTemp = bMvdImgData[3 * i];
                bMvdImgData[3 * i] = bMvdImgData[3 * i + 2];
                bMvdImgData[3 * i + 2] = bTemp;
            }
        }
    }
    finally
    {
        cBitmapImg.UnlockBits(bitmapData);
    }
}
```

```csharp
private static void ConvertMVDImage2Bitmap(CMvdImage cMvdImg, ref Bitmap cBitmapImg)
{
    // 参数合法性判断
    if (null == cMvdImg)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL);
    }

    // 判断像素格式
    if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 != cMvdImg.PixelFormat && MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 != cMvdImg.PixelFormat)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    Int32 nImageWidth = Convert.ToInt32(cMvdImg.Width);
    Int32 nImageHeight = Convert.ToInt32(cMvdImg.Height);
    Int32 nChannelNum = 0;
    BitmapData bitmapData = null;
    byte[] bBitmapDataTemp = null;
    try
    {
        // 获取图像信息
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == cMvdImg.PixelFormat) // 灰度图
        {
            cBitmapImg = new Bitmap(nImageWidth, nImageHeight, PixelFormat.Format8bppIndexed);

            // 灰度图需指定调色板
            ColorPalette colorPalette = cBitmapImg.Palette;
            for (int j = 0; j < 256; j++)
            {
                colorPalette.Entries[j] = Color.FromArgb(j, j, j);
            }
            cBitmapImg.Palette = colorPalette;

            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, nImageWidth, nImageHeight)
                                                            , ImageLockMode.WriteOnly
                                                            , PixelFormat.Format8bppIndexed);

            // 灰度图不做深拷贝
            bBitmapDataTemp = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
            nChannelNum = 1;
        }
        else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == cMvdImg.PixelFormat) // 彩色图
        {
            cBitmapImg = new Bitmap(nImageWidth, nImageHeight, PixelFormat.Format24bppRgb);
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, nImageWidth, nImageHeight)
                                                        , ImageLockMode.WriteOnly
                                                        , PixelFormat.Format24bppRgb);
            // 彩色图做深拷贝
            bBitmapDataTemp = new byte[cMvdImg.GetImageData().stDataChannel[0].arrDataBytes.Length];
            Array.Copy(cMvdImg.GetImageData().stDataChannel[0].arrDataBytes, bBitmapDataTemp, bBitmapDataTemp.Length);
            nChannelNum = 3;
        }

        // bitmap 彩色图按BGR 存储，而MVDimg 按RGB 存储，改变存储顺序
        // 交换R 和B
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == cMvdImg.PixelFormat)
        {
            byte bTemp;
            for (int i = 0; i < nImageWidth * nImageHeight; i++)
            {
                bTemp = bBitmapDataTemp[3 * i];
                bBitmapDataTemp[3 * i] = bBitmapDataTemp[3 * i + 2];
                bBitmapDataTemp[3 * i + 2] = bTemp;
            }
        }

        // 考虑图像是否4 字节对齐，bitmap 要求4 字节对齐，而mvdimage 不要求对齐
        if (0 == nImageWidth % 4) // 4 字节对齐时，直接拷贝
        {
            Marshal.Copy(bBitmapDataTemp, 0, bitmapData.Scan0, nImageWidth * nImageHeight * nChannelNum);
        }
        else // 按步长逐行拷贝
        {
            // 每行实际占用字节数
            Int32 nRowPixelByteNum = nImageWidth * nChannelNum + 4 - (nImageWidth * nChannelNum % 4);
            // 每行首字节首地址
            IntPtr bitmapDataRowPos = IntPtr.Zero;
            for (int i = 0; i < nImageHeight; i++)
            {
                // 获取每行第一个像素值的首地址
                bitmapDataRowPos = new IntPtr(bitmapData.Scan0.ToInt64() + nRowPixelByteNum * i);
                Marshal.Copy(bBitmapDataTemp, i * nImageWidth * nChannelNum, bitmapDataRowPos, nImageWidth * nChannelNum);
            }
        }

        cBitmapImg.UnlockBits(bitmapData);
    }
    catch (MvdException ex)
    {
        if (null != cBitmapImg)
        {
            cBitmapImg.UnlockBits(bitmapData);
            cBitmapImg.Dispose();
            cBitmapImg = null;
        }
        throw ex;
    }
    catch (System.Exception ex)
    {
        if (null != cBitmapImg)
        {
            cBitmapImg.UnlockBits(bitmapData);
            cBitmapImg.Dispose();
            cBitmapImg = null;
        }
        throw ex;
    }
}
```

**注意事项 / 坑**：非 4 字节对齐宽度必须逐行拷贝；彩色必须 BGR↔RGB 交换；灰度 `Bitmap` 必须设 256 级灰度调色板，否则显示异常；`ConvertMVDImage2Bitmap` 彩色图先深拷贝 `arrDataBytes` 再交换，避免改到源 `CMvdImage`。

#### 3.3.5 流程输出（ImageBaseData_V2 / ImageBaseData）转 Bitmap

**适用场景**：VM4.2 流程输出 `ImageBaseData_V2` 转 `Bitmap`；VM4.3 流程输出 `ImageBaseData` 转 `Bitmap`（两个函数）。

```csharp
public Bitmap ImageBaseData_V2ToBitmap(ImageBaseData_V2 imageBaseData_V2)//VM4.2SDK 流程输出图像类型为ImageBaseData_V2
{
    Bitmap bmpInputImg = null;
    byte[] buffer = new byte[imageBaseData_V2.DataLen];
    Marshal.Copy(imageBaseData_V2.ImageData, buffer, 0, buffer.Length);

    if (VMPixelFormat.VM_PIXEL_MONO_08 == imageBaseData_V2.Pixelformat)
    {
        Int32 imageWidth = Convert.ToInt32(imageBaseData_V2.Width);
        Int32 imageHeight = Convert.ToInt32(imageBaseData_V2.Height);
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = System.Drawing.Imaging.PixelFormat.Format8bppIndexed;
        bmpInputImg = new Bitmap(imageWidth, imageHeight, bitMaPixelFormat);
        int offset = imageWidth % 4 != 0 ? (4 - imageWidth % 4) : 0;//添加冗余位，变成4 的倍数
        int strid = imageWidth + offset;
        int bitmapBytesLenth = strid * imageHeight;
        byte[] bitmapDataBytes = new byte[bitmapBytesLenth];
        for (int i = 0; i < imageHeight; i++)
        {
            for (int j = 0; j < strid; j++)
            {
                int bitIndex = i * strid + j;
                int mvdIndex = i * imageWidth + j;
                if (j >= imageWidth)
                {
                    bitmapDataBytes[bitIndex] = 0;//冗余位填充0
                }
                else
                {
                    bitmapDataBytes[bitIndex] = buffer[mvdIndex];
                }
            }
        }
        BitmapData bitmapData = bmpInputImg.LockBits(new Rectangle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitMaPixelFormat);
        IntPtr imageBufferPtr = bitmapData.Scan0;
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapBytesLenth);
        bmpInputImg.UnlockBits(bitmapData);

        var colorPalettes = bmpInputImg.Palette;
        for (int j = 0; j < 256; j++)
        {
            colorPalettes.Entries[j] = Color.FromArgb(j, j, j);
        }
        bmpInputImg.Palette = colorPalettes;
    }
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == imageBaseData_V2.Pixelformat)
    {
        Int32 imageWidth = Convert.ToInt32(imageBaseData_V2.Width);
        Int32 imageHeight = Convert.ToInt32(imageBaseData_V2.Height);
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = System.Drawing.Imaging.PixelFormat.Format24bppRgb;
        bmpInputImg = new Bitmap(imageWidth, imageHeight, bitMaPixelFormat);
        int offset = imageWidth % 4 != 0 ? (4 - (imageWidth * 3) % 4) : 0;//添加冗余位，变成4 的倍数
        int strid = imageWidth * 3 + offset;
        int bitmapBytesLenth = strid * imageHeight;
        byte[] bitmapDataBytes = new byte[bitmapBytesLenth];
        for (int i = 0; i < imageHeight; i++)
        {
            for (int j = 0; j < imageWidth; j++)
            {
                int mvdIndex = i * imageWidth * 3 + j * 3;
                int bitIndex = i * strid + j * 3;
                bitmapDataBytes[bitIndex] = buffer[mvdIndex + 2];
                bitmapDataBytes[bitIndex + 1] = buffer[mvdIndex + 1];
                bitmapDataBytes[bitIndex + 2] = buffer[mvdIndex];
            }
            for (int k = 0; k < offset; k++)
            {
                bitmapDataBytes[i * strid + imageWidth * 3 + k] = 0;
            }
        }
        BitmapData bitmapData = bmpInputImg.LockBits(new Rectangle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitMaPixelFormat);
        IntPtr imageBufferPtr = bitmapData.Scan0;
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapBytesLenth);
        bmpInputImg.UnlockBits(bitmapData);
    }
    return bmpInputImg;
}
```

```csharp
public static Bitmap ImageBaseDatToBitmap(ImageBaseData imageBaseDataInput)// VM4.3SDK 流程输出图像类型为ImageBaseData
{
    Bitmap bmpOutputImg = null;
    byte[] buffer = new byte[imageBaseDataInput.DataLen];
    buffer = imageBaseDataInput.ImageData;

    if (VMPixelFormat.VM_PIXEL_MONO_08 == (VMPixelFormat)imageBaseDataInput.Pixelformat)
    {
        Int32 imageWidth = Convert.ToInt32(imageBaseDataInput.Width);
        Int32 imageHeight = Convert.ToInt32(imageBaseDataInput.Height);
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = System.Drawing.Imaging.PixelFormat.Format8bppIndexed;
        bmpOutputImg = new Bitmap(imageWidth, imageHeight, bitMaPixelFormat);
        int offset = imageWidth % 4 != 0 ? (4 - imageWidth % 4) : 0;//添加冗余位，变成4 的倍数
        int strid = imageWidth + offset;
        int bitmapBytesLenth = strid * imageHeight;
        byte[] bitmapDataBytes = new byte[bitmapBytesLenth];
        for (int i = 0; i < imageHeight; i++)
        {
            for (int j = 0; j < strid; j++)
            {
                int bitIndex = i * strid + j;
                int mvdIndex = i * imageWidth + j;
                if (j >= imageWidth)
                {
                    bitmapDataBytes[bitIndex] = 0;//冗余位填充0
                }
                else
                {
                    bitmapDataBytes[bitIndex] = buffer[mvdIndex];
                }
            }
        }
        BitmapData bitmapData = bmpOutputImg.LockBits(new Rectangle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitMaPixelFormat);
        IntPtr imageBufferPtr = bitmapData.Scan0;
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapBytesLenth);
        bmpOutputImg.UnlockBits(bitmapData);

        var colorPalettes = bmpOutputImg.Palette;
        for (int j = 0; j < 256; j++)
        {
            colorPalettes.Entries[j] = Color.FromArgb(j, j, j);
        }
        bmpOutputImg.Palette = colorPalettes;
    }
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == (VMPixelFormat)imageBaseDataInput.Pixelformat)
    {
        Int32 imageWidth = Convert.ToInt32(imageBaseDataInput.Width);
        Int32 imageHeight = Convert.ToInt32(imageBaseDataInput.Height);
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = System.Drawing.Imaging.PixelFormat.Format24bppRgb;
        bmpOutputImg = new Bitmap(imageWidth, imageHeight, bitMaPixelFormat);
        int offset = imageWidth % 4 != 0 ? (4 - (imageWidth * 3) % 4) : 0;//添加冗余位，变成4 的倍数
        int strid = imageWidth * 3 + offset;
        int bitmapBytesLenth = strid * imageHeight;
        byte[] bitmapDataBytes = new byte[bitmapBytesLenth];
        for (int i = 0; i < imageHeight; i++)
        {
            for (int j = 0; j < imageWidth; j++)
            {
                int mvdIndex = i * imageWidth * 3 + j * 3;
                int bitIndex = i * strid + j * 3;
                bitmapDataBytes[bitIndex] = buffer[mvdIndex + 2];
                bitmapDataBytes[bitIndex + 1] = buffer[mvdIndex + 1];
                bitmapDataBytes[bitIndex + 2] = buffer[mvdIndex];
            }
            for (int k = 0; k < offset; k++)
            {
                bitmapDataBytes[i * strid + imageWidth * 3 + k] = 0;
            }
        }
        BitmapData bitmapData = bmpOutputImg.LockBits(new Rectangle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitMaPixelFormat);
        IntPtr imageBufferPtr = bitmapData.Scan0;
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapBytesLenth);
        bmpOutputImg.UnlockBits(bitmapData);
    }
    return bmpOutputImg;
}
```

**注意事项 / 坑**：VM 输出是 RGB，Bitmap 是 BGR，彩色需交换 R/B；Bitmap 必须补齐行到 4 字节对齐（`offset`）；灰度需设调色板。

**问题根因**：不熟悉 Bitmap 转换为其它类型。

---

### 3.4 Mat 转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、算子输出、流程输出、脚本图像

**适用场景**：`OpenCvSharp.Mat` → 流程输入 / Group 输入 / 图像源 SDK / 模块输入 / 算子输入；算子输出 → Mat；流程输出 → Mat；Mat ↔ 脚本图像 `ImageData`。

**关键类型 / 类名**：`Mat`、`MatType`、`Cv2`、`ColorConversionCodes`、`ImageBaseData_V2`、`ImageBaseData`、`InputImageData`、`CMvdImage`、`MVD_PIXEL_FORMAT`、`ImageData`、`ImagePixelFormate`。

#### 3.4.1 Mat 转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V2）

```csharp
public ImageBaseData_V2 MatToImageBaseData_V2(Mat matInputImg)
{
    ImageBaseData_V2 imageBaseData_V2 = new ImageBaseData_V2();
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height * matInputImg.Channels());
    if (1 == matInputImg.Channels())
    {
        imageBaseData_V2 = new ImageBaseData_V2(matInputImg.Ptr(0), dataLen, matInputImg.Width, matInputImg.Height, VMPixelFormat.VM_PIXEL_MONO_08);
    }
    else if (3 == matInputImg.Channels())
    {
        //交换R 与B 通道
        Cv2.CvtColor(matInputImg, matInputImg, ColorConversionCodes.BGR2RGB);
        imageBaseData_V2 = new ImageBaseData_V2(matInputImg.Ptr(0), dataLen, matInputImg.Width, matInputImg.Height, VMPixelFormat.VM_PIXEL_RGB24_C3);
    }
    return imageBaseData_V2;
}
```

**注意事项 / 坑**：`ImageBaseData_V2(IntPtr)` 浅拷贝 Mat 缓冲，Mat 释放后该图像悬空；彩色先 `BGR2RGB` 再传。

#### 3.4.2 Mat 转图像源 SDK 输入（ImageBaseData）

```csharp
public ImageBaseData MatToImageBaseData(Mat matInputImg)
{
    ImageBaseData imageBaseData = new ImageBaseData();
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height * matInputImg.Channels());
    byte[] buffer = new byte[dataLen];
    Marshal.Copy(matInputImg.Ptr(0), buffer, 0, buffer.Length);
    if (1 == matInputImg.Channels())
    {
        imageBaseData = new ImageBaseData(buffer, dataLen, matInputImg.Width, matInputImg.Height, (int)VMPixelFormat.VM_PIXEL_MONO_08);
    }
    else if (3 == matInputImg.Channels())
    {
        //交换R 与B 通道
        for (int i = 0; i < buffer.Length - 2; i += 3)
        {
            byte temp = buffer[i];
            buffer[i] = buffer[i + 2];
            buffer[i + 2] = temp;
        }
        imageBaseData = new ImageBaseData(buffer, dataLen, matInputImg.Width, matInputImg.Height, (int)VMPixelFormat.VM_PIXEL_RGB24_C3);
    }
    return imageBaseData;
}
```

#### 3.4.3 Mat 转模块输入（InputImageData）

```csharp
public InputImageData MatToInputImageData(Mat matInputImg)
{
    InputImageData inputImageData = new InputImageData();
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height * matInputImg.Channels());
    byte[] buffer = new byte[dataLen];
    Marshal.Copy(matInputImg.Ptr(0), buffer, 0, buffer.Length);

    inputImageData.Names.DataName = "InImage";//只能使用默认名称InImage
    inputImageData.Names.HeightName = "InImageHeight";//默认InImageHeight
    inputImageData.Names.WidthName = "InImageWidth";//默认InImageWidth
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";//默认InImagePixelFormat
    inputImageData.Width = matInputImg.Width;
    inputImageData.Height = matInputImg.Height;
    inputImageData.DataLen = dataLen;
    //inputImageData.Data 需要申请内存
    inputImageData.Data = Marshal.AllocHGlobal((int)dataLen);

    if (1 == matInputImg.Channels())
    {
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;
        Marshal.Copy(buffer, 0, inputImageData.Data, buffer.Length);
    }
    else if (3 == matInputImg.Channels())
    {
        //交换R 与B 通道
        for (int i = 0; i < buffer.Length - 2; i += 3)
        {
            byte temp = buffer[i];
            buffer[i] = buffer[i + 2];
            buffer[i + 2] = temp;
        }
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_RGB24;
        Marshal.Copy(buffer, 0, inputImageData.Data, buffer.Length);
    }
    return inputImageData;
}
```

#### 3.4.4 Mat 与算子图像（CmvdImage）互转

```csharp
private static void ConvertMat2MVDImage(Mat mat, CMvdImage cMvdImg)
{
    // 参数合法性判断
    if (null == mat || null == cMvdImg)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_HANDLE);
    }
    // 像素格式判断
    if (MatType.CV_8UC1 != mat.Type() && MatType.CV_8UC3 != mat.Type())
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    uint imgWidth = (uint)mat.Size().Width;// 图片的真实宽度
    uint imgHeight = (uint)mat.Size().Height;// 图片的真实高度
    byte[] bMvdImgData = null;

    // 根据传入的mat 图像初始化MVDImage，并进行转换
    if (mat.Type() == MatType.CV_8UC1)
    {
        cMvdImg.InitImage(imgWidth, imgHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08);
        bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
        Marshal.Copy(mat.Ptr(0), bMvdImgData, 0, bMvdImgData.Length);
    }
    else if (mat.Type() == MatType.CV_8UC3)
    {
        cMvdImg.InitImage(imgWidth, imgHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3);
        bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
        Marshal.Copy(mat.Ptr(0), bMvdImgData, 0, bMvdImgData.Length);

        // Mat 为BGRBGR...存储，MVDImage 为RGBRGB...存储，需要调整
        byte bTemp;
        for (int i = 0; i < imgWidth * imgHeight; i++)
        {
            bTemp = bMvdImgData[3 * i];
            bMvdImgData[3 * i] = bMvdImgData[3 * i + 2];
            bMvdImgData[3 * i + 2] = bTemp;
        }
    }
}
```

```csharp
private static void ConvertMVDImage2Mat(CMvdImage mvdImage, Mat mat)
{
    // 参数合法性判断
    if (null == mat || null == mvdImage)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_HANDLE);
    }

    // 像素格式判断
    if (mvdImage.PixelFormat != MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 && mvdImage.PixelFormat != MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    int imgWidth = (int)mvdImage.Width;
    int imgHeight = (int)mvdImage.Height;

    // 根据传入的MVDImage 类型初始化Mat
    if (mvdImage.PixelFormat == MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08)
    {
        mat.Create(imgHeight, imgWidth, MatType.CV_8UC1);
        Marshal.Copy(mvdImage.GetImageData(0).arrDataBytes, 0, mat.Ptr(0), mvdImage.GetImageData(0).arrDataBytes.Length);
    }
    else if (mvdImage.PixelFormat == MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3)
    {
        mat.Create(imgHeight, imgWidth, MatType.CV_8UC3);
        // 先备份MVD 图像数据，保证不改变源图像数据
        byte[] bMvdImgDataTemp = new byte[mvdImage.GetImageData(0).arrDataBytes.Length];
        Array.Copy(mvdImage.GetImageData(0).arrDataBytes, bMvdImgDataTemp, bMvdImgDataTemp.Length);

        // Mat 为BGRBGR...存储，MVD 为RGBRGB...存储，需要调整
        byte bTemp;
        for (int i = 0; i < imgWidth * imgHeight; i++)
        {
            bTemp = bMvdImgDataTemp[3 * i];
            bMvdImgDataTemp[3 * i] = bMvdImgDataTemp[3 * i + 2];
            bMvdImgDataTemp[3 * i + 2] = bTemp;
        }
        // 将数据拷贝至Mat 图像
        Marshal.Copy(bMvdImgDataTemp, 0, mat.Ptr(0), bMvdImgDataTemp.Length);
    }
}
```

#### 3.4.5 流程输出（ImageBaseData_V2）转 Mat

```csharp
public Mat ImageBaseData_V2ToMat(ImageBaseData_V2 imageBaseData_V2)
{
    Mat matInputImg = new Mat();
    byte[] buffer = new byte[imageBaseData_V2.DataLen];
    Marshal.Copy(imageBaseData_V2.ImageData, buffer, 0, buffer.Length);

    if (VMPixelFormat.VM_PIXEL_MONO_08 == imageBaseData_V2.Pixelformat)
    {
        matInputImg.Create(imageBaseData_V2.Height, imageBaseData_V2.Width, MatType.CV_8UC1);
        Marshal.Copy(buffer, 0, matInputImg.Ptr(0), buffer.Length);
    }
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == imageBaseData_V2.Pixelformat)
    {
        matInputImg.Create(imageBaseData_V2.Height, imageBaseData_V2.Width, MatType.CV_8UC3);

        //交换R 与B 通道
        for (int i = 0; i < buffer.Length - 2; i += 3)
        {
            byte temp = buffer[i];
            buffer[i] = buffer[i + 2];
            buffer[i + 2] = temp;
        }
        Marshal.Copy(buffer, 0, matInputImg.Ptr(0), buffer.Length);
    }
    return matInputImg;
}
```

#### 3.4.6 Mat 与脚本图像（ImageData）互转

```csharp
public ImageData MatToImageData(Mat matImage)
{
    ImageData imgOut = new ImageData();
    byte[] buffer = new Byte[matImage.Width * matImage.Height * matImage.Channels()];
    Marshal.Copy(matImage.Ptr(0), buffer, 0, buffer.Length);
    if (1 == matImage.Channels())
    {
        imgOut.Buffer = buffer;
        imgOut.Width = matImage.Width;
        imgOut.Heigth = matImage.Height;
        imgOut.PixelFormat = ImagePixelFormate.MONO8;
    }
    else if (3 == matImage.Channels())
    {
        //交换R 与B 通道
        for (int i = 0; i < buffer.Length - 2; i += 3)
        {
            byte temp = buffer[i];
            buffer[i] = buffer[i + 2];
            buffer[i + 2] = temp;
        }

        imgOut.Buffer = buffer;
        imgOut.Width = matImage.Width;
        imgOut.Heigth = matImage.Height;
        imgOut.PixelFormat = ImagePixelFormate.RGB24;
    }
    return imgOut;
}
```

```csharp
public Mat ImageDataToMat(ImageData img)
{
    Mat matImage = new Mat();
    if (ImagePixelFormate.MONO8 == img.PixelFormat)
    {
        matImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV_8UC1);
        IntPtr grayPtr = Marshal.AllocHGlobal(img.Width * img.Heigth);
        Marshal.Copy(img.Buffer, 0, matImage.Ptr(0), img.Buffer.Length);

        //用完记得释放指针
        Marshal.FreeHGlobal(grayPtr);
    }
    else if (ImagePixelFormate.RGB24 == img.PixelFormat)
    {
        matImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV_8UC3);
        IntPtr rgbPtr = Marshal.AllocHGlobal(img.Width * img.Heigth * 3);
        Marshal.Copy(img.Buffer, 0, matImage.Ptr(0), img.Buffer.Length);
        Cv2.CvtColor(matImage, matImage, ColorConversionCodes.RGB2BGR);

        //用完记得释放指针
        Marshal.FreeHGlobal(rgbPtr);
    }
    return matImage;
}
```

**注意事项 / 坑**：`ImageData.Heigth` 是官方原文拼写（非 Height，注意脚本图像属性名就是 `Heigth`）；`ImageDataToMat` 中 `grayPtr`/`rgbPtr` 分配后并未真正用于拷贝（直接拷 `img.Buffer`），分配仅为示例，实际需释放；彩色脚本图是 RGB，转 Mat 需 `RGB2BGR`。

**问题根因**：不熟悉 Mat 转换为其它类型。

---

### 3.5 Halcon 转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、算子输出、流程输出、脚本图像

**适用场景**：`HalconDotNet.HObject` → 流程输入 / Group 输入 / 图像源 SDK / 模块输入 / 算子输入；算子输出 → Halcon；流程输出 → Halcon；Halcon ↔ 脚本图像 `ImageData`。

**关键类型 / 类名**：`HObject`、`HOperatorSet`、`HTuple`、`GetObjClass`、`GetImageType`、`CountChannels`、`GetImagePointer1` / `GetImagePointer3`、`GenImage1` / `GenImage3`、`ImageBaseData_V2`、`ImageBaseData`、`InputImageData`、`CMvdImage`、`ImageData`、`ImagePixelFormate`。

#### 3.5.1 Halcon 图像转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V2）

```csharp
public static ImageBaseData_V2 HalconImageToImageBaseDataV2(HObject hImageObj)
{
    try
    {
        ImageBaseData_V2 imageBaseData = new ImageBaseData_V2();
        HTuple imageWidth = 0;
        HTuple imageHeight = 0;
        HTuple objClass = hImageObj.GetObjClass();
        if (objClass.S.Equals("image"))
        {
            HTuple imageType;
            HOperatorSet.GetImageType(hImageObj, out imageType);
            if (imageType.S.Equals("byte"))
            {
                //获取图像通道数
                HTuple channels = 0;
                HOperatorSet.CountChannels(hImageObj, out channels);
                //如果是单通道
                if (channels.I == 1)
                {
                    HTuple imagePointer;
                    HOperatorSet.GetImagePointer1(hImageObj, out imagePointer, out imageType, out imageWidth, out imageHeight);
                    imageBaseData.Width = imageWidth.I;
                    imageBaseData.Height = imageHeight.I;
                    imageBaseData.Pixelformat = VMPixelFormat.VM_PIXEL_MONO_08;
                    imageBaseData.DataLen = (uint)(imageWidth.I * imageBaseData.Height);
                    imageBaseData.ImageData = imagePointer;
                }
                //如果是三通道
                else if (channels.I == 3)
                {
                    HTuple redChannel;
                    HTuple greenChannel;
                    HTuple blueChannel;
                    HOperatorSet.GetImagePointer3(hImageObj, out redChannel, out greenChannel, out blueChannel, out imageType, out imageWidth, out imageHeight);
                    imageBaseData.Width = imageWidth.I;
                    imageBaseData.Height = imageHeight.I;
                    imageBaseData.Pixelformat = VMPixelFormat.VM_PIXEL_RGB24_C3;
                    byte[] imageRedBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageGreenBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageBlueBuffer = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(redChannel, imageRedBuffer, 0, imageRedBuffer.Length);
                    Marshal.Copy(greenChannel, imageGreenBuffer, 0, imageGreenBuffer.Length);
                    Marshal.Copy(blueChannel, imageBlueBuffer, 0, imageBlueBuffer.Length);
                    byte[] imageBuffer = new byte[imageWidth.I * imageHeight.I * 3];
                    for (int row = 0; row < imageHeight.I; row++)
                    {
                        for (int col = 0, index = 0; col < imageWidth.I; col++, index += 3)
                        {
                            imageBuffer[index] = imageRedBuffer[row * imageWidth + col];
                            imageBuffer[index + 1] = imageGreenBuffer[row * imageWidth + col];
                            imageBuffer[index + 2] = imageBlueBuffer[row * imageWidth + col];
                        }
                    }
                    imageBaseData.DataLen = (uint)(imageWidth.I * imageBaseData.Height * 3);
                    imageBaseData.ImageData = Marshal.UnsafeAddrOfPinnedArrayElement(imageBuffer, 0);
                }
                else
                {
                    hImageObj?.Dispose();
                    throw new Exception("不支持单通道，三通道以外的图像");
                }
            }
            else
            {
                hImageObj?.Dispose();
                throw new Exception("不支持8bit 以外的位深度图像");
            }
        }
        else
        {
            hImageObj?.Dispose();
            throw new Exception("HObject 非图像类型对象");
        }
        return imageBaseData;
    }
    catch (Exception ex)
    {
        hImageObj?.Dispose();
        throw new Exception(ex.Message);
    }
}
```

**注意事项 / 坑**：三通道用 `Marshal.UnsafeAddrOfPinnedArrayElement` 取 `imageBuffer` 地址——`imageBuffer` 必须被 pin 住（GC 不能移动），否则悬空；单通道直接 `ImageData = imagePointer`（`HTuple` 底层指针，生命周期随 `hImageObj`）。

#### 3.5.2 Halcon 图像转图像源 SDK 输入（ImageBaseData）

```csharp
public static ImageBaseData HalconImageToImageBaseData(HObject hImageObj)
{
    try
    {
        ImageBaseData imageBaseData = new ImageBaseData();
        HTuple imageWidth = 0;
        HTuple imageHeight = 0;
        HTuple objClass = hImageObj.GetObjClass();
        if (objClass.S.Equals("image"))
        {
            HTuple imageType;
            HOperatorSet.GetImageType(hImageObj, out imageType);
            if (imageType.S.Equals("byte"))
            {
                //获取图像通道数
                HTuple channels = 0;
                HOperatorSet.CountChannels(hImageObj, out channels);
                //如果是单通道
                if (channels.I == 1)
                {
                    HTuple imagePointer;
                    HOperatorSet.GetImagePointer1(hImageObj, out imagePointer, out imageType, out imageWidth, out imageHeight);
                    imageBaseData.Width = imageWidth.I;
                    imageBaseData.Height = imageHeight.I;
                    imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_MONO_08;
                    imageBaseData.DataLen = (uint)(imageBaseData.Width * imageBaseData.Height);
                    imageBaseData.ImageData = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(imagePointer, imageBaseData.ImageData, 0, imageWidth.I * imageHeight.I);
                }
                //如果是三通道
                else if (channels.I == 3)
                {
                    HTuple redChannel;
                    HTuple greenChannel;
                    HTuple blueChannel;
                    HOperatorSet.GetImagePointer3(hImageObj, out redChannel, out greenChannel, out blueChannel, out imageType, out imageWidth, out imageHeight);
                    imageBaseData.Width = imageWidth.I;
                    imageBaseData.Height = imageHeight.I;
                    imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_RGB24_C3;
                    imageBaseData.DataLen = (uint)(imageWidth.I * imageBaseData.Height * 3);
                    imageBaseData.ImageData = new byte[imageWidth.I * imageHeight.I * 3];
                    byte[] imageRedBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageGreenBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageBlueBuffer = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, imageRedBuffer.Length);
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer, 0, imageGreenBuffer.Length);
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, imageBlueBuffer.Length);
                    for (int row = 0; row < imageHeight.I; row++)
                    {
                        for (int col = 0, index = 0; col < imageWidth.I; col++, index += 3)
                        {
                            imageBaseData.ImageData[index] = imageRedBuffer[row * imageWidth + col];
                            imageBaseData.ImageData[index + 1] = imageGreenBuffer[row * imageWidth + col];
                            imageBaseData.ImageData[index + 2] = imageBlueBuffer[row * imageWidth + col];
                        }
                    }
                }
                else
                {
                    hImageObj?.Dispose();
                    throw new Exception("不支持单通道，三通道以外的图像");
                }
            }
            else
            {
                hImageObj?.Dispose();
                throw new Exception("不支持8bit 以外的位深度图像");
            }
        }
        else
        {
            hImageObj?.Dispose();
            throw new Exception("HObject 非图像类型对象");
        }
        return imageBaseData;
    }
    catch (Exception ex)
    {
        hImageObj?.Dispose();
        throw new Exception(ex.Message);
    }
}
```

#### 3.5.3 Halcon 图像转模块输入（InputImageData）

```csharp
public static InputImageData HalconImageToModuleInputImage(HObject hImageObj)
{
    try
    {
        InputImageData inputImageData = new InputImageData();
        HTuple imageWidth = 0;
        HTuple imageHeight = 0;
        HTuple objClass = hImageObj.GetObjClass();
        if (objClass.S.Equals("image"))
        {
            HTuple imageType;
            HOperatorSet.GetImageType(hImageObj, out imageType);
            if (imageType.S.Equals("byte"))
            {
                //获取图像通道数
                HTuple channels = 0;
                HOperatorSet.CountChannels(hImageObj, out channels);
                //如果是单通道
                if (channels.I == 1)
                {
                    HTuple imagePointer;
                    HOperatorSet.GetImagePointer1(hImageObj, out imagePointer, out imageType, out imageWidth, out imageHeight);
                    inputImageData.Width = imageWidth.I;
                    inputImageData.Height = imageHeight.I;
                    inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO8;
                    inputImageData.DataLen = (uint)(inputImageData.Width * inputImageData.Height);
                    inputImageData.Data = imagePointer;
                    inputImageData.Names.DataName = "InImage";
                    inputImageData.Names.WidthName = "InImageWidth";
                    inputImageData.Names.HeightName = "InImageHeight";
                    inputImageData.Names.PixelFormatName = "InImagePixelFormat";
                }
                //如果是三通道
                else if (channels.I == 3)
                {
                    HTuple redChannel;
                    HTuple greenChannel;
                    HTuple blueChannel;
                    HOperatorSet.GetImagePointer3(hImageObj, out redChannel, out greenChannel, out blueChannel, out imageType, out imageWidth, out imageHeight);
                    inputImageData.Width = imageWidth.I;
                    inputImageData.Height = imageHeight.I;
                    inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_RGB24;

                    byte[] imageRedBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageGreenBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageBlueBuffer = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, imageRedBuffer.Length);
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer, 0, imageGreenBuffer.Length);
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, imageBlueBuffer.Length);
                    byte[] imageBuffer = new byte[imageWidth.I * imageHeight * 3];
                    for (int row = 0; row < imageHeight.I; row++)
                    {
                        for (int col = 0, index = 0; col < imageWidth.I; col++, index += 3)
                        {
                            imageBuffer[index] = imageRedBuffer[row * imageWidth + col];
                            imageBuffer[index + 1] = imageGreenBuffer[row * imageWidth + col];
                            imageBuffer[index + 2] = imageBlueBuffer[row * imageWidth + col];
                        }
                    }
                    inputImageData.DataLen = (uint)(inputImageData.Width * inputImageData.Height * 3);
                    inputImageData.Data = Marshal.UnsafeAddrOfPinnedArrayElement(imageBuffer, 0);
                    inputImageData.Names.DataName = "InImage";
                    inputImageData.Names.WidthName = "InImageWidth";
                    inputImageData.Names.HeightName = "InImageHeight";
                    inputImageData.Names.PixelFormatName = "InImagePixelFormat";
                }
                else
                {
                    hImageObj?.Dispose();
                    throw new Exception("不支持单通道，三通道以外的图像");
                }
            }
            else
            {
                hImageObj?.Dispose();
                throw new Exception("不支持8bit 以外的位深度图像");
            }
        }
        else
        {
            hImageObj?.Dispose();
            throw new Exception("HObject 非图像类型对象");
        }
        return inputImageData;
    }
    catch (Exception ex)
    {
        hImageObj?.Dispose();
        throw new Exception(ex.Message);
    }
}
```

**注意事项 / 坑**：单通道 `inputImageData.Data = imagePointer`（`HTuple` 指针，随 Halcon 对象）；三通道 `Data` 用 `UnsafeAddrOfPinnedArrayElement`，`imageBuffer` 须 pin 住。

#### 3.5.4 Halcon 图像与算子图像（CmvdImage）互转

```csharp
private static void ConvertHalcon2MVDImage(HObject cHalconImg, CMvdImage cMvdImg)
{
    // 参数合法性判断
    if (null == cHalconImg || null == cMvdImg)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL);
    }

    // 获取通道数量
    HTuple ChannelNum;
    HOperatorSet.CountChannels(cHalconImg, out ChannelNum);
    if (1 != ChannelNum.I && 3 != ChannelNum.I)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    HTuple ImageType;
    HTuple ImageWidth;
    HTuple ImageHeight;
    // 获取图像信息
    if (1 == ChannelNum.I) // 灰度图
    {
        HTuple ImagePoint;
        HOperatorSet.GetImagePointer1(cHalconImg, out ImagePoint, out ImageType, out ImageWidth, out ImageHeight);
        cMvdImg.InitImage(Convert.ToUInt32(ImageWidth.I), Convert.ToUInt32(ImageHeight.I), MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08);
        Marshal.Copy(ImagePoint.IP, cMvdImg.GetImageData().stDataChannel[0].arrDataBytes, 0, ImageWidth.I * ImageHeight.I);
    }
    else if (3 == ChannelNum)
    {
        HTuple ImagePointR;
        HTuple ImagePointG;
        HTuple ImagePointB;
        HOperatorSet.GetImagePointer3(cHalconImg, out ImagePointR, out ImagePointG, out ImagePointB, out ImageType, out ImageWidth, out ImageHeight);
        cMvdImg.InitImage(Convert.ToUInt32(ImageWidth.I), Convert.ToUInt32(ImageHeight.I), MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3);

        // 将IntPtr 转为byte 数组
        int nImageWidth = ImageWidth.I;
        int nImageHeight = ImageHeight.I;
        int nChannelDataLen = nImageWidth * nImageHeight;
        byte[] bImageBufR = new byte[nChannelDataLen];
        byte[] bImageBufG = new byte[nChannelDataLen];
        byte[] bImageBufB = new byte[nChannelDataLen];
        Marshal.Copy(ImagePointR.IP, bImageBufR, 0, nChannelDataLen);
        Marshal.Copy(ImagePointG.IP, bImageBufG, 0, nChannelDataLen);
        Marshal.Copy(ImagePointB.IP, bImageBufB, 0, nChannelDataLen);

        byte[] bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
        // 将图像数据拷贝至算子图像组件
        for (int i = 0; i < nImageHeight; i++)
        {
            for (int j = 0; j < nImageWidth; j++)
            {
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 0] = bImageBufR[i * nImageWidth + j];
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 1] = bImageBufG[i * nImageWidth + j];
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 2] = bImageBufB[i * nImageWidth + j];
            }
        }
    }
}
```

```csharp
private static void ConvertMVDImage2Halcon(CMvdImage cMvdImg, HObject cHalconImg)
{
    // 参数合法性判断
    if (null == cHalconImg || null == cMvdImg)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL);
    }

    // 像素格式判断
    MVD_PIXEL_FORMAT enMvdImagePixel = cMvdImg.PixelFormat;
    if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 != enMvdImagePixel && MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 != enMvdImagePixel)
    {
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT);
    }

    GCHandle hImageData = new GCHandle();
    GCHandle hImageDataR = new GCHandle();
    GCHandle hImageDataG = new GCHandle();
    GCHandle hImageDataB = new GCHandle();
    try
    {
        int nImageWidth = Convert.ToInt32(cMvdImg.Width);
        int nImageHeight = Convert.ToInt32(cMvdImg.Height);
        // 根据传入的图像初始化Halcon
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == enMvdImagePixel)
        {
            // 引用MvdImg 数据来创建halcon 图像;halcon 内部会深拷贝
            hImageData = GCHandle.Alloc(cMvdImg.GetImageData().stDataChannel[0].arrDataBytes, GCHandleType.Pinned);
            HOperatorSet.GenImage1(out cHalconImg, "byte", nImageWidth, nImageHeight, hImageData.AddrOfPinnedObject());
        }
        else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == enMvdImagePixel)
        {
            // MVDImage 图像是一个通道RGBRGBRGB...存放；需要另外开辟块内存
            int nChannelDataLen = nImageWidth * nImageHeight;
            byte[] bImageBufR = new byte[nChannelDataLen];
            byte[] bImageBufG = new byte[nChannelDataLen];
            byte[] bImageBufB = new byte[nChannelDataLen];
            byte[] bMvdImageData = cMvdImg.GetImageData().stDataChannel[0].arrDataBytes;
            // 引用MVDImage 数据进行填充
            for (int i = 0; i < nImageHeight; i++)
            {
                for (int j = 0; j < nImageWidth; j++)
                {
                    bImageBufR[i * nImageWidth + j] = bMvdImageData[i * nImageWidth * 3 + j * 3 + 0];
                    bImageBufG[i * nImageWidth + j] = bMvdImageData[i * nImageWidth * 3 + j * 3 + 1];
                    bImageBufB[i * nImageWidth + j] = bMvdImageData[i * nImageWidth * 3 + j * 3 + 2];
                }
            }
            // 创建halcon 图像
            hImageDataR = GCHandle.Alloc(bImageBufR, GCHandleType.Pinned);
            hImageDataG = GCHandle.Alloc(bImageBufG, GCHandleType.Pinned);
            hImageDataB = GCHandle.Alloc(bImageBufB, GCHandleType.Pinned);
            HOperatorSet.GenImage3(out cHalconImg, "byte", nImageWidth, nImageHeight, hImageDataR.AddrOfPinnedObject(), hImageDataG.AddrOfPinnedObject(), hImageDataB.AddrOfPinnedObject());
        }
    }
    finally
    {
        if (hImageData.IsAllocated)
        {
            hImageData.Free();
        }
        if (hImageDataR.IsAllocated)
        {
            hImageDataR.Free();
        }
        if (hImageDataG.IsAllocated)
        {
            hImageDataG.Free();
        }
        if (hImageDataB.IsAllocated)
        {
            hImageDataB.Free();
        }
    }
}
```

**注意事项 / 坑**：Halcon `GenImage1/3` 内部会深拷贝，传给它的托管数组必须用 `GCHandle.Alloc(..., Pinned)` 钉住，否则 GenImage 期间 GC 移动导致崩溃；`finally` 中务必 `Free`。

#### 3.5.5 流程输出（ImageBaseData_V2）转 Halcon 图像

```csharp
public static HObject ImageBaseDataV2ToHalconImage(ImageBaseData_V2 image)
{
    try
    {
        HObject imageObj = new HObject();
        HTuple width = image.Width;
        HTuple height = image.Height;
        if (image.Pixelformat == VMPixelFormat.VM_PIXEL_MONO_08)
        {
            HOperatorSet.GenImage1(out imageObj, "byte", width, height, image.ImageData);
        }
        else if (image.Pixelformat == VMPixelFormat.VM_PIXEL_RGB24_C3)
        {
            byte[] imageRedBuffer = new byte[width * height.I];
            byte[] imageGreenBuffer = new byte[width * height.I];
            byte[] imageBlueBuffer = new byte[width * height.I];
            byte[] imageBuffer = new byte[width * height.I * 3];
            Marshal.Copy(image.ImageData, imageBuffer, 0, imageBuffer.Length);
            for (int row = 0; row < height.I; row++)
            {
                for (int col = 0, index = 0; col < width.I; col++, index += 3)
                {
                    imageRedBuffer[row * width.I + col] = imageBuffer[index];
                    imageGreenBuffer[row * width.I + col] = imageBuffer[index + 1];
                    imageBlueBuffer[row * width.I + col] = imageBuffer[index + 2];
                }
            }
            HOperatorSet.GenImage3(
                out imageObj,
                "byte",
                width,
                height,
                Marshal.UnsafeAddrOfPinnedArrayElement(imageRedBuffer, 0),
                Marshal.UnsafeAddrOfPinnedArrayElement(imageGreenBuffer, 0),
                Marshal.UnsafeAddrOfPinnedArrayElement(imageBlueBuffer, 0));
        }
        return imageObj;
    }
    catch (Exception ex)
    {
        throw new Exception(ex.Message);
    }
}
```

**注意事项 / 坑**：`GenImage3` 的 R/G/B 指针用 `UnsafeAddrOfPinnedArrayElement`——三个 buffer 必须 pin 住（GC 不能移动），否则崩溃；`image.ImageData` 为 `IntPtr`，单通道直接喂 `GenImage1`。

#### 3.5.6 Halcon 图像与脚本图像（ImageData）互转

```csharp
public static ImageData HalconImageToImageData(HObject hImageObj)
{
    try
    {
        ImageData imageData = new ImageData();
        HTuple imageWidth = 0;
        HTuple imageHeight = 0;
        HTuple objClass = hImageObj.GetObjClass();
        if (objClass.S.Equals("image"))
        {
            HTuple imageType;
            HOperatorSet.GetImageType(hImageObj, out imageType);
            if (imageType.S.Equals("byte"))
            {
                //获取图像通道数
                HTuple channels = 0;
                HOperatorSet.CountChannels(hImageObj, out channels);
                //如果是单通道
                if (channels.I == 1)
                {
                    HTuple imagePointer;
                    HOperatorSet.GetImagePointer1(hImageObj, out imagePointer, out imageType, out imageWidth, out imageHeight);
                    imageData.Width = imageWidth.I;
                    imageData.Heigth = imageHeight.I;
                    imageData.PixelFormat = ImagePixelFormate.MONO8;
                    imageData.Buffer = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(imagePointer, imageData.Buffer, 0, imageWidth.I * imageHeight.I);
                }
                //如果是三通道
                else if (channels.I == 3)
                {
                    HTuple redChannel;
                    HTuple greenChannel;
                    HTuple blueChannel;
                    HOperatorSet.GetImagePointer3(hImageObj, out redChannel, out greenChannel, out blueChannel, out imageType, out imageWidth, out imageHeight);
                    imageData.Width = imageWidth.I;
                    imageData.Heigth = imageHeight.I;
                    imageData.PixelFormat = ImagePixelFormate.RGB24;
                    imageData.Buffer = new byte[imageWidth.I * imageHeight.I * 3];
                    byte[] imageRedBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageGreenBuffer = new byte[imageWidth.I * imageHeight.I];
                    byte[] imageBlueBuffer = new byte[imageWidth.I * imageHeight.I];
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, imageRedBuffer.Length);
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer, 0, imageGreenBuffer.Length);
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, imageBlueBuffer.Length);
                    for (int row = 0; row < imageHeight.I; row++)
                    {
                        for (int col = 0, index = 0; col < imageWidth.I; col++, index += 3)
                        {
                            imageData.Buffer[index] = imageRedBuffer[row * imageWidth + col];
                            imageData.Buffer[index + 1] = imageGreenBuffer[row * imageWidth + col];
                            imageData.Buffer[index + 2] = imageBlueBuffer[row * imageWidth + col];
                        }
                    }
                }
                else
                {
                    hImageObj?.Dispose();
                    throw new Exception("不支持单通道，三通道以外的图像");
                }
            }
            else
            {
                hImageObj?.Dispose();
                throw new Exception("不支持8bit 以外的位深度图像");
            }
        }
        else
        {
            hImageObj?.Dispose();
            throw new Exception("HObject 非图像类型对象");
        }
        return imageData;
    }
    catch (Exception ex)
    {
        hImageObj?.Dispose();
        throw new Exception(ex.Message);
    }
}
```

```csharp
public static HObject ImageDataToHalconImage(ImageData image)
{
    IntPtr imagePointer = IntPtr.Zero;
    IntPtr redChannel = IntPtr.Zero;
    IntPtr greenChannel = IntPtr.Zero;
    IntPtr blueChannel = IntPtr.Zero;
    try
    {
        HObject imageObj = new HObject();
        HTuple width = image.Width;
        HTuple height = image.Heigth;
        if (image.PixelFormat == ImagePixelFormate.MONO8)
        {
            imagePointer = Marshal.AllocHGlobal(image.Buffer.Length);
            Marshal.Copy(image.Buffer, 0, imagePointer, image.Buffer.Length);
            HOperatorSet.GenImage1(out imageObj, "byte", width, height, imagePointer);
        }
        else if (image.PixelFormat == ImagePixelFormate.RGB24)
        {
            byte[] imageRedBuffer = new byte[image.Buffer.Length / 3];
            byte[] imageGreBuffer = new byte[image.Buffer.Length / 3];
            byte[] imageBluBuffer = new byte[image.Buffer.Length / 3];
            int index = 0;
            for (int i = 0; i < image.Buffer.Length; index++, i += 3)
            {
                imageRedBuffer[index] = image.Buffer[i];
                imageGreBuffer[index] = image.Buffer[i + 1];
                imageBluBuffer[index] = image.Buffer[i + 2];
            }
            redChannel = Marshal.AllocHGlobal(imageRedBuffer.Length);
            greenChannel = Marshal.AllocHGlobal(imageGreBuffer.Length);
            blueChannel = Marshal.AllocHGlobal(imageBluBuffer.Length);
            Marshal.Copy(imageRedBuffer, 0, redChannel, imageRedBuffer.Length);
            Marshal.Copy(imageGreBuffer, 0, greenChannel, imageGreBuffer.Length);
            Marshal.Copy(imageBluBuffer, 0, blueChannel, imageBluBuffer.Length);
            HOperatorSet.GenImage3(out imageObj, "byte", width, height, redChannel, greenChannel, blueChannel);
        }
        return imageObj;
    }
    catch (Exception ex)
    {
        Marshal.FreeHGlobal(imagePointer);
        Marshal.FreeHGlobal(redChannel);
        Marshal.FreeHGlobal(greenChannel);
        Marshal.FreeHGlobal(blueChannel);
        throw new Exception(ex.Message);
    }
}
```

**注意事项 / 坑**：脚本图 RGB24 已是 RGB 顺序，转 Halcon 时按 R/G/B 分块；`AllocHGlobal` 的指针需在异常分支 `FreeHGlobal`（正常路径下 Halcon `GenImage1/3` 已深拷贝，官方示例未在正常路径释放，注意确认 SDK 版本是否自动回收）。

**问题根因**：不熟悉 Halcon 图像转换为其它类型。

---

### 3.6 流程图像与算子图像互转

**适用场景**：VM SDK 流程图像 `ImageBaseData_V2` ↔ 算子 SDK 算子图像 `CMvdImage`。

**关键类型 / 类名**：`ImageBaseData_V2`、`CMvdImage`、`MVD_IMAGE_DATA_INFO`、`MVD_PIXEL_FORMAT`、`VMPixelFormat`。

#### 3.6.1 流程图像转算子图像

```csharp
public CMvdImage ImageBaseData_V2ToCMvdImage(ImageBaseData_V2 ImageBaseDataV2)
{
    VisionDesigner.CMvdImage cmvdImage = new VisionDesigner.CMvdImage();
    VisionDesigner.MVD_IMAGE_DATA_INFO stImageData = new VisionDesigner.MVD_IMAGE_DATA_INFO();

    if (VMPixelFormat.VM_PIXEL_MONO_08 == ImageBaseDataV2.Pixelformat)
    {
        stImageData.stDataChannel[0].nRowStep = (uint)ImageBaseDataV2.Width;
        stImageData.stDataChannel[0].nLen = (uint)(ImageBaseDataV2.Width * ImageBaseDataV2.Height);
        stImageData.stDataChannel[0].nSize = (uint)(ImageBaseDataV2.Width * ImageBaseDataV2.Height);
        byte[] m_BufForDriver1 = new byte[ImageBaseDataV2.Width * ImageBaseDataV2.Height];
        //数据Copy
        Marshal.Copy(ImageBaseDataV2.ImageData, m_BufForDriver1, 0, ((int)ImageBaseDataV2.Width * ImageBaseDataV2.Height));
        stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver1;
        //初始化CMvdImage
        cmvdImage.InitImage((uint)ImageBaseDataV2.Width, (uint)ImageBaseDataV2.Height, MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08, stImageData);
    }
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == ImageBaseDataV2.Pixelformat)
    {
        stImageData.stDataChannel[0].nRowStep = (uint)ImageBaseDataV2.Width * 3;
        stImageData.stDataChannel[0].nLen = (uint)(ImageBaseDataV2.Width * ImageBaseDataV2.Height * 3);
        stImageData.stDataChannel[0].nSize = (uint)(ImageBaseDataV2.Width * ImageBaseDataV2.Height * 3);
        byte[] m_BufForDriver1 = new byte[3 * (ImageBaseDataV2.Width * ImageBaseDataV2.Height)];
        //数据Copy
        Marshal.Copy(ImageBaseDataV2.ImageData, m_BufForDriver1, 0, ((int)(ImageBaseDataV2.Width * ImageBaseDataV2.Height) * 3));
        stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver1;
        //初始化CMvdImage
        cmvdImage.InitImage((uint)ImageBaseDataV2.Width, (uint)ImageBaseDataV2.Height, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3, stImageData);
    }
    return cmvdImage;
}
```

#### 3.6.2 算子图像转流程图像

```csharp
public ImageBaseData_V2 CMvdImageToImageBaseData_V2(CMvdImage cmvdImage)
{
    VM.PlatformSDKCS.ImageBaseData_V2 ImageBaseDataV2 = null;
    if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == cmvdImage.PixelFormat)
    {
        var cmvdImageData = cmvdImage.GetImageData();
        IntPtr imagedata = Marshal.AllocHGlobal(cmvdImageData.stDataChannel[0].arrDataBytes.Length);
        Marshal.Copy(cmvdImageData.stDataChannel[0].arrDataBytes, 0, imagedata, cmvdImageData.stDataChannel[0].arrDataBytes.Length);
        ImageBaseDataV2 = new ImageBaseData_V2(imagedata, (uint)cmvdImageData.stDataChannel[0].arrDataBytes.Length, (int)cmvdImage.Width, (int)cmvdImage.Height, VMPixelFormat.VM_PIXEL_MONO_08);

        //使用结束后需要手动释放
        //Marshal.FreeHGlobal(imagedata);
        //imagedata = IntPtr.Zero;
    }
    else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == cmvdImage.PixelFormat)
    {

        var cmvdImageData = cmvdImage.GetImageData();
        IntPtr imagedata = Marshal.AllocHGlobal(cmvdImageData.stDataChannel[0].arrDataBytes.Length);
        Marshal.Copy(cmvdImageData.stDataChannel[0].arrDataBytes, 0, imagedata, cmvdImageData.stDataChannel[0].arrDataBytes.Length);
        ImageBaseDataV2 = new ImageBaseData_V2(imagedata, (uint)cmvdImageData.stDataChannel[0].arrDataBytes.Length, (int)cmvdImage.Width, (int)cmvdImage.Height, VMPixelFormat.VM_PIXEL_RGB24_C3);
        //使用结束后需要手动释放
        //Marshal.FreeHGlobal(imagedata);
        //imagedata = IntPtr.Zero;
    }
    return ImageBaseDataV2;
}
```

**注意事项 / 坑**：`ImageBaseData_V2(IntPtr)` 浅拷贝，算子图转流程图用 `AllocHGlobal` 后必须 `FreeHGlobal`；两个方向像素格式一致（均为 RGB），无需交换通道。

**问题根因**：不熟悉流程图像与算子图像互转。

---

# C++ 篇

## 命名空间与引用（原文出现的命名空间，非编造）

- `VisionMasterSDK::MvdPixelFormat` —— `MVD_PIXEL_MONO_08` / `MVD_PIXEL_RGB_RGB24_C3`；类型 `IoImage` / `ImageBaseData`
- `VisionDesigner::_MVD_PIXEL_FORMAT_` —— `MVD_PIXEL_MONO_08` / `MVD_PIXEL_BGR_BGR24_C3`；类型 `IMvdImage` / `MVD_IMAGE_DATA_INFO`（`stDataChannel[0].pData` / `nRowStep` / `nLen` / `nSize`）
- `MvCameraControl` —— `MV_FRAME_OUT` / `PixelType_Gvsp_Mono8` / `PixelType_Gvsp_RGB8_Packed`
- `HalconCpp` —— `HImage` / `Hobject` / `HString` / `Hlong` / `Herror`；`get_image_pointer1` / `get_image_pointer3` / `gen_image1` / `gen_image3` / `count_channels`
- `cv`（`OpenCV`）—— `cv::Mat` / `CV_8UC1` / `CV_8UC3` / `cv::cvtColor` / `CV_BGR2RGB` / `CV_RGB2BGR`
- `Qt` —— `QImage`（`Format_Indexed8` / `Format_RGB888` / `Format_Grayscale8` / `constBits()`）
- 算法模块 —— `HKA_IMAGE`（`format` / `width` / `height` / `step[0]` / `data[0]`；`HKA_IMG_MONO_08` / `HKA_IMG_RGB_RGB24_C3`）、`CreateImageInstance`（创建 `IMvdImage*`）、`IMVDException` / `MVD_MODUL_APP` / `MVD_E_*`

---

### 3.7 图像转换扫盲篇（C++）

**适用场景**：了解 C++ 侧各开发形态下"图像"类型，建立转换全景。

**关键类型 / 类名**：`MV_FRAME_OUT`、`IMvdImage`、`ImageData`（C# 脚本类型）、`IoImage`、`ImageBaseData`、`IMvdImage`、`HKA_IMAGE`。

**图像格式一览**（原文转录）：

- 相机：图像数据流类型 `MyCamera.MV_FRAME_OUT`（来自 `MvCameraControl.Net.dll`，即海康机器人工业相机 SDK，在 MVS SDK 和算子 SDK 中都有这个 dll；算子 SDK 的 `MVDCamera.Net.dll` 也可以取流，它是对 `MvCameraControl.Net.dll` 的二次封装，用 `MVDCamera.Net.dll` 时图像数据流类型是 `IMvdImage`）。
- VM：脚本输入图像，类型是 `ImageData`（C# 中图像类型）。
- VM SDK：
  - 流程输入图像 `IoImage`
  - Group 输入图像 `IoImage`
  - 图像源 SDK 输入图像 `ImageBaseData`
  - 模块输入图像 `ImageBaseData`
- 算子 SDK：输入图像 `IMvdImage`
- 算法模块：输入图像 `HKA_IMAGE`

**转换说明**：三通道的 Mat 为 **BGR**，三通道 QImage、VM 和二次开发为 **RGB**。常用转换见 3.8 ~ 3.13。

**注意事项 / 坑**：C++ 算子图像像素格式枚举用 `MVD_PIXEL_BGR_BGR24_C3`（BGR），而 VM 图像用 `MVD_PIXEL_RGB_RGB24_C3`（RGB），与 C# 习惯不同，注意核对 SDK 版本。

---

### 3.8 相机采图转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入图像

**适用场景**：`MV_FRAME_OUT` → 流程输入 `IoImage` / Group 输入 `IoImage` / 图像源 SDK `ImageBaseData` / 模块输入 `ImageBaseData` / 算子输入 `IMvdImage`。

**关键类型 / 类名**：`MV_FRAME_OUT`、`PixelType_Gvsp_Mono8` / `PixelType_Gvsp_RGB8_Packed`、`IoImage`、`ImageBaseData`、`IMvdImage`、`MVD_IMAGE_DATA_INFO`、`MvdPixelFormat`、`VisionDesigner::_MVD_PIXEL_FORMAT_`（`MVD_PIXEL_MONO_08` / `MVD_PIXEL_RGB_RGB24_C3` / `MVD_PIXEL_BGR_BGR24_C3`）。

#### 3.8.1 相机采图转流程输入（IoImage）、Group 输入（IoImage）

```cpp
IoImage MV_FRAME_OUTToProcedureIoImage(MV_FRAME_OUT stImageInfo)
{

// TODO: 在此处添加实现代码.

IoImage ioImage{};

unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,控制释放时机防止内存泄漏，写在此处为了方便参考

m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned char) * stImageInfo.stFrameInfo.nFrameLen);

memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInfo.stFrameInfo.nFrameLen);


ioImage.stImage.Width = stImageInfo.stFrameInfo.nWidth;

ioImage.stImage.Height = stImageInfo.stFrameInfo.nHeight;

ioImage.stImage.DataLen = stImageInfo.stFrameInfo.nFrameLen;

ioImage.stImage.ImageData = m_pSaveImageBuf;

if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_Mono8)
{

    ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_PIXEL_MONO_08;

}
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_RGB8_Packed)
{

    ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3;

}

return ioImage;
}
```

#### 3.8.2 相机采图转图像源 SDK 输入（ImageBaseData）、模块输入（ImageBaseData）

```cpp
ImageBaseData MV_FRAME_OUTToImageBaseData(MV_FRAME_OUT stImageInfo)
{

// TODO: 在此处添加实现代码.

ImageBaseData imageBaseData{};

unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,控制释放时机防止内存泄漏，写在此处为了方便参考

m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned char) * stImageInfo.stFrameInfo.nFrameLen);

memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInfo.stFrameInfo.nFrameLen);


imageBaseData.Width = stImageInfo.stFrameInfo.nWidth;

imageBaseData.Height = stImageInfo.stFrameInfo.nHeight;

imageBaseData.DataLen = stImageInfo.stFrameInfo.nFrameLen;

imageBaseData.ImageData = m_pSaveImageBuf;

if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_Mono8)
{

    imageBaseData.Pixelformat = MvdPixelFormat::MVD_PIXEL_MONO_08;

}
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_RGB8_Packed)
{

    imageBaseData.Pixelformat = MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3;

}

return imageBaseData;
}
```

#### 3.8.3 相机采图转算子输入（IMvdImage）

```cpp
IMvdImage* MV_FRAME_OUTToIMvdImage(MV_FRAME_OUT stImageInfo)
{

// TODO: 在此处添加实现代码.

IMvdImage* iMvdImage = NULL;

unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,控制释放时机防止内存泄漏，写在此处为了方便参考

m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned char) * stImageInfo.stFrameInfo.nFrameLen);

memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInfo.stFrameInfo.nFrameLen);

MVD_IMAGE_DATA_INFO stImageData{ };


if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_Mono8)
{


    stImageData.stDataChannel[0].nRowStep = stImageInfo.stFrameInfo.nWidth;


    stImageData.stDataChannel[0].nLen = stImageInfo.stFrameInfo.nFrameLen;


    stImageData.stDataChannel[0].nSize = stImageInfo.stFrameInfo.nFrameLen;


    stImageData.stDataChannel[0].pData = m_pSaveImageBuf;

    iMvdImage->InitImage(stImageInfo.stFrameInfo.nWidth, stImageInfo.stFrameInfo.nHeight, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_MONO_08, stImageData);

}
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_RGB8_Packed)
{


    stImageData.stDataChannel[0].nRowStep = stImageInfo.stFrameInfo.nWidth*3;


    stImageData.stDataChannel[0].nLen = stImageInfo.stFrameInfo.nFrameLen;


    stImageData.stDataChannel[0].nSize = stImageInfo.stFrameInfo.nFrameLen;


    stImageData.stDataChannel[0].pData = m_pSaveImageBuf;

    iMvdImage->InitImage(stImageInfo.stFrameInfo.nWidth, stImageInfo.stFrameInfo.nHeight, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_BGR_BGR24_C3, stImageData);

}

return iMvdImage;
}
```

**注意事项 / 坑**：
- `m_pSaveImageBuf` 用 `malloc` 分配，需在使用完后 `free`，否则内存泄漏；官方注释建议放在头文件声明以管控释放时机。
- 3.8.3 中 `iMvdImage` 必须先通过 `CreateImageInstance(&iMvdImage)`（见 3.9.3 / 3.13.3）创建后再 `InitImage`，原文 `IMvdImage* iMvdImage = NULL;` 后直接 `->InitImage` 为示例片段，实际调用前务必先创建实例。
- C++ 算子图像 RGB 用 `MVD_PIXEL_BGR_BGR24_C3`，与 VM 图像（`MVD_PIXEL_RGB_RGB24_C3`）不同。

**问题根因**：不熟悉相机采图转换为其它类型。

---

### 3.9 QImage 转流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、流程输出图像

**适用场景**：`QImage` → 流程输入 `IoImage` / Group 输入 `IoImage` / 图像源 SDK `ImageBaseData` / 模块输入 `ImageBaseData` / 算子输入 `IMvdImage`；流程输出 `IoImage` → `QImage`。

**关键类型 / 类名**：`QImage`（`Format_Indexed8` / `Format_RGB888` / `Format_Grayscale8` / `constBits()`）、`IoImage`、`ImageBaseData`、`IMvdImage`、`MVD_IMAGE_DATA_INFO`、`_MvdPixelFormat_`（`MVD_PIXEL_MONO_08` / `MVD_PIXEL_RGB_RGB24_C3`）、`MVD_PIXEL_FORMAT`。

#### 3.9.1 QImage 转流程输入（IoImage）、Group 输入（IoImage）

```cpp
IoImage QImageToIoImage(QImage qImage)
{
    QString strReMsg = "";
    IoImage ioImage;
    switch (qImage.format())
    {
    case QImage::Format_Indexed8:
        ioImage.stImage.Width=qImage.width();
        ioImage.stImage.Height=qImage.height();
        ioImage.stImage.DataLen=qImage.sizeInBytes();
        ioImage.stImage.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_MONO_08;
        ioImage.stImage.ImageData=(void *)qImage.constBits();
        //ioImage.stImage.ImageData=qImage.data_ptr();
        //QImage(ioImage.stImage.ImageData,ioImage.stImage.Width,ioImage.stImage.Width,QImage::Format_RGB888);
        break;
    case QImage::Format_RGB888:
        ioImage.stImage.Width=qImage.width();
        ioImage.stImage.Height=qImage.height();
        ioImage.stImage.DataLen=qImage.sizeInBytes();
        ioImage.stImage.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_RGB_RGB24_C3;
        ioImage.stImage.ImageData=(void *)qImage.constBits();
        break;
    }
    strReMsg = "QImageToIoImage s uccess.";
    ui->textEdit->append(strReMsg);
    return ioImage;
}
```

#### 3.9.2 QImage 转图像源 SDK 输入（ImageBaseData）、模块输入（ImageBaseData）

```cpp
ImageBaseData QImageToImageBaseData(QImage qImage)
{
    ImageBaseData  imageBaseData;
    switch (qImage.format())
    {
    case QImage::Format_Indexed8:
        imageBaseData.Width=qImage.width();
        imageBaseData.Height=qImage.height();
        imageBaseData.DataLen=qImage.sizeInBytes();
        imageBaseData.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_MONO_08;
        imageBaseData.ImageData=(void *)qImage.constBits();
        //ioImage.stImage.ImageData=qImage.data_ptr();
        break;
    case QImage::Format_RGB888:
        imageBaseData.Width=qImage.width();
        imageBaseData.Height=qImage.height();
        imageBaseData.DataLen=qImage.sizeInBytes();
        imageBaseData.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_RGB_RGB24_C3;
        imageBaseData.ImageData=(void *)qImage.constBits();
        break;
    }
    return imageBaseData;
}
```

#### 3.9.3 QImage 与算子图像（IMvdImage）互转

```cpp
IMvdImage* QImageToIMvdImage(QImage qImage)
{
    IMvdImage* iMvdImage;
    CreateImageInstance(&iMvdImage);
    MVD_IMAGE_DATA_INFO stImageData;
    switch (qImage.format())
    {
    case QImage::Format_Indexed8:
        stImageData.stDataChannel[0].nRowStep = qImage.width();
        stImageData.stDataChannel[0].nLen = qImage.sizeInBytes();
        stImageData.stDataChannel[0].nSize = qImage.sizeInBytes();
        stImageData.stDataChannel[0].pData = (unsigned char*)qImage.constBits();
        iMvdImage->InitImage(qImage.width(), qImage.height(),MVD_PIXEL_FORMAT::MVD_PIXEL_MONO_08, stImageData);
        break;
    case QImage::Format_RGB888:
        stImageData.stDataChannel[0].nRowStep = qImage.width()*3;
        stImageData.stDataChannel[0].nLen = qImage.sizeInBytes();
        stImageData.stDataChannel[0].nSize = qImage.sizeInBytes();
        stImageData.stDataChannel[0].pData = (unsigned char*)qImage.constBits();
        iMvdImage->InitImage(qImage.width(), qImage.height(),MVD_PIXEL_FORMAT::MVD_PIXEL_RGB_RGB24_C3, stImageData);
        break;
    }
    return iMvdImage;
}

//算子转QImage
QImage IMvdImageToQImage(IMvdImage * iMvdImage)
{
    if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PIXEL_MONO_08)
    {
        //QImage qImage((const uchar*)iMvdImage->GetImageData(0)->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),iMvdImage->GetImageData(0)->nLen/iMvdImage->GetHeight(),QImage::Format_Indexed8);
        //QImage qImage(iMvdImage->GetImageData(0)->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),iMvdImage->GetImageData(0)->nLen/iMvdImage->GetHeight(),QImage::Format_Indexed8);
        QImage qImage((const uchar*)iMvdImage->GetImageData(0)->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),QImage::Format_Grayscale8);//Format_Indexed8
        return qImage;
    }
    if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PIXEL_RGB_RGB24_C3)
    {
        QImage qImage((const uchar*)iMvdImage->GetImageData(0)->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),QImage::Format_RGB888);
        return qImage;
    }
}
```

**注意事项 / 坑**：`qImage.constBits()` 返回 `const` 指针，直接赋给 `ImageData` 属浅引用，QImage 释放后悬空；算子图转 QImage 同样用 `GetImageData(0)->pData` 浅引用，注意生命周期。`CreateImageInstance` 创建 `IMvdImage*` 后需对应释放接口释放。

#### 3.9.4 流程输出（IoImage）转 QImage

```cpp
QImage IoImageToQImage(IoImage inIoImage)
{
    if (inIoImage.stImage.Pixelformat == _MvdPixelFormat_::MVD_PIXEL_MONO_08)
    {
        QImage qImage((const uchar*)inIoImage.stImage.ImageData,inIoImage.stImage.Width,inIoImage.stImage.Height,QImage::Format_Grayscale8);
        return qImage;
    }
    if (inIoImage.stImage.Pixelformat == _MvdPixelFormat_::MVD_PIXEL_RGB_RGB24_C3)
    {
        QImage qImage((const uchar*)inIoImage.stImage.ImageData,inIoImage.stImage.Width,inIoImage.stImage.Height,QImage::Format_RGB888);
        return qImage;
    }
}
```

**注意事项 / 坑**：QImage（RGB888）与 VM 图像（RGB）一致，无需交换通道；`Format_Grayscale8` 用于 8bit 灰度。

**问题根因**：不熟悉 QImage 转换为其它类型。

---

### 3.10 Mat 与流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、算子输出、流程输出

**适用场景**：`cv::Mat` → 流程输入 `IoImage` / Group 输入 `IoImage` / 图像源 SDK `ImageBaseData` / 模块输入 `ImageBaseData` / 算子输入 `IMvdImage`；算子输出 → Mat；流程输出 `IoImage` → Mat。

**关键类型 / 类名**：`cv::Mat`、`CV_8UC1` / `CV_8UC3`、`cv::cvtColor`、`CV_BGR2RGB` / `CV_RGB2BGR`、`IoImage`、`ImageBaseData`、`IMvdImage`、`_MvdPixelFormat_`、`MVD_PIXEL_FORMAT`、`IMVDException`、`CVmException`、`MVD_MODUL_APP`、`MVD_E_*`。

#### 3.10.1 Mat 转流程输入（IoImage）、Group 输入（IoImage）

```cpp
IoImage MatToProcedureInputImage(Mat matInputImg)
{

if (matInputImg.empty())
{

    throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);

}

if ((CV_8UC1 != matInputImg.type()) && (CV_8UC3 != matInputImg.type()))
{

    throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);

}

IoImage  m_pIoImage{};

uint dataLen = (uint)(matInputImg.cols * matInputImg.rows * matInputImg.channels());

CString strReMsg = _T("");

try
{

    if (CV_8UC1 == matInputImg.type())
    {

        m_pIoImage.stImage.Width = matInputImg.cols;

        m_pIoImage.stImage.Height = matInputImg.rows;

        m_pIoImage.stImage.DataLen = dataLen;

        m_pIoImage.stImage.Pixelformat = _MvdPixelFormat_::MVD_PIXEL_MONO_08;

        m_pIoImage.stImage.ImageData = matInputImg.ptr(0);

    }

    else if (CV_8UC3 == matInputImg.type())
    {

        cv::cvtColor(matInputImg, matInputImg, CV_BGR2RGB);

        m_pIoImage.stImage.Width = matInputImg.cols;

        m_pIoImage.stImage.Height = matInputImg.rows;

        m_pIoImage.stImage.DataLen = dataLen;

        m_pIoImage.stImage.Pixelformat = _MvdPixelFormat_::MVD_PIXEL_RGB_RGB24_C3;

        m_pIoImage.stImage.ImageData = matInputImg.ptr(0);

    }

}
catch (CVmException e)
{

    strReMsg.Format(_T("%x"), e.GetErrorCode());

    strReMsg = _T("0x") + strReMsg + _T(" == SaveProcedureToFile()");

}

return m_pIoImage;
}
```

**注意事项 / 坑**：彩色 `cv::cvtColor(matInputImg, matInputImg, CV_BGR2RGB)` 就地转成 RGB；`ImageData = matInputImg.ptr(0)` 浅引用 Mat 缓冲，Mat 释放后悬空。

#### 3.10.2 Mat 转图像源 SDK 输入（ImageBaseData）、模块输出（ImageBaseData）

```cpp
ImageBaseData MatToImageBaseData(Mat matInputImg)
{

if (matInputImg.empty())
{

    throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);

}

if ((CV_8UC1 != matInputImg.type()) && (CV_8UC3 != matInputImg.type()))
{

    throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);

}

ImageBaseData  m_pImageBaseData{};

uint dataLen = (uint)(matInputImg.cols * matInputImg.rows * matInputImg.channels());

CString strReMsg = _T("");

try
{

    if (CV_8UC1 == matInputImg.type())
    {

        m_pImageBaseData.Width = matInputImg.cols;

        m_pImageBaseData.Height = matInputImg.rows;

        m_pImageBaseData.DataLen = dataLen;

        m_pImageBaseData.Pixelformat = _MvdPixelFormat_::MVD_PIXEL_MONO_08;

        m_pImageBaseData.ImageData = matInputImg.ptr(0);

    }

    else if (CV_8UC3 == matInputImg.type())
    {

        cv::cvtColor(matInputImg, matInputImg, CV_BGR2RGB);

        m_pImageBaseData.Width = matInputImg.cols;

        m_pImageBaseData.Height = matInputImg.rows;

        m_pImageBaseData.DataLen = dataLen;

        m_pImageBaseData.Pixelformat = _MvdPixelFormat_::MVD_PIXEL_RGB_RGB24_C3;

        m_pImageBaseData.ImageData = matInputImg.ptr(0);

    }

}
catch (CVmException e)
{

    strReMsg.Format(_T("%x"), e.GetErrorCode());

    strReMsg = _T("0x") + strReMsg + _T(" == SaveProcedureToFile()");

}

return m_pImageBaseData;
}
```

#### 3.10.3 Mat 与算子图像（IMvdImage）互转

```cpp
void ConvertMat2MvdImage(IN Mat& stMatImg, INOUT IMvdImage* pMvdImg)
{
    // 参数合法性判断
    if (stMatImg.empty() || NULL == pMvdImg)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);
    }

    // 像素格式判断
    if ((CV_8UC1 != stMatImg.type()) && (CV_8UC3 != stMatImg.type()))
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);
    }

    int nImageWidth = stMatImg.size().width;
    int nImageHeight = stMatImg.size().height;
    int nChannelNum = stMatImg.channels();
    int nImageSize = stMatImg.size().width * stMatImg.size().height * nChannelNum;

    // 根据传入的mat 图像初始化ImvdImage
    if (CV_8UC1 == stMatImg.type())
    {
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXEL_MONO_08);
    }
    else if (CV_8UC3 == stMatImg.type())
    {
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXEL_RGB_RGB24_C3);
    }

    unsigned char* pszMvdImgData = pMvdImg->GetImageData(0)->pData;
    if (stMatImg.isContinuous()) //  灰度图一定连续，彩色图不一定
    {
        uchar* pdata = stMatImg.ptr<uchar>(0);
        memcpy(pszMvdImgData, pdata, nImageSize);
    }
    else // 避免彩色图有裁剪等操作导致图像数据不连续问题
    {
        for (int i = 0; i < nImageHeight; i++)    // 逐行拷贝
        {
            uchar* pdata = stMatImg.ptr<uchar>(i);
            memcpy(&pszMvdImgData[i * nImageWidth * nChannelNum], pdata, nImageWidth * nChannelNum);
        }
    }

    if (MVD_PIXEL_RGB_RGB24_C3 == pMvdImg->GetPixelFormat()) // 交换R 和B
    {
        uchar cTemp;
        for (int i = 0; i < nImageWidth * nImageHeight; i++)
        {
            cTemp = pszMvdImgData[3 * i];
            pszMvdImgData[3 * i] = pszMvdImgData[3 * i + 2];
            pszMvdImgData[3 * i + 2] = cTemp;
        }
    }
}
```

```cpp
void ConvertMvdImage2Mat(IN IMvdImage* pMvdImg, INOUT Mat* pMatImg)
{
    // 参数合法性判断
    if (NULL == pMvdImg || NULL == pMatImg)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);
    }

    // 像素格式判断
    MVD_PIXEL_FORMAT enSrcPixelFormat = pMvdImg->GetPixelFormat();
    if ((MVD_PIXEL_MONO_08 != enSrcPixelFormat) && (MVD_PIXEL_RGB_RGB24_C3 != enSrcPixelFormat))
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);
    }

    int nImageWidth = pMvdImg->GetWidth();
    int nImageHeight = pMvdImg->GetHeight();

    // 根据传入的ImvdImage 图像初始化mat
    if (MVD_PIXEL_MONO_08 == enSrcPixelFormat)
    {
        pMatImg->create(nImageHeight, nImageWidth, CV_8UC1);
    }
    if (MVD_PIXEL_RGB_RGB24_C3 == enSrcPixelFormat)
    {
        pMatImg->create(nImageHeight, nImageWidth, CV_8UC3);
    }

    if (pMatImg->empty())
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE);
    }

    // 上述方式为mat 分配的内存一定是连续的
    uchar* pdata = pMatImg->ptr<uchar>(0);
    memcpy(pdata, pMvdImg->GetImageData(0)->pData, pMvdImg->GetImageData(0)->nLen);
    if (CV_8UC3 == pMatImg->type()) // 交换R 和B
    {
        uchar cTemp;
        for (int i = 0; i < nImageWidth * nImageHeight; i++)
        {
            cTemp = pdata[3 * i];
            pdata[3 * i] = pdata[3 * i + 2];
            pdata[3 * i + 2] = cTemp;
        }
    }
}
```

#### 3.10.4 流程输出（IoImage）转 Mat

```cpp
Mat IoImageToMat(IoImage m_pIoImage)
{

Mat stMatImg;

CString strReMsg = _T("");

try
{

    MvdPixelFormat srcPixelFormat = m_pIoImage.stImage.Pixelformat;

    if ((VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_MONO_08 != srcPixelFormat) && (VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3 != srcPixelFormat))
    {

        throw CVmException(0xE0000503);

    }

    // 根据传入的IoImage 图像初始化mat
    if (VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_MONO_08 == srcPixelFormat)
    {

        stMatImg.create((int)m_pIoImage.stImage.Height, (int)m_pIoImage.stImage.Width, CV_8UC1);

    }
    else if (VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3 == srcPixelFormat)
    {

        stMatImg.create((int)m_pIoImage.stImage.Height, (int)m_pIoImage.stImage.Width, CV_8UC3);

    }

    if (stMatImg.empty())
    {

        throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE);

    }

    // 上述方式为mat 分配的内存一定是连续的
    uchar* pdata = stMatImg.ptr<uchar>(0);
    memcpy(pdata, m_pIoImage.stImage.ImageData, m_pIoImage.stImage.DataLen);

    if (CV_8UC3 == stMatImg.type())
    {

        cvtColor(stMatImg, stMatImg, CV_RGB2BGR);

    }

}
catch (CVmException e)
{

    strReMsg.Format(_T("%x"), e.GetErrorCode());

    strReMsg = _T("0x") + strReMsg + _T(" == SaveProcedureToFile()");

}

return stMatImg;
}
```

**注意事项 / 坑**：
- Mat 连续性问题：`isContinuous()` 判断后统一 `memcpy`，彩色裁剪后可能不连续，需逐行拷贝。
- 通道顺序：Mat 侧统一用 `cv::cvtColor` + `CV_BGR2RGB`（Mat→VM）和 `CV_RGB2BGR`（VM→Mat）交换。
- `IoImageToMat` 中用了 `throw CVmException(0xE0000503)` 作为不支持格式的异常（原文直接硬编码错误码）。

**问题根因**：不熟悉 Mat 转换为其它类型。

---

### 3.11 Halcon 与流程输入、Group 输入、图像源 SDK 输入、模块输入、算子输入、算子输出、流程输出

**适用场景**：`HalconCpp::HImage` → 流程输入 `IoImage` / Group 输入 `IoImage` / 图像源 SDK `ImageBaseData` / 模块输入 `ImageBaseData` / 算子输入 `IMvdImage`；算子输出 → Halcon；流程输出 `IoImage` → Halcon。

**关键类型 / 类名**：`HImage`、`Hobject`、`HString`、`Hlong`、`Herror`、`count_channels`、`get_image_pointer1` / `get_image_pointer3`、`gen_image1` / `gen_image3`、`IoImage`、`ImageBaseData`、`IMvdImage`、`MvdPixelFormat`、`MVD_PIXEL_FORMAT`、`IMVDException`、`MVD_MODUL_APP`、`MVD_E_*`。

#### 3.11.1 Halcon 图像转流程输入（IoImage）、Group 输入（IoImage）

```cpp
// Halcon 图像转流程输入（IoImage）、Group 输入（IoImage）,HImageToImageBaseData 函数的实现见“2 Halcon 图像转ImageBaseData“
IoImage HImageToIoImage(HImage image)
{

IoImage ioImage{};

ImageBaseData imageBaseData = HImageToImageBaseData(image);

ioImage.stImage = imageBaseData;

return ioImage;
}
```

#### 3.11.2 Halcon 图像转图像源 SDK 输入（ImageBaseData）、模块输入（ImageBaseData）

```cpp
ImageBaseData HImageToImageBaseData(HImage image)
{

ImageBaseData imageBaseData{};

// 获取图像通道位深度信息
HString bitdepth = image.GetChannelInfo("type", 1);
assert(!strcmp(bitdepth.Text(), "byte"));

int channels = image.CountChannels();
assert(channels == 1 || channels == 3);

HString type;
Hlong width, height;

// 单通道
if (channels == 1)
{

    void* imagePtr = image.GetImagePointer1(&type, &width, &height);
    imageBaseData.DataLen = width * height;
    imageBaseData.Width = width;
    imageBaseData.Height = height;
    imageBaseData.Pixelformat = MvdPixelFormat::MVD_PIXEL_MONO_08;
    imageBaseData.ImageData = imagePtr;

}
// 3 通道
if (channels == 3)
{

    void* imageRedPtr;
    void* imageGreenPtr;
    void* imageBluePtr;

    image.GetImagePointer3(&imageRedPtr, &imageGreenPtr, &imageBluePtr, &type, &width, &height);

    byte* imageRedBuf = new byte[width * height];
    byte* imageGreenBuf = new byte[width * height];
    byte* imageBlueBuf = new byte[width * height];
    memcpy(imageRedBuf, imageRedPtr, width * height);
    memcpy(imageGreenBuf, imageGreenPtr, width * height);
    memcpy(imageBlueBuf, imageBluePtr, width * height);

    byte* imageBuf = new byte[width * height * 3];
    int index = 0;
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++, index += 3)
        {
            imageBuf[index] = imageRedBuf[row * width + col];
            imageBuf[index + 1] = imageGreenBuf[row * width + col];
            imageBuf[index + 2] = imageBlueBuf[row * width + col];
        }
    }

    delete[] imageRedBuf;
    delete[] imageGreenBuf;
    delete[] imageBlueBuf;

    imageBaseData.DataLen = width * height * 3;
    imageBaseData.Width = width;
    imageBaseData.Height = height;
    imageBaseData.Pixelformat = MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3;
    imageBaseData.ImageData = imageBuf;

}

return imageBaseData;
}
```

**注意事项 / 坑**：单通道 `ImageData = imagePtr` 浅引用 Halcon 图像，双通道需 `new byte[]` 拼成 RGB 并 `delete[]` 三块临时缓冲；返回的 `imageBaseData` 内 `ImageData` 在三通道时为 `new` 出的 `imageBuf`，需在使用完后 `delete[]`。

#### 3.11.3 Halcon 图像与算子图像（IMvdImage）互转

```cpp
void ConvertHalcon2MvdImage(IN Hobject stHalconImg, INOUT IMvdImage* pMvdImg)
{
    // 判断输入是否合法
    if (NULL == pMvdImg)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);
    }

    Herror stErr;
    Hlong nChannelNum;
    stErr = count_channels(stHalconImg, &nChannelNum);
    if (H_MSG_OK != stErr)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNOW, "Failed to get channel num!");
    }
    if (1 != nChannelNum && 3 != nChannelNum)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);
    }

    Hlong nImageWidth = 0;
    Hlong nImageHeight = 0;
    char szType[128] = { 0 };

    // 获取图像信息
    if (1 == nChannelNum) // 灰度图
    {
        unsigned char* pData;
        stErr = get_image_pointer1(stHalconImg, (Hlong*)&pData, szType, &nImageWidth, &nImageHeight);
        if (H_MSG_OK != stErr)
        {
            throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNOW, "Failed to get image info!");
        }
        if (strcmp("byte", szType))
        {
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT, "Image type not supported!");
        }
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXEL_MONO_08);
        unsigned char* pszMvdImgData = pMvdImg->GetImageData(0)->pData;
        memcpy(pszMvdImgData, pData, nImageWidth * nImageHeight);
    }
    else if (3 == nChannelNum) // 彩色图(注意：位深为8 的图像不一定是灰度图，也可能是伪彩图)
    {
        unsigned char* pRData;
        unsigned char* pGData;
        unsigned char* pBData;
        stErr = get_image_pointer3(stHalconImg, (Hlong*)&pRData, (Hlong*)&pGData, (Hlong*)&pBData, szType, &nImageWidth, &nImageHeight);
        if (H_MSG_OK != stErr)
        {
            throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNOW, "Failed to get image info!");
        }
        if (strcmp("byte", szType))
        {
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT, "Image type not supported!");
        }
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXEL_RGB_RGB24_C3);

        unsigned char* pszMvdImgData = pMvdImg->GetImageData(0)->pData;
        for (unsigned int i = 0; i < nImageHeight; i++)
        {
            for (unsigned int j = 0; j < nImageWidth; j++)
            {
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 0] = pRData[i * nImageWidth + j];
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 1] = pGData[i * nImageWidth + j];
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 2] = pBData[i * nImageWidth + j];
            }
        }
    }
}
```

```cpp
void ConvertMvdImage2Halcon(IN IMvdImage* pMvdImg, INOUT Hobject* pHObject)
{
    // 传参合法性判断
    if (NULL == pMvdImg || NULL == pHObject)
    {
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETER_ILLEGAL);
    }

    Herror stErr;
    unsigned char* pRData = NULL;
    unsigned char* pGData = NULL;
    unsigned char* pBData = NULL;
    try
    {
        MVD_PIXEL_FORMAT enSrcPixelFormat = pMvdImg->GetPixelFormat();
        if ((MVD_PIXEL_MONO_08 != enSrcPixelFormat) && (MVD_PIXEL_RGB_RGB24_C3 != enSrcPixelFormat))
        {
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT);
        }

        int nImageWidth = pMvdImg->GetWidth();
        int nImageHeight = pMvdImg->GetHeight();

        // 根据传入的MVDImage 图像初始化Halcon 图像
        if (MVD_PIXEL_MONO_08 == enSrcPixelFormat)
        {
            // 直接引用MVDImage 图像数据的地址，进行新建Halcon 图像;halcon 内部会对图像数据深拷贝
            stErr = gen_image1(pHObject, "byte", nImageWidth, nImageHeight, (Hlong)pMvdImg->GetImageData(0)->pData);
            if (H_MSG_OK != stErr)
            {
                throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE, "Failed to create halcon image!");
            }
        }
        else if (MVD_PIXEL_RGB_RGB24_C3 == enSrcPixelFormat)
        {
            // MVDImage 图像是一个通道RGBRGBRGB...存放；需要另外开辟块内存
            int nChannelDataLen = nImageWidth * nImageHeight;
            unsigned char* pszMvdImgData = pMvdImg->GetImageData(0)->pData;

            pRData = (unsigned char*)malloc(nChannelDataLen);
            if (NULL == pRData)
            {
                throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE, "Failed to malloc buffer for image!");
            }
            pGData = (unsigned char*)malloc(nChannelDataLen);
            if (NULL == pGData)
            {
                throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE, "Failed to malloc buffer for image!");
            }
            pBData = (unsigned char*)malloc(nChannelDataLen);
            if (NULL == pBData)
            {
                throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE, "Failed to malloc buffer for image!");
            }

            // 引用MVDImage 图像进行填充
            for (unsigned int i = 0; i < nImageHeight; i++)
            {
                for (unsigned int j = 0; j < nImageWidth; j++)
                {
                    pRData[i * nImageWidth + j] = pszMvdImgData[i * nImageWidth * 3 + j * 3 + 0];
                    pGData[i * nImageWidth + j] = pszMvdImgData[i * nImageWidth * 3 + j * 3 + 1];
                    pBData[i * nImageWidth + j] = pszMvdImgData[i * nImageWidth * 3 + j * 3 + 2];
                }
            }

            // 创建Halcon 图像;halcon 内部会深拷贝图像数据
            stErr = gen_image3(pHObject, "byte", nImageWidth, nImageHeight, (Hlong)pRData, (Hlong)pGData, (Hlong)pBData);
            if (H_MSG_OK != stErr)
            {
                throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE, "Failed to create halcon image!");
            }

            // halcon 图像创建时,图像数据进行了深拷贝，这里直接释放即可
            if (NULL != pRData)
            {
                free(pRData);
                pRData = NULL;
            }
            if (NULL != pGData)
            {
                free(pGData);
                pGData = NULL;
            }
            if (NULL != pBData)
            {
                free(pBData);
                pBData = NULL;
            }
        }
    }
    catch (IMVDException &ex)
    {
        if (NULL != pRData)
        {
            free(pRData);
            pRData = NULL;
        }
        if (NULL != pGData)
        {
            free(pGData);
            pGData = NULL;
        }
        if (NULL != pBData)
        {
            free(pBData);
            pBData = NULL;
        }
        throw ex;
    }
}
```

**注意事项 / 坑**：`gen_image1/3` 内部深拷贝，Gray 直接传 `pData` 指针即可；Color 需先 `malloc` 三块再拼 R/G/B，`gen_image3` 后立刻 `free`（Halcon 已深拷贝）；`catch` 中再次释放防泄漏。注意原文彩色分支 `stImageData` 用 `MVD_PIXEL_RGB_RGB24_C3`（RGB）。

#### 3.11.4 流程输出（IoImage）转 Halcon 图像

```cpp
HImage IoImageToHImage(IoImage ioImage)
{

HImage image;

if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXEL_MONO_08)
{

    image.GenImage1("byte", ioImage.stImage.Width, ioImage.stImage.Height, ioImage.stImage.ImageData);

}
if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3)
{

    int width = ioImage.stImage.Width;
    int height = ioImage.stImage.Height;
    long size = width * height * 3;

    byte* imageRedBuf = new byte[(long)width * height];
    byte* imageGreenBuf = new byte[(long)width * height];
    byte* imageBlueBuf = new byte[(long)width * height];
    byte* imageBuffer = new byte[size];
    memcpy(imageBuffer, ioImage.stImage.ImageData, size);

    int index = 0;
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++, index += 3)
        {
            imageRedBuf[row * width + col] = imageBuffer[index];
            imageGreenBuf[row * width + col] = imageBuffer[index + 1];
            imageBlueBuf[row * width + col] = imageBuffer[index + 2];
        }
    }

    delete[] imageBuffer;

    image.GenImage3("byte", width, height, imageRedBuf, imageGreenBuf, imageBlueBuf);

}

return image;
}
```

**注意事项 / 坑**：VM 输出 RGB 顺序，拆 R/G/B 三块传给 `GenImage3`；`imageRedBuf/GreenBuf/BlueBuf` 在 `GenImage3`（深拷贝）后未 `delete[]`，官方示例未释放，注意在 `gen_image3` 后释放以防泄漏。

**问题根因**：不熟悉 Halcon 图像转换为其它类型。

---

### 3.12 流程图像与算子图像互转

**适用场景**：VM SDK 流程图像 `IoImage` ↔ 算子 SDK 算子图像 `IMvdImage`。

**关键类型 / 类名**：`IoImage`、`IMvdImage`、`MVD_IMAGE_DATA_INFO`、`MvdPixelFormat`、`VisionDesigner::_MVD_PIXEL_FORMAT_`（`MVD_PIXEL_MONO_08` / `MVD_PIXEL_BGR_BGR24_C3` / `MVD_PIXEL_RGB_RGB24_C3`）。

#### 3.12.1 流程图像转算子图像

```cpp
IMvdImage* ImageConvert::IoImageToIMvdImage(IoImage ioImage)
{

// TODO: 在此处添加实现代码.

IMvdImage* iMvdImage = NULL;

MVD_IMAGE_DATA_INFO stImageData{ };


if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXEL_MONO_08)
{

    stImageData.stDataChannel[0].nRowStep = ioImage.stImage.Width;

    stImageData.stDataChannel[0].nLen = ioImage.stImage.DataLen;

    stImageData.stDataChannel[0].nSize = ioImage.stImage.DataLen;

    stImageData.stDataChannel[0].pData = (unsigned char*)ioImage.stImage.ImageData;

    iMvdImage->InitImage(ioImage.stImage.Width, ioImage.stImage.Height, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_MONO_08, stImageData);

}
else if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3)
{

    stImageData.stDataChannel[0].nRowStep = ioImage.stImage.Width*3;

    stImageData.stDataChannel[0].nLen = ioImage.stImage.DataLen;

    stImageData.stDataChannel[0].nSize = ioImage.stImage.DataLen;

    stImageData.stDataChannel[0].pData = (unsigned char*)ioImage.stImage.ImageData;

    iMvdImage->InitImage(ioImage.stImage.Width, ioImage.stImage.Height, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_BGR_BGR24_C3, stImageData);

}

return iMvdImage;
}
```

**注意事项 / 坑**：VM 图像 RGB（`MVD_PIXEL_RGB_RGB24_C3`）转算子图像时被标为 `MVD_PIXEL_BGR_BGR24_C3`（C++ 算子侧约定 BGR），这是 C++ 篇刻意写法；`iMvdImage` 需先 `CreateImageInstance` 创建，`InitImage` 前不可为空。

#### 3.12.2 算子图像转流程图像

```cpp
IoImage ImageConvert::IMvdImageToIoImage(IMvdImage* iMvdImage)
{

// TODO: 在此处添加实现代码.

IoImage ioImage{};

ioImage.stImage.Width = iMvdImage->GetWidth();
ioImage.stImage.Height = iMvdImage->GetHeight();

ioImage.stImage.ImageData = iMvdImage->GetImageData(0)->pData;//图像数据内存地址是连续的

if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PIXEL_MONO_08)
{

    ioImage.stImage.DataLen = iMvdImage->GetImageData(0)->nLen;

    ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_PIXEL_MONO_08;

}
else if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PIXEL_BGR_BGR24_C3)
{

    ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_PIXEL_RGB_RGB24_C3;

}

return ioImage;
}
```

**注意事项 / 坑**：算子图像 BGR（`MVD_PIXEL_BGR_BGR24_C3`）转流程图像时把像素格式标记为 RGB（`MVD_PIXEL_RGB_RGB24_C3`），与 3.12.1 成对；`ImageData` 浅引用 `GetImageData(0)->pData`，算子图像释放后流程图像悬空，需保证生命周期。

**问题根因**：不熟悉流程图像与算子图像互转。

---

### 3.13 算法模块图像与 Mat、Halcon、算子图像互转的方法

**适用场景**：自定义算法模块开发，C++ 工程中算法图像类型 `HKA_IMAGE` 与 `cv::Mat` / `HalconCpp::HImage` / `IMvdImage` 互转。

**关键类型 / 类名**：`HKA_IMAGE`（`format` / `width` / `height` / `step[0]` / `data[0]`；`HKA_IMG_MONO_08` / `HKA_IMG_RGB_RGB24_C3`）、`cv::Mat`、`cv::cvtColor` / `COLOR_RGB2BGR` / `COLOR_BGR2RGB`、`HImage`、`HString`、`get_image_pointer1/3` / `gen_image1/3`、`IMvdImage`、`CreateImageInstance`、`MVD_IMAGE_DATA_INFO`、`MVD_PIXEL_MONO_08` / `MVD_PIXEL_RGB_RGB24_C3`、`memcpy_s` / `memset`。

#### 3.13.1 HKA_IMAGE 与 Mat 互转

```cpp
Mat CAlgorithmModule::HKAImageToMat(HKA_IMAGE inputimage)
{
    Mat mat, mat1;
    if (inputimage.format == HKA_IMG_MONO_08)
    {
        mat = Mat(inputimage.height, inputimage.width, CV_8UC1, inputimage.data[0]);
    }
    else if (inputimage.format == HKA_IMG_RGB_RGB24_C3)
    {
        mat1 = Mat(inputimage.height, inputimage.width, CV_8UC3, inputimage.data[0]);
        cvtColor(mat1, mat, COLOR_RGB2BGR);
    }
    return mat;
}
```

```cpp
HKA_IMAGE CAlgorithmModule::MatToHKAImage(Mat mat)
{

    HKA_IMAGE inputimage;

    if (mat.channels() == 1)
    {

        inputimage = { HKA_IMG_MONO_08, 0 };

        inputimage.width = mat.cols;
        inputimage.height = mat.rows;
        inputimage.format = HKA_IMG_MONO_08;
        inputimage.step[0] = mat.cols;
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height);

        if (inputimage.data[0] != NULL)
        {

            memset(inputimage.data[0], 0, inputimage.width * inputimage.height);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height, mat.data, inputimage.width * inputimage.height);

        }

    }
    else if (mat.channels() == 3)
    {

        cvtColor(mat, mat, COLOR_BGR2RGB);

        inputimage = { HKA_IMG_RGB_RGB24_C3, 0 };

        inputimage.width = mat.cols;
        inputimage.height = mat.rows;
        inputimage.format = HKA_IMG_RGB_RGB24_C3;
        inputimage.step[0] = mat.cols * 3;
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height * 3);

        if (inputimage.data[0] != NULL)
        {

            memset(inputimage.data[0], 0, inputimage.width * inputimage.height * 3);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height * 3, mat.data, inputimage.width * inputimage.height * 3);

        }

    }

    return inputimage;
}
```

**注意事项 / 坑**：
- `HKA_IMAGE` 的 `data[0]` 用 `malloc`，返回值交还后由算法模块框架负责释放（或调用方释放）。
- Mat→HKA 彩色需 `COLOR_BGR2RGB`（Mat 是 BGR，HKA 是 RGB）；HKA→Mat 彩色需 `COLOR_RGB2BGR`。
- `Mat(inputimage.height, inputimage.width, ..., inputimage.data[0])` 为浅引用，原 `HKA_IMAGE` 释放后 Mat 悬空。

#### 3.13.2 HKA_IMAGE 与 Halcon 图像互转

```cpp
HImage CAlgorithmModule::HKAImageToHImage(HKA_IMAGE inputimage)
{

    HImage himage;

    if (HKA_IMG_MONO_08 == inputimage.format)
    {

        himage.GenImage1("byte", inputimage.width, inputimage.height, inputimage.data[0]);

    }

    if (HKA_IMG_RGB_RGB24_C3 == inputimage.format)
    {

        int width = inputimage.width;
        int height = inputimage.height;
        long size = width * height * 3;

        byte* imageRedBuf = new byte[(long)width * height];
        byte* imageGreenBuf = new byte[(long)width * height];
        byte* imageBlueBuf = new byte[(long)width * height];
        byte* imageBuffer = new byte[size];
        memcpy(imageBuffer, inputimage.data[0], size);

        int index = 0;
        for (int row = 0; row < height; row++)
        {
            for (int col = 0; col < width; col++, index += 3)
            {
                imageRedBuf[row * width + col] = imageBuffer[index];
                imageGreenBuf[row * width + col] = imageBuffer[index + 1];
                imageBlueBuf[row * width + col] = imageBuffer[index + 2];
            }
        }

        delete[] imageBuffer;

        himage.GenImage3("byte", width, height, imageRedBuf, imageGreenBuf, imageBlueBuf);

    }

    return himage;
}
```

```cpp
HKA_IMAGE CAlgorithmModule::HImageToHKAIMAGE(HImage himage)
{

    HKA_IMAGE inputimage;
    HString type;
    Hlong width, height;

    if (himage.CountChannels() == 1)
    {

        inputimage = { HKA_IMG_MONO_08, 0 };

        void* imagePtr = himage.GetImagePointer1(&type, &width, &height);
        inputimage.width = width;
        inputimage.height = height;
        inputimage.format = HKA_IMG_MONO_08;
        inputimage.step[0] = width;
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height);

        if (inputimage.data[0] != NULL)
        {

            memset(inputimage.data[0], 0, inputimage.width * inputimage.height);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height, imagePtr, inputimage.width * inputimage.height);

        }

    }
    else if (himage.CountChannels() == 3)
    {

        inputimage = { HKA_IMG_RGB_RGB24_C3, 0 };

        void* imageRedPtr;
        void* imageGreenPtr;
        void* imageBluePtr;

        himage.GetImagePointer3(&imageRedPtr, &imageGreenPtr, &imageBluePtr, &type, &width, &height);

        long size = width * height * 3;
        byte* imageRedBuf = new byte[width * height];
        byte* imageGreenBuf = new byte[width * height];
        byte* imageBlueBuf = new byte[width * height];
        memcpy_s(imageRedBuf, imageRedPtr, width * height);
        memcpy_s(imageGreenBuf, imageGreenPtr, width * height);
        memcpy_s(imageBlueBuf, imageBluePtr, width * height);

        byte* imageBuffer = new byte[size];
        int index = 0;
        for (int row = 0; row < height; row++)
        {
            for (int col = 0; col < width; col++, index += 3)
            {
                imageBuffer[index] = imageRedBuf[row * width + col];
                imageBuffer[index + 1] = imageGreenBuf[row * width + col];
                imageBuffer[index + 2] = imageBlueBuf[row * width + col];
            }
        }

        delete[] imageRedBuf;
        delete[] imageGreenBuf;
        delete[] imageBlueBuf;

        inputimage.width = width;
        inputimage.height = height;
        inputimage.format = HKA_IMG_RGB_RGB24_C3;
        inputimage.step[0] = width * 3;
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height * 3);

        if (inputimage.data[0] != NULL)
        {

            memset(inputimage.data[0], 0, inputimage.width * inputimage.height * 3);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height * 3, imageBuffer, inputimage.width * inputimage.height * 3);

        }

        delete[] imageBuffer;
    }

    return inputimage;
}
```

**注意事项 / 坑**：`HKAImageToHImage` 彩色中 `imageRedBuf/GreenBuf/BlueBuf` 在 `GenImage3`（深拷贝）后未 `delete[]`，官方示例未释放，注意释放；`HImageToHKAIMAGE` 的 `data[0]` 为 `malloc`，需释放；HKA 是 RGB 顺序，拆/拼无需交换通道。

#### 3.13.3 HKA_IMAGE 与算子图像（ImvdImage）互转

```cpp
IMvdImage* CAlgorithmModule::HKAImageToIMvdImage(HKA_IMAGE inputimage)
{
    IMvdImage* iMvdImage = NULL;
    CreateImageInstance(&iMvdImage);

    MVD_IMAGE_DATA_INFO stImageData;

    if (inputimage.format == HKA_IMG_MONO_08)
    {
        uint dataLen = (uint)(inputimage.width * inputimage.height);
        stImageData.stDataChannel[0].nRowStep = inputimage.width;
        stImageData.stDataChannel[0].nLen = dataLen;
        stImageData.stDataChannel[0].nSize = dataLen;
        stImageData.stDataChannel[0].pData = (unsigned char*)malloc(inputimage.width * inputimage.height);
        memset(stImageData.stDataChannel[0].pData, 0, inputimage.width * inputimage.height);
        stImageData.stDataChannel[0].pData = (unsigned char*)inputimage.data[0];
        iMvdImage->InitImage(inputimage.width, inputimage.height, MVD_PIXEL_MONO_08, stImageData);
    }
    else if (inputimage.format == HKA_IMG_RGB_RGB24_C3)
    {
        uint dataLen = (uint)(inputimage.width * inputimage.height * 3);
        stImageData.stDataChannel[0].nRowStep = inputimage.width * 3;
        stImageData.stDataChannel[0].nLen = dataLen;
        stImageData.stDataChannel[0].nSize = dataLen;
        stImageData.stDataChannel[0].pData = (unsigned char*)malloc(inputimage.width * inputimage.height * 3);
        memset(stImageData.stDataChannel[0].pData, 0, inputimage.width * inputimage.height);
        stImageData.stDataChannel[0].pData = (unsigned char*)inputimage.data[0];
        iMvdImage->InitImage(inputimage.width, inputimage.height, MVD_PIXEL_RGB_RGB24_C3, stImageData);
    }
    return iMvdImage;
}
```

```cpp
HKA_IMAGE CAlgorithmModule::IMvdImageToHKA_IMAGE(IMvdImage* iMvdImage)
{
    HKA_IMAGE inputimage;
    if (iMvdImage->GetPixelFormat() == MVD_PIXEL_MONO_08)
    {
        inputimage = { HKA_IMG_MONO_08, 0 };
        inputimage.width = iMvdImage->GetWidth();
        inputimage.height = iMvdImage->GetHeight();
        inputimage.format = HKA_IMG_MONO_08;
        inputimage.step[0] = iMvdImage->GetWidth();
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height);
        if (inputimage.data[0] != NULL)
        {
            memset(inputimage.data[0], 0, inputimage.width * inputimage.height);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height, iMvdImage->GetImageData()->stDataChannel[0].pData, inputimage.width * inputimage.height);
        }
    }
    else if (iMvdImage->GetPixelFormat() == MVD_PIXEL_RGB_RGB24_C3)
    {
        inputimage = { HKA_IMG_RGB_RGB24_C3, 0 };
        inputimage.width = iMvdImage->GetWidth();
        inputimage.height = iMvdImage->GetHeight();
        inputimage.format = HKA_IMG_RGB_RGB24_C3;
        inputimage.step[0] = iMvdImage->GetWidth() * 3;
        inputimage.data[0] = (char*)malloc(inputimage.width * inputimage.height * 3);
        if (inputimage.data[0] != NULL)
        {
            memset(inputimage.data[0], 0, inputimage.width * inputimage.height * 3);
            memcpy_s(inputimage.data[0], inputimage.width * inputimage.height * 3, iMvdImage->GetImageData()->stDataChannel[0].pData, inputimage.width * inputimage.height * 3);
        }
    }
    return inputimage;
}
```

**注意事项 / 坑**：
- `HKAImageToIMvdImage` 中先 `malloc` 再直接把 `pData` 指向 `inputimage.data[0]`，前者立刻泄漏（原文示例如此，实际应避免无谓 malloc 或记得释放）。
- `iMvdImage` 由 `CreateImageInstance` 创建，需对应释放接口释放。
- 算子图像此处用 `MVD_PIXEL_RGB_RGB24_C3`（RGB），与算法模块 HKA 一致，无需交换通道。

**问题根因**：算法模块图像转换相关（原文末节未单列根因句，归入 3.13 主题）。

---

## 条目索引

**C# 篇**
- 3.1 图像转换扫盲篇（CSharp）— 图像格式一览（MV_FRAME_OUT / ImageData / ImageBaseData_V2 / ImageBaseData / InputImageData / CMvdImage / HKA_IMAGE）+ 类型转换说明
- 3.2 相机采图转流程/Group/图像源SDK/模块/算子输入 — 3.2.1 CCDToImageBaseDataV2；3.2.2 CCDToImageBaseData；3.2.3 CCDToInputImageData；3.2.4 CCDToCMvdImage
- 3.3 Bitmap 转流程/Group/图像源SDK/模块/算子输入 + 流程输出转 Bitmap — 3.3.1 BitmapToImageBaseData_V2；3.3.2 BitmapToImageBaseData；3.3.3 BitmapToInputImageData；3.3.4 ConvertBitmap2MVDImage / ConvertMVDImage2Bitmap；3.3.5 ImageBaseData_V2ToBitmap / ImageBaseDatToBitmap
- 3.4 Mat 转流程/Group/图像源SDK/模块/算子输入 + 算子输出/流程输出转 Mat + 脚本图像互转 — 3.4.1 MatToImageBaseData_V2；3.4.2 MatToImageBaseData；3.4.3 MatToInputImageData；3.4.4 ConvertMat2MVDImage / ConvertMVDImage2Mat；3.4.5 ImageBaseData_V2ToMat；3.4.6 MatToImageData / ImageDataToMat
- 3.5 Halcon 转流程/Group/图像源SDK/模块/算子输入 + 算子输出/流程输出转 Halcon + 脚本图像互转 — 3.5.1 HalconImageToImageBaseDataV2；3.5.2 HalconImageToImageBaseData；3.5.3 HalconImageToModuleInputImage；3.5.4 ConvertHalcon2MVDImage / ConvertMVDImage2Halcon；3.5.5 ImageBaseDataV2ToHalconImage；3.5.6 HalconImageToImageData / ImageDataToHalconImage
- 3.6 流程图像与算子图像互转 — 3.6.1 ImageBaseData_V2ToCMvdImage；3.6.2 CMvdImageToImageBaseData_V2

**C++ 篇**
- 3.7 图像转换扫盲篇（C++）— 图像格式一览（MV_FRAME_OUT / ImageData / IoImage / ImageBaseData / IMvdImage / HKA_IMAGE）+ 类型转换说明
- 3.8 相机采图转流程/Group/图像源SDK/模块/算子输入 — 3.8.1 MV_FRAME_OUTToProcedureIoImage；3.8.2 MV_FRAME_OUTToImageBaseData；3.8.3 MV_FRAME_OUTToIMvdImage
- 3.9 QImage 转流程/Group/图像源SDK/模块/算子输入 + 流程输出转 QImage — 3.9.1 QImageToIoImage；3.9.2 QImageToImageBaseData；3.9.3 QImageToIMvdImage / IMvdImageToQImage；3.9.4 IoImageToQImage
- 3.10 Mat 转流程/Group/图像源SDK/模块/算子输入 + 算子输出/流程输出转 Mat — 3.10.1 MatToProcedureInputImage；3.10.2 MatToImageBaseData；3.10.3 ConvertMat2MvdImage / ConvertMvdImage2Mat；3.10.4 IoImageToMat
- 3.11 Halcon 转流程/Group/图像源SDK/模块/算子输入 + 算子输出/流程输出转 Halcon — 3.11.1 HImageToIoImage；3.11.2 HImageToImageBaseData；3.11.3 ConvertHalcon2MvdImage / ConvertMvdImage2Halcon；3.11.4 IoImageToHImage
- 3.12 流程图像与算子图像互转 — 3.12.1 IoImageToIMvdImage；3.12.2 IMvdImageToIoImage
- 3.13 算法模块图像与 Mat/Halcon/算子图像互转 — 3.13.1 HKAImageToMat / MatToHKAImage；3.13.2 HKAImageToHImage / HImageToHKAIMAGE；3.13.3 HKAImageToIMvdImage / IMvdImageToHKA_IMAGE

**通用坑索引**
- 通道顺序：Bitmap/Mat 为 BGR，VM/二次开发为 RGB（C# 与 C++ VM 侧）；C++ 算子图像枚举用 BGR（`MVD_PIXEL_BGR_BGR24_C3`），C# 算子图像用 RGB（`MVD_PIXEL_RGB_RGB24_C3`），核对 SDK 版本。
- 内存释放：`ImageBaseData_V2(IntPtr)` 浅拷贝需 `FreeHGlobal`；`InputImageData.Data` 需 `AllocHGlobal`/`FreeHGlobal`；C++ `malloc`/`new` 需 `free`/`delete[]`；`IMvdImage` 需 `CreateImageInstance` 后释放。
- 4 字节对齐：Bitmap 行 `Stride` 含冗余位，转 VM/MVD 需去冗余；反向需补冗余位。
- 指针生命周期：大量转换用浅引用（`ptr(0)` / `constBits()` / `GetImageData()->pData` / `ImageData=指针`），源对象释放即悬空。
- Halcon 深拷贝：`GenImage1/3` 内部深拷贝，传给它的托管/ pinned 数组需 `GCHandle.Pinned` 或 `malloc` 后释放。
- 位深：仅支持 8bit（byte / Mono8），其他位深需扩展。
- 属性拼写：脚本图像 `ImageData.Heigth`（官方原文，非 Height）。
