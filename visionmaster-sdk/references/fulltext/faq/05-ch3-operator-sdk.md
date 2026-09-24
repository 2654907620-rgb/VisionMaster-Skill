# 第3章 算子SDK开发（公共工具/模块工具/控件嵌入）
<!-- pages 598-702 -->

<!-- page 598 -->
HIKROBOT 
 
589 
 
 
 
}; 
然后用户程序在主窗口类中，创建一个MyProcedureEvent 实例，如下： 
 
MyProcedureEvent myProcedureEvent; 
例如：我们要注册流程1 的结果回调，只需要在流程1 加载完成的地方插入代码，调用注
册回调的接口，典型的代码如下： 
 
IVmSolution* vmSolution = LoadSolution(solPath, ""); 
IVmProcedure* vmProcedure = (IVmProcedure*)((*vmSolution)["流程1
"]); 
vmProcedure->RegisterCallBackEvent((IVmProcedureEvent*)&myProce
dureEvent,this); 
剩下就是用户在MyProcedureEvent 类中，实现OnWorkEndStatusCallBack 方法即
可，比如在OnWorkEndStatusCallBack 中获取流程1 的运行结果，代码如下： 
 
vector matchX; 
vector matchY; 



<!-- page 599 -->
HIKROBOT 
 
590 
 
 
vector matchR; 
 
void MyProcedureEvent::OnWorkEndStatusCallBack(IN const IMVS_PF_
MODULE_WORK_STAUS * const pstWorkStatus, IN void * const pUse
r) 
{ 
 
try 
 
{ 
 
 
CMFCVM42DemoDlg* pDlg = (CMFCVM42DemoDlg*)
pUser; 
 
 
ObjectList list = pDlg->m_pSolution->GetAllProcedure
Objects();  //获取当前方案的所有流程 
 
 
IVmProcedure* procedure1 = (IVmProcedure*)(list.pO
bjects[0]);   //获取第一个流程 
 
 
//获取配置的matchX,matchY,matchR 输出 
 
 
FloatDataArray matchXArray = procedure1->GetResult
()->GetOutputFloat("matchX"); 
 
 
FloatDataArray matchYArray = procedure1->GetResult
()->GetOutputFloat("matchY"); 
 
 
FloatDataArray matchRArray = procedure1->GetResult
()->GetOutputFloat("matchR"); 



<!-- page 600 -->
HIKROBOT 
 
591 
 
 
 
 
 
 
 
for (int i = 0; i < matchXArray.nValueNum; i++) 
 
 
{ 
 
 
 
matchX.push_back(matchXArray.pFloatVal[i]); 
 
 
 
matchY.push_back(matchYArray.pFloatVal[i]); 
 
 
 
matchR.push_back(matchRArray.pFloatVal[i]); 
 
 
} 
 
} 
 
catch (CVmException ex) 
 
{ 
 
 
throw CVmException(ex); 
 
} 
} 
问题根因 
不熟悉流程相关回调函。  



<!-- page 601 -->
HIKROBOT 
 
592 
 
 
2.5 全工具类 
2.5.1 全局相机：获取全局相机列表和设置
相机参数的方法  
描述 
环境：VM4.2 + VS2013 及以上  
问题：问题1：如何获取方案中所有的全局相机的连接状态，如下图所示：  
 
如何在流程运行时监控全局相机1 和全局相机2 的连接状态？  
问题2：如何设置全局相机的基本参数，例如设置全局相机1 的曝光和增益？  
解答 
问题1 的解答： 



<!-- page 602 -->
HIKROBOT 
 
593 
 
 
在4.2.1 中，VM SDK 增加了获取相机连接状态的API，在GlobalCameraTool 类中，方
法bIsCameraConnect( )可以获取相机的连接状态。如果要监控方案中所有全局相机模块
的连接状态可以参考下面的代码：  
在程序初始化时，启动监控线程，如下：  
 
C# 
//获取流程中所有全局相机模块 
List<GlobalCameraModuleTool> glCameralist = new List<GlobalCame
raModuleTool>(); 
List<VmModule> vmModules = new List<VmModule>(); 
VmSolution.Instance.GetAllModule(vmModules); 
foreach(VmModule module in vmModules) 
{ 
    if(module.GetType()==typeof(GlobalCameraModuleTool)) 
    { 
        glCameralist.Add((GlobalCameraModuleTool) module); 
    } 
} 
//启动全局相机连接状态监控线程 



<!-- page 603 -->
HIKROBOT 
 
594 
 
 
Thread watchThread = new Thread(new ParameterizedThreadStart(Ca
meraConnectionWatchDog)); 
watchThread.IsBackground = true; 
watchThread.Start(glCameralist); 
监控相机连接状态的线程函数，如下：  
 
C# 
public void CameraConnectionWatchDog(object obj) 
{ 
    List<GlobalCameraModuleTool> globalCameraToolList = (List<Gl
obalCameraModuleTool>)obj; 
    bool[] isCameraConected = new bool[globalCameraToolList.Coun
t]; 
    while (true) 
    { 
        try 
        { 
            //获取流程中所有已配置的连接状态 
            foreach (var cameraTool in globalCameraToolList) 
            { 



<!-- page 604 -->
HIKROBOT 
 
595 
 
 
 
 



<!-- page 605 -->
HIKROBOT 
 
596 
 
 
                if (cameraTool.bIsCameraConnect() == false) 
                { 
                    Debug.WriteLine(string.Format($"警告: {cameraToo
l.Name} 已经离线！")); 
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
问题2 的解答：  
全局相机参数设置，通过调用GlobalCameraParam 这个类的方法和属性就可以做到。  
例如设置全局相机1 的曝光和增益，代码如下：  
 



<!-- page 606 -->
HIKROBOT 
 
597 
 
 
GlobalCameraModuleTool cameraModuleTool = VmSolution.Instance
["全局相机1"] as GlobalCameraModuleTool; 
GlobalCameraParam globalCameraParam = cameraModuleTool.Modu
Params; 
globalCameraParam.ExposureTime = 5000; 
globalCameraParam.Gain = 5.0; 
需要注意的地方：全局相机模块在VM SDK 中使用，如果没有使用添加引用的工具，可
以手动添加GlobalCameraModuleCs.dll 引用，并将引用属性的“复制到本地”选项设
置为False, 然后在程序代码文件中，添加命名空间的引用：using GlobalCameraModu
leCs; 
问题根因  
不了解VM SDK 中全局相机模块的使用  
不知道如何访问全局相机模块的方法和属性  
 
 



<!-- page 607 -->
HIKROBOT 
 
598 
 
 
VM 4.x （算子SDK 和算法模块开发） 
第3 章 算子SDK 开发 
3.1 环境配置类 
3.1.1 环境配置：CSharp 算子SDK 开发
环境配置方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：WinForm 下的算子SDK 开发环境配置方法  
解答  
WinForm 下进行算子SDK 开发的环境配置分为三步  
第一步，使用VS 新建一个窗体类项目  
第二步，为该项目添加算子的dll 引用，将该路径C:\Program Files (x86)\MVDAlgorith
mSDK\ReferencedAssemblies\Algorithms 下的所有dll 文件添加到项目中，将该路径
C:\Program Files (x86)\MVDAlgorithmSDK\ReferencedAssemblies\ 



<!-- page 608 -->
HIKROBOT 
 
599 
 
 
Common 下的引用除了第一个和第二个其他全部引用都加到项目中，第一个和第二个不
能添加，否则引用会报错。  
第三步，此时，我们会在工具箱内看到一些封装好的控件，将这些控件拉到窗体上生成并
启动即可。注意，所有的控件都在C:\Program Files (x86)\MVDAlgorithmSDK 
\ReferencedAssemblies\Control 文件夹下的，只有一个控件在Common 文件夹下，这
个控件叫MvRenderActiveX.Net.dll，是一个图形处理的渲染控件，大家需要单独将这个
控件添加到工具箱中。  
第一步 
 
第二步  



<!-- page 609 -->
HIKROBOT 
 
600 
 
 
 



<!-- page 610 -->
HIKROBOT 
 
601 
 
 
 
第三步  
 
问题原因  
缺少引用或者缺少控件  
 
 



<!-- page 611 -->
HIKROBOT 
 
602 
 
 
3.1.2 算子封装：使用C++封装算子SDK
的方法  
描述  
环境：MVDAlgrithm SDK 3.4 及以上 + VS2013 及以上  
问题：有的用户在使用算子SDK 开发时，为了使各个算法模块更加的统一和抽象，将不同
的算子工具抽象出共同的接口，例如：  
初始化-Initialize，  
加载配置-LoadConfiguration，  
训练模型-Trian，  
加载模型-LoadModel，  
执行算法-Run。  
解答  
我们的算子SDK 已经是封装程度比较高的了，算子工具的程序调用是完全面向对象的，通
过操作对象的方法和属性就能实现特定的算法流程，可能有些客户需要对算子做进一步的
抽象，将算子工具的内部属性的赋值，参数的保存与加载，模型的加载与保存，结果的获
取都抽象为共同的几个接口函数，如上描述的那样。使用C++是很容易做到的，使用虚函



<!-- page 612 -->
HIKROBOT 
 
603 
 
 
数将上面提到的提到的几个接口抽象，然后在具体的类中实现接口即可。我们用代码来说
明，如下：  
 
C++ 
class IVisionTool 
{ 
public: 
    IVisionTool() = default; 
    virtual ~IVisionTool() = default; 
 
    //使用参数文件初始化配置 
    virtual int Initilize(std::string& paramFilePath = "") = 0; 
 
    //导入数据，数据可以是训练好的模型文件、标定文件、参数配置文件等
等 
    virtual int ImportData(int &fileType,const std::string &inputPath) 
= 0; 
 
    //导出数据，数据可以是训练的模型文件、标定文件、参数配置文件等等 
    virtual int ExportData(int &fileType,const std::string &inputPath) 
= 0; 



<!-- page 613 -->
HIKROBOT 
 
604 
 
 
 
    //训练模型 
    virtual int Train(IMVdImage& image,IMvdShape* roi,IMvdShape* 
mask) = 0; 
 
    //执行算法工具 
virtual int Run(IMVdImage &image,IMvdShape* roi,IMvdShape* mask
[],int maskCount) = 0; 
//获取算法工具运行结果 
   virtual int GetResult(AlgToolResult &result) = 0; 
}; 
接着，我们通过具体的算法工具类，实现一个特定的算法工具，以直线查找工具为例，我
们可以设计一个LineFindTool 继承IVisionTool, 代码如下：  
 
C++ 
class FindLineTool:public IVisionTool 
{ 
public: 
 
FindLineTool(); 
 
~FindLineTool(); 



<!-- page 614 -->
HIKROBOT 
 
605 
 
 
 
int Initilize(const std::string& paramFilePath = "") override; 
 
int ImportData(const int &fileType,const std::string &inputPat
h) override; 
 
int ExportData(const int &fileType,const std::string &inputPat
h) override; 
 
int Train(const IMVdImage& image,IMvdShape* roi,IMvdShap
e* mask) override; 
 
int Run(const IMVdImage &image,IMvdShape* roi,IMvdShape
* mask[],int maskCount) override; 
 
int GetResult(AlgToolResult &result) override; 
private: 
 
ILineFindTool* pLineFindTool; 
}; 
这里篇幅所限，就不将FindLineTool 的所有接口全部实现罗列在这里了，这里将重要的
构造函数，析构函数，Initialize 和Run 方法实现罗列出来，代码如下：  
 
C++ 
//构造函数 
FindLineTool::FindLineTool() 
{ 



<!-- page 615 -->
HIKROBOT 
 
606 
 
 
 
try 
 
{ 
 
 
int nRet = CreateLineFindToolInstance(&pLineFindToo
l); 
 
 
if (nRet != 0) 
 
 
{ 
 
 
 
throw std::exception("Create FindLineTool inst
ance failed"); 
 
 
} 
 
} 
 
catch (IMVDException& ex) 
 
{ 
 
 
throw std::exception(ex); 
 
} 
 
} 
//析构函数 
FindLineTool::~FindLineTool() 
{ 
    if (pLineFindTool != nullptr) 
    { 



<!-- page 616 -->
HIKROBOT 
 
607 
 
 
        DestroyLineFindToolInstance(pLineFindTool); 
    } 
} 
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



<!-- page 617 -->
HIKROBOT 
 
608 
 
 
 
    } 
    catch (IMVDException&ex) 
 
{ 
        if (paramBuffer != nullptr) 
            delete[] paramBuffer; 
        return ex.GetErrorCode(); 
    } 
} 
//运行一次 
int Run(const IMVdImage &image, IMvdShape* roi, IMvdShape* mas
k[], int maskCount) 
{ 
    try 
    { 
        //1.设置输入图像 
        pLineFindTool->SetInputImage(image); 
        //2.设置ROI 
        pLineFindTool->SetROI(roi); 
        //3.设置屏蔽区 
        //设置屏蔽区之前先移除vMaskShapes 所有元素 



<!-- page 618 -->
HIKROBOT 
 
609 
 
 
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
需要注意的地方：算子SDK 大部分输入都是指针，因此一定要记得释放指针占用的内
存，否则会内存泄漏，上面的例子中，指针的释放放在了调用层，由调用者负责释放，因
此调用的时候，记得在调用结束后释放作为函数参数传入的IMvdImage*,IMvdShape
*等指针所占用的内存，需要显式调用DestroyImageInstance,DestroyShapeInsta
nce 等API 函数。  
问题根因  



<!-- page 619 -->
HIKROBOT 
 
610 
 
 
不了解C++ 中虚函数的用法  
不熟悉算子SDK 的常用接口函数  
 
 



<!-- page 620 -->
HIKROBOT 
 
611 
 
 
3.1.3 异常中断：算子SDK 软件运行报错
“托管调试助手”中断的解决方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：运行算子SDK 软件Demo 时，Visual Studio 软件出现“托管调试助手”中断。  
解答  
运行算子SDK 软件Demo 时，Visual Studio 软件出现“托管调试助手”中断，如下图
所示。  
 



<!-- page 621 -->
HIKROBOT 
 
612 
 
 
解决办法：打开异常设置，取消勾选【ContextSwitchDeadlock】和【DisconnectedCo
ntext】。  
 
问题根因  
不熟悉Visual Studio 软件的异常设置。  
 
 



<!-- page 622 -->
HIKROBOT 
 
613 
 
 
3.1.4 深度学习：GPU 运行深度学习算子引
发StackOverFlow 异常的方法 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上 
现象：深度学习算子运行报StackOverFlow 异常，如何解决？ 
  
解答 
第一步，深度学习算子需要在×64 平台下运行，检查平台是否为×64，win32 则需改为x6
4； 
第二步，第一步修改后仍然报StackOvreFlow 异常，则需调大堆栈提交大小； 



<!-- page 623 -->
HIKROBOT 
 
614 
 
 
 
 
问题根因 
不熟悉内存环境配置。 
 
 



<!-- page 624 -->
HIKROBOT 
 
615 
 
 
3.2 公用工具类 
3.2.1 图像载入：本地图像的载入方法 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上 
现象：彩色图像如何载入？ 
解答 
示例代码如下： 
一、彩色图像的载入 
1. C# 
2.   
3. CMvdImage cMvdImage = new CMvdImage(); 
4. cMvdImage.InitImage(ImagePathStr,MVD_PIXEL_FORMAT.MVD_P
IXEL_RGB_RGB24_C3); 
二、灰度图像的载入 
1. C# 
2.   



<!-- page 625 -->
HIKROBOT 
 
616 
 
 
3. CMvdImage cMvdImage = new CMvdImage(); 
4. cMvdImage.InitImage(ImagePathStr,MVD_PIXEL_FORMAT.MVD_P
IXELMONO_08); 
问题根因 
不熟悉彩色图像的像素格式。  
提示 
 
如果原图像素格式为BGR，需要转换通道灰度值，再调用上述像素格式。其它接口，例如
MVD_PIXEL_RGB_BGR24_C3 等不可使用。 
 
 



<!-- page 626 -->
HIKROBOT 
 
617 
 
 
3.2.2 相机取流：相机SDK 取流的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：如何使用相机SDK 取流？  
解答  
可以通过调用相机SDK 来实现相机取流。  
1.截取相机帧数据。示例代码如下。  
1. C# 
2. //相机相关变量 
3. private VisionDesigner.Camera.CCameraTool m_cMyCameraTool
Obj = null; 
4.   
5. /// <summary> 
6. /// 打开相机并开始取图 
7. /// </summary> 
8. public int OpenCamera(int cameraindex = 0) 
9. { 



<!-- page 627 -->
HIKROBOT 
 
618 
 
 
10.     try 
11.     { 
12.         //DeviceListAcq();//获取相机列表方法 
13.         //创建相机算子实例 
14.         if (null == m_cMyCameraToolObj) 
15.         { 
16.             m_cMyCameraToolObj = new VisionDesigner.Came
ra.CCameraTool(); 
17.             if (null == m_cMyCameraToolObj) 
18.             { 
19.                 return -1; 
20.             } 
21.         } 
22.         //设置连续采集模式 
23.         m_cMyCameraToolObj.SelectDevice(cameraindex);//默认
选择索引为0 的相机 
24.         m_cMyCameraToolObj.OpenDevice(); 
25.         m_cMyCameraToolObj.SetEnumValue("AcquisitionMode
", (uint)MVD_CAM_ACQUISITION_MODE.MVD_ACQ_MODE_CON
TINUOUS); 



<!-- page 628 -->
HIKROBOT 
 
619 
 
 
26.         m_cMyCameraToolObj.SetEnumValue("TriggerMode", (ui
nt)MVD_CAM_TRIGGER_MODE.MVD_TRIGGER_MODE_OFF); 
27.         m_cMyCameraToolObj.SetEnumValue("TriggerSource", 
(uint)MVD_CAM_TRIGGER_SOURCE.MVD_TRIGGER_SOURCE_SOF
TWARE); 
28.         m_cMyCameraToolObj.StartGrab();//开始取图 
29.         return 0; 
30.     } 
31.     catch (Exception ex) 
32.     { 
33.         return -1; 
34.     } 
35. } 
36. /// <summary> 
37. /// 从相机获取一帧图像 
38. /// </summary> 
39. private void GetStreamThreadProc() 
40. { 
41.     int nRet = 0; 
42.     CMvdImage imgtemp = null; 
43.     nRet = 0; 



<!-- page 629 -->
HIKROBOT 
 
620 
 
 
44.     nRet = m_cMyCameraToolObj.CameraGrabResult.GetOneFra
meTimeout (ref imgtemp); 
45.     if (0 == nRet && imgtemp != null) 
46.     { 
47.         ImageData imageshow1 = CMvdImageToImageData(im
gtemp); 
48.      } 
49. } 
2.将相机帧类型CMvdImage 图像数据转换成ImageData 类型数据，代码如下。  
1. C# 
2. /// <summary> 
3. /// CMvdImage 格式的图像转为imagedata 图像 
4. /// </summary> 
5. /// <param name="image"></param> 
6. /// <returns></returns> 
7. public ImageData CMvdImageToImageData(CMvdImage image) 
8. { 
9.     if (image != null) 
10.     { 
11.         ImageData imageData = new ImageData(); 



<!-- page 630 -->
HIKROBOT 
 
621 
 
 
12.         imageData.Width = (int)image.Width; 
13.         imageData.Height = (int)image.Height; 
14.         imageData.PixelFormat = PixelFormats.Gray8; 
15.         imageData.ImageBuffer = new byte[image.GetImageDa
ta(0).arrDataBytes.Length]; 
16.         Array.Copy(image.GetImageData(0).arrDataBytes, image
Data.ImageBuffer, imageData.ImageBuffer.Length); 
17.         return imageData; 
18.     } 
19.     else 
20.     { 
21.         return null; 
22.     } 
23. } 
问题根因  
不熟悉相机SDK 及其接口。  
 
 



<!-- page 631 -->
HIKROBOT 
 
622 
 
 
3.2.3 输入图像：给算子模块输入图像数据
的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：如何通过图像数据给算子模块输入图像？  
解答  
以字符识别算子模块为例，代码如下所示，分为c++和c#。  
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



<!-- page 632 -->
HIKROBOT 
 
623 
 
 
stImageData.stDataChannel[0].nLen = width * height; 
MVD_PIXEL_FORMAT pixelFormat = MVD_PIXEL_MONO_08;   //灰度
图 
 
IMvdImage* pInputImage = NULL; 
CreateImageInstance(&pInputImage); 
pInputImage->InitImage(width, height , pixelFormat, stImageData); //
加载内存图像的唯一方法，SetPrivateData/SetPixel 均不能使用 
//字符识别算子 
IOCRSegmenter* pOCRSegmentTool = NULL; 
CreateOCRSegmenterInstance(&pOCRSegmentTool); 
pOCRSegmentTool->SetInputImage(pInputImage); 
 
//c# 
//设置输入图像 
uint width = 2048; 
uint height = 2024; 
byte[] data = new byte[2048 * 2024]; 
MVD_IMAGE_DATA_INFO stImageData = new MVD_IMAGE_DATA_INF
O(); 
stImageData.stDataChannel[0].arrDataBytes = data; 



<!-- page 633 -->
HIKROBOT 
 
624 
 
 
stImageData.stDataChannel[0].nRowStep = width; 
stImageData.stDataChannel[0].nSize = width * height; 
stImageData.stDataChannel[0].nLen = width * height; 
MVD_PIXEL_FORMAT pixelFormat = MVD_PIXEL_FORMAT.MVD_PIXEL_
MONO_08; 
VisionDesigner.CMvdImage cInputImg = new CMvdImage(); 
cInputImg.InitImage(width, height , pixelFormat, stImageData); 
//字符识别算子 
VisionDesigner.OCR.COCRTool cOCRToolObj = new VisionDesigner.O
CR.COCRTool (); 
cOCRToolObj.InputImage = cInputImg; 
问题根因  
不熟悉算子模块函数接口  
 
 



<!-- page 634 -->
HIKROBOT 
 
625 
 
 
3.2.4 实时取流：实时取流的实现方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：在算子SDK 开发中，如何实现实时取流？  
解答  
VM 算子SDK 中提供了有关相机的操作算子，首先，我们需要了解一般步骤。对于设备进
行操作，实现图像采集、参数配置等功能，需要先连接设备（打开设备），其具体流程如
下图所示。  
用代码实现步骤如下,连接相机并开始取流。  
 
C#  
using VisionDesigner.Camera; //引用命名空间 
private CCameraTool m_cMyCameraToolObj = null;//定义一个设备对象 
Thread m_hReceiveThread = null;//定义取流线程 
private bool _bGrabbing = false; 
// 打开相机并开始取图方法 
public int OpenCamera(int cameraIndex = 0) 



<!-- page 635 -->
HIKROBOT 
 
626 
 
 
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
        //1、通过MVD_TRANSFER_LAYER_TYPE 类型枚举设备，返回设备
个数 
        int nRet = CCameraTool.EnumDevices((uint)MVD_TRANSFER_L
AYER_TYPE.MVD_USB_DEVICE | (uint)MVD_TRANSFER_LAYER_TYPE.MV
D_GIGE_DEVICE); 
        if (0 == nRet) 
        { 
            return -1; 
        } 
        //2、选择索引的设备并判断是否可达 



<!-- page 636 -->
HIKROBOT 
 
627 
 
 
        m_cMyCameraToolObj.SelectDevice(cameraIndex); 
        if (!m_cMyCameraToolObj.IsDeviceAccessible(1)) 
            return -1; 
        //3、打开设备，并设置相机参数(相机参数根据实际需求进行设置) 
        m_cMyCameraToolObj.OpenDevice(); 
        m_cMyCameraToolObj.SetEnumValue("AcquisitionMode", (uin
t)MVD_CAM_ACQUISITION_MODE.MVD_ACQ_MODE_CONTINUOUS); 
        m_cMyCameraToolObj.SetEnumValue("TriggerMode", (uint)MV
D_CAM_TRIGGER_MODE.MVD_TRIGGER_MODE_OFF); 
        m_cMyCameraToolObj.SetEnumValue("PixelFormat", (uint)MVD
_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3); 
        //4、开始取图 
        m_cMyCameraToolObj.StartGrab(); 
        _bGrabbing = true; 
        m_hReceiveThread = new Thread(GetStreamThreadProc); 
        m_hReceiveThread.Start();//启动线程主动取流 
        return 0; 
 
    } 
    catch (Exception) 
    { 



<!-- page 637 -->
HIKROBOT 
 
628 
 
 
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
        m_cMyCameraToolObj.CameraGrabResult.GetOneFrameTimeou
t(ref cFrameImage); 
        //判断图像格式，将图像加载到UI 界面的控件mvdRenderActivex1
上 
        if ((VisionDesigner.MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08
 == imgtemp.PixelFormat) || (VisionDesigner.MVD_PIXEL_FORMAT.MV
D_PIXEL_RGB_RGB24_C3 == imgtemp.PixelFormat)) 
        { 
            mvdRenderActivex1.LoadImageFromObject(cFrameImage); 
            mvdRenderActivex1.Display(); 
        } 



<!-- page 638 -->
HIKROBOT 
 
629 
 
 
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



<!-- page 639 -->
HIKROBOT 
 
630 
 
 
除了直接使用VisionDesigner.Camera.CCameraTool，通过以上步骤完成，也可以使用
VM 算子SDK 的相机控件mvdCameraEdit，需要调用mvdCameraEdit.GetSubject()将
算子对象赋给CCameraTool，再调用GetOneFrameTimeout()获取帧图像即可，详细可
以参考路径“C:\Program Files (x86)\MVDAlgorithmSDK\Samples\CSharp\ControlS
amples”下的CameraControlDemo 示例。  
问题根因  
VM 算子SDK 中相机取流的步骤不熟悉。  
 
 



<!-- page 640 -->
HIKROBOT 
 
631 
 
 
3.2.5 卡尺ROI：卡尺型ROI 的生成方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上    
现象：算子SDK 开发，默认支持的ROI 类型不包含直线卡尺ROI 和圆卡尺ROI，那么该
如何生成这两种类型的ROI，并且正确传递给算子使用呢？  
解答  
1.直线卡尺ROI 
直线卡尺ROI 是由线段、卡尺数量、卡尺宽、卡尺高四个元素组合生成的，生成示例
代码如下：  
C# 
private void GenLineCaliperROIAlg(MVD_POINT_F startPoint, MVD_PO
INT_F endPoint, float angle, int caliperCount, float caliperWidth, float
 caliperHeight, ref List<CMvdRectangleF> cMvdRectangleFList, ref C
MvdRectangleF minRect) 
{ 
      CaliperCenters.Clear(); 
 
      float fLineHeight = endPoint.fY - startPoint.fY; 



<!-- page 641 -->
HIKROBOT 
 
632 
 
 
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
           rectangleF = new CMvdRectangleF(stCenter.fX, stCenter.fY,
 caliperWidth, caliperHeight); 
           rectangleF.Angle = fRotateAngle; 
           rectangleF.BorderColor = blue; 
           cMvdRectangleFList.Add(rectangleF); 
      } 
 
      // 生成最小外接矩形 



<!-- page 642 -->
HIKROBOT 
 
633 
 
 
      float LineMidX = (float)(0.5 * (endPoint.fX + startPoint.fX)); 
      float LineMidY = (float)(0.5 * (endPoint.fY + startPoint.fY)); 
      minRect = new CMvdRectangleF(LineMidX, LineMidY, fLineWidt
h, caliperHeight); 
      minRect.Angle = fRotateAngle; 
} 
生成直线卡尺ROI 后，一般提供给直线查找算子使用。使用时，算子的ROI 设置为直
线卡尺ROI 的最小外接矩形，算子基本参数的运行模式设置为ONLY_FIND 模式，算子基
本参数的卡尺框列表设置为卡尺框的列表。调用示例代码如下：  
C# 
private List<CMvdRectangleF> cMvdRectangleFs = new List<CMvdRe
ctangleF>(); 
cMvdRectangleFs.Clear(); 
 
CMvdRectangleF minRect = new CMvdRectangleF(cMvdImage.Width 
/ 2, cMvdImage.Height / 2, cMvdImage.Width / 4, cMvdImage.Heigh
t / 4); 
MVD_POINT_F lineStartPoint = new MVD_POINT_F(1700, 1122); 
MVD_POINT_F lineEndPoint = new MVD_POINT_F(2286, 1122); 
float angleRad = (float)Math.Atan2((lineEndPoint.fY - lineStartPoint.f
Y), (lineEndPoint.fX - lineStartPoint.fX)); 



<!-- page 643 -->
HIKROBOT 
 
634 
 
 
float angle = (float)(angleRad / Math.PI * 180.0); 
GenLineCaliperROIAlg(lineStartPoint, lineEndPoint, angle, caliperCoun
t, caliperWidth, caliperHeight, ref cMvdRectangleFs, ref minRect); 
 
// 直线查找 
CLineFindTool cLineFindTool = new CLineFindTool(); 
cLineFindTool.InputImage = cMvdImage; 
cLineFindTool.ROI = minRect; 
cLineFindTool.BasicParam.RunningMode = VisionDesigner.LineFind.MV
D_RUNNING_MODE.MVD_RUNNING_MODE_ONLY_FIND; // 查找结果受
ROI 和CaliperList 影响      
cLineFindTool.BasicParam.CaliperList = cMvdRectangleFs; 
cLineFindTool.SetRunParam("LineFindMode", "Best"); 
cLineFindTool.SetRunParam("EdgePolarity", "Both"); 
cLineFindTool.Run(); 
 
CLineFindResult cLineFindRes = cLineFindTool.Result; 
List<CLineFindEdgePointInfo> cLineFindEdgePointInfos = cLineFindRe
s.EdgePointInfo; 
 
// 直线轮廓点 



<!-- page 644 -->
HIKROBOT 
 
635 
 
 
CMvdPointSetF lineEdgePoint = new CMvdPointSetF(); 
lineEdgePoint.BorderColor = green; 
for (int i = 0; i < cLineFindEdgePointInfos.Count; i++) 
{ 
lineEdgePoint.AddPoint(cLineFindEdgePointInfos[i].EdgePoint.fX, cLineF
indEdgePointInfos[i].EdgePoint.fY, i); 
} 
mvdRenderActivex1.AddShape(lineEdgePoint); 
 
// 输出直线 
CMvdLineSegmentF line = new CMvdLineSegmentF(new MVD_POINT
_F(cLineFindRes.LineStartPoint.fX, cLineFindRes.LineStartPoint.fY), new 
MVD_POINT_F(cLineFindRes.LineEndPoint.fX, cLineFindRes.LineEndPoin
t.fY)); 
line.BorderColor = green; 
mvdRenderActivex1.AddShape(line); 
 
// 直线卡尺框 
for (int i = 0; i < caliperCount; i++) 
{ 
mvdRenderActivex1.AddShape(cMvdRectangleFs[i]); 



<!-- page 645 -->
HIKROBOT 
 
636 
 
 
} 
 
// 直线检测区域 
minRect.BorderColor = blue; 
mvdRenderActivex1.AddShape(minRect); 
mvdRenderActivex1.Display(); 
2.圆卡尺ROI 
圆卡尺ROI 是由圆心、半径、卡尺数量、卡尺宽、卡尺高五个元素组合生成的，生成
示例代码如下：  
C# 
private void GenCircleCaliperROIAlg(MVD_POINT_F centerPoint, float 
radius, int caliperCount, float caliperWidth, float caliperHeight, ref Lis
t<CMvdRectangleF> cMvdRectangleFList, ref CMvdRectangleF minRe
ct) 
{ 
     CaliperCenters.Clear(); 
 
      float angleOffset = 360.0f / caliperCount; 
      float angleStart = 180.0f / caliperCount; 
 



<!-- page 646 -->
HIKROBOT 
 
637 
 
 
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
           stCenter.fX = (float)(radius * Math.Cos(fRotateAngle / 18
0.0f * Math.PI) + centerPoint.fX); 
           stCenter.fY = (float)(radius * Math.Sin(fRotateAngle / 180.
0f * Math.PI) + centerPoint.fY); 
           CaliperCenters.Add(stCenter); 
           rectangleF = new CMvdRectangleF(stCenter.fX, stCenter.fY,
 caliperHeight, caliperWidth); 
           rectangleF.Angle = fRotateAngle; 
           rectangleF.BorderColor = blue; 
           cMvdRectangleFList.Add(rectangleF); 
      } 



<!-- page 647 -->
HIKROBOT 
 
638 
 
 
 
      // 生成最小外接矩形 
      float CircleMidX = centerPoint.fX; 
      float CircleMidY = centerPoint.fY; 
      minRect = new CMvdRectangleF(CircleMidX, CircleMidY, (float)
(2 * radius + caliperHeight), (float)(2 * radius + caliperHeight)); 
      minRect.Angle = 0.0f; 
} 
生成圆卡尺ROI 后，一般提供给圆查找算子使用。使用时，算子的ROI 设置为圆卡尺
ROI 的最小外接矩形，算子基本参数的运行模式设置为ONLY_FIND 模式，算子基本参数
的卡尺框列表设置为卡尺框的列表。调用示例代码如下：  
C# 
private List<CMvdRectangleF> cMvdRectangleFs = new List<CMvdRe
ctangleF>(); 
cMvdRectangleFs.Clear(); 
 
CMvdRectangleF minRect = new CMvdRectangleF(cMvdImage.Width 
/ 2, cMvdImage.Height / 2, cMvdImage.Width / 4, cMvdImage.Heigh
t / 4); 
MVD_POINT_F circleCenter = new MVD_POINT_F(2258, 1961); 
float circleRadius = 357; 



<!-- page 648 -->
HIKROBOT 
 
639 
 
 
GenCircleCaliperROIAlg(circleCenter, circleRadius, caliperCount, caliper
Width, caliperHeight, ref cMvdRectangleFs, ref minRect); 
 
// 圆查找 
CCircleFindTool cCircleFindTool = new CCircleFindTool(); 
cCircleFindTool.InputImage = cMvdImage; 
cCircleFindTool.ROI = minRect; 
cCircleFindTool.BasicParam.RunningMode = VisionDesigner.CircleFind.
MVD_RUNNING_MODE.MVD_RUNNING_MODE_ONLY_FIND; // 查找结
果受ROI 和CaliperList 影响      
cCircleFindTool.BasicParam.CaliperList = cMvdRectangleFs; 
float fMinRadius = (float)(circleRadius - 0.5 * caliperHeight); 
float fMaxRadius = (float)(circleRadius + 0.5 * caliperHeight); 
cCircleFindTool.SetRunParam("MinRadius", Convert.ToInt32(fMinRadiu
s).ToString()); 
cCircleFindTool.SetRunParam("MaxRadius", Convert.ToInt32(fMaxRadiu
s).ToString()); 
cCircleFindTool.SetRunParam("EdgeThresh", "15"); 
cCircleFindTool.SetRunParam("CircleFindMode", "Best"); 
cCircleFindTool.SetRunParam("EdgePolarity", "WhiteToBlack"); 
cCircleFindTool.SetRunParam("RejectNum", "0"); 



<!-- page 649 -->
HIKROBOT 
 
640 
 
 
cCircleFindTool.SetRunParam("RejectDist", "5"); 
cCircleFindTool.Run(); 
 
CCircleFindResult cCircleFindRes = cCircleFindTool.Result; 
List<CCircleFindEdgePointInfo> cCircleFindEdgePointInfos = cCircleFin
dRes.EdgePointInfo; 
 
// 圆轮廓点 
CMvdPointSetF circleEdgePoint = new CMvdPointSetF(); 
circleEdgePoint.BorderColor = green; 
for (int i = 0; i < cCircleFindEdgePointInfos.Count; i++) 
{ 
circleEdgePoint.AddPoint(cCircleFindEdgePointInfos[i].EdgePoint.fX, cCi
rcleFindEdgePointInfos[i].EdgePoint.fY, i); 
} 
mvdRenderActivex1.AddShape(circleEdgePoint); 
 
// 输出圆环 
CMvdCircleF circle = new CMvdCircleF(cCircleFindRes.Circle.Center, c
CircleFindRes.Circle.Radius); 
circle.BorderColor = green; 



<!-- page 650 -->
HIKROBOT 
 
641 
 
 
mvdRenderActivex1.AddShape(circle); 
 
// 输出ROI 圆弧 
CMvdAnnularSectorF circleAnnu = new CMvdAnnularSectorF(circleCe
nter, fMinRadius, fMaxRadius, 0.0f, 360.0f); 
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
运行效果如下图所示。  



<!-- page 651 -->
HIKROBOT 
 
642 
 
 
 
问题根因  
不熟悉卡尺型ROI 的生成方法。  
 
 



<!-- page 652 -->
HIKROBOT 
 
643 
 
 
3.2.6 DL 算子耗时：深度学习算子长时间
停止再运行耗时变长问题的解决方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：深度学习算子长时间停止再运行，第一次运行耗时会变长，如何解决？  
解答  
原因是显卡休眠，深度学习算子运行前需要初始化CUDA 资源，故第一次耗时较长。长时
间停止将导致显卡休眠，从而导致再运行耗时变长。所以，需每隔一定周期将显卡唤醒，
防止软件一段时间未运行时显卡休眠。显卡唤醒进程代码如下：  
C++ 
int main() 
{ 
 
printf("====================Awake Gpu start=====
===============\n"); 
 
// 覆盖写入文件，不必删除文件 
 
std::ofstream outFile("AwakenGPUToolLog.txt"); 
 
outFile << "Awake Gpu start" << std::endl; 
 



<!-- page 653 -->
HIKROBOT 
 
644 
 
 
 
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
 
 
 
outFile << "Have no cuda device, err = " <<
 err << std::endl; 
 
 
 
break; 
 
 
} 
 
 
 
err = cudaMalloc((void**)&data_g, sizeof(int)); 
 
 
 
if (cudaSuccess != err) 



<!-- page 654 -->
HIKROBOT 
 
645 
 
 
 
 
{ 
 
 
 
printf("Cuda malloc error. err = %d\n", err); 
 
 
 
outFile << "Cuda malloc error, err = " << er
r << std::endl; 
 
 
 
break; 
 
 
} 
 
 
 
outFile << "GPU OK." << std::endl; 
 
 
 
while (1) 
 
 
{ 
 
 
 
Sleep(10000); 
 
 
 
 
err = cudaMemcpy(data_g, data_c, sizeof(int), 
cudaMemcpyHostToDevice); 
 
 
 
if (cudaSuccess != err) 
 
 
 
{ 
 
 
 
 
printf("Cuda memcpy error.\n"); 
 
 
 
 
outFile << "Cuda memcpy error, err 
= " << err << std::endl; 
 
 
 
 
continue; 



<!-- page 655 -->
HIKROBOT 
 
646 
 
 
 
 
 
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
问题根因  
不熟悉显卡唤醒的方法。  
 
 



<!-- page 656 -->
HIKROBOT 
 
647 
 
 
3.3. 模块工具类 
3.3.1 位置修正：位置修正算子工具的使用
方法 
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：位置修正工具使用方法  
解答  
示例代码如下：  
1. C#  
2.   
3. bool re = true; 
4. //位置修正基准参数 
5.  CPositionFixTool PosFixToolObj = new CPositionFixTool(); 
6.  CPositionFixBasicParam BasicParam = PosFixToolObj.BasicPara
m; 
7.  VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F stBasinInit 
= new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F(); 



<!-- page 657 -->
HIKROBOT 
 
648 
 
 
8.  stBasinInit.stPosition.fX = MatchPoint.X; 
9.  stBasinInit.stPosition.fY = MatchPoint.Y; 
10.  stBasinInit.fAngle = Angle; 
11.  BasicParam.BasePoint = stBasinInit;//设置基准点 
12. //位置修正运行参数 
13.  VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F stBasicRun 
= new VisionDesigner.PositionFix.MVD_FIDUCIAL_POINT_F(); 
14.  stBasicRun.stPosition.fX = stPositionfX; 
15.  stBasicRun.stPosition.fY = stPositionfY; 
16.  stBasicRun.fAngle = stPositionAngle; 
17.  BasicParam.RunningPoint = stBasicRun;//设置运行点 
18.  //获取工具位置修正后Roi 
19.  MVD_SIZE_I stImageSize = new MVD_SIZE_I(); 
20.  stImageSize.nWidth = ImageWidth; 
21.  stImageSize.nHeight = ImageHeight; 
22.  BasicParam.RunImageSize = stImageSize; 
23.  BasicParam.FixMode = MVD_POSFIX_MODE.MVD_POSFIX_MOD
E_HVA; 
24.  PosFixToolObj.BasicParam.InitialShape = SrcRegionROI; 
25.  PosFixToolObj.Run(); 
26.  DesRegionROI = PosFixToolObj.Result.CorrectedShape; 



<!-- page 658 -->
HIKROBOT 
 
649 
 
 
问题根因  
不熟悉位置修正算子工具使用方法  
 
 



<!-- page 659 -->
HIKROBOT 
 
650 
 
 
3.3.2 模板保存：实现模板自动加载的方法
  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
问题：用户在使用算子SDK 开发的模板匹配功能时，希望能在程序运行时可以自动加载之
前训练过的模板。  
解答  
可以使用模板的导入导出方法，步骤如下：  
第一步：程序初始化时导入模板  
1. C#  
2.   
3. public FrmMain() 
4. { 
5.     InitializeComponent(); 
6.     if (File.Exists(savePatternPath))//判断文件是否存在 
7.     { 
8.         pattern.ImportPattern(savePatternPath); 



<!-- page 660 -->
HIKROBOT 
 
651 
 
 
9.     } 
10. } 
第二步：加载模板训练窗口时进行赋值  
1. C#  
2.   
3. private void FrmTempleteMatch_Load(object sender, EventArg
s e) 
4. { 
5.     mvdAlmightyPatternEdit1.SetSubject(savePattern); 
6. } 
第三步：在关闭训练窗口时导出模板：  
1. C#  
2.   
3. private void FrmTempleteMatch_FormClosing(object sender, F
ormClosingEventArgs e) 
4. { 
5.     savePattern.ExportPattern(savePatternPath); 
6. } 
问题根因  



<!-- page 661 -->
HIKROBOT 
 
652 
 
 
不熟悉SDK 算子的相关方法。  
 
 



<!-- page 662 -->
HIKROBOT 
 
653 
 
 
3.3.3 模板匹配： 获取模板匹配框和轮廓点
的方法 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：如何获取模板匹配轮廓点？  
解答 
依次实例化模板匹配工具、设置输入图像、设置ROI、运行、获取匹配点、轮廓点，示例
代码如下： 
C# 
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
    var matchBox = new CMvdRectangleF(item.MatchBox.CenterX, item.MatchBox.CenterY, it
em.MatchBox.Width, item.MatchBox.Height); 
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



<!-- page 663 -->
HIKROBOT 
 
654 
 
 
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
问题根因 
不熟悉如何获取匹配框和匹配点 
 
 



<!-- page 664 -->
HIKROBOT 
 
655 
 
 
3.3.4 模板训练：模板训练执行完成的判断
方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象： 算子SDK 开发打开模板匹配后未训练模板，但模板状态不为null。. 
解答  
模板是否训练完成的条件不应以模板是否等于null 来判断，模板是否训练成功以模板的结
果来判断，C#代码如下：  
1. C# 
2.   
3. if(pattern != null){}//判断模板是否为空 
4. if(pattern.ReginList.Count != 0){}//判断模板训练的区域个数是否为
0 
5. if( pattern1.GetPatternResult() != null){}//判断模板是否训练成功 
问题根因  
不熟悉SDK 算子的相关方法。  



<!-- page 665 -->
HIKROBOT 
 
656 
 
 
 
 



<!-- page 666 -->
HIKROBOT 
 
657 
 
 
3.3.5 图像相减：算子SDK 开发图像相减
的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上+ VS2013 及以上  
现象：WinForm 下的算子SDK 图像相减的使用方法  
解答  
WinForm 下进行算子SDK 开发时图像相减的使用方法，先定义一个图像基准图像CMvdI
mageimage1，图像修正后的图像CMvdImage image2，注意，image2 是图像修正后
的图像。 
1. C# 
2.  
3. if (image1.Width == image2.Width && image1.Height == ima
ge2.Height && image1.PixelFormat == image2.PixelFormat) 
4. { 
5.    CMvdImage diffImage = new CMvdImage(); 
6.    diffImage.InitImage(image1.Width,image1.Height, image1.Pix
elFormat); 



<!-- page 667 -->
HIKROBOT 
 
658 
 
 
7.    for (uint row = 0; row < image1.Height; row++) 
8.    { 
9.       uint nStep = image1.GetImageData(0).nRowStep; 
10.       for (uint col = 0; col < nStep; col++) 
11.       { 
12.          diffImage.GetImageData(0).arrDataBytes[row * nStep +
 col] = (byte)Math.Abs(image1.GetImageData(0).arrDataBytes[ro
w * nStep + col] -image2.GetImageData(0).arrDataBytes[row * 
nStep + col]); 
13.       } 
14.    } 
15.    return diffImage; 
16. } 
问题根因  
不熟悉SDK 算子的相关方法。  
 
 



<!-- page 668 -->
HIKROBOT 
 
659 
 
 
3.3.6 图像修正：图像修正工具的使用方法
  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发图像修正的使用方法  
解答  
首先将工具实例化、工具参数赋值，示例代码如下  
1. C#  
2.   
3. CImageFixtureTool tool = new CImageFixtureTool(); 
4. tool.InputImage = inputImage; 
5. tool.BasicParam.FixMode = MVD_IMGFIX_MODE.MVD_IMGFIX_
MODE_HVA; 
6. tool.BasicParam.BasePoint = new VisionDesigner.ImageFixture.
MVD_FIDUCIAL_POINT_F(basePoint, baseAngle);//基准点 
7. tool.BasicParam.RunningPoint = new VisionDesigner.ImageFixtu
re.MVD_FIDUCIAL_POINT_F(runPoint, runAngle);//运行点 
8. tool.Run(); 



<!-- page 669 -->
HIKROBOT 
 
660 
 
 
问题根因  
不熟悉SDK 算子的相关方法。  
 
 



<!-- page 670 -->
HIKROBOT 
 
661 
 
 
3.3.7 Blob 工具：Blob 工具的使用方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发Blob 工具的使用方法  
解答  
首先将工具实例化、工具参数赋值，然后使用位置修正工具进行位置修正，最后绘制Blob
框。示例代码如下  
1. C#  
2. CBlobFindTool tool = new CBlobFindTool(); 
3. tool.BasicParam.ShowOutlineStatus = true; 
4. tool.BasicParam.ShowBlobImageStatus = true; 
5. tool.InputImage = inputImage; 
6. if (BlobRoi != null){  tool.ROI = BlobRoi;} 
7. tool.SetRunParam("Polarity", "BrightObject");//Blob 工具参数设置 
8. tool.SetRunParam("LowThreshold", "180"); 
9. tool.SetRunParam("HightThreshold", "255"); 
10. tool.SetRunParam("MinArea", "5"); 
11. tool.SetRunParam("MaxArea", "5000"); 



<!-- page 671 -->
HIKROBOT 
 
662 
 
 
12. tool.Run(); 
13. List<CBlobInfo> blobInfoList = tool.Result.BlobInfo; 
14. CPositionFixTool fixTool = new CPositionFixTool();//位置修正 
15. fixTool.BasicParam.BasePoint = new VisionDesigner.PositionFix.
MVD_FIDUCIAL_POINT_F(basePoint, baseAngle); 
16. fixTool.BasicParam.RunImageSize = new MVD_SIZE_I((int)inputI
mage.Width, (int)inputImage.Height); 
17. mvdRenderActivex1.ClearShapes(); 
18. foreach (var blobInfo in blobInfoList)//绘制blob 框数据 
19. { 
20.      CMvdRectangleF rectangleF = blobInfo.BoxInfo; 
21.      rectangleF.BorderColor = new MVD_COLOR(0xFF, 0x00, 0x
00); 
22.      rectangleF.BorderWidth = 2; 
23.      fixTool.BasicParam.InitialShape = rectangleF; 
24.      fixTool.BasicParam.RunningPoint = new VisionDesigner.Pos
itionFix.MVD_FIDUCIAL_POINT_F(runPoint, runAngle); 
25.      fixTool.BasicParam.FixMode = MVD_POSFIX_MODE.MVD_P
OSFIX_MODE_HVA; 
26.      fixTool.Run(); 



<!-- page 672 -->
HIKROBOT 
 
663 
 
 
27.      mvdRenderActivex1.AddShape(fixTool.Result.CorrectedShap
e); 
28. } 
问题根因  
不熟悉相关接口的使用。 
 
 



<!-- page 673 -->
HIKROBOT 
 
664 
 
 
3.3.8 点点测量：点点测量工具的使用方法
  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发点点测量工具的使用方法  
解答  
首先将工具实例化,然后选择两个点,下面以测量两个圆的圆心距为例，示例代码如下  
1. C#  
2.   
3. float distance; 
4. VisionDesigner.P2PMeasure.CP2PMeasureTool cP2PMeasureTool
 = new VisionDesigner.P2PMeasure.CP2PMeasureTool; 
5. cP2PMeasureTool.BasicParam.Point1 = cCirFindTool1.Result.Circl
eCenter; 
6. cP2PMeasureTool.BasicParam.Point2 = cCirFindTool2.Result.Circl
eCenter; 
7. cP2PMeasureTool.Run(); 



<!-- page 674 -->
HIKROBOT 
 
665 
 
 
8. distance= cP2PMeasureTool.Result.Dist();     
问题根因  
不熟悉相关接口的使用。 
 
 



<!-- page 675 -->
HIKROBOT 
 
666 
 
 
3.3.9 亮度测量：亮度测量工具的使用方法
  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发亮度测量工具的使用方法  
解答  
首先将工具实例化,输入图片,最后设置ROI 参数,示例代码如下：  
1. C#  
2.   
3. VisionDesigner.IntensityTool.CIntensityToolTool cIntensityToolTo
ol = newVisionDesigner.IntensityTool.CIntensityToolTool(); 
4. VisionDesigner.CMvdImage InputImg = new CMvdImage(); 
5. InputImg.InitImage("Input.bmp"); 
6. cIntensityToolTool.InputImage = InputImg; 
7. cIntensityToolTool.ROI = new VisionDesigner.CMvdRectangleF(I
nputImg.Width / 2, InputImg.Height / 2, InputImg.Width / 4, I
nputImg.Height / 4); 



<!-- page 676 -->
HIKROBOT 
 
667 
 
 
8. cIntensityToolToolObj.Run(); 
问题根因  
不熟悉相关接口的使用。 
 
 



<!-- page 677 -->
HIKROBOT 
 
668 
 
 
3.3.10 圆查找：圆查找的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：WinForm 下的算子SDK 圆查找的使用方法  
解答  
WinForm 下进行算子SDK 开发时圆查找的使用方法  
第一步，初始化参数列表让用户修改参数。  
第二步，加载图像，设置ROI 等参数，执行找圆操作。  
1. C# 
2. //第一步，初始化参数 
3. try 
4. { 
5.    VisionDesigner.CircleFind.CCircleFindTool m_cCircleFindToolO
bj =newVisionDesigner.CircleFind.CCircleFindTool(); 
6.    //Set input image 
7.    VisionDesigner.CMvdImage cInputImg = new CMvdImage(); 
8.    cInputImg.InitImage("InputTest.bmp"); 



<!-- page 678 -->
HIKROBOT 
 
669 
 
 
9.    m_cCircleFindToolObj.InputImage = cInputImg; 
10.    // Set ROI region (optional) 
11.    m_cCircleFindToolObj.ROI = new VisionDesigner.CMvdRecta
ngleF(cInputImg.Width / 2, cInputImg.Height / 2, cInputImg.Wi
dth / 4, cInputImg.Height / 4); 
12.    //保存参数设置 
13.    byte[] fileBytes = new byte[256]; 
14.    uint nConfigDataSize = 256; 
15.    uint nConfigDataLen = 0; 
16.    try 
17.    { 
18.      m_cCircleFindToolObj.SaveConfiguration(fileBytes, nConfig
DataSize, ref nConfigDataLen); 
19.    } 
20.    catch (MvdException ex) 
21.    { 
22.       if (MVD_ERROR_CODE.MVD_E_NOENOUGH_BUF == ex.Err
orCode) 
23.       { 
24.          fileBytes = new byte[nConfigDataLen]; 
25.          nConfigDataSize = nConfigDataLen; 



<!-- page 679 -->
HIKROBOT 
 
670 
 
 
26.          m_cCircleFindToolObj.SaveConfiguration(fileBytes, nCo
nfigDataSize, ref nConfigDataLen); 
27.       } 
28.       else 
29.       { 
30.          throw ex; 
31.       } 
32.    } 
33. } 
34. //第二步，加载图片并运行 
35. m_cCircleFindToolObj.Run(); 
36. //输出结果 
37. CCircleFindResult circleFindResult = m_CircleFindTool.Result; 
问题原因  
参数设置错误  
 
 



<!-- page 680 -->
HIKROBOT 
 
671 
 
 
3.3.11 仿射变换：图像仿射变换的使用方
法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：WinForm 下的算子SDK 图像仿射变换的使用方法  
解答  
WinForm 下进行算子SDK 开发时图像仿射变换的使用方法  
第一步，初始化参数列表修改参数  
第二步，加载图像，使用当前的参数设置运行工具  
1. C# 
2.   
3. //第一步，设置参数 
4. //定义仿射变换工具对象 
5. m_stImageAffineTransformToolObj = new CImageAffineTransfor
mTool(); 
6. //可修改参数 



<!-- page 681 -->
HIKROBOT 
 
672 
 
 
7. byte[] fileBytes = new byte[256]; 
8. uint nConfigDataSize = 256; 
9. uint nConfigDataLen = 0; 
10. //保存参数 
11. m_stImageAffineTransformToolObj.SaveConfiguration(fileBytes, n
ConfigDataSize, ref nConfigDataLen); 
12. //设置运行参数，输入图像，ROI 面积等，运行 
13. m_stImageAffineTransformToolObj.BasicParam.Aspect = fAspect
Value; 
14. m_stImageAffineTransformToolObj.InputImage = m_stInputImag
e; 
15. m_stImageAffineTransformToolObj.ROIShape = cDefaultRect; 
16. m_stImageAffineTransformToolObj.Run(); 
17. //输出结果 
18. CMvdImage stOutputImage = m_stImageAffineTransformToolO
bj.Result.OutputImage; 
问题原因  
参数设置错误或者缺少参数设置  
 
 



<!-- page 682 -->
HIKROBOT 
 
673 
 
 
3.3.12 直线查找：直线查找工具的使用方
法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：如何进行直线查找  
解答  
使用直线查找工具进行直线查找，在算子SDK 开发中，工具入口为xxxTool，则直线查找
的工具入口为CEdgeFindTool，首先定义接口对象，然后在图片上设置待直线查找的ROI
区域，最后通过接口函数Run 就可以获得直线的相关结果。  
1. C#  
2. // 创建对象 
3. VisionDesigner.EdgeFind.CEdgeFindTool cEdgeFindToolObj = ne
w VisionDesigner.EdgeFind.CEdgeFindTool(); 
4. // 给定输入图片 
5. VisionDesigner.CMvdImage cInputImg = new CMvdImage(); 
6. cInputImg.InitImage("..\\InputTest.bmp"); 
7. cEdgeFindToolObj.InputImage = cInputImg; 



<!-- page 683 -->
HIKROBOT 
 
674 
 
 
8. // 设置ROI 
9. cEdgeFindToolObj.ROI = new VisionDesigner.CMvdRectangleF(c
InputImg.Width / 2, cInputImg.Height / 2, cInputImg.Width / 
4, cInputImg.Height / 4); 
10. // 运行 
11. cEdgeFindToolObj.Run(); 
12. // 获取结果 
13. VisionDesigner.EdgeFind.CEdgeFindResult cEdgeFindRes = cEdg
eFindToolObj.Result; 
14. Console.WriteLine("The number of edge: {0}", cEdgeFindRes. Si
ngleEdgeInfo.Count); 
15. List lcEdgePtInfo = cEdgeFindRes.SingleEdgeInfo; 
16. foreach (CEdgeFindSingleEdgeInfo cCurEdgePt in lstEdgePtInf
o) 
17. { 
18.     Console.WriteLine("EdgePoint: {0}, Sore={1}", cCurEdgePt.Sc
ore); 
19. } 
问题根因  
不熟悉直线查找工具的使用。  



<!-- page 684 -->
HIKROBOT 
 
675 
 
 
 
 



<!-- page 685 -->
HIKROBOT 
 
676 
 
 
3.3.13 缺陷检测：直线边缘缺陷检测工具
的使用方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发直线边缘缺陷检测的使用方法  
解答  
首先将直线边缘缺陷检测工具实例化，然后设置输入图片并选择ROI 区域，最后获取结
果，示例代码如下  
1. C#  
2. VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspTool cLineE
dgeFlawInspToolObj = new VisionDesigner.LineEdgeFlawInsp.CL
ineEdgeFlawInspTool();//工具实例化 
3. VisionDesigner.CMvdImage InputImg = new CMvdImage(); 
4. InputImg.InitImage("InputTest.bmp");//设置输入图片 
5. cLineEdgeFlawInspToolObj.InputImage = InputImg; 



<!-- page 686 -->
HIKROBOT 
 
677 
 
 
6. cLineEdgeFlawInspToolObj.ROI = new VisionDesigner.CMvdRect
angleF(InputImg.Width / 2, InputImg.Height / 2, InputImg.Widt
h / 4, InputImg.Height / 4);//选择ROI 区域； 
7. cLineEdgeFlawInspToolObj.Run();//工具执行 
8. VisionDesigner.LineEdgeFlawInsp.CLineEdgeFlawInspResult cLine
EdgeFlawInspRes = cLineEdgeFlawInspToolObj.Result;//获取结果 
9. String message= "缺陷数":+ cLineEdgeFlawInspRes.FlawInfoList.
Count.Tostring();    
问题根因  
不熟悉相关接口的使用。 
 
 



<!-- page 687 -->
HIKROBOT 
 
678 
 
 
3.3.14 N 点标定：N 点标定的使用方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发N 点标定的使用方法  
解答  
首先记录文本输入的坐标图像点a、b 与物理点c、d，最少需要4 组点，如图可每输入一
组点点击确认，输入点个数大于等于4 时，可点击生成标定文件（CalibRun=true）,示例
代码如下 
1. C#  
2. VisionDesigner.NPointCalib.CNPointCalibTool cNPointCalibToolO
bj =new VisionDesigner.NPointCalib.CNPointCalibTool();//工具实
例化 
3. cNPointCalibToolObj.BasicParam.CameraMode = VisionDesigne
r.NPointCalib.MVD_CAMERA_MODE.MVD_CAMERA_MODE_MOV
E;//基本参数设置 
4. MVD_CALIB_POINT_F stCalibPoint = new MVD_CALIB_POINT_F
(); 
5. stCalibPoint.stImageCoordinate.fX = a; 



<!-- page 688 -->
HIKROBOT 
 
679 
 
 
6. stCalibPoint.stImageCoordinate.fY = b;//图像点 
7. stCalibPoint.stWorldCoordinate.fX = c; 
8. stCalibPoint.stWorldCoordinate.fY = d;//物理点 
9. cNPointCalibToolObj.BasicParam.OffsetPointList.Add(stCalibPoin
t); 
10. //至少需要4 组点 
11. if (cNPointCalibToolObj.BasicParam.OffsetPointList.Count>=4&&
CalibRun==true) 
12. { 
13.      cNPointCalibToolObj.Run();//执行 
14.      VisionDesigner.NPointCalib.CNPointCalibResult cNPointCali
bRes = cNPointCalibToolObj.Result;//获取标定结果 
15.      CalibRun = false; 
16.      if(cNPointCalibRes.OffsetPointCalibInfo.HomoEstStatus!=0) 
17.      { 
18.         cNPointCalibToolObj.ExportCalibFile("E://新建文件夹//cali
b.iccal"); 
19.      }                         
20. } 



<!-- page 689 -->
HIKROBOT 
 
680 
 
 
 
问题根因  
不熟悉相关接口的使用。 
 
 



<!-- page 690 -->
HIKROBOT 
 
681 
 
 
3.3.15 畸变校正：畸变校正的使用方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发畸变校正的使用方法  
解答  
首先将畸变校正工具实例化,然后设置输入图片并选择标定文件，最后获取结果，示例代码
如下  
1. C#  
2. VisionDesigner.ImageCorrectCalib.CImageCorrectCalibTool cIma
geCorrectCalibToolObj = new VisionDesigner.ImageCorrectCali
b.CImageCorrectCalibTool (); 
3. VisionDesigner.CMvdImage cInputImg = new CMvdImage(); 
4. cInputImg.InitImage("InputTest.bmp"); 
5. cImageCorrectCalibToolObj.InputImage = cInputImg; 
6. cImageCorrectCalibToolObj.ImportCalibFile("calib.iccal");//选择标
定文件 
7. cImageCorrectCalibToolObj.Run(); 



<!-- page 691 -->
HIKROBOT 
 
682 
 
 
8. VisionDesigner.ImageCorrectCalib.CImageCorrectCalibResult cIm
ageCorrectCalibRes = cImageCorrectCalibToolObj.Result; 
问题根因  
不熟悉相关接口的使用。 
 
 
 



<!-- page 692 -->
HIKROBOT 
 
683 
 
 
3.3.16 字符识别：多线程同时读取同一个
本地模型的方法 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上 
现象：多线程如何调用本地同一个模型。 
解答 
读取本地模型数据，在经过深拷贝后，使用LoadModelData 接口调用模型。 
C# 
for (int i = 0; i < 3; i++) 
{ 
int temp = i; 
Task.Factory.StartNew(new Action<object>(t =>  
{ 
FileStream fs = new FileStream(modelpath, FileMode.Open); 
long size = fs.Length; 
byte[] array = new byte[size]; 
fs.Read(array, 0, array.Length); 
CNNOCRTool tool = new CNNOCRTool(MVD_ALGORITHM_PLATFORM_TYPE.MVD_A
LGORITHM_PLATFORM_CPU); 
byte[] ModelArray= new byte[array.Length]; 
Array.Copy(array, ModelArray, array.Length); 
tool.BasicParam.LoadModelData(ModelArray, ModelArray.Length); 
//设置图片等参数 
tool.Run(); 
 
}), temp); 
} 
问题根因 
不熟悉多线程同时读取同一个本地模型 
 
 



<!-- page 693 -->
HIKROBOT 
 
684 
 
 
3.3.17 字符识别：VM 自带字符识别模型
的区分 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上 
现象：安装VM 和深度学习包之后，VM 安装路径下的字符识别模块有两个模型：lpr_ocr.
bin 和mvb_ocr.bin，分别对应哪个算子。 
解答 
VM 安装路径中，字符识别模块中有两个已经训练好的模型：lpr_ocr.bin 和mvb_ocr.bi
n，分别对应训练平台-字符识别的字符模型类型：文本行识别和文本行识别（拓展）。 
 
在VM 中，使用字符识别模块，两个模型都可以可以调； 
在算子SDK 开发中，针对自带的两个模型，字符识别算子调用规则是，CNNOCRTool 算
子调用模型lpr_ocr.bin，CNNCharRecogTool 算子调用mvb_ocr.bin。 
问题根因 
不熟悉字符识别模型。 



<!-- page 694 -->
HIKROBOT 
 
685 
 
 
 
 
 



<!-- page 695 -->
HIKROBOT 
 
686 
 
 
3.3.18 设置掩膜：给模块设置掩膜的方法 
描述 
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上 
现象：如何给模块设置掩膜（针对需要设置多个感兴趣区域及屏蔽区域场景可通过掩膜设
置）？ 
解答 
通过掩膜算子CPreproMaskTool 获取掩模图像，例如给Blob 分析模块设置掩膜示例代码
如下； 
C# 
public void SetBlobMask() 
{ 
    //实例掩膜工具 
    CPreproMaskTool cPrepromaskTool = new CPreproMaskTool(); 
    //创建Shape链表 
    List<Tuple<CMvdShape, bool>> maskList = new List<Tuple<CMvdShape, bool>>(); 
    var rect1 = new CMvdRectangleF(rect.CenterX, rect.CenterY, rect.Width - 200, rect.Hei
ght - 200); 
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



<!-- page 696 -->
HIKROBOT 
 
687 
 
 
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
问题根因 
不熟悉掩膜工具的使用。 
 
 
 



<!-- page 697 -->
HIKROBOT 
 
688 
 
 
3.4 控件嵌入类 
3.4.1 图片存储：图片保存的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发如何存储图片。  
解答  
调用SaveImage（图片储存），以存储图片到E 盘为例，示例代码如下，其中要判断路径
中的文件夹已经创建。 
1. C# 
2.  
3. string imageName="a"; 
4. MVD_FILE_FORMAT ms=MVD_FILE_FORMAT.MVD_FILE_BMP;//图
片格式 
5. //保存原图 
6. runImage.SaveImage(“E:\\”+imageName+”_origin.bmp”); 
7. //保存渲染图，参数分别为图片路径，图片格式，图片质量（0-100） 



<!-- page 698 -->
HIKROBOT 
 
689 
 
 
8. mvdRenderActivex1.SaveImage(“E:\\”+imageName+”_render.
bmp”,ms,100,MVD_SAVE_TYPE.MVD_SAVE_RESULT_IMAGE); 
问题根因  
不熟悉相关接口的使用。  
 
 



<!-- page 699 -->
HIKROBOT 
 
690 
 
 
3.4.2 辅助十字线：给图像添加辅助十字线
的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：有的用户在使用算子SDK 开发时，希望能够在图像上显示辅助十字线。  
解答  
算子SDK 在图像上显示辅助十字线的方法如下：  
1. c# 
2.   
3. CMvdLineSegmentF line1 = new CMvdLineSegmentF(new MVD
_POINT_F(mvdimage.Width/2, 0),new MVD_POINT_F(mvdimage.
Width / 2, mvdimage.Height ));//定义线段 
4. CMvdLineSegmentF line2 = new CMvdLineSegmentF(new MVD
_POINT_F(0, mvdimage.Height/2),new MVD_POINT_F(mvdimage.
Width, mvdimage.Height/2));//定义线段 
5. line1.BorderStyle = MVD_DASH_STYLE.MvDashStyleDashDot;//设
置线型 



<!-- page 700 -->
HIKROBOT 
 
691 
 
 
6. line1.BorderColor = new MVD_COLOR(250, 0, 0);//设置线的颜色 
7. line2.BorderStyle = MVD_DASH_STYLE.MvDashStyleDashDot;//设
置线型 
8. line2.BorderColor = new MVD_COLOR(250, 0, 0);//设置线的颜色 
9. mvdRenderActivex1.AddShape(line1);//添加线段1 
10. mvdRenderActivex1.AddShape(line2);//添加线段2 
11. mvdRenderActivex1.Display();//渲染 
问题根因  
不了解算子SDK 的相关接口  
 
 



<!-- page 701 -->
HIKROBOT 
 
692 
 
 
3.4.3 控件调用：在WPF 中使用Winfor
m 控件的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：在算子SDK 开发过程中，用户如何使用封装好的Winform 模板匹配等控件？ 
解答 
1. 首先添加对如下两个dll 文件的引用：WindowsFormsIntegration.dll，System.Wind
ows.Forms.dll。  
 
2. 在要使用WinForm 控件的WPF 窗体的XAML 文件中添加引用。示例代码如下： 
C#  
  
xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Wi
ndows. Forms" 



<!-- page 702 -->
HIKROBOT 
 
693 
 
 
xmlns:wfi="clr-namespace:System.Windows.Forms.Integration;assembly
= WindowsFormsIntegration" 
3. 在WPF 的容器控件内如StackPanel 内首先要添加WinForm 控件的宿主容器，用于衔
接WPF 和WinForm。示例代码如下： 
C# XAML 
  
<StackPanel> 
 
<wfi:WindowsFormsHost x:Name="host" Margin="0,0,0,0" /> 
      
</StackPanel>" 
4. 在代码中定义UserControl1 user= new UserControl1 (); 这里不要忘记添加引用。
UserControl1 是自定义的Winform 用户控件，用于存放控件。然后再将控件放入Wind
owsFormsHost 中，示例代码如下： 
C# .CS 
  
UserControl1 user= new UserControl1 (); 
this.host.Child = user; //使XML 文件中的host 中的内容为用户控件user 
5. 如算子SDK 中渲染控件在WPF 中的调用，添加渲染控件dll，示例代码如下。  


