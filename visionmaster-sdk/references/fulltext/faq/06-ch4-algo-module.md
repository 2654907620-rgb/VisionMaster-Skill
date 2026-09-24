# 第4章 算法模块开发（开发配置/OpenCV/Halcon联合/异常处理）
<!-- pages 703-800 -->

<!-- page 703 -->
HIKROBOT 
 
694 
 
 
 
 



<!-- page 704 -->
HIKROBOT 
 
695 
 
 
问题根因  
对于WPF 如何使用自定义Winform 控件不了解。  
 
 



<!-- page 705 -->
HIKROBOT 
 
696 
 
 
3.4.4 图形改变事件：渲染控件上图形改变
事件的实现方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 +VS2013 及以上  
现象：算子SDK 中如何使用图形改变事件？  
解答  
在算子SDK 中支持五种类型的图形改变事件，分别是图形添加事件（MVD_SHAPE_ADD
ED），图形删除事件（MVD_SHAPE_DELETED），图形编辑事件（MVD_SHAPE_EDITE
D），图形选中事件（MVD_SHAPE_SELECTED）以及未定义事件（MVD_SHAPE_UNDE
FINE）。下面以使用最多的图形添加事件为例，代码如下：  
 
C#   
//注册图形改变事件 
this.mvdRenderActivex1.MVDShapeChangedEvent += mvdRenderActiv
ex1_MVDShapeChangedEvent; 
 
//实现图形改变事件 



<!-- page 706 -->
HIKROBOT 
 
697 
 
 
private void mvdRenderActivex1_MVDShapeChangedEvent(VisionDesi
gner.MVDRenderActivex.MVD_SHAPE_EVENT_TYPE enEventType, Visio
nDesigner.MVD_SHAPE_TYPE enShapeType, VisionDesigner.CMvdShap
e cShapeObj) 
{ 
    if (MVDRenderActivex.MVD_SHAPE_EVENT_TYPE.MVD_SHAPE_ADD
ED == enEventType) 
    { 
        //添加图形时具体执行的逻辑代码 
    } 
} 
 
问题根因  
不熟悉图形改变事件的实现方式。  
 
 



<!-- page 707 -->
HIKROBOT 
 
698 
 
 
3.4.5 鼠标事件：渲染控件上鼠标事件实现
的方法  
描述  
环境：MVDAlgrithm SDK3.4 及以上 + VS2013 及以上  
现象：算子SDK 开发中，渲染控件如何触发鼠标事件  
解答  
在算子sdk 开发过程中，支持7 中鼠标事件类型。切鼠标左键按下（LButtonDown），
鼠标左键抬起（LButtonUp），鼠标右键按下（RButtonDown），鼠标右键抬起（RButt
onUp），鼠标左键双击（LButtonDblClk），鼠标移动（MouseMove），鼠标滚轮（M
ouseWheel）。比较常用的是根据鼠标在控件上的位置来显示图像坐标及像素值，代码如
下所示：  
 
C# 
//在初始化的时候，设置交互模式，标准交互+自定义交互（StandardAndC
ustom） 



<!-- page 708 -->
HIKROBOT 
 
699 
 
 
mvdRenderActivex1.SetConfiguration((uint)MVD_RENDER_PARAM_KEY.
MvdRenderInteractType, (int)MVDRenderInteractType.StandardAndCus
tom); 
 
//事件注册，打开渲染控件属性，选择相应事件可以自动生成 
//用户想要实现自定义交互需通过SetConfiguration 接口启用自定义交互 
//用户可根据enMouseEventType 判断鼠标事件类型，编写对应的响应函数 
//示例：实时显示鼠标所在位置的图像坐标和像素值 
private void mvdRenderActivex1_MVDMouseEvent(MVDMouseEventTy
pe enMouseEventType, int nPointX, int nPointY, short nZDelta) 
{     
    try 
    { 
        //窗口坐标转图像坐标 
        float fImgX = 0.0f, fImgY = 0.0f; 
        mvdRenderActivex1.TransformCoordinate(nPointX, nPointY, re
f fImgX, ref fImgY, MVDCoordTransType.Wnd2Img); 
 
        //获取像素信息显示 
        do 
        { 



<!-- page 709 -->
HIKROBOT 
 
700 
 
 
            if (false == _ImageLoaded) 
            { 
                break; 
            } 
 
            int nImagePointX = (int)fImgX; 
            int nImagePointY = (int)fImgY; 
            int nWidth = (int)_InputImage.Width; 
            int nHeight = (int)_InputImage.Height; 
            if (nImagePointX < 0 || nImagePointX >= nWidth 
                || nImagePointY < 0 || nImagePointY >= nHeight) 
            { 
                break; 
            } 
 
            string pixelInfo = string.Empty; 
            List<byte> pixelValue = _InputImage.GetPixel(nImagePoin
tX, nImagePointY); 
            MVD_PIXEL_FORMAT enPixelFormat = _InputImage.PixelF
ormat; 



<!-- page 710 -->
HIKROBOT 
 
701 
 
 
            if (MVD_PIXEL_FORMAT.MVD_PIXEL_MONO_08 == enPixe
lFormat) 
            { 
                pixelInfo = string.Format("X:{0:D4} Y:{1:D4} | R:{2:D3} 
G:{3:D3} B:{4:D3}", nImagePointX, nImagePointY, pixelValue[0], pixelVa
lue[0], pixelValue[0]); 
            } 
            else if (MVD_PIXEL_FORMAT.MVD_PIXEL_RGB_RGB24_C3 
== enPixelFormat) 
            { 
                pixelInfo = string.Format("X:{0:D4} Y:{1:D4} | R:{2:D3} 
G:{3:D3} B:{4:D3}", nImagePointX, nImagePointY, pixelValue[0], pixelVa
lue[1], pixelValue[2]); 
            } 
            else 
            { 
                throw new MvdException(MVD_MODULE_TYPE.MVD_
MODUL_APP, MVD_ERROR_CODE.MVD_E_SUPPORT, "Unsupported pix
el format."); 
            } 
            this.tbPixelInfo.Text = pixelInfo; 



<!-- page 711 -->
HIKROBOT 
 
702 
 
 
        } while (false); 
    } 
    catch (MvdException ex) 
    { 
        this.rtbInfoMessage.Text += String.Format("Fail to respond to
 mouse event! Module : {0}, ErrorCode : 0x{1}, Message : {2}.\r\n", e
x.ModuleType.ToString(), ex.ErrorCode.ToString("X"), ex.Message); 
    } 
    catch (System.Exception ex) 
    { 
        this.rtbInfoMessage.Text += String.Format("Fail to respond to
 mouse event! Message : {0}, StackTrace : {1}.\r\n", ex.Message, ex.St
ackTrace); 
    } 
} 
问题根因  
不熟悉鼠标事件的实现方法  
 
 
 



<!-- page 712 -->
HIKROBOT 
 
703 
 
 
第4 章 算法模块开发 
4.1 开发配置类 
4.1.1 算法开发：算法模块的开发流程 
描述 
环境：VM4.0 及以上 + VS2013 
现象：图像类算子模块的开发流程。 
解答 
第一步，打开算子生成器，配置算法模块名称、自定义输入输出参数，单击下一步。 
 



<!-- page 713 -->
HIKROBOT 
 
704 
 
 
第二步，配置算法模块基本参数和运行参数，并依次生成XML、C++工程、C#工程。 
 
第三步，打开生成的C#工程，选择Release，编译生成dll 并拷贝到XML 文件夹。 
 
第四步，打开生成的C++工程，选择Release、x64，禁用优化。 
 



<!-- page 714 -->
HIKROBOT 
 
705 
 
 
第五步，在C++工程的AlgorithmModule.cpp 中的Process()函数中实现自
定义算法。 
 
第六步，编译C++工程，生成的dll 拷贝到XML 文件夹。  
第七步，将XML 文件夹拷贝到VisionMaster4.0.0\Applications\Module(sp)\x64\XX 
(工具箱名，例如Measurement)，即完成图像类算子模块的开发与嵌入。  
问题根因 
不熟悉图像类算子模块的开发流程。  
 
 



<!-- page 715 -->
HIKROBOT 
 
706 
 
 
4.1.2 参数操作：获取与设置模块参数的方
法  
描述  
环境：VM4.0 及以上 + VS2013 
现象：算法模块开发中如何获取和设置参数? 
解答  
在大多数的VM 模块中，模块参数可以分为基本参数（基本参数包含输入输出参数，输入
参数一般通过订阅的方式获取，输出参数不在VM 参数配置界面上，而是在VM 右边用来
显示结果）和运行参数（算法参数），在算子模块开发中这两种参数的获取和设置的方式
是不同的。  
参数类型主要包括整型（int）、浮点型(float)、字符串型(string)、二进制型(byte)、图像
类型(image)、点集型(pointset)六种。  
基本参数通过VM_M_Getxxxx()函数来获取，如，通过VM_M_Setxxxx()来输出相应的结
果，其用法如下。当需要输入输出浮点数组时，可以通过遍历函数来输入输出，也可以调
用VmModule_GetInputVectorIndex_32f()或者VmModule_OutputVector_32f()函数
一次性输入输出。  



<!-- page 716 -->
HIKROBOT 
 
707 
 
 
 
C++ 
//运行函数 
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput, IN
 MVDSDK_BASE_MODU_INPUT* modu_input) 
{ 
 
HKA_F32 fValue = 0; 
 
int nArrayCount = 0; 
 
int nRet = IMVS_EC_UNKNOWN; 
 
 
//从模块界面中拿到名为ImagePointA 的数组中索引为0 的浮点值 
 
nRet = VM_M_GetFloat(hInput, "ImagePointA", 0, &fValue, &
nArrayCount); 
 
 
//将模块输出中名为ModuStatus 的整型数组中索引为0 的值设置为
1 
 
VM_M_SetInt(hOutput, "ModuStatus", 0, 1); 
} 
针对运行参数（算法参数），可在GetParam( )或SetParam( )函数里加上相应的判断，
从而在每一次运行时自动获取或设置算法参数；也可在函数里调用函数里调用GetPara
m( )或SetParam( )来获取或设置算法参数，如下所示：  



<!-- page 717 -->
HIKROBOT 
 
708 
 
 
 
C++ 
//运行函数 
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput, IN
 MVDSDK_BASE_MODU_INPUT* modu_input) 
{ 
 
char pBuff[1024] = {1024}; 
 
int pDataLen=1024; 
 
 
//获取模块界面中名为threshold 的运行参数的值 
 
GetParam("threshold", pBuff, sizeof(pBuff), &pDataLen); 
 
//获取到的值做转换 
 
int thresh = atoi(pBuff); 
 
 
//将模块中名为threshold 的运行参数设置为240 
 
SetParam("threshold", "240", pDataLen); 
} 
注意：基本参数和运行参数的参数名可以在模块对应的xxxxAlgorithmTab.xml 文件中找
到，即参数配置界面xml，文件路径如下。另外，输入输出参数需要在xxxxModu.xml 文
件中定义。  



<!-- page 718 -->
HIKROBOT 
 
709 
 
 
 
 
 
问题根因  
算子模块开发中模块参数的相关接口  



<!-- page 719 -->
HIKROBOT 
 
710 
 
 
4.1.3 文件交互：文件交互操作的配置方法
  
描述  
环境：VM4.0 及以上 + VS2013  
现象：自定义算子模块开发中如何实现文件交互？  
解答  
1. 打开模块对应的***AlgorithmTab.xml 配置文件，在Name 是Tab_Basic Params 的
Tab 中添加如下方格式的xml 信息；  
 
<OpenFileForCalibDialog Name="CalibPathName" NameSpace="Stan
dard"> 
 
<Description>Load Calib File Path</Description> 
 
<DisplayName>RunParam_Load Calibration File</DisplayNam
e> 
 
<Visibility>Beginner</Visibility> 
 
<AccessMode>RW</AccessMode> 
 
<CurValue></CurValue> 



<!-- page 720 -->
HIKROBOT 
 
711 
 
 
 
<DefaultValue></DefaultValue> 
 
<FileOption> 
 
 
<IsMultiselect>false</IsMultiselect> 
 
 
<FilterName>.xml|*.xml;*.iwcal</FilterName> 
 
</FileOption> 
</OpenFileForCalibDialog> 
界面示意如下：  
 
2. C++工程中添加底层逻辑代码，主要通过SetParam 和GetParam 两个函数去设置和
获取文件路径代码如下。  



<!-- page 721 -->
HIKROBOT 
 
712 
 
 
 
C++ 
//SetParam 函数中加入以下代码来获取文件路径并设置到底层，选择路径时
触发读取文件函数 
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
 
memcpy_s(m_chSaveCalibPathName, MAX_FILE_PATH, pData, 
strlen(pData)); 
 
//读取文件操作 
 
nErrCode = LoadFile(m_chSaveCalibPathName); 
} 
//GetParam 函数中加入以下代码来获取底层文件路径信息 
else if (0 == strcmp("CalibPathName", szParamName)) 



<!-- page 722 -->
HIKROBOT 
 
713 
 
 
{ 
 
sprintf_s(pBuff, nBuffSize, "%s", m_chSaveCalibPathName); 
} 
3. 完成以上两步就可以实现界面选择文件并加载文件操作，要实现每次执行时能同步加载
最新的文件还需添加刷新标志位并在process 函数中添加触发代码。  
刷新标志位控件添加方法：打开模块对应的***AlgorithmTab.xml 配置文件，在Name 是
Tab_Basic Params 的Tab 中添加如下方格式的xml 信息（在添加文件操作控件下面添
加）；  
 
<Boolean Name="RefreshFileEnable" NameSpace="Standard"> 
 
<CurValue>False</CurValue> 
 
<DefaultValue>False</DefaultValue> 
 
<Description>RefreshFileEnable</Description> 
 
<DisplayName>RefreshFileEnable</DisplayName> 
 
<Visibility>Beginner</Visibility> 
 
<AccessMode>RW</AccessMode> 
</Boolean> 
界面示意如下：  



<!-- page 723 -->
HIKROBOT 
 
714 
 
 
 
C++工程中添加底层逻辑代码，主要通过SetParam 和GetParam 两个函数去设置和获取
文件路径代码如下。  
 
C++ 
//SetParam 函数中加入以下代码来将更新文件使能设置到底层，更改状态时
触发 
else if (0 == strcmp("RefreshFileEnable", szParamName)) 
{ 
 
if (0 == strncmp(pData, "True", strlen("True"))) 
 
{ 



<!-- page 724 -->
HIKROBOT 
 
715 
 
 
 
 
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
并在process 函数中添加触发代码: 



<!-- page 725 -->
HIKROBOT 
 
716 
 
 
 
C++ 
if (m_bRefreshFileEnable) 
{ 
 
m_calibPathName = m_chSaveCalibPathName; 
 
SetParam("CalibPathName", m_calibPathName.c_str(), m_calibP
athName.length()); 
} 
问题根因  
不熟悉算子模块开发文件交互方法。  
 
 



<!-- page 726 -->
HIKROBOT 
 
717 
 
 
4.1.4 输出显示：设置输出并显示在VM 界
面的方法  
描述  
环境：VM4.0 及以上 + VS2013 
现象：算法模块开发中，如何设置输出并显示在VM 界面上  
解答  
1、在xxxxModu.xml 中配置要输出的参数名称和类型，这些其实一一对应着VM 中模块
运行之后的数据结果。以直线查找模块为例，如下图所示，当在此xml 中将某一个参数的
属性Visible=“false”或者注释掉这个参数，这个参数将不在界面上显示。这个xml 最后
一个是输出基准点和运行点相关信息。  
 



<!-- page 727 -->
HIKROBOT 
 
718 
 
 
2、在xxxxModu.xml 文件中配置输出参数之后，还要在c++工程代码里添加代码，主要
在Process 函数里用VM_M_Setxxxx()函数来设置相应输出参数的值。  
 
//c++设置模块状态 
VM_M_SetInt(hOutput, "ModuStatus", 0, 1); 
3、拿到模块的结果数值之后，就可以进行任意组合将结果显示在图像上，通过配置xxxx
Display.xml 文件来进行渲染操作。以直线查找模块为例，每一项里面都有Mapping 映射
到输出值，从而显示相关内容。下图中各项显示内容分别为：“InputImage”显示图像结
果；“Line Result”显示直线结果，“Through Line”也是显示直线结果，但它是贯穿
线；“Contour Point”显示每个边缘点；“CaliperBox”显示卡尺框，“DetectCaliper
Box”显示卡尺框检测区域，其实观察输出数值，也可以发现这两者的显示是一样的；“R
OI”显示检测区域；“Fixtured Point”显示基准点；“Unfixtured Point”显示运行
点；“Data Record”显示历史结果；“Result List”显示当前结果；“ExternROI”观
察里面的映射值，其实是显示屏蔽区。  



<!-- page 728 -->
HIKROBOT 
 
719 
 
 
 
此处参考其它模块，在图像区域显示文本，在xxxxDisplay.xml 中文件中添加“Show Te
xt”及其中的内容。重新拖拉直线模块，不然不会生效，拖拉直线模块并执行，此时图像
显示就会显示文本信息  
 



<!-- page 729 -->
HIKROBOT 
 
720 
 
 
4、提示：在进行算法模块开发时，关于界面所显示的内容，可以参考已有的模块进行相
应的xml 配置。  
问题根因  
不熟悉如何设置输出并显示在VM 界面上  
 
 



<!-- page 730 -->
HIKROBOT 
 
721 
 
 
4.1.5 模板配置：模板配置界面的实现方法 
描述 
环境：VM4.0 及以上 + VS2013 
现象：自定义模块如何实现模板配置界面。 
解答 
开发模板匹配等模块时，需要进行模板界面的配置，并实现界面与底层数据交互。  
第一步：在算法模块生成器中配置建模的配置参数，如速度尺度、特征尺度等参数。  
 



<!-- page 731 -->
HIKROBOT 
 
722 
 
 
 
第二步：定义数据源类。  
 
第三步：配置AlgorithmTab.xml。  



<!-- page 732 -->
HIKROBOT 
 
723 
 
 
 
 
第四步：新建参数配置界面模板控件。  



<!-- page 733 -->
HIKROBOT 
 
724 
 
 
 
 
第五步：将新建的控件应用于DataTemplate。  
 



<!-- page 734 -->
HIKROBOT 
 
725 
 
 
第六步：新建模板配置弹出窗口。  
 
第七步：建模界面与算法底层数据交互实现。  
 
数据交互代码示例：  
1)界面数据传给底层  



<!-- page 735 -->
HIKROBOT 
 
726 
 
 
(paramsConfig as IUserStringData)["SetImageWidth"] = model.Image
Width.ToString(); //int 
(paramsConfig as IUserStringData)["TextBoxMsg"] = textMsg; //string 
(paramsConfig as IUserBytesData)["SetImageData"] = model.ImageBuf
fer; //byte[] 
2)底层数据传给界面  
 
int ImageWidth = int.Parse((paramsConfig as IUserStringData)["GetIm
ageWidth"]); //int 
byte[] ImageBuffer = (paramsConfig as IUserBytesData)["GetImageDa
ta"]; //byte[] 
byte[] roiBuffer = (paramsConfig as IUserBytesData)["GetRoiData"]; //
byte[] 
3)底层获取界面数据并处理  
 
在AlgorithmModule.cpp 的GetParam 函数中获取界面参数。  



<!-- page 736 -->
HIKROBOT 
 
727 
 
 
 
在AlgorithmModule.cpp 的SetParam 函数中进行建模及参数处理。  



<!-- page 737 -->
HIKROBOT 
 
728 
 
 
 
按照上述步骤开发完成后，运行模块效果如下图所示。  
 



<!-- page 738 -->
HIKROBOT 
 
729 
 
 
问题根因 
不熟悉自定义模块界面配置开发的方法。  
 
 



<!-- page 739 -->
HIKROBOT 
 
730 
 
 
4.1.6 命名翻译：自定义模块在VM 界面显
示中文的方法 
描述 
环境：VM4.0 及以上 + VS2013 
现象：如何给自定义模块添加中文名称。 
解答 
第一步，使用VisionMaster4.X.0\Applications\Lang 中LanguageTool 工具，给算法模
块增加中英文资源。具体步骤：【通过Key 查找资源】中输入模块名称，然后下方分别添
加模块中文值(中文名称)和英文值(英文名称)，最后点击“增加/编辑”按扭。  
 
第二步，重新打开VM，模块中文名添加成功。  



<!-- page 740 -->
HIKROBOT 
 
731 
 
 
 
问题根因 
不熟悉给算法模块添加中英文资源的方法。  
 
 



<!-- page 741 -->
HIKROBOT 
 
732 
 
 
4.1.7 无图像源：算法模块无输入图像的方
法  
描述  
环境：VM4.0 及以上 + VS2013 
现象：算法模块通常是输入一张图片，进行相应的处理。当算法模块不需要图像时，如何
进行修改？  
解答  
1）修改xml，使得界面无输入图像项  
注释图像输入部分，模块的参数配置窗口就没有图像输入部分。  
 
2）修改C++代码，重载Process 函数。  



<!-- page 742 -->
HIKROBOT 
 
733 
 
 
C++ 
int CAlgorithmModule::Process(IN void* hInput, IN void* hOutput)//
模块无输入图片时 
{ 
 
int nRet = IMVS_EC_OK; 
 
//...... 
 
//...... 
 
//...... 
 
return IMVS_EC_OK; 
} 
问题根因  
不熟悉如何修改自定义算法模块为无图像输入。  
 
 



<!-- page 743 -->
HIKROBOT 
 
734 
 
 
4.1.8 多图像源：算法模块输入多幅图像的
方法  
描述  
环境：VM4.0 及以上 + VS2013  
现象：自定义算法模块如何添加多幅图像输入，从而扩展到双目视觉算法领域？  
解答  
根据算法模块生成器生成的模块默认只支持单幅图像输入，如果需要添加多幅图像输入
需要按照下述步骤对模块xml 文件和C++算法代码进行修改和补充。  
1）界面区别  
单目视图算法模块基本参数界面：  



<!-- page 744 -->
HIKROBOT 
 
735 
 
 
 
双目视图算法模块基本参数界面：  



<!-- page 745 -->
HIKROBOT 
 
736 
 
 
 
2）界面XML 修改  
在模块名.xml 的图像输入部分，增加图像输入源2，名称可自定义(图像名、宽、高、
像素格式均需要重命名)。  
 
接着打开模块名AlgorithmTab.xml，将图像输入Category 段改为如下所示(注意：O



<!-- page 746 -->
HIKROBOT 
 
737 
 
 
perationParams 名必须与模块名.xml 中Filter Name 一致)：  
<Category Name="图像输入"> 
 
<Items> 
 
 
<EnumerationG Name="ImageSource"> 
 
 
 
<Description>Input Source 1</Description> 
 
 
 
<DisplayName>RunParam_Input Source 1</Di
splayName> 
 
 
 
<Visibility>Beginner</Visibility> 
 
 
 
<AccessMode>O</AccessMode> 
 
 
 
<Triggers> 
 
 
 
 
<Trigger> 
 
 
 
 
 
<Property>CurValue</Propert
y> 
 
 
 
 
 
<Setters> 
 
 
 
 
 
 
<Setter> 
 
 
 
 
 
 
 
<OperationNam
e>SetCombinationSourceOperation</OperationName> 
 
 
 
 
 
 
 
<OperationPara
ms>InputImage</OperationParams> 
 
 
 
 
 
 
</Setter> 
 
 
 
 
 
</Setters> 



<!-- page 747 -->
HIKROBOT 
 
738 
 
 
 
 
 
 
</Trigger> 
 
 
 
</Triggers> 
 
 
 
<Initers> 
 
 
 
 
<Setter> 
 
 
 
 
 
<TargetName>EnumEntrys</Ta
rgetName> 
 
 
 
 
 
<OperationName>GetFrontPara
mItemsOperation</OperationName> 
 
 
 
 
 
<OperationParams>IMAGE</O
perationParams> 
 
 
 
 
</Setter> 
 
 
 
 
<Setter> 
 
 
 
 
 
<TargetName>CurValue</Targ
etName> 
 
 
 
 
 
<OperationName>GetSelected
CombinationOperation</OperationName> 
 
 
 
 
 
<OperationParams>InputImage
</OperationParams> 
 
 
 
 
</Setter> 
 
 
 
</Initers> 
 
 
</EnumerationG> 



<!-- page 748 -->
HIKROBOT 
 
739 
 
 
 
 
<EnumerationG Name="ImageSource2"> 
 
 
 
<Description>Input Source 2</Description> 
 
 
 
<DisplayName>RunParam_Input Source 2</Di
splayName> 
 
 
 
<Visibility>Beginner</Visibility> 
 
 
 
<AccessMode>O</AccessMode> 
 
 
 
<Triggers> 
 
 
 
 
<Trigger> 
 
 
 
 
 
<Property>CurValue</Propert
y> 
 
 
 
 
 
<Setters> 
 
 
 
 
 
 
<Setter> 
 
 
 
 
 
 
 
<OperationNam
e>SetCombinationSourceOperation</OperationName> 
 
 
 
 
 
 
 
<OperationPara
ms>InputImage2</OperationParams> 
 
 
 
 
 
 
</Setter> 
 
 
 
 
 
</Setters> 
 
 
 
 
</Trigger> 
 
 
 
</Triggers> 
 
 
 
<Initers> 



<!-- page 749 -->
HIKROBOT 
 
740 
 
 
 
 
 
 
<Setter> 
 
 
 
 
 
<TargetName>EnumEntrys</Ta
rgetName> 
 
 
 
 
 
<OperationName>GetFrontPara
mItemsOperation</OperationName> 
 
 
 
 
 
<OperationParams>IMAGE</O
perationParams> 
 
 
 
 
</Setter> 
 
 
 
 
<Setter> 
 
 
 
 
 
<TargetName>CurValue</Targ
etName> 
 
 
 
 
 
<OperationName>GetSelected
CombinationOperation</OperationName> 
 
 
 
 
 
<OperationParams>InputImage
2</OperationParams> 
 
 
 
 
</Setter> 
 
 
 
</Initers> 
 
 
</EnumerationG> 
 
</Items> 
</Category> 
3）底层算法代码修改  



<!-- page 750 -->
HIKROBOT 
 
741 
 
 
由于输入为两幅图像，而标准Demo 中GenerateImage 函数是获取单幅图像，因此
需要重写取图方法，示例代码如下：  
/// <summary> 
/// 获取两幅输入图像(HKA_IMAGE) 
/// </summary> 
/// <param name="hInput">输入体指针</param> 
/// <returns></returns> 
int CAlgorithmModule::GetInputImage(IN void* hInput, bool &bCame
ra1, bool &bCamera2, HKA_IMAGE struInputImg[2]) 
{ 
 
HKA_S32             nRet = IMVS_EC_UNKNOWN; 
 
HKA_U32             nImageStatus = 0; 
 
 
//HKA_IMAGE struInputImg[2]; 
 
do 
 
{ 
 
 
nRet = VmModule_GetInputImageByName(hInput, 
 
 
 
"InImage", 
 
 
 
"InImageWidth", 
 
 
 
"InImageHeight", 
 
 
 
"InImagePixelFormat", 



<!-- page 751 -->
HIKROBOT 
 
742 
 
 
 
 
 
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



<!-- page 752 -->
HIKROBOT 
 
743 
 
 
最后，在Process 函数中调用该方法，即可获取两张输入图像，示例代码如下：  
//获取输入的两张图片 
 
bool bCamera1 = false; 
 
bool bCamera2 = false; 
 
HKA_IMAGE struInputImg[2]; 
 
int nRet = GetInputImage(hInput, bCamera1, bCamera2, struI
nputImg); 
 
if (!bCamera1 && !bCamera2) 
 
{ 
 
 
//两个图片都没有,返回错误 
 
 
return IMVS_EC_MODULE_SUB_RST_NOT_FOUND; 
 
} 
 
if (IMVS_EC_OK != nRet) 
 
{ 
 
 
return IMVS_EC_MODULE_INPUT_NOT_FOUND; 
 
} 
如果基类中没有VmModule_GetInputImageByName 方法，则将下面这段代码复制
粘贴到VmModule_IO.cpp 中。  
HKA_S32 VmModule_GetInputImageByName(IN const void * const hI
nput, 
                                     char          *strImage, 



<!-- page 753 -->
HIKROBOT 
 
744 
 
 
                                     char          *strWidth, 
                                     char          *strHeight, 
                                     char          *strFormat, 
                                     HKA_IMAGE     *image, 
 
 
 
 
 
 
 
 
 
 HKA_U32       *imageStatus) 
{ 
    HKA_S32          nRet          = IMVS_EC_UNKNOWN; 
    HKA_S32          format        = 0; 
    HKA_IMAGE_FORMAT formatAlg     = HKA_IMG_MONO_08; 
    HKA_U32          nStatusImage  = IMVS_MODU_ENUM_STATUS
_ERROR; 
    HKA_U32          nStatusWidth  = IMVS_MODU_ENUM_STATUS
_ERROR; 
    HKA_U32          nStatusHeight = IMVS_MODU_ENUM_STATUS_
ERROR; 
    HKA_U32          nStatusFormat = IMVS_MODU_ENUM_STATUS
_ERROR; 
    char* 
 
 
 addr          = 0; 
 



<!-- page 754 -->
HIKROBOT 
 
745 
 
 
    HKA_CHECK_ERROR(HKA_NULL == hInput,      IMVS_EC_PARA
M); 
    HKA_CHECK_ERROR(HKA_NULL == image,       IMVS_EC_PARA
M); 
    HKA_CHECK_ERROR(HKA_NULL == imageStatus, IMVS_EC_PARA
M); 
 
    nRet = VmModule_GetInputImageAddress(hInput, strImage, &ad
dr, &nStatusImage); 
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
    nRet = VmModule_GetInputScalar_32i(hInput, strWidth, &(image
->width), &nStatusWidth); 
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
    nRet = VmModule_GetInputScalar_32i(hInput, strHeight, &(image
->height), &nStatusHeight); 
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
    nRet = VmModule_GetInputScalar_32i(hInput, strFormat, &format,
 &nStatusFormat); 



<!-- page 755 -->
HIKROBOT 
 
746 
 
 
    HKA_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
    if(image->height <= 0) 
    { 
        nStatusHeight = IMVS_MODU_ENUM_STATUS_INPUT_INVALI
D; 
    } 
 
    if(image->width <= 0) 
    { 
        nStatusWidth = IMVS_MODU_ENUM_STATUS_INPUT_INVALID; 
    } 
 
    *imageStatus =   (IMVS_MODU_ENUM_STATUS_OK == nStatusI
mage) 
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusW
idth) 
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusH
eight) 
                  && (IMVS_MODU_ENUM_STATUS_OK == nStatusF
ormat); 



<!-- page 756 -->
HIKROBOT 
 
747 
 
 
 
    nRet = VmModule_iMVSFormatToAlgFormat(format, &formatAlg); 
    HKA_CHECK_ERROR(HKA_TRUE != nRet, nRet); 
 
    image->format  = formatAlg; 
    image->data[0] = addr; 
    image->step[0] = (HKA_IMG_RGB_RGB24_C3 == formatAlg) ? (3 
* image->width) : image->width; 
 
    return IMVS_EC_OK; 
} 
问题根因  
不熟悉自定义算法模块添加多幅图像输入的方法。  
 
4.1.9 断点调试：附加断点调试的注意事项
  
描述  



<!-- page 757 -->
HIKROBOT 
 
748 
 
 
环境：VM4.0 及VM4.2 + VS2013 
现象：自定义算法模块附加断点调试的注意事项有哪些？  
解答  
自定义算法模块附加断点调试的注意事项如下：  
1.勾选“显示所有用户的进程”，进程选择“VmModuleProxy.exe”  
 
2.附加代码类型选择“本机”  
 
问题根因  
不熟悉自定义算法模块附加断点调试的注意事项。  



<!-- page 758 -->
HIKROBOT 
 
749 
 
 
 
 



<!-- page 759 -->
HIKROBOT 
 
750 
 
 
4.1.10 点集参数：点集输入、输出实现方法
  
描述  
环境：VM4.0 及以上 + VS2013  
现象：自定义算法模块如何获取输入点集、输出点集，从而扩展到几何基元拟合等算法领
域？  
解答  
1.在算法模块生成器的自定义输入输出中配置输入点集、输出点集参数。  
 
编译界面工程、算法工程，并将文件拷贝到安装目录工具箱后，效果如下图所示。  
 
输入点集、输出点集的参数名称从模块.xml 中查看，子元素类型均为float。  



<!-- page 760 -->
HIKROBOT 
 
751 
 
 
 
2.在算法工程中获取输入点集的数据。  
首先在AlgorithmModule.h 文件中定义输入、输出点集数组变量，示例代码如下：  
#define MVBCALIBTRANS_MAX_POINT_NUM                         
 (100000) 
 
HKA_F32 
 
m_fImagePointX[MVBCALIBTRANS_MAX_POINT
_NUM];    // 像素坐标X 
HKA_F32 
 
m_fImagePointY[MVBCALIBTRANS_MAX_POINT
_NUM];    // 像素坐标Y 
HKA_F32 
 
m_fWorldPointX[MVBCALIBTRANS_MAX_POINT
_NUM];    // 物理坐标X 
HKA_F32 
 
m_fWorldPointY[MVBCALIBTRANS_MAX_POINT
_NUM];    // 物理坐标Y 



<!-- page 761 -->
HIKROBOT 
 
752 
 
 
然后在AlgorithmModule.cpp 文件的Process()函数中获取输入的点集数据，示例代码
如下： 
int nRet = IMVS_EC_UNKNOWN; 
HKA_CHECK_ERROR((IMVS_NULL == hInput || IMVS_NULL == hOutp
ut), IMVS_EC_PARAM); 
 
 
HKA_F32 fValue = 0; 
int nCount = 0; 
int nArrayCount = 0;        // 数组大小 
int pointXCount = 0;        // X 坐标数组大小 
int pointYCount = 0;        // Y 坐标数组大小 
 
// 获取输入点集 
nRet = VM_M_GetFloat(hInput, "ImagePointPointX", 0, &fValue, &nAr
rayCount); 
if (IMVS_EC_OK == nRet && nArrayCount > 0) 
{ 
    for (int i = 0; i<nArrayCount; ++i) 
 
{ 
        nRet = VM_M_GetFloat(hInput, "ImagePointPointX", i, &fValu
e, &nArrayCount); 



<!-- page 762 -->
HIKROBOT 
 
753 
 
 
 
 
if (IMVS_EC_OK != nRet) 
 
 
{ 
 
 
    break; 
 
 
} 
 
 
m_fImagePointX[i] = fValue; 
 
} 
 
pointXCount = nArrayCount; 
} 
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
nRet = VM_M_GetFloat(hInput, "ImagePointPointY", 0, &fValue, &nAr
rayCount); 
if (IMVS_EC_OK == nRet && nArrayCount > 0) 
{ 
    for (int i = 0; i<nArrayCount; ++i) 
 
{ 
 
    nRet = VM_M_GetFloat(hInput, "ImagePointPointY", i, &f
Value, &nArrayCount); 
 
 
if (IMVS_EC_OK != nRet) 
 
 
{ 
 
 
    break; 



<!-- page 763 -->
HIKROBOT 
 
754 
 
 
 
 
} 
 
 
m_fImagePointY[i] = fValue; 
 
} 
 
pointYCount = nArrayCount; 
} 
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
HKA_MODU_CHECK_ERROR((pointXCount != pointYCount), IMVS_EC_P
ARAM); 
3.在算法工程中对输入点集进行处理，给输出点集数组赋值。示例代码如下： 
// 输出物理点 
for (int i = 0; i < pointXCount; ++i) 
{ 
   m_fWorldPointX[i] = m_fImagePointX[i] + 400; 
   m_fWorldPointY[i] = m_fImagePointY[i] + 500; 
} 
4.在算法工程中设置点集输出。示例代码如下：  
if (IMVS_EC_OK == nRet) 
{ 



<!-- page 764 -->
HIKROBOT 
 
755 
 
 
 
VM_M_SetInt(hOutput, "ModuStatus", 0, 1);        // 模块状态 
 
int nProcessStatus = 1;
 
 
 
 
 
 
// 1 表示模块正常，0 表
示模块异常 
 
nRet = VmModule_OutputVector_32f(hOutput, nProcessStatu
s, m_fWorldPointX, "WorldPointPointX", nArrayCount); 
 
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
 
nRet = VmModule_OutputVector_32f(hOutput, nProcessStatu
s, m_fWorldPointY, "WorldPointPointY", nArrayCount); 
 
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
} 
else 
{ 
 
VM_M_SetInt(hOutput, "ModuStatus", 0, 0); 
} 
模块运行效果如下图所示。  
 



<!-- page 765 -->
HIKROBOT 
 
756 
 
 
问题根因  
不熟悉自定义算法模块点集输入与输出的方法。  
 
 



<!-- page 766 -->
HIKROBOT 
 
757 
 
 
4.1.11 直线参数：获取输入直线的方法  
描述  
环境：VM4.2 及以上 + VS2013  
现象：自定义算法模块如何获取输入直线，从而扩展到直线边缘缺陷检测等算法领域？  
解答  
1.在算法模块生成器的自定义输入输出中配置输入直线参数。  
 
编译界面工程、算法工程，并将文件拷贝到工具箱目录后，模块界面如下图所示。  



<!-- page 767 -->
HIKROBOT 
 
758 
 
 
 
输入直线的参数名称从模块.xml 中查看，子元素类型均为float。  
 
2.在算法工程中获取输入直线的数据。  



<!-- page 768 -->
HIKROBOT 
 
759 
 
 
首先在AlgorithmModule.h 文件中定义输入直线的起点、终点变量，示例代码如下： 
float lineStartPX; 
float lineStartPY; 
float lineEndPX; 
float lineEndPY; 
然后在AlgorithmModule.cpp 文件的Process()函数中获取输入直线的数据，示例代码
如下：  
int nRet = IMVS_EC_UNKNOWN; 
HKA_CHECK_ERROR((IMVS_NULL == hInput || IMVS_NULL == hOutp
ut), IMVS_EC_PARAM); 
 
HKA_F32 fValue = 0; 
int nArrayCount = 0; 
 
nRet = VM_M_GetFloat(hInput, "lineStartPX", 0, &fValue, &nArrayCou
nt); 
if (IMVS_EC_OK == nRet && nArrayCount > 0) 
{ 
 
lineStartPX = fValue; 
} 



<!-- page 769 -->
HIKROBOT 
 
760 
 
 
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



<!-- page 770 -->
HIKROBOT 
 
761 
 
 
HKA_MODU_CHECK_ERROR(IMVS_EC_OK != nRet, nRet); 
问题根因  
不熟悉自定义算法模块获取输入直线的方法。  
 
 



<!-- page 771 -->
HIKROBOT 
 
762 
 
 
4.1.12 矩形参数：输出和显示矩形检测框
的方法  
描述  
环境：VM4.2 及以上 + VS2013  
现象：自定义算法模块如何输出和显示矩形检测框，从而扩展到深度学习目标检测等算法
领域？  
解答  
1.在算法模块生成器的自定义输入输出中配置矩形框输出参数。  
 
编译界面工程、算法工程，并将文件拷贝到工具箱目录后，模块界面如下图所示。  



<!-- page 772 -->
HIKROBOT 
 
763 
 
 
 
输出矩形框的参数名称从模块.xml 中查看，子元素类型均为float。  
 
2.在算法工程中输出检测框的数据。开发者可以输出单个矩形框，也可以输出多个。  
在AlgorithmModule.cpp 文件的Process()函数中输出矩形框数据，示例代码如下：  



<!-- page 773 -->
HIKROBOT 
 
764 
 
 
//输出矩形框1 
VM_M_SetFloat(hOutput, "RectCenterX", 0, 50); 
VM_M_SetFloat(hOutput, "RectCenterY", 0, 50); 
VM_M_SetFloat(hOutput, "RectWidth", 0, 50); 
VM_M_SetFloat(hOutput, "RectHeight", 0, 50); 
VM_M_SetFloat(hOutput, "RectAngle", 0, 10); 
 
//输出矩形框2 
VM_M_SetFloat(hOutput, "RectCenterX", 1, 150); 
VM_M_SetFloat(hOutput, "RectCenterY", 1, 150); 
VM_M_SetFloat(hOutput, "RectWidth", 1, 150); 
VM_M_SetFloat(hOutput, "RectHeight", 1, 150); 
VM_M_SetFloat(hOutput, "RectAngle", 1, 20); 
模块运行结果如下图所示。  



<!-- page 774 -->
HIKROBOT 
 
765 
 
 
 
3.进一步地，如果希望在图像图层上显示输出的矩形检测框图形，则需要让模块输出图像
(图形显示依赖图像)，具体方法和示例代码参见FAQ 专题篇1.4 章节，或者VM4.0-第4
章-4.1.4。获取输入图像并输出图像后，模块运行结果如下图所示。  
 



<!-- page 775 -->
HIKROBOT 
 
766 
 
 
4.打开模块Display.xml，添加矩形框输出，示例如下图所示，每一项里面都有Mapping
映射到输出值。  
 
模块运行效果如下图所示。可以看到，输出图像图层上已叠加检测框图层。  
 
问题根因  
不熟悉自定义算法模块输出和显示矩形检测框的方法。  
 
 



<!-- page 776 -->
HIKROBOT 
 
767 
 
 
4.1.13 多ROI：获取多个ROI 的方法 
描述 
环境：VM4.0.0 及以上 + VS2013 
现象：自研算法模块如何获取多个ROI，从而封装类似BLOB、边缘交点、矩形查找等模块？ 
解答 
1.在模块名AlgorithmTab.xml 中找到ROISelecter 节点，在ROISelection 属性中添加D
oubleBox（双矩形框）。 
 
添加ROI 类型后，从工具箱中拖拽相应模块到流程编辑区，效果如下图所示。 



<!-- page 777 -->
HIKROBOT 
 
768 
 
 
 
2.在算法工程的AlgorithmModule.cpp 文件的Process()函数中获取界面绘制的多ROI。 
C++ 
 
if (modu_input->vtFixRoiShapeObj.size() == 2) 
{ 
 
IMvdRectangleF *rectangleRoi = dynamic_cast<IMvdRectangleF*>(modu_input->vtFix
RoiShapeObj[0]); 
 
width = rectangleRoi->GetWidth(); 
 
height = rectangleRoi->GetHeight(); 
 
centerX = rectangleRoi->GetCenterX(); 
 
centerY = rectangleRoi->GetCenterY(); 
 
 
IMvdRectangleF *rectangleRoi2 = dynamic_cast<IMvdRectangleF*>(modu_input->vtFix
RoiShapeObj[1]); 
 
width2 = rectangleRoi2->GetWidth(); 
 
height2 = rectangleRoi2->GetHeight(); 
 
centerX2 = rectangleRoi2->GetCenterX(); 
 
centerY2 = rectangleRoi2->GetCenterY(); 
} 
3.在算法工程的VmAlgModuBase.cpp 文件的ResetDefaultRoi()函数中，屏蔽原有所有
代码，改成下述代码： 
C++ 
 
int CVmAlgModuleBase::ResetDefaultRoi(OUT BASE_MODU_ROI_DATA* stBaseModuROIData) 
{ 
int nRet = IMVS_EC_OK; 
 
stBaseModuROIData->stRoiBox.clear(); 
 
IMVS_ROI_BOX roiBox = { 0.0f }; 



<!-- page 778 -->
HIKROBOT 
 
769 
 
 
 
 
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
问题根因 
不熟悉自研算法模块的ROI 获取机制。 
 
 



<!-- page 779 -->
HIKROBOT 
 
770 
 
 
4.1.14 日志打印：日志打印的方法 
描述 
环境：VM4.0.0 及以上 + VS2013 
现象：自研算法模块如何打印日志，从而协助定位问题点？ 
解答 
1.针对VM4.3 之前版本，在算法工程的AlgorithmModule.cpp 文件中，在需要打印日志
的位置调用MLOG_ERROR 接口，调用示例如下图所示。 
提示：针对VM4.2 自定义算法模块开发，需要向海康技术或研发获取spdlog 文件夹，放
到c++工程中src 目录下；还需要日志接口初始化：Spdlog_Init4Module(moduName)
和获取模块Id：VM_M_GetModuleId(m_hModule,&m_nModuleId)。日志查看路径，A
pplications\log\Module。 
 
MLOG 日志接口，支持不同等级的日志输出，严重级别从高到低分别是ERROR、WARN、
INFO、DEBUG、TRACE。开发者可根据实际情况选择相应等级的日志接口。 



<!-- page 780 -->
HIKROBOT 
 
771 
 
 
 
2.针对VM4.3 及之后版本，在算法工程的AlgorithmModule.cpp 文件中，在需要打印日
志的位置调用MLOG_ERROR 或者LOG_ERROR 接口，调用示例如下图所示。 
 
 
MLOG 和LOG 日志接口，支持不同等级的日志输出，严重级别从高到低分别是ERROR、
WARN、INFO、DEBUG、TRACE。开发者可根据实际情况选择相应等级的日志接口。 
 
3.模块中打印的日志，会记录在Applications\log\Module\对应模块名.log 文件中。 
 
问题根因 



<!-- page 781 -->
HIKROBOT 
 
772 
 
 
不熟悉自研算法模块的日志打印机制。 
 
 



<!-- page 782 -->
HIKROBOT 
 
773 
 
 
4.1.15 参数自执行：参数自执行的方法 
描述 
环境：VM4.3.0 及以上 + VS2013 
现象：自研算法模块如何实现参数自执行，从而调整参数时能实时看到模块结果？ 
解答 
在模块名AlgorithmTab.xml 中找到Tab_ROI Area 节点，增加CanTriggerRun = “TR
UE”，如下图所示。 
 
 
问题根因 
不熟悉自研算法模块参数自执行的机制。 
 
 
 



<!-- page 783 -->
HIKROBOT 
 
774 
 
 
4.2 联合OpenCV 开发 
4.2.1 环境配置：使用OpenCV 开发的环
境配置 
描述  
环境：VM4.0.0 及以上 + VS2013 
现象：使用第三方库OpenCV 开发时，如何进行环境配置。 
解答  
环境配置时，首先要注意OpenCV 版本与集成环境VS 版本（生成工具）的对应。  
1. 在官网下载相应的OpenCV，例如VS2013（VC=120）这种老版本的集成环境，则O
pencCV 的版本则需包含VC=120，所以OpenCV 的3.1.0 版本满足需求。  
2. 将OpenCV 的安装包进行解压，然后进行系统环境配置。在Path 中添加OpenCV 的
相关路径。如D: \OpenCV3.1.0\opencv\build\x64\vc12\bin 



<!-- page 784 -->
HIKROBOT 
 
775 
 
 
 
3. 接着在VS 中新建项目，打开项目的属性页。  
(1)在VC++目录=>包含目录中添加三个OpenCV 的相关路径。  



<!-- page 785 -->
HIKROBOT 
 
776 
 
 
 
（2）在VC++目录=>库含目录中添加一个OpenCV 的相关路径。  



<!-- page 786 -->
HIKROBOT 
 
777 
 
 
 
（3）在链接器=>库含目录中添加opencv_world310.lib。（注意：如果是Debug 编
译，则是添加opencv_world310d.lib。标红字体对应的是OpenCV 版本）  



<!-- page 787 -->
HIKROBOT 
 
778 
 
 
 
问题根因  
不熟悉如何配置第三方库OpenCV。  
 
 



<!-- page 788 -->
HIKROBOT 
 
779 
 
 
4.2.2 图像类算法：使用OpenCV 开发算
法模块的方法 
描述 
环境：VM4.0 及以上 + VS2013 
现象：如何使用OpenCV 开源库开发算法模块？ 
解答 
使用OpenCV 开源库开发算法模块的步骤如下： 
第一步，输入图像格式由HKA_IMAGE 转Mat 
 
第二步，调用OpenCV 算子API 处理图像 



<!-- page 789 -->
HIKROBOT 
 
780 
 
 
 
第三步，输出图像格式由Mat 转HKA_IMAGE 
 
第四步，输出图像  
 
问题根因 



<!-- page 790 -->
HIKROBOT 
 
781 
 
 
不熟悉OpenCV 开源库开发算法模块的方法。  
 
 



<!-- page 791 -->
HIKROBOT 
 
782 
 
 
4.3 联合Halcon 开发 
4.3.1 联合开发：集成HALCON 第三方算子到VM
工具箱的方法  
描述  
环境：VM4.0 及以上 + VS2013  
问题：有的用户在使用VisionMaster 软件在开发视觉项目时，可能同时也使用HALCO
N，OpenCV 等视觉算法库做一些图像的处理，并且希望能将HALCON 等第三方算子集
成到VM 工具箱，能够在VM 工具箱中拖拽出来，就像VisionMaster 中的其他算法模块
工具一样，可以通过弹出窗口配置运行参数，通过连线订阅其他模块传递的参数，设置R
OI，通过图像窗口查看算法直接结果的渲染效果。实际上是可行的，VisionMaster 是一
个开放平台，可以接入第三方生态，这也是VisionMaster 的一大亮点。这里以封装HAL
CON 的动态阈值算子Dyn_Threshold 来举例说明如何集成第三方算法库中的算子到VM
工具箱中。  
解答  
1 开始之前的准备工作  
在编写自定义算子之前，首先必须了解以下几个概念：  
1.1 VM 软件中所有的算法模块工具的参数调试界面都是依赖XML 文件，VM 软件在启动
时会在加载工具的XML 配置文件，根据XML 配置文件配置的输入输出参数来呈现用户界



<!-- page 792 -->
HIKROBOT 
 
783 
 
 
面。每个算法模块的XML 配置文件存放在VM 安装目录下的Module(sp)文件夹内，例
如，以高精度匹配为例，XML 配置文件存放在下面的目录：（打开XML 文件夹的快捷键
方式：在VM 中选中模块后，点击Ctrl+m） C:\Program Files\VisionMaster4.0.0\Applicatio
ns\Module(sp)\x64\Location\IMVSHPFeatureMatchModu，其中Location 是表示在工具箱的
定位工具组。  
1.2 算法模块的输入输出是由基础的数据类型组成，例如Int，Float，string, bool, enu
m 类型等。  
 
对应的在该模块的XML 文件中，是由XML 的树形节点来描述的。  
在XXXAlgorithmTab.xml（XXX 指代模块的名称）文件中的Tab_Run_Params（模块运
行参数）中可以找到对这些运行的参数的描述。如下图所示：  



<!-- page 793 -->
HIKROBOT 
 
784 
 
 
 
1.3 算法模块一般都要包含ROI 输入，模块是否要接受ROI 输入，位置修正由XML 配置
决定。  



<!-- page 794 -->
HIKROBOT 
 
785 
 
 
 
如图所示的Blob 模块，它的ROI 类型，在IMVSBlobFindModuAlrorithemTab.xml 配
置文件有相关的Item 决定，如下图所示：  



<!-- page 795 -->
HIKROBOT 
 
786 
 
 
 
事实上，我们并不需要非常清楚XML 配置文件中的每一项对应界面上哪些元素，才能开
发出自定义算法模块，我们只需要了解一个事实：XML 配置决定界面上显示的内容。所以
VM 开发组给我们提供了一个便捷的工具来配置工具模块的输入输出配置。这个工具在V
M 软件工具菜单下可以找到。  



<!-- page 796 -->
HIKROBOT 
 
787 
 
 
 
1.4 集成自定义算法模块需要完成3 个工作  
1) 通过自定义模块生成工具生成界面  
2) 生成自定义算法模块的界面需要用到C# DLL  
3) 生成自定义算法模块的算法流程需要用到的C++ DLL  



<!-- page 797 -->
HIKROBOT 
 
788 
 
 
 
定义好输入输出之后，执行生成XML，生成C++工程，生成C# 工程这3 步，就初步完
成了准备工作，执行了上面3 个步骤，应该会生成以模块名字命名开头的3 个文件夹，例
如：  
 
2 举例说明  



<!-- page 798 -->
HIKROBOT 
 
789 
 
 
我们集成一个Halcon 中的算子DynThreshold 到VM 的图像处理工具箱中，DynThresh
old 算子的定义如下：  
DynThreshold（  
HObject inputImage, 
HTuple darkLight,  
HTuple maskWidth,  
HTuple maskHeight, 
HTuple offset,  
HTuple minArea, 
HTuple maxArea,  
HTuple *area）  
由于输入图像可以订阅VM 流程中的图像源模块，用户输入的ROI 可以从界面交互获得，
所以它的输入对应在VM 中的输入如下：  



<!-- page 799 -->
HIKROBOT 
 
790 
 
 
 
对应在VM 中的输出：  
 
第一步：根据上面的定义得输入输出，使用AlgorithmXMLGenerator 工具生成XML 文
件夹，如上图1-6 所示。接着生成模块参数界面的C#工程和模块算法流程的C++工程。
生成工程之后会有以模块名称为前缀的3 个文件夹 ，如上面图1-7 所示。这3 个文件
夹，其中，DynThreshold 文件夹是需要用户最终拷贝到VM 的Applications\Module(s
p)\x64 目录下的模块类别下。  
以Cs 开头的文件夹，是生成界面相关资源的C#工程，我们只需要打开其中的工程，编译
其中的以模块名称命名的工程即可（注意：选择Release 模式，只需要编译以模块名称命
名的工程，不需要编译工程名+Control 的那个工程）。如图2-1 所示：  



<!-- page 800 -->
HIKROBOT 
 
791 
 
 
 
编译完成后，将生成的模块名称+cs.dll 和模块名称.pdb 文件拷贝到DynThreshold 文件
夹中。  
第二步：编写C++工程，工程是上一步自动生成的C++工程，工程名是Proj_+模块名称
命名，就本例来说，就是Proj_DynThreshold 工程。建议使用VS2013 来编写这个工
程。因为VM 中使用的算子基本都是msvc2013 编译器。（注意：选择Release、x64，禁
用优化。）针对本例是VM 联合Halcon 开发算子模块，所以需要在项目中配置halcon 环
境，如附加包含目录，附加库目录，附加依赖项。  


