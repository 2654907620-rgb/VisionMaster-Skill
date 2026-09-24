# 专题·图像转换（C#/C++ 与各图像类型互转）
<!-- pdf pages 1122-1297 -->

<!-- page 1122 -->
HIKROBOT 
 
1113 
 
 
3 图像转换 
3.1 图像转换扫盲篇（CSharp）  
描述  
环境：VM4.2 + VS2013 及以上  
现象：相机、VM 脚本、VM SDK、算子SDK、算法模块中的图像类型是什么？  
解答  
1 图像格式一览  
除了Bitmap、Mat 和Halcon 中的图像类型，在VM 和开发（开发包含三种：VM SDK
开发（也称VM 二次开发）算子SDK 开发、自定义算法模块开发）中涉及的图像类型如
下：  
相机：图像数据流（此处图像数据流类型是MyCamera.MV_FRAME_OUT，是来自海康
机器人工业相机SDK），算子SDK 的MVDCamera.Net.dll 可以进行相机取流，它是对
相机SDK 的二次封装，取流时图像数据流类型是CMvdImage；算子SDK 中还有MvCa
meraControl.Net.dll 也可以进行相机取流，取流时图像数据流类型是MyCamera.MV_F
RAME_OUT； 
VM：脚本输入图像（图像类型是ImageData）；  



<!-- page 1123 -->
HIKROBOT 
 
1114 
 
 
VM SDK：流程输入图像（ImageBaseData_V2，VM4.2 SDK 新增）、Group 输入图像
（ImageBaseData_V2，VM4.2 SDK 新增）、图像源SDK 输入图像（ImageBaseDat
a）、模块输入图像（InputImageData）、流程输出图像（区分VM4.0 SDK 和VM4.2 
SDK 的获取输出图像的方式，VM4.2 获取流程图像的类型是ImageBaseData_V2） ；  
提示：VM4.3 SDK 中，流程、Group、模块输出输出图像类型统一为ImageBaseData； 
算子SDK：输入图像(CMvdImage)；  
算法模块：输入图像(HKA_IMAGE，是C++中图像类型)。  
2 图像类型转换（含单通道和三通道图像）三通道的Bitmap、Mat 为BGR，三通道的V
M 和二次开发为RGB，针对常用图像转换场景，列举如下（见3.2~3.6）。篇幅所致，后
续每种图像转换用函数表达，函数输入某种图像类型，返回转换后的某种图像类型。  
 
 



<!-- page 1124 -->
HIKROBOT 
 
1115 
 
 
3.2 相机采图转流程输入、Group 输入、图
像源SDK 输入、模块输入、算子输入图像  
描述  
环境：VM4.2 + VS2013 及以上  
现象：相机采图转换成其他图像类型  
解答  
相机采图（MyCamera.MV_FRAME_OUT）转换为流程输入图像、Group 输入图像、图
像源SDK 输入图像、模块输入图像、算子输入图像。  
1 相机采图转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V
2）  
public ImageBaseData_V2 CCDToImageBaseDataV2(MyCamera.MV_FR
AME_OUT frameOut) 
{ 
    ImageBaseData_V2 imageBaseDataV2 = new ImageBaseData_V2(); 
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelT
ype.PixelType_Gvsp_Mono8) 
    { 



<!-- page 1125 -->
HIKROBOT 
 
1116 
 
 
        imageBaseDataV2 = new ImageBaseData_V2(frameOut.pBufA
ddr, frameOut.stFrameInfo.nFrameLen, frameOut.stFrameInfo.nWidth, f
rameOut.stFrameInfo.nHeight, VMPixelFormat.VM_PIXEL_MONO_08); 
    } 
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvsp
PixelType.PixelType_Gvsp_RGB8_Packed) 
    { 
        imageBaseDataV2 = new ImageBaseData_V2(frameOut.pBufA
ddr, frameOut.stFrameInfo.nFrameLen, frameOut.stFrameInfo.nWidth, f
rameOut.stFrameInfo.nHeight, VMPixelFormat.VM_PIXEL_RGB24_C3); 
    } 
 
    return imageBaseDataV2; 
} 
var image = CCDToImageBaseDataV2(stFrameOut); 
//设置到流程 
var procedure = VmSolution.Instance["流程1"] as VmProcedure; 
procedure.ModuParams.SetInputImage_V2("ImageData", image); 
//设置到Group 
var group = VmSolution.Instance["流程1.组合模块1"] as IMVSGroupT
ool; 



<!-- page 1126 -->
HIKROBOT 
 
1117 
 
 
group.ModuParams.SetInputImage_V2("ImageData", image); 
2 相机采图转图像源SDK 输入（ImageBaseData）  
public ImageBaseData CCDToImageBaseData(MyCamera.MV_FRAME_
OUT frameOut) 
{ 
    ImageBaseData imageBaseData = new ImageBaseData(); 
    imageBaseData.Width = frameOut.stFrameInfo.nWidth; 
    imageBaseData.Height = frameOut.stFrameInfo.nHeight; 
    imageBaseData.DataLen = frameOut.stFrameInfo.nFrameLen; 
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelT
ype.PixelType_Gvsp_Mono8) 
    { 
        imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_M
ONO_08; 
    } 
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvsp
PixelType.PixelType_Gvsp_RGB8_Packed) 
    { 
        imageBaseData.Pixelformat = (int)VMPixelFormat.VM_PIXEL_R
GB24_C3; 



<!-- page 1127 -->
HIKROBOT 
 
1118 
 
 
    } 
    imageBaseData.ImageData = new byte[frameOut.stFrameInfo.nFra
meLen]; 
    Marshal.Copy(frameOut.pBufAddr, imageBaseData.ImageData, 0, (i
nt)frameOut.stFrameInfo.nFrameLen); 
    return imageBaseData; 
} 
var image = CCDToImageBaseData(stFrameOut); 
//设置到图像源 
ImageSourceModuleTool imageSourceModuleTool = (ImageSourceMo
duleTool)VmSolution.Instance["流程1.图像源1"]; 
imageSourceModuleTool.SetImageData(image); 
3 相机采图转模块输入（InputImageData）  
public InputImageData CCDToInputImageData(MyCamera.MV_FRAME_
OUT frameOut) 
{ 
    InputImageData inputImageData = new InputImageData(); 
    inputImageData.Names.DataName = "InImage";//只能使用默认名称
InImage 



<!-- page 1128 -->
HIKROBOT 
 
1119 
 
 
    inputImageData.Names.HeightName = "InImageHeight";//默认InI
mageHeight 
    inputImageData.Names.WidthName = "InImageWidth";//默认InIm
ageWidth 
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";
//默认InImagePixelFormat 
    inputImageData.Width = frameOut.stFrameInfo.nWidth; 
    inputImageData.Height = frameOut.stFrameInfo.nHeight; 
    inputImageData.DataLen = frameOut.stFrameInfo.nFrameLen; 
 
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelT
ype.PixelType_Gvsp_Mono8) 
    { 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_MONO8; 
 
    } 
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvsp
PixelType.PixelType_Gvsp_RGB8_Packed) 
    { 



<!-- page 1129 -->
HIKROBOT 
 
1120 
 
 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_RGB24; 
    } 
    //申请内存，记得inputImageData 使用完成后，手动释放内存，Marsh
al.FreeHGlobal 
    inputImageData.Data = Marshal.AllocHGlobal((int)frameOut.stFram
eInfo.nFrameLen); 
    byte[] imagedataBuffer = new byte[(int)frameOut.stFrameInfo.nFr
ameLen]; 
    Marshal.Copy(frameOut.pBufAddr, imagedataBuffer, 0, (int)frameO
ut.stFrameInfo.nFrameLen); 
    Marshal.Copy(imagedataBuffer, 0, inputImageData.Data, (int)frame
Out.stFrameInfo.nFrameLen); 
    return inputImageData; 
} 
var image= CCDToInputImageData(stFrameOut); 
//设置到模块         
var circlefindTool = VmSolution.Instance["流程1.圆查找1"] as IMVSIm
ageEnhanceModuCs.IMVSImageEnhanceModuTool; 
circlefindTool.ModuParams.SetInputImage(image); 
4 相机采图转算子输入（CmvdImage）  



<!-- page 1130 -->
HIKROBOT 
 
1121 
 
 
public CMvdImage CCDToCMvdImage(MyCamera.MV_FRAME_OUT fra
meOut) 
{ 
    VisionDesigner.CMvdImage cMvdImage = new VisionDesigner.C
MvdImage(); 
    VisionDesigner.MVD_IMAGE_DATA_INFO stImageData = new Visi
onDesigner.MVD_IMAGE_DATA_INFO(); 
    stImageData.stDataChannel[0].nLen = (uint)(frameOut.stFrameInfo.
nFrameLen); 
    stImageData.stDataChannel[0].nSize = (uint)(frameOut.stFrameInf
o.nFrameLen); 
    byte[] m_BufForDriver1 = new byte[frameOut.stFrameInfo.nFrame
Len]; 
    //数据Copy 
    Marshal.Copy(frameOut.pBufAddr, m_BufForDriver1, 0, (int)frameO
ut.stFrameInfo.nFrameLen); 
    stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver1; 
    if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvspPixelT
ype.PixelType_Gvsp_Mono8) 
    { 



<!-- page 1131 -->
HIKROBOT 
 
1122 
 
 
        stImageData.stDataChannel[0].nRowStep = (uint)frameOut.stFr
ameInfo.nWidth; 
        //初始化CMvdImage 
        cMvdImage.InitImage((uint)frameOut.stFrameInfo.nWidth, (uin
t)frameOut.stFrameInfo.nHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_MO
NO_08, stImageData); 
    } 
    else if (frameOut.stFrameInfo.enPixelType == MyCamera.MvGvsp
PixelType.PixelType_Gvsp_RGB8_Packed) 
    { 
        stImageData.stDataChannel[0].nRowStep = (uint)frameOut.stFr
ameInfo.nWidth * 3; 
        //初始化CMvdImage 
        cMvdImage.InitImage((uint)frameOut.stFrameInfo.nWidth, (uin
t)frameOut.stFrameInfo.nHeight, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB
_RGB24_C3, stImageData); 
    } 
    return cMvdImage; 
} 
问题根因  



<!-- page 1132 -->
HIKROBOT 
 
1123 
 
 
不熟悉相机采图转换为其它类型  
 
 



<!-- page 1133 -->
HIKROBOT 
 
1124 
 
 
3.3 Bitmap 转流程输入、Group 输入、图
像源SDK 输入、模块输入、算子输入、算
子输出、流程输出图像  
描述  
环境：VM4.2 + VS2013 及以上  
现象：Bitmap 转换成其他图像类型  
解答  
Bitmap 转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图像、
算子输入图像，流程输出图像转换为Bitmap。  
1 Bitmap 转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V
2）  
public ImageBaseData_V2 BitmapToImageBaseData_V2(Bitmap bmpIn
putImg) 
{ 
    ImageBaseData_V2 imageBaseData_V2 = new ImageBaseData_V2
(); 



<!-- page 1134 -->
HIKROBOT 
 
1125 
 
 
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputI
mg.PixelFormat; 
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0,
 bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnl
y, bitPixelFormat);//锁定 
 
    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format
8bppIndexed) 
    { 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width; 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height;/
/imageBaseData_V2 图像真正的缓存长度 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 



<!-- page 1135 -->
HIKROBOT 
 
1126 
 
 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex++]; 
            } 
            bitmapIndex += offset;//删除冗余数据 
        } 
        IntPtr _ImageBaseDataIntptr = Marshal.AllocHGlobal(ImageBa
seDataSize); 
 
Marshal.Copy(_ImageBaseDataBufferBytes, 0, _ImageBaseDataI
ntptr, ImageBaseDataSize); 
        imageBaseData_V2 = new ImageBaseData_V2(_ImageBaseDat
aIntptr, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, VMP
ixelFormat.VM_PIXEL_MONO_08); 
 
// 上面new imageBaseData_V2 是浅拷贝，imageBaseData_V2
使用结束后需要手动释放 
        //Marshal.FreeHGlobal(_ImageBaseDataIntptr); 
    } 



<!-- page 1136 -->
HIKROBOT 
 
1127 
 
 
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Fo
rmat24bppRgb) 
    { 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width * 3; 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height 
* 3;//imageBaseData_V2 图像真正的缓存长度 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 



<!-- page 1137 -->
HIKROBOT 
 
1128 
 
 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 2];//bitmap 为BGR，imageBas
eData_V2 为RGB 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 1]; 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex]; 
                bitmapIndex += 3; 
            } 
            bitmapIndex += offset; 
        } 
        IntPtr _ImageBaseDataIntptr = Marshal.AllocHGlobal(ImageBa
seDataSize); 
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, _ImageBaseDataI
ntptr, ImageBaseDataSize); 
        imageBaseData_V2 = new ImageBaseData_V2(_ImageBaseDat
aIntptr, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, VMP
ixelFormat.VM_PIXEL_RGB24_C3); 
        // 上面new imageBaseData_V2 是浅拷贝，使用结束后需要手动释
放 
        //Marshal.FreeHGlobal(_ImageBaseDataIntptr); 



<!-- page 1138 -->
HIKROBOT 
 
1129 
 
 
} 
bmpInputImg.UnlockBits(bmData);  // 解除锁定 
    return imageBaseData_V2; 
} 
2 Bitmap 转图像源SDK 输入（ImageBaseData）  
public ImageBaseData BitmapToImageBaseData(Bitmap bmpInputImg) 
{ 
    ImageBaseData imageBaseData = new ImageBaseData(); 
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputI
mg.PixelFormat; 
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0,
 bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnl
y, bitPixelFormat);//锁定 
 
    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format
8bppIndexed) 
    { 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width; 



<!-- page 1139 -->
HIKROBOT 
 
1130 
 
 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height; 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex++]; 
            } 
            bitmapIndex += offset; 
        } 
        imageBaseData = new ImageBaseData(_ImageBaseDataBuffer
Bytes, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, (int)V
MPixelFormat.VM_PIXEL_MONO_08); 
    } 



<!-- page 1140 -->
HIKROBOT 
 
1131 
 
 
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Fo
rmat24bppRgb) 
    { 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width * 3; 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height 
* 3; 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 2]; 



<!-- page 1141 -->
HIKROBOT 
 
1132 
 
 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 1]; 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex]; 
                bitmapIndex += 3; 
            } 
            bitmapIndex += offset; 
        } 
        imageBaseData = new ImageBaseData(_ImageBaseDataBuffer
Bytes, (uint)ImageBaseDataSize, bmData.Width, bmData.Height, (int)V
MPixelFormat.VM_PIXEL_RGB24_C3); 
} 
bmpInputImg.UnlockBits(bmData);  // 解除锁定 
    return imageBaseData; 
} 
3 Bitmap 转模块输入（InputImageData）  
public InputImageData BitmapToInputImageData(Bitmap bmpInputIm
g) 
{ 
    InputImageData inputImageData = new InputImageData(); 



<!-- page 1142 -->
HIKROBOT 
 
1133 
 
 
    System.Drawing.Imaging.PixelFormat bitPixelFormat = bmpInputI
mg.PixelFormat; 
    BitmapData bmData = bmpInputImg.LockBits(new Rectangle(0, 0,
 bmpInputImg.Width, bmpInputImg.Height), ImageLockMode.ReadOnl
y, bitPixelFormat);//锁定 
 
    inputImageData.Names.DataName = "InImage";//只能使用默认名称
InImage 
    inputImageData.Names.HeightName = "InImageHeight";//默认InI
mageHeight 
    inputImageData.Names.WidthName = "InImageWidth";//默认InIm
ageWidth 
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";
//默认InImagePixelFormat 
    inputImageData.Width = bmData.Width; 
    inputImageData.Height = bmData.Height; 
 
    if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Format
8bppIndexed) 
    { 



<!-- page 1143 -->
HIKROBOT 
 
1134 
 
 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width; 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height; 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex++]; 
            } 
            bitmapIndex += offset; 
        } 



<!-- page 1144 -->
HIKROBOT 
 
1135 
 
 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_MONO8; 
        inputImageData.DataLen = (uint)ImageBaseDataSize; 
        inputImageData.Data = Marshal.AllocHGlobal(ImageBaseData
Size);//inputImageData.Data 需要申请内存; 记得inputImageData 使用完
成后，手动释放内存，Marshal.FreeHGlobal 
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, inputImageData.
Data, _ImageBaseDataBufferBytes.Length); 
    } 
    else if (bitPixelFormat == System.Drawing.Imaging.PixelFormat.Fo
rmat24bppRgb) 
    { 
        Int32 bitmapDataSize = bmData.Stride * bmData.Height;//bit
map 图像缓存长度 
        int offset = bmData.Stride - bmData.Width * 3; 
        Int32 ImageBaseDataSize = bmData.Width * bmData.Height 
* 3; 
        byte[] _BitImageBufferBytes = new byte[bitmapDataSize]; 
        byte[] _ImageBaseDataBufferBytes = new byte[ImageBaseDat
aSize]; 



<!-- page 1145 -->
HIKROBOT 
 
1136 
 
 
        Marshal.Copy(bmData.Scan0, _BitImageBufferBytes, 0, bitmap
DataSize); 
        int bitmapIndex = 0; 
        int ImageBaseDataIndex = 0; 
        for (int i = 0; i < bmData.Height; i++) 
        { 
            for (int j = 0; j < bmData.Width; j++) 
            { 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 2]; 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex + 1]; 
                _ImageBaseDataBufferBytes[ImageBaseDataIndex++] 
= _BitImageBufferBytes[bitmapIndex]; 
                bitmapIndex += 3; 
            } 
            bitmapIndex += offset; 
        } 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_RGB24; 
        inputImageData.DataLen = (uint)ImageBaseDataSize; 



<!-- page 1146 -->
HIKROBOT 
 
1137 
 
 
        inputImageData.Data = Marshal.AllocHGlobal(ImageBaseData
Size);// //inputImageData.Data 需要申请内存; 记得inputImageData 使用
完成后，手动释放内存，Marshal.FreeHGlobal 
        Marshal.Copy(_ImageBaseDataBufferBytes, 0, inputImageData.
Data, _ImageBaseDataBufferBytes.Length); 
    } 
    bmpInputImg.UnlockBits(bmData);  // 解除锁定 
    return inputImageData; 
} 
4 Bitmap 与算子（CmvdImage）互转  
private static void ConvertBitmap2MVDImage(Bitmap cBitmapImg, C
MvdImage cMvdImg) 
{ 
    // 参数合法性判断 
    if(null == cBitmapImg || null == cMvdImg) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL); 
    } 
 



<!-- page 1147 -->
HIKROBOT 
 
1138 
 
 
    // 判断像素格式 
    if (PixelFormat.Format8bppIndexed != cBitmapImg.PixelFormat &
& PixelFormat.Format24bppRgb != cBitmapImg.PixelFormat) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    } 
 
    Int32 nImageWidth = cBitmapImg.Width; 
    Int32 nImageHeight = cBitmapImg.Height; 
    Int32 nChannelNum = 0; 
    BitmapData bitmapData = null; 
 
    try  
    { 
        // 获取图像信息 
        if (PixelFormat.Format8bppIndexed == cBitmapImg.PixelForm
at) // 灰度图 
        { 
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, n
ImageWidth, nImageHeight) 



<!-- page 1148 -->
HIKROBOT 
 
1139 
 
 
                                                            , ImageL
ockMode.ReadOnly 
                                                            , PixelFor
mat.Format8bppIndexed); 
            cMvdImg.InitImage(Convert.ToUInt32(nImageWidth), Conv
ert.ToUInt32(nImageHeight), MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_
08); 
            nChannelNum = 1; 
        } 
        else if (PixelFormat.Format24bppRgb == cBitmapImg.PixelFor
mat) // 彩色图 
        { 
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, n
ImageWidth, nImageHeight) 
                                                        , ImageLock
Mode.ReadOnly 
                                                        , PixelForma
t.Format24bppRgb); 
            cMvdImg.InitImage(Convert.ToUInt32(nImageWidth), Conv
ert.ToUInt32(nImageHeight), MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RG
B24_C3); 



<!-- page 1149 -->
HIKROBOT 
 
1140 
 
 
            nChannelNum = 3; 
        } 
 
        // 考虑图像是否4 字节对齐，bitmap 要求4 字节对齐，而mvdima
ge 不要求对齐 
        if (0 == nImageWidth % 4) // 4 字节对齐时，直接拷贝 
        { 
            Marshal.Copy(bitmapData.Scan0, cMvdImg.GetImageData
().stDataChannel[0].arrDataBytes, 0, nImageWidth * nImageHeight * n
ChannelNum); 
        } 
        else // 按步长逐行拷贝 
        { 
            // 每行实际占用字节数 
            Int32 nRowPixelByteNum = nImageWidth * nChannelNu
m + 4 - (nImageWidth * nChannelNum % 4); 
            // 每行首字节首地址 
            IntPtr bitmapDataRowPos = IntPtr.Zero; 
            for (int i = 0; i < nImageHeight; i++) 
            { 
                // 获取每行第一个像素值的首地址 



<!-- page 1150 -->
HIKROBOT 
 
1141 
 
 
                bitmapDataRowPos = new IntPtr(bitmapData.Scan0.T
oInt64() + nRowPixelByteNum * i); 
                Marshal.Copy(bitmapDataRowPos, cMvdImg.GetImage
Data().stDataChannel[0].arrDataBytes, i * nImageWidth * nChannelNu
m, nImageWidth * nChannelNum); 
            } 
        } 
 
        // bitmap 彩色图按BGR 存储，而MVDimg 按RGB 存储，改变存
储顺序 
        // 交换R 和B 
        if (PixelFormat.Format24bppRgb == cBitmapImg.PixelFormat) 
        { 
            byte bTemp; 
            byte[] bMvdImgData = cMvdImg.GetImageData().stDataC
hannel[0].arrDataBytes; 
            for (int i = 0; i < nImageWidth * nImageHeight; i++) 
            { 
                bTemp = bMvdImgData[3 * i]; 
                bMvdImgData[3 * i] = bMvdImgData[3 * i + 2]; 
                bMvdImgData[3 * i + 2] = bTemp; 



<!-- page 1151 -->
HIKROBOT 
 
1142 
 
 
            } 
        }   
    } 
    finally 
    { 
        cBitmapImg.UnlockBits(bitmapData); 
    }          
} 
 
private static void ConvertMVDImage2Bitmap(CMvdImage cMvdImg, 
ref Bitmap cBitmapImg) 
{ 
    // 参数合法性判断 
    if (null == cMvdImg) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL); 
    } 
 
    // 判断像素格式 



<!-- page 1152 -->
HIKROBOT 
 
1143 
 
 
    if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 != cMvdImg.PixelF
ormat && MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 != cMvdI
mg.PixelFormat) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    } 
 
    Int32 nImageWidth = Convert.ToInt32(cMvdImg.Width); 
    Int32 nImageHeight = Convert.ToInt32(cMvdImg.Height); 
    Int32 nChannelNum = 0; 
    BitmapData bitmapData = null; 
    byte[] bBitmapDataTemp = null; 
    try 
    { 
        // 获取图像信息 
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == cMvdImg.
PixelFormat) // 灰度图 
        { 
            cBitmapImg = new Bitmap(nImageWidth, nImageHeight, 
PixelFormat.Format8bppIndexed); 



<!-- page 1153 -->
HIKROBOT 
 
1144 
 
 
 
            // 灰度图需指定调色板 
            ColorPalette colorPalette = cBitmapImg.Palette; 
            for (int j = 0; j < 256; j++) 
            { 
                colorPalette.Entries[j] = Color.FromArgb(j, j, j); 
            } 
            cBitmapImg.Palette = colorPalette; 
 
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, n
ImageWidth, nImageHeight) 
                                                            , ImageL
ockMode.WriteOnly 
                                                            , PixelFor
mat.Format8bppIndexed); 
 
            // 灰度图不做深拷贝 
            bBitmapDataTemp = cMvdImg.GetImageData().stDataCha
nnel[0].arrDataBytes; 
            nChannelNum = 1; 
        } 



<!-- page 1154 -->
HIKROBOT 
 
1145 
 
 
        else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == c
MvdImg.PixelFormat) // 彩色图 
        { 
            cBitmapImg = new Bitmap(nImageWidth, nImageHeight, 
PixelFormat.Format24bppRgb); 
            bitmapData = cBitmapImg.LockBits(new Rectangle(0, 0, n
ImageWidth, nImageHeight) 
                                                        , ImageLock
Mode.WriteOnly 
                                                        , PixelForma
t.Format24bppRgb); 
            // 彩色图做深拷贝 
            bBitmapDataTemp = new byte[cMvdImg.GetImageData().
stDataChannel[0].arrDataBytes.Length]; 
            Array.Copy(cMvdImg.GetImageData().stDataChannel[0].arr
DataBytes, bBitmapDataTemp, bBitmapDataTemp.Length); 
            nChannelNum = 3; 
        } 
 
        // bitmap 彩色图按BGR 存储，而MVDimg 按RGB 存储，改变存
储顺序 



<!-- page 1155 -->
HIKROBOT 
 
1146 
 
 
        // 交换R 和B 
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == cMvdI
mg.PixelFormat) 
        { 
            byte bTemp; 
            for (int i = 0; i < nImageWidth * nImageHeight; i++) 
            { 
                bTemp = bBitmapDataTemp[3 * i]; 
                bBitmapDataTemp[3 * i] = bBitmapDataTemp[3 * i +
 2]; 
                bBitmapDataTemp[3 * i + 2] = bTemp; 
            } 
        } 
            
        // 考虑图像是否4 字节对齐，bitmap 要求4 字节对齐，而mvdima
ge 不要求对齐 
        if (0 == nImageWidth % 4) // 4 字节对齐时，直接拷贝 
        { 
            Marshal.Copy(bBitmapDataTemp, 0, bitmapData.Scan0, nI
mageWidth * nImageHeight * nChannelNum); 
        } 



<!-- page 1156 -->
HIKROBOT 
 
1147 
 
 
        else // 按步长逐行拷贝 
        { 
            // 每行实际占用字节数 
            Int32 nRowPixelByteNum = nImageWidth * nChannelNu
m + 4 - (nImageWidth * nChannelNum % 4); 
            // 每行首字节首地址 
            IntPtr bitmapDataRowPos = IntPtr.Zero; 
            for (int i = 0; i < nImageHeight; i++) 
            { 
                // 获取每行第一个像素值的首地址 
                bitmapDataRowPos = new IntPtr(bitmapData.Scan0.T
oInt64() + nRowPixelByteNum * i); 
                Marshal.Copy(bBitmapDataTemp, i * nImageWidth * 
nChannelNum, bitmapDataRowPos, nImageWidth * nChannelNum); 
            } 
        } 
 
        cBitmapImg.UnlockBits(bitmapData); 
    } 
    catch (MvdException ex) 
    { 



<!-- page 1157 -->
HIKROBOT 
 
1148 
 
 
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
5 流程输出（ImageBaseData_V2）转Bitmap  



<!-- page 1158 -->
HIKROBOT 
 
1149 
 
 
public Bitmap ImageBaseData_V2ToBitmap(ImageBaseData_V2 image
BaseData_V2)//VM4.2SDK 流程输出图像类型为ImageBaseData_V2 
{ 
    Bitmap bmpInputImg = null; 
    byte[] buffer = new byte[imageBaseData_V2.DataLen]; 
    Marshal.Copy(imageBaseData_V2.ImageData, buffer, 0, buffer.Len
gth); 
 
    if (VMPixelFormat.VM_PIXEL_MONO_08 == imageBaseData_V2.Pix
elformat) 
    { 
        Int32 imageWidth = Convert.ToInt32(imageBaseData_V2.Widt
h); 
        Int32 imageHeight = Convert.ToInt32(imageBaseData_V2.Heig
ht); 
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = Syst
em.Drawing.Imaging.PixelFormat.Format8bppIndexed; 
        bmpInputImg = new Bitmap(imageWidth, imageHeight, bitM
aPixelFormat); 
        int offset = imageWidth % 4 != 0 ? (4 - imageWidth % 4) :
 0;//添加冗余位，变成4 的倍数 



<!-- page 1159 -->
HIKROBOT 
 
1150 
 
 
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



<!-- page 1160 -->
HIKROBOT 
 
1151 
 
 
        BitmapData bitmapData = bmpInputImg.LockBits(new Rectan
gle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitM
aPixelFormat); 
        IntPtr imageBufferPtr = bitmapData.Scan0; 
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapByte
sLenth); 
        bmpInputImg.UnlockBits(bitmapData); 
 
        var colorPalettes = bmpInputImg.Palette; 
        for (int j = 0; j < 256; j++) 
        { 
            colorPalettes.Entries[j] = Color.FromArgb(j, j, j); 
        } 
        bmpInputImg.Palette = colorPalettes; 
    } 
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == imageBaseData_V
2.Pixelformat) 
    { 
        Int32 imageWidth = Convert.ToInt32(imageBaseData_V2.Widt
h); 



<!-- page 1161 -->
HIKROBOT 
 
1152 
 
 
        Int32 imageHeight = Convert.ToInt32(imageBaseData_V2.Heig
ht); 
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = Syst
em.Drawing.Imaging.PixelFormat.Format24bppRgb; 
        bmpInputImg = new Bitmap(imageWidth, imageHeight, bitM
aPixelFormat); 
        int offset = imageWidth % 4 != 0 ? (4 - (imageWidth * 3)
 % 4) : 0;//添加冗余位，变成4 的倍数 
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
                bitmapDataBytes[bitIndex + 1] = buffer[mvdIndex + 
1]; 
                bitmapDataBytes[bitIndex + 2] = buffer[mvdIndex]; 



<!-- page 1162 -->
HIKROBOT 
 
1153 
 
 
            } 
            for (int k = 0; k < offset; k++) 
            { 
                bitmapDataBytes[i * strid + imageWidth * 3 + k] = 
0; 
            } 
        } 
        BitmapData bitmapData = bmpInputImg.LockBits(new Rectan
gle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bitM
aPixelFormat); 
        IntPtr imageBufferPtr = bitmapData.Scan0; 
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapByte
sLenth); 
        bmpInputImg.UnlockBits(bitmapData); 
    } 
    return bmpInputImg; 
} 
 
public static Bitmap ImageBaseDatToBitmap(ImageBaseData imageBa
seDataInput)// VM4.3SDK 流程输出图像类型为ImageBaseData 
{ 



<!-- page 1163 -->
HIKROBOT 
 
1154 
 
 
    Bitmap bmpOutputImg = null; 
    byte[] buffer = new byte[imageBaseDataInput.DataLen]; 
    buffer = imageBaseDataInput.ImageData; 
 
    if (VMPixelFormat.VM_PIXEL_MONO_08 == (VMPixelFormat)image
BaseDataInput.Pixelformat) 
    { 
        Int32 imageWidth = Convert.ToInt32(imageBaseDataInput.Wi
dth); 
        Int32 imageHeight = Convert.ToInt32(imageBaseDataInput.He
ight); 
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = Syst
em.Drawing.Imaging.PixelFormat.Format8bppIndexed; 
        bmpOutputImg = new Bitmap(imageWidth, imageHeight, bit
MaPixelFormat); 
        int offset = imageWidth % 4 != 0 ? (4 - imageWidth % 4) :
 0;//添加冗余位，变成4 的倍数 
        int strid = imageWidth + offset; 
        int bitmapBytesLenth = strid * imageHeight; 
        byte[] bitmapDataBytes = new byte[bitmapBytesLenth]; 
        for (int i = 0; i < imageHeight; i++) 



<!-- page 1164 -->
HIKROBOT 
 
1155 
 
 
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
        BitmapData bitmapData = bmpOutputImg.LockBits(new Rect
angle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bi
tMaPixelFormat); 
        IntPtr imageBufferPtr = bitmapData.Scan0; 
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapByte
sLenth); 



<!-- page 1165 -->
HIKROBOT 
 
1156 
 
 
        bmpOutputImg.UnlockBits(bitmapData); 
 
        var colorPalettes = bmpOutputImg.Palette; 
        for (int j = 0; j < 256; j++) 
        { 
            colorPalettes.Entries[j] = Color.FromArgb(j, j, j); 
        } 
        bmpOutputImg.Palette = colorPalettes; 
    } 
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == (VMPixelFormat)i
mageBaseDataInput.Pixelformat) 
    { 
        Int32 imageWidth = Convert.ToInt32(imageBaseDataInput.Wi
dth); 
        Int32 imageHeight = Convert.ToInt32(imageBaseDataInput.He
ight); 
        System.Drawing.Imaging.PixelFormat bitMaPixelFormat = Syst
em.Drawing.Imaging.PixelFormat.Format24bppRgb; 
        bmpOutputImg = new Bitmap(imageWidth, imageHeight, bit
MaPixelFormat); 



<!-- page 1166 -->
HIKROBOT 
 
1157 
 
 
        int offset = imageWidth % 4 != 0 ? (4 - (imageWidth * 3)
 % 4) : 0;//添加冗余位，变成4 的倍数 
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
                bitmapDataBytes[bitIndex + 1] = buffer[mvdIndex + 
1]; 
                bitmapDataBytes[bitIndex + 2] = buffer[mvdIndex]; 
            } 
            for (int k = 0; k < offset; k++) 
            { 
                bitmapDataBytes[i * strid + imageWidth * 3 + k] = 
0; 
            } 



<!-- page 1167 -->
HIKROBOT 
 
1158 
 
 
        } 
        BitmapData bitmapData = bmpOutputImg.LockBits(new Rect
angle(0, 0, imageWidth, imageHeight), ImageLockMode.WriteOnly, bi
tMaPixelFormat); 
        IntPtr imageBufferPtr = bitmapData.Scan0; 
        Marshal.Copy(bitmapDataBytes, 0, imageBufferPtr, bitmapByte
sLenth); 
        bmpOutputImg.UnlockBits(bitmapData); 
    } 
    return bmpOutputImg; 
} 
问题根因  
不熟悉Bitmap 转换为其它类型  
3.4 Mat 转流程输入、Group 输入、图像
源SDK 输入、模块输入、算子输入、算子
输出、流程输出、脚本图像  
描述  



<!-- page 1168 -->
HIKROBOT 
 
1159 
 
 
环境：VM4.2 + VS2013 及以上  
现象：Mat 转换成其他图像类型  
解答  
Mat 转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图像、算
子输入图像，算子输出图像转Mat，流程输出图像转换为Mat，Mat 与脚本图像互转。  
1 Mat 转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_V2）  
 
public ImageBaseData_V2 MatToImageBaseData_V2(Mat matInputIm
g) 
{ 
    ImageBaseData_V2 imageBaseData_V2 = new ImageBaseData_V2
(); 
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height *
 matInputImg.Channels()); 
    if (1 == matInputImg.Channels()) 
    { 
        imageBaseData_V2 = new ImageBaseData_V2(matInputImg.Pt
r(0), dataLen, matInputImg.Width, matInputImg.Height, VMPixelForma
t.VM_PIXEL_MONO_08); 



<!-- page 1169 -->
HIKROBOT 
 
1160 
 
 
    } 
    else if (3 == matInputImg.Channels()) 
    { 
        //交换R 与B 通道 
        Cv2.CvtColor(matInputImg, matInputImg, ColorConversionCod
es.BGR2RGB); 
        imageBaseData_V2 = new ImageBaseData_V2(matInputImg.Pt
r(0), dataLen, matInputImg.Width, matInputImg.Height, VMPixelForma
t.VM_PIXEL_RGB24_C3); 
    } 
    return imageBaseData_V2; 
} 
2 Mat 转图像源SDK 输入（ImageBaseData）  
 
public ImageBaseData MatToImageBaseData(Mat matInputImg) 
{ 
    ImageBaseData imageBaseData = new ImageBaseData(); 
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height *
 matInputImg.Channels()); 
    byte[] buffer = new byte[dataLen]; 



<!-- page 1170 -->
HIKROBOT 
 
1161 
 
 
    Marshal.Copy(matInputImg.Ptr(0), buffer, 0, buffer.Length); 
    if (1 == matInputImg.Channels()) 
    { 
        imageBaseData = new ImageBaseData(buffer, dataLen, matIn
putImg.Width, matInputImg.Height, (int)VMPixelFormat.VM_PIXEL_MO
NO_08); 
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
        imageBaseData = new ImageBaseData(buffer, dataLen, matIn
putImg.Width, matInputImg.Height, (int)VMPixelFormat.VM_PIXEL_RGB
24_C3); 
    } 
    return imageBaseData; 



<!-- page 1171 -->
HIKROBOT 
 
1162 
 
 
} 
3 Mat 转模块输入（InputImageData）  
 
public InputImageData MatToInputImageData(Mat matInputImg) 
{ 
    InputImageData inputImageData = new InputImageData(); 
    uint dataLen = (uint)(matInputImg.Width * matInputImg.Height *
 matInputImg.Channels()); 
    byte[] buffer = new byte[dataLen]; 
    Marshal.Copy(matInputImg.Ptr(0), buffer, 0, buffer.Length); 
 
    inputImageData.Names.DataName = "InImage";//只能使用默认名称
InImage 
    inputImageData.Names.HeightName = "InImageHeight";//默认InI
mageHeight 
    inputImageData.Names.WidthName = "InImageWidth";//默认InIm
ageWidth 
    inputImageData.Names.PixelFormatName = "InImagePixelFormat";
//默认InImagePixelFormat 
    inputImageData.Width = matInputImg.Width; 



<!-- page 1172 -->
HIKROBOT 
 
1163 
 
 
    inputImageData.Height = matInputImg.Height; 
    inputImageData.DataLen = dataLen; 
    //inputImageData.Data 需要申请内存 
    inputImageData.Data = Marshal.AllocHGlobal((int)dataLen); 
 
    if (1 == matInputImg.Channels()) 
    { 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_MONO8; 
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



<!-- page 1173 -->
HIKROBOT 
 
1164 
 
 
        inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL
_FORMAT_RGB24; 
        Marshal.Copy(buffer, 0, inputImageData.Data, buffer.Length); 
    } 
    return inputImageData; 
} 
4 Mat 与算子图像（CmvdImage）互转  
private static void ConvertMat2MVDImage(Mat mat, CMvdImage cM
vdImg) 
{ 
    // 参数合法性判断 
    if (null == mat || null == cMvdImg) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_HANDLE); 
    } 
    // 像素格式判断 
    if (MatType.CV_8UC1 != mat.Type() && MatType.CV_8UC3 != ma
t.Type()) 
    { 



<!-- page 1174 -->
HIKROBOT 
 
1165 
 
 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    } 
 
    uint imgWidth = (uint)mat.Size().Width;// 图片的真实宽度 
    uint imgHeight = (uint)mat.Size().Height;// 图片的真实高度 
    byte[] bMvdImgData = null; 
 
    // 根据传入的mat 图像初始化MVDImage，并进行转换 
    if (mat.Type() == MatType.CV_8UC1) 
    { 
        cMvdImg.InitImage(imgWidth, imgHeight, MVD_PIXEL_FORMA
T.MVD_PIXEL_MONO_08); 
        bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].a
rrDataBytes; 
        Marshal.Copy(mat.Ptr(0), bMvdImgData, 0, bMvdImgData.Len
gth); 
    } 
    else if (mat.Type() == MatType.CV_8UC3) 
    { 



<!-- page 1175 -->
HIKROBOT 
 
1166 
 
 
        cMvdImg.InitImage(imgWidth, imgHeight, MVD_PIXEL_FORMA
T.MVD_PIXEL_RGB_RGB24_C3); 
        bMvdImgData = cMvdImg.GetImageData().stDataChannel[0].a
rrDataBytes; 
        Marshal.Copy(mat.Ptr(0), bMvdImgData, 0, bMvdImgData.Len
gth); 
 
        // Mat 为BGRBGR...存储，MVDImage 为RGBRGB...存储，需要调
整 
        byte bTemp;  
        for (int i = 0; i < imgWidth * imgHeight; i++) 
        { 
            bTemp = bMvdImgData[3 * i]; 
            bMvdImgData[3 * i] = bMvdImgData[3 * i + 2]; 
            bMvdImgData[3 * i + 2] = bTemp; 
        } 
    } 
} 
 
 



<!-- page 1176 -->
HIKROBOT 
 
1167 
 
 
private static void ConvertMVDImage2Mat(CMvdImage mvdImage, M
at mat) 
{ 
    // 参数合法性判断 
    if (null == mat || null == mvdImage) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_HANDLE); 
    } 
 
    // 像素格式判断 
    if (mvdImage.PixelFormat != MVD_PIXEL_FORMAT.MVD_PIXEL_MO
NO_08 && mvdImage.PixelFormat != MVD_PIXEL_FORMAT.MVD_PIXE
L_RGB_RGB24_C3) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    } 
 
    int imgWidth = (int)mvdImage.Width; 
    int imgHeight = (int)mvdImage.Height; 



<!-- page 1177 -->
HIKROBOT 
 
1168 
 
 
 
    // 根据传入的MVDImage 类型初始化Mat 
    if (mvdImage.PixelFormat == MVD_PIXEL_FORMAT.MVD_PIXEL_M
ONO_08) 
    { 
        mat.Create(imgHeight, imgWidth, MatType.CV_8UC1); 
        Marshal.Copy(mvdImage.GetImageData(0).arrDataBytes, 0, ma
t.Ptr(0), mvdImage.GetImageData(0).arrDataBytes.Length); 
    } 
    else if (mvdImage.PixelFormat == MVD_PIXEL_FORMAT.MVD_PIX
EL_RGB_RGB24_C3) 
    { 
        mat.Create(imgHeight, imgWidth, MatType.CV_8UC3); 
        // 先备份MVD 图像数据，保证不改变源图像数据 
        byte[] bMvdImgDataTemp = new byte[mvdImage.GetImageD
ata(0).arrDataBytes.Length]; 
        Array.Copy(mvdImage.GetImageData(0).arrDataBytes, bMvdIm
gDataTemp, bMvdImgDataTemp.Length); 
 
        // Mat 为BGRBGR...存储，MVD 为RGBRGB...存储，需要调整 
        byte bTemp; 



<!-- page 1178 -->
HIKROBOT 
 
1169 
 
 
        for (int i = 0; i < imgWidth * imgHeight; i++) 
        { 
            bTemp = bMvdImgDataTemp[3 * i]; 
            bMvdImgDataTemp[3 * i] = bMvdImgDataTemp[3 * i + 
2]; 
            bMvdImgDataTemp[3 * i + 2] = bTemp; 
        } 
        // 将数据拷贝至Mat 图像 
        Marshal.Copy(bMvdImgDataTemp, 0, mat.Ptr(0), bMvdImgDat
aTemp.Length); 
    } 
           
} 
5 流程输出（ImageBaseData_V2）转Mat 
 
public Mat ImageBaseData_V2ToMat(ImageBaseData_V2 imageBaseDa
ta_V2) 
{ 
    Mat matInputImg = new Mat(); 
    byte[] buffer = new byte[imageBaseData_V2.DataLen]; 



<!-- page 1179 -->
HIKROBOT 
 
1170 
 
 
    Marshal.Copy(imageBaseData_V2.ImageData, buffer, 0, buffer.Len
gth); 
 
    if (VMPixelFormat.VM_PIXEL_MONO_08 == imageBaseData_V2.Pix
elformat) 
    { 
        matInputImg.Create(imageBaseData_V2.Height, imageBaseDat
a_V2.Width, MatType.CV_8UC1); 
        Marshal.Copy(buffer, 0, matInputImg.Ptr(0), buffer.Length); 
    } 
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == imageBaseData_V
2.Pixelformat) 
    { 
        matInputImg.Create(imageBaseData_V2.Height, imageBaseDat
a_V2.Width, MatType.CV_8UC3); 
 
        //交换R 与B 通道 
        for (int i = 0; i < buffer.Length - 2; i += 3) 
        { 
            byte temp = buffer[i]; 
            buffer[i] = buffer[i + 2]; 



<!-- page 1180 -->
HIKROBOT 
 
1171 
 
 
            buffer[i + 2] = temp; 
        } 
        Marshal.Copy(buffer, 0, matInputImg.Ptr(0), buffer.Length); 
    } 
    return matInputImg; 
} 
6 Mat 与脚本图像（ImageData）互转  
 
public ImageData MatToImageData(Mat matImage) 
{ 
    ImageData imgOut = new ImageData(); 
    byte[] buffer = new Byte[matImage.Width * matImage.Height * 
matImage.Channels()]; 
    Marshal.Copy(matImage.Ptr(0), buffer, 0, buffer.Length); 
    if (1 == matImage.Channels()) 
    { 
        imgOut.Buffer = buffer; 
        imgOut.Width = matImage.Width; 
        imgOut.Heigth = matImage.Height; 
        imgOut.PixelFormat = ImagePixelFormate.MONO8; 



<!-- page 1181 -->
HIKROBOT 
 
1172 
 
 
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
public Mat ImageDataToMat(ImageData img) 
{ 
    Mat matImage = new Mat(); 



<!-- page 1182 -->
HIKROBOT 
 
1173 
 
 
    if(ImagePixelFormate.MONO8 == img.PixelFormat) 
    { 
        matImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV_8
UC1); 
        IntPtr grayPtr = Marshal.AllocHGlobal(img.Width * img.Heigt
h); 
        Marshal.Copy(img.Buffer, 0, matImage.Ptr(0), img.Buffer.Lengt
h); 
 
        //用完记得释放指针  
        Marshal.FreeHGlobal(grayPtr); 
    } 
    else if (ImagePixelFormate.RGB24 == img.PixelFormat) 
    { 
        matImage = Mat.Zeros(img.Heigth, img.Width, MatType.CV_8
UC3); 
        IntPtr rgbPtr = Marshal.AllocHGlobal(img.Width * img.Heigth
 * 3); 
        Marshal.Copy(img.Buffer, 0, matImage.Ptr(0), img.Buffer.Lengt
h); 



<!-- page 1183 -->
HIKROBOT 
 
1174 
 
 
        Cv2.CvtColor(matImage, matImage, ColorConversionCodes.RG
B2BGR); 
 
        //用完记得释放指针  
        Marshal.FreeHGlobal(rgbPtr); 
    } 
    return matImage; 
} 
问题根因  
不熟悉Mat 转换为其它类型  
 
 



<!-- page 1184 -->
HIKROBOT 
 
1175 
 
 
3.5 Halcon 转流程输入、Group 输入、图
像源SDK 输入、模块输入、算子输入、算
子输出、流程输出、脚本图像  
描述  
环境：VM4.2 + VS2013 及以上  
现象：Halcon 转换成其他图像类型  
解答  
Halcon 图像转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图
像、算子输入图像，算子输出图像转Halcon 图像，流程输出图像转换为Halcon 图像，H
alcon 图像与脚本图像互转。  
1 Halcon 图像转流程输入（ImageBaseData_V2）、Group 输入（ImageBaseData_
V2）  
public static ImageBaseData_V2 HalconImageToImageBaseDataV2(HO
bject hImageObj) 
{ 
    try 



<!-- page 1185 -->
HIKROBOT 
 
1176 
 
 
    { 
        ImageBaseData_V2 imageBaseData = new ImageBaseData_V2
(); 
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
                HOperatorSet.CountChannels(hImageObj, out channel
s); 
                //如果是单通道 
                if (channels.I == 1) 
                { 
                    HTuple imagePointer; 



<!-- page 1186 -->
HIKROBOT 
 
1177 
 
 
                    HOperatorSet.GetImagePointer1(hImageObj, out i
magePointer, out imageType, out imageWidth, out imageHeight); 
                    imageBaseData.Width = imageWidth.I; 
                    imageBaseData.Height = imageHeight.I; 
                    imageBaseData.Pixelformat = VMPixelFormat.VM_
PIXEL_MONO_08; 
                    imageBaseData.DataLen = (uint)(imageWidth.I * i
mageBaseData.Height); 
                    imageBaseData.ImageData = imagePointer; 
                } 
                //如果是三通道 
                else if (channels.I == 3) 
                { 
                    HTuple redChannel; 
                    HTuple greenChannel; 
                    HTuple blueChannel; 
                    HOperatorSet.GetImagePointer3(hImageObj, out r
edChannel, out greenChannel, out blueChannel, out imageType, out 
imageWidth, out imageHeight); 
                    imageBaseData.Width = imageWidth.I; 
                    imageBaseData.Height = imageHeight.I; 



<!-- page 1187 -->
HIKROBOT 
 
1178 
 
 
                    imageBaseData.Pixelformat = VMPixelFormat.VM_
PIXEL_RGB24_C3; 
                    byte[] imageRedBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    byte[] imageGreenBuffer = new byte[imageWidt
h.I * imageHeight.I]; 
                    byte[] imageBlueBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    Marshal.Copy(redChannel, imageRedBuffer, 0, im
ageRedBuffer.Length); 
                    Marshal.Copy(greenChannel, imageGreenBuffer, 0,
 imageGreenBuffer.Length); 
                    Marshal.Copy(blueChannel, imageBlueBuffer, 0, i
mageBlueBuffer.Length); 
                    byte[] imageBuffer = new byte[imageWidth.I * i
mageHeight.I * 3]; 
                    for (int row = 0; row < imageHeight.I; row++) 
                    { 
                        for (int col = 0, index = 0; col < imageWidt
h.I; col++, index += 3) 
                        { 



<!-- page 1188 -->
HIKROBOT 
 
1179 
 
 
                            imageBuffer[index] = imageRedBuffer[ro
w * imageWidth + col]; 
                            imageBuffer[index + 1] = imageGreenBu
ffer[row * imageWidth + col]; 
                            imageBuffer[index + 2] = imageBlueBuff
er[row * imageWidth + col]; 
                        } 
                    } 
                    imageBaseData.DataLen = (uint)(imageWidth.I * i
mageBaseData.Height * 3); 
                    imageBaseData.ImageData = Marshal.UnsafeAddr
OfPinnedArrayElement(imageBuffer, 0); 
                } 
                else 
                { 
                    hImageObj?.Dispose(); 
                    throw new Exception("不支持单通道，三通道以外的
图像"); 
                } 
            } 
            else 



<!-- page 1189 -->
HIKROBOT 
 
1180 
 
 
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
2 Halcon 图像转图像源SDK 输入（ImageBaseData）  



<!-- page 1190 -->
HIKROBOT 
 
1181 
 
 
public static ImageBaseData HalconImageToImageBaseData(HObject 
hImageObj) 
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
                HOperatorSet.CountChannels(hImageObj, out channel
s); 
                //如果是单通道 
                if (channels.I == 1) 



<!-- page 1191 -->
HIKROBOT 
 
1182 
 
 
                { 
                    HTuple imagePointer; 
                    HOperatorSet.GetImagePointer1(hImageObj, out i
magePointer, out imageType, out imageWidth, out imageHeight); 
                    imageBaseData.Width = imageWidth.I; 
                    imageBaseData.Height = imageHeight.I; 
                    imageBaseData.Pixelformat = (int)VMPixelFormat.
VM_PIXEL_MONO_08; 
                    imageBaseData.DataLen = (uint)(imageBaseData.
Width * imageBaseData.Height); 
                    imageBaseData.ImageData = new byte[imageWid
th.I * imageHeight.I]; 
                    Marshal.Copy(imagePointer, imageBaseData.Imag
eData, 0, imageWidth.I * imageHeight.I); 
                } 
                //如果是三通道 
                else if (channels.I == 3) 
                { 
                    HTuple redChannel; 
                    HTuple greenChannel; 
                    HTuple blueChannel; 



<!-- page 1192 -->
HIKROBOT 
 
1183 
 
 
                    HOperatorSet.GetImagePointer3(hImageObj, out r
edChannel, out greenChannel, out blueChannel, out imageType, out 
imageWidth, out imageHeight); 
                    imageBaseData.Width = imageWidth.I; 
                    imageBaseData.Height = imageHeight.I; 
                    imageBaseData.Pixelformat = (int)VMPixelFormat.
VM_PIXEL_RGB24_C3; 
                    imageBaseData.DataLen = (uint)(imageWidth.I * i
mageBaseData.Height * 3); 
                    imageBaseData.ImageData = new byte[imageWid
th.I * imageHeight.I * 3]; 
                    byte[] imageRedBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    byte[] imageGreenBuffer = new byte[imageWidt
h.I * imageHeight.I]; 
                    byte[] imageBlueBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, i
mageRedBuffer.Length); 
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer,
 0, imageGreenBuffer.Length); 



<!-- page 1193 -->
HIKROBOT 
 
1184 
 
 
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, 
imageBlueBuffer.Length); 
                    for (int row = 0; row < imageHeight.I; row++) 
                    { 
                        for (int col = 0, index = 0; col < imageWidt
h.I; col++, index += 3) 
                        { 
                            imageBaseData.ImageData[index] = imag
eRedBuffer[row * imageWidth + col]; 
                            imageBaseData.ImageData[index + 1] = i
mageGreenBuffer[row * imageWidth + col]; 
                            imageBaseData.ImageData[index + 2] = i
mageBlueBuffer[row * imageWidth + col]; 
                        } 
                    } 
                } 
                else 
                { 
                    hImageObj?.Dispose(); 
                    throw new Exception("不支持单通道，三通道以外的
图像"); 



<!-- page 1194 -->
HIKROBOT 
 
1185 
 
 
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



<!-- page 1195 -->
HIKROBOT 
 
1186 
 
 
3 Halcon 图像转模块输入（InputImageData）  
public static InputImageData HalconImageToModuleInputImage(HObj
ect hImageObj) 
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
                HOperatorSet.CountChannels(hImageObj, out channel
s); 
                //如果是单通道 



<!-- page 1196 -->
HIKROBOT 
 
1187 
 
 
                if (channels.I == 1) 
                { 
                    HTuple imagePointer; 
                    HOperatorSet.GetImagePointer1(hImageObj, out i
magePointer, out imageType, out imageWidth, out imageHeight); 
                    inputImageData.Width = imageWidth.I; 
                    inputImageData.Height = imageHeight.I; 
                    inputImageData.Pixelformat = ImagePixelFormat.I
MAGE_PIXEL_FORMAT_MONO8; 
                    inputImageData.DataLen = (uint)(inputImageData.
Width * inputImageData.Height); 
                    inputImageData.Data = imagePointer; 
                    inputImageData.Names.DataName = "InImage"; 
                    inputImageData.Names.WidthName = "InImageW
idth"; 
                    inputImageData.Names.HeightName = "InImageH
eight"; 
                    inputImageData.Names.PixelFormatName = "InIm
agePixelFormat"; 
                } 
                //如果是三通道 



<!-- page 1197 -->
HIKROBOT 
 
1188 
 
 
                else if (channels.I == 3) 
                { 
                    HTuple redChannel; 
                    HTuple greenChannel; 
                    HTuple blueChannel; 
                    HOperatorSet.GetImagePointer3(hImageObj, out r
edChannel, out greenChannel, out blueChannel, out imageType, out 
imageWidth, out imageHeight); 
                    inputImageData.Width = imageWidth.I; 
                    inputImageData.Height = imageHeight.I; 
                    inputImageData.Pixelformat = ImagePixelFormat.I
MAGE_PIXEL_FORMAT_RGB24; 
 
                    byte[] imageRedBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    byte[] imageGreenBuffer = new byte[imageWidt
h.I * imageHeight.I]; 
                    byte[] imageBlueBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, i
mageRedBuffer.Length); 



<!-- page 1198 -->
HIKROBOT 
 
1189 
 
 
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer,
 0, imageGreenBuffer.Length); 
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, 
imageBlueBuffer.Length); 
                    byte[] imageBuffer = new byte[imageWidth.I * i
mageHeight * 3]; 
                    for (int row = 0; row < imageHeight.I; row++) 
                    { 
                        for (int col = 0, index = 0; col < imageWidt
h.I; col++, index += 3) 
                        { 
                            imageBuffer[index] = imageRedBuffer[ro
w * imageWidth + col]; 
                            imageBuffer[index + 1] = imageGreenBu
ffer[row * imageWidth + col]; 
                            imageBuffer[index + 2] = imageBlueBuff
er[row * imageWidth + col]; 
                        } 
                    } 
                    inputImageData.DataLen = (uint)(inputImageData.
Width * inputImageData.Height * 3); 



<!-- page 1199 -->
HIKROBOT 
 
1190 
 
 
                    inputImageData.Data = Marshal.UnsafeAddrOfPin
nedArrayElement(imageBuffer, 0); 
                    inputImageData.Names.DataName = "InImage"; 
                    inputImageData.Names.WidthName = "InImageW
idth"; 
                    inputImageData.Names.HeightName = "InImageH
eight"; 
                    inputImageData.Names.PixelFormatName = "InIm
agePixelFormat"; 
                } 
                else 
                { 
                    hImageObj?.Dispose(); 
                    throw new Exception("不支持单通道，三通道以外的
图像"); 
                } 
            } 
            else 
            { 
                hImageObj?.Dispose(); 
                throw new Exception("不支持8bit 以外的位深度图像"); 



<!-- page 1200 -->
HIKROBOT 
 
1191 
 
 
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
4 Halcon 图像与算子图像（CmvdImage）互转  
private static void ConvertHalcon2MVDImage(HObject cHalconImg, C
MvdImage cMvdImg) 
{ 



<!-- page 1201 -->
HIKROBOT 
 
1192 
 
 
    // 参数合法性判断 
    if(null == cHalconImg || null == cMvdImg) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL); 
    } 
 
    // 获取通道数量 
    HTuple ChannelNum; 
    HOperatorSet.CountChannels(cHalconImg, out ChannelNum); 
    if(1 != ChannelNum.I && 3 != ChannelNum.I) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    }  



<!-- page 1202 -->
HIKROBOT 
 
1193 
 
 
 
    HTuple ImageType; 
    HTuple ImageWidth; 
    HTuple ImageHeight; 
    // 获取图像信息 
    if(1 == ChannelNum.I) // 灰度图 
    { 
        HTuple ImagePoint; 
        HOperatorSet.GetImagePointer1(cHalconImg, out ImagePoint, 
out ImageType, out ImageWidth, out ImageHeight); 
        cMvdImg.InitImage(Convert.ToUInt32(ImageWidth.I), Convert.T
oUInt32(ImageHeight.I), MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08); 
        Marshal.Copy(ImagePoint.IP, cMvdImg.GetImageData().stDataC
hannel[0].arrDataBytes, 0, ImageWidth.I * ImageHeight.I); 
    } 
    else if(3 == ChannelNum) 



<!-- page 1203 -->
HIKROBOT 
 
1194 
 
 
    { 
        HTuple ImagePointR; 
        HTuple ImagePointG; 
        HTuple ImagePointB; 
        HOperatorSet.GetImagePointer3(cHalconImg, out ImagePoint
R, out ImagePointG, out ImagePointB, out ImageType, out ImageWi
dth, out ImageHeight); 
        cMvdImg.InitImage(Convert.ToUInt32(ImageWidth.I), Convert.T
oUInt32(ImageHeight.I), MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_
C3); 
 
        // 将IntPtr 转为byte 数组 
        int nImageWidth = ImageWidth.I; 
        int nImageHeight = ImageHeight.I; 
        int nChannelDataLen = nImageWidth * nImageHeight; 
        byte[] bImageBufR = new byte[nChannelDataLen]; 



<!-- page 1204 -->
HIKROBOT 
 
1195 
 
 
        byte[] bImageBufG = new byte[nChannelDataLen]; 
        byte[] bImageBufB = new byte[nChannelDataLen]; 
        Marshal.Copy(ImagePointR.IP, bImageBufR, 0, nChannelDataL
en); 
        Marshal.Copy(ImagePointG.IP, bImageBufG, 0, nChannelDataL
en); 
        Marshal.Copy(ImagePointB.IP, bImageBufB, 0, nChannelDataL
en); 
 
        byte[] bMvdImgData = cMvdImg.GetImageData().stDataChan
nel[0].arrDataBytes; 
        // 将图像数据拷贝至算子图像组件 
        for (int i = 0; i < nImageHeight; i++) 
        { 
            for (int j = 0; j < nImageWidth; j++) 
            { 



<!-- page 1205 -->
HIKROBOT 
 
1196 
 
 
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 0] = b
ImageBufR[i * nImageWidth + j]; 
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 1] = b
ImageBufG[i * nImageWidth + j]; 
                bMvdImgData[i * nImageWidth * 3 + j * 3 + 2] = b
ImageBufB[i * nImageWidth + j]; 
            } 
        } 
    } 
} 
 
private static void ConvertMVDImage2Halcon(CMvdImage cMvdImg, 
HObject cHalconImg) 
{ 
    // 参数合法性判断 
    if (null == cHalconImg || null == cMvdImg) 



<!-- page 1206 -->
HIKROBOT 
 
1197 
 
 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_PARAMETER_ILLEGAL); 
    } 
 
    // 像素格式判断 
    MVD_PIXEL_FORMAT enMvdImagePixel = cMvdImg.PixelFormat; 
    if(MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 != enMvdImagePix
el && MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 != enMvdIma
gePixel) 
    { 
        throw new MvdException(MVD_MODULE_TYPE.MVD_MODUL_
APP, MVD_ERROR_CODE.MVD_E_SUPPORT); 
    } 
 
    GCHandle hImageData = new GCHandle(); 



<!-- page 1207 -->
HIKROBOT 
 
1198 
 
 
    GCHandle hImageDataR = new GCHandle(); 
    GCHandle hImageDataG = new GCHandle(); 
    GCHandle hImageDataB = new GCHandle(); 
    try  
    { 
        int nImageWidth = Convert.ToInt32(cMvdImg.Width); 
        int nImageHeight = Convert.ToInt32(cMvdImg.Height); 
        // 根据传入的图像初始化Halcon 
        if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == enMvdIma
gePixel) 
        { 
            // 引用MvdImg 数据来创建halcon 图像;halcon 内部会深拷贝 
            hImageData = GCHandle.Alloc(cMvdImg.GetImageData().s
tDataChannel[0].arrDataBytes, GCHandleType.Pinned); 
            HOperatorSet.GenImage1(out cHalconImg, "byte", nImag
eWidth, nImageHeight, hImageData.AddrOfPinnedObject()); 



<!-- page 1208 -->
HIKROBOT 
 
1199 
 
 
        } 
        else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == e
nMvdImagePixel) 
        { 
            // MVDImage 图像是一个通道RGBRGBRGB...存放；需要另外
开辟块内存 
            int nChannelDataLen = nImageWidth * nImageHeight; 
            byte[] bImageBufR = new byte[nChannelDataLen]; 
            byte[] bImageBufG = new byte[nChannelDataLen]; 
            byte[] bImageBufB = new byte[nChannelDataLen]; 
            byte[] bMvdImageData = cMvdImg.GetImageData().stDat
aChannel[0].arrDataBytes; 
            // 引用MVDImage 数据进行填充 
            for (int i = 0; i < nImageHeight; i++) 
            { 
                for (int j = 0; j < nImageWidth; j++) 



<!-- page 1209 -->
HIKROBOT 
 
1200 
 
 
                { 
                    bImageBufR[i * nImageWidth + j] = bMvdImage
Data[i * nImageWidth * 3 + j * 3 + 0]; 
                    bImageBufG[i * nImageWidth + j] = bMvdImage
Data[i * nImageWidth * 3 + j * 3 + 1]; 
                    bImageBufB[i * nImageWidth + j] = bMvdImage
Data[i * nImageWidth * 3 + j * 3 + 2]; 
                } 
            } 
            // 创建halcon 图像 
            hImageDataR = GCHandle.Alloc(bImageBufR, GCHandleTy
pe.Pinned); 
            hImageDataG = GCHandle.Alloc(bImageBufG, GCHandleT
ype.Pinned); 
            hImageDataB = GCHandle.Alloc(bImageBufB, GCHandleTy
pe.Pinned); 



<!-- page 1210 -->
HIKROBOT 
 
1201 
 
 
            HOperatorSet.GenImage3(out cHalconImg, "byte", nImag
eWidth, nImageHeight, hImageDataR.AddrOfPinnedObject(), hImageD
ataG.AddrOfPinnedObject(), hImageDataB.AddrOfPinnedObject()); 
        } 
    } 
    finally 
    { 
        if(hImageData.IsAllocated) 
        { 
            hImageData.Free(); 
        } 
        if (hImageDataR.IsAllocated) 
        { 
            hImageDataR.Free(); 
        } 



<!-- page 1211 -->
HIKROBOT 
 
1202 
 
 
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
5 流程输出（ImageBaseData_V2）转Halcon 图像  
public static HObject ImageBaseDataV2ToHalconImage(ImageBaseDat
a_V2 image) 
{ 
    try 
    { 



<!-- page 1212 -->
HIKROBOT 
 
1203 
 
 
        HObject imageObj = new HObject(); 
        HTuple width = image.Width; 
        HTuple height = image.Height; 
        if (image.Pixelformat == VMPixelFormat.VM_PIXEL_MONO_0
8) 
        { 
            HOperatorSet.GenImage1(out imageObj, "byte", width, he
ight, image.ImageData); 
        } 
        else if (image.Pixelformat == VMPixelFormat.VM_PIXEL_RGB2
4_C3) 
        { 
            byte[] imageRedBuffer = new byte[width * height.I]; 
            byte[] imageGreenBuffer = new byte[width * height.I]; 
            byte[] imageBlueBuffer = new byte[width * height.I]; 
            byte[] imageBuffer = new byte[width * height.I * 3]; 
            Marshal.Copy(image.ImageData, imageBuffer, 0, imageBuf
fer.Length); 
            for (int row = 0; row < height.I; row++) 
            { 



<!-- page 1213 -->
HIKROBOT 
 
1204 
 
 
                for (int col = 0, index = 0; col < width.I; col++, ind
ex += 3) 
                { 
                    imageRedBuffer[row * width.I + col] = imageBuf
fer[index]; 
                    imageGreenBuffer[row * width.I + col] = imageB
uffer[index + 1]; 
                    imageBlueBuffer[row * width.I + col] = imageBuf
fer[index + 2]; 
                } 
            } 
            HOperatorSet.GenImage3( 
                out imageObj, 
                "byte", 
                width, 
                height, 
                Marshal.UnsafeAddrOfPinnedArrayElement(imageRedB
uffer, 0), 
                Marshal.UnsafeAddrOfPinnedArrayElement(imageGree
nBuffer, 0), 



<!-- page 1214 -->
HIKROBOT 
 
1205 
 
 
                Marshal.UnsafeAddrOfPinnedArrayElement(imageBlue
Buffer, 0)); 
        } 
        return imageObj; 
    } 
    catch (Exception ex) 
    { 
        throw new Exception(ex.Message); 
    } 
} 
6 halcon 图像与脚本图像（ImageData）互转  
public static ImageData HalconImageToImageData(HObject hImageO
bj) 
{ 
    try 
    { 
        ImageData imageData = new ImageData(); 
        HTuple imageWidth = 0; 
        HTuple imageHeight = 0; 
        HTuple objClass = hImageObj.GetObjClass(); 



<!-- page 1215 -->
HIKROBOT 
 
1206 
 
 
        if (objClass.S.Equals("image")) 
        { 
            HTuple imageType; 
            HOperatorSet.GetImageType(hImageObj, out imageType); 
            if (imageType.S.Equals("byte")) 
            { 
                //获取图像通道数 
                HTuple channels = 0; 
                HOperatorSet.CountChannels(hImageObj, out channel
s); 
                //如果是单通道 
                if (channels.I == 1) 
                { 
                    HTuple imagePointer; 
                    HOperatorSet.GetImagePointer1(hImageObj, out i
magePointer, out imageType, out imageWidth, out imageHeight); 
                    imageData.Width = imageWidth.I; 
                    imageData.Heigth = imageHeight.I; 
                    imageData.PixelFormat = ImagePixelFormate.MO
NO8; 



<!-- page 1216 -->
HIKROBOT 
 
1207 
 
 
                    imageData.Buffer = new byte[imageWidth.I * ima
geHeight.I]; 
                    Marshal.Copy(imagePointer, imageData.Buffer, 0, 
imageWidth.I * imageHeight.I); 
                } 
                //如果是三通道 
                else if (channels.I == 3) 
                { 
                    HTuple redChannel; 
                    HTuple greenChannel; 
                    HTuple blueChannel; 
                    HOperatorSet.GetImagePointer3(hImageObj, out r
edChannel, out greenChannel, out blueChannel, out imageType, out 
imageWidth, out imageHeight); 
                    imageData.Width = imageWidth.I; 
                    imageData.Heigth = imageHeight.I; 
                    imageData.PixelFormat = ImagePixelFormate.RGB
24; 
                    imageData.Buffer = new byte[imageWidth.I * ima
geHeight.I * 3]; 



<!-- page 1217 -->
HIKROBOT 
 
1208 
 
 
                    byte[] imageRedBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    byte[] imageGreenBuffer = new byte[imageWidt
h.I * imageHeight.I]; 
                    byte[] imageBlueBuffer = new byte[imageWidth.I 
* imageHeight.I]; 
                    Marshal.Copy(redChannel.IP, imageRedBuffer, 0, i
mageRedBuffer.Length); 
                    Marshal.Copy(greenChannel.IP, imageGreenBuffer,
 0, imageGreenBuffer.Length); 
                    Marshal.Copy(blueChannel.IP, imageBlueBuffer, 0, 
imageBlueBuffer.Length); 
                    for (int row = 0; row < imageHeight.I; row++) 
                    { 
                        for (int col = 0, index = 0; col < imageWidt
h.I; col++, index += 3) 
                        { 
                            imageData.Buffer[index] = imageRedBuff
er[row * imageWidth + col]; 
                            imageData.Buffer[index + 1] = imageGre
enBuffer[row * imageWidth + col]; 



<!-- page 1218 -->
HIKROBOT 
 
1209 
 
 
                            imageData.Buffer[index + 2] = imageBlu
eBuffer[row * imageWidth + col]; 
                        } 
                    } 
                } 
                else 
                { 
                    hImageObj?.Dispose(); 
                    throw new Exception("不支持单通道，三通道以外的
图像"); 
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



<!-- page 1219 -->
HIKROBOT 
 
1210 
 
 
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



<!-- page 1220 -->
HIKROBOT 
 
1211 
 
 
        HTuple height = image.Heigth; 
        if (image.PixelFormat == ImagePixelFormate.MONO8) 
        { 
            imagePointer = Marshal.AllocHGlobal(image.Buffer.Lengt
h); 
            Marshal.Copy(image.Buffer, 0, imagePointer, image.Buffer.
Length); 
            HOperatorSet.GenImage1(out imageObj, "byte", width, he
ight, imagePointer); 
        } 
        else if (image.PixelFormat == ImagePixelFormate.RGB24) 
        { 
            byte[] imageRedBuffer = new byte[image.Buffer.Length / 
3]; 
            byte[] imageGreBuffer = new byte[image.Buffer.Length / 
3]; 
            byte[] imageBluBuffer = new byte[image.Buffer.Length / 
3]; 
            int index = 0; 
            for (int i = 0; i < image.Buffer.Length; index++, i += 3) 
            { 



<!-- page 1221 -->
HIKROBOT 
 
1212 
 
 
                imageRedBuffer[index] = image.Buffer[i]; 
                imageGreBuffer[index] = image.Buffer[i + 1]; 
                imageBluBuffer[index] = image.Buffer[i + 2]; 
            } 
            redChannel = Marshal.AllocHGlobal(imageRedBuffer.Lengt
h); 
            greenChannel = Marshal.AllocHGlobal(imageGreBuffer.Len
gth); 
            blueChannel = Marshal.AllocHGlobal(imageBluBuffer.Leng
th); 
            Marshal.Copy(imageRedBuffer, 0, redChannel, imageRedB
uffer.Length); 
            Marshal.Copy(imageGreBuffer, 0, greenChannel, imageGre
Buffer.Length); 
            Marshal.Copy(imageBluBuffer, 0, blueChannel, imageBluB
uffer.Length); 
            HOperatorSet.GenImage3(out imageObj, "byte", width, he
ight, redChannel, greenChannel, blueChannel); 
        } 
        return imageObj; 
    } 



<!-- page 1222 -->
HIKROBOT 
 
1213 
 
 
    catch (Exception ex) 
    { 
        Marshal.FreeHGlobal(imagePointer); 
        Marshal.FreeHGlobal(redChannel); 
        Marshal.FreeHGlobal(greenChannel); 
        Marshal.FreeHGlobal(blueChannel); 
        throw new Exception(ex.Message); 
    } 
} 
问题根因  
不熟悉Halcon 图像转换为其它类型  
 
 



<!-- page 1223 -->
HIKROBOT 
 
1214 
 
 
3.6 流程图像与算子图像互转  
描述  
环境：VM4.2 + VS2013 及以上  
现象：流程图像与算子图像互转  
解答  
VM SDK 开发中流程输入输出图像都是ImageBaseData_V2，算子SDK 开发中算子输入
输出图像都是CmvdImage，两者可以实现互转。  
1 流程图像转算子图像  
 
public CMvdImage ImageBaseData_V2ToCMvdImage(ImageBaseData_
V2 ImageBaseDataV2) 
{ 
    VisionDesigner.CMvdImage cmvdImage = new VisionDesigner.C
MvdImage(); 
    VisionDesigner.MVD_IMAGE_DATA_INFO stImageData = new Visi
onDesigner.MVD_IMAGE_DATA_INFO(); 



<!-- page 1224 -->
HIKROBOT 
 
1215 
 
 
    if (VMPixelFormat.VM_PIXEL_MONO_08 == ImageBaseDataV2.Pixe
lformat) 
    { 
        stImageData.stDataChannel[0].nRowStep = (uint)ImageBaseDa
taV2.Width; 
        stImageData.stDataChannel[0].nLen = (uint)(ImageBaseDataV
2.Width * ImageBaseDataV2.Height); 
        stImageData.stDataChannel[0].nSize = (uint)(ImageBaseDataV
2.Width * ImageBaseDataV2.Height); 
        byte[] m_BufForDriver1 = new byte[ImageBaseDataV2.Width 
* ImageBaseDataV2.Height]; 
        //数据Copy 
        Marshal.Copy(ImageBaseDataV2.ImageData, m_BufForDriver1, 
0, ((int)ImageBaseDataV2.Width * ImageBaseDataV2.Height)); 
        stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver
1; 
        //初始化CMvdImage 
        cmvdImage.InitImage((uint)ImageBaseDataV2.Width, (uint)Ima
geBaseDataV2.Height, MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08, stI
mageData); 
    } 



<!-- page 1225 -->
HIKROBOT 
 
1216 
 
 
    else if (VMPixelFormat.VM_PIXEL_RGB24_C3 == ImageBaseDataV
2.Pixelformat) 
    { 
        stImageData.stDataChannel[0].nRowStep = (uint)ImageBaseDa
taV2.Width * 3; 
        stImageData.stDataChannel[0].nLen = (uint)(ImageBaseDataV
2.Width * ImageBaseDataV2.Height * 3); 
        stImageData.stDataChannel[0].nSize = (uint)(ImageBaseDataV
2.Width * ImageBaseDataV2.Height * 3); 
        byte[] m_BufForDriver1 = new byte[3 * (ImageBaseDataV2.Wi
dth * ImageBaseDataV2.Height)]; 
        //数据Copy 
        Marshal.Copy(ImageBaseDataV2.ImageData, m_BufForDriver1, 
0, ((int)(ImageBaseDataV2.Width * ImageBaseDataV2.Height) * 3)); 
        stImageData.stDataChannel[0].arrDataBytes = m_BufForDriver
1; 
        //初始化CMvdImage 
        cmvdImage.InitImage((uint)ImageBaseDataV2.Width, (uint)Ima
geBaseDataV2.Height, MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C
3, stImageData); 
    } 



<!-- page 1226 -->
HIKROBOT 
 
1217 
 
 
    return cmvdImage; 
} 
2 算子图像转流程图像  
 
public ImageBaseData_V2 CMvdImageToImageBaseData_V2(CMvdIma
ge cmvdImage) 
{ 
    VM.PlatformSDKCS.ImageBaseData_V2 ImageBaseDataV2 = null; 
    if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == cmvdImage.Pix
elFormat) 
    { 
        var cmvdImageData = cmvdImage.GetImageData(); 
        IntPtr imagedata = Marshal.AllocHGlobal(cmvdImageData.stD
ataChannel[0].arrDataBytes.Length); 
        Marshal.Copy(cmvdImageData.stDataChannel[0].arrDataBytes, 
0, imagedata, cmvdImageData.stDataChannel[0].arrDataBytes.Length); 
        ImageBaseDataV2 = new ImageBaseData_V2(imagedata, (uin
t)cmvdImageData.stDataChannel[0].arrDataBytes.Length, (int)cmvdIma
ge.Width, (int)cmvdImage.Height, VMPixelFormat.VM_PIXEL_MONO_0
8); 



<!-- page 1227 -->
HIKROBOT 
 
1218 
 
 
        //使用结束后需要手动释放 
        //Marshal.FreeHGlobal(imagedata); 
        //imagedata = IntPtr.Zero; 
    } 
    else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 == cmv
dImage.PixelFormat) 
    { 
 
        var cmvdImageData = cmvdImage.GetImageData(); 
        IntPtr imagedata = Marshal.AllocHGlobal(cmvdImageData.stD
ataChannel[0].arrDataBytes.Length); 
        Marshal.Copy(cmvdImageData.stDataChannel[0].arrDataBytes, 
0, imagedata, cmvdImageData.stDataChannel[0].arrDataBytes.Length); 
        ImageBaseDataV2 = new ImageBaseData_V2(imagedata, (uin
t)cmvdImageData.stDataChannel[0].arrDataBytes.Length, (int)cmvdIma
ge.Width, (int)cmvdImage.Height, VMPixelFormat.VM_PIXEL_RGB24_C
3); 
        //使用结束后需要手动释放 
        //Marshal.FreeHGlobal(imagedata); 
        //imagedata = IntPtr.Zero; 
    } 



<!-- page 1228 -->
HIKROBOT 
 
1219 
 
 
    return ImageBaseDataV2; 
} 
问题根因  
不熟悉流程图像与算子图像互转  
 
 



<!-- page 1229 -->
HIKROBOT 
 
1220 
 
 
3.7 图像转换扫盲篇（C++）  
描述  
环境：VM4.2 + VS2013 及以上  
现象：有哪些图像类型可以进行转换？  
解答  
1 图像格式一览  
除了QImage、Mat 和Halcon 中的图像类型，在VM 和开发（二次开发包含三种：VM 
SDK 开发、算子SDK 开发、算法模块开发）中涉及的图像类型如下：  
相机：图像数据流（此处图像数据流类型是MyCamera.MV_FRAME_OUT，是来自MvC
ameraControl.Net.dll，即海康机器人工业相机SDK，在MVS SDK 和算子SDK 中都有
这个dll；算子SDK 的MVDCamera.Net.dll 也可以进行相机取流，它是对MvCameraC
ontrol.Net.dll 的二次封装，用MVDCamera.Net.dll 时，图像数据流类型是IMvdImag
e）；  
VM：脚本输入图像（图像类型是ImageData，是C#中图像类型）；  
VM SDK：流程输入图像（IoImage）、Group 输入图像（IoImage）、图像源SDK 输
入图像（ImageBaseData）、模块输入图像（ImageBaseData）；  



<!-- page 1230 -->
HIKROBOT 
 
1221 
 
 
算子SDK：输入图像(IMvdImage)；  
算法模块：输入图像(HKA_IMAGE)。  
2 图像类型转换（含单通道和三通道图像）三通道的Mat 为BGR，三通道QImage、VM
和二次开发为RGB，针对常用图像转换场景，列举如下（见3.8-3.13）。篇幅所致，后续
每种转换用函数表达，函数输入某种图像类型，返回某种图像类型。  
 
 



<!-- page 1231 -->
HIKROBOT 
 
1222 
 
 
3.8 相机采图转流程输入、Group 输入、图
像源SDK 输入、模块输入、算子输入图像  
描述  
环境：VM4.2 + VS2013 及以上  
现象：相机采图转换成其他图像类型  
解答  
相机采图（MyCamera.MV_FRAME_OUT）转换为流程输入图像、Group 输入图像、图
像源SDK 输入图像、模块输入图像、算子输入图像。  
1 相机采图转流程输入（IoImage）、Group 输入（IoImage）  
IoImage MV_FRAME_OUTToProcedureIoImage(MV_FRAME_OUT stIma
geInfo) 
{ 
 
// TODO: 在此处添加实现代码. 
 
IoImage ioImage{}; 
 
unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,
控制释放时机防止内存泄漏，写在此处为了方便参考 



<!-- page 1232 -->
HIKROBOT 
 
1223 
 
 
 
m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned c
har) * stImageInfo.stFrameInfo.nFrameLen); 
 
memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInf
o.stFrameInfo.nFrameLen); 
 
 
ioImage.stImage.Width = stImageInfo.stFrameInfo.nWidth; 
 
ioImage.stImage.Height = stImageInfo.stFrameInfo.nHeight; 
 
ioImage.stImage.DataLen = stImageInfo.stFrameInfo.nFrameLe
n; 
 
ioImage.stImage.ImageData = m_pSaveImageBuf; 
 
if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_M
ono8) 
 
{ 
 
 
ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_
PIXEL_MONO_08; 
 
} 
 
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvs
p_RGB8_Packed) 
 
{ 
 
 
ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_
PIXEL_RGB_RGB24_C3; 



<!-- page 1233 -->
HIKROBOT 
 
1224 
 
 
 
} 
 
return ioImage; 
} 
2 相机采图转图像源SDK 输入（ImageBaseData）、模块输入（ImageBaseData）  
ImageBaseData MV_FRAME_OUTToImageBaseData(MV_FRAME_OUT st
ImageInfo) 
{ 
 
// TODO: 在此处添加实现代码. 
 
ImageBaseData imageBaseData{}; 
 
unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,
控制释放时机防止内存泄漏，写在此处为了方便参考 
 
m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned c
har) * stImageInfo.stFrameInfo.nFrameLen); 
 
memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInf
o.stFrameInfo.nFrameLen); 
 
 
imageBaseData.Width = stImageInfo.stFrameInfo.nWidth; 
 
imageBaseData.Height = stImageInfo.stFrameInfo.nHeight; 
 
imageBaseData.DataLen = stImageInfo.stFrameInfo.nFrameLen; 
 
imageBaseData.ImageData = m_pSaveImageBuf; 



<!-- page 1234 -->
HIKROBOT 
 
1225 
 
 
 
if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_M
ono8) 
 
{ 
 
 
imageBaseData.Pixelformat = MvdPixelFormat::MVD_PI
XEL_MONO_08; 
 
} 
 
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvs
p_RGB8_Packed) 
 
{ 
 
 
imageBaseData.Pixelformat = MvdPixelFormat::MVD_PI
XEL_RGB_RGB24_C3; 
 
} 
 
 
return imageBaseData; 
} 
3 相机采图转算子输入（IMvdImage）  
IMvdImage* MV_FRAME_OUTToIMvdImage(MV_FRAME_OUT stImageI
nfo) 
{ 
 
// TODO: 在此处添加实现代码. 



<!-- page 1235 -->
HIKROBOT 
 
1226 
 
 
 
IMvdImage* iMvdImage = NULL; 
 
unsigned char* m_pSaveImageBuf = NULL;//建议在头文件声明,
控制释放时机防止内存泄漏，写在此处为了方便参考 
 
m_pSaveImageBuf = (unsigned char*)malloc(sizeof(unsigned c
har) * stImageInfo.stFrameInfo.nFrameLen); 
 
memcpy(m_pSaveImageBuf, stImageInfo.pBufAddr, stImageInf
o.stFrameInfo.nFrameLen); 
 
MVD_IMAGE_DATA_INFO stImageData{ }; 
 
 
if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvsp_M
ono8) 
 
{ 
 
 
stImageData.stDataChannel[0].nRowStep = stImageInf
o.stFrameInfo.nWidth; 
 
 
stImageData.stDataChannel[0].nLen = stImageInfo.stFr
ameInfo.nFrameLen; 
 
 
stImageData.stDataChannel[0].nSize = stImageInfo.stFr
ameInfo.nFrameLen; 
 
 
stImageData.stDataChannel[0].pData = m_pSaveImage
Buf; 



<!-- page 1236 -->
HIKROBOT 
 
1227 
 
 
 
 
iMvdImage->InitImage(stImageInfo.stFrameInfo.nWidt
h, stImageInfo.stFrameInfo.nHeight, VisionDesigner::_MVD_PIXEL_FOR
MAT_::MVD_PIXEL_MONO_08, stImageData); 
 
} 
 
else if (stImageInfo.stFrameInfo.enPixelType == PixelType_Gvs
p_RGB8_Packed) 
 
{ 
 
 
stImageData.stDataChannel[0].nRowStep = stImageInf
o.stFrameInfo.nWidth*3; 
 
 
stImageData.stDataChannel[0].nLen = stImageInfo.stFr
ameInfo.nFrameLen; 
 
 
stImageData.stDataChannel[0].nSize = stImageInfo.stFr
ameInfo.nFrameLen; 
 
 
stImageData.stDataChannel[0].pData = m_pSaveImage
Buf; 
 
 
iMvdImage->InitImage(stImageInfo.stFrameInfo.nWidt
h, stImageInfo.stFrameInfo.nHeight, VisionDesigner::_MVD_PIXEL_FOR
MAT_::MVD_PIXEL_BGR_BGR24_C3, stImageData); 
 
} 
 
 
return iMvdImage; 



<!-- page 1237 -->
HIKROBOT 
 
1228 
 
 
} 
问题根因  
不熟悉相机采图转换为其它类型  
 
 



<!-- page 1238 -->
HIKROBOT 
 
1229 
 
 
3.9 QImage 转流程输入、Group 输入、
图像源SDK 输入、模块输入、算子输入、
流程输出图像  
描述  
环境：VM4.2 + VS2013 及以上  
现象：QImage 转换成其他图像类型  
解答  
QImage 转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图
像、算子输入图像，流程输出图像转换为Bitmap。  
1 QImage 转流程输入（IoImage）、Group 输入（IoImage）  
IoImage QImageToIoImage(QImage qImage) 
{ 
    QString strReMsg = ""; 
    IoImage ioImage; 
    switch (qImage.format()) 
    { 



<!-- page 1239 -->
HIKROBOT 
 
1230 
 
 
    case QImage::Format_Indexed8: 
        ioImage.stImage.Width=qImage.width(); 
        ioImage.stImage.Height=qImage.height(); 
        ioImage.stImage.DataLen=qImage.sizeInBytes(); 
        ioImage.stImage.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_M
ONO_08; 
        ioImage.stImage.ImageData=(void *)qImage.constBits(); 
        //ioImage.stImage.ImageData=qImage.data_ptr(); 
        //QImage(ioImage.stImage.ImageData,ioImage.stImage.Width,i
oImage.stImage.Width,QImage::Format_RGB888); 
        break;        
    case QImage::Format_RGB888: 
        ioImage.stImage.Width=qImage.width(); 
        ioImage.stImage.Height=qImage.height(); 
        ioImage.stImage.DataLen=qImage.sizeInBytes(); 
        ioImage.stImage.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_R
GB_RGB24_C3; 
        ioImage.stImage.ImageData=(void *)qImage.constBits(); 
        break; 
    } 
    strReMsg = "QImageToIoImage s uccess."; 



<!-- page 1240 -->
HIKROBOT 
 
1231 
 
 
    ui->textEdit->append(strReMsg); 
    return ioImage; 
} 
2 QImage 转图像源SDK 输入（ImageBaseData）、模块输入（ImageBaseData）  
ImageBaseData QImageToImageBaseData(QImage qImage) 
{ 
    ImageBaseData  imageBaseData; 
    switch (qImage.format()) 
    { 
    case QImage::Format_Indexed8: 
        imageBaseData.Width=qImage.width(); 
        imageBaseData.Height=qImage.height(); 
        imageBaseData.DataLen=qImage.sizeInBytes(); 
        imageBaseData.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_M
ONO_08; 
        imageBaseData.ImageData=(void *)qImage.constBits(); 
        //ioImage.stImage.ImageData=qImage.data_ptr(); 
        break; 
    case QImage::Format_RGB888: 
        imageBaseData.Width=qImage.width(); 



<!-- page 1241 -->
HIKROBOT 
 
1232 
 
 
        imageBaseData.Height=qImage.height(); 
        imageBaseData.DataLen=qImage.sizeInBytes(); 
        imageBaseData.Pixelformat=_MvdPixelFormat_::MVD_PIXEL_RG
B_RGB24_C3; 
        imageBaseData.ImageData=(void *)qImage.constBits(); 
        break; 
    } 
    return imageBaseData; 
} 
3 Qimage 与算子图像（IMvdImage）互转  
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



<!-- page 1242 -->
HIKROBOT 
 
1233 
 
 
        stImageData.stDataChannel[0].nSize = qImage.sizeInBytes(); 
        stImageData.stDataChannel[0].pData = (unsigned char*)qImag
e.constBits(); 
        iMvdImage->InitImage(qImage.width(), qImage.height(),MVD_
PIXEL_FORMAT::MVD_PIXEL_MONO_08, stImageData); 
        break; 
    case QImage::Format_RGB888: 
        stImageData.stDataChannel[0].nRowStep = qImage.width()*3; 
        stImageData.stDataChannel[0].nLen = qImage.sizeInBytes(); 
        stImageData.stDataChannel[0].nSize = qImage.sizeInBytes(); 
        stImageData.stDataChannel[0].pData = (unsigned char*)qImag
e.constBits(); 
        iMvdImage->InitImage(qImage.width(), qImage.height(),MVD_
PIXEL_FORMAT::MVD_PIXEL_RGB_RGB24_C3, stImageData); 
        break; 
    } 
    return iMvdImage; 
} 
 
//算子转QImage 
QImage IMvdImageToQImage(IMvdImage * iMvdImage) 



<!-- page 1243 -->
HIKROBOT 
 
1234 
 
 
{ 
    if(iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PI
XEL_MONO_08) 
    { 
        //QImage qImage((const uchar*)iMvdImage->GetImageData
(0)->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),iMvdIma
ge->GetImageData(0)->nLen/iMvdImage->GetHeight(),QImage::Format
_Indexed8); 
        //QImage qImage(iMvdImage->GetImageData(0)->pData,iMvd
Image->GetWidth(),iMvdImage->GetHeight(),iMvdImage->GetImageD
ata(0)->nLen/iMvdImage->GetHeight(),QImage::Format_Indexed8); 
        QImage qImage((const uchar*)iMvdImage->GetImageData(0)
->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),QImage::For
mat_Grayscale8);//Format_Indexed8 
        return qImage; 
    } 
    if(iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::MVD_PI
XEL_RGB_RGB24_C3) 
    { 



<!-- page 1244 -->
HIKROBOT 
 
1235 
 
 
        QImage qImage((const uchar*)iMvdImage->GetImageData(0)
->pData,iMvdImage->GetWidth(),iMvdImage->GetHeight(),QImage::For
mat_RGB888); 
        return qImage; 
    } 
} 
4 流程输出（IoImage）转QImage  
QImage IoImageToQImage(IoImage inIoImage) 
{ 
    if(inIoImage.stImage.Pixelformat == _MvdPixelFormat_::MVD_PIXE
L_MONO_08) 
    { 
        QImage qImage((const uchar*)inIoImage.stImage.ImageData,i
nIoImage.stImage.Width,inIoImage.stImage.Height,QImage::Format_Gra
yscale8); 
        return qImage; 
    } 
    if(inIoImage.stImage.Pixelformat == _MvdPixelFormat_::MVD_PIXE
L_RGB_RGB24_C3) 
    { 



<!-- page 1245 -->
HIKROBOT 
 
1236 
 
 
        QImage qImage((const uchar*)inIoImage.stImage.ImageData,i
nIoImage.stImage.Width,inIoImage.stImage.Height,QImage::Format_RG
B888); 
        return qImage; 
    } 
} 
问题根因  
不熟悉QImage 转换为其它类型  
 
 



<!-- page 1246 -->
HIKROBOT 
 
1237 
 
 
3.10 Mat 与流程输入、Group 输入、图像
源SDK 输入、模块输入、算子输入、算子
输出、流程输出  
描述  
环境：VM4.2 + VS2013 及以上  
现象：Mat 转换成其他图像类型  
解答  
Mat 转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图像、算
子输入图像，算子输出图像转Mat，流程输出图像转换为Mat。  
1 Mat 转流程输入（IoImage）、Group 输入（IoImage）  
IoImage MatToProcedureInputImage(Mat matInputImg) 
{ 
 
if (matInputImg.empty()) 
 
{ 
 
 
throw IMVDException(MVD_MODUL_APP, MVD_E_PAR
AMETER_ILLEGAL); 



<!-- page 1247 -->
HIKROBOT 
 
1238 
 
 
 
} 
 
if ((CV_8UC1 != matInputImg.type()) && (CV_8UC3 != matInp
utImg.type())) 
 
{ 
 
 
throw IMVDException(MVD_MODUL_APP, MVD_E_SUP
PORT); 
 
} 
 
 
IoImage  m_pIoImage{}; 
 
uint dataLen = (uint)(matInputImg.cols * matInputImg.rows * 
matInputImg.channels()); 
 
CString strReMsg = _T(""); 
 
try 
 
{ 
 
 
if (CV_8UC1 == matInputImg.type()) 
 
 
{ 
 
 
 
m_pIoImage.stImage.Width = matInputImg.col
s; 
 
 
 
m_pIoImage.stImage.Width = matInputImg.col
s; 



<!-- page 1248 -->
HIKROBOT 
 
1239 
 
 
 
 
 
m_pIoImage.stImage.Height = matInputImg.ro
ws; 
 
 
 
m_pIoImage.stImage.DataLen = dataLen; 
 
 
 
m_pIoImage.stImage.Pixelformat = _MvdPixelF
ormat_::MVD_PIXEL_MONO_08; 
 
 
 
m_pIoImage.stImage.ImageData = matInputIm
g.ptr(0); 
 
 
} 
 
 
else if (CV_8UC3 == matInputImg.type()) 
 
 
{ 
 
 
 
cv::cvtColor(matInputImg, matInputImg, CV_BG
R2RGB); 
 
 
 
m_pIoImage.stImage.Width = matInputImg.col
s; 
 
 
 
m_pIoImage.stImage.Height = matInputImg.ro
ws; 
 
 
 
m_pIoImage.stImage.DataLen = dataLen; 
 
 
 
m_pIoImage.stImage.Pixelformat = _MvdPixelF
ormat_::MVD_PIXEL_RGB_RGB24_C3; 
 
 
 
m_pIoImage.stImage.ImageData = matInputIm
g.ptr(0); 



<!-- page 1249 -->
HIKROBOT 
 
1240 
 
 
 
 
} 
 
} 
 
catch (CVmException e) 
 
{ 
 
 
strReMsg.Format(_T("%x"), e.GetErrorCode()); 
 
 
strReMsg = _T("0x") + strReMsg + _T(" == SaveProc
edureToFile()"); 
 
} 
 
 
return m_pIoImage; 
} 
2 Mat 转图像源SDK 输入（ImageBaseData）、模块输出（ImageBaseData）  
ImageBaseData MatToImageBaseData(Mat matInputImg) 
{ 
 
if (matInputImg.empty()) 
 
{ 
 
 
throw IMVDException(MVD_MODUL_APP, MVD_E_PAR
AMETER_ILLEGAL); 
 
} 



<!-- page 1250 -->
HIKROBOT 
 
1241 
 
 
 
if ((CV_8UC1 != matInputImg.type()) && (CV_8UC3 != matInp
utImg.type())) 
 
{ 
 
 
throw IMVDException(MVD_MODUL_APP, MVD_E_SUP
PORT); 
 
} 
 
 
ImageBaseData  m_pImageBaseData{}; 
 
uint dataLen = (uint)(matInputImg.cols * matInputImg.rows * 
matInputImg.channels()); 
 
CString strReMsg = _T(""); 
 
try 
 
{ 
 
 
if (CV_8UC1 == matInputImg.type()) 
 
 
{ 
 
 
 
m_pImageBaseData.Width = matInputImg.cols; 
 
 
 
m_pImageBaseData.Height = matInputImg.row
s; 
 
 
 
m_pImageBaseData.DataLen = dataLen; 
 
 
 
m_pImageBaseData.Pixelformat = _MvdPixelFo
rmat_::MVD_PIXEL_MONO_08; 



<!-- page 1251 -->
HIKROBOT 
 
1242 
 
 
 
 
 
m_pImageBaseData.ImageData = matInputIm
g.ptr(0); 
 
 
} 
 
 
else if (CV_8UC3 == matInputImg.type()) 
 
 
{ 
 
 
 
cv::cvtColor(matInputImg, matInputImg, CV_BG
R2RGB); 
 
 
 
m_pImageBaseData.Width = matInputImg.cols; 
 
 
 
m_pImageBaseData.Height = matInputImg.row
s; 
 
 
 
m_pImageBaseData.DataLen = dataLen; 
 
 
 
m_pImageBaseData.Pixelformat = _MvdPixelFo
rmat_::MVD_PIXEL_RGB_RGB24_C3; 
 
 
 
m_pImageBaseData.ImageData = matInputIm
g.ptr(0); 
 
 
} 
 
} 
 
catch (CVmException e) 
 
{ 
 
 
strReMsg.Format(_T("%x"), e.GetErrorCode()); 



<!-- page 1252 -->
HIKROBOT 
 
1243 
 
 
 
 
strReMsg = _T("0x") + strReMsg + _T(" == SaveProc
edureToFile()"); 
 
} 
 
 
return m_pImageBaseData; 
} 
3 Mat 与算子图像（IMvdImage）互转  
void ConvertMat2MvdImage(IN Mat& stMatImg, INOUT IMvdImage* 
pMvdImg) 
{ 
    // 参数合法性判断 
    if(stMatImg.empty() || NULL == pMvdImg) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETE
R_ILLEGAL); 
    } 
 
    // 像素格式判断 
    if((CV_8UC1 != stMatImg.type()) && (CV_8UC3 !=stMatImg.type
())) 



<!-- page 1253 -->
HIKROBOT 
 
1244 
 
 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT); 
    } 
 
    int nImageWidth = stMatImg.size().width; 
    int nImageHeight = stMatImg.size().height; 
    int nChannelNum = stMatImg.channels(); 
    int nImageSize = stMatImg.size().width * stMatImg.size().height * 
nChannelNum; 
 
    // 根据传入的mat 图像初始化ImvdImage 
    if (CV_8UC1 == stMatImg.type()) 
    { 
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXE
L_MONO_08); 
    } 
    else if(CV_8UC3 == stMatImg.type()) 
    { 
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXE
L_RGB_RGB24_C3); 
    } 



<!-- page 1254 -->
HIKROBOT 
 
1245 
 
 
 
    unsigned char* pszMvdImgData = pMvdImg->GetImageData(0)
->pData; 
    if (stMatImg.isContinuous()) //  灰度图一定连续，彩色图不一定 
    { 
        uchar* pdata= stMatImg.ptr<uchar>(0); 
        memcpy(pszMvdImgData, pdata, nImageSize); 
    } 
    else //避免彩色图有裁剪等操作导致图像数据不连续问题 
    { 
        for(int i = 0; i< nImageHeight; i++)    // 逐行拷贝 
        { 
            uchar* pdata= stMatImg.ptr<uchar>(i); 
            memcpy(&pszMvdImgData[i * nImageWidth * nChannelN
um], pdata, nImageWidth * nChannelNum); 
        } 
    } 
 
    if(MVD_PIXEL_RGB_RGB24_C3 == pMvdImg->GetPixelFormat()) // 
交换R 和B 
    { 



<!-- page 1255 -->
HIKROBOT 
 
1246 
 
 
        uchar cTemp; 
        for(int i = 0; i < nImageWidth * nImageHeight; i++) 
        { 
            cTemp = pszMvdImgData[3 * i]; 
            pszMvdImgData[3 * i] = pszMvdImgData[3 * i + 2]; 
            pszMvdImgData[3 * i + 2] = cTemp; 
        } 
    } 
} 
 
void ConvertMvdImage2Mat(IN IMvdImage* pMvdImg, INOUT Mat* 
pMatImg) 
{ 
    // 参数合法性判断 
    if (NULL == pMvdImg || NULL == pMatImg) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETE
R_ILLEGAL); 
    } 
 
    // 像素格式判断 



<!-- page 1256 -->
HIKROBOT 
 
1247 
 
 
    MVD_PIXEL_FORMAT enSrcPixelFormat = pMvdImg->GetPixelFor
mat(); 
    if((MVD_PIXEL_MONO_08 != enSrcPixelFormat) && (MVD_PIXEL_R
GB_RGB24_C3 != enSrcPixelFormat)) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT); 
    } 
 
    int nImageWidth = pMvdImg->GetWidth(); 
    int nImageHeight = pMvdImg->GetHeight(); 
 
    // 根据传入的ImvdImage 图像初始化mat 
    if(MVD_PIXEL_MONO_08 == enSrcPixelFormat) 
    { 
        pMatImg->create(nImageHeight, nImageWidth, CV_8UC1); 
 
    } 
    if(MVD_PIXEL_RGB_RGB24_C3 == enSrcPixelFormat) 
    { 
        pMatImg->create(nImageHeight, nImageWidth, CV_8UC3); 
    } 



<!-- page 1257 -->
HIKROBOT 
 
1248 
 
 
    if(pMatImg->empty()) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_RESOURCE); 
    } 
 
    // 上述方式为mat 分配的内存一定是连续的 
    uchar* pdata= pMatImg->ptr<uchar>(0); 
    memcpy(pdata, pMvdImg->GetImageData(0)->pData, pMvdImg->
GetImageData(0)->nLen); 
    if(CV_8UC3 == pMatImg->type()) // 交换R 和B 
    { 
        uchar cTemp; 
        for(int i = 0; i < nImageWidth * nImageHeight; i++) 
        { 
            cTemp = pdata[3 * i]; 
            pdata[3 * i] = pdata[3 * i + 2]; 
            pdata[3 * i + 2] = cTemp; 
        } 
    } 
} 
4 流程输出（IoImage）转Mat 



<!-- page 1258 -->
HIKROBOT 
 
1249 
 
 
Mat IoImageToMat(IoImage m_pIoImage) 
{ 
 
Mat stMatImg; 
 
CString strReMsg = _T(""); 
 
try 
 
{ 
 
 
MvdPixelFormat srcPixelFormat = m_pIoImage.stImag
e.Pixelformat; 
 
 
if ((VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_MO
NO_08 != srcPixelFormat) && (VisionMasterSDK::MvdPixelFormat::MV
D_PIXEL_RGB_RGB24_C3 != srcPixelFormat)) 
 
 
{ 
 
 
 
throw CVmException(0xE0000503); 
 
 
} 
 
 
// 根据传入的IoImage 图像初始化mat 
 
 
if (VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_MON
O_08 == srcPixelFormat) 
 
 
{ 
 
 
 
stMatImg.create((int)m_pIoImage.stImage.Heig
ht, (int)m_pIoImage.stImage.Width, CV_8UC1); 
 
 
} 



<!-- page 1259 -->
HIKROBOT 
 
1250 
 
 
 
 
else if (VisionMasterSDK::MvdPixelFormat::MVD_PIXEL_
RGB_RGB24_C3 == srcPixelFormat) 
 
 
{ 
 
 
 
stMatImg.create((int)m_pIoImage.stImage.Heig
ht, (int)m_pIoImage.stImage.Width, CV_8UC3); 
 
 
} 
 
 
if (stMatImg.empty()) 
 
 
{ 
 
 
 
throw IMVDException(MVD_MODUL_APP, MV
D_E_RESOURCE); 
 
 
} 
 
 
// 上述方式为mat 分配的内存一定是连续的 
 
 
uchar* pdata = stMatImg.ptr<uchar>(0); 
 
 
memcpy(pdata, m_pIoImage.stImage.ImageData, m_pI
oImage.stImage.DataLen); 
 
 
if (CV_8UC3 == stMatImg.type()) 
 
 
{ 
 
 
 
cvtColor(stMatImg, stMatImg, CV_RGB2BGR); 
 
 
} 
 
} 
 
catch (CVmException e) 



<!-- page 1260 -->
HIKROBOT 
 
1251 
 
 
 
{ 
 
 
strReMsg.Format(_T("%x"), e.GetErrorCode()); 
 
 
strReMsg = _T("0x") + strReMsg + _T(" == SaveProc
edureToFile()"); 
 
} 
 
 
return stMatImg; 
} 
问题根因  
不熟悉Mat 转换为其它类型  
 
 



<!-- page 1261 -->
HIKROBOT 
 
1252 
 
 
3.11 Halcon 与流程输入、Group 输入、
图像源SDK 输入、模块输入、算子输入、
算子输出、流程输出  
描述  
环境：VM4.2 + VS2013 及以上  
现象：Halcon 转换成其他图像类型  
解答  
Halcon 图像转换为流程输入图像、Group 输入图像、图像源SDK 输入图像、模块输入图
像、算子输入图像，算子输出图像转Halcon 图像，流程输出图像转换为Halcon 图像。  
1 Halcon 图像转流程输入（IoImage）、Group 输入（IoImage）,HImageToImage
BaseData 函数的实现见“2 Halcon 图像转ImageBaseData“  
IoImage HImageToIoImage(HImage image) 
{ 
 
IoImage ioImage{}; 
 
ImageBaseData imageBaseData = HImageToImageBaseData(i
mage); 



<!-- page 1262 -->
HIKROBOT 
 
1253 
 
 
 
ioImage.stImage = imageBaseData; 
 
return ioImage; 
} 
2 Halcon 图像转图像源SDK 输入（ImageBaseData）、模块输入（ImageBaseDat
a）  
ImageBaseData HImageToImageBaseData(HImage image) 
{ 
 
ImageBaseData imageBaseData{}; 
 
//获取图像通道位深度信息 
 
HString bitdepth = image.GetChannelInfo("type", 1); 
 
assert(!strcmp(bitdepth.Text(), "byte")); 
 
int channels = image.CountChannels(); 
 
assert(channels == 1 || channels == 3); 
 
HString type; 
 
Hlong width, height; 
 
//单通道 
 
if (channels == 1) 
 
{ 
 
 
void* imagePtr = image.GetImagePointer1(&type, &w
idth, &height); 



<!-- page 1263 -->
HIKROBOT 
 
1254 
 
 
 
 
imageBaseData.DataLen = width * height; 
 
 
imageBaseData.Width = width; 
 
 
imageBaseData.Height = height; 
 
 
imageBaseData.Pixelformat = MvdPixelFormat::MVD_PI
XEL_MONO_08; 
 
 
imageBaseData.ImageData = imagePtr; 
 
} 
 
//3 通道 
 
if (channels == 3) 
 
{ 
 
 
void* imageRedPtr; 
 
 
void* imageGreenPtr; 
 
 
void* imageBluePtr; 
 
 
image.GetImagePointer3(&imageRedPtr, &imageGreen
Ptr, &imageBluePtr, &type, &width, &height); 
 
 
byte* imageRedBuf = new byte[width * height]; 
 
 
byte* imageGreenBuf = new byte[width * height]; 
 
 
byte* imageBlueBuf = new byte[width * height]; 
 
 
memcpy(imageRedBuf, imageRedPtr, width * height); 
 
 
memcpy(imageGreenBuf, imageGreenPtr, width * heig
ht); 



<!-- page 1264 -->
HIKROBOT 
 
1255 
 
 
 
 
memcpy(imageBlueBuf, imageBluePtr, width * height); 
 
 
byte* imageBuf = new byte[width * height * 3]; 
 
 
int index = 0; 
 
 
for (int row = 0; row < height; row++) 
 
 
{ 
 
 
 
for (int col = 0; col < width; col++, index +
= 3) 
 
 
 
{ 
 
 
 
 
imageBuf[index] = imageRedBuf[row *
 width + col]; 
 
 
 
 
imageBuf[index + 1] = imageGreenBuf
[row * width + col]; 
 
 
 
 
imageBuf[index + 2] = imageBlueBuf[r
ow * width + col]; 
 
 
 
} 
 
 
} 
 
 
delete[] imageRedBuf; 
 
 
delete[] imageGreenBuf; 
 
 
delete[] imageBlueBuf; 
 
 
imageBaseData.DataLen = width * height * 3; 
 
 
imageBaseData.Width = width; 



<!-- page 1265 -->
HIKROBOT 
 
1256 
 
 
 
 
imageBaseData.Height = height; 
 
 
imageBaseData.Pixelformat = MvdPixelFormat::MVD_PI
XEL_RGB_RGB24_C3; 
 
 
imageBaseData.ImageData = imageBuf; 
 
} 
 
return imageBaseData; 
} 
3 Halcon 图像与算子图像（IMvdImage）互转  
void ConvertHalcon2MvdImage(IN Hobject stHalconImg, INOUT IMvd
Image* pMvdImg) 
{ 
    // 判断输入是否合法 
    if (NULL == pMvdImg) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETE
R_ILLEGAL); 
    } 
 
    Herror stErr; 
    Hlong nChannelNum; 



<!-- page 1266 -->
HIKROBOT 
 
1257 
 
 
    stErr = count_channels(stHalconImg, &nChannelNum); 
    if(H_MSG_OK != stErr) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNOW,"
Failed to get channel num!"); 
    } 
    if(1 != nChannelNum && 3!= nChannelNum) 
    { 
        throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPORT); 
    } 
 
    Hlong nImageWidth = 0; 
    Hlong nImageHeight = 0; 
    char szType[128] = { 0 }; 
 
    // 获取图像信息 
    if(1 == nChannelNum) // 灰度图 
    { 
        unsigned char* pData; 
        stErr = get_image_pointer1(stHalconImg, (Hlong*)&pData, szT
ype, &nImageWidth, &nImageHeight); 



<!-- page 1267 -->
HIKROBOT 
 
1258 
 
 
        if(H_MSG_OK != stErr) 
        { 
            throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNO
W,"Failed to get image info!"); 
        } 
        if(strcmp("byte",szType)) 
        { 
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPO
RT,"Image type not supported!"); 
        } 
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXE
L_MONO_08); 
        unsigned char* pszMvdImgData = pMvdImg->GetImageData
(0)->pData; 
        memcpy(pszMvdImgData, pData, nImageWidth * nImageHeig
ht); 
    } 
    else if(3 == nChannelNum) // 彩色图(注意：位深为8 的图像不一定
是灰度图，也可能是伪彩图) 
    { 
        unsigned char* pRData; 



<!-- page 1268 -->
HIKROBOT 
 
1259 
 
 
        unsigned char* pGData; 
        unsigned char* pBData; 
 
        stErr = get_image_pointer3(stHalconImg, (Hlong*)&pRData, 
(Hlong*)&pGData, (Hlong*)&pBData, szType, &nImageWidth, &nImag
eHeight); 
        if(H_MSG_OK != stErr) 
        { 
            throw IMVDException(MVD_MODUL_APP, MVD_E_UNKNO
W,"Failed to get image info!"); 
        } 
        if(strcmp("byte",szType)) 
        { 
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPO
RT,"Image type not supported!"); 
        } 
        pMvdImg->InitImage(nImageWidth, nImageHeight, MVD_PIXE
L_RGB_RGB24_C3); 
 
        unsigned char* pszMvdImgData = pMvdImg->GetImageData
(0)->pData; 



<!-- page 1269 -->
HIKROBOT 
 
1260 
 
 
        for(unsigned int i = 0; i < nImageHeight; i++) 
        { 
            for(unsigned int j = 0; j < nImageWidth; j++) 
            { 
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 0] =
 pRData[i * nImageWidth + j]; 
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 1] =
 pGData[i * nImageWidth + j]; 
                pszMvdImgData[i * nImageWidth * 3 + j * 3 + 2] =
 pBData[i * nImageWidth + j]; 
            } 
        } 
    } 
} 
 
void ConvertMvdImage2Halcon(IN IMvdImage* pMvdImg, INOUT Ho
bject* pHObject) 
{ 
    // 传参合法性判断 
    if (NULL == pMvdImg || NULL == pHObject) 
    { 



<!-- page 1270 -->
HIKROBOT 
 
1261 
 
 
        throw IMVDException(MVD_MODUL_APP, MVD_E_PARAMETE
R_ILLEGAL); 
    } 
 
    Herror stErr; 
    unsigned char* pRData = NULL; 
    unsigned char* pGData = NULL; 
    unsigned char* pBData = NULL; 
    try 
    { 
        MVD_PIXEL_FORMAT enSrcPixelFormat = pMvdImg->GetPixel
Format(); 
        if((MVD_PIXEL_MONO_08 != enSrcPixelFormat) && (MVD_PIX
EL_RGB_RGB24_C3 != enSrcPixelFormat)) 
        { 
            throw IMVDException(MVD_MODUL_APP, MVD_E_SUPPO
RT); 
        } 
 
        int nImageWidth = pMvdImg->GetWidth(); 
        int nImageHeight = pMvdImg->GetHeight(); 



<!-- page 1271 -->
HIKROBOT 
 
1262 
 
 
 
        // 根据传入的MVDImage 图像初始化Halcon 图像 
        if(MVD_PIXEL_MONO_08 == enSrcPixelFormat) 
        { 
            // 直接引用MVDImage 图像数据的地址，进行新建Halcon 图
像;halcon 内部会对图像数据深拷贝 
            stErr = gen_image1(pHObject, "byte", nImageWidth, nIm
ageHeight, (Hlong)pMvdImg->GetImageData(0)->pData); 
            if(H_MSG_OK != stErr) 
            { 
                throw IMVDException(MVD_MODUL_APP, MVD_E_RES
OURCE,"Failed to create halcon image!"); 
            } 
        } 
        else if(MVD_PIXEL_RGB_RGB24_C3 == enSrcPixelFormat) 
        { 
            // MVDImage 图像是一个通道RGBRGBRGB...存放；需要另外
开辟块内存 
            int nChannelDataLen = nImageWidth *nImageHeight; 
            unsigned char* pszMvdImgData = pMvdImg->GetImage
Data(0)->pData; 



<!-- page 1272 -->
HIKROBOT 
 
1263 
 
 
 
            pRData = (unsigned char*)malloc(nChannelDataLen); 
            if(NULL == pRData) 
            { 
                throw IMVDException(MVD_MODUL_APP, MVD_E_RES
OURCE,"Failed to malloc buffer for image!"); 
            } 
            pGData = (unsigned char*)malloc(nChannelDataLen); 
            if(NULL == pGData) 
            { 
                throw IMVDException(MVD_MODUL_APP, MVD_E_RES
OURCE,"Failed to malloc buffer for image!"); 
            } 
            pBData = (unsigned char*)malloc(nChannelDataLen); 
            if(NULL == pBData) 
            { 
                throw IMVDException(MVD_MODUL_APP, MVD_E_RES
OURCE,"Failed to malloc buffer for image!"); 
            } 
 
            // 引用MVDImage 图像进行填充 



<!-- page 1273 -->
HIKROBOT 
 
1264 
 
 
            for(unsigned int i = 0; i < nImageHeight; i++) 
            { 
                for(unsigned int j = 0; j < nImageWidth; j++) 
                { 
                    pRData[i * nImageWidth + j] = pszMvdImgData
[i * nImageWidth * 3 + j * 3 + 0]; 
                    pGData[i * nImageWidth + j] = pszMvdImgData
[i * nImageWidth * 3 + j * 3 + 1]; 
                    pBData[i * nImageWidth + j] = pszMvdImgData
[i * nImageWidth * 3 + j * 3 + 2]; 
                } 
            } 
 
            // 创建Halcon 图像;halcon 内部会深拷贝图像数据 
            stErr = gen_image3(pHObject, "byte", nImageWidth, nIm
ageHeight, (Hlong)pRData, (Hlong)pGData, (Hlong)pBData); 
            if(H_MSG_OK != stErr) 
            { 
                throw IMVDException(MVD_MODUL_APP, MVD_E_RES
OURCE,"Failed to create halcon image!"); 
            } 



<!-- page 1274 -->
HIKROBOT 
 
1265 
 
 
 
            // halcon 图像创建时,图像数据进行了深拷贝，这里直接释放即
可 
            if(NULL != pRData) 
            { 
                free(pRData); 
                pRData = NULL; 
            } 
            if(NULL != pGData) 
            { 
                free(pGData); 
                pGData = NULL; 
            } 
            if(NULL != pBData) 
            { 
                free(pBData); 
                pBData = NULL; 
            } 
        } 
    } 
    catch (IMVDException &ex) 



<!-- page 1275 -->
HIKROBOT 
 
1266 
 
 
    { 
        if(NULL != pRData) 
        { 
            free(pRData); 
            pRData = NULL; 
        } 
        if(NULL != pGData) 
        { 
            free(pGData); 
            pGData = NULL; 
        } 
        if(NULL != pBData) 
        { 
            free(pBData); 
            pBData = NULL; 
        } 
        throw ex; 
    } 
} 
4 流程输出（IoImage）转Halcon 图像  



<!-- page 1276 -->
HIKROBOT 
 
1267 
 
 
HImage IoImageToHImage(IoImage ioImage) 
{ 
 
HImage image; 
 
if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXE
L_MONO_08) 
 
{ 
 
 
image.GenImage1("byte", ioImage.stImage.Width, ioIm
age.stImage.Height, ioImage.stImage.ImageData); 
 
} 
 
if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXE
L_RGB_RGB24_C3) 
 
{ 
 
 
int width = ioImage.stImage.Width; 
 
 
int height = ioImage.stImage.Height; 
 
 
long size = width * height * 3; 
 
 
byte* imageRedBuf = new byte[(long)width * height]; 
 
 
byte* imageGreenBuf = new byte[(long)width * heigh
t]; 
 
 
byte* imageBlueBuf = new byte[(long)width * height]; 
 
 
byte* imageBuffer = new byte[size]; 



<!-- page 1277 -->
HIKROBOT 
 
1268 
 
 
 
 
memcpy(imageBuffer, ioImage.stImage.ImageData, siz
e); 
 
 
int index = 0; 
 
 
for (int row = 0; row < height; row++) 
 
 
{ 
 
 
 
for (int col = 0; col < width; col++, index +
= 3) 
 
 
 
{ 
 
 
 
 
imageRedBuf[row * width + col] = im
ageBuffer[index]; 
 
 
 
 
imageGreenBuf[row * width + col] = i
mageBuffer[index + 1]; 
 
 
 
 
imageBlueBuf[row * width + col] = im
ageBuffer[index + 2]; 
 
 
 
} 
 
 
} 
 
 
delete[] imageBuffer; 
 
 
image.GenImage3("byte", width, height, imageRedBuf, 
imageGreenBuf, imageBlueBuf); 
 
} 
 
return image; 



<!-- page 1278 -->
HIKROBOT 
 
1269 
 
 
} 
问题根因  
不熟悉Halcon 图像转换为其它类型  
 
 



<!-- page 1279 -->
HIKROBOT 
 
1270 
 
 
3.12 流程图像与算子图像互转  
描述  
环境：VM4.2 + VS2013 及以上  
现象：流程图像与算子图像互转  
解答  
VM SDK 开发中流程输入输出图像都是IoImage，算子SDK 开发中算子输入输出图像都
是ImvdImage，两者可以实现互转。  
1 流程图像转算子图像  
IMvdImage* ImageConvert::IoImageToIMvdImage(IoImage ioImage) 
{ 
 
// TODO: 在此处添加实现代码. 
 
IMvdImage* iMvdImage = NULL; 
 
MVD_IMAGE_DATA_INFO stImageData{ }; 
 
 
if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD_PIXE
L_MONO_08) 
 
{ 



<!-- page 1280 -->
HIKROBOT 
 
1271 
 
 
 
 
stImageData.stDataChannel[0].nRowStep = ioImage.stI
mage.Width; 
 
 
stImageData.stDataChannel[0].nLen = ioImage.stImag
e.DataLen; 
 
 
stImageData.stDataChannel[0].nSize = ioImage.stImag
e.DataLen; 
 
 
stImageData.stDataChannel[0].pData = (unsigned char
*)ioImage.stImage.ImageData; 
 
 
iMvdImage->InitImage(ioImage.stImage.Width, ioImag
e.stImage.Height, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_
MONO_08, stImageData); 
 
} 
 
else if (ioImage.stImage.Pixelformat == MvdPixelFormat::MVD
_PIXEL_RGB_RGB24_C3) 
 
{ 
 
 
stImageData.stDataChannel[0].nRowStep = ioImage.stI
mage.Width*3; 
 
 
stImageData.stDataChannel[0].nLen = ioImage.stImag
e.DataLen; 
 
 
stImageData.stDataChannel[0].nSize = ioImage.stImag
e.DataLen; 



<!-- page 1281 -->
HIKROBOT 
 
1272 
 
 
 
 
stImageData.stDataChannel[0].pData = (unsigned char
*)ioImage.stImage.ImageData; 
 
 
iMvdImage->InitImage(ioImage.stImage.Width, ioImag
e.stImage.Height, VisionDesigner::_MVD_PIXEL_FORMAT_::MVD_PIXEL_
BGR_BGR24_C3, stImageData); 
 
} 
 
 
return iMvdImage; 
} 
2 算子图像转流程图像  
IoImage ImageConvert::IMvdImageToIoImage(IMvdImage* iMvdImag
e) 
{ 
 
// TODO: 在此处添加实现代码. 
 
IoImage ioImage{}; 
 
 
ioImage.stImage.Width = iMvdImage->GetWidth(); 
 
ioImage.stImage.Height = iMvdImage->GetHeight(); 
 
 



<!-- page 1282 -->
HIKROBOT 
 
1273 
 
 
 
ioImage.stImage.ImageData = iMvdImage->GetImageData(0)
->pData;//图像数据内存地址是连续的 
 
if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMAT::M
VD_PIXEL_MONO_08) 
 
{ 
 
 
ioImage.stImage.DataLen = iMvdImage->GetImageDat
a(0)->nLen; 
 
 
ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_
PIXEL_MONO_08; 
 
} 
 
else if (iMvdImage->GetPixelFormat() == MVD_PIXEL_FORMA
T::MVD_PIXEL_BGR_BGR24_C3) 
 
{ 
 
 
ioImage.stImage.Pixelformat = MvdPixelFormat::MVD_
PIXEL_RGB_RGB24_C3; 
 
} 
 
return ioImage; 
} 
问题根因  
不熟悉流程图像与算子图像互转  



<!-- page 1283 -->
HIKROBOT 
 
1274 
 
 
 
 



<!-- page 1284 -->
HIKROBOT 
 
1275 
 
 
3.13 算法模块图像与Mat、Halcon、算子
图像互转的方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：算法模块图像转换成其它类型  
解答  
算法模块图像与Mat、Halcon 图像、算子图像实现互转，自定义算法模块开发时，在C+
+工程中，算法的图像类型为HKA_IMAGE。  
1 HKA_IMAGE 与Mat 互转  
 
Mat CAlgorithmModule::HKAImageToMat(HKA_IMAGE inputimage) 
{ 
    Mat mat, mat1; 
    if (inputimage.format == HKA_IMG_MONO_08) 
    { 
        mat = Mat(inputimage.height, inputimage.width, CV_8UC1, in
putimage.data[0]); 



<!-- page 1285 -->
HIKROBOT 
 
1276 
 
 
    } 
    else if (inputimage.format == HKA_IMG_RGB_RGB24_C3) 
    { 
        mat1 = Mat(inputimage.height, inputimage.width, CV_8UC3, i
nputimage.data[0]); 
        cvtColor(mat1, mat, COLOR_RGB2BGR); 
    } 
    return mat; 
} 
 
 
 
HKA_IMAGE CAlgorithmModule::MatToHKAImage(Mat mat) 
{ 
 
 
HKA_IMAGE inputimage; 
 
if (mat.channels() == 1) 
 
{ 
 
 
inputimage = { HKA_IMG_MONO_08, 0 }; 
 
 
inputimage.width = mat.cols; 
 
 
inputimage.height = mat.rows; 
 
 
inputimage.format = HKA_IMG_MONO_08; 



<!-- page 1286 -->
HIKROBOT 
 
1277 
 
 
 
 
inputimage.step[0] = mat.cols; 
 
 
inputimage.data[0] = (char*)malloc(inputimage.width *
 inputimage.height); 
 
 
if (inputimage.data[0] != NULL) 
 
 
{ 
 
 
 
memset(inputimage.data[0], 0, inputimage.widt
h * inputimage.height); 
 
 
 
memcpy_s(inputimage.data[0], inputimage.widt
h * inputimage.height, mat.data, inputimage.width * inputimage.heig
ht); 
 
 
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



<!-- page 1287 -->
HIKROBOT 
 
1278 
 
 
 
 
inputimage.data[0] = (char*)malloc(inputimage.width *
 inputimage.height * 3); 
 
 
if (inputimage.data[0] != NULL) 
 
 
{ 
 
 
 
memset(inputimage.data[0], 0, inputimage.widt
h * inputimage.height * 3); 
 
 
 
memcpy_s(inputimage.data[0], inputimage.widt
h * inputimage.height * 3, mat.data, inputimage.width * inputimage.
height * 3); 
 
 
} 
 
} 
 
return inputimage; 
} 
2 HKA_IMAGE 与Halcon 图像互转  
HImage CAlgorithmModule::HKAImageToHImage(HKA_IMAGE inputim
age) 
{ 
 
HImage himage; 
 
if (HKA_IMG_MONO_08 == inputimage.format) 
 
{ 



<!-- page 1288 -->
HIKROBOT 
 
1279 
 
 
 
 
himage.GenImage1("byte", inputimage.width, inputima
ge.height, inputimage.data[0]); 
 
} 
 
if (HKA_IMG_RGB_RGB24_C3 == inputimage.format) 
 
{ 
 
 
int width = inputimage.width; 
 
 
int height = inputimage.height; 
 
 
long size = width * height * 3; 
 
 
byte* imageRedBuf = new byte[(long)width * height]; 
 
 
byte* imageGreenBuf = new byte[(long)width * heigh
t]; 
 
 
byte* imageBlueBuf = new byte[(long)width * height]; 
 
 
byte* imageBuffer = new byte[size]; 
 
 
memcpy(imageBuffer, inputimage.data[0], size); 
 
 
int index = 0; 
 
 
for (int row = 0; row < height; row++) 
 
 
{ 
 
 
 
for (int col = 0; col < width; col++, index +
= 3) 
 
 
 
{ 



<!-- page 1289 -->
HIKROBOT 
 
1280 
 
 
 
 
 
 
imageRedBuf[row * width + col] = im
ageBuffer[index]; 
 
 
 
 
imageGreenBuf[row * width + col] = i
mageBuffer[index + 1]; 
 
 
 
 
imageBlueBuf[row * width + col] = im
ageBuffer[index + 2]; 
 
 
 
} 
 
 
} 
 
 
delete[] imageBuffer; 
 
 
himage.GenImage3("byte", width, height, imageRedBu
f, imageGreenBuf, imageBlueBuf); 
 
} 
 
return himage; 
} 
 
 
HKA_IMAGE CAlgorithmModule::HImageToHKAIMAGE(HImage himag
e) 
{ 
 
HKA_IMAGE inputimage; 
 
HString type; 



<!-- page 1290 -->
HIKROBOT 
 
1281 
 
 
 
Hlong width, height; 
 
if (himage.CountChannels() == 1) 
 
{ 
 
 
inputimage = { HKA_IMG_MONO_08, 0 }; 
 
 
void* imagePtr = himage.GetImagePointer1(&type, &
width, &height); 
 
 
inputimage.width = width; 
 
 
inputimage.height = height; 
 
 
inputimage.format = HKA_IMG_MONO_08; 
 
 
inputimage.step[0] = width; 
 
 
inputimage.data[0] = (char*)malloc(inputimage.width *
 inputimage.height); 
 
 
if (inputimage.data[0] != NULL) 
 
 
{ 
 
 
 
memset(inputimage.data[0], 0, inputimage.widt
h * inputimage.height); 
 
 
 
memcpy_s(inputimage.data[0], inputimage.widt
h * inputimage.height, imagePtr, inputimage.width * inputimage.heig
ht); 
 
 
} 
 
} 



<!-- page 1291 -->
HIKROBOT 
 
1282 
 
 
 
else if (himage.CountChannels() == 3) 
 
{ 
 
 
inputimage = { HKA_IMG_RGB_RGB24_C3, 0 }; 
 
 
void* imageRedPtr; 
 
 
void* imageGreenPtr; 
 
 
void* imageBluePtr; 
 
 
himage.GetImagePointer3(&imageRedPtr, &imageGree
nPtr, &imageBluePtr, &type, &width, &height); 
 
 
 
 
long size = width * height * 3; 
 
 
byte* imageRedBuf = new byte[width * height]; 
 
 
byte* imageGreenBuf = new byte[width * height]; 
 
 
byte* imageBlueBuf = new byte[width * height]; 
 
 
memcpy_s(imageRedBuf, imageRedPtr, width * heigh
t); 
 
 
memcpy_s(imageGreenBuf, imageGreenPtr, width * he
ight); 
 
 
memcpy_s(imageBlueBuf, imageBluePtr, width * heigh
t); 
 
 
byte* imageBuffer = new byte[size]; 
 
 
int index = 0; 
 
 
for (int row = 0; row < height; row++) 



<!-- page 1292 -->
HIKROBOT 
 
1283 
 
 
 
 
{ 
 
 
 
for (int col = 0; col < width; col++, index +
= 3) 
 
 
 
{ 
 
 
 
 
imageBuffer[index] = imageRedBuf[ro
w * width + col]; 
 
 
 
 
imageBuffer[index + 1] = imageGreen
Buf[row * width + col]; 
 
 
 
 
imageBuffer[index + 2] = imageBlueB
uf[row * width + col]; 
 
 
 
} 
 
 
} 
 
 
delete[] imageRedBuf; 
 
 
delete[] imageGreenBuf; 
 
 
delete[] imageBlueBuf; 
 
 
inputimage.width = width; 
 
 
inputimage.height = height; 
 
 
inputimage.format = HKA_IMG_RGB_RGB24_C3; 
 
 
inputimage.step[0] = width * 3; 
 
 
inputimage.data[0] = (char*)malloc(inputimage.width *
 inputimage.height * 3); 



<!-- page 1293 -->
HIKROBOT 
 
1284 
 
 
 
 
if (inputimage.data[0] != NULL) 
 
 
{ 
 
 
 
memset(inputimage.data[0], 0, inputimage.widt
h * inputimage.height * 3); 
 
 
 
memcpy_s(inputimage.data[0], inputimage.widt
h * inputimage.height * 3, imageBuffer, inputimage.width * inputima
ge.height * 3); 
 
 
} 
 
 
delete[] imageBuffer;       
 
} 
 
return inputimage; 
} 
 
3 HKA_IMAGE 与算子图像（ImvdImage）互转  
 
IMvdImage* CAlgorithmModule::HKAImageToIMvdImage(HKA_IMAGE 
inputimage) 
{ 
    IMvdImage* iMvdImage = NULL; 
    CreateImageInstance(&iMvdImage); 



<!-- page 1294 -->
HIKROBOT 
 
1285 
 
 
    MVD_IMAGE_DATA_INFO stImageData; 
 
    if (inputimage.format == HKA_IMG_MONO_08) 
    { 
        uint dataLen = (uint)(inputimage.width * inputimage.height); 
        stImageData.stDataChannel[0].nRowStep = inputimage.width; 
        stImageData.stDataChannel[0].nLen = dataLen; 
        stImageData.stDataChannel[0].nSize = dataLen; 
        stImageData.stDataChannel[0].pData = (unsigned char*)mallo
c(inputimage.width * inputimage.height); 
        memset(stImageData.stDataChannel[0].pData, 0, inputimage.w
idth * inputimage.height); 
        stImageData.stDataChannel[0].pData = (unsigned char*)inputi
mage.data[0]; 
        iMvdImage->InitImage(inputimage.width, inputimage.height, 
MVD_PIXEL_MONO_08, stImageData); 
    } 
    else if (inputimage.format == HKA_IMG_RGB_RGB24_C3) 
    { 
        uint dataLen = (uint)(inputimage.width * inputimage.height *
 3); 



<!-- page 1295 -->
HIKROBOT 
 
1286 
 
 
        stImageData.stDataChannel[0].nRowStep = inputimage.width 
* 3; 
        stImageData.stDataChannel[0].nLen = dataLen; 
        stImageData.stDataChannel[0].nSize = dataLen; 
        stImageData.stDataChannel[0].pData = (unsigned char*)mallo
c(inputimage.width * inputimage.height * 3); 
        memset(stImageData.stDataChannel[0].pData, 0, inputimage.w
idth * inputimage.height); 
        stImageData.stDataChannel[0].pData = (unsigned char*)inputi
mage.data[0]; 
        iMvdImage->InitImage(inputimage.width, inputimage.height, 
MVD_PIXEL_RGB_RGB24_C3, stImageData); 
 
    } 
    return iMvdImage; 
} 
 
 
HKA_IMAGE CAlgorithmModule::IMvdImageToHKA_IMAGE(IMvdImage
* iMvdImage) 
{ 



<!-- page 1296 -->
HIKROBOT 
 
1287 
 
 
    HKA_IMAGE inputimage; 
    if (iMvdImage->GetPixelFormat() == MVD_PIXEL_MONO_08) 
    { 
        inputimage = { HKA_IMG_MONO_08, 0 }; 
        inputimage.width = iMvdImage->GetWidth(); 
        inputimage.height = iMvdImage->GetHeight(); 
        inputimage.format = HKA_IMG_MONO_08; 
        inputimage.step[0] = iMvdImage->GetWidth(); 
        inputimage.data[0] = (char*)malloc(inputimage.width * inputi
mage.height); 
        if (inputimage.data[0] != NULL) 
        { 
            memset(inputimage.data[0], 0, inputimage.width * inputi
mage.height); 
            memcpy_s(inputimage.data[0], inputimage.width * inputi
mage.height, iMvdImage->GetImageData()->stDataChannel[0].pData, i
nputimage.width * inputimage.height); 
        } 
    } 
    else if (iMvdImage->GetPixelFormat() == MVD_PIXEL_RGB_RGB24
_C3) 



<!-- page 1297 -->
HIKROBOT 
 
1288 
 
 
    { 
        inputimage = { HKA_IMG_RGB_RGB24_C3, 0 }; 
        inputimage.width = iMvdImage->GetWidth(); 
        inputimage.height = iMvdImage->GetHeight(); 
        inputimage.format = HKA_IMG_RGB_RGB24_C3; 
        inputimage.step[0] = iMvdImage->GetWidth() * 3; 
        inputimage.data[0] = (char*)malloc(inputimage.width * inputi
mage.height * 3); 
        if (inputimage.data[0] != NULL) 
        { 
            memset(inputimage.data[0], 0, inputimage.width * inputi
mage.height * 3); 
            memcpy_s(inputimage.data[0], inputimage.width * inputi
mage.height * 3, iMvdImage->GetImageData()->stDataChannel[0].pDa
ta, inputimage.width * inputimage.height * 3); 
        } 
    } 
    return inputimage; 
} 
问题根因  


