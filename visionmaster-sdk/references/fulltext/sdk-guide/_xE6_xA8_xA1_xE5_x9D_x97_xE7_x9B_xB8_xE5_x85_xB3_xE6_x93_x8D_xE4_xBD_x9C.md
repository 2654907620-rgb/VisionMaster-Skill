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
