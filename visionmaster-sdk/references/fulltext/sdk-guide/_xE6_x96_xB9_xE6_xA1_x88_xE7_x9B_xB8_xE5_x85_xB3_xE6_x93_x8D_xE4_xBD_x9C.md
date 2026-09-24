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
