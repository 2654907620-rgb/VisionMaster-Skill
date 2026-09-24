# 第2章 VM二次开发（VM4.0：环境配置/模块API/控件嵌入/结果获取/全局工具）
<!-- pages 218-386 -->

<!-- page 218 -->
HIKROBOT 
 
209 
 
 
 
发送事件中配置好需要发送的数据，上图中配置好了触发数据（注意选择正确的绑定地
址，绑定地址在前面添加通讯设备时已经创建）接着配置特征匹配状态，如下图所示：  
 
配置特征点X 坐标数据，如下图所示：  



<!-- page 219 -->
HIKROBOT 
 
210 
 
 
 
配置特征点Y 坐标数据，如下图所示：  
 
配置发送角度，如下图所示：  



<!-- page 220 -->
HIKROBOT 
 
211 
 
 
 
  
第六步，在流程中配置发送数据模块，在流程编辑页面添加数据发送模块，如下图所示： 
 



<!-- page 221 -->
HIKROBOT 
 
212 
 
 
如图中所示的那样，这里配置了5 个数据发送模块，之所以要配置5 个数据发送模块，是
因为单个数据发送模块，发送非字符串类型且每一项数据类型又不相同是做不到的，其
中复位寄存器，匹配状态数据类型是整数类型，而匹配点X，匹配点Y，匹配角度是浮点
数类型，因此，这里只能用5 个数据发送模块来实现。以上图中，发送数据1 为例，需要
发送0 到寄存器0000，所以配置如下图所示： 
 
由于输出数据，订阅的值不可以是常量，所以这里选择订阅一个全局变量，这个全局变量
的值为0。  



<!-- page 222 -->
HIKROBOT 
 
213 
 
 
其他4 个发送数据模块的配置，也同样配置，主要是发送事件中下来选择正确的地址即
可。匹配状态的数据发送配置如下图所示：  
 
坐标X 的数据发送配置，坐标Y 的数据发送，如下图所示： 



<!-- page 223 -->
HIKROBOT 
 
214 
 
 
 
匹配坐标Y 的数据发送，如下图所示： 



<!-- page 224 -->
HIKROBOT 
 
215 
 
 
 
匹配角度的数据发送，如下图所示： 



<!-- page 225 -->
HIKROBOT 
 
216 
 
 
 
至此为止，所有配置全部完成了，其实需要配置的步骤并不多，这里之所以把详细的每一
步都贴图出来，目的就是为了让阅读本文的初级用户，按照本文的操作步骤一步一步来，
也能解决该问题。  
问题根因 
1. 不了解接收事件怎么用 
2. 不了解发送事件怎么用 



<!-- page 226 -->
HIKROBOT 
 
217 
 
 
3. 发送非字符串类型的多个组合数据怎么操作 
4. 不了解全局触发工具怎么用  
 
 
 



<!-- page 227 -->
HIKROBOT 
 
218 
 
 
第2 章 VM 二次开发 
2.1 环境配置类 
2.1.1 环境配置：CSharp 二次开发环境配
置方法  
描述  
环境：VM4.0.0 + VS2015 及以上 
现象：C#二次开发环境的配置方法  
解答  
以WinForm 为例，进行VM 二次开发的环境配置分为三步：  
第一步，使用VS 新建一个框架为.NET Framework 4.6.1 的工程，平台首选32 位取消勾
选，重新生成解决方案，保证工程Debug 下存在exe 文件，最后关闭新建工程。  



<!-- page 228 -->
HIKROBOT 
 
219 
 
 
 
 
第二步，将VM 安装目录下的文件“\VisionMaster4.0.0\Development\V4.0.0 \ComC
ontrols\bin\x64”下整体拷贝到新建工程的Debug 下。  



<!-- page 229 -->
HIKROBOT 
 
220 
 
 
 
第三步，启动二次开发导入工具（“\VisionMaster4.0.0\Development\V4.0.0 \ComC
ontrols\Tool\ImportRef.exe”），Module(sp)的路径在生成工程Debug 下的Module
（sp）文件夹，项目所在路径为bin 文件的上一层，在选择完指定的路径之后，需要选择
引用模块的dll 以及是否选择相对路径，最后点击确定，完成环境配置。  



<!-- page 230 -->
HIKROBOT 
 
221 
 
 
 
另外，当用户是第一次配置环境时，工具箱中将没有VM 相关控件，可按如下步骤进行添
加。  
（1）右击所有窗体，点击选择项。  



<!-- page 231 -->
HIKROBOT 
 
222 
 
 
 
（2）浏览当前项目路径的debug 路径，Winform 项目选择VMControls.Wi
nform.Release.dll，最后点击确认。WPF 应用程序则是选择VMControls.WP
F.Release.dll 



<!-- page 232 -->
HIKROBOT 
 
223 
 
 
 
问题根因  
不熟悉C#二次开发环境配置。  
 
 



<!-- page 233 -->
HIKROBOT 
 
224 
 
 
2.1.2 环境配置：Qt 二次开发环境配置方法
  
描述  
环境：VM4.0.0 + VS2019+Qt5.12.3  
现象：Qt+VS 二次开发环境如何配置？  
解答  
1 新建Qt 工程，添加Qt 模块Core、GUI、Active Qt 和Container Widgets 
 



<!-- page 234 -->
HIKROBOT 
 
225 
 
 
 
2 拷贝DLL:VM\VisionMaster4.0.0\Development\V4.0.0\ComControl\bin\x64 下的
所有拷贝到项目工程输出目录下，如下图所示，项目的输出路径是Dll 文件夹。  
 
 
3 第一种方法：通过拷贝include 文件及lib 文件至项目工程中的方式配置VM 环境  
3.1 拷贝\VisionMaster4.0.0\Development\V4.0.0\includes 下的头文件。  



<!-- page 235 -->
HIKROBOT 
 
226 
 
 
 
3.2 拷贝\VisionMaster4.0.0\Development\V4.0.0\ComControl\includes\QT 下的头
文件。  
 
3.3 拷贝\VisionMaster4.0.0\Development\V4.0.0\libraries\win64\C 下的所有库文
件。  
 
将以上三个文件夹拷贝到如下所示的项目路径中。  



<!-- page 236 -->
HIKROBOT 
 
227 
 
 
 
4 第二种方法：通过配置VC++目录和链接器的方式配置VM 环境  
4.1 VC++目录下包含目录添加以下路径：  
1):\VisionMaster4.0.0\Development\V4.0.0\includes 2):\VisionMaster4.0.0\De
velopment\V4.0.0\ComControl\includes\QT 
 
4.2 库目录添加以下路径：  
\VisionMaster4.0.0\Development\V4.0.0\libraries\win64\C 



<!-- page 237 -->
HIKROBOT 
 
228 
 
 
 
4.3 VC 链接器附加依赖项写入iMVS-6000PlatformSDK.lib 
 
5.配置完成：#include 能索引到VM 模块.h 文件。  
 
6 第一个VM 界面：  



<!-- page 238 -->
HIKROBOT 
 
229 
 
 
6.1 添加容器控件QAxWidget:QAxWidget 类是一个包装ActiveX 控件的Qwidget，绑
定VM 控件到QAxWidget 控件，VM 相关控件在安装时已经注册到windows 组件中。  
 
6.2 创建方案句柄初始化控件：在ui 界面布局相关控件后，创建VM 方案句柄，初始化V
M 控件。  



<!-- page 239 -->
HIKROBOT 
 
230 
 
 
CreateSolutionInstance(); 
ui.axWidget->dynamicCall("GetObjectPointer()"); 
6.3 运行结果：  
 
问题根因  
不熟悉Qt 二次开发环境配置。  
 
 



<!-- page 240 -->
HIKROBOT 
 
231 
 
 
2.1.3 环境配置：MFC 二次开发环境配置
方法  
描述  
环境：VM4.0.0 + VS2015 及以上 
现象：MFC 二次开发环境如何配置？  
解答  
1 新建MFC 工程，拷贝DLL:VM\VisionMaster4.0.0\Development\V4.0.0 \ComCont
rol\bin\x64 下的所有拷贝到项目工程输出目录下，如下图所示，项目的输出路径是Dll 文
件夹。  
 



<!-- page 241 -->
HIKROBOT 
 
232 
 
 
 
2 通过配置C++目录和链接器的方式配置VM 环境 
2.1 C++目录下添加附加包含目录.\Includes。  



<!-- page 242 -->
HIKROBOT 
 
233 
 
 
 
2.2 链接器下添加库目录.\Libraries\win64\C。  
 
2.3 链接器输入里的附加依赖项写入VM 的算法依赖库iMVS-6000PlatformSDK.lib  



<!-- page 243 -->
HIKROBOT 
 
234 
 
 
 
3 添加控件源文件至工程中，复制.\VisionMaster4.0.0\Development\V4.0.0\ComCont
rols\Includes\VS2017(根据VS 版本选择)下的控件源文件至工程目录下并引入到工程文
件。  
 



<!-- page 244 -->
HIKROBOT 
 
235 
 
 
 
4 配置完成：#include 能索引到模块.h 文件。  
 
5 第一个VM 界面：  



<!-- page 245 -->
HIKROBOT 
 
236 
 
 
5.1 添加ActiveX 控件，VM 控件在安装时已注册如windows，可直接选择。  
 
5.2 控件绑定与初始化  
定义控件变量：  
protected: 
 
CVmProcedureControlInterface m_ctrlProcedure; 
控件绑定：  
void CVMMFCApplication1Dlg::DoDataExchange(CDataExchange* pDX) 
{ 
 
CDialogEx::DoDataExchange(pDX); 
 
DDX_Control(pDX, IDC_VMUSERCONTROL1, m_ctrlProcedure); 
} 



<!-- page 246 -->
HIKROBOT 
 
237 
 
 
控件初始化：  
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
5.3 运行结果：  



<!-- page 247 -->
HIKROBOT 
 
238 
 
 
 
问题根因  
不熟悉MFC 二次开发环境配置。  
 
 



<!-- page 248 -->
HIKROBOT 
 
239 
 
 
2.1.4 环境配置：VB.Net 二次开发环境配
置方法  
描述  
环境：VM4.0+VS2015 及以上  
现象：使用Visual Basic 语言来进行VM 二次开发的环境搭建。  
解答  
Visual Basic 进行VM 二次开发的环境配置分为三步。  
第一步，使用VS 新建一个框架为.NET Framework 4.6.1，平台去勾选首选32 为的
工程，重新生成解决方案，保证工程Debug 下存在exe 文件，最后关闭新建工程；  



<!-- page 249 -->
HIKROBOT 
 
240 
 
 
 
 
第二步，将VM 安装目录下的文件“\VisionMaster4.0.0\Development\V4.0.0\ComCo
ntrols\bin\x64”整体复制拷贝到新建工程的Debug 下；  



<!-- page 250 -->
HIKROBOT 
 
241 
 
 
 
第三步，添加工程引用，需要手动引用基本库和相关模块工具的dll；  
 
第四步，修改APP.Config 文件，拷贝了众多VM 依托dll 于项目的Debug 目录下，
还需要在项目的APP.Config 中的privatePath 上指明dll 位置，因此需要客户对AP
P.Config 中添加如下代码，完成整体环境配置。  



<!-- page 251 -->
HIKROBOT 
 
242 
 
 
 
问题根因  
二次开发环境配置功能不熟悉。  
2.1.5 环境配置：运行出现Vm.Core.Solu
tion 报错的解决方法  
描述  
环境：VM4.0.0 + VS2015 及以上 
现象：VM4.0.0 环境配置运行出现Vm.Core.Solution 报错。  
解答  
（1）检查加密狗有没有插好？ 是否以管理员权限启动程序？首选32 位是否取消勾选？ 
（2）查看VM4.0 的版本信息是否为最新版本？版本信息为20220415 以上，版本越新问
题就会越少。如果打过最新补丁（截止20220505，最新补丁为20220505，建议用户打



<!-- page 252 -->
HIKROBOT 
 
243 
 
 
上最新补丁），则需要将打完补丁后的VisionMaster4.0.0\Development\V4.0.0\ComC
ontrols\bin\x64 下面所有的文件全部替换到二次开发项目的EXE 生成路径下（Debug
下）。  
（3）在任务管理器中关闭所有VM 相关程序，这种操作可以在二次开发的初始化处用如
下代码代替。（以防VM 双开） 。 
 
C# 
KillProcess("VisionMasterServerApp"); 
KillProcess("VisionMaster"); 
void KillProcess(string strKillName) 
{ 
    foreach(System.Diagnostics.Process p in System.Diagnostics.Proce
ss.GetProcesses()) 
    { 
        if (p.ProcessName == strKillName) 
        { 
            try 
            { 
                p.Kill(); 
                p.WaitForExit(); 



<!-- page 253 -->
HIKROBOT 
 
244 
 
 
            } 
            catch(Exception e) 
            { 
                Console.WriteLine(e.Message.ToString()); 
            } 
        } 
    }           
} 
补充： 
VM 启动时，拉起来的进程有四个：VisionMaster.exe，VisionMasterServer.exe，Visio
nMasterServerAPP.exe，VmModuleProxy.exe； 
VM SDK 程序启动时，拉起来的进程有两个：VisionMasterServer.exe，VmModulePro
xy.exe； 
所以，只需要结束VisionMaster.exe 和VisionMasterServerAPP.exe 进程即可。 
（4）检查VM 安装环境是否正常？运行VisionMaster4.0.0\Applications\Tools 目录下
的EnvironmentDetectionTool.exe。  
（5）如果这期间打开过多个版本的VM，可以试一下重启电脑或打开相应版本的VM 来
拉起相应版本的服务。  



<!-- page 254 -->
HIKROBOT 
 
245 
 
 
（6）是否严格按照环境步骤来配置环境？是使用ImportRef 工具添加引用，针对一个项
目，工具只使用一次。  
问题根因  
不熟悉如何排查报错原因 
 
 



<!-- page 255 -->
HIKROBOT 
 
246 
 
 
2.1.6 模块索引：MFC 模块索引异常解决
办法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：文件编码格式为UTF-8 不带签名编码格式，模块索引会出现 模块无法找到异常  
 
 
解答  
更改文件类型为UTF-8 带签名格式或vs 默认GBK2312 编码格式 



<!-- page 256 -->
HIKROBOT 
 
247 
 
 
 
问题根因  
不熟悉引用库环境配置。  
 
 



<!-- page 257 -->
HIKROBOT 
 
248 
 
 
2.1.7 环境配置：报错序列不包含任何元素
的解决方法  
描述  
环境：VM4.0.0+VS2015 及以上 
现象：配置环境后，获取线线测量模块结果，报错“序列不包含任何元素”。如下图所
示： 
 
解答  
将“\VisionMaster4.0.0\Development\V4.0.0 \ComControls\bin\x64”下整体重新拷
贝。 
问题根因  



<!-- page 258 -->
HIKROBOT 
 
249 
 
 
相关依赖库未拷贝。  
2.1.8 环境配置：提示未注册ActiveX 控件
的解决方法  
描述  
环境：VM4.0.0 +VS2015 及以上  
问题：如何解决MFC 插入VM 的控件时，报错未注册ActiveX 控件的问题，报错截图如
下：  



<!-- page 259 -->
HIKROBOT 
 
250 
 
 
 
解答  
关闭VS 后，重新注册VM 控件，注册步骤如下：  



<!-- page 260 -->
HIKROBOT 
 
251 
 
 
10 解注册VM 控件，找到如下的win64 路径下，右键以管理员权限运行ComUnRegiste
r.bat 执行解注册。  
2）注册VM 控件，找到如下的win64 路径下，右键以管理员权限运行ComRegister.bat
执行注册。  
3）对win32 文件夹下的两个文件重复上述操作。  
 



<!-- page 261 -->
HIKROBOT 
 
252 
 
 
 
问题根因  
不了解如何注册VM 控件。  
 
 



<!-- page 262 -->
HIKROBOT 
 
253 
 
 
2.1.9 控件失效：VM 控件运行时不显示的
解决方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：编译成功后，没有报错，运行之后VM 控件是黑色的，不显示任何内容。如下图右
边的黑色区域所示。  
 
解答  
此时为环境配置错误，确定本地VM 是否是最新版本，然后将本地VM 的路径（如：D:\V



<!-- page 263 -->
HIKROBOT 
 
254 
 
 
M4.0\VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64）下的所有文件
复制到项目路径的Debug 文件下。  
问题根因  
不熟悉全局变量工具及其接口。  
 
 



<!-- page 264 -->
HIKROBOT 
 
255 
 
 
2.1.10 环境配置：Qt 开发环境出现rc.ex
e 无法启动报错解决办法  
描述  
环境：VM4.0.0 + VS2015+Qt5.9.9 
现象：编译出现rc.exe 无法启动  
解答  
1. 找到WindowsSDK 的x86 目录下的rc.exe 以及rcdll.dll 文件  
 
2. 复制到VS bin 目录下  



<!-- page 265 -->
HIKROBOT 
 
256 
 
 
 
问题根因  
系统问题  
 
 



<!-- page 266 -->
HIKROBOT 
 
257 
 
 
2.1.11 控件失效：添加引用后导致控件失
效的解决方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：在VM 二次开发中，有些引用需要手动添加，如引用VMControls.WPF.dll 进行在
渲染控件上绘图。但是，在添加之后运行项目，界面上的VM 控件区失效，如下图所示的
vmProcedureConfigControl、vmRenderControl 和vmGlobalToolControl。 
 
解答  
因为VM 的引用都是采用相对路径的方式，如果此时是从VM 的安装路径中来添加相加的
引用，则需要打开当前引用的dll 的属性，将复制本地改为False，如下图所示：  



<!-- page 267 -->
HIKROBOT 
 
258 
 
 
 
问题根因  
不熟悉VM 二次开发中的引用。  
 
 



<!-- page 268 -->
HIKROBOT 
 
259 
 
 
2.1.12 添加引用：在原有项目中新配置深
度学习环境的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：在VM 没有装深度学习模块时搭建了二次开发项目，后来项目中需要应用到深度学
习。VM 中可以很方便的安装深度学习模块，那么如何在原有的项目中配置深度学习模块
的dll 呢？  
解答  
在原有项目中新配置深度学习环境的步骤如下所示：  
1、VM 中安装好深度学习模块后，将本地VM 路径下\VM4.0\VisionMaster4.0.0\Devel
opment\V4.0.0\ComControls\bin\x64 的dll 全部拷贝到项目的debug 下。  
2、手动添加引用项目debug 下Module(sp)\x64\DeepLearning 相应文件里面的dll， 
C 代表CPU。  



<!-- page 269 -->
HIKROBOT 
 
260 
 
 
 
注意手动添加后，引用的属性立马修改（复制本地路径为false）。为true 时，debug 就
会有刚刚复制过来的dll，debug\Module(sp)\x64 下的文件夹中也有，代码就会找不
到。如果debug 下已经有了，就要删除掉。  
 
3、修改app.config，在<probing privatePath=>的后面添加相应的深度学习的相对路
径Module(sp)\x64\DeepLearning\ IMVSCnnClassifyModuC 
4、注意，其它模块手动添加引用的步骤类似，但是由于手动添加引用的步骤比较复杂，
且对于模块以外的dll 很难添加齐全，所以推荐使用引用工具来添加引用（“\VisionMast



<!-- page 270 -->
HIKROBOT 
 
261 
 
 
er4.0.0\Development\V4.0.0 \ComControls\Tool\ImportRef.exe”），且对于一个项
目只使用一次工具。  
问题根因  
不熟悉环境配置  
 
 



<!-- page 271 -->
HIKROBOT 
 
262 
 
 
2.1.13 用户权限：普通用户权限以EXE 方
式启动Server 的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：当客户二次开发程序，需要以Windows 普通用户权限调用Vm 做视觉处理，需要
将Server 以EXE 方式启动。  
解答  
1）安装VM20220415 的安装包，然后安装补丁包（截止20220505，最新补丁为2022
0505，建议用户打上最新补丁）。如果VM4.0 维护版2022 年5 月份之后的有完整包，
直接安装即可，不用安装补丁包。  
2）修改二次开发程序的xxx.exe.config 配置文件，在“AppSettings”里面增加以下两
条信息。下图以圆查找demo 程序为例。注意“ServerPath”是该电脑上Server 的绝对
路径，要填正确。  
 



<!-- page 272 -->
HIKROBOT 
 
263 
 
 
 
问题根因  
不熟悉普通用户权限二次开发的配置。  
 
 



<!-- page 273 -->
HIKROBOT 
 
264 
 
 
2.1.14 引用工具：使用引用工具添加引用
报错的解决方法  
描述  
环境：VM4.0.0 +VS2015 及以上  
现象：在VM4.0 的二次开发环境配置中，ImportRef 可以帮助用户为项目自动添加引
用，但有时会报错缺少mfc120u.dll。  
 
解答  
这个问题可以直接运行VM 安装路径下的驱动MSVBCRT.AIO_v2020.05.20.exe 解决：  



<!-- page 274 -->
HIKROBOT 
 
265 
 
 
 
问题根因  
不熟悉VM 自带的驱动。  
 
 



<!-- page 275 -->
HIKROBOT 
 
266 
 
 
2.1.15 环境配置：句柄创建失败解决问题
排查方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：VM 二次开发执行CreateSolutionInstance() 出现句柄错误问题。 
解答 
问题截图如下： 
 
解决办法：  
1. VM 平台软件如果开启，需要关闭退出。  



<!-- page 276 -->
HIKROBOT 
 
267 
 
 
2. VS 未开启管理员权限。  
3. 加密狗未插上，或未安装驱动。  
问题根因 
不熟悉VM 二次开发流程。  
 
 



<!-- page 277 -->
HIKROBOT 
 
268 
 
 
2.2 模块API 类 
2.2.1 方案保存：方案高速保存的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：二次开发软件调用VmSolution.Export(string Path)接口保存方案，保存时间较
长。 
解答  
保存方案将接口参数bDisplayProgress 置为false，或放在线程里调用。示例代码如下：  
C# 
VmSolution.Export(tb_SolPath.Text, "", false); 
问题根因  
不熟悉方案的相关接口  
 
 



<!-- page 278 -->
HIKROBOT 
 
269 
 
 
2.2.2 Group 模块：Group 输入输出图像
数据的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：Group 模块可以设置输入和输出，那如何进行图像数据的输入和输出？  
解答  
Group 相当于一个模块，实例化Group，通过相关接口可以设置图像数据的输入和输出。
  
1）设置图像数据的输入，下面是以独立的Group 为例，导入一个后缀为gro 的独立Gro
up。  
C# 
IMVSGroupTool group=null; 
//加载group 模块 
group = IMVSGroupTool.LoadGroup(@"C:\Users\zhouyigen\Desktop\L
ackImage.gro", ""); 
//利用OpenCV 的读图方法，读取图像 



<!-- page 279 -->
HIKROBOT 
 
270 
 
 
Mat matImage = Cv2.ImRead(@"C:\Users\zhouyigen\Desktop\Demo
(2)\smile.png",ImreadModes.Grayscale); 
//实例化VM 接口可接收的图像类型 
InputImageData StImg = new InputImageData(); 
//设置图像参数 
StImg.Names.DataName = "Imagein"; 
StImg.Names.HeightName = "ImageHeightin"; 
StImg.Names.WidthName = "ImageWidthin"; 
StImg.Names.PixelFormatName = "ImagePixelFormatin"; 
StImg.Height = matImage.Rows; 
StImg.Width = matImage.Cols; 
StImg.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO
8; 
StImg.DataLen = (uint)(matImage.Width * matImage.Height); 
StImg.Data = new byte[matImage.Width * matImage.Height]; 
  
//将读取到的图像拷贝给StImg 
Marshal.Copy(matImage.Data, StImg.Data, 0, matImage.Width * matI
mage.Height); 
// 设置图像数据 
group.ModuParams.SetInputImage(StImg);  



<!-- page 280 -->
HIKROBOT 
 
271 
 
 
//绑定渲染源 
vmRenderControl1.ModuleSource = group; 
也可以将流程中的Group 实例化，再使用流程的SetInputImage 接口。流程中的Group
中没有图像源模块，Group 的输入设置如下图，Group 中的其他模块需要选择图像输入
源，需要提前建立联系。  
 
2）获取输出的图像数据  



<!-- page 281 -->
HIKROBOT 
 
272 
 
 
可以参考2.4.1，给Group 中添加一个输出图像模块，通过输出图像模块来获取输出的图
像数据byte。  
也可以配置Group 的显示设置，订阅输出图像模块，再依照2.4.1 中获取流程中的图像数
据方法，Imgaeout 才是真正的图像名称。像素格式17301505 为MONO8 灰度图，像
素格式 35127316 为RGB24 彩色图。  
 
问题根因  
不熟悉针对Group 模块如何输入输出图像数据  
 
 



<!-- page 282 -->
HIKROBOT 
 
273 
 
 
2.2.3 模块操作类：设置输入图像、参数和
ROI 的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：每个模块类型命名不同，但拥有部分共同的相关操作。  
解答  
1 给模块设置输入图像，对应VM 中模块的图像输入源功能，以圆查找模块为例 。注
意：设置输入参数（基本参数），参数配置窗口界面不会显示所设置的参数，此时模块运
行，参数永久有效，流程运行，参数一次有效；设置运行参数，参数配置窗口界面会显示
所设置的参数，此时模块和流程运行，参数都永久有效。  
 
C# 
//VisionMaster4.0.0\Development\V4.0.0\ComControls\bin\x64 中包含O
penCvSharp.dll 



<!-- page 283 -->
HIKROBOT 
 
274 
 
 
Mat matImage = Cv2.ImRead(path, ImreadModes.Grayscale);//使用op
encv 读图，也可以使用BitMap 读图 
InputImageData StImg = new InputImageData(); 
StImg.Names.DataName = "InImage";//只能使用默认名称InImage 
StImg.Names.HeightName = "InImageHeight";//默认InImageHeight 
StImg.Names.WidthName = "InImageWidth";//默认InImageWidth 
StImg.Names.PixelFormatName = "InImagePixelFormat";//默认InImage
PixelFormat 
StImg.Height = matImage.Rows; 
StImg.Width = matImage.Cols; 
StImg.Pixelformat = ImagePixelFormat.IMAGE_PIXEL_FORMAT_MONO
8; 
StImg.DataLen = (uint)(matImage.Width * matImage.Height); 
StImg.DataLen = (uint)(matImage.Width * matImage.Height); 
Marshal.Copy(matImage.Data,StImg.Data,0,matImage.Width*matImage.
Height); 
IMVSCircleFindModuTool Circle = (IMVSCircleFindModuTool)process["
圆查找1"]; 
Circle.ModuParams.SetInputImage(StImg); 
2 配置参数，实例化模块为tool，然后设置tool.ModuParams 的属性。这里以圆查找模
块为例。如果没有相应的属性，则需要联系销售进行定制。 



<!-- page 284 -->
HIKROBOT 
 
275 
 
 
C# 
IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolutio
n.Instance[“流程1.圆查找1”]; 
tool.ModuParams.RadNum=10；// 卡尺数量 
3 设置ROI，这里以DL 字符识别CPU 模块为例，代码如下，其中0.5f 是比例关系（将
图像看作1）。  
C# 
public void OCRROISetFunc(ref VMControls.WPF.Release.VmRenderCo
ntrol vmRenderControl1) 
{ 
    /////////OCRROISET 
    MVSOcrDlModuCTool iMVSOcrDlModuCTool = (IMVSOcrDlModu
CTool)VmSolution.Instance["流程1.DL 字符识别C1"]; 
 
    RoiBox roiBox = new RoiBox(); 
    roiBox.bRoiType = (byte)RoiType.ROI_TYPE_BOX; 
    roiBox.fCenterX = 0.5f; 
    roiBox.fCenterY = 0.68f; 
    roiBox.fWidth = 0.5f; 
    roiBox.fHeight = 0.1f; 



<!-- page 285 -->
HIKROBOT 
 
276 
 
 
 
    IntPtr ptr = Marshal.AllocHGlobal(Marshal.SizeOf(roiBox)); 
    Marshal.StructureToPtr(roiBox, ptr, false); 
    iMVSOcrDlModuCTool.ModuParams.SetBinaryData("RoiType", ptr, 
(uint)Marshal.SizeOf(roiBox)); 
    vmRenderControl1.ModuleSource = iMVSOcrDlModuCTool; 
} 
4 C++中获取ROI、设置ROI、设置多个ROI、设置屏蔽区、设置多个屏蔽区的方法  
1）//拿到指向圆查找模块的指针 
IMVSCircleFindModuTool *CircleFindModu=static_cast((*m_pVmSol)["
流程1.圆查找1"]); 
ROI_BOX roiBox = { 0 }; 
unsigned int nLen=0; 
//获取ROI  
CircleFindModu->GetParamObj()->GetBinaryData("RoiType",&roiBox,si
zeof(roiBox), nLen); 
 
2）//圆卡尺类型ROI 
ROI_CIRCLECALIPER RoiCircle = { 0 ,0,0 ,0 ,0 ,0,0,0,0,0}; 
unsigned int nLen ; 



<!-- page 286 -->
HIKROBOT 
 
277 
 
 
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
CircleFindModu->GetParamObj()->SetBinaryData("RoiType",&RoiCircle,
sizeof(RoiCircle)); 
 
3）//获取指向BLOB 分析模块的指针 
IMVSBlobFindModuTool *blobFindMou=static_cast 
((*m_pVmSol)["流程1.BLOB 分析1"]); 
//设置ROI 数据 
ROI_BOX roiBox[2] = { 0 }; 
roiBox[0].bRoiType = ROI_TYPE_BOX; 
roiBox[0].bVersion = 0; 



<!-- page 287 -->
HIKROBOT 
 
278 
 
 
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
blobFindMou->GetParamObj()->SetBinaryData("RoiType",temp,sizeof(R
OI_BOX) * 2); 
 
4）// 



<!-- page 288 -->
HIKROBOT 
 
279 
 
 
ROI_POLYGON polygon = { 0 }; 
polygon.bRoiType = ROI_TYPE_POLYGON; 
polygon.bVersion = 0; 
polygon.nVertexNum = 4; 
//设置屏蔽区的4 个点 
polygon.stVertexPoints[0] = { 0.3,0.125 }; 
polygon.stVertexPoints[1] = { 0.575,0.087 }; 
polygon.stVertexPoints[2] = { 0.712,0.799 }; 
polygon.stVertexPoints[3] = { 0.31,0.8 }; 
//设置屏蔽区 
blobFindMou->GetParamObj()->SetBinaryData("ExternRoiType",&polyg
on,38); 
 
5）// 
polygon[1].bRoiType = ROI_TYPE_POLYGON; 
polygon[1].bVersion = 0; 
polygon[1].nVertexNum = 4; 
polygon[1].stVertexPoints[0] = { 0.6f,0.125f }; 
polygon[1].stVertexPoints[1] = { 0.8f,0.087f }; 
polygon[1].stVertexPoints[2] = { 0.4f,0.799f }; 
polygon[1].stVertexPoints[3] = { 0.3f,0.8f }; 



<!-- page 289 -->
HIKROBOT 
 
280 
 
 
//拷贝整合 
char* temp=new char[76]; 
memcpy(temp,&polygon[0],38); 
memcpy(temp+38,&polygon[1],38); 
//设置多个屏蔽区 
blobFindMou->GetParamObj()->SetBinaryData("ExternRoiType",temp,7
6); 
其中38 根据结构体内容计算字节数1+1+4+（4+4）*2：  
 
 
问题根因  
不熟悉如何对模块进行一些操作  



<!-- page 290 -->
HIKROBOT 
 
281 
 
 
 
 



<!-- page 291 -->
HIKROBOT 
 
282 
 
 
2.2.4 图像源：通过图像源模块接口设置图
像输入的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：在VM 中，可以通过如下图标给图像源模块输入本地图像，那如何通过代码的方式
给图像源模块设置图像的输入呢？  
解答  
知识点：图像源模块的输入图像分8 位图和24 位图，但图像算子只能处理8 位图。  
1）当图像源模块输入图像为24 位图，可以将像素格式选择MONO8，此时运行流程，图
像源的输出图像为8 位图，圆查找模块的图像输入源则选择图像源的图像数据。  
 



<!-- page 292 -->
HIKROBOT 
 
283 
 
 
 
2）当图像源模块输入图像为24 位图，也可以将像素格式选择位RGB24，并且打开输出
Mono8 使能，此时运行流程，图像源的输出图像为24 位图，并多了一个灰度图像数据，
圆查找模块的图像输入源则选择图像源的灰度图像数据。  
 
 
图像源接口的使用：  



<!-- page 293 -->
HIKROBOT 
 
284 
 
 
1 ）图像源类型为本地时LocalImage，此功能是VM 软件平台添加单个图像的实现，若
要添加图像文件夹，则是使用SetParamValue 接口来遍历文件夹中所有图像。  
 
C# 
ImageSourceModuleTool imageSourcTool = (ImageSourceModuleToo
l)VmSolution.Instance["流程1.图像源1"]; 
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.
ImageSourceTypeEnum.LocalImage; 
//给本地图增加图像 
imageSourcTool.ModuParams.SetParamValue("AddImage", "E:\\VSVM4.
0\\1.bmp"); 
//给本地图删除图像 
imageSource.ModuParams.SetParamValue("DeleteImage","C:\\Users\\zh
ouyigen\\Desktop\\2.jpg"); 
//给本地图清空图像 
imageSource.ModuParams.SetParamValue("ClearImage", "");   
 



<!-- page 294 -->
HIKROBOT 
 
285 
 
 
DirectoryInfo dir = new DirectoryInfo("E:\\VSVM4.2\\图像\\新建文件夹
"); 
FileInfo[] dirinfo = dir.GetFiles(); 
for (int i = 0; i < dirinfo.Length; i++) 
{ 
    string str= dirinfo[i].FullName; 
    imageSourcTool.ModuParams.SetParamValue("AddImage", str); 
} 
2） 图像源类型为SDK 时，通过SetImagePath 接口或者SetImageData 接口，其中Im
ageBaseData 类型，注意其像素格式Pixelformat，ImagePixelFormat.IMAGE_PIXEL_F
ORMAT_MONO8 为灰度图，ImagePixelFormat.IMAGE_PIXEL_FORMAT_RGB24 为
彩色图。  
C# 
imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.
ImageSourceTypeEnum.SDK; 
imageSourcTool.SetImagePath("E:\\VSVM4.0\\1.bmp"); 
imageSourcTool.SetImageData(imageBaseData);//参数类型为ImageBase
Data 
问题根因  



<!-- page 295 -->
HIKROBOT 
 
286 
 
 
不熟悉如何通过图像源模块接口设置输入图像  
2.2.5 图像源：通过SDK 传入相机图像的
方法  
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：在2.2.4 中介绍，当图像源类型为SDK 时， 可以使用SetImagePath 接口或者Se
tImageData 接口给图像源模块输入图像，那么如何使用SetImageData 传入相机图像
呢？  
解答  
1）可以手动将图像源类型设为SDK，也可以通过代码设置ImageSourceType 属性为SD
K 
 



<!-- page 296 -->
HIKROBOT 
 
287 
 
 
2）使用海康相机SDK 取流，输入图像源模块示例代码如下：  
C# 
private void SetImageTest() 
{ 
 
MyCamera m_MyCamera = new MyCamera(); 
 
try 
 
{ 
 
 
// ch:开始采集 | en:Start Grabbing  
 
 
int nRet=m_MyCamera.MV_CC_StartGrabbing_NET(); 
 
 
if (MyCamera.MV_OK != nRet){return;} 
 
 
//1.海康相机SDK 截取帧 
 
 
MyCamera.MV_FRAME_OUT stFrameOut = new MyCa
mera.MV_FRAME_OUT(); 
 
 
nRet = m_MyCamera.MV_CC_GetImageBuffer_NET(ref 
stFrameOut, 1000);         
 
 
if (nRet == MyCamera.MV_OK) 
 
 
{ 
 
 
 
//2.申请byte[]             
 
 
 
byte[] m_BufForDriver1 = new byte[stFrameO
ut.stFrameInfo.nFrameLen]; 
 
 
 
//3.海康相机取流 指针转byte[] 



<!-- page 297 -->
HIKROBOT 
 
288 
 
 
 
 
 
Marshal.Copy(stFrameOut.pBufAddr, m_BufFor
Driver1, 0, ((int)stFrameOut.stFrameInfo.nFrameLen)); 
 
 
 
//4.byte[]转ImageBaseData，其中1 也可以写成I
magePixelFormat.IMAGE_PIXEL_FORMAT_MONO8 
 
 
 
ImageBaseData stInputImageInfo = new Imag
eBaseData(m_BufForDriver1, stFrameOut.stFrameInfo.nFrameLen, stFra
meOut.stFrameInfo.nWidth, stFrameOut.stFrameInfo.nHeight, 1); 
 
 
 
//5.图像源设置ImageBaseData 图像数据 
 
 
 
ImageSourceModuleTool imageSourceModuleT
ool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"]; 
 
 
 
imageSourceModuleTool.SetImageData(stInputI
mageInfo); 
 
 
 
//流程执行 
 
 
 
process.Run(); 
 
 
} 
 
 
// ch:停止采集 | en:Stop Grabbing 
 
 
nRet = m_MyCamera.MV_CC_StopGrabbing_NET(); 
 
 
if (nRet != MyCamera.MV_OK) 
 
} 
 
catch (VmException ex) 
 
{ 



<!-- page 298 -->
HIKROBOT 
 
289 
 
 
 
 
return; 
 
} 
} 
C++ 
MV_FRAME_OUT_INFO_EX stImageInfo = { 0 }; 
//相机获取一帧图像 
nRet = m_pcMyCamera->GetOneFrameTimeout(m_pGrabBuf, m_nGra
bBufSize, &stImageInfo, 1000); 
ImageSourceModuleTool * pObject = (ImageSourceModuleTool *)(*m
_pVmSol)["流程1.图像源1"]; 
if (NULL == pObject) return; 
ImageBaseData pstImgData = { 0 }; 
pstImgData.ImageData = m_pGrabBuf; 
pstImgData.DataLen = stImageInfo.nWidth * stImageInfo.nHeight; 
pstImgData.Width = stImageInfo.nWidth; 
pstImgData.Height = stImageInfo.nHeight; 
pstImgData.Pixelformat = PIXEL_FORMAT_MONO8; 
pObject->SetImageData(&pstImgData); 
m_pVmSol->Run(); 
问题根因  



<!-- page 299 -->
HIKROBOT 
 
290 
 
 
不熟悉如何通过图像源模块接口SetImageData 传入相机图像  
 
 



<!-- page 300 -->
HIKROBOT 
 
291 
 
 
2.2.6 输出图像：获取渲染图像数据的方法
  
描述 
环境：VM4.0.0 + VS2015 及以上  
现象： 如何获取渲染图像的数据？  
解答  
1）存图到本地：在输出图像模块中，像素格式可选择为RGB24 或者MONO8，渲染设置
页面中可以订阅相应模块，获取渲染结果。保存渲染图到本地时，输出图像模块可以打开
存图使能，选择存图路径和文件命名，从而将渲染图保存到指定路径中。提示：渲染控件
也有存图接口，可以保存渲染图和原图到指定路径中，注意VM4.0 中渲染控件存图为24
位图。  



<!-- page 301 -->
HIKROBOT 
 
292 
 
 
 
 
2）获取渲染图像数据：通过实例化输出图像模块，从而获取图像数据byte。或者通过流
程输出设置订阅输出图像模块，从而获取流程输出图像数据byte。以通过模块输出为例的



<!-- page 302 -->
HIKROBOT 
 
293 
 
 
代码如下。详情可以参考2.4.1，像素格式17301505 为MONO8 灰度图，像素格式 351
27316 为RGB24 彩色图。  
C# 
SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance[“流
程1.输出图像1”];//实例化输出图像模块 
Var saveImageResult=saveIamge.ModuResult.OutputImage;  
byte[] imageData= saveImageResult.ImageData; 
int imagePixelformat= saveImageResult.Pixelformat;// 35127316 为彩
色图 
问题根因  
不熟悉如何获取渲染图像数据  
 
 



<!-- page 303 -->
HIKROBOT 
 
294 
 
 
2.2.7 N 点标定：清空标定点、生成标定文
件和渲染轨迹的方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：通过代码清空N 点标定模块中标定点的数据，通过代码生成标定文件。 
解答 
1）清空标定点、生成标定文件  
定义需要清空标定点的N 点标定模块，设置模块的ModuParams.SetParamValue()中"Cl
ear"参数为空；生成标定文件，设置模块的ModuParams.SetParamValue()中SaveCaib
Path 为指定路径。  
C# 
IMVSNPointCalibModuTool iMVSNPoint = (IMVSNPointCalibModuToo
l)VmSolution.Instance["流程1.N 点标定1"]; 
//清空标定点 
iMVSNPoint.ModuParams.SetParamValue("Clear" , ""); 
//生成标定文件 
iMVSNPoint.ModuParams.SetParamValue("SaveCalibPath" , path); 



<!-- page 304 -->
HIKROBOT 
 
295 
 
 
需要注意的是，用代码保存标定文件时需要先判断当前标定的状态，是否标定完，不然在
未标定完就保存标定文件就会报错保存失败。  
C# 
//获取标定状态 
IMVSNPointCalibModuTool iMVSNPoint = (IMVSNPointCalibModuToo
l)VmSolution.Instance["流程1.N 点标定1"]; 
int i = too.ModuResult.ModuStatus; 
if(i ==1){ } 
2）渲染控件渲染N 点标定轨迹  
N 点标定渲染显示和常规的模块有所不同，除了将N 点标定模块赋值给渲染控件外还需要
设置背景图像。示例代码如下  
C# 
vmRenderControl1.ModuleSource = N 点标定模块; 
VmIO CalibIO = VmSolution.Instance["流程名.图像源名.ImageData"] as 
VmIO; 
vmRenderControl1.SetBackgroundImage(CalibIO); 
问题根因 
不熟悉VM 二次开发接口。  



<!-- page 305 -->
HIKROBOT 
 
296 
 
 
2.2.8 耗时统计：流程与模块运行耗时的获
取方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：为计算总耗时间，需要了解如何获取流程或某个模块的运行时间。 
解答 
首先对流程、模块或算法进行实例化，然后调用接口ProcessTime（流程耗时）、Modul
eTime(模块耗时)、AlgorithmTime(算法耗时)查看耗时，以查看流程1 及圆查找运行时间
为例，代码如下：  
C# 
VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流
程1"]; 
IMVSCircleFindModuTool circleFind = (IMVSCircleFindModuTool)VmS
olution.Instance ["流程1.圆查找1"];  
float processtime = vmProcedure .ProcessTime;//流程运行时间 
float moduletime = circleFind.ModuleTime;//模块运行时间 
注意在回调函数里获取流程耗时，两种方法如下：  



<!-- page 306 -->
HIKROBOT 
 
297 
 
 
 
Task.Run(() => 
{ 
    float processtime = vmProcedure .ProcessTime;//流程运行时间 
}); 
 
或者 
 
float time = workStatusInfo.fProcessTime; 
问题根因  
不熟悉相关接口的使用。  
 
 



<!-- page 307 -->
HIKROBOT 
 
298 
 
 
2.2.9 资源释放：方案资源释放的方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：如何释放资源？  
解答 
当关闭VM 二次开发程序时，推荐使用Dispose 接口来释放资源。  
C# 
private void Form1_FormClosing(object sender, FormClosingEventArgs
 e) 
{ 
    VmSolution.Instance.Dispose(); 
} 
问题根因  
不熟悉相关接口的使用。  
 
 



<!-- page 308 -->
HIKROBOT 
 
299 
 
 
2.2.10 条件检测：条件检测模块设置范围
的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何用编程实现对条件检测模块所订阅的相关模块结果进行范围的设置。  
解答  
条件检测的相关接口类为IfModuleTool，int0 为所订阅的变量名，具体实现过程如下所
示：  
C# 
IfModuleTool ifModuleTool = (IfModuleTool)VmSolution.Instance["流
程1.条件检测1"]; 
ifModuleTool.ModuParams.GetDynamicParam("int0_Max").SetIntValue
(1000); 
ifModuleTool.ModuParams.GetDynamicParam("int0_Min").SetIntValue
(1); 
问题根因 



<!-- page 309 -->
HIKROBOT 
 
300 
 
 
不熟悉条件检测的相关接口。  
2.2.11 流程ID：通过流程名获取流程ID 的方法 
环境：VM4.0.0+vs2015 及以上 
现象：怎么获取流程ID？  
解答  
通过流程名可以获取流程ID。  
c# 
public static bool GetProcessID(string ProcessName, ref int ProcessI
D, ref string ErrorMessage) 
{ 
 
bool findIDResult = false; 
 
try 
 
{ 
 
 
ProcessInfoList stProcList = VmSolution.Instance.GetAll
ProcedureList(); // 获取所有流程列表 
 
 
for (int i = 0; i < stProcList.nNum; i++) 
 
 
{ 



<!-- page 310 -->
HIKROBOT 
 
301 
 
 
         
string _ProcessName = stProcList.astProcessInfo[i].strP
rocessName; 
         
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
问题根因  
不熟悉流程接口功能编写  



<!-- page 311 -->
HIKROBOT 
 
302 
 
 
 
 



<!-- page 312 -->
HIKROBOT 
 
303 
 
 
2.2.12 几何创建：绘制形状的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：在几何创建模块中，VM 二次开发如何通过代码绘制形状？  
解答  
因为几何创建中的绘制形状与设置ROI 相关，所以需要用ROI 的方式进行设置，需要拼
装二进制的数据。  
private void button6_Click(object sender, EventArgs e) 
{ 
    GeometryCreateTool tool = (GeometryCreateTool)VmSolution.Inst
ance["流程1.几何创建1"]; 
    Geo1line linetool = new Geo1line(); 
    linetool.nType = (byte)8; 
    linetool.fStartX = 123.0f / 5472; //由于归一化，所以要除以图像的高
和宽 
    linetool.fStartY = 100.0f / 3648; 
    linetool.fEndX = 2000.0f / 5472; 
    linetool.fEndY = 2000.0f / 3648; 



<!-- page 313 -->
HIKROBOT 
 
304 
 
 
    int size = Marshal.SizeOf(linetool); 
    IntPtr intpt = Marshal.AllocHGlobal(Marshal.SizeOf(linetool)); 
    Marshal.StructureToPtr(linetool, intpt, true); 
    //SetBinaryData 接口的参数分别为GeometryType，地址指针，内存大
小 
    tool.ModuParams.SetBinaryData("GeometryType", intpt, (uint)size);
//接口函数 
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



<!-- page 314 -->
HIKROBOT 
 
305 
 
 
问题根因  
不熟悉几何创建模块的接口。  
 
 



<!-- page 315 -->
HIKROBOT 
 
306 
 
 
2.2.13 运行间隔：设置和获取流程运行间
隔的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：VM 二次开发如何设置和获取流程运行间隔？  
解答  
C#  
//设置方案运行间隔 
VmSolution.Instance.SetRunInterval(500); 
  
//设置流程运行间隔 
VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//流程实例化 
VmProcess.SetContinousRunInterval(500); 
  
//获取流程运行间隔                        
uint time = 0; 



<!-- page 316 -->
HIKROBOT 
 
307 
 
 
ServerSDKManager.serverSDKManager.mProcessManager.GetContinous
RunInterval(10000, ref time); //第一个参数为流程ID，第二个参数为间隔
时间 
问题根因  
不熟悉二次开发设置与获取流程运行间隔的接口。  
 
 



<!-- page 317 -->
HIKROBOT 
 
308 
 
 
2.2.14 分支字符：控制调试模式开关的方
法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何控制分支字符调试模式的开关？  
解答  
在图的右边分支字符模块有两个分支，通过C#代码GetParamValue 函数可以看到调试模
式的相关参数ModuleInfoList 的值为：4#1#0$10#0#0$。其中分支4#1#0$的4 表示模
块id，1 表示这个分支的条件输入值，0 代表是否打开调试模式。  
 
问题根因  



<!-- page 318 -->
HIKROBOT 
 
309 
 
 
不熟悉分支字符模块的调试模式参数名及协议格式。  
 
 



<!-- page 319 -->
HIKROBOT 
 
310 
 
 
2.2.15 模块禁用：模块禁用的方法  
描述  
环境：VM4.0 + VS2015 及以上  
现象：如何将模块通过代码控制是否禁用与启用？效果类似VM 中的操作，如下所示：  
 
解答  
用户可以使用模块的IsForbidden 属性来禁用模块，但对于Group 模块的禁用之后无法
开启，改接口还未推荐对外使用，所以用的时候需要注意。  
 



<!-- page 320 -->
HIKROBOT 
 
311 
 
 
C# 
using IMVSCircleFindModuCs; 
IMVSCircleFindModuTool circleTool=( IMVSCircleFindModuTool)VmSol
ution.Instance["流程1.圆查找1"]; 
moduleTool.IsForbidden = true; 
问题根因  
不熟悉模块接口使用。  
 
 



<!-- page 321 -->
HIKROBOT 
 
312 
 
 
2.2.16 Group 循环：获取Group 循环数
据结果的方法  
描述  
环境：VM4.0.0+2015 及以上  
现象：如何获取Group 循环的所有数据结果？  
解答  
在Group 中使用数据集合模块，然后在Group 的输出设置订阅数据集合模块相关结果，
最后在二次开发中获取Group 的数据结果。如下图所示，参数out1 为Group 订阅的数
据集合，在代码中可以获取数据数组，但是在界面的显示上out1 中有重复值，后续会进
行改进。  
 
问题根因  
不熟悉如何获取Group 循环数据结果。  



<!-- page 322 -->
HIKROBOT 
 
313 
 
 
2.3 控件嵌入类 
2.3.1 渲染结果：通过绑定流程或模块获取
渲染结果的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：方案或流程运行执行之后，就可以获取结果，可以通过获取渲染结果和数据结果，
渲染结果通过绑定渲染控件进行显示。  
解答  
渲染结果的显示可以通过渲染控件绑定流程或者模块，推荐使用绑定流程，符合高内聚低
耦合的思想（绑定流程可以实现单个渲染控件绑定多个算法模块渲染结果）。详细介绍如
下所示：  
1 通过绑定流程显示渲染结果，一个渲染控件同时只能绑定一个流程，如需绑定多个流
程，需要分时绑定，或使用多个渲染控件。  
1.1 流程配置-显示设置  



<!-- page 323 -->
HIKROBOT 
 
314 
 
 
 
1.2 绑定流程  
C# 
VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程
1"];//实例化流程1 
vmRenderControl.ModuleSource=VmProcess; 
 
C++ MFC 
IVmProcedure *vmprc = (IVmProcedure*)(*m_pVmSol)["流程1"]; 
m_ctrlRender.SetParamsInfo(vmprc ->GetControlInfo()); 
 



<!-- page 324 -->
HIKROBOT 
 
315 
 
 
C++ Qt 
IVmProcedure *vmprc = (IVmProcedure*)(*m_pVmSol)["流程1"]; 
ui.axWidget_Cam1->dynamicCall("SetParamsInfo(qlongqlong)",(qlonglo
ng)(vmprc->GetControlInfo())); 
2 通过绑定模块显示渲染结果，只能渲染某个模块的渲染结果。  
C# 
IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool=(IMVSCircl
eFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆
查找1"]; 
vmRenderControl.ModuleSource= circleTool; 
 
C++ MFC 
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTo
ol *)(*m_pVmSol)["流程1.圆查找1"]; 
m_ctrlRender.SetParamsInfo(pCirFindObject ->GetControlInfo()); 
 
C++ Qt 
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTo
ol *)(*m_pVmSol)["流程1.圆查找1"]; 



<!-- page 325 -->
HIKROBOT 
 
316 
 
 
ui.axWidget_Cam1->dynamicCall("SetParamsInfo(qlongqlong)",(qlonglo
ng)(pCirFindObject ->GetControlInfo())); 
3 环境配置没有问题，程序编译运行都没有报错的情况下，但渲染控件界面不显示渲染结
果时，可以使用刷新接口。  
C# 
vmRenderControl1.UpdateVMResultShow(); 
问题根因  
不熟悉如何获取渲染结果  
 
 



<!-- page 326 -->
HIKROBOT 
 
317 
 
 
2.3.2 渲染控件：渲染控件加载本地图像的
方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：渲染控件如何显示本地图像？  
解答  
思路：在2.3.1 中，可以通过绑定流程或者模块来显示图像和渲染效果。因此，第一步，
可以使用在VM 软件平台中给图像源模块添加本地图像，或者通过图像源模块的接口来获
取本地图像（参考2.2.4）；第二步，渲染控件绑定图像源模块或者绑定流程（流程中提前
配置显示设置：订阅图像源模块）。示例代码如下：  
C#  
//使用VM 软件平台已经给图像源模块添加本地图像，再使用渲染控件绑定模
块 
ImageSourceModuleTool testImage = (ImageSourceModuleIool)VmSo
lution.Instance["流程1.图像源1"]; 
vmRenderControl.ModuleSource= testImage; 
MFC  



<!-- page 327 -->
HIKROBOT 
 
318 
 
 
 
Qt  
 
问题根因  
不熟悉如何使用渲染控件显示本地图像  
 
 



<!-- page 328 -->
HIKROBOT 
 
319 
 
 
2.3.3 渲染控件：渲染控件上自定义图形的
方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：如何在渲染控件上绘图？  
解答  
引用VMControls.WPF.dll（路径：\VisionMaster4.0.0\Development\V4.0.0\ComCon
trols\bin\x64），手动添加这个dll 后，属性的复制到本地改为false。创建所需shape
的对象，给对象属性赋值。调用VMRenderConTrol.DrawShape()函数，在控件上画出想
要的图形。注意：模块的渲染效果和自定义图形建议放在不同的线程里渲染，且如果连续
运行如果自定义图形跟不上，渲染前要加个延时。示例代码如下：  
C#  
Task.Run(()=> 
{ 
 
System.Threading.Thread.Sleep(50); 
 
This.BeginInvoke(new Action(()=> 
 
{ 



<!-- page 329 -->
HIKROBOT 
 
320 
 
 
 
 
//画线 
 
 
VMControls.WPF.LineEx line = new VMControls.WPF.Li
neEx(); 
 
 
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
 
 
VMControls.WPF.RectangleEx rect = new VMControls.
WPF.RectangleEx(); 
 
 
rect.CenterX = 1000; 
 
 
rect.CenterX = 1000; 



<!-- page 330 -->
HIKROBOT 
 
321 
 
 
 
 
rect.Width = 500; 
 
 
rect.Height = 500;                            
 
 
vmRenderControl1.DrawShape(rect); 
 
 
//画文本 
 
 
VMControls.WPF.TextEx text = new VMControls.WPF.T
extEx(); 
 
 
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
 
 
VMControls.WPF.CircleEx circle = new VMControls.WP
F.CircleEx(); 
 
 
circle.CenterX = 2000; 
 
 
circle.CenterY = 2000; 
 
 
circle.Color = nArgb; 



<!-- page 331 -->
HIKROBOT 
 
322 
 
 
 
 
circle.FillColor = nArgb; 
 
 
circle.MajorRadius = 50;//外半径和内半径不等时，则是椭
圆 
 
 
circle.MinorRadius = 50; 
 
 
circle.Opacity = 2; 
 
 
circle.StrokeThickness = 3; 
 
 
vmRenderControl1.DrawShape(circle); 
 
}),null); 
}); 
  
Qt 
//矩形框颜色颜色 
int nArgb = 0; 
nArgb += 255 << 16; 
nArgb += 0 << 8; 
nArgb += 0; 
 
RectangleEx rectangle = { 0 }; 
rectangle.CenterX = 550; 
rectangle.CenterY = 550; 



<!-- page 332 -->
HIKROBOT 
 
323 
 
 
rectangle.Width = 250; 
rectangle.Height = 200; 
rectangle.Angle = 25; 
rectangle.Opacity = 0.5; 
rectangle.SkewAngle = 0; 
rectangle.Color = nArgb; 
rectangle.FillColor = nArgb; 
rectangle.StrokeThickness = 3; 
//绘制矩形 
ui->axWidget_render->dynamicCall("SetRectangle(qlonglong)", reinter
pret_cast(&rectangle)); 
问题根因  
不熟悉如何使用渲染控件显示本地图像  
 
 



<!-- page 333 -->
HIKROBOT 
 
324 
 
 
2.3.4 参数控件：参数配置控件绑定模块的
方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：参数控件如何设定参数？  
解答 
参数配置控件的使用需要绑定相应的参数  
1）C#中  
IMVSCircleFindModuTool circleFindModule = (IMVSCircleFindModuTo
ol)VmSolution.Instance["流程1.圆查找1"]; 
//普通的参数配置控件 
vmParamsConfigControl1.ParamsConfig = circleFindModule.Params; 
//带渲染的参数配置控件 
vmParamsConfigWithRenderControl1.ModuleSource = circleFindModu
le; 
当不确定具体是哪一个模块时，使用IVmModule 类，示例如下：  



<!-- page 334 -->
HIKROBOT 
 
325 
 
 
IVmModule module = (VmModule)VmSolution.Instance[ "流程名.模块
名"]; 
vmParamsConfigWithRenderControl1.ModuleSource = module; 
2)MFC 中  
IMVSCircleFindModuTool * pCirFindObject = (IMVSCircleFindModuTo
ol *)(*m_pVmSol)["流程1.圆查找1"]; 
if (NULL == pCirFindObject) return; 
CircleFindParams * pCirFindParam = pCirFindObject->GetParamObj(); 
if (NULL == pCirFindParam) return; 
CCircleFindDlg::GetExeFilePath(); 
m_ctrlParamRender.SetParamsInfo(pCirFindParam->GetControlInfo(), m
_strFilePath.c_str()); 
3）Qt 中  
//获得指向圆查找模块的指针 
IMVSCircleFindModuTool *circleFindMou=static_cast<IMVSCircleFindM
oduTool*>((*m_pVmSol)["流程1.圆查找1"]); 
 
//获得圆查找模块的参数 



<!-- page 335 -->
HIKROBOT 
 
326 
 
 
ParamCtrlInput *param=reinterpret_cast<ParamCtrlInput*>(circleFindM
ou ->GetParamObj()); 
ParamBaseEx stParamData={0}; 
stParamData.Handle=param->Handle; 
stParamData.ModuId=param->ModuId; 
stParamData.TimeOut=0; 
 
//绑定参数渲染控件 
ui->axWidget_3->dynamicCall("SetParamsInfo(qlonglong)",reinterpret_
cast<qlonglong>(&stParamData)); 
 
问题根因  
不熟悉参数配置控件的使用 
 
 



<!-- page 336 -->
HIKROBOT 
 
327 
 
 
2.3.5 控件颜色：控件颜色修改的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：简易修改VM 控件的颜色？  
解答  
对二次开发中嵌入控件的颜色进行修改，具体代码如下：  
C#  
string colorinfo = "ColorStyle3"; 
AppColorService.CurColorDefine = colorinfo; 
“ColorStyle3”文件在VM 安装路径的ColorStyle 文件夹下面，其中内容如下图所示，
客户可以自行编辑XAML 文件，修改自己想要控件的颜色即可生效  



<!-- page 337 -->
HIKROBOT 
 
328 
 
 
 
默认控件颜色：  



<!-- page 338 -->
HIKROBOT 
 
329 
 
 
 
修改后控件颜色：  



<!-- page 339 -->
HIKROBOT 
 
330 
 
 
 
问题根因  
不了解VM 控件颜色可以改变。  
 
 



<!-- page 340 -->
HIKROBOT 
 
331 
 
 
2.3.6 VM 嵌入：嵌入用户软件界面的方法
  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：将VM 整体嵌入到客户软件界面中？  
解答  
将VM 软件整体嵌入到客户软件中，需要利用Panel 控件，并且需要先启动VM 软件，具
体代码如下：  
C#  
[DllImport("User32.dll", EntryPoint = "SetParent")] 
public static extern int SetParent(IntPtr hWndChild, IntPtr hWndNew
Parent); 
 
[DllImport("user32.dll", CharSet = CharSet.Auto)] 
public static extern int MoveWindow(IntPtr hWnd, int x, int y, int n
Width, int nHeight, bool BRePaint); 
 



<!-- page 341 -->
HIKROBOT 
 
332 
 
 
// Start the process 
  p = System.Diagnostics.Process.Start 
(@"D: \VisionMaster4.0.0\Applications\VisionMaster.exe"); 
// Wait for process to be created and enter idle condition 
  p.WaitForInputIdle(); 
// Get the main handle 
appWin = p.MainWindowHandle; 
//需要等待p 启动，可自行判断，可加上Thread.Sleep(10000);             
SetParent(appWin, panel1.Handle);//this 在这里是Panel 控件 
MoveWindow(appWin, 0, 0, this.panel1.Width, this.panel1.Height, tru
e); 
最终效果如下图所示，VM 就整体嵌入到客户软件的Panel 空间中，并且可以保持VM 所
具备的功能  
 



<!-- page 342 -->
HIKROBOT 
 
333 
 
 
问题根因  
不了解Panel 控件用法，如何嵌入第三方程序。  
 
 



<!-- page 343 -->
HIKROBOT 
 
334 
 
 
2.3.7 参数控件：隐藏参数设置控件上某些
参数的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何隐藏参数设置控件上的某些参数？  
解答  
   可以通过修改VM 配置文件，来决定参数设置控件上某些参数的隐藏与否。这里以隐藏
圆查找模块的运行参数中的卡尺数量为例。步骤如下：  
1 隐藏之前，绑定圆查找模块的参数控件上运行参数如下：  



<!-- page 344 -->
HIKROBOT 
 
335 
 
 
 
2 在二次开发程序中找到圆查找模块的配置路径\VMTest\VMTest \bin\Debug\Module
(sp)\x64\Location\IMVSCircleFindModu 路径下找到IMVSCircleFindModuAlgorithm
Tab.xml 配置文件，双击打开配置文件。  
 
3 找到运行参数中卡尺数量的位置处，找到属性<Visibility>Beginner</Visibility>，  



<!-- page 345 -->
HIKROBOT 
 
336 
 
 
 
4 将<Visibility>Beginner</Visibility>修改为<CustomVisible> False </CustomVisi 
ble> 
 
5 隐藏之后的绑定圆查找模块的参数控件的运行参数如下：  



<!-- page 346 -->
HIKROBOT 
 
337 
 
 
 
同理：VM 中隐藏模块的某些参数，同样是打开模块的xml 文件，在VM 安装路径中，V
M4.0.0\VisionMaster4.0.0\Applications\Module(sp)\x64\Location\IMVS 
CircleFindModu 路径下找到IMVSCircleFindModuAlgorithmTab.xml 配置文件  
问题根因  
不熟悉配置文件修改方式。  
 
 



<!-- page 347 -->
HIKROBOT 
 
338 
 
 
2.3.8 渲染控件：通过鼠标点击获取渲染控
件像素坐标的方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何通过鼠标事件获取渲染控件上的图像坐标？  
解答  
通过鼠标事件获取渲染控件指定位置图像坐标，示例代码如下。  
C# 
// 注册鼠标点击事件 
public OneWindowUserControl(MainWindow mainWindow) 
{ 
    InitializeComponent(); 
    RenderImage1.OnMouseLeftButtonDownPixelChanged += RenderI
mage_OnMouseLeftButtonDownPixelChanged1; 
} 
 
// 获取锚点事件 



<!-- page 348 -->
HIKROBOT 
 
339 
 
 
private void RenderImage_OnMouseLeftButtonDownPixelChanged1(int
 x, int y) 
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
问题根因  
不熟悉控件事件。  
 
 



<!-- page 349 -->
HIKROBOT 
 
340 
 
 
2.3.9 控件显示：控件显示所加载的流程的方法  
描述  
环境：VM4.0 + VS2015 及以上  
问题：基于对话框的MFC程序，在主窗口放置了一个VmMainView控件，程序初始化时可
以显示，但是加载方案完成时，不会显示已经加载的流程，如下图所示：  
 
解答  
使用了带有流程显示的控件，如VmMainView 控件，需要在控件的初始化代码GetObjec
tPointer( )之前，调用一次CreateSolutionInstance( ),这样流程加载完成的时候，VmM
ainView 控件就能显示加载的流程了。所以：关键代码如下：  



<!-- page 350 -->
HIKROBOT 
 
341 
 
 
 
CreateSolutionInstance(); 
mainViewControl.GetObjectPointer(); 
问题根因  
CreateSolutionInstance( )需要在控件初始化时调用一次，用来提前绑定VmMainView
控件关联的方案。  
 
 



<!-- page 351 -->
HIKROBOT 
 
342 
 
 
2.3.10 前端界面控件：前端界面控件大小
自适应的方法  
描述  
环境：VM4.0 + VS2015 及以上  
现象：WinForm 中使用前端界面控件，设置Anchor/Dock 属性后控件内的元素不随界面
放缩，如何实现前端界面大小自适应？  
解答  
1. 首先需要在界面上拖拽vmFrontendControl 控件（该控件专门用于显示VM 方案的前
端界面）并设置好Anchor/Dock 属性。  
2.方案加载完成后加载前端界面资源，代码如下。  
 
C# 
private void button16_Click(object sender, EventArgs e) 
{ 
    vmFrontendControl.LoadFrontendSource(); 
} 



<!-- page 352 -->
HIKROBOT 
 
343 
 
 
3.给控件添加大小变化事件，在前端控件大小改变时调用控件的AutoChangeSize 接口。
  
 
C# 
private void vmFrontendControl_SizeChanged(object sender, EventArg
s e) 
{ 
    vmFrontendControl.AutoChangeSize(); 
} 
4.显示效果  
 
问题根因  



<!-- page 353 -->
HIKROBOT 
 
344 
 
 
不熟悉控件内容放缩接口的调用时机。  
 
 



<!-- page 354 -->
HIKROBOT 
 
345 
 
 
2.3.11 渲染控件：渲染控件存图的方法  
描述  
环境：VM4.0 + VS2015 及以上  
现象：常见的存图方法有输出图像模块以及渲染控件存图，渲染控件存图的方法如何实
现？  
解答  
渲染控件存图代码如下所示，但推荐使用输出图像模块进行存图。因为渲染时机是在回调
结束之后的，所以在回调函数中进行渲染控件存图，保存的图片会是未完成渲染的。在Ru
n 接口之后直接使用渲染控件存图也会是渲染控件上无图或者未渲染完成。在button 事
件中进行渲染控件存图，才能正常存图。  
 
C# 
vmRenderControl1.SaveOriginalImage("E:\\VSVM4.2\\VMTestB\\origina
l.bmp"); 
vmRenderControl1.SaveRenderedImage("E:\\VSVM4.2\\VMTestB\\Rend
erImage.bmp"); 
问题根因  



<!-- page 355 -->
HIKROBOT 
 
346 
 
 
不熟悉渲染控件存图接口  
2.4 结果获取类 
2.4.1 数据结果：通过流程输出或模块输出
获取数据结果的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：方案或流程运行执行之后，就可以获取结果（建议将结果获取写在回调函数里），
可以通过获取渲染结果和数据结果，渲染结果通过绑定渲染控件进行显示，数据结果分为
整型、浮点型、字符串型和图像型等等，VM 二次开发如何获取数据结果？ 
解答  
数据结果的获取可以通过流程的输出或者模块的输出，推荐使用通过流程的输出，符合高
内聚低耦合的思想，详细介绍如下所示：  
1 通过流程的输出获取数据结果  
1.1 流程配置-输出设置  



<!-- page 356 -->
HIKROBOT 
 
347 
 
 
 
1.2 获取整型、浮点型、字符串型数据  
C# 
VmProcedure vmprocess = (VmProcedure)VmSolution.Instance["流程1
"]; 
string str = vmprocess.GetIntOutputResult("out").pIntValue[0].ToString
();                 
string str1 = vmprocess.GetFloatOutputResult("out0").pFloatValue[0].T
oString(); 
string str2 = vmprocess.GetStringOutputResult("out1").astStringValue
[0].strValue; 
 
C# 
// 流程拿结果，c 从界面层获取的方法，适用于高内存场景 



<!-- page 357 -->
HIKROBOT 
 
348 
 
 
string str2 = ((ImvsSdkDefine.IMVS_MODULE_STRING_VALUE_EX)(vmP
rocess["out1.Value"] as Array).GetValue(0)).strValue.ToString();//字符串
型结果 
string str1 = ((vmProcess["out0.Value"] as Array).GetValue(0)).ToString
();//浮点型结果 
1.3 获取图像数据  
流程输出设置中输出IMAGE 类型的图像数据，不能通过前面参数名称image 拿取，需要
通过Imageout0，ImageWidthout0，ImageHeightout0,ImagePixelFormatout0，这
四个参数进行获取。示例代码和图像如下：  
 
C# 
VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程
1"];//实例化流程1 



<!-- page 358 -->
HIKROBOT 
 
349 
 
 
ImageResultInfo resultInfo0 =VmProcess.GetImageOutputResult("Imag
eout0"); 
IntResultInfo resultInfo1 =VmProcess.GetIntOutputResult("ImageWidth
out0"); 
IntResultInfo resultInfo2 =VmProcess.GetIntOutputResult("ImageHeigh
tout0"); 
IntResultInfo resultInfo3 =VmProcess.GetIntOutputResult("ImagePixelF
ormatout0"); 
byte[] imageData=resultInfo0.pstImageValue[0].pData; 
2 通过模块的输出获取数据结果  
2.1 获取模块的浮点型数据  
C# 
IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool=(IMVSCircl
eFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆
查找1"]; 
//只调用一次circleTool.ModuResult 表示只从底层拿一次结果，适用于高内
存场景 
var circleToolResult = circleTool.ModuResult; 
string circleX = circleToolResult.OutputCircle.CenterPoint.X.ToString(); 
string circleY = circleToolResult.OutputCircle.CenterPoint.Y.ToString(); 



<!-- page 359 -->
HIKROBOT 
 
350 
 
 
string circleR = circleToolResult.OutputCircle.Radius.ToString(); 
2.2 获取图像数据，针对有图像输出的模块  
C# 
//图像源模块 
Using ImageSourceModuleCs; 
ImageSourceModuleTool sourceImage=(ImageSourceModuleTool)VmS
olution.Instance[“流程1.图像源1”];//实例化输出图形模块 
Var sourceImageResult=sourceIamge.ModuResult.ImageData;//只需要
调用一次ModuResult,适用于高内存场景 
byte[] imageData= sourceImageResult.ImageData; 
int imagePixelformat= sourceImageResult.Pixelformat; 
 
C# 
//输出图像模块 
Using SaveImageCs; 
SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance[“流
程1.输出图像1”];//实例化输出图像模块 
Var saveImageResult=saveIamge.ModuResult.OutputImage;//只需要调
用一次ModuResult,适用于高内存场景 
byte[] imageData= saveImageResult.ImageData; 



<!-- page 360 -->
HIKROBOT 
 
351 
 
 
int imagePixelformat= saveImageResult.Pixelformat; 
像素格式17301505 为MONO8 灰度图，像素格式 35127316 为RGB24 彩色图，需要
注意的是输出图像模块的像素格式默认是RGB24，所以此时的输出图像模块的imagePix
elformat 为35127316。  
 
问题根因  
不熟悉如何获取数据结果  
 
 



<!-- page 361 -->
HIKROBOT 
 
352 
 
 
2.4.2 流程运行：所有流程运行结束的回调
方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象： 流程运行的触发方式有多种，无论哪种方式都可以进入回调函数，因此建议在回
调函数中获取结果。  
解答 
1）流程运行的触发方式  
 
2）所有流程运行结束的都会进入的回调函数，建议在回调函数里获取数据结果（参考2.4.
1）和渲染结果（2.3.1），其中在回调函数里获取渲染结果时，需要使用委托(this.BeginI
nvoke)对控件进行绑定操作。  
C# 
  



<!-- page 362 -->
HIKROBOT 
 
353 
 
 
public Form1() 
{ 
 
InitializeComponent(); 
 
//注册回调函数，流程运行状态回调 
    VmSolution.OnWorkStatusEvent += VmSolution_OnWorkStatusEve
nt; 
} 
private void VmSolution_OnWorkStatusEvent(ImvsSdkDefine.IMVS_MO
DULE_WORK_STAUS workStatusInfo) 
{ 
 
if (workStatusInfo.nWorkStatus == 0 && workStatusInfo.nPro
cessID == 10000)//为0 表示执行完毕，为1 表示正在执行；10000 表示流
程1 
 
{ 
      //获取结果 
 
} 
} 
 
C++ 
//类中声明变量和函数 
IVmSolution* m_pVmSol; 



<!-- page 363 -->
HIKROBOT 
 
354 
 
 
IVmProcedure* m_pVmPrc; 
static int __stdcall SolutionCallback(IN OutputPlatformInfo * const pst
InputPlatformInfo, IN void * const pUser); 
int SolutionCallbackFunc(IN OutputPlatformInfo * const pstInputPlatf
ormInfo); 
 
//在初始化时用方案注册回调函数，这是所有流程运行结束都会自动进的回调
函数 
m_pVmSol->RegisterCallBack(SolutionCallback, this); 
 
//回调函数的实现方法,Demo 为项目类名 
int __stdcall Demo::SolutionCallback(IN OutputPlatformInfo * const ps
tInputPlatformInfo, IN void * const pUser) 
{ 
 
auto *pCtrlDemoThis = static_cast<Demo*>(pUser); 
 
int nRet = IMVS_EC_UNKNOWN; 
 
if (pCtrlDemoThis) 
 
{ 
 
 
nRet = pCtrlDemoThis->SolutionCallbackFunc(pstInput
PlatformInfo); 
 
 
if (IMVS_EC_OK != nRet) 



<!-- page 364 -->
HIKROBOT 
 
355 
 
 
 
 
{ 
 
 
 
return nRet; 
 
 
} 
 
} 
 
return IMVS_EC_OK; 
} 
int Demo::SolutionCallbackFunc(IN OutputPlatformInfo * const pstInp
utPlatformInfo) 
{ 
 
if (pstInputPlatformInfo->nInfoType == IMVS_ENUM_CTRLC_O
UTPUT_PLATFORM_INFO_WORK_STATE) 
 
{ 
 
 
try { 
 
 
 
auto workstateInfo = static_cast<IMVS_PF_MO
DULE_WORK_STAUS*>(pstInputPlatformInfo->pData); 
 
 
 
if (workstateInfo->nWorkStatus == 0 && wor
kstateInfo->nProcessID == 10000)//判断流程执行状态和流程ID 
 
 
 
{ 
 
 
 
 
auto m_pVmPro = (IVmProcedure*)(*
m_pVmSol)["流程1"]; 



<!-- page 365 -->
HIKROBOT 
 
356 
 
 
 
 
 
 
float info = m_pVmPro->GetResult()->
GetOutputFloat("out").pFloatVal[0]; 
 
 
 
} 
 
 
} 
 
 
catch (exception *e) 
 
 
{ 
 
 
 
TRACE(e->what()); 
 
 
} 
 
} 
 
return 0; 
} 
 
问题根因  
不熟悉流程运行结束的回调函数 
 
 



<!-- page 366 -->
HIKROBOT 
 
357 
 
 
2.4.3 模块回调：所有模块运行结束的回调
方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：模块运行结束就会进入的回调函数  
解答 
所有模块运行结束就会进入的回调函数，代码如下：  
C# 
  
//注册回调函数 
VmSolution.OnModuleResultCallbackEvent += VmSolution_OnModule
ResultCallbackEvent; 
private void VmSolution_OnModuleResultCallbackEvent (ImvsSdkDefin
e.IMVS_MODULE_RESULT_INFO_LIST_EX_Data moduleResultExInfo) 
{ 
 
if (moduleResultExInfo.nModuleID == moduleID )//判断模块Id 
 
{ 



<!-- page 367 -->
HIKROBOT 
 
358 
 
 
 
 
if (moduleResultExInfo.nStatus == 1)//判断模块状态，1
表示模块运行成功 
 
 
{ 
 
 
 
//获取结果 
 
 
} 
 
} 
} 
问题根因  
不熟悉所有模块运行结束的回调  
 
 



<!-- page 368 -->
HIKROBOT 
 
359 
 
 
2.4.4 加密狗回调：获取加密狗状态的回调
方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：如何获取加密狗编号？  
解答 
建立ServerSDKManager.serverSDKManager.mSolutionManager.OnDongleCallBack
事件，对事件中的moduleInfo 进行处理。moduleInfo.nDongleStatus = 0 代表加密狗
状态正常，moduleInfo.strDongleType 为加密狗编号。  
 
C# 
 
ServerSDKManager.serverSDKManager.mSolutionManager.OnDongleCa
llBack += MSolutionManager_OnDongleCallBack; 
private void MSolutionManager_OnDongleCallBack(ImvsSdkDefine.IMV
S_DONGLE_INFO moduleInfo) 
{ 



<!-- page 369 -->
HIKROBOT 
 
360 
 
 
    if(moduleInfo.nDongleStatus == 0)//获取加密狗状态 
    { 
       string dogNum = System.Text.Encoding.Default.GetString(mod
uleInfo.strDongleType);//获取加密狗型号 
    } 
 
else 
 
{ 
     
MessageBox.Show("未检测到加密狗！"); 
 
} 
} 
问题根因  
不熟悉如何获取加密狗编号，从而判断是否插了加密狗  
 
 



<!-- page 370 -->
HIKROBOT 
 
361 
 
 
2.4.5 方案加载：方案加载结束的回调方法
  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：方案加载结束进入的回调函数。 
解答 
首先，建立VmSolution.OnSolutionLoadEndEvent（方案加载结束）事件，对事件中的
solutionLoadEndInfo 进行判断，对方案的nStatus 进行判定，其中0 表示方案为空闲状
态，可在其中获得方案加载结果，1 表示方案处于忙碌状态。  
C# 
  
VmSolution.OnSolutionLoadEndEvent += VmSolution_OnSolutionLoad
EndEvent; 
//方案加载成功 
  
private void VmSolution_OnSolutionLoadEndEvent 



<!-- page 371 -->
HIKROBOT 
 
362 
 
 
(ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO solutionLoadEndInf
o) 
{ 
    if (solutionLoadEndInfo.nStatus == 0)//0 为方案加载成功 
    { 
       //这里可以插入相关函数 
    }   
} 
提示：当方案中包含脚本模块或者深度学习模块，方案第一次执行耗时就会比较长，因此
可以在方案加载成功后，静默执行一次，即在会回调函数里写静默执行语句：VmSolutio
n.Instance.SilentExecute(true)。  
问题根因  
不熟悉方案加载结束的回调 
 
 



<!-- page 372 -->
HIKROBOT 
 
363 
 
 
2.4.6 模块回调：指定模块运行结束的回调
方法  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：指定模块，在运行结束后进入回调函数。 
解答 
1）注册回调函数，模块被执行一次就会进该函数一次。  
C# 
  
IVmModule module = (IMVSCircleFindModuTool)VmSolution.Instance
["流程1.圆查找1"]; 
module.ModuleResultCallBackArrived += ModuleResultCallBackArrive
d; 
2）回调函数，目前模块回调函数不是事件，因此无法快捷键自动补全代码，函
数如下：  
C# 



<!-- page 373 -->
HIKROBOT 
 
364 
 
 
private void ModuleResultCallBackArrived(object sender ,EventArgs e) 
{ 
   IMVSCircleFindModuTool circleFind = (IMVSCircleFindModuTool)se
nder; 
   float x = circleFind.ModuResult.OutputCircle.Radius; 
} 
问题根因  
不熟悉指定模块运行结束的回调 
 
 



<!-- page 374 -->
HIKROBOT 
 
365 
 
 
2.4.7 模块回调：禁用模块结果回调的方法
  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：为了提高内存利用率，禁用不必要的模块结果回调。  
解答 
禁用和启用模块结果回调，禁用之后将无法获取模块的结果，代码如下：  
C# 
  
//禁用所有模块的回调 
VmSolution.Instance.DisableModulesCallback(); 
//控制方案中回调，ID 指模块ID，0 是禁用，1 是启用 
ServerSDKManager.serverSDKManager.mModuleManager.CtrlCallBack
ModuResult(ID,0); 
//启用所有回调 
VmSolution.Instance.EnableModulesCallback(); 
问题根因  



<!-- page 375 -->
HIKROBOT 
 
366 
 
 
不熟悉相关接口的使用。  
2.4.8 通讯回调：通讯设备状态和接收数据
的回调方法  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何获取通讯设备的状态是开启还是关闭？如何获取通讯数据？  
解答  
1. 获取通讯设备的状态  
 
C# 
//注册回调 
VmSolution.OnCommunicationStatusCallBackEvent += VmSolution_On
CommunicationStatusCallBackEvent; 
 
private void VmSolution_OnCommunicationStatusCallBackEvent(ImvsS
dkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo) 
{ 



<!-- page 376 -->
HIKROBOT 
 
367 
 
 
    int nType = reportDataInfo.nType; 
    byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pDat
a, reportDataInfo.nLen); 
    int len = btarr.Length; 
    string ID = btarr[1].ToString();//通讯设备ID 
    string Open = btarr[0].ToString();//开关状态，1 表示开，0 表示关 
} 
2. 获取通讯数据  
 
C# 
//注册回调 
VmSolution.OnCommunicationRecvCallBackEvent += VmSolution_OnC
ommunicationRecvCallBackEvent; 
private void VmSolution_OnCommunicationRecvCallBackEvent(ImvsSd
kDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo) 
{ 
    string strMsg; 
    try 
    { 
        int nType = reportDataInfo.nType; 



<!-- page 377 -->
HIKROBOT 
 
368 
 
 
 
        byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.p
Data, reportDataInfo.nLen); 
        int len = btarr.Length; 
        string ID = btarr[0].ToString(); 
        byte[] vs = new byte[len - 2]; 
        Array.Copy(btarr, 2, vs, 0, len - 2); 
        string ReceiveData = System.Text.Encoding.Default.GetString
(vs); 
        strMsg = ID + "号设备接受到：" + ReceiveData; 
        Logger.WriteLog(LogLevel.INFO, strMsg); 
    } 
    catch (VmException ex) 
    { 
        strMsg = "读取通信数据失败. Error Code: " + Convert.ToString
(ex.errorCode, 16); 
        Logger.WriteLog(LogLevel.ERROR, strMsg); 
        return; 
    } 
} 
 



<!-- page 378 -->
HIKROBOT 
 
369 
 
 
问题根因  
不熟悉通讯相关的回调方法  
 
 



<!-- page 379 -->
HIKROBOT 
 
370 
 
 
2.5 全局工具 
2.5.1 全局相机：全局相机设置参数的方法 
描述 
环境：VM4.0.0 + VS2015 及以上  
现象：全局相机一些参数如何设置或获取？ 
解答  
1）全局相机连接状态的获取方法只有在图像源绑定相机里面全局相机才可获取绑定该相机
的状态，获取全局相机中相机的连接状态是Open 还是Close，监测相机是否掉线。获取绑
定该相机图像源的"CameraName"参数的Value，会获取类似"0$0$$$$Close"的数据，对
此数据按$分割获取第一个数据，第一个值大于0 表示连接，等于0 表示未连接，如上数据
表示该相机未连接。  



<!-- page 380 -->
HIKROBOT 
 
371 
 
 
 
C# 
  
ImageSourceModuleTool imageSourceModule = (ImageSourceModule
Tool)VmSolution.Instance["流程1.图像源1"]; 
tring i = null; 
imageSourceModule.ModuParams.GetParamValue("CameraName", ref 
i); 
2）全局相机触发源的获取和设置方法，触发源枚举值为枚举值就是 0 是LINE0, 1 是LI
NE1,2 是LINE2,3 是LINE3, 7 是SOFTWARE。  
C# 



<!-- page 381 -->
HIKROBOT 
 
372 
 
 
GlobalCameraModuleTool globalTool = VmSolution.Instance["全局相机
1"] as GlobalCameraModuleTool; 
//获取 
string strVal11 = ""; 
globalTool.ModuParams.GetParamValue("TriggerSource", ref strVal11); 
//设置 
globalTool.ModuParams.SetParamValue("TriggerSource", "7"); 
3）全局相机设置曝光的方法  
C# 
GlobalCameraModuleTool tool = (GlobalCameraModuleTool)VmSoluti
on.Instance["全局相机1"]; 
//获取 
string strValue = ""; 
tool.ModuParams.GetParamValue("ExposureTime", ref strValue); 
//设置 
tool.ModuParams.SetParamValue("ExposureTime", "5000"); 
问题根因  
不熟悉全局相机的一些参数配置  



<!-- page 382 -->
HIKROBOT 
 
373 
 
 
 
 



<!-- page 383 -->
HIKROBOT 
 
374 
 
 
2.5.2 全局相机：获取全局相机列表的方法
  
描述  
环境：VM4.0.0 + VS2015 及以上  
现象：如何获取全局相机列表并给图像源设置指定相机？  
解答  
1.获取全局相机列表，示例代码如下。  
C# 
// 全局相机下拉列表 
private void vmGalobalCameraCombBox_DropDownOpened(object se
nder, EventArgs e) 
{ 
    try 
    { 
        var moduleList = ServerSDKManager.serverSDKManager.mSol
utionManager.GetAllModuleList(); 
 



<!-- page 384 -->
HIKROBOT 
 
375 
 
 
        vmGalobalCameraCombBox.Items.Clear(); 
        if (moduleList.HasValue) 
        { 
            foreach (var item in moduleList.Value.astModuleInfo) 
            { 
                if (item.nModuleType == 6) 
                { 
                    string str = Encoding.UTF8.GetString(item.strDispl
ayName); 
                    vmGalobalCameraCombBox.Items.Add(item.nNode
ID.ToString() + " " + str); 
                } 
            } 
        } 
    } 
    catch (VmException ex) 
    { 
        System.Windows.MessageBox.Show("获取相机列表失败！" + ex.
ToString()); 
    } 
} 



<!-- page 385 -->
HIKROBOT 
 
376 
 
 
2.图像源模块设置相机，代码如下。  
C# 
// 图像源绑定相机 
private void BindingCamera_Click_1(object sender, RoutedEventArgs 
e) 
{ 
    try 
    { 
        var imageSourceModuleTool = (ImageSourceModuleTool)Vm
Solution.Instance["流程1.图像源1"]; 
        imageSourceModuleTool.ModuParams.SetParamValue("Camera
ID",”1”); 
        System.Windows.MessageBox.Show("绑定成功！"); 
    } 
    catch (Exception ex) 
    { 
        System.Windows.MessageBox.Show("绑定失败！"); 
    } 
} 
问题根因  



<!-- page 386 -->
HIKROBOT 
 
377 
 
 
相关接口没有对外开放，后续版本（VM4.2）会开放出来。  
2.5.3 全局通信：通信管理中设备开启状态
管理  
描述 
环境：VM4.0.0 + VS2015 及以上 
现象：通信管理中设备开启状态和如何通过代码设置，如何通过回调获取开启状态。 
 
解答 


