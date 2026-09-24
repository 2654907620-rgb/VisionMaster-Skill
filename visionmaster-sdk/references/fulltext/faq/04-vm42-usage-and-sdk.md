# VM4.2 章节（常用工具和配置修改 + VM4.2 第1章/第2章）
<!-- pages 387-597 -->

<!-- page 387 -->
HIKROBOT 
 
378 
 
 
1. 调用通讯管理模块中SetParamValue()函数，其中nDeviceID 表示设备列表中处于第
几位，"ConnectState"参数设置true 表示打开，false 表示关闭。获取调用bIsDeviceCo
nnect()函数，返还Bool 类型的值。 
C#  
  
CommManagerModuleTool commManagerModule = (CommManager
ModuleTool)VmSolution.Instance["通信管理1"]; 
//设置通讯设备的开启  
commManagerModule.SetParamValue(1, "ConnectState", "true"); 
//获取通讯的开启状态 
bool m= commManagerModule.bIsDeviceConnect(1); 
2. 通过回调获取设备是否开启  
 
//注册回调函数 
VmSolution.OnCommunicationStatusCallBackEvent += VmSolution_On
CommunicationStatusCallBackEvent; 
private void VmSolution_OnCommunicationStatusCallBackEvent(ImvsS
dkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo) 
{ 
    int nType = reportDataInfo.nType; 



<!-- page 388 -->
HIKROBOT 
 
379 
 
 
    byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pDat
a, reportDataInfo.nLen);//IntPtr 转Byte,可使用Marshal.Copy 
    int len = btarr.Length; 
    string ID = btarr[1].ToString(); 
    string Open = btarr[0].ToString();//开关状态，1 表示开，0 表示关 
} 
问题根因 
不熟悉VM 二次开发接口。  
 
 



<!-- page 389 -->
HIKROBOT 
 
380 
 
 
2.5.4 全局通信：接收和发送数据的方法  
描述  
环境：VM4.0 + VS2015 及以上  
现象：二次开发中，全局模块控件中的通信管理如何接收和发送数据 ？  
解答  
1. 通过接口GetReadData 来接收数据以及SetInt 或者SetString 来发送整型或字符串数
据。其中，需要注意的有两点，一是“通信管理1”指的是当前运行的通信设备；二是接
口函数SetString 中的设备号2，则为通信管理中自动生成的设备序号。  
 
//C# 
CommManagerModuleTool commTool = (CommManagerModuleTool)
VmSolution.Instance["通信管理1"]; 
if (null != commTool) 
{ 
 
commTool.SetString(2, "abcd"); // 发送字符串型数据     
 
int[] aIntVal = new int[3]; 
 
aIntVal[0] = 10; 
 
aIntVal[1] = 11; 



<!-- page 390 -->
HIKROBOT 
 
381 
 
 
 
aIntVal[2] = 12; 
 
commTool.SetInt(1, aIntVal, 0); // 发送整型数据     
 
byte[] btData = null; 
 
commTool.GetReadData(2, ref btData);//接收数据 
} 
2. 通过回调来接收数据  
 
C# 
//注册回调函数，通讯接受事件回调 
VmSolution.OnCommunicationRecvCallBackEvent += VmSolution_OnC
ommunicationRecvCallBackEvent; 
private void VmSolution_OnCommunicationRecvCallBackEvent(ImvsSd
kDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo) 
{ 
 
string strMsg; 
 
try 
 
{ 
 
 
int nType = reportDataInfo.nType; 
 



<!-- page 391 -->
HIKROBOT 
 
382 
 
 
 
 
byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDa
taInfo.pData, reportDataInfo.nLen); 
 
 
int len = btarr.Length; 
 
 
string ID = btarr[0].ToString(); 
 
 
byte[] vs = new byte[len - 2]; 
 
 
Array.Copy(btarr, 2, vs, 0, len - 2); 
 
 
string ReceiveData = System.Text.Encoding.Default.Get
String(vs);//数据 
 
 
strMsg = ID + "号设备接受到：" + ReceiveData; 
 
} 
 
catch (VmException ex) 
 
{ 
 
 
strMsg = "读取通信数据失败. Error Code: " + Convert.
ToString(ex.errorCode, 16); 
 
} 
} 
 
//发送字符串数据同样是使用commManagerModule.SetString ()接口 
public void SendCommDeviceData(int Num, string SendMessage) 
{ 



<!-- page 392 -->
HIKROBOT 
 
383 
 
 
 
CommManagerModuleTool commManagerModule = (Comm
ManagerModuleTool)VmSolution.Instance["通信管理1"]; 
 
string strMsg; 
 
try 
 
{ 
 
 
//获取通讯的连接状态 
 
 
if (commManagerModule.bIsDeviceConnect(Num)) 
 
 
{ 
 
 
 
commManagerModule.SetString(Num, SendMe
ssage);//给连接VM 通讯的设备发送 
 
 
 
strMsg = "发送信号：" + SendMessage + "给"
 + Num + "号通讯设备"; 
 
 
} 
 
 
else 
 
 
{ 
 
 
 
strMsg = Num + "号通讯设备未打开"; 
 
 
} 
 
} 
 
catch (Exception) 
 
{ 
 
 
strMsg = "发送信号失败"; 



<!-- page 393 -->
HIKROBOT 
 
384 
 
 
 
 
return; 
 
} 
} 
问题根因  
不熟悉全局模块中通信管理的相关接口和回调函数。  
 
 



<!-- page 394 -->
HIKROBOT 
 
385 
 
 
2.5.5 全局变量：获取和设置全局变量的方
法  
描述  
环境：VM4.0 + VS2015 及以上  
现象：如何获取和设置全局变量的值？  
解答  
获取方案中的全局变量：  
 
C# 
GlobalVariableModuleTool globalVar = VmSolution.Instance["全局变量
1"] as GlobalVariableModuleTool; 
if (globalVar != null) 
string strX = globalVar.GetGlobalVar(“PhotoX”);//获取 
globalVar.SetGlobalVar("PhotoX", "150.229");//设置 
globalVar.SetGlobalVar("PhotoY", "225.651"); 
globalVar.SetGlobalVar("PhotoR", "23.12"); 



<!-- page 395 -->
HIKROBOT 
 
386 
 
 
 
问题根因  
不熟悉全局变量工具及其接口。  
 
 
 



<!-- page 396 -->
HIKROBOT 
 
387 
 
 
VM4.2（应用&VM SDK 开发） 
VM4.2 手册查找必读  
VM4.2 相比较VM4.0 有一部分更新，因此VM4.2 章节仅提供相对于4.0 有更新的部分，
有些重复性内容可查看4.0 章节，重复性问题举例如下： 
篇幅所致，此表格未完全列出重复问题。 
重复问题 
链接 
MFC 模块索引异常 
2.1.6 模块索引：MFC 模块索引异常解决办法 
提示未注册ActiveX 控件 2.1.8 环境配置：提示未注册ActiveX 控件的解决方法 
二次开发时不显示VM 图
标 
2.1.16 图标隐藏：电脑右下角VM 图标不显示的方法 
获取渲染图像数据 
2.2.6 输出图像：获取渲染图像数据的方法 
流程与模块运行耗时 
2.2.8 耗时统计：流程与模块运行耗时的获取方法 
方案资源释放 
2.2.9 资源释放：方案资源释放的方法 
获取渲染结果 
2.3.1 渲染结果：通过渲染控件绑定流程或模块获取渲染结
果的方法 
所有流程运行结束的回调
函数 
2.4.2 流程运行：所有流程运行结束的回调方法 



<!-- page 397 -->
HIKROBOT 
 
388 
 
 
常用工具和配置修改 
 
 



<!-- page 398 -->
HIKROBOT 
 
389 
 
 
 
 



<!-- page 399 -->
HIKROBOT 
 
390 
 
 
 
 



<!-- page 400 -->
HIKROBOT 
 
391 
 
 
 
 



<!-- page 401 -->
HIKROBOT 
 
392 
 
 
 
 



<!-- page 402 -->
HIKROBOT 
 
393 
 
 
 
 



<!-- page 403 -->
HIKROBOT 
 
394 
 
 
 
 



<!-- page 404 -->
HIKROBOT 
 
395 
 
 
 
 



<!-- page 405 -->
HIKROBOT 
 
396 
 
 
 
 



<!-- page 406 -->
HIKROBOT 
 
397 
 
 
 
 



<!-- page 407 -->
HIKROBOT 
 
398 
 
 
 
 



<!-- page 408 -->
HIKROBOT 
 
399 
 
 
 
 



<!-- page 409 -->
HIKROBOT 
 
400 
 
 
 
 



<!-- page 410 -->
HIKROBOT 
 
401 
 
 
 
 
 



<!-- page 411 -->
HIKROBOT 
 
402 
 
 
第1 章 VM 软件使用 
1.1 环境配置类 
1.1.1 用户权限：普通用户权限使用VM 的
方法  
描述  
环境：VM4.2  
现象：生产现场只部署了普通用户权限，而VM 需要使用管理员权限，这种情况下无法正
常启动VM42。  
解答  
1）管理员权限下，安装VM4.2.0 安装包。  
2）开VM 安装路径下.\Tools\ SetNormalUserPermissions.exe。输入S，按回车键。  
 



<!-- page 412 -->
HIKROBOT 
 
403 
 
 
3）管理员权限下，手动在VM 安装路径，配置要使用的普通用户（此处为Users 用户）
的完全控制权限。此步骤不配置可能会导致加载资源失败；  
 
4）理员权限下，关闭防火墙和杀毒软件。此步骤不配置，软件有时会打不开；  
5）不必要步骤，根据现场情况，需要使用深度学习GPU 模块的不用配置）管理员权限
下，将AwakenGpuTool.exe 删掉。否则有的电脑测试会出现cudart64_110.dll 丢失报
错，如不发生此报错无需删除。（此工具用于深度学习模块，不影响2D 算法模块使用，
如需使用深度学习模块不需执行步骤5）  



<!-- page 413 -->
HIKROBOT 
 
404 
 
 
 
6）不必要步骤，根据现场情况）有些电脑打开VM 时会提示需要输入管理员密码，要在
管理员账户下改一下组策略。  
点击坐标左下角“Win”图标，搜索处输入“gpedit.msc”
按“确定”，打开“本地组
策略编辑器”，然后“计算机配置”
“Windows 设置”
“安全设置”
“本地策
略”
“安全选项”
“用户帐户控制：以管理员批准模式运行所有管理员”，改为已禁
用。  
 



<!-- page 414 -->
HIKROBOT 
 
405 
 
 
问题根因  
不熟悉普通用户权限配置VM 的使用。  
 
 



<!-- page 415 -->
HIKROBOT 
 
406 
 
 
1.1.2 脚本环境：联合OpenCV 开发的环
境配置方法  
描述  
环境：VM4.2  
现象： 联合OpenCV 进行脚本模块开发时，如何配置环境？  
解答  
第一步，给脚本模块添加引用程序集，opencv 可以在VM 安装路径下获取；  
 
第二步，将VM 安装路径下的第三方库中的OpenCvSharpExtern.dll 手动拷贝到脚本依
赖目录下，即拷贝到D:\VM4.2\VisionMaster4.2.0\Applications\VmModuleProxy\x64
文件中。  



<!-- page 416 -->
HIKROBOT 
 
407 
 
 
 
问题根因  
不熟悉脚本模块Opencv 环境配置  
 
 



<!-- page 417 -->
HIKROBOT 
 
408 
 
 
1.1.3 环境配置：规避流程运行时卡死的方
法 
描述 
环境：VM4.2  
现象：流程运行卡死场景。  
解答 
场景1：安装VM4.2 版本，运行久了会出现软件进程卡死的情况，每次卡死都需要重新启
动电脑解决。 
远程查看后发现后台有两个server 进程，其中一个进程卡死无法关闭。 
解决策略：加密狗不能使用usb 延长线，必须直插。否则会出现加密狗接口在退出时卡
死，造成服务无法退出。 
场景2：客户全局脚本设置，VM 加载方案完成后，全局脚本直接触发流程1 进行连续运
行。（1）重启设备设置开机自启动加载方案，偶现全局脚本代码无法触发流程运行；（2）
偶现切换方案，主界面卡死无法操作。 
远程发现客户在全局脚本加载结束回调中调用连续执行接口，连续执行会回调信息给界
面，与界面线程锁死。 
解决策略：不要在全局脚本的加载结束回调中调用连续执行接口，可以把连续执行接
口写在其它地方。如果要达到加载方案结束后就自动触发连续执行，可以在回调里触
发一个信号量，线程监督此信号量，从而控制流程连续执行。 
问题根因 



<!-- page 418 -->
HIKROBOT 
 
409 
 
 
不正规操作导致进程卡死的场景 
 
 



<!-- page 419 -->
HIKROBOT 
 
410 
 
 
1.2 工具类 
1.2.1 平移旋转标定：平移旋转标定模块的
使用方法  
描述  
环境：VM4.2 
现象：VM 二次开发如何使用平移旋转标定模块？  
解答  
适用场景：单相机与机构(模组/机械手)的标定场景。  
标定方式：单相机与机构做平移标定(9 点标定)或平移旋转标定(12 点标定)。前者适用于
吸嘴与旋转轴共轴的场景，后者适用于吸嘴与旋转轴不共轴的场景）。  
限制条件：不支持多相机联立坐标系。  
模块界面如下：  



<!-- page 420 -->
HIKROBOT 
 
411 
 
 



<!-- page 421 -->
HIKROBOT 
 
412 
 
 
 
（1）标定类型  
确定标定类型是平移标定（九点标定）还是平移旋转标定（十二点标定）。平移标定如
左下图：只需图像点和物理点；平移旋转标定如右下图：需要图像点、物理点、图像角度和
物理角度。  



<!-- page 422 -->
HIKROBOT 
 
413 
 
 



<!-- page 423 -->
HIKROBOT 
 
414 
 
 
 
（2）标定点获取  
支持触发获取及手动输入两种方式。触发获取：需要订阅图像点和机构物理点作为输入
参数；手动输入：手动填写图像点及物理点坐标。其中标定点输入支持按点和按坐标两种方
式。  
注意：由于手动输入模式缺少图像角度，故无法计算旋转一致性和左右手手性。  



<!-- page 424 -->
HIKROBOT 
 
415 
 
 
 
 
（3）相机模式：支持相机静止和相机运动两种模式。自由度：支持三种自由度，默认仿
射模式。  



<!-- page 425 -->
HIKROBOT 
 
416 
 
 



<!-- page 426 -->
HIKROBOT 
 
417 
 
 
 
（4）平移次数：默认9 次可根据实际情况进行调整（4-16）。旋转次数:平移标定自动隐
藏；平移旋转标定需手动输入，建议3 次，可根据实际情况进行调整（3-16）。  



<!-- page 427 -->
HIKROBOT 
 
418 
 
 
 
（5）更新文件：默认不更新，开启后若进行一次标定，则会自动更新指定路径下的标定
文件。标定文件路径：设置标定文件保存的路径（保存为xml 格式）。  
 
（6）示教（选择项，可关闭）：开启后，若通讯触发字符与输入的外部触发字符相匹
配，则将示教的基准图像坐标，示教点物理坐标，拍照位物理坐标（默认标定中心点坐
标，如九点标定则为第五点坐标）保存至标定文件。  



<!-- page 428 -->
HIKROBOT 
 
419 
 
 
 
问题根因  
不熟悉平移旋转标定模块。  
 
 



<!-- page 429 -->
HIKROBOT 
 
420 
 
 
1.2.2 旋转标定：旋转标定模块的使用方法
  
描述  
环境：VM4.2 
现象：VM 二次开发如何使用旋转标定模块？  
解答  
适用场景：单相机与机构(模组/机械手)的旋转中心标定场景。  
标定方式：相机静止时，机构带标定物旋转N 次，相机运动时，机构带相机旋转N 次，
标定机构旋转轴中心坐标。  
限制条件：保证运动是纯旋转(无平移)，每次旋转角度需严格相等，旋转次数至少为3
次。  
 
模块界面如下：  



<!-- page 430 -->
HIKROBOT 
 
421 
 
 
 
（1）图像点  
图像中特征点的像素坐标。输入支持按点和按坐标两种方式。  
（2）物理旋转角度  
机构每次旋转的角度值。  
（3）旋转次数  



<!-- page 431 -->
HIKROBOT 
 
422 
 
 
机构旋转的次数。  
（4）标定文件（如未加载平移标定文件，则无法标定旋转中心）  
加载平移标定文件，支持.xml 和.iwcal 格式。刷新信号的填写说明为：空或0 时，表示该
模块读取标定文件后，便不再更新，一直使用第一次读取的标定文件；非零时，表示该模
块运行时会读取该路径下的标定文件，当该路径下的标定文件发生更新时，模块读取的标
定文件就是最新的。  
（5）模块结果  
模块结果包括模块状态、剩余标定次数、旋转轴图像点、旋转中心物理点、旋转像素平均
误差、旋转真实平均误差。  
 



<!-- page 432 -->
HIKROBOT 
 
423 
 
 
 
模块状态：运行成功为1，运行失败为0 
剩余标定次数：该值等于标定总次数减去标定已运行次数，值为0 表示旋转标定结束  
旋转轴图像点：旋转轴中心的像素坐标值  
旋转中心物理点：旋转轴中心的物理坐标值  
旋转像素平均误差：旋转标定的拟合平均误差，单位为像素  
旋转真实平均误差：旋转标定的拟合平均误差，单位为平移标定的物理运动量(通常为m
m) 
问题根因  
不熟悉旋转标定模块。  
 
 



<!-- page 433 -->
HIKROBOT 
 
424 
 
 
1.2.3 单点抓取：单点抓取模块的使用方法
  
描述  
环境：VM4.2 
现象：VM 二次开发如何使用单点抓取模块？  
解答  
适用场景：单相机拍物料的抓取场景。  
标定方式：单相机与机构做平移标定(9 点标定)或平移旋转标定(12 点标定)。前者适用于
吸嘴与旋转轴共轴的场景，后者适用于吸嘴与旋转轴不共轴的场景）。  
限制条件：不支持多相机联立坐标系、分离轴抓取、相机拍照位变化(可后接变量计算模块
实现)等场景。  
模块界面如下：  



<!-- page 434 -->
HIKROBOT 
 
425 
 
 



<!-- page 435 -->
HIKROBOT 
 
426 
 
 
 
（1）输入方式  
确定标定类型是平移标定还是平移旋转标定，确定是按点输入还是按坐标输入。可以订阅
前序模块的输出结果，也可以手动输入。  
（2）像素点  
在抓取场景中，需要依次输入图像基准点和图像运行点。  
基准像素点的输入步骤如下图所示，输入方式需选择“按坐标”：  



<!-- page 436 -->
HIKROBOT 
 
427 
 
 
 
 
 
基准点创建成功时，弹窗如下图所示：  
 
 



<!-- page 437 -->
HIKROBOT 
 
428 
 
 
 
运行像素点的输入步骤如下图所示：  
 
 
 
（3）示教抓取物理点：物料在基准位置时，机构抓取物料的绝对物理坐标  
示教拍照物理点：物料在基准位置时，机构携带相机拍照的绝对物理坐标  
如无需示教抓取物理点、示教拍照物理点，则手动输入0  



<!-- page 438 -->
HIKROBOT 
 
429 
 
 
 
 
 
（4）标定文件  



<!-- page 439 -->
HIKROBOT 
 
430 
 
 
 
 
 
加载本地标定文件，支持.xml 和.iwcal 格式。刷新信号的填写说明为：空或0 时，表示该
模块读取标定文件后，便不再更新，一直使用第一次读取的标定文件；非零时，表示该模
块运行时会读取该路径下的标定文件，当该路径下的标定文件发生更新时，模块读取的标
定文件就是最新的。  
（5）模块结果  



<!-- page 440 -->
HIKROBOT 
 
431 
 
 
模块结果分为相对坐标及绝对坐标，绝对坐标为机构抓取的绝对物理位置。  
 
问题根因  
不熟悉单点抓取模块。  
 
 



<!-- page 441 -->
HIKROBOT 
 
432 
 
 
1.2.4 单点纠偏：单点纠偏模块的使用方法
  
描述  
环境：VM4.2 
现象：VM 二次开发如何使用单点纠偏模块？  
解答  
适用场景：单相机拍物料的纠偏场景。  
标定方式：单相机与机构做平移标定(9 点标定)或平移旋转标定(12 点标定)。前者适用于
吸嘴与旋转轴共轴的场景，后者适用于吸嘴与旋转轴不共轴的场景）。  
限制条件：不支持多相机联立坐标系、分离轴纠偏、相机拍照位变化(可后接变量计算模块
实现)等场景。  
模块界面如下：  



<!-- page 442 -->
HIKROBOT 
 
433 
 
 



<!-- page 443 -->
HIKROBOT 
 
434 
 
 
 
（1）输入方式  
确定标定类型是平移标定还是平移旋转标定，确定是按点输入还是按坐标输入。可以订阅
前序模块的输出结果，也可以手动输入。  
（2）像素点  
在纠偏场景中，需要依次输入图像基准点和图像运行点。  
基准像素点的输入步骤如下图所示，输入方式需选择“按坐标”：  



<!-- page 444 -->
HIKROBOT 
 
435 
 
 
 
 
 
       基准点创建成功时，弹窗如下图所示：  
 



<!-- page 445 -->
HIKROBOT 
 
436 
 
 
运行像素点的输入步骤如下图所示：  
 
（3）示教物理点：物料在基准位置时的机构绝对物理坐标  
如无需示教物理点，则手动输入0  



<!-- page 446 -->
HIKROBOT 
 
437 
 
 
 
 
 
（4）标定文件  
 
加载本地标定文件，支持.xml 和.iwcal 格式。刷新信号的填写说明为：空或0 时，表示该
模块读取标定文件后，便不再更新，一直使用第一次读取的标定文件；非零时，表示该模



<!-- page 447 -->
HIKROBOT 
 
438 
 
 
块运行时会读取该路径下的标定文件，当该路径下的标定文件发生更新时，模块读取的标
定文件就是最新的。  
（5）模块结果  
模块结果分为相对坐标及绝对坐标，绝对坐标为机构纠偏的绝对物理位置。  
 
问题根因  
不熟悉单点纠偏模块。  
 
 



<!-- page 448 -->
HIKROBOT 
 
439 
 
 
1.2.5 单点对位：单点映射对位模块的使用
方法  
描述  
环境：VM4.2 
现象：VM 二次开发如何使用单点映射对位模块？  
解答  
适用场景：上相机拍目标，下相机拍对象的对位贴合场景。  
标定方式：上相机到下相机做映射标定，下相机与机构做平移旋转标定(12 点标定)。  
限制条件：不支持单相机(循环)对位贴合，上、下相机各自基准对位等场景。  
模块界面如下：  



<!-- page 449 -->
HIKROBOT 
 
440 
 
 



<!-- page 450 -->
HIKROBOT 
 
441 
 
 
 
（1）输入方式  
确定是按点输入还是按坐标输入，可以订阅前序模块的输出结果，也可以手动输入。  
（2）像素点  
在单点映射对位场景中，需要依次输入对象像素点和目标像素点，输入方式选择“按坐
标”：  



<!-- page 451 -->
HIKROBOT 
 
442 
 
 
 
 
 
给目标像素直线起点/终点的X、Y 坐标订阅数值(映射后夹角会变化，因此需要将目标
图像中指定直线映射到对象坐标系再求目标点的角度)，输入如下图所示：  



<!-- page 452 -->
HIKROBOT 
 
443 
 
 
 
 
 
（3）示教抓理点：映射标定时机构反向吸取标定板的绝对物理坐标  
如无需示教物理点，则手动输入0  



<!-- page 453 -->
HIKROBOT 
 
444 
 
 
 
 
 
（4）标定文件（映射标定文件将上相机中目标像素映射到下相机的像素坐标系中，N 点
标定文件是将下相机的像素坐标映射到机构的物理坐标系中）  
 
加载本地标定文件，支持.xml 和.iwcal 格式。刷新信号的填写说明为：空或0 时，表示
该模块读取标定文件后，便不再更新，一直使用第一次读取的标定文件；非零时，表示该模
块运行时会读取该路径下的标定文件，当该路径下的标定文件发生更新时，模块读取的标定
文件就是最新的。  



<!-- page 454 -->
HIKROBOT 
 
445 
 
 
（5）模块结果  
模块结果分为相对坐标及绝对坐标，绝对坐标为机构对位的绝对物理位置。  
 
问题根因  
不熟悉单点映射对位模块。  
 
 



<!-- page 455 -->
HIKROBOT 
 
446 
 
 
1.2.6 流程配置：配置流程的输入、输出与
显示的方法 
描述 
环境：VM4.2  
现象：如何在VM 中给流程配置输入设置、输出设置与显示设置  
解答  
下面以在流程2 订阅流程1 中图像为例介绍配置流程输入、流程输出与显示设置  
1、如图方案中存在两个流程，流程1 与流程2 ，选择流程1 前的小扳手  
 
2、如图配置流程1 的输出图像为图像源1 的图像  



<!-- page 456 -->
HIKROBOT 
 
447 
 
 
 
3、在点击橘色箭头所指图标，将流程1 与流程2 连接。  
 
4、再如步骤1 将流程2 的输入订阅为流程1 是输出  



<!-- page 457 -->
HIKROBOT 
 
448 
 
 
 
5、然后在流程2 中的任意模块的模块输入中就可以订阅到流程2 的输入图像 
 
6、同理可配置显示设置 



<!-- page 458 -->
HIKROBOT 
 
449 
 
 
 
问题根因 
不熟悉VM 配置流程输入、输出与显示的方法 
 
 



<!-- page 459 -->
HIKROBOT 
 
450 
 
 
1.2.7 数据队列：多流程间传图及协作的方法  
描述  
环境：VM4.2 
现象：如何两个流程执行得到的图像拼接输出（流程1 和流程2 都执行完毕后，将两个流
程输出的图像传输到流程3 中拼接）？  
解答  
1 首先需要拖拽数据队列模块并配置需要入队的列，数据类型为IMAGE，然后配置触发
流程（触发流程逻辑为所有队列都有数据时才会触发列表中的流程）。  
 
2 配置流程1 和流程2：流程1 和流程2 中配置发送数据模块，将图像数据传入数据队
列。  



<!-- page 460 -->
HIKROBOT 
 
451 
 
 
 
 
3 配置流程3：流程3 中配置接收数据模块，取出数据队列中的图像数据并拼接。  



<!-- page 461 -->
HIKROBOT 
 
452 
 
 
 
问题根因  
不熟悉数据队列的使用方法。  
 
 



<!-- page 462 -->
HIKROBOT 
 
453 
 
 
1.2.8 脚本模块：脚本模块保存图像的方法
  
描述  
环境：VM4.0 及以上  
现象：如何使用脚本模块保存前序模块传入的图像？  
解答  
C# 
public bool Process() 
{ 
    ImageData DetImg = new ImageData(); 
    GetImageValue("DetImg",ref DetImg); 
    byte[] bytes = new byte[1024 * 1024]; 
    bytes = DetImg.Buffer; 
         
    int wid = DetImg.Width; 
    int hei = DetImg.Heigth; 
    Mat src = new Mat(); 
    if (ImagePixelFormate.MONO8 == DetImg.PixelFormat) 



<!-- page 463 -->
HIKROBOT 
 
454 
 
 
    { 
        int dataLen = wid * hei; 
        src.Create(hei, wid, MatType.CV_8UC1); 
        Marshal.Copy(DetImg.Buffer, 0, src.Ptr(0), dataLen); 
    } 
    else if (ImagePixelFormate.RGB24 == DetImg.PixelFormat) 
    { 
        int dataLen = wid * hei * 3; 
        src.Create(hei, wid, MatType.CV_8UC3); 
        Marshal.Copy(DetImg.Buffer, 0, src.Ptr(0), dataLen); 
        Cv2.CvtColor(src, src, ColorConversionCodes.RGB2BGR); 
    } 
    string savePath = "E:\\Test";   // 存图路径 
 
  string imageName = "1.jpg";   // 存图名称 
    if (!Directory.Exists(savePath)) 
    { 
        Directory.CreateDirectory(savePath); 
    } 
    Cv2.ImWrite(savePath + "\\" + imageName, src); 
    src.Release(); 
    return true; 



<!-- page 464 -->
HIKROBOT 
 
455 
 
 
} 
问题根因  
不熟悉使用脚本模块调用第三方库的方法。  
 
 



<!-- page 465 -->
HIKROBOT 
 
456 
 
 
1.2.9 创建基准：全局触发配置模块动作的
方法 
描述 
环境：VM4.2  
现象：如何通过全局触发模块动作？例如创建基准。  
解答 
1.打开单点抓取模块路径下的SinglePointGrabModuAlgorithmTab.xml 配置文件，在It
em 集合下面加上Command 节点。 
<Command Name="BasicInit" NameSpace="Standard"> 
 
<Description> BasicPoitnInit </Description> 
      <DisplayName> BasicPoitnInit </DisplayName> 
      <Visibility>Expert</Visibility> 
      <AccessMode>Rw</AccessMode> 
      <CustomVisible>False</CustomVisible> 
 
<SupportCommTrigger>True</SupportCommTrigger> 
</Command> 
 
2.保存配置文件，重新启动VM 



<!-- page 466 -->
HIKROBOT 
 
457 
 
 
可以在全局触发处配置模块动作处可以看到相应模块的动作，如果需要显示中文，将配置
节点中的DisplayName 属性的值添加到多语言。 
 
问题根因 
不熟悉如何配置从而触发模块动作 
 
 



<!-- page 467 -->
HIKROBOT 
 
458 
 
 
1.2.10 条件检测：条件检测结果显示颜色
为模块最终检测状态的方法 
描述 
环境：VM4.2  
现象：如何将条件检测结果显示颜色设置为模块最终检测状态？ 
 
解答 
1.修改条件检测模块结果显示内容为条件检测结果。 



<!-- page 468 -->
HIKROBOT 
 
459 
 
 
 
2.修改条件检测模块IfModuleDisplay.xml 文件的Status 节点，将映射改为NIfResult. 
 
 
 



<!-- page 469 -->
HIKROBOT 
 
460 
 
 
问题根因 
不熟悉模块xml 文件的使用。 
 
 
 



<!-- page 470 -->
HIKROBOT 
 
461 
 
 
第2 章 VM 二次开发 
2.1 环境配置类 
2.1.1 环境配置：基于Csharp 二次开发环
境配置方法  
描述  
环境：VM4.2 + VS2013 及以上，注意，只要VS2013 有.NET Framework4.6.1，就可
以使用VS2013 进行VM SDK 开发。  
现象：基于C#如何进行VM 二次开发环境配置？  
解答  
WinForm、WPF 开发平台，两者二次开发环境配置步骤基本一致。  
第一步：新建项目。使用VS 新建一个窗体应用程序，以WinForm 为例，框架选择.NET 
Framework4.6.1，接着打开项目属性页面，取消勾选【首选32 位】，然后重新编译项
目。最后，关闭项目。 



<!-- page 471 -->
HIKROBOT 
 
462 
 
 
 
 
第二步：添加引用。使用导入工具来添加引用，工具路径VisionMaster4.2.0\Developm
ent\V4.x\ComControls\Tool\ImportRef.exe。操作步骤：选择项目所在的路径，勾选需
要引用的模块，也可以全部引用。点击确定按钮，待进度条100%后，打开项目，可以发
现项目的引用中出现VM 二次开发相关的dll。  



<!-- page 472 -->
HIKROBOT 
 
463 
 
 
 



<!-- page 473 -->
HIKROBOT 
 
464 
 
 
 
第三步：添加控件。在WinForm 窗体程序中，打开工具箱，鼠标右击【所有Windows
窗体】，点击【选择项】，弹出.NET Framework 组件窗口，浏览VM4.2 的安装路径文
件夹：VisionMaster4.2.0\Development\V4.x\ComControls\Assembly，选择VMCon
trols.Winform.Release.dll，添加后工具箱出现VM 二次开发控件。  



<!-- page 474 -->
HIKROBOT 
 
465 
 
 
 
控件分别为：  
VmFrontend 前端运行界面控件  
VmGlobalTool 全局模块控件  
VmMainView 主界面控件  
VmParams 参数配置控件  
VmParamsConfigWithRender 参数配置带渲染控件  
VmProcedure 流程配置控件  
VmRenderControl 渲染控件  
VmSingleModuleSet 独立Group 控件  
用户可将控件拖拽到窗体中使用。  



<!-- page 475 -->
HIKROBOT 
 
466 
 
 
如上所述为WinForm 窗体应用程序添加控件的方法，下面介绍WPF 添加控件的方法。  
在WPF 窗体应用程序->工具箱中点击【选择项】，弹出WPF 组件窗口，接着浏览VM4.
2 的安装路径文件夹：VisionMaster4.2.0\Development\V4.x\ComControls\Assembl
y，选择VMControls.WPF.Release.dll。拖拉控件至窗口中，xaml 中代码自动生成。  
 
添加完依赖库引用和控件后，启动程序，效果如下图所示。  
用户可在流程配置控件中新建流程，搭建和调试视觉方案。同时，用户可在程序中引用平
台库（using VM.Core 和using VM.PlatformSDKCS）和模块库（查阅VisionMaster4.
2.0\Development\V4.x\Documentations 中的开发手册查看模块库名称）来实现业务代
码开发。  



<!-- page 476 -->
HIKROBOT 
 
467 
 
 
 
问题根因  
不熟悉基于C#的VM 二次开发环境配置步骤  
 
 



<!-- page 477 -->
HIKROBOT 
 
468 
 
 
2.1.2 环境配置：基于MFC 二次开发环境
配置方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：基于MFC 如何进行VM 二次开发环境配置？  
解答  
第一步：新建项目。以MFC+ VS2013 为例。应用程序类型选择：基于对话框。  
 



<!-- page 478 -->
HIKROBOT 
 
469 
 
 
第二步：配置VC++目录。打开项目属性页，平台选择x64。依次配置头文件目录、库文
件目录和附加依赖项。  
其中，头文件目录需要配置模块头文件。库目录选择win64\C。附加依赖项选择iMVS-60
00PlatformSDK.lib。  
 



<!-- page 479 -->
HIKROBOT 
 
470 
 
 
 
 
第三步：添加控件头文件和源文件。将控件头文件、源文件拷贝到工程目录下(本例为VS2
013 创建的程序，控件文件路径VisionMaster4.2.0\Development\V4.x\ComControls\I
ncludes\VS2013，VS2017 创建的程序则选择VS2017 文件夹)，拷贝之后再添加头文件
和源文件。  



<!-- page 480 -->
HIKROBOT 
 
471 
 
 
 
第四步：添加VM 封装的ActiveX 控件，这些控件在VM 安装时已经注册，可以直接选
择。  
 
第五步：在程序中包含头文件，并进行控件的绑定与初始化。  



<!-- page 481 -->
HIKROBOT 
 
472 
 
 
 
定义控件变量：  
 
private: 
 
CVmMainViewControlInterface m_MainViewctr; 
控件变量绑定界面：  
 
void CVMMFCApplication1Dlg::DoDataExchange(CDataExchange* pDX) 
{ 
 
CDialogEx::DoDataExchange(pDX); 
 
DDX_Control(pDX, IDC_VMUSERCONTROL1, m_MainViewctr); 
} 



<!-- page 482 -->
HIKROBOT 
 
473 
 
 
通过控件变量给控件初始化：  
 
BOOL CVMMFCApplication1Dlg::OnInitDialog() 
{ 
 
CDialogEx::OnInitDialog(); 
 
// 将“关于...”菜单项添加到系统菜单中。 
             … 
 
// TODO: 在此添加额外的初始化代码 
 
try 
 
{ 
 
 
m_MainViewctr.GetObjectPointer(); 
 
} 
 
catch (CVmException e) 
 
{} 
 
return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE 
} 
至此，完成环境配置。启动程序，效果如下图所示。  
用户可在主界面控件中新建流程，搭建和调试视觉方案。用户可在程序中引用平台库和模
块库（查阅VisionMaster4.2.0\Development\V4.x\Documentations 中的开发手册查
看模块库名称）来实现业务代码开发。  



<!-- page 483 -->
HIKROBOT 
 
474 
 
 
 
问题根因  
不熟悉基于MFC 的VM 二次开发环境配置步骤  
 
 



<!-- page 484 -->
HIKROBOT 
 
475 
 
 
2.1.3 环境配置：基于Qt 二次开发环境配
置方法  
描述  
环境：VM4.2 + Qt5.14  
现象：基于Qt 如何进行VM 二次开发环境配置？  
解答  
第一步：新建项目。打开QTCreate，编译器推荐选择MSVC2017 64bit。  
 



<!-- page 485 -->
HIKROBOT 
 
476 
 
 
 
第二步：配置外部库。打开后缀为.pro 的文件，在代码区域鼠标右击，选择【添加库】，
选择【外部库】，选择VM 安装路径下的相关库文件和包含路径， 效果如下图所示。  
 
为了控件能正常显示，在此代码区域头部添加一句QT +=axcontainer。  



<!-- page 486 -->
HIKROBOT 
 
477 
 
 
第三步：添加控件头文件和源文件。将控件头文件、源文件拷贝到工程目录下(本例为VS2
013 创建的程序，控件文件路径VisionMaster4.2.0\Development\V4.x\ComControls\I
ncludes\QT)，拷贝之后再添加头文件和源文件。  
 
第四步：添加VM 封装的ActiveX 控件，这些控件在VM 安装时已经注册，可以直接选
择。  
 
第五步：在程序中包含头文件，并进行控件的初始化。  



<!-- page 487 -->
HIKROBOT 
 
478 
 
 
 
 
至此，完成环境配置。启动程序，效果如下图所示。 注意加载方案时，在控件上显示
方案，则需要在控件初始化前，调用CreateSolutionInstance(); 



<!-- page 488 -->
HIKROBOT 
 
479 
 
 
 
用户可在主界面控件中新建流程，搭建和调试视觉方案。用户可在程序中引用平台库和模
块库（查阅VisionMaster4.2.0\Development\V4.x\Documentations 中的开发手册查
看模块库名称）来实现业务代码开发。  
问题根因  
不熟悉基于Qt 的VM 二次开发环境配置步骤  
 
 



<!-- page 489 -->
HIKROBOT 
 
480 
 
 
2.1.4 用户权限：普通以EXE 方式启动Se
rver 的方法  
描述  
环境：VM4.2 +VS2013 及以上  
现象：当客户二次开发程序，需要以Windows 普通用户权限调用Vm 做视觉处理，需要
将Server 以EXE 方式启动。  
解答  
1）C#二次开发：修改二次开发程序的xxx.exe.config 配置文件，在“AppSettings”里
面增加以下两条信息。下图以圆查找demo 程序为例。注意“ServerPath”是该电脑上S
erver 的绝对路径，要填正确。  
 



<!-- page 490 -->
HIKROBOT 
 
481 
 
 
 
2）C++二次开发：在所有VM 二次开发接口前（如程序的入口处）调用IVmSolution.h
文件中的SetServerPath 接口，设置服务的绝对路径。  
举例：SetServerPath(“C:\\Program Files\\VisionMaster4.0.0\\Applications\\Server
\\VisionMasterServer.exe”); 
问题根因  
不熟悉普通用户权限二次开发的配置。  
 
 



<!-- page 491 -->
HIKROBOT 
 
482 
 
 
2.1.5 环境配置：程序启动后报错的通用方
法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：二次开发过程中，通常会遇到启动后直接报错VM.Core.xxxx 类型初始值设定引发
异常，或者启动后控件是黑色，或者模块相关报错，或者启动后加载方案报错，或者获取
不到流程列表，或者流程和结果为空等等。  
 
解答  
启动时报错一般时环境问题，启动后的相关报错有可能是环境问题。二次开发，首先要确
保代码无误，再从其他角度排查问题。  
1. 确保方案未损坏：VM 能正常打开，且能打开方案；  



<!-- page 492 -->
HIKROBOT 
 
483 
 
 
2. 确保环境配置步骤正确：是否插好加密狗；是否以管理员身份运行VS 再打开项
目；项目框架是否是4.6.1（4.7 或4.8，win10 之外其它未作测试可能存在问
题），项目属性的32 位是否取消勾选；程序启动前关闭VM 软件；  
3. 确保dll 路径正确：VM4.2SDK 开发不需拷贝操作，所以项目exe 生成路径无VM
SDK 的dll；但打完补丁，最好运行下unGAC.bat 和GAC.bat；补充：VM4.0SD
K 开发在打完补丁后，重新拷贝一次；  
4. 确保版本适配：多版本时，方案和程序的升级是否适配当前VM 版本和接口函
数。  
通用手段：  
1. 在界面拖个显示方案的控件，比如主界面控件（VmMainViewConfigControl），观察
方案加载、运行及结果获取；  
2. 使用trycatch 捕获异常码，并在手册中查找异常码对应的内容；  
C# 
try{ }catch(VmException ex) 
{MessageBox.Show(Convert.ToString(ex.errorCode, 16));} 
catch(Exception ex) 
{MessageBox.Show(ex.Message.ToString());} 
3. 确保自带的Demo 能正常运行，或者在相同的操作下能正常运行；  



<!-- page 493 -->
HIKROBOT 
 
484 
 
 
4. 程序中使用判空操作；关闭时释放VM 资源；断点调试；线程同步异步的概念掌握。  
5. 偶发问题、内存泄漏或崩溃问题，复现问题后，用工具打包日志给研发。  
问题根因  
不熟悉二次开发程序启动后报错排查方法。  
 
 



<!-- page 494 -->
HIKROBOT 
 
485 
 
 
2.1.6 VM 路径：通过注册表获取VM 安装
路径的方法  
描述  
环境：VM4.0 及以上 +VS2013 及以上  
现象：如何后台自动获取VM 的安装路径。  
解答  
C# 
//从注册表读取VM 安装路径 
public string GetVisionMasterInstallPath() 
{ 
    try 
    { 
        RegistryKey Key = RegistryKey.OpenBaseKey(RegistryHive.Loc
alMachine, RegistryView.Registry64); 
        RegistryKey myreg = Key.OpenSubKey(@"SOFTWARE\WOW6
432Node\Microsoft\Windows\CurrentVersion\Uninstall\VisionMaster_" 
+ "4.2.0", RegistryKeyPermissionCheck.Default,System.Security.AccessC
ontrol.RegistryRights.FullControl); 



<!-- page 495 -->
HIKROBOT 
 
486 
 
 
        string VisionMasterInstallPath = myreg.GetValue("DisplayIcon
").ToString(); 
        Key.Close(); 
        myreg.Close(); 
        return VisionMasterInstallPath.Replace("Applications\\VisionM
aster.exe", ""); ; 
    } 
    catch (System.Exception ex) 
    { 
        throw ex; 
    } 
}      
问题根因  
不熟悉如何获取VM 注册表路径  
 
 



<!-- page 496 -->
HIKROBOT 
 
487 
 
 
2.1.7 第三方库：格式化模块参数配置界面
乱码的解决方法 
描述 
环境：VM4.0+VS2013 及以上 
现象：二次开发时，格式化配置界面乱码或无法打开脚本，变量计算，全局脚本配置界面。
  
解答 
1. 查看App.config 配置文件，在配置文件中可以看到针对Json 库做了版本重定向，统
一使用13.0.0.0 的版本，这里导致VM 中使用Json 库时尝试去寻找13.0.0.0 导致失败报
错。通常是因为VM 二次开发时，使用了第三方库（例如HslCommunication.dll），导
入了这种配置。VM 版本界面默认使用的Json 库版本是11.0.0.0。 
 
2.解决办法 
找寻13.0.0.0 版本的Json 库拷贝到二次开发的exe 的同级目录下，使得VM 和第三方库
所需要的json 都自动引用这个版本的Json 库。 



<!-- page 497 -->
HIKROBOT 
 
488 
 
 
问题根因 
不熟悉如何解决格式化模块乱码 
2.1.8 第三方库：控件与三方样式库冲突问
题解决方法 
描述 
环境：VM4.0 及以上 + VS2013 及以上 
现象：当使用VM 进行二次开发时，VM 提供的VmMainViewConfigControl 控件或Vm
ParamsConfigControl 控件与自身引用的第三方MaterialDesign 样式库产生冲突，导致
VM 控件中字体显示异常。 
 
针对该控件冲突问题，猜测是由于VM 的控件中未对其中的TextBox 的Fontsize 属性进行
设置，导致针对整个程序或用户自定义控件引用MaterialDesign 样式库时，样式库中的样
式覆盖VM 控件中相应样式，造成字体显示异常。 
解答 
针对该问题有以下几种解决方案： 
VM 修改相关控件的样式以避免冲突。 



<!-- page 498 -->
HIKROBOT 
 
489 
 
 
修改MaterialDesign 样式库中相关样式以避免冲突。 
修改MaterialDesign 样式库的引用方式。 
方法1：VM 修改相关控件的样式以避免冲突。但是，由于这是三方库与VM 控件样式设置
不同导致的冲突问题，而不同的三方库可能会引发不同位置的冲突问题，因此该做法无法解
决开发者的根本问题。 
方法2：对MaterialDesign 样式库中的相关样式进行修改以避免与VM 控件产生冲突，该
方法可以由用户自行修改相应冲突的代码，且不需要更改现有程序，如果能实现，确实不失
为一种很好的解决办法。由于MaterialDesign 样式库为第三方库，所以使用反编译工具，
对该样式库进行反编译，之后找到对应冲突处的代码。找到该样式库下的资源文件夹，找到
TextBoxBase 样式设置。 
 
在找到相关的源代码位置后，发现在反编译出来的样式库当中无法对资源文件样式进行修
改，所以当前方案行不通。 
方法3：改变对MaterialDesign 样式库的引用方式，在发现该问题之后，首先想到的其实



<!-- page 499 -->
HIKROBOT 
 
490 
 
 
是更改程序对三方库的引用方式，改变对整个程序引用该三方库，仅在需要使用该样式的自
定义用户控件中对该样式库进行引用。然而这样做需要对VM 控件及其他控件做隔离处理，
对程序改动太大，所以并不实用。 
最终解决办法：由于在方法2 中已经对MaterialDesign 库完成了反编译，且找到了对应的
源代码，最终考虑在自定义用户控件中对TextBox 的相关样式进行重新定义，覆盖掉Mat
erialDesign 库中引发冲突的部分，最终使该问题成功得到解决。 
代码片段： 
 
这里提供了一种在不对程序进行太大改动的情形下，控件库样式冲突的解决思路。控件库冲
突是一种比较常见的问题，在其他客户进行VM SDK 开发过程中也同样遇到过类似的问题，
使用该方法均可以快速进行问题的定位及解决。 
问题根因 
不熟悉VM 二开过程中，发生样式库冲突的解决方法。 
 
 



<!-- page 500 -->
HIKROBOT 
 
491 
 
 
2.1.9 用户日志：用户日志打印的方法 
描述 
环境：VM4.0+VS2013 及以上 
现象：VMSDK 开发时，如何打印用户日志？  
解答 
1.配置日志xml，命名为log4Net.config，放在exe 的同级目录下。 
<?xml version="1.0" encoding="utf-8" ?> 
 
<configuration> 
  <configSections> 
    <section name="log4net" type="log4net.Config.Log4NetConfigurationSectionHandler, log
4net"/> 
  </configSections> 
   
  <log4net> 
    <appender name="RollingLogFileAppender" type="log4net.Appender.RollingFileAppender
"> 
   
      <!--日志路径--> 
      <param name= "File" type="log4net.Util.PatternString" value= ".\user\user.log"/> 
      <!--是否是向文件中追加日志--> 
      <param name= "AppendToFile" value= "true"/> 
 
    <!--编码--> 
 
    <param name="Encoding" value="utf-8" /> 
      <!--log 保留天数--> 
      <param name= "MaxSizeRollBackups" value= "5"/> 
      <!--日志文件名是否是固定不变的--> 
      <param name= "StaticLogFileName" value= "false"/> 
      <!--日志文件名格式为:2008-08-31.log--> 
      <param name= "DatePattern" value= "yyyy-MM-dd&quot;.log&quot;"/> 
      <!--日志根据日期滚动--> 
      <param name= "RollingStyle" value= "Size"/> 
 
    <param name="MaximumFileSize" value="10MB"/> 
 
   
<!--多进程同时写入时加锁--> 
 
    <lockingModel type="log4net.Appender.FileAppender+MinimalLock" /> 
      <layout type="log4net.Layout.PatternLayout"> 



<!-- page 501 -->
HIKROBOT 
 
492 
 
 
        <!-- <param name="ConversionPattern" value="%d [%t] %-5p %c - %m%n %logge
rname" /> --> 
 
 
    <!--<conversionPattern value="Time：%date ThreadID:[%thread] Lev
el：%-5level MSG：%message%newlineNUM：%-5L FILE：%F%newline" />--> 
 
 
    <conversionPattern value="%date{yyyy-MM-dd HH:mm:ss.fff} %-5lev
el [%thread] [%class::%method@%L] %message%newline%newline" /> 
      </layout> 
 
    <filter type="log4net.Filter.LoggerMatchFilter"> 
        <loggerToMatch value="UserLog" /><!--过滤器--> 
      </filter> 
      <filter type="log4net.Filter.DenyAllFilter" /> 
    </appender> 
 
 
 
    <root> 
      <!--(高) OFF > FATAL > ERROR > WARN > INFO > DEBUG > ALL (低) --> 
      <level value="info" /> 
 
    <appender-ref ref="RollingLogFileAppender"/>  
 
    <appender-ref ref="UserRollingLogFileAppender"/>  
    </root> 
  </log4net> 
</configuration> 
2.生成用户日志类别，读取log4Net.config 文件。 
using log4net; 
using log4net.Appender; 
using System; 
using System.Collections.Generic; 
using System.Linq; 
using System.Reflection; 
using System.Text; 
using System.Threading.Tasks; 
 
namespace VMTestB3 
{ 
    public class LogHelper 
    { 
        public static readonly ILog objLog = null; 
        static LogHelper() 
        { 
            try 
            { 



<!-- page 502 -->
HIKROBOT 
 
493 
 
 
                string stmp = Assembly.GetExecutingAssembly().Location; 
                stmp = stmp.Substring(0, stmp.LastIndexOf('\\') + 1); 
                string path = stmp + "log4Net.config"; 
                log4net.Config.XmlConfigurator.ConfigureAndWatch(new System.IO.FileInfo(p
ath)); 
                objLog = log4net.LogManager.GetLogger("UserLog"); 
            } 
            catch (Exception ex) 
            { 
                //程序异常 
            } 
        }      
        public void Info(object message) 
        { 
            objLog?.Info(message); 
            //objLog?.Error(message); 
        } 
    } 
} 
3.在主函数中进行调用，打印日志到项目生成路径\ user\user.log 
LogHelper loguser=new LogHelper(); 
loguser.Info("加载方案............................................."); 
VmSolution.Load(textBoxSolPath.Text, ""); 
问题根因 
不熟悉生成用户日志 
 
 



<!-- page 503 -->
HIKROBOT 
 
494 
 
 
2.1.10 环境配置：基于LabView 二次开发
环境配置方法 
描述 
环境：VM4.2 +labview2015 
现象：基于LabView 如何进行VM 二次开发环境配置？ 
解答 
1 预备知识 
在 LabVIEW 中调用第三方库函数，有这么几种方式，如下： 
1.1 调用库函数方式 
在 LabVIEW 的程序面板中，右键选择“互连接口”，接着选择“库与可执行程序”，如下
图所示： 
 
接着选择调用库函数节点，接着右键菜单中选择“配置”，在随后弹出的对话框中， 选择
库函数 DLL 所在路径， 选择对应的 DLL ， 这里以调用海康渲染库MVRenderPlus.dll 



<!-- page 504 -->
HIKROBOT 
 
495 
 
 
为例，如下图所示： 
 
选择对应的函数名，配置对应的函数的参数和返回值即可。到这一步就结束了，这种方式
的调用适合调用 C/C++编写的独立的动态库，我们 VM 之前的版本，例如VM3.4 用这
种方式调用就足够了，只需要选择 imvs6000-PlatformSDK.dll,然后选择对应的 API 函
数，比如 LoadSolution 这样的 API，配置好正确的输入参数和返回值就行了。不过这种
方式有一个缺憾，就是调用者必须事先对要调用的 SDK 接口有一个比较全面的了解，必
须掌握 LabVIEW 编程语言之外的语言，比如掌握了一定的 C 语言编程基础，拿到DLL 
文件配套的头文件（.h  文件），对照着头文件配置输入参数和返回值。 
1.2 使用 ActiveX 容器方式调用 
这种方式对遵循 COM 标准编写出来的动态库是很方便的，COM 是微软开发的一套跨语
言的二进制调用标准，基于 COM 编写的动态库，不管这个动态库是用什么语言开发的
（C++，VB，VB.net，C#, Delphi），都能被其他语言调用（如 Java，Python 等），甚
至可以在网页上运行。ActiveX 容器的调用如下图所示： 



<!-- page 505 -->
HIKROBOT 
 
496 
 
 
 
以调用 VM SDK 中的 VmMainView 控件为例，在 LabVIEW 的 ActiveX 选板中选择
“ 打开自动化” ，然 后 再 随 后 弹 出 的 对 话 框 中 ， 浏览 ， 然后选择VmM
ainViewControlWinform Version 1.0 ,如下如所示： 
 
通过选择 VmMainViewControlInterface，来创建控件的引用实例，接着在选板中选择
“ 调用节点” ， 将引用指向刚才创建的实例， 选择调用方法， 例如调用“GetObject
Pointer”, 如下图所示： 



<!-- page 506 -->
HIKROBOT 
 
497 
 
 
 
1.3 使用.net 容器的方式调用 
在  Lab VIEW  中通过.net  容器调用第三方库是最简单的方式（当然前提是第三库有.
Net 封装），幸运的是，海康机器人的算法平台 SDK 刚好有.net 的封装，使用.net 的封
装库，调用者不需要管理内存（绝大多数情况下不需要关心内存的申请和释放），更加激动
人心的是，Lab VIEW 开发者调用 VM SDK，是不需要事先了解 SDK 内部 的工作原
理，不需要深入理解它的框架，就可以快速开发属于自己的视觉应用。LabVIEW 的.net 
容器调用方式如下所示： 
 
在构造器节点中创建 VMSolution 的实例，接着调用属性节点来操作 VM 的一些常用方
法，如加载方案，加载流程，运行方案，运行流程，获取模块结果等等。同时， 由于VM
 SDK 将方案中的所有模块结果和运行状态都和渲染控件做了数据绑定，也就是模块结果



<!-- page 507 -->
HIKROBOT 
 
498 
 
 
数据发生改变，会立刻在渲染控件上得到呈现，是典型的数据和界面代码分离的一种架
构，这种模式对 LabVIEW 开发者很友好，因为 LabVIEW 开发者将不需要调用低级的绘
图和像素操作 API（甚至都不需要关注渲染是怎么实现的） 就能将结果呈现给客户。 
2 遇到的困境 
如上所述，使用.net 容器调用VM SDK 是我们推荐的方式，但在具体是操作环节，还是
有很多开发者要载跟斗，这里将 LabVIEW 调用 VM4.2（VM4.0 也是差不多的）SDK 
遇到的问题描述一下。 
困境 1：选择 GAC 列表中的 VM 控件库无反应。 
首先，很多开发者是在前面板中，添加了一个.net 容器，然后选择插入.net 控件，如下
图所示： 
 
接着选择 VM SDK 的.net 封装控件，例如 VMControls.Winform.Release.dll，然后展
开VMControls.Winform.Release, 选择 VmMainViewConfigControl 控件，如下如图
所示： 



<!-- page 508 -->
HIKROBOT 
 
499 
 
 
 
选择后按下确定按钮，按下了之后，发现毫无反应，前面板的.net 容器没有任何反应， 
无法开展下一步了，很多开发者进行到这一步基本上要打退堂鼓了，毫无头绪啊。 
困境 2：尝试加载程序集发生错误。 
好，我们继续挣扎一下，我们知道在 VM 的安装目录下，倒是有 VM 控件的DLL，是不
是我们不应该选择 GAC（全局程序集缓存）列表中的 VMControls.Winform.Release.dl
l, 而应该选择 VM 安装目录： 
C:\Program Files\VisionMaster4.2.0\Development\V4.x\ComControls\Libraries\win
64 下的dll 库呢？我们尝试加载上面目录下的 VMMainViewControlWinform，却又遇
到下面的问题，尝试加载程序集时发生错误。 



<!-- page 509 -->
HIKROBOT 
 
500 
 
 
 
3 解决的办法 
首先，好消息是使用.net 容器调用 VM SDK 这条路是行得通的，我们要解决的是，如何
正确的加载 VM.Controls.Winform.Release 这个动态库。 
上面提到的困境1 是因为 LabVIEW 在加载 GAC 中的VM.Controls.Winform.Release.
dll 后，接着加载控件 dll，在初始化控件的时候，发生了异常，这个异常被 SDK 捕捉
到， 但并未抛出，相当于在 VM SDK 内部是知道发生了异常的，但是没有通知到 LabV
IEW, 所以 LabVIEW 无法正确的完成对这个控件的初始化操做的时候，无法向用户传达
出这种异常，表现为.net 容器外观未发生任何变化，没有响应。 
由于 VM 控件的初始化需要依赖的 DLL 不仅仅是 VM.Controls.Winform.Release，还
依赖 VMControls.Interface.dll,VMControls.RenderInterface.dll, VMControls.WPF.dll



<!-- page 510 -->
HIKROBOT 
 
501 
 
 
 等等,因此正确的初始化控件，需要手动做得工作更多。 
为了能正确的初始化 VM 控件，我们可以对 VM 控件做一层浅封装，所谓浅封装，就是
将 VM 控件做成用户自定义控件的方式，在 LabVIEW 中加载用户自定义控件，这种方
式就可以不用 LabVIEW 来自动初始化控件（LabVIEW 会在控件拖动到前面板时自动初
始化）。 
操作步骤： 
第 1 步：将 VM 控件封装成 UserControl。新建一个 C#的用户自定义控件工程，如下
图所示，选择 Windows 桌面项目，接着选择 Windows 窗体控件库，需要注意的是， 
框架必须选择.NET Framework4.6.1 以上。 
 
第 2 步：在VS 工具箱中添加 VM 控件到用户窗体上。如下图所示，在 VS 工具箱中，
找到VmMainViewConfigControl 控件（选择其他控件也可以，这里只是举例说明 Vm
MainView 控件如何浅封装，其他控件的封装方法和这个方式是完全一样的） 



<!-- page 511 -->
HIKROBOT 
 
502 
 
 
 
 
将控件拖动到窗体后，有一个需要注意的点，为了保证控件能够主动适应调用它的宿主  
窗口和在 LabVIEW 中可以通过拖动鼠标改变大小，应该将控件的 Dock 属性设置为“Fi
ll”， 如下图所示： 



<!-- page 512 -->
HIKROBOT 
 
503 
 
 
 
第 3 步：编译工程生成 dll。 
在这一步我们只需要编译工程，不需要写一行代码，是的，不要怀疑，就是不需要编写一
行代码，按下 CTRL+SHIFT+B 组合键直接编译即可。不过在进行编译之前，我们最好对
 UserControl1 做一下重命名，不然生成的控件名称叫做 UserControl1，没有很好指示
性，重命名要用右键，不要直接改名。具体做法是：在代码编辑器中对 UserControl1 这
个单词按下鼠标右键，在弹出菜单中找到重命名，重命名成你想要的名字。 
编译完成后，会在工程所在的 Debug 目录下生成用户控件dll,  默认情况下，VisualStu
dio 会把所有引用到的 dll 都会复制到这个 Debug 目录下，这样，你的工程 Debug 目
录下将会产生一堆 dll 文件，所以为了让生成目录看起来干净整洁一些，我们可以对所有
引用到的 dll 的引用属性“复制到本地”的属性值设置为“False”（当然，你可以不设
置，保持默认的”True”,只是生成的目录下会多出一堆 DLL） 如下图所示： 



<!-- page 513 -->
HIKROBOT 
 
504 
 
 
 
这样，在你的工程 Debug 目录下只会产生一个 dll，就是以工程名命名的控件 dll，例
如下图所示： 
 



<!-- page 514 -->
HIKROBOT 
 
505 
 
 
其中 pdb 文件，是调试信息文件，用来单步调试代码，跟踪断点用的，用户是用不上
的，这个在客户机上可以不需要。直接将 VmMainViewControl 拷贝到用户的 LabVIE
W 程序所在目录即可。 
好了经过上面 3 步，我们再次回到 LabVIEW 中，以.net 容器方式调用 VM 控件，就
不会出现上文提到到困境 1 出现的问题。在 LabVIEW 的前面板中，右键菜单“.NET 与
ActiveX”菜单项下的子菜单“.NET 容器”，添加一个.NET 容器，然后执行：插入.NET 
控件。在随后弹出的窗口中，选择刚才编译好的 VmMainViewControl.dll ,如下图所示： 
 
选择 UserControl1，按下确定按钮，在前面板中按一下运行按钮，接着激动人心的一面
出现了，如下图所示： 



<!-- page 515 -->
HIKROBOT 
 
506 
 
 
 
4 VM SDK 非界面控件的封装 
界面控件调用问题只是解决了一部分问题，VM SDK 中涉及到的非界面的控制，例如， 
加载方案，控制流程运行等等操作，就需要直接调用 VM SDK 的一些 API 函数了，前
文我们提到了可以使用调用库函数方式来调用三方库，这种方式对于 VM3.x 版本是完全
没问题的，因为整个 VM SDK 从头到尾就依赖一个 imvs6000-platform.dll ，但是到
了VM4.x VM 的 SDK 接口已经是完全的面向对象了，VM SDK 已经抽象为 IVMSolut
ion, IVMModule, IVMProcedure 等等一系列的抽象接口，对 VM 的控制被分散在几
十个不同模块之中，不再是一个个全局的静态函数, 因此还是需要将 VM SDK 常用方法
提取出来， 封装成 C#调用接口。 
不过好消息是，我们将 VM SDK 封装,NET 调用接口，仍然是浅封装，因为 VM SDK 



<!-- page 516 -->
HIKROBOT 
 
507 
 
 
本身就有已经开发好的 C#封装接口，我们只需要做浅封装，仅仅是为了让 LabVIEW 能
方便的找到依赖。 
操作步骤 
第 1 步：创建类库工程 
新建一个C#的类库工程，类库取个名字叫 VMOperator（名字随便取）如下图所示： 
 
第 2 步：添加引用 
只需要添加两个dll 的引用，一个是 VM.Core, 一个是VM.PlatformSDKCS,并将它们的
引用属性“复制到本地”设置为 False, 如下图所示： 



<!-- page 517 -->
HIKROBOT 
 
508 
 
 
 
第 3 步：编写类库 
这一步是有点代码量的，如果完全不懂 C#编程的，只会 LabVIEW 的编程的同学您还是
绕道走吧，找一个会 C#编程的，让其封装一下供你调用。不过这个类库的编写非常的简
单，只是简单的将接口再包装一下，有点像将酒厂的原浆倒进自己的瓶子里，就可以号称
这个酒是您自己的酿造的（自己不说，旁人还真以为你有酿酒的本事似的）。 
这一层的 SDK 封装，我们新建一个VMOperator 类，如下所示： 
C# 
C# 
using System; 
using System.Collections.Generic; using System.Linq; 
using System.Text; 
using System.Threading.Tasks; using VM.Core; 
using  VM.PlatformSDKCS; using GlobalVariableModuleCs;  
namespace HIKVMOperator 
{ 



<!-- page 518 -->
HIKROBOT 
 
509 
 
 
 
public class VMOperator 
 
{ 
 
} 
} 
接着就是对这个类添加一些和VM 相关的方法来丰富它。所有的方法，我们遵循一个共同
的模板，如下，伪代码可以表示为： 
int foobar(param1,param2,…) 
{ 
 
try 
 
{ 
 
 
int ret = vm_sdk_api(param1,pram2,…); return 0; 
 
} 
 
catch(VmException ex) 
 
{ 
 
 
return ex.ErrorCode; 
 
} 
} 
之所以这样写，是为了让调用者在调用的时候知道错误发生的原因，有助于排查问题。按
照这种模板，我们将 VM 的常用操作封装如下： 
加载方案方法 
public static int LoadSolution(string solPath,string password) 
{ 
 
try 
 
{ 
 
 
VmSolution.Load(solPath, password); return 0; 
 
} 
 
catch(VmException ex) 
 
{ 
 
 
return ex.errorCode; 
 
} 
} 
运行流程方法 
public static int RunProcedure(string procedureName) 
{ 
 
try 
 
{ 



<!-- page 519 -->
HIKROBOT 
 
510 
 
 
 
 
VmProcedure vmProcedure = VmSolution.Instance[procedureName] as 
VmProcedure; 
 
 
vmProcedure.Run();  
 
 
return 0; 
 
} 
 
catch (VmException ex) 
 
{ 
 
 
return ex.errorCode; 
 
} 
} 
获取流程配置的输出值 
public static int GetProcedureResult(string procedureName,string resultName,ref int resultCo
unt,ref object[] resultVal) 
{ 
 
try 
 
{ 
 
 
VmProcedure vmProcedure = VmSolution.Instance[procedureName] as 
VmProcedure; 
 
 
if (resultVal.Length > 0) 
 
 
{ 
 
 
 
if(resultVal[0].GetType()==typeof(float)) 
 
 
 
{ 
 
 
 
 
FloatDataArray floatDataArray = vmProcedure.Mod
uResult.GetOutputFloat(resultName);  
 
 
 
 
resultCount = floatDataArray.nValueNum; 
 
 
 
 
for(int i=0;i< resultCount; i++) 
 
 
 
 
{ 
 
 
 
 
 
resultVal[i] = floatDataArray.pFloatVal[i]; 
 
 
 
 
} 
 
 
 
} 
 
 
 
if (resultVal[0].GetType() == typeof(int)) 
 
 
 
{ 
 
 
 
 
IntDataArray intDataArray = vmProcedure.ModuRes
ult.GetOutputInt(resultName); resultCount = intDataArray.nValueNum; 
 
 
 
 
for (int i = 0; i < resultCount; i++) 
 
 
 
 
{ 
 
 
 
 
 
resultVal[i] = intDataArray.pIntVal[i]; 
 
 
 
 
} 
 
 
 
} 
 
 
 
if (resultVal[0].GetType() == typeof(string)) 
 
 
 
{ 



<!-- page 520 -->
HIKROBOT 
 
511 
 
 
 
 
 
 
StringDataArray strDataArray = vmProcedure.Modu
Result.GetOutputString(resultName); resultCount = strDataArray.nValueNum; 
 
 
 
 
for (int i = 0; i < resultCount; i++) 
 
 
 
 
{ 
 
 
 
 
 
resultVal[i] = strDataArray.astStringVal[i]; 
 
 
 
 
} 
 
 
 
} 
 
 
} 
 
 
else 
 
 
{ 
 
 
 
return int.MinValue; 
 
 
} 
 
 
return 0; 
 
} 
 
catch (VmException ex) 
 
{ 
 
return ex.errorCode; 
 
} 
} 
VMOperator 的资源释放方法 
public static int DestroyInstance() 
{ 
 
try 
 
{ 
 
 
VmSolution.Instance.Dispose();  
 
 
return 0; 
 
} 
 
catch (VmException ex) 
 
{ 
 
return ex.errorCode; 
 
} 
} 
这里就不贴出全部的封装的接口代码了，总体上还是非常的简单搬运，并不存在复杂的编
程逻辑。封装好 VmOperator 类库后，我们就可以使用.NET 容器调用 VmOperator 来
实现对VM SDK 的调用了。 
第 4 步：在 LabVIEW 中调用封装好的VMOperator 类库 
在 LabVIEW 的后置面板中，右键菜单选择“.NET 和 ActiveX”，接着选择“.NET”，拖



<!-- page 521 -->
HIKROBOT 
 
512 
 
 
出一个构造器节点，如下图所示： 
 
选择我们刚才封装好的 VMOperator 类库。 
接着再添加一个调用节点，选择方法，在方法列表中选择想要调用的方法，例如调用加载
方案接口，如下图所示： 
 
5 举个例子 
经过上面铺垫，对 LabVIEW 调用 VM SDK 遇到的阻碍我们就已经完全攻破了，接着我
们举一个实际的例子来演示如何 LabVIEW 中调用 VM SDK，也使这份文档能真正帮助
到 LabVIEW 开发者，而不是夸夸其谈，言之无物。 



<!-- page 522 -->
HIKROBOT 
 
513 
 
 
我们要实现一个这样的简单需求 
（1）在 LabVIEW 前面板放置一个路径选择按钮，选择方案路径，放置一个方案加载按
钮，放置一个方案运行一次按钮，放置一个停止按钮，放置一个 VM MainView 控件，
放置一个VM RenderControl 控件 
（2）按下路径选择按钮传入路径，按下加载按钮加载选择的方案文件，按下运行按钮运
行方案中的流程 1 一次。 
（3）方案中的流程 1 运行一次，VM Render 控件渲染流程 1 的运行结果。 
（4）VM MainView 控件用来调试流程 
根据以上需求，我们在 LabVIEW 的前面板放置几个按钮和相关VM 控件，如下图所
示： 
 
在 LabVIEW 的后置面板，也就是程序编辑区，编写程序框图，我们用顺序结构，顺序结
构包含两帧，前一帧在 While 循环中运行程序主干，结束帧用来释放 VmOperator 资



<!-- page 523 -->
HIKROBOT 
 
514 
 
 
源（敲重点：这个非常非常重要！！！，不然你的 LabVIEW 程序分分钟死给你看）。 
所以程序框图如下： 
加载方案按钮和运行一次按钮用了事件结构，下图是加载方案按钮按下事件响应： 
 
运行一次按钮的事件响应如下如所示： 



<!-- page 524 -->
HIKROBOT 
 
515 
 
 
 
再次强调： 程序的结束帧一定要释放 VMOperator, 也就是调用 VMOperator 的Disto
ryInstance 方法，如果不释放 VMOperator, LabVIEW 程序会崩溃，同时也会在LabVI
EW 程序目录下生成 VM 的 dump 文件。 
程序的运行效果，如下图所示： 



<!-- page 525 -->
HIKROBOT 
 
516 
 
 
 
6 更进一步 
既然通过调用封装后的 VMOperator 类库结合 VM 的界面控件就可以在 LabVIEW 中
畅行无阻，为什么我们不将 VMOperator 和VM 的界面控件整合在一起作为一个用户控
件放在 LabVIEW 中呢？为什么不呢？实在是没有理由让两者分开了，VMOperator 和 
VM 界面控件本该就是一个整体， 而不是按照这种割裂开来的方式用， 所以我们将VM
Operator 和 VM 界面控件封装成一个用户控件。 
操作步骤： 
第 1 步：创建窗体控件库工程 
新建一个 C#的窗体控件工程，如下图所示： 



<!-- page 526 -->
HIKROBOT 
 
517 
 
 
 
第 2 步：设计界面 
我们在控件界面上放置一个 VM RenderControl 和几个按钮控件，分别用来加载方案， 
运行方案，流程调试按钮（通过按下此按钮进入  VM MainView  界面），模块调试按钮 
（通过按下此按钮进入 VM ParamConfigWithRender  界面），然后放置一个流程列表
和模块列表，用来显示所有流程和所有模块，加一个流程结果输出显示 List，会枚举出所
有配置过的流程输出结果项。基本上这一个控件就包含了百分之 90 以上的 VM 调试场
景，足以应付常规应用了。如下图所示： 
 



<!-- page 527 -->
HIKROBOT 
 
518 
 
 
 
第 3 步：代码编写 
这部分就是 VMOperator 类库的各种方法的调用，以及界面控件的使用，代码逻辑极其
简单，这一步对于熟悉 C#编程和 VM 二次开发的视觉开发者来说，应该说半天时间足以
编写完成。这里我就不把全部的代码在这里展示了。 
第 4 步：编译生成用户控件 DLL 
这一步没啥好说的，编写好代码，按下 CTRL+SHIFT+B 组合键即可，会在工程目录下生
成 UserControl1.dll (当然UserControl1 这个名称你可以在工程代码中重构) 
第 5 步：在 LabVIEW 中调用 
在 LabVIEW 中调用我们使用.NET 容器的方式调用，LabVIEW 的调用代码如下： 



<!-- page 528 -->
HIKROBOT 
 
519 
 
 
 
看看，这个程序如此的简洁，这才是正确的使用姿势。好，我们来看看它的运行效果 
 
再看看程序调试界面 



<!-- page 529 -->
HIKROBOT 
 
520 
 
 
 
7 总结 
通过上面的每一步的解释说明，可以归纳总结以下几个结论 
（1）在 LabVIEW 中调用 VM4.x 版本的 SDK 是完全可以做得到的，在 LabVIEW 中
使用面向对象的编程方式开发VM 应用是很方便的。 
（2）直接使用 VM SDK 提供的 DLL 和控件 DLL，LabVIEW 加载程序集会出错，是因
为GAC 并没有把 LabVIEW 需要的基础程序集也加进去，我们可以通过对 VM SDK 做
一层简单的浅层封装，用自定义控件和用户自定义库的方式让 LabVIEW 加载可以避免这
个问题。 
（3）LabVIEW 中调用 VM SDK 时，程序结束时一定要记得释放 VmSoluition 这个全
局对象，否则会是使 VM 崩溃从而导致 LabVIEW 这个宿主也跟着崩溃。 
（4）在 VS 中将所有VM 控件和 VM 操作 API 封装成一个整体的库，然后在 LabVIE



<!-- page 530 -->
HIKROBOT 
 
521 
 
 
W 中调用，会显著降低 LabVIEW 使用VM SDK 的难度。 
（5）图形化编程是 LabVIEW 的突出特点，也是 VM 的突出优点，也是有别于其他机器
视觉算法平台之处，LabVIEW 和 VM 混合编程是很好的一种视觉应用开发模式。 
问题根因 
不熟悉基于Labview 二次开发环境配置 
 
 
 



<!-- page 531 -->
HIKROBOT 
 
522 
 
 
2.2 模块操作类 
2.2.1 流程操作：通过流程或Group 设置
输入输出图像的方法 
描述 
环境：VM4.2 + VS2013 及以上 
现象：如何在二次开发中设置流程输入输出图像 
解答 
 
打开流程的配置窗口，获取流程1 的输出图像，将其设置为流程2 的输入图像，虽然在V
M 中可以通过连线的方式实现，但也可以通过代码的方式实现，C#代码如下 。另外，通
过Group 设置输入输出图像也是调用同样的接口函数SetInputImage_V2()和GetOutpu



<!-- page 532 -->
HIKROBOT 
 
523 
 
 
tImageV2()，其中要注意的是，当用代码给流程输入图像时，流程中的其它模块的图像输
入源需要订阅流程的图像参数。注意:Mat 和Bitmap 彩色图转流程输入时，Mat 和Bit
map 是BGR，流程输入图像是RGB，通道需要交换  
 
C#  
VmProcedure process = (VmProcedure)VmSolution.Instance["流程1"]; 
InputImageData vmImageData = new InputImageData(); 
//获取流程1 输出图像 
ImageBaseData_V2 image =process.ModuResult.GetOutputImageV2("o
ut2"); 
//设置流程2 输入图像 
VmProcedure vmProcedure = VmSolution.Instance["流程2"] asVmProc
edure; 
vmProcedure.ModuParams.SetInputImage_V2("ImageData", image); 
 
问题根因 
不熟悉二次开发设置流程输入图像的方法。  
 
 



<!-- page 533 -->
HIKROBOT 
 
524 
 
 
2.2.2 模块操作：设置输入图像、参数和R
OI  
描述  
环境：VM4.2+ VS2013 及以上  
现象：在VM SDK 二次开发中，如何设置指定模块的输入图像、模块参数及ROI 区域？  
解答  
首先，我们需要知道，一个VM 模块的输入包含几个部分：基本参数（图像输入、ROI 区
域）、运行参数，以圆查找为例，如下图所示：  
 
通过VM SDK 二次开发，我们可以通过代码去修改指定模块的输入参数。注意：设置输
入参数（基本参数），参数配置窗口界面不会显示所设置的参数，此时模块运行，参数永



<!-- page 534 -->
HIKROBOT 
 
525 
 
 
久有效，流程运行，参数一次有效；设置运行参数，参数配置窗口界面会显示所设置的参
数，此时模块和流程运行，参数都永久有效  
1、设置模块输入图像，以“圆查找模块”为例，首先，添加相应的命名空间IMVSCircleF
indModuCs，实现代码如下：  
 
C#  
Mat mat = Cv2.ImRead(path, ImreadModes.Grayscale); //调用OpenCv
方法读取图像数据，这里的path 为图片路径 
InputImageData inputImageData = new InputImageData();//实例化一
个输入图像对象 
inputImageData.Names.DataName = "InImage";//只能使用默认名称InI
mage 
inputImageData.Names.HeightName = "InImageHeight";//默认InImag
eHeight 
inputImageData.Names.WidthName = "InImageWidth";//默认InImage
Width 
inputImageData.Names.PixelFormatName = "InImagePixelFormat";//默
认InImagePixelFormat 
inputImageData.Data = mat.Data; 
inputImageData.DataLen = (uint)(mat.Width * mat.Height); 



<!-- page 535 -->
HIKROBOT 
 
526 
 
 
inputImageData.Height = mat.Height; 
inputImageData.Width = mat.Width; 
inputImageData.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMA
T 
_MONO8; 
 
IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["
流程1.圆查找1"] as IMVSCircleFindModuTool;//实例化指定的模块工具 
circleFindModuTool.ModuParams.SetInputImage(inputImageData);//设
置输入图像 
2、设置指定模块运行参数，以“圆查找模块”为例，设置对象中ModuParams 的属性，
代码如下：  
 
C#  
IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["
流程1.圆查找1"] as IMVSCircleFindModuTool;//实例化指定的模块工具 
circleFindModuTool.ModuParams.EdgeThresh = 30;//设置边缘阈值为30 
3、设置指定模块的ROI 区域，代码如下。  
 



<!-- page 536 -->
HIKROBOT 
 
527 
 
 
C#  
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolutio
n.Instance["流程1.圆查找1"]; 
RectBox rectBox = new RectBox(new VM.PlatformSDKCS.PointF(1000, 
1000), 500, 500, 0); 
tool.ModuParams.ModuRoiManager.RoiRectangle = rectBox;//代码设置
ROI 
问题根因  
不了解VM SDK 二次开发中模块结构，以及如何对其参数进行相应的修改。  
 
 



<!-- page 537 -->
HIKROBOT 
 
528 
 
 
2.2.3 N 点标定：清空标定点、生成标定文
件  
描述  
环境：VM4.2 + VS2013 及以上 
现象：VM 二次开发如何设置对应的N 点标定模块的清空标定点与生成标定文件的功能  
解答  
 
C# 
//获取对应的模块实例 
IMVSNPointCalibModuTool tool=(IMVSNPointCalibModuTool)VmSoluti
on.Instance["流程1.N 点标定1"]; 
tool.ModuParams.DoClearPoint();//清空标定点 
tool.ModuParams.DoSaveFile(path);//根据路径保存标定文件 
int i = tool.ModuResult.ModuStatus;//获取标定状态，1 为成功，0 为失败 
问题根因  
不熟悉模块的函数  



<!-- page 538 -->
HIKROBOT 
 
529 
 
 
2.2.4 分支字符：控制调试模式开关的方法
  
描述  
环境：VM4.2 + VS2013 及以上  
现象：VM 二次开发如何设置分支字符模块的调试模式  
解答  
 
C# 
C# 
//获取对应的模块实例 
BranchStringCpmLTool tool = (BranchStringCpmLTool)VmSolution.Inst
ance["流程1.分支字符1"]; 
List<BranchStringItemParam> itemList = tool.ModuParams.GetBranch
StrItemParamList();//获取所有分支 
foreach( var item in itemList) 
{ 
    item.IsDebugMode = false; //可根据需求将某一个分支关闭调试模式 
} 



<!-- page 539 -->
HIKROBOT 
 
530 
 
 
问题根因  
不熟悉分支字符工具及其接口。  
 
 



<!-- page 540 -->
HIKROBOT 
 
531 
 
 
2.2.5 条件检测：条件检测模块设置范围的
方法  
描述  
环境：VM4.2 + VS2013 及以上 
现象：VM 二次开发如何设置条件检测模块的范围值  
解答  
修改前：  
 
执行代码：  
 
//C# 



<!-- page 541 -->
HIKROBOT 
 
532 
 
 
//获取对应的模块实例 
IfModuleTool tool = (IfModuleTool)VmSolution.Instance["流程1.条件检
测1"]; 
//获取对应的检测项名称 
IfItemParam item1 = tool.ModuParams.GetIfItemParam("int0"); 
IfItemParam item2 = tool.ModuParams.GetIfItemParam("float0"); 
//对检测范围进行修改 
item1.MinValue = 0; 
item1.MaxValue = 888; 
item2.MinValue = 0; 
item2.MaxValue = 999; 
修改后：  
 
问题根因  



<!-- page 542 -->
HIKROBOT 
 
533 
 
 
不熟悉条件检测工具及其接口。  
 
 



<!-- page 543 -->
HIKROBOT 
 
534 
 
 
2.2.6 图像源：图像源模块输入图像的方法
  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何通过代码给图像源模块输入图像？  
解答  
图像源模块输入图像，除了在界面上操作来添加图像或图像文件夹，还可以通过代码的方
式使得图像源模块可以通过本地输入图像，也可以通过SDK 输入图像。  
 
C# 
ImageSourceModuleTool imageSourcTool = (ImageSourceModuleToo
l)VmSolution.Instance["流程1.图像源1"]; 
//通过本地输入图像，图像源类型为本地 
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.
ImageSourceTypeEnum.LocalImage; 
imageSourcTool.AddInputImageByPath("D:\\3.ProjectCode\\VM4.2\\VM
TestB\\1.bmp");//添加图片 



<!-- page 544 -->
HIKROBOT 
 
535 
 
 
imageSourcTool.DeleteInputImageByPath("D:\\1.bmp");//删除图片 
imageSourcTool.ClearAllInputImage();//清空图片 
//通过SDK 输入图像，图像源类型为SDK,通过SetImagePath 接口或者SetI
mageData 接口 
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.
ImageSourceTypeEnum.SDK; 
imageSourcTool.SetImagePath("D:\\3.ProjectCode\\VM4.2\\VMTestB3-2
\\1.bmp"); 
imageSourcTool.SetImageData(imageBaseData);//参数类型为ImageBase
Data 
问题根因  
不熟悉图像源模块输入图像  
 
 



<!-- page 545 -->
HIKROBOT 
 
536 
 
 
2.2.7 所有流程：获取所有流程对象的方法
  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何获取一个方案中的所有流程对象，进而可以直接运行所获取的流程，或者获取
流程名、流程ID 等等。  
解答  
在VM4.0 通过VmSolution.Instance.GetAllProcedureList()仅仅能或流程列表，下面是
获取流程对象的接口：  
 
c# 
List<VmProcedure> procedures = new List<VmProcedure>(); 
VmSolution.Instance.GetAllProcedureObjects(ref procedures); 
string name = procedures[0].FullName; 
string id = procedures[0].ID; 
procedures[0].Run(); 
 



<!-- page 546 -->
HIKROBOT 
 
537 
 
 
问题根因  
不熟悉如何获取流程对象  
 
 



<!-- page 547 -->
HIKROBOT 
 
538 
 
 
2.2.8 几何创建：绘制形状的方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：在几何创建模块中，VM 二次开发如何通过代码绘制形状？  
解答  
VM4.2 中几何创建通过代码的方式可以输入图像、点、直线、圆、矩形，注意仅当次执行
有效。下面示例代码绘制直线。  
 
C# 
GeometryCreateCs.GeometryCreateTool geoTool = (GeometryCreateC
s.GeometryCreateTool)VmSolution.Instance["流程1.几何创建1"]; 
Line line1 = new Line(new VM.PlatformSDKCS.PointF(500, 500), new 
VM.PlatformSDKCS.PointF(3000, 3000), 0); 
List<Line> line = new List<Line>(); 
line.Add(line1); 
geoTool.ModuParams.InputLine = line; 
问题根因  



<!-- page 548 -->
HIKROBOT 
 
539 
 
 
不熟悉几何创建模块的接口。  
 
 



<!-- page 549 -->
HIKROBOT 
 
540 
 
 
2.2.9 模板匹配：模板匹配模块导入算子模
型文件的方法  
描述  
环境：VM4.2.0 + VS2013 及以上  
现象：VM 二次开发，高精度模板匹配模块如何导入算子导出的模型？  
解答  
安装20220902 及后续补丁包，注册GAC 后，在二次开发软件中可调用模板匹配模块的I
mportSDKModelData(string[] strPaths)接口导入模型文件。示例代码如下：  
 
C# 
using IMVSHPFeatureMatchModuCs; 
using VisionDesigner; 
using VisionDesigner.HPFeaturePatMatch; 
 
private string modelExportPathDefault = "HPPattern.hpmxml"; // 模型
导出默认路径 



<!-- page 550 -->
HIKROBOT 
 
541 
 
 
private string[] modelExportPathList = new string[1]; // 本示例只有一
个模型文件，所以数组长度设为1 
 
// 高精度匹配算子建模，导出模型 
CHPFeaturePattern cHPFeaturePatternObj = new CHPFeaturePattern(); 
cHPFeaturePatternObj.InputImage = cInputImg; 
CMvdRectangleF cMvdRectangleF = new CMvdRectangleF((float)rect.
CenterPoint.X, (float)rect.CenterPoint.Y, (float)rect.Width, (float)rect.Hei
ght); 
var region = new CPatMatchRegion(cMvdRectangleF, true);   //true
表示为ROI，false 表示屏蔽区  region.Shape = cShapeObj as CMvdRect
angleF; 
cHPFeaturePatternObj.RegionList.Add(region); 
cHPFeaturePatternObj.Train(); 
cHPFeaturePatternObj.ExportPattern(modelExportPathDefault); 
modelExportPathList[0] = modelExportPathDefault; 
 
// 模板匹配导入算子导出的模型 
IMVSHPFeatureMatchModuTool iMVSHPFeatureMatchModuTool = (I
MVSHPFeatureMatchModuTool)VmSolution.Instance[FeatureModuleNa
me]; 



<!-- page 551 -->
HIKROBOT 
 
542 
 
 
iMVSHPFeatureMatchModuTool.ClearModelData();  // 导入模型前，清
空已有模型 
iMVSHPFeatureMatchModuTool.ImportSDKModelData(modelExportPat
hList);  // 模板匹配模块导入算子导出的模型(定制接口，0902 加入基线) 
目前只有高精度模板匹配支持导入算子导出的模型，快速模板匹配、灰度模板匹配等模块
暂不支持导入算子导出的模型文件。  
问题根因  
不熟悉模板匹配的相关接口。  
 
 



<!-- page 552 -->
HIKROBOT 
 
543 
 
 
2.2.10 图像源：通过SDK 传入图像数据的
方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：当图像源类型为SDK 时， 可以使用SetImagePath 接口或者SetImageData 接口
给图像源模块输入图像，那么如何使用SetImageData 传入相机图像呢？  
解答  
1.确保图像源类型为SDK 
2.使用SetImageData 的参数类型可以为ImageBaseData，其中图像格式使用VMPixel
Format 或ImvsSdkDefine 的枚举（灰度图是17301505，彩色图是35127316），在
VM4.0 中使用的是ImagePixelFormat 类型的枚举（灰度图是1，彩色图是2）。  
 
C# 
ImageBaseData imageBaseData = new ImageBaseData(imagedata, StI
mg.DataLen, StImg.Width, StImg.Height, VMPixelFormat.VM_PIXEL_M
ONO_08) 



<!-- page 553 -->
HIKROBOT 
 
544 
 
 
ImageSourceModuleTool imageSourcTool = (ImageSourceModuleToo
l)VmSolution.Instance["流程1.图像源1"]; 
imageSourcTool.SetImageData(imageBaseData); 
3.当图像数据为彩色图像时，开启图像源模的输出MONO8 使能，其他模块的图像输入则
是图像源.灰度数据。  
 
问题根因  
不熟悉图像源通过SDK 传图  
 
 



<!-- page 554 -->
HIKROBOT 
 
545 
 
 
2.2.11 流程触发：在相机回调函数里短时
间多次触发同一流程报错的解决方法  
描述  
环境：VM4.0 及以上+ VS2013 及以上  
现象：在二次开发中，如果在流程未执行完之前再次触发该流程会导致程序报错，该如何
解决这一问题？  
解答  
由于在VM 中同一流程的运行是同步的，因此当某一流程未执行完毕时再次执行该流程会
出现报错现象，可以使用标志位在流程运行完成之后，再去调用下一次流程的运行。  
如在相机回调函数中调用流程的Run 接口，如果相机每两次回调间隔过短就会导致调用R
un 接口报错。回调中在调用流程执行接口之前使用标志位，使单个流程执行完之后，才触
发流程的下一次执行。  
 
 
C#  
bool flag=true; 
 



<!-- page 555 -->
HIKROBOT 
 
546 
 
 
//回调或者其他会导致流程未执行再次触发的函数 
{ 
    if (flag) 
 
{ 
 
 
flag = false; 
 
 
VmProcess1.Run(); 
 
 
flag = true; 
 
} 
} 
问题根因  
不熟悉流程自身同步运行的机制。  
 
 



<!-- page 556 -->
HIKROBOT 
 
547 
 
 
2.2.12 检测加密狗：检测加密狗有无的方
法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何在VM 二次开发程序启动时，检测加密狗的有无？  
解答  
程序启动时，在Program.cs 的Main()函数中通过捕获异常码来检测加密狗的有无。  
C# 
try 
{ 
    Application.EnableVisualStyles(); 
    Application.SetCompatibleTextRenderingDefault(false); 
    Application.Run(new Form1()); 
} 
catch (Exception ex) 
{ 



<!-- page 557 -->
HIKROBOT 
 
548 
 
 
    VM.PlatformSDKCS.VmException vmEx = VM.Core.VmSolution.Get
VmException(ex); 
    if (null != vmEx) 
    { 
        string strMsg = "InitControl failed. Error Code: " + Convert.T
oString(vmEx.errorCode, 16); 
        MessageBox.Show(strMsg); 
    } 
    else 
    { 
        return; 
  
  } 
}   
问题根因  
不熟悉如何检测加密狗的有无  
 
 



<!-- page 558 -->
HIKROBOT 
 
549 
 
 
2.3 控件嵌入类 
2.3.1 渲染控件：渲染控件上自定义图形的
方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：VM4.2 如何在渲染控件上自定义图形？  
解答  
VM4.2 二次开发相比较VM4.0 二次开发，渲染控件上自定义图形有一些更新，除了接口
vmRenderControl.DrawShape()，新增加一个接口vmRenderControl.AddShape(),前
者是立刻绘制，后者是在下次刷新渲染时自动绘制。所以在VM4.0 二次开发回调函数中
图像渲染并添加自定义图形时， DrawShape 接口函数前需要添加延时，不然回调中的图
像渲染还没更新，自定义的图形已经调用DrawShape 函数，从而导致自定义图形不能很
好的渲染在图像上。在VM4.2 二次开发中使用AddShape 接口就不要加延时，它会在图
像渲染结束后再绘制自定义图形。  
手动添加引用VMControls.WPF.dll、WindowsBase.dll（路径：\VisionMaster4.2.0\De
velopment\V4.x\ComControls\Assembly），添加后，引用属性【复制本地】改为fals
e；渲染控件需要先绑定图像，再调用渲染控件的AddShape 绘图接口；支持直线、圆



<!-- page 559 -->
HIKROBOT 
 
550 
 
 
形、矩形、文本等图形元素绘制；绘制时机：流程运行结束，在流程结果回调函数中绘
制。下面绘制了直线和文本，其它图形依次类推。  
 
C# 
//绘制直线 
VMControls.WPF.LineEx line = new VMControls.WPF.LineEx(new Syste
m.Windows.Point(100, 100), new System.Windows.Point(600, 600), str
oke: "#FF0000", strokeThickness: 10); 
vmRenderControl1.AddShape(line); 
//绘制文本 
VMControls.WPF.TextEx text = new VMControls.WPF.TextEx("欢迎使用
VM4.2 二次开发！", new System.Windows.Point(1000, 1000), fontSize: 
20, stroke: "#FF0000"); 
vmRenderControl1.AddShape(text); 
问题根因  
不熟悉如何绘制自定义图形。  
 
 



<!-- page 560 -->
HIKROBOT 
 
551 
 
 
2.3.2 参数控件：参数配置控件绑定模块的
方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何给参数配置控件绑定指定模块？  
解答  
1. 参数配置控件绑定模块方法（C#），示例代码如下。  
 
C# 
 
// 参数配置控件模块绑定 
private void button3_Click(object sender, EventArgs e) 
{ 
    try 
    { 
        //参数配置 



<!-- page 561 -->
HIKROBOT 
 
552 
 
 
        var blobTool = (VMControls.Interface.IVmModule)VmSolution.
Instance["流程1.BLOB 分析1"]; 
        //参数配置控件 
        vmParamsConfigControl1.ModuleSource=blobTool; 
        //参数配置控件带渲染 
        vmParamsConfigWithRenderControl1.ModuleSource = blobTo
ol; 
    } 
    catch (VmException ex) 
    { 
        MessageBox.Show(Convert.ToString(ex.errorCode, 16)); 
    } 
} 
2.参数配置控件绑定模块方法（C++），代码如下。  
 
C++ 
//参数设置 
void CMFCApplication5Dlg::OnBnClickedButton4() 
{ 
 
// TODO: 在此添加控件通知处理程序代码 



<!-- page 562 -->
HIKROBOT 
 
553 
 
 
 
try 
 
{ 
 
 
auto pObject = (CModuParamsBase*)(*m_pVmSol)
[“流程1.圆查找1”]; 
 
 
m_ParamsRender.SetParamsInfo(pObject, ""); 
 
} 
 
catch (CVmException ex) 
 
{ 
 
 
CString strTemp; 
 
 
strTemp.Format(_T("%d"), ex.GetErrorCode()); 
 
} 
} 
3.绑定效果  



<!-- page 563 -->
HIKROBOT 
 
554 
 
 
 
问题根因  
不熟悉控件的资源绑定方法。  
 
 



<!-- page 564 -->
HIKROBOT 
 
555 
 
 
2.3.3 控件颜色：控件颜色修改方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何修改控件颜色？  
解答  
1. 修改控件背景色，示例代码（C#）如下。注意：渲染控件颜色修改的前提是渲染控件
已经绘制到窗口中。  
当通过拖拉渲染控件到窗口中时，控件颜色修改只能写在窗口初始化之后，如Load 事件
中或按钮事件中； 
当通过动态定义渲染控件到窗口中时，控件颜色修改只能写在窗口Add 渲染控件之后，如
this.Controls.Add(vmRenderControl1)之后。 
 
C# 
private void button16_Click(object sender, EventArgs e) 
{ 
    string str = "#DD22AA";//十六进制颜色码 
    vmRenderControl1.SetBackground(str); 



<!-- page 565 -->
HIKROBOT 
 
556 
 
 
} 
2.修改控件背景色，示例代码（C++）如下。  
 
C++ 
//修改控件背景色 
int CMFCApplication5Dlg::SetBackGroundColor() 
{ 
 
// TODO: 在此处添加实现代码. 
 
CString str("#DD22AA");//十六进制颜色码 
 
m_RenderCtr.SetBackground(str.GetBuffer()); 
 
return 0; 
} 
3.修改效果  



<!-- page 566 -->
HIKROBOT 
 
557 
 
 
 
问题根因  
不熟悉控件接口。  
 
 



<!-- page 567 -->
HIKROBOT 
 
558 
 
 
2.3.4 独立控件：二次开发单独显示Group 的方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：如何单独显示Group（.gro 后缀）文件？  
解答  
1. 首先需要在界面上拖拽SingleModuleSetConfigControl 控件，该控件专门用于显示
Group。  
2.加载Group 文件并绑定到该控件的ModuleSource 属性，代码如下。  
 
C# 
private void button16_Click(object sender, EventArgs e) 
{ 
    vmSingleModuleSetConfigControl1.ModuleSource = VmSolution.L
oadIndependentGroup("D://Files//test.gro"); 
} 
3.显示效果  



<!-- page 568 -->
HIKROBOT 
 
559 
 
 
 
问题根因  
不熟悉控件的资源绑定方法。  
 
 



<!-- page 569 -->
HIKROBOT 
 
560 
 
 
2.3.5 取流控件：实时取流控件的使用方法
  
描述  
环境：VM4.2 + VS2013 及以上 
现象：VM4.2 新增了一个控件，实时取流控件。  
解答  
1.在工具箱添加控件后，就可以拖拽实时取流控件VmRealTimeAcqControl 到窗体中进
行使用。  
2.拖拉控件后，还需要将全局相机与控件进行绑定，代码如下所示：  
 
C# 
GlobalCameraModuleCs.GlobalCameraModuleTool cameraModu=(Glo
balCameraModuleCs.GlobalCameraModuleTool)VmSolution.Instance["
全局相机1"]; 
vmRealTimeAcqControl1.ModuleSource = cameraModu; 
vmRealTimeAcqControl1.StartGrabbing();//开始采集 
vmRealTimeAcqControl1.Stop Grabbing();//停止采集 



<!-- page 570 -->
HIKROBOT 
 
561 
 
 
问题根因  
不熟悉实时取流控件的使用。  
 
 



<!-- page 571 -->
HIKROBOT 
 
562 
 
 
2.3.6 渲染控件：渲染控件绘制ROI 的方法
  
描述  
环境：VM4.2.0 + VS2013 及以上  
现象：VM 二次开发，如何在渲染控件上绘制ROI，以实现界面快速建模、调整模块RO
I？  
解答  
安装20220914 及后续补丁包，注册GAC 后，在二次开发软件中注册ROI 绘制事件。示
例代码如下：  
 
C# 
using VMControls.RenderInterface; 
using VMControls.Interface; 
using VMControls.Winform.Release; 
 
// 注册ROI 绘制事件 
vmRenderControl1.IsShowCustomROIMenu = true; 



<!-- page 572 -->
HIKROBOT 
 
563 
 
 
vmRenderControl1.OnCustomRoiAddEvent -= VmRenderControl1_OnC
ustomRoiAddEvent; 
vmRenderControl1.OnCustomRoiAddEvent += VmRenderControl1_On
CustomRoiAddEvent; 
 
// ROI 绘制事件 
private void VmRenderControl1_OnCustomRoiAddEvent(object sender,
 VMControls.RenderInterface.RoiEventArgs e) 
{ 
 
roi = e.Roi; 
 
roi.DataChangedCommand = new DelegateCommand<IROI>
(OnDataChangedCommandExcute); 
    if (roi is IRectROI rect)  // 绘制的ROI 为矩形 
 
{ 
 
// Avoid 表示ROI 类型为屏蔽区 
 
if (!(rect.UseType == ROIUseType.Avoid)) { // To Do Code } 
 
// To Do Code 例如设置模块ROI、例如模板匹配建模等 
 
} 
} 
 
// ROI 修改事件 



<!-- page 573 -->
HIKROBOT 
 
564 
 
 
private void OnDataChangedCommandExcute(IROI obj) 
{ 
 
if (roi is IRectROI rect)  // 绘制的ROI 为矩形 
 
{  
 
if (!(rect.UseType == ROIUseType.Avoid)) //屏蔽区 
 
{ // To Do Code } 
 
// To Do Code 例如设置模块ROI、例如模板匹配建模等 
 
} 
} 
问题根因  
不熟悉渲染控件的相关事件。  
 
 



<!-- page 574 -->
HIKROBOT 
 
565 
 
 
2.3.7 控件语言：控件设置为英文的方法  
描述  
环境：VM4.2+VS2013 及以上  
现象：如何设置控件为英文？  
解答  
在VM4.0 的二次开发中，控件设置为英文的相关配置文件在debug 路径中LangCFG 文
件中，修改配置文件LanguageSet.cfg。在VM4.2 的二次开发中，因为debug 中没有进
行拷贝操作，所以修改配置文件路径如下图所示，zh-cn 表示中文，英文则用en-us。  
 
上图中是手动打开配置文件直接进行修改，也可以通过代码来修改配置文件： 
C# 
///修改对应cfg 文件内容，切换中文 



<!-- page 575 -->
HIKROBOT 
 
566 
 
 
string path2 =Path+ "Development\\V4.x\\ComControls\\Assembly\\L
angCFG\\LanguageSet.cfg"; 
string[] filelines = File.ReadAllLines(path2); 
filelines[2] = "  <LangSet>zh-cn</LangSet>"; 
File.WriteAllLines(path2, filelines); 
 
///修改对应文件内容，切换英文 
string path2 =Path+ "Development\\V4.x\\ComControls\\Assembly\\L
angCFG\\LanguageSet.cfg"; 
string[] filelines = File.ReadAllLines(path2); 
filelines[2] = "  <LangSet>en-us</LangSet>"; 
File.WriteAllLines(path2, filelines); 
注意：切换后VM 二次开发需要重新启动才会生效  
问题根因  
不熟悉如何修改VM4.2 二次开发控件的语言  
2.3.8 控件报错：子窗口包含主界面控件及
其它控件时报错的解决方法  
描述  



<!-- page 576 -->
HIKROBOT 
 
567 
 
 
环境：VM4.0 及以上 + VS2013 及以上  
现象：子窗口包含主界面控件（VmMainViewConfigControl）及其它控件时，打开子窗
口报错如下所示。  
 
解答  
将子窗口中的VM 控件的属性【TopStop】都改为false 即可。  



<!-- page 577 -->
HIKROBOT 
 
568 
 
 
 
问题根因  
主界面控件机制问题，VM4.3 将会改善。  
 
 



<!-- page 578 -->
HIKROBOT 
 
569 
 
 
2.3.9 图像传入：给渲染控件传入图像的方
法  
描述  
环境：VM4.0 及以上 + VS2013 及以上  
现象：VM 二次开发如何将在渲染控件上显示本地图像？  
解答  
1．可以通过模块的方式，再将渲染控件绑定模块或流程来显示本地图像，也可以通过Vm
RnderControl 控件的ImageSource 属性来设置图像。  
2.首先需要继承IImaageData 接口实现图像数据类。示例代码如下： 
C# 
public class ImageSource : VMControls.RenderInterface.IImageData 
{ 
    public ImageSource(int width, int height, byte[] buffer, VMPixelF
ormat pixelformat) 
    { 
        Width = width; 
        Height = height; 



<!-- page 579 -->
HIKROBOT 
 
570 
 
 
        PixelFormat = pixelformat == VMPixelFormat.VM_PIXEL_MO
NO_08 ? "Gray8" : "Rgb24"; 
        int channels = pixelformat == VMPixelFormat.VM_PIXEL_MO
NO_08 ? 1 : 3; 
        if (buffer.Length != width * height * channels) 
            throw new Exception("buffer is error"); 
        Buffer = new byte[buffer.Length]; 
        Array.Copy(buffer, Buffer, buffer.Length); 
    } 
 
    public int Width { get; set; } 
 
    public int Height { get; set; } 
 
    public byte[] Buffer { get; set; } 
 
    public string MemoryAddress 
    { 
        get 
        { 



<!-- page 580 -->
HIKROBOT 
 
571 
 
 
            GCHandle gCHandle = GCHandle.Alloc(Buffer, GCHandleT
ype.WeakTrackResurrection); 
            IntPtr bufferAddress = GCHandle.ToIntPtr(gCHandle); 
            return bufferAddress.ToString(); 
        } 
    } 
 
    public string PixelFormat { get; } 
} 
3.使用OpenCV 等接口获取本地图像数据流并转换成ImageSource 类型显示，示例代码
如下： 
C# 
private void button1_Click(object sender, EventArgs e) 
{ 
    OpenFileDialog openFile = new OpenFileDialog(); 
    if (openFile.ShowDialog() == DialogResult.OK) 
    { 
        pictureBox1.Image = Image.FromFile(openFile.FileName); 
        var mat = Cv2.ImRead(openFile.FileName); 



<!-- page 581 -->
HIKROBOT 
 
572 
 
 
        byte[] imageByte = new byte[mat.Width * mat.Height * mat.
Channels()]; 
        ImageSource imageSource = null; 
        if (mat.Channels() == 1) 
        { 
            imageSource = new ImageSource(mat.Width, mat.Height,
 imageByte, VMPixelFormat.VM_PIXEL_MONO_08); 
        } 
        else 
        { 
            //OpenCV 为BGR VM 为RGB 通道 
            Cv2.CvtColor(mat,mat,ColorConversionCodes.BGR2RGB); 
            Marshal.Copy(mat.Data, imageByte, 0, imageByte.Length); 
            imageSource = new ImageSource(mat.Width, mat.Height,
 imageByte, VMPixelFormat.VM_PIXEL_RGB24_C3); 
        } 
        if(imageSource!=null) 
        vmRenderControl1.ImageSource = imageSource; 
   } 
} 



<!-- page 582 -->
HIKROBOT 
 
573 
 
 
注意事项：灰度图读取到的如果是三通道需先转成单通道图像，彩色图需要交换下R 和G
通道，即用Cv2.CvtColor 转换一下。  
问题根因  
不熟ImageSource 属性及接口。  
 
 



<!-- page 583 -->
HIKROBOT 
 
574 
 
 
2.3.10 主界面控件：主界面控件添加参数
修改记录并将记录保存至本地的方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：在VisionMaster 软件里，修改模块参数值时，右下角的状态栏会显示修改记录并
且记录至本地日志，而在VM 二次开发里不会显示修改和记录日志。  
 
解答  
当前VM 二次开发默认不支持，要支持需手动添加代码Apps.XmlParser.ParamTab.
NameValueItem.logManager = new Apps.XmlUI.UILogManager(false);



<!-- page 584 -->
HIKROBOT 
 
575 
 
 
加载到程序初始化函数里。其中，添加引用集Apps.XmlParser.dll 和Apps.XmlUI.dll 在
VM 安装路径“VisionMaster4.2.0\Development\V4.x\ComControls\Assembly”下。
  
示例代码如下：  
C#  
public Form1() 
{ 
InitializeComponent(); 
Apps.XmlParser.ParamTab.NameValueItem.logManager = new Apps.X
mlUI.UILogManager(false); 
} 
添加后，控件日志显示如下：  



<!-- page 585 -->
HIKROBOT 
 
576 
 
 
 
并且，在二次开发应用程序exe 同级下的log/UI/SystemLog.log 就会记录模块参
数修改的日志。  
注：若没有该log，请将VisionMaster 路径“VisionMaster4.2.0\Development\V4.x 
\ComControls\Assembly”下的第一个文件夹“3rdLib”拷贝替换至二次开发应用程序e
xe 同级路径下。  
问题根因  
某些功能接口不对外开放，需手动添加。 
 
 



<!-- page 586 -->
HIKROBOT 
 
577 
 
 
2.3.11 渲染控件：渲染控件绘制十字方法 
描述 
环境：VM4.2 + VS2013 及以上 
现象：如何在vmRenderControl 控件上显示十字线？  
解答 
1. 使用控件AddShape()接口显示十字线(渲染控件渲染时机为流程执行结束回调，适合静
态显示)，示例代码如下； 
C# 
 
/// <summary> 
/// 流程工作状态回调 
/// </summary> 
/// <param name="workStatusInfo"></param> 
private void VmSolution_OnWorkStatusEvent(VM.PlatformSDKCS.ImvsSdkDefine.IMVS_MODULE_
WORK_STAUS workStatusInfo) 
{ 
    if (workStatusInfo.nWorkStatus == 0 && workStatusInfo.nProcessID == 10000)//流程
空闲且为流程1 
    { 
        if (vmRenderControl1.ImageSource != null) 
        { 
            var width = vmRenderControl1.ImageSource.Width; 
            var height = vmRenderControl1.ImageSource.Height; 
            var lineY = new LineEx(new System.Windows.Point(width / 2, 0), new Syste
m.Windows.Point(width / 2, height), stroke: "#4400FF"); 
            var lineX = new LineEx(new System.Windows.Point(0, height / 2), new Syste
m.Windows.Point(width, height / 2), stroke: "#4400FF"); 
            renderControl.vmRenderControl1.AddShape(lineX); 
            renderControl.vmRenderControl1.AddShape(lineY); 
        } 
    } 
} 
2. 使用几何创建模块生成直线的方式创建十字线(推荐)； 



<!-- page 587 -->
HIKROBOT 
 
578 
 
 
 
 
最终二次开发渲染控件显示效果如图所示： 



<!-- page 588 -->
HIKROBOT 
 
579 
 
 
 
问题根因 
不熟悉渲染控件的使用。 
 
 
 



<!-- page 589 -->
HIKROBOT 
 
580 
 
 
2.4 结果获取类 
2.4.1 数据结果：通过流程输出或者模块输
出获取数据结果的方法  
描述  
环境：VM4.2 + VS2013 及以上  
现象：方案或流程运行执行之后，就可以获取结果（建议将结果获取写在回调函数里），
可以通过流程或者模块的输出获取渲染结果和数据结果，推荐使用流程的输出，符合高内
聚低耦合，渲染结果通过绑定渲染控件进行显示，数据结果分为整型、浮点型、字符串型
和图像型等等，VM 二次开发如何获取数据结果？  
解答  
数据结果的获取可以通过流程的输出或者模块的输出，推荐使用通过流程的输出，符合高
内聚低耦合的思想，VM4.2 二次开发相比较VM4.0 二次开发获取数据结果有一些更新，
详细介绍如下所示：  
1 通过流程的输出获取数据结果  
1.1 流程配置-输出设置  



<!-- page 590 -->
HIKROBOT 
 
581 
 
 
 
1.2 获取整型、浮点型、字符串型数据  
 
C# 
VmProcedure vmprocess = (VmProcedure)VmSolution.Instance["流程1
"]; 
var moduResult = vmprocess.ModuResult; 
string str = moduResult.GetOutputInt(“out”).pIntVal[0].ToString();   
              
string str1 = moduResult.GetOutputFloat(“out0”).pFloatVal[0].ToStri
ng(); 
string str2 = moduResult.GetOutputString("out1").astStringVal[0].strVa
lue; 
//获取流程结果列表，str3 与str2 结果一致 



<!-- page 591 -->
HIKROBOT 
 
582 
 
 
List<VmDynamicIODefine.IoNameInfo> ioNameInfos = VmProcess.Mo
duResult.GetAllOutputNameInfo(); 
string str3 = VmProcess.ModuResult.GetOutputString(ioNameInfos[2].
Name).astStringVal[0].strValue; 
1.3 获取图像数据  
流程输出设置中输出IMAGE 类型的图像数据，能通过前面参数名称ImageD 直接获取。  
 
C# 
ImageBaseData_V2 processImageData = VmProcess1.ModuResult.Get
OutputImageV2("ImageD"); 
int width = processImageData.Width;//宽 
int height = processImageData.Height;//高 
IntPtr imageByte = processImageData.ImageData;//数据 
VMPixelFormat pixelformat = processImageData.Pixelformat;//格式 
2 通过模块的输出获取数据结果 （与4.0 二次开发相比无变化）  
2.1 获取模块的浮点型数据  
 
C# 



<!-- page 592 -->
HIKROBOT 
 
583 
 
 
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolutio
n.Instance["流程1.圆查找1"]; 
var moduResult = tool.ModuResult; 
string circleX = moduResult.OutputCircle.CenterPoint.X.ToString(); 
string circleY = moduResult.OutputCircle.CenterPoint.Y.ToString(); 
string circleR = moduResult.OutputCircle.Radius.ToString(); 
2.2 获取图像数据，针对有图像输出的模块，例如，输出图像模块，注意像素格式17301
505 为MONO8 灰度图，像素格式 35127316 为RGB24 彩色图。  
 
C# 
SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance[“流
程1.输出图像1”]; 
Var saveImageResult=saveIamge.ModuResult.OutputImage; 
byte[] imageData= saveImageResult.ImageData; 
int imagePixelformat= saveImageResult.Pixelformat; 
问题根因  
不熟悉如何获取数据结果。  



<!-- page 593 -->
HIKROBOT 
 
584 
 
 
2.4.2 流程回调：某个流程运行开始与结束
的回调方法 
描述 
环境：VM4.2 + VS2013 及以上 
现象：除了所有流程运行结束的回调方法，如何注册某一流程开始与结束回调函数。 
解答 
1、C#中调用某个流程的开始与结束回调 
加载sol 文件后，根据流程名称注册流程开始和结束回调函数代码如下，其中textBoxProce
ssName.Text 为流程名。  
 
c# 
try   
{   
    m_VmPrc = (VmProcedure)VmSolution.Instance[textBoxProcessNa
me.Text];   
    if (null == m_VmPrc)   
    {   



<!-- page 594 -->
HIKROBOT 
 
585 
 
 
        MessageBoxButtons msgType = MessageBoxButtons.OK;   
        DialogResult diagMsg = MessageBox.Show(textBoxProcessNa
me.Text + " name procedure does't exist", "Prompt", msgType);   
        if (diagMsg == DialogResult.OK)   
        {   
            return;   
        }   
    }   
    m_VmPrc.OnWorkBeginStatusCallBack += M_VmPrc_OnWorkBegin
StatusCallBack;   
    m_VmPrc.OnWorkEndStatusCallBack += M_VmPrc_OnWorkEndSta
tusCallBack;   
}   
catch (VmException ex)   
{   
    string strMsg = "Process failed. Error Code: " + Convert.ToString
(ex.errorCode, 16);   
    listBoxMsg.Items.Add(strMsg);   
    listBoxMsg.TopIndex = listBoxMsg.Items.Count - 1;   
    return;   
}   



<!-- page 595 -->
HIKROBOT 
 
586 
 
 
注消流程开始和结束回调函数代码如下。  
 
try   
{   
    m_VmPrc = (VmProcedure)VmSolution.Instance[textBoxProcessNa
me.Text];   
    if (null == m_VmPrc)   
    {   
        MessageBoxButtons msgType = MessageBoxButtons.OK;   
        DialogResult diagMsg = MessageBox.Show(textBoxProcessNa
me.Text + " name procedure does't exist", "Prompt", msgType);   
        if (diagMsg == DialogResult.OK)   
        {   
            return;   
        }   
    }   
   m_VmPrc.OnWorkBeginStatusCallBack -= M_VmPrc_OnWorkBeginS
tatusCallBack;   
   m_VmPrc.OnWorkEndStatusCallBack -= M_VmPrc_OnWorkEndStatu
sCallBack;   
}   



<!-- page 596 -->
HIKROBOT 
 
587 
 
 
catch (VmException ex)   
{   
    string strMsg = "Process failed. Error Code: " + Convert.ToString
(ex.errorCode, 16);   
    listBoxMsg.Items.Add(strMsg);   
    listBoxMsg.TopIndex = listBoxMsg.Items.Count - 1;   
    return;   
}  
测试用回调函数如下。  
   
private void M_VmPrc_OnWorkBeginStatusCallBack(object sender, Eve
ntArgs e)   
{   
    Console.WriteLine($"{DateTime.Now.ToString("yyyy-MM-dd HH:m
m:ss.fff")} 流程开始");   
    //获取此流程中的模块结果 
}  
private void M_VmPrc_OnWorkEndStatusCallBack(object sender, Event
Args e)   
{   



<!-- page 597 -->
HIKROBOT 
 
588 
 
 
    Console.WriteLine($"{DateTime.Now.ToString("yyyy-MM-dd HH:m
m:ss.fff")} 流程结束");   
} 
单次运行流程  m_VmPrc.Run()，执行效果如下，说明首先执行的是M_VmPrc_OnWork
BeginStatusCallBack 函数，然后执行的是M_VmPrc_OnWorkEndStatusCallBack 函
数； 
2、C++ 中调用某个流程的开始与结束回调 
注册回调，只需要创建一个流程事件类，这个流程事件类继承IVmProcedureEvent，代
码如下所示： 
 
class MyProcedureEvent :public  IVmProcedureEvent 
{ 
public: 
 
virtual void  OnWorkBeginStatusCallBack(IN const IMVS_PF_M
ODULE_WORK_STAUS *const pstWorkStatus, IN void *const pUser) o
verride; 
 
virtual void  OnWorkEndStatusCallBack(IN const IMVS_PF_MO
DULE_WORK_STAUS *const pstWorkStatus, IN void *const pUser) ov
erride; 


