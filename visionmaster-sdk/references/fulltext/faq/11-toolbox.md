# 专题·宝藏工具合集（问题采集助手/定位精度评估/服务管家）
<!-- pdf pages 1401-1414 -->

<!-- page 1401 -->
HIKROBOT 
 
1392 
 
 
5 宝藏工具合集 
5.1 VM 问题采集助手：VM 应用和开发问
题排查及异常收集工具 
1. 软件说明 
VM 问题采集助手集多项功能于一体，目的是帮助客户快速定位和修复环境类问题，降
低在非代码类、功能性问题上的沟通成本，提高问题排查效率。 
首先检测VM 安装环境或VM SDK 开发环境是否正常，软件提供一键修复功能。然后，
若修复环境后，仍然不能解决问题或定位问题具体原因，则利用软件调整日志等级（一般调
整为Debug 等级），软件运行时底层将打印更详细的日志信息。最后，利用软件日志收集
功能，获取系统和软件版本信息、VM 日志、算子日志和dump 文件等研发排查问题所需
文件的压缩包。 
用户将日志压缩文件、问题现象和出现问题的时间点及时反馈给研发，以防日志发生覆
盖。 
适用VM 版本：VM4.0 及以上； 
其中日志调整功能适用版本：VM4.2 及以上。 
针对VM4.0-VM4.2，下载链接：https://drive.ticklink.com/hcs/controller/hik-man
age/fileDownload?link=ZcKDXpwK。 
针对VM4.3，获取方式如图所示： 



<!-- page 1402 -->
HIKROBOT 
 
1393 
 
 
 
2. VM 环境检测 
 
检测VM 版本，VM 系统环境变量，用户权限，python 版本，加密驱动，相机驱动，
软件运行依赖库，算子版本等等。 



<!-- page 1403 -->
HIKROBOT 
 
1394 
 
 
 
3. SDK 引用 
 
此处给出VM SDK 程序报错的排查步骤。安装VM 补丁后，建议点击按钮【确认更
新】，等待更新之后的弹出提示。 



<!-- page 1404 -->
HIKROBOT 
 
1395 
 
 
 
4. 日志调整 
当无法定位问题原因时，需要调整日志等级（一般调整到Debug 级别），收集更详细
的日志信息。当前版本只适用于自动调整VM4.2 及以上版本日志等级，其它版本需手动增
加文件。 
 
 
切换等级完成的是在指定文件夹下增加相应的文件（也可以根据下面描述手动增加文件，



<!-- page 1405 -->
HIKROBOT 
 
1396 
 
 
新建一个txt，根据下面描述命名，然后去掉后缀），例如将日志等级调整到Debug 级别（级
别简写：i，t，d，e）。还原等级则是删除所增加的文件。 
针对VM4.2： 
\Applications 路径下增加文件：sdk_log_d； 
\Applications\Server 路径下增加文件：server_log_d； 
\Applications\VmModuleProxy\x64 路径下增加：proxy_log_d，vmframe_log_d，mo
dule_log_d。 
针对VM4.2 SDK： 
项目exe 生成路径下增加文件：sdk_log_d；所以需要在上一步中输入项目exe 生成路径。 
针对VM4.3 和VM4.3 SDK： 
\Applications 路径下增加文件：sdk_log_d； 
\Applications\Server 路径下增加文件：server_log_d； 
\Applications\VmModuleProxy\x64 路径下增加：proxy_log_d，vmframe_log_d，mo
dule_log_d。 
针对VM4.0 和VM4.0 SDK：需要手动增加文件来达到调整日志文件效果，复现问题后，
需要手动删除所增加的文件。 
VM SDK：在VisionMaster.exe 或目EXE 生成路径的同级目录，新建一个文件夹，重命名
为sdk_debug（日志等级调整为debug）或sdk_trace（日志调整为最低等trace）；  
Server：在VM 安装目录\Applications\Server 中建一个文件夹，重命名为server_log_d
（日志等级调整为debug）或server_log_t（日志等级调整为最低等trace）；  
模块框架：在VM 安装目录\Applications\VmModuleProxy\x64 中建一个文件，重命名



<!-- page 1406 -->
HIKROBOT 
 
1397 
 
 
为vmframe_log_d（日志等级调整为debug）或vmframe_log_t（日志等级调整为最低
等trace）。 
5. 日志收集 
 
VM 应用问题，则勾选VM 应用问题日志； 
VM SDK 问题，则勾选VM SDK 问题日志，项目exe 生成路径可以根据提示选择文件夹
路径。 
勾选VMSDK 问题日志时，会默认同时收集VM 日志和项目exe 生成路径下的日志。根据
下面描述，也可以根据路径手动收集日志。比如，算法SDK 开发问题，则只需要手动收集
算子日志即可，其中算子版本可以查看C:\Program Files (x86)\MVDAlgorithmSDK\Re
ferencedAssemblies\Algorithms 中MVD_Algorithm.Net.dll 的属性-详细信息页-产品
版本。 
VM 应用问题，需要收集的信息： 



<!-- page 1407 -->
HIKROBOT 
 
1398 
 
 
（1）VM 版本：VisionMaster\\Applications 路径下VersionInfo.config； 
（2）VM 日志：VisionMaster\\Applications 路径下log 文件夹； 
（3）VM Dump 文件：VisionMaster\\Applications 路径下所有文件中的后缀为dmp 的
文件，包含Application 及Application 所有的文件夹中； 
（4）算子日志：C:\\Windows\\Temp 路径下MVDSDKLog 文件夹； 
（5）系统信息：此工具自动收集到BaseInfo.txt 中； 
（6）系统日志：此工具自动收集到SystemEventLog.txt 中。 
VM SDK 问题，需要收集的信息： 
（1）VM 版本：VisionMaster\\Applications 路径下VersionInfo.config； 
（2）VM 日志：VisionMaster\\Applications 路径下log 文件夹； 
（3）VM Dump 文件：VisionMaster\\Applications 路径下所有的后缀为dmp 的文件，
包含Application 及Application 所有的文件夹中； 
（4）算子日志：C:\\Windows\T\emp 路径下MVDSDKLog 文件夹； 
（5）系统信息：此工具自动收集到BaseInfo.txt 中； 
（6）系统日志：此工具自动收集到SystemEventLog.txt 中。 
（7）VMSDK 日志：项目exe 生成路径同级目录下的log 文件夹和dump 文件，此工具将
全部收集到Development 文件夹中。 
 
 



<!-- page 1408 -->
HIKROBOT 
 
1399 
 
 
5.2 定位精度评估助手：定位精度评估及误
差分析工具 
1. 软件说明 
该软件用于视觉定位应用项目前期的精度评估及实施阶段的误差排查。 
下载链接：https://drive.ticklink.com/hcs/controller/hik-manage/fileDownload?li
nk=ZcKDXpwK 
2. 功能说明 
2.1 精度评估 
该页面主要用于评估视觉定位系统的各部分精度及整体精度。  
 
具体操作步骤如下： 
1) 加载标定文件，平移旋转标定文件/框架标定文件（.xml/.iwcal 格式）； 
2) 查看标定文件检查结果，初步确定旋转一致性及手性一致性是否正常； 
3) 做相机静态测试，验证相机及图像算法的精度（初始值为参考值，以实际测试为准）； 



<!-- page 1409 -->
HIKROBOT 
 
1400 
 
 
4) 做机构动态测试，验证机构精度； 
5) 做机构旋转测试，验证机构旋转精度； 
6) 进行机构示教，填写示教引入误差； 
7) 点击“开始评估”，评估系统所能达到的最终精度。 
精度评估结果以物理值和像素值的参考范围给出，演示效果如下图所示。 
 
2.2 问题查找页面 
根据精度评估界面结果进行误差排查优化，哪方面误差大可根据检测项优先优化。 



<!-- page 1410 -->
HIKROBOT 
 
1401 
 
 
 
1） 选择偏差范围，是小偏差还是大偏差； 
2） 选择定位引导场景； 
3） 按步骤进行误差排查； 
4） 根据提示操作排查优化，完成项目可标记记录。 
将所有项目检测完毕，视觉定位精度应能达到要求。 
 



<!-- page 1411 -->
HIKROBOT 
 
1402 
 
 
5.3 VM 服务管家：VM 常见问题智能应答
小程序 
1. 软件说明 
VM 服务管家是一款提供常见问题问答的微信小程序，24 小时值守。 
获取方法：在微信中搜索小程序VM 服务管家。 
2. 功能说明 
2.1 问答页面 
在微信中打开VM 服务管家小程序，直接根据问题所属类别输入相应的序号，最终打
开答案所指链接页面。 



<!-- page 1412 -->
HIKROBOT 
 
1403 
 
 
 
2.2 资料页面 
除了问答功能，还可以在资料页面获取VM 生态提供的全面的学习资料。 



<!-- page 1413 -->
HIKROBOT 
 
1404 
 
 
 
其中，资料荟萃中包含资料如图所示，下载链接：https://drive.hikvision.com/hcs/contr
oller/hik-manage/fileDownload?link=lNgmEJx1&。 



<!-- page 1414 -->
HIKROBOT 
 
1405 
 
 
 
