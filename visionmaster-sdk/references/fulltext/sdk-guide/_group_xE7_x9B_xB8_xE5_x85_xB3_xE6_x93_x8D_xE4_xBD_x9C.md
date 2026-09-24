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
