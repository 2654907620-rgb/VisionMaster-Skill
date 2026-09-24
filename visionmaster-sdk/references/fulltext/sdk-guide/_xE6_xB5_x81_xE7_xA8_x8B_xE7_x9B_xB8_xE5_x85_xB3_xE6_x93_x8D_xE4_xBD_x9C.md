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
