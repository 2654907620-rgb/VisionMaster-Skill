<!-- src:_xE7_x8E_xAF_xE5_xA2_x83_xE6_xA3_x80_xE6_xB5_x8B_xE5_xB7_xA5_xE5_x85_xB7.html -->
<!-- path:工具 > 环境检测工具 -->
# 环境检测工具

VisionMaster软件安装完成后，在二次开发的过程可能遇到一些典型性问题，例如：由于环境变量未生效导致未找到iMVS-6000PlatformSDK.dll，或者找到错误版本的iMVS-6000PlatformSDK.dll。
为了解决以上问题，建议使用环境检测工具，工具名称为：**VMCollector.exe**，所在路径为：..\Applications\Tools\VMCollector。

环境检测工具主要检测如下内容：

* **VisionMaster检测**
  1. 获取当前默认的VisionMaster版本：

     通过获取注册表SOFTWARE\WOW6432Node\Microsoft.NETFramework\v4.0.30319\AssemblyFoldersEx\VisionMaster的数值所包含的版本信息。该版本的语言类型通过LanguageSet.cfg文件读取获得。
  2. 获取当前运行的VisionMaster版本：

     通过获取进程中的VisionMaster程序，得到程序启动路径，然后将路径和所有版本中的信息进行对比得到当前运行版本号。该版本的语言类型通过LanguageSet.cfg文件读取获得。

     注意
     :   VisionMaster软件名称可通过中性包工具进行修改，为了获取该软件的实际名称，需要从配置文件读取软件名称。由于中性包工具没有修改注册表名称，因此不能从注册表直接获取软件名称。
  3. 判断VisionMaster系统环境变量设置是否正确：

     检测系统环境变量Path是否保存当前版本VisionMaster的路径。例如：4.2版本为当前默认版本，则需添加如下环境变量：

     D:\Program Files\VisionMaster4.2.0\Applications\PublicFile\x64
     D:\Program Files\VisionMaster4.2.0\Applications\PublicFile\x86

     注意
     :   若将以上路径添加在Path的末尾，则一些同名库的使用，会被Path列表中靠前的路径指错目录，导致运行异常。因此，需要将以上路径添加到Path的最前面。
* **二次开发依赖DLL检测**
  1. 加载当前系统环境变量中的iMVS-6000PlatformSDK.dll：

     尝试加载iMVS-6000PlatformSDK.dll，判断加载是否成功。若不成功，则提示错误信息。
  2. 使用iMVS-6000PlatformSDK.dll创建句柄：

     尝试进行初始化，判断过程是否成功。若不成功，则抛出对应错误码。如：加密狗未检测到或检测异常，可以通过检查加密狗是否插好来排查故障。
