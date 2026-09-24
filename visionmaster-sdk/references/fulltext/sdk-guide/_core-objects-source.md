

<!-- ===== 编程引导 > 配置流程 > WPF框架 ===== -->

<!-- src:_w_p_f_xE6_xA1_x86_xE6_x9E_xB6.html -->
<!-- path:编程引导 > 配置流程 > WPF框架 -->
# WPF框架

本章节主要介绍WPF框架的配置流程及其注意事项。

## 控件调用

1. 动态库文件 VMControls.WPF.Release.dll 内，已定义以WPF方式封装的控件类。
2. 使用自动工具/手动添加该动态库及其依赖库的引用，推荐自动工具方式，工具路径：..\Development\V4.x\ComControls\Tool\ImportRef.exe。
3. 正常安装后，默认可从WPF工具箱中拖出控件。

   注解
   :   若工具箱中无对应控件，可通过右键菜单【选择项】打开【选择工具箱项】界面，然后手动浏览打开对应版本VMControls.WPF.Release.dll动态库文件，最后勾选WPF组件以添加对应控件。
4. （可选）：若不使用WPF工具箱，也可通过xaml设计器方式直接集成其中的控件。

## 注意事项

* 支持.NET Framework，要求4.6.1版本及以上，不支持.NET Core。
* 在项目属性中的平台目标选择【Any CPU】的情况下，需去除勾选【首选32位】。
* 手动添加VM相关动态库引用后，需设置库属性中的复制本地为【False】。
* 在程序退出前，可调用接口释放VM相关资源，请避免在析构函数中调用接口。
* 参数控件和参数渲染控件暂不支持记忆参数订阅框显示的默认方式。
* 独立Group控件暂不支持执行和耗时显示功能。



<!-- ===== 编程引导 > 配置流程 > WinForm框架 ===== -->

<!-- src:_win_form_xE6_xA1_x86_xE6_x9E_xB6.html -->
<!-- path:编程引导 > 配置流程 > WinForm框架 -->
# WinForm框架

本章节主要介绍WinForm框架的配置流程及其注意事项。

## 控件调用

1. 动态库文件 VMControls.Winform.Release.dll 内，已定义以Winform方式封装的控件类。
2. 使用自动工具/手动添加该动态库及其依赖库的引用，推荐自动工具方式，工具路径：..\Development\V4.x\ComControls\Tool\ImportRef.exe。
3. 正常安装后，默认可从WinForm工具箱中拖出控件。

   注解
   :   若工具箱中无对应控件，可通过右键菜单【选择项】打开【选择工具箱项】界面，然后手动浏览打开对应版本VMControls.Winform.Release.dll动态库文件，最后勾选.NET Framework组件以添加对应控件。

## 注意事项

* 支持.NET Framework，要求4.6.1版本及以上，不支持.NET Core。
* 在项目属性中的平台目标选择【Any CPU】的情况下，需去除勾选【首选32位】。
* 手动添加VM相关动态库引用后，需设置库属性中的复制本地为【False】。
* 程序退出前，可调用接口释放VM相关资源，请避免在析构函数中调用接口。
* 参数控件和参数渲染控件暂不支持记忆参数订阅框显示的默认方式。
* 独立Group控件暂不支持执行和耗时显示功能。



<!-- ===== 编程引导 > 配置流程 > 动态库介绍及添加说明 ===== -->

<!-- src:_xE5_x8A_xA8_xE6_x80_x81_xE5_xBA_x93_xE4_xBB_x8B_xE7_xBB_x8D_xE5_x8F_x8A_xE6_xB7_xBB_xE5_x8A_xA0_xE8_xAF_xB4_xE6_x98_x8E.html -->
<!-- path:编程引导 > 配置流程 > 动态库介绍及添加说明 -->
# 动态库介绍及添加说明

本章节主要介绍配置流程中涉及的动态库及其添加说明。

## dll动态库功能

* VM.Core.dll：包含所有方案、流程的对外接口。
* VM.PlatformSDKCS.dll：提供对外接口的底层实现，是所有对外接口的基础库。
* VMControls.Interface.dll、VMControls.BaseInterface.dll：控件对外接口的基础库。
* VMControls.RenderInterface.dll：带渲染功能控件的基础库，如ROI、图形显示等。
* VMControls.Winform.Release.dll：Winform控件的基础库，包含Winform控件的对外接口。
* VMControls.WPF.Release.dll：包含WPF控件的对外接口。

## 开发方式说明

以下开发方式说明不包含具体模块，如使用到模块，在以下基础上导入使用到的对应模块dll即可。

* 纯调接口方式（无控件）需导入以下2个dll：

  + VM.Core.dll
  + VM.PlatformSDKCS.dll
* Winform控件需导入以下6个dll：

  + VM.Core.dll
  + VM.PlatformSDKCS.dll
  + VMControls.Interface.dll
  + VMControls.BaseInterface.dll
  + VMControls.RenderInterface.dll
  + VMControls.Winform.Release.dll
* WPF控件需导入以下6个dll：
  + VM.Core.dll
  + VM.PlatformSDKCS.dll
  + VMControls.Interface.dll
  + VMControls.BaseInterface.dll
  + VMControls.RenderInterface.dll
  + VMControls.WPF.Release.dll



<!-- ===== 编程引导 > 方案相关操作 ===== -->

<!-- src:_xE6_x96_xB9_xE6_xA1_x88_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 方案相关操作 -->
# 方案相关操作

方案相关操作主要包括加载方案、保存方案、获取方案版本与路径信息、禁用/启用流程、方案执行一次、连续执行、停止执行等。

## 接口调用流程

方案相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

方案相关操作示例代码如下，仅供参考。

```
using System;
using System.Collections.Generic;
using VM.Core;
using VM.PlatformSDKCS;

namespace VM.Test
{
 public class SolutionTest
    {
 static void Main()
        {
 try
            {
 //获取方案版本号
 string strVersion = VmSolution.Instance.GetSolutionVersion("D:\\Test.sol", "");

 //判断方案是否加密
 bool bPassword = VmSolution.Instance.HasPassword("D:\\Test.sol");

 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //获取当前方案路径
 string strPath = VmSolution.Instance.SolutionPath;

 //使用流程名称获取流程对象
                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];

 //获取方案所有流程对象
                List<VmProcedure> procedureList = new List<VmProcedure>();
                VmSolution.Instance.GetAllProcedureObjects(ref procedureList);

 //获取方案所有流程信息
 ProcessInfoList stProcInfoList = VmSolution.Instance.GetAllProcedureList();

 //获取方案所有模块信息
 ModuleInfoList stModuInfoList = VmSolution.Instance.GetAllModuleList();

 //使用流程名称禁用流程，禁用后流程不参与方案运行
                VmSolution.Instance.DisableProcedure("流程1");

 //使用流程名称启用流程
                VmSolution.Instance.EnableProcedure("流程1");

 //使用流程名称删除流程
                VmSolution.Instance.DeleteOneProcedure("流程2");

 //禁用方案所有流程/Group/模块回调，可提高运行效率，降低CPU资源依赖
 //注意若需获取流程/Group/模块输出，还需单独启用对应流程/Group/模块的回调
                VmSolution.Instance.DisableModulesCallback();
                vmProcedure.EnableResultCallback();

 //启用方案所有流程/Group/模块回调
                VmSolution.Instance.EnableModulesCallback();

 //方案同步执行一次
                VmSolution.Instance.SyncRun();

 //设置连续执行时间间隔
                VmSolution.Instance.SetRunInterval(500);

 //方案开始连续执行
                VmSolution.Instance.ContinuousRunEnable = true;

 //方案停止连续执行
                VmSolution.Instance.ContinuousRunEnable = false;

 //保存当前方案
                VmSolution.Save();

 //方案另存为
                VmSolution.SaveAs("D:\\Test1.sol", "");

 //关闭当前方案
                VmSolution.Instance.CloseSolution();

 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 模块相关操作 ===== -->

<!-- src:_xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 模块相关操作 -->
# 模块相关操作

模块相关操作主要包括加载方案、获取模块对象、设置参数、运行、获取结果等。

## 接口调用流程

模块相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

模块相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using ImageSourceModuleCs;
using IMVSFastFeatureMatchModuCs;

namespace VM.Test
{
 public class ModuleTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用模块全名称获取模块对象
                ImageSourceModuleTool imageModu = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
                IMVSFastFeatureMatchModuTool fastMatchModu = (IMVSFastFeatureMatchModuTool)VmSolution.Instance["流程1.快速匹配1"];

 //通过模块对象接口获取模块参数对象，用于设置/获取模块参数
                imageModu.ModuParams.ImageSourceType = ImageSourceTypeEnum.SDK;

 //图像源模块选择SDK模式，可使用接口设置图像数据
 //注意设置后图像数据仅当次执行有效，执行完成后清空，再次执行需再次设置
                imageModu.SetImagePath("D:\\test.jpg");

 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                imageModu.SetImageData(inputImage);

 //方案同步执行一次
                VmSolution.Instance.SyncRun();

 //通过模块对象接口获取模块结果对象，用于获取模块输出
 //注意每次方案执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                ImageSourceResult imageSourceResult = imageModu.ModuResult;
 ImageBaseData outputImage = imageSourceResult.ImageData;

 //通过模块对象接口导入模型文件，注意会替换模块当前所有模型文件
 string[] moduDataPath = new string[1] { @"D:\test.fmxml" };
                fastMatchModu.ImportModelData(moduDataPath);

 //通过模块参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
                fastMatchModu.ModuParams.InputImage = outputImage;

 //通过模块参数对象接口获取模块ROI对象，用于设置模块ROI数据
 //注意设置后ROI数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 //注意设置图形和设置掩膜功能互斥，不会同时起效
                FastFeatureMatchRoiManager nFastFeatModuRoiManager = fastMatchModu.ModuParams.ModuRoiManager;

 VM.PlatformSDKCS.PointF nPointF = new VM.PlatformSDKCS.PointF(1, 1);
 RectBox nRectBox = new RectBox(nPointF, 100, 100, 90);
                nFastFeatModuRoiManager.RoiRectangle = nRectBox;
                nFastFeatModuRoiManager.MaskImage = outputImage;

 //通过模块对象接口自执行模块，仅该模块会同步执行一次，其余模块无动作
 //注意执行前需使用流程执行、接口设置等方式填充完毕模块执行所需输入数据，不然会执行错误
                fastMatchModu.Run();

 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 流程相关操作 ===== -->

<!-- src:_xE6_xB5_x81_xE7_xA8_x8B_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 流程相关操作 -->
# 流程相关操作

流程相关操作主要包括导入流程、获取所有模块列表、禁用/启用流程、获取输出配置结果、流程执行一次、连续执行、停止执行、删除流程实例等。

## 接口调用流程

流程相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

流程相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;

namespace VM.Test
{
 public class ProcedureTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用流程名称获取流程对象
                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];

 //获取流程所有模块信息
 ModuleInfoList stModuInfoList = vmProcedure.GetAllModuleList();

 //获取流程本层级模块信息，不包含Group内部模块
 ModuleInfoList stSomeModuInfoList = vmProcedure.GetProcedureModuleList();

 //禁用流程，禁用后流程不参与方案运行
                vmProcedure.IsEnabled = false;

 //启用流程
                vmProcedure.IsEnabled = true;

 //通过流程对象接口获取流程局部变量对象，用于设置/获取局部变量等
                IVarModule procedureVar = vmProcedure.LocalVariable;

 //通过流程对象接口获取流程参数对象，用于设置输入数据、设置/获取模块参数等
                ProcedureParam procedureParam = vmProcedure.ModuParams;

 //通过流程参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                procedureParam.SetInputImage_V2("ImageData", inputImage);

 //流程同步执行一次
                vmProcedure.Run();

 //通过流程对象接口获取流程结果对象，用于获取流程输出
 //注意每次流程执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                ProcedureResult procedureResult = vmProcedure.ModuResult;
 ImageBaseData outputImage = procedureResult.GetOutputImageV2("ImageData0");

 //加载流程，仅支持绝对路径，编码格式UTF-8
 //注意非线程安全，不支持多线程调用
                vmProcedure = VmProcedure.Load("D:\\TestPrc.prc", "");

 //设置连续执行时间间隔
                vmProcedure.SetContinousRunInterval(500);

 //流程开始连续执行
                vmProcedure.ContinuousRunEnable = true;

 //流程停止连续执行
                vmProcedure.ContinuousRunEnable = false;

 //保存流程
 //注意非线程安全，不支持多线程调用
                vmProcedure.SaveAs("D:\\TestPrc1.prc", "");

 //删除流程
                vmProcedure.Dispose();

 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > Group相关操作 ===== -->

<!-- src:_group_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > Group相关操作 -->
# Group相关操作

Group相关操作主要包括导入Group、获取模块列表、禁用/启用Group、自执行、导出Group、删除Group等。

## 接口调用流程

Group相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

Group相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using IMVSGroupCs;

namespace VM.Test
{
 public class GroupTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用Group全名称获取方案内Group对象
                IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];

 //禁用Group，禁用后Group不参与方案运行
                groupTool.DisableGroup();

 //启用Group
                groupTool.EnableGroup();

 //加载独立Group，仅支持绝对路径，编码格式UTF-8
 //注意非线程安全，不支持多线程调用
 //注意独立Group与方案并列，并非所属关系，无法使用方案对象获取或操作
                groupTool = IMVSGroupTool.LoadIndependentGroup("D:\\TestGro.gro");

 //获取Group所有模块信息
 GroupModuInfoList stModuInfoList = groupTool.GetAllModuleList();

 //通过Group对象接口获取Group参数对象，用于设置输入数据、设置/获取模块参数等
                GroupParam groupParam = groupTool.ModuParams;

 //通过Group参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                groupParam.SetInputImage_V2("ImageData", inputImage);

 //Group同步执行一次
                groupTool.Run();

 //通过Group对象接口获取Group结果对象，用于获取Group输出
 //注意每次Group执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                GroupResult groupResult = groupTool.ModuResult;
 ImageBaseData outputImage = groupResult.GetOutputImageV2("ImageData0");

 //保存Group
 //注意非线程安全，不支持多线程调用
                groupTool.SaveAs("D:\\TestGro1.gro");

 //删除Group
                groupTool.DestroyGroup();

 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 全局模块相关操作 ===== -->

<!-- src:_xE5_x85_xA8_xE5_xB1_x80_xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 全局模块相关操作 -->
# 全局模块相关操作

全局模块相关操作主要包括全局变量、全局通信、全局光源、数据队列等全局模块功能交互。

## 示例代码

全局模块相关操作示例代码如下，仅供参考。

```
using VM.Core;
using VM.PlatformSDKCS;
using CommManagerModuleCs;
using DataQueueModuleCs;
using GlobalVariableModuleCs;
using GlobalCameraModuleCs;
using LightControlCs;
using System;
using System.Text;

namespace VM.Test
{
 public class GlobalModuleTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //中文VM下搭建的方案，使用全局模块中文名称获取模块对象
                GlobalVariableModuleTool globalVar = (GlobalVariableModuleTool)VmSolution.Instance["全局变量1"];
                CommManagerModuleTool commManager = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];
                DataQueueModuleTool dataQueue = (DataQueueModuleTool)VmSolution.Instance["数据队列1"];
                GlobalCameraModuleTool globalCamera = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"];
                LightControlTool lightControl = (LightControlTool)VmSolution.Instance["全局光源1"];

 //英文VM下搭建的方案，使用全局模块英文名称获取模块对象
                GlobalVariableModuleTool eGlobalVar = (GlobalVariableModuleTool)VmSolution.Instance["Global Variable1"];
                CommManagerModuleTool eCommManager = (CommManagerModuleTool)VmSolution.Instance["CommManagerModule1"];
                DataQueueModuleTool eDataQueue = (DataQueueModuleTool)VmSolution.Instance["Data Queue1"];
                GlobalCameraModuleTool eGlobalCamera = (GlobalCameraModuleTool)VmSolution.Instance["Global Camera1"];
                LightControlTool eLightControl = (LightControlTool)VmSolution.Instance["Light Control1"];

 //模块对象进行判空后，调用接口/属性实现操作
 if (null != globalVar)
                {
 //设置全局变量
                    globalVar.SetGlobalVar("var0", "100");

 //获取全局变量
 string tmp = globalVar.GetGlobalVar("var0");
                }
 //通信管理模块设置数据和获取数据，是否连接
 if (null != commManager)
                {
 // 设置字符串型数据
                    commManager.SetString(0, "abcd");
 int[] aIntVal = new int[3];
                    aIntVal[0] = 10;
                    aIntVal[1] = 11;
                    aIntVal[2] = 12;
 // 设置整型数据
                    commManager.SetInt(1, aIntVal, 0);
 byte[] btData = null;
                    commManager.GetReadData(1, ref btData);

 string strData = Encoding.UTF8.GetString(btData).TrimEnd('\0');

 bool isDeviceConnect = commManager.bIsDeviceConnect(1);
                }
 //全局光源模块设置全局参数信息
 if (null != lightControl)
                {
                    GlobalLightParam stLight = new GlobalLightParam();
                    stLight.nDeviceIndex = 1;
                    stLight.nDeviceType = (int)DeviceTypeEnum.TYPE_VC3000_GPIO;
                    stLight.nTriggerTime = 100;
 // 设置所有通道值
                    stLight.stLightConfig.stChannel1.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel1.bChannelEnable = true;
                    stLight.stLightConfig.stChannel1.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel1.nLightState = 1;
                    stLight.stLightConfig.stChannel1.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel1.nDurationTime = 10;

                    stLight.stLightConfig.stChannel2.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel2.bChannelEnable = true;
                    stLight.stLightConfig.stChannel2.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel2.nLightState = 1;
                    stLight.stLightConfig.stChannel2.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel2.nDurationTime = 10;

                    stLight.stLightConfig.stChannel3.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel3.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel3.nLightState = 1;
                    stLight.stLightConfig.stChannel3.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel3.nDurationTime = 10;

                    stLight.stLightConfig.stChannel4.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel4.bChannelEnable = true;
                    stLight.stLightConfig.stChannel4.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel4.nLightState = 1;
                    stLight.stLightConfig.stChannel4.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel4.nDurationTime = 10;

                    lightControl.SetGlobalLightParam(stLight);

                }
 //数据队列模块设置数据和获取数据
 if (null != dataQueue)
                {
                    StringValue stStr = new StringValue();
                    stStr.astValue = new StringInfo[256];
                    stStr.nNum = 1;
                    stStr.nIndex = 0;
                    stStr.astValue[0].strValue = "abcd";
                    dataQueue.SetStringData(stStr);
                    VmSolution.Instance.Run();
                    StringValue stVal = dataQueue.GetStringData(0);
                    VmSolution.Instance.Run();
                    IntValue stIntVal = dataQueue.GetIntData(1);
                    VmSolution.Instance.Run();
                    FloatValue stFloatVal = dataQueue.GetFloatData(2);

                }
 //全局相机模块设置触发源，获取相机列表+设置和获取选中相机
 if (null != globalCamera)
                {
                    globalCamera.ModuParams.TriggerSource = 1;
                    CameraInfoList cameraInfoList = globalCamera.ModuParams.GetCameraInfoList();

 string sn = globalCamera.ModuParams.GetChosenCameraSN();
                    globalCamera.ModuParams.SetChosenCameraSN(sn);

                }
 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 控件相关调用 ===== -->

<!-- src:_xE6_x8E_xA7_xE4_xBB_xB6_xE7_x9B_xB8_xE5_x85_xB3_xE8_xB0_x83_xE7_x94_xA8.html -->
<!-- path:编程引导 > 控件相关调用 -->
# 控件相关调用

控件相关调用主要包括流程配置控件、参数配置控件、渲染控件、全局模块控件、前端运行界面控件等接口调用。

此处呈现几个常用控件的界面，如下图所示。

## 接口调用流程

控件相关调用接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

控件相关调用示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using VMControls.WPF.Release;
using VMControls.Winform.Release;
using GlobalCameraModuleCs;
using IMVSCircleFindModuCs;
using IMVSGroupCs;

namespace VM.Test
{
 public class ControlsTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //注意Winform或WPF控件需要从不同库文件引用，控件接口相似，示例代码以Winform为例

                #region 1.流程配置控件
                VMControls.Winform.Release.VmProcedureConfigControl vmProcedureConfigControl = new VMControls.Winform.Release.VmProcedureConfigControl();

 //根据流程名称绑定显示某个流程，控件默认显示所有流程
                vmProcedureConfigControl.BindSingleProcedure("流程1");

 //控件恢复显示所有流程
                vmProcedureConfigControl.BindMultiProcedure();

 //锁定工作区，不允许编辑方案
                vmProcedureConfigControl.LockWorkArea();

 //解锁工作区，允许编辑方案
                vmProcedureConfigControl.UnlockWorkArea();

 //锁定参数配置页，不允许编辑流程/Group/模块的参数配置页
                vmProcedureConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数配置页
                vmProcedureConfigControl.SetParamTabEditable(true);

 //设置控件自适应属性
                vmProcedureConfigControl.AutoSize = true;

 // 释放控件资源
                vmProcedureConfigControl.Dispose();
                #endregion

                #region 2.参数配置控件
                VMControls.Winform.Release.VmParamsConfigControl vmParamsConfigControl = new VMControls.Winform.Release.VmParamsConfigControl();

 //绑定流程对象，可配置其参数
                VmProcedure paramsConfigCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlProcess;

 //绑定Group对象，可配置其参数
                IMVSGroupTool paramsConfigCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlGroup;

 //绑定模块对象，可配置其参数
                IMVSCircleFindModuTool paramsConfigCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlCircleTool;

 //锁定参数配置页，不允许编辑流程/Group/模块的参数
                vmParamsConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数
                vmParamsConfigControl.SetParamTabEditable(true);

 //获取绑定模块参数配置页面的所有Tab名称
                vmParamsConfigControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmParamsConfigControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmParamsConfigControl.SetParamTabVisible(tabName, true);

 // 释放控件资源
                vmParamsConfigControl.Dispose();

                #endregion

                #region 3.渲染控件
                VMControls.Winform.Release.VmRenderControl vmRenderControl = new VMControls.Winform.Release.VmRenderControl();

 //绑定流程对象，执行后自动显示其图形图像
                VmProcedure renderCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmRenderControl.ModuleSource = renderCtrlProcess;

 //绑定Group对象，执行后自动显示其图形图像
                IMVSGroupTool renderCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmRenderControl.ModuleSource = renderCtrlGroup;

 //绑定模块对象，执行后自动显示其图形图像
                IMVSCircleFindModuTool renderCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmRenderControl.ModuleSource = renderCtrlCircleTool;

 //绘制图像，若控件已绑定对象，需考虑执行前后的时序配合
 VM.PlatformSDKCS.ImageBaseData renderCtrlImage = new VM.PlatformSDKCS.ImageBaseData();
                vmRenderControl.ImageSource = renderCtrlImage;

 //绘制图形，若控件已绑定对象，需考虑执行前后的时序配合
                VMControls.WPF.TextEx renderCtrlText = new VMControls.WPF.TextEx();
                renderCtrlText.Content = "Hello";
                vmRenderControl.DrawShape(renderCtrlText);

 //添加图形，控件需绑定对象，执行前添加，执行后显示
 //注意添加后图形数据仅当次执行有效，执行完成后清空，再次执行需再次添加
                renderCtrlText.Content = "Hello";
                vmRenderControl.AddShape(renderCtrlText);

 //清空当前显示的图形图像
                vmRenderControl.ClearDisplayView();

 //使用文件路径设置控件显示区背景图
 //注意该图片的尺寸需小于100*100
                vmRenderControl.SetBackground("D:\\background.bmp");

 //使用RGB数值设置控件显示区背景色
 //需传入“#+16进制数”表示的颜色字符串
                vmRenderControl.SetBackground("#FF00FF");

 //使用文件路径保存当前显示的原始图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmRenderControl.SaveOriginalImage("D:\\save.bmp");

 //使用文件路径保存当前显示的渲染图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmRenderControl.SaveRenderedImage("D:\\save.bmp");

 //隐藏图层选择控件
                vmRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmRenderControl.SwitchBackgroundImage(backgroundImageName);

 // 释放控件资源
                vmRenderControl.Dispose();


                #endregion

                #region 4.全局模块控件
                VMControls.Winform.Release.VmGlobalToolControl vmGlobalToolControl = new VMControls.Winform.Release.VmGlobalToolControl();

 //打开全局变量
                vmGlobalToolControl.OpenGlobalVariable();

 //打开全局脚本
                vmGlobalToolControl.OpenGlobalScript();

 //打开相机管理
                vmGlobalToolControl.OpenGlobalCamera();

 //打开通信管理
                vmGlobalToolControl.OpenCommunicationManager();

 //打开全局触发
                vmGlobalToolControl.OpenGlobalTrigger();

 // 释放控件资源
                vmGlobalToolControl.Dispose();

                #endregion

                #region 5.前端运行界面控件
                VMControls.Winform.Release.VmFrontendControl vmFrontendControl = new VMControls.Winform.Release.VmFrontendControl();

 //当前方案已配置运行界面，使用控件进行加载显示
                vmFrontendControl.LoadFrontendSource();

 //控件主动自适应大小
                vmFrontendControl.AutoChangeSize();

 //锁定运行界面关联的流程/Group/模块参数配置页，不允许编辑流程/Group/模块的参数
                vmFrontendControl.SetParamTabEditable(false);

 //解锁运行界面关联的流程/Group/模块参数配置页，允许编辑流程/Group/模块的参数
                vmFrontendControl.SetParamTabEditable(true);

 // 释放控件资源
                vmFrontendControl.Dispose();

                #endregion

                #region 6.主界面配置控件相关操作
                VMControls.Winform.Release.VmMainViewConfigControl vmMainViewConfigControl = new VMControls.Winform.Release.VmMainViewConfigControl();

 //根据流程名称绑定显示某个流程，控件默认显示所有流程
                vmMainViewConfigControl.BindSingleProcedure("流程1");

 //控件恢复显示所有流程
                vmMainViewConfigControl.BindMultiProcedure();

 //锁定工作区，不允许编辑方案
                vmMainViewConfigControl.LockWorkArea();

 //解锁工作区，允许编辑方案
                vmMainViewConfigControl.UnlockWorkArea();

 //锁定参数配置页，不允许编辑流程/Group/模块的参数配置页
                vmMainViewConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数配置页
                vmMainViewConfigControl.SetParamTabEditable(true);

 // 释放控件资源
                vmMainViewConfigControl.Dispose();
                #endregion

                #region 7.独立Group控件
                VMControls.Winform.Release.VmSingleModuleSetConfigControl vmSingleModuleSetConfigControl = new VMControls.Winform.Release.VmSingleModuleSetConfigControl();

 //绑定独立Group对象
                IMVSGroupTool groupTool = IMVSGroupTool.LoadIndependentGroup("D:\\test.gro");
                vmSingleModuleSetConfigControl.ModuleSource = groupTool;

 //锁定参数配置页，不允许编辑Group/模块的参数
                vmSingleModuleSetConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑Group/模块的参数
                vmSingleModuleSetConfigControl.SetParamTabEditable(true);

 // 释放控件资源
                vmSingleModuleSetConfigControl.Dispose();
                #endregion

                #region 8.实时取流控件相关操作
                VMControls.Winform.Release.VmRealTimeAcqControl vmRealTimeAcqControl = new VMControls.Winform.Release.VmRealTimeAcqControl();

 //绑定待取流模块，仅支持全局相机模块
                vmRealTimeAcqControl.ModuleSource = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"];

 //全局相机模块选中对应相机，开始实时取流
                vmRealTimeAcqControl.StartGrabbing();

 //停止实时取流
                vmRealTimeAcqControl.StopGrabbing();

 //设置功能按钮可见
                vmRealTimeAcqControl.ShowButton(true);

 // 释放控件资源
                vmRealTimeAcqControl.Dispose();
                #endregion

                #region 9.参数配置带渲染控件
                VMControls.Winform.Release.VmParamsConfigWithRenderControl vmParamsConfigWithRenderControl = new VMControls.Winform.Release.VmParamsConfigWithRenderControl();

 //绑定流程对象，可配置其参数，并在执行后自动显示其图形图像
                VmProcedure paramRenderCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlProcess;

 //绑定Group对象，可配置其参数，并在执行后自动显示其图形图像
 //注意点击控件的执行按钮，仅该对象会自执行一次，其余模块无动作
 //注意自执行前需使用流程执行、接口设置等方式填充完毕对象执行所需输入数据，不然会执行错误
                IMVSGroupTool paramRenderCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlGroup;

 //绑定模块对象，可配置其参数，并在执行后自动显示其图形图像
 //注意点击控件的执行按钮，仅该对象会自执行一次，其余模块无动作
 //注意自执行前需使用流程执行、接口设置等方式填充完毕对象执行所需输入数据，不然会执行错误
                IMVSCircleFindModuTool paramRenderCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlCircleTool;

 //锁定参数配置页，不允许编辑流程/Group/模块的参数
                vmParamsConfigWithRenderControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数
                vmParamsConfigWithRenderControl.SetParamTabEditable(true);

 //显示单/双画面模式切换按钮，双画面模式下渲染功能相关接口需使用参数区分所需操作画面
                vmParamsConfigWithRenderControl.MultiImageButtonVisible = true;

 //绘制图像，若控件已绑定对象，需考虑执行前后的时序配合
 VM.PlatformSDKCS.ImageBaseData paramRenderCtrlImage = new VM.PlatformSDKCS.ImageBaseData();
                vmParamsConfigWithRenderControl.ImageSource = paramRenderCtrlImage;

 //绘制图形，若控件已绑定对象，需考虑执行前后的时序配合
                VMControls.WPF.TextEx paramRenderCtrlText = new VMControls.WPF.TextEx();
                paramRenderCtrlText.Content = "Hello";
                vmParamsConfigWithRenderControl.DrawShape(paramRenderCtrlText);

 //添加图形，控件需绑定对象，执行前添加，执行后显示
 //注意添加后图形数据仅当次执行有效，执行完成后清空，再次执行需再次添加
                vmParamsConfigWithRenderControl.AddShape(paramRenderCtrlText);

 //清空当前显示的图形图像
                vmParamsConfigWithRenderControl.ClearDisplayView();

 //使用文件路径设置控件显示区背景图
                vmParamsConfigWithRenderControl.SetBackground("D:\\background.bmp");

 //使用RGB数值设置控件显示区背景色
                vmParamsConfigWithRenderControl.SetBackground("#FF00FF");

 //使用文件路径保存当前显示的原始图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmParamsConfigWithRenderControl.SaveOriginalImage("D:\\save.bmp");

 //使用文件路径保存当前显示的渲染图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmParamsConfigWithRenderControl.SaveRenderedImage("D:\\save.bmp");

 //获取绑定模块参数配置页面的所有Tab名称
                vmParamsConfigWithRenderControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmParamsConfigWithRenderControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmParamsConfigWithRenderControl.SetParamTabVisible(tabName, true);

 //隐藏图层选择控件
                vmParamsConfigWithRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmParamsConfigWithRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmParamsConfigWithRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmParamsConfigWithRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmParamsConfigWithRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmParamsConfigWithRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmParamsConfigWithRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmParamsConfigWithRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmParamsConfigWithRenderControl.SwitchBackgroundImage(backgroundImageName);
 //调整参数配置页面宽度
                vmParamsConfigWithRenderControl.SetParamConfigUIWidth(500);

 //窗口式参数渲染控件和该控件相似，可直接作为窗口显示，仅支持Winform
                VMControls.Winform.Release.VmParamsWithRenderForm vmParamsWithRenderForm = new VMControls.Winform.Release.VmParamsWithRenderForm();

 // 释放控件资源
                vmParamsConfigWithRenderControl.Dispose();
                #endregion

                #region 9.综合配置控件
                VMControls.Winform.Release.VmComprehensiveConfigWithRenderControl vmComprehensiveConfigWithRenderControl = new VMControls.Winform.Release.VmComprehensiveConfigWithRenderControl();

 //绑定对象，可配置其参数，并在执行后自动显示其图形图像
                vmComprehensiveConfigWithRenderControl.ModuleSource = VmSolution.Instance;

 //获取综合模块参数配置页面的所有Tab名称
                vmComprehensiveConfigWithRenderControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmComprehensiveConfigWithRenderControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmComprehensiveConfigWithRenderControl.SetParamTabVisible(tabName, true);

 //隐藏图层选择控件
                vmComprehensiveConfigWithRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmComprehensiveConfigWithRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmComprehensiveConfigWithRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmComprehensiveConfigWithRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmComprehensiveConfigWithRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmComprehensiveConfigWithRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmComprehensiveConfigWithRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmComprehensiveConfigWithRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmComprehensiveConfigWithRenderControl.SwitchBackgroundImage(backgroundImageName);

 //调整参数配置页面宽度
                vmComprehensiveConfigWithRenderControl.SetParamConfigUIWidth(500);
 // 释放控件资源
                vmComprehensiveConfigWithRenderControl.Dispose();
                #endregion

 //退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 事件 > 事件设置方法 ===== -->

<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:编程引导 > 事件 > 事件设置方法 -->
# 事件设置方法

事件设置方法的示例代码如下，仅供参考。

```
using System;
using System.Text;
using VM.Core;
using VM.PlatformSDKCS;
using IMVSCircleFindModuCs;
using IMVSGroupCs;

namespace VM.Test
{
 public class EventTest
    {
 static void Main()
        {
 try
            {
                EventClass eventClass = new EventClass();

 // 初始化订阅方案事件
                eventClass.InitSubscribeSolutionEvent();

 // 加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
                if (null == vmProcedure) return;

 // 初始化订阅流程事件
                eventClass.InitSubscribeProcedureEvent(vmProcedure);

                IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                if (null == groupTool) return;

 // 初始化订阅Group事件
                eventClass.InitSubscribeGroupEvent(groupTool);

                IMVSCircleFindModuTool circleFindModule = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                if (null == circleFindModule) return;

 // 初始化订阅模块事件
                eventClass.InitSubscribeModuleEvent(circleFindModule);

 // 退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }

 public class EventClass
    {
 // 初始化订阅方案事件
 public void InitSubscribeSolutionEvent()
        {
 // 流程工作状态
            VmSolution.OnWorkStatusEvent += Handle_OnWorkStatusEvent;

 // 加密狗状态
            VmSolution.OnDongleEvent += Handle_OnDongleEvent;

 // 开始加载方案
            VmSolution.OnSolutionLoadBeginEvent += Handle_OnSolutionLoadBeginEvent;

 // 方案加载结束
            VmSolution.OnSolutionLoadEndEvent += Handle_OnSolutionLoadEndEvent;

 // 模块方案加载进度
            VmSolution.OnSolutionLoadProgressEvent += Handle_OnSolutionLoadProgressEvent;

 // 服务状态回调，VM单进程版本不触发此事件
            VmSolution.OnServerStatusEvent += Handle_OnServerStatusEvent;

 // 代理崩溃，VM单进程版本不触发此事件
            VmSolution.OnProxyCrashEvent += Handle_OnProxyCrashEvent;

 // 流程解注册状态信息
            VmSolution.OnProcedureUnRegisterEvent += Handle_OnProcedureUnRegisterEvent;

 // 方案加载时模块错误警告信息
            VmSolution.OnModelLoadWarnEvent += Handle_OnModelLoadWarnEvent;

 // 连续执行开始状态信息
            VmSolution.OnProcessStatusStartEvent += Handle_OnProcessStatusStartEvent;

 // 连续执行结束状态信息
            VmSolution.OnProcessStatusStopEvent += Handle_OnProcessStatusStopEvent;

 // 模块结果信息回调
            VmSolution.OnModuleResultCallbackEvent += Handle_OnModuleResultCallbackEvent;

 // 接收数据回调（设备ID（1字节） AddressID（1字节） 数据）
            VmSolution.OnCommunicationRecvCallBackEvent += Handle_OnCommunicationRecvCallBackEvent;

 // 通信状态回调（状态 设备ID（1字节））
            VmSolution.OnCommunicationStatusCallBackEvent += Handle_OnCommunicationStatusCallBackEvent;

 // 相机取图结束信息回调
            VmSolution.OnCameraCollectCallBackEvent += Handle_OnCameraCollectCallBackEvent;

 // 相机取图开始信息回调
            VmSolution.OnCameraCollectStartCallBackEvent += Handle_OnCameraCollectStartCallBackEvent;

 // 通信连接状态回调
            VmSolution.OnCommuConnectCallBackEvent += Handle_OnCommuConnectCallBackEvent;

 // 相机连接状态回调
            VmSolution.OnCameraConnectStatusCallBackEvent += Handle_OnCameraConnectStatusCallBackEvent;

 // 相机模块添加事件
            VmSolution.OnGlobalCameraModuleAddedEvent += Handle_OnGlobalCameraModuleAddedEvent;

 // 相机模块删除事件
            VmSolution.OnGlobalCameraModuleDeletedEvent += Handle_OnGlobalCameraModuleDeletedEvent;
        }

 // 初始化订阅流程事件
 public void InitSubscribeProcedureEvent(VmProcedure vmProcedure)
        {
 // 流程开始执行状态回调
            vmProcedure.OnWorkBeginStatusCallBack += Handle_OnWorkBeginStatusCallBack;

 // 流程执行结束状态回调
            vmProcedure.OnWorkEndStatusCallBack += Handle_OnWorkEndStatusCallBack;
        }

 // 初始化订阅Group事件
 public void InitSubscribeGroupEvent(IMVSGroupTool groupModuTool)
        {
 // IO重命名事件
            groupModuTool.OnModuleIONameChanged += Handle_OnModuleIONameChanged;

 // 显示IO重命名事件
            groupModuTool.OnModuleDisplayParamNameChanged += Handle_OnModuleDisplayParamNameChanged;
        }

 // 初始化订阅模块事件
 public void InitSubscribeModuleEvent(VmModule vmModule)
        {
 // 模块结果回调
            vmModule.ModuleResultCallBackArrived += Handle_ModuleResultCallBackArrived;
        }

 // Solution 方案回调函数
 private void Handle_OnWorkStatusEvent(ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo)
        {
 // 获取流程ID，多个流程时用于区分流程
            uint processID = workStatusInfo.nProcessID;

 // 获取流程状态，1运行开始，0运行结束
            uint workStatus = workStatusInfo.nWorkStatus;

 // 获取流程耗时，仅在运行结束时有效
 float processTime = workStatusInfo.fProcessTime;
        }
 private void Handle_OnDongleEvent(ImvsSdkDefine.IMVS_DONGLE_INFO moduleInfo)
        {
 // 获取加密狗状态，正常时为0，异常时为错误码
 int dongleStatus = moduleInfo.nDongleStatus;

 // 获取加密狗型号
 byte[] bytDongleType = moduleInfo.strDongleType;
 string str = Encoding.UTF8.GetString(bytDongleType).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadBeginEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_BEGEIN_INFO solutionLoadBeginInfo)
        {
 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadBeginInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');

        }
 private void Handle_OnSolutionLoadEndEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO solutionLoadEndInfo)
        {
 // 获取加载方案状态，正常时为0，异常时为错误码
            uint status = solutionLoadEndInfo.nStatus;

 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadEndInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadProgressEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_PROCESS_INFO solutionLoadProcessInfo)
        {
 // 获取加载方案的百分比进度，取值范围0~100
            uint process = solutionLoadProcessInfo.nProcess;

        }
 private void Handle_OnServerStatusEvent(ImvsSdkDefine.IMVS_SERVER_INFO moduleInfo)
        {
 // 获取服务进程状态，单进程版本不触发
            uint serverStatus = moduleInfo.nServerStatus;

        }
 private void Handle_OnProxyCrashEvent(ImvsSdkDefine.IMVS_PROXY_CRASH_SP_INFO proxyCrashInfoo)
        {
 // 获取代理进程状态，单进程版本不触发
 int hasSolStatu = proxyCrashInfoo.nHasSolStatu;

        }
 private void Handle_OnProcedureUnRegisterEvent(ImvsSdkDefine.IMVS_PROCEDURE_UNREGISTER_INFO procedureUnregisterInfo)
        {
 // 获取删除流程ID
            uint processID = procedureUnregisterInfo.nProcessID;

 // 获取删除流程名称
 byte[] strProcessName = procedureUnregisterInfo.strProcessName;
 string str = Encoding.UTF8.GetString(strProcessName).TrimEnd('\0');
        }
 private void Handle_OnModelLoadWarnEvent(ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO_LIST loadModuleInfoList)
        {
 // 获取加载方案时，加载失败模块的信息，包括模块ID/名称等
            uint moduleNum = loadModuleInfoList.nModuleNum;
 VM.PlatformSDKCS.ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO[] astLoadModuErrInfo = loadModuleInfoList.astLoadModuErrInfo;
        }
 private void Handle_OnProcessStatusStartEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_START_CONTINUOUSLY_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnProcessStatusStopEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_STOP_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnModuleResultCallbackEvent(ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data moduleResultExInfo)
        {
 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = moduleResultExInfo.nErrorCode;

 // 获取流程/Group/模块ID
            uint moduleID = moduleResultExInfo.nModuleID;

 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = moduleResultExInfo.fModuleTime;

 // 获取流程/Group/模块算法耗时
 float algorithmTime = moduleResultExInfo.fAlgorithmTime;

 // 获取流程/Group/模块运行结果数据
 int resultNum = moduleResultExInfo.nResultNum;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data[] pInfo = moduleResultExInfo.pInfo;
 if (resultNum > 0)
            {
 // 获取其中一个结果数据
                ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data pTmpData = pInfo[0];
 // 获取结果数据名称
 string str = pTmpData.strParamName;
            }
        }
 private void Handle_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 获取接收该数据的设备的类型
 int type = reportDataInfo.nType;

 // 获取接收的数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCommunicationStatusCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 该事件使用较复杂，建议使用事件OnCommuConnectCallBackEvent
 // 获取通信状态变更的设备的类型
 int type = reportDataInfo.nType;

 // 获取通信状态变更数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCameraConnectStatusCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_CONNECT_STATUS_INFO cameraConnectStatusInfo)
        {
 // 获取相机ID
 int cameraID = cameraConnectStatusInfo->nCameraID;

 // 获取相机连接状态
 int connectStatus = cameraConnectStatusInfo->nConnectStatus;

 // 获取相机SN
 byte[] strCameraSN = cameraConnectStatusInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnGlobalCameraModuleAddedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnGlobalCameraModuleDeletedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnCameraCollectCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图结束的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图结束的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCameraCollectStartCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图开始的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图开始的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCommuConnectCallBackEvent(ImvsSdkDefine.IMVS_COMMUNICATION_CONNECT_INFO connectCollectInfo)
        {
 // 获取通信状态变更后的状态，连接为1，断开为0
            uint deviceStatus = connectCollectInfo.nDeviceStatus;

 // 获取通信状态变更的设备ID
            uint deviceID = connectCollectInfo.nDeviceID;
        }

 // Procedure 流程回调函数
 private void Handle_OnWorkBeginStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;
        }
 private void Handle_OnWorkEndStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;

 // 获取流程耗时
 float processTime = data.fProcessTime;
        }

 // Group 组合模块回调函数
 private void Handle_OnModuleIONameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }
 private void Handle_OnModuleDisplayParamNameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }

 // Module 模块回调函数
 private void Handle_ModuleResultCallBackArrived(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data data = (ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data)eventArgs.Value;

 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = data.nErrorCode;
 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = data.fModuleTime;
 // 获取流程/Group/模块算法耗时
 float algorithmTime = data.fAlgorithmTime;

 // 获取运行结果数据
            if (data.nResultNum > 0)
            {
 // 获取其中一个结果数据的名称
 string str = data.pInfo[0].strParamName;
            }
        }
    }
}
```



<!-- ===== 编程引导 > 事件 > 事件类型 ===== -->

<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE7_xB1_xBB_xE5_x9E_x8B.html -->
<!-- path:编程引导 > 事件 > 事件类型 -->
# 事件类型

事件类型具体请见下表。

| 接口 | 类型 | C# 事件 | 描述 |
| --- | --- | --- | --- |
| **方案** | 流程工作状态 | OnWorkStatusEvent | 反馈流程执行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 加密狗状态 | OnDongleEvent | 反馈加密狗状态，在加密狗插拔等状态变更时触发 |
| 开始加载方案 | OnSolutionLoadBeginEvent | 反馈方案加载开始，方案加载期间其他大多数接口不支持调用，可用于屏蔽其他接口的调用 |
| 方案加载结束 | OnSolutionLoadEndEvent | 反馈方案加载结束，方案加载期间其他大多数接口不支持调用，可用于恢复其他接口的调用 |
| 模块方案加载进度 | OnSolutionLoadProgressEvent | 反馈方案加载的百分比进度，可用于粗略显示加载进度条 |
| 服务状态回调（VM单进程版本不触发此事件） | OnServerStatusEvent | 反馈服务进程状态，服务断线或崩溃时触发一次，单进程版本不触发 |
| 代理崩溃（VM单进程版本不触发此事件） | OnProxyCrashEvent | 反馈代理进程状态，代理断线或崩溃时触发一次，单进程版本不触发 |
| 流程解注册状态信息 | OnProcedureUnRegisterEvent | 反馈流程删除状态，每个流程被删除时触发一次 |
| 方案加载时模块错误警告信息 | OnModelLoadWarnEvent | 反馈方案加载中的警告，每个模块若由于系统环境等因素加载失败时触发一次 |
| 连续执行开始状态信息 | OnProcessStatusStartEvent | 反馈流程连续执行状态，每个流程开始连续执行时触发一次 |
| 连续执行结束状态信息 | OnProcessStatusStopEvent | 反馈流程连续执行状态，每个流程停止连续执行时触发一次 |
| 模块结果信息回调 | OnModuleResultCallbackEvent | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |
| 接收数据回调 | OnCommunicationRecvCallBackEvent | 反馈通信接收到的数据，每个通信设备接收到数据时触发一次 |
| 通信状态回调 | OnCommunicationStatusCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| 相机取图结束信息回调 | OnCameraCollectCallBackEvent | 反馈相机取图信息，每个全局相机每次取图结束时触发一次 |
| 相机取图开始信息回调 | OnCameraCollectStartCallBackEvent | 反馈相机取图信息，每个全局相机每次取图开始时触发一次 |
| 相机连接状态信息回调 | OnCameraConnectStatusCallBackEvent | 反馈相机连接状态信息，每个相机上下线及创建链接触发一次，可在回调中拿到相机相对应状态的数值 |
| 创建相机时模块信息回调 | OnGlobalCameraModuleAddedEvent | 反馈模块信息，创建全局相机模块时触发一次 |
| 删除相机时模块信息回调 | OnGlobalCameraModuleDeletedEvent | 反馈模块信息，删除全局相机模块时触发一次 |
| 通信连接状态回调 | OnCommuConnectCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| **流程** | 流程开始执行状态回调 | OnWorkBeginStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 流程执行结束状态回调 | OnWorkEndStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| **Group** | IO重命名事件 | OnModuleIONameChanged | 反馈Group输入输出设置修改，每个输入/输出名称修改时触发一次 |
| 显示IO重命名事件 | OnModuleDisplayParamNameChanged | 反馈Group显示设置修改，每个显示名称修改时触发一次 |
| **模块** | 模块结果回调 | ModuleResultCallBackArrived | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |
