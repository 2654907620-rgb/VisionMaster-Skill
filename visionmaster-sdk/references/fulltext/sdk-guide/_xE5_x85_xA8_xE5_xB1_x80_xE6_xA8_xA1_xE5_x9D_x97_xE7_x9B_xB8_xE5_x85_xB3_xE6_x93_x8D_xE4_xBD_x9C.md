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
