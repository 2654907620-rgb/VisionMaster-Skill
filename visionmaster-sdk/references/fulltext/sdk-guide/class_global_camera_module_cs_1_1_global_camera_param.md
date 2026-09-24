<!-- src:class_global_camera_module_cs_1_1_global_camera_param.html -->
<!-- path:接口函数 > 全局模块 > 全局相机 > GlobalCameraParam -->
# GlobalCameraParam类 参考 全局模块 » 全局相机

全局相机参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | GammaSelectorEnum {     GammaSelector\_USER = 1,     GammaSelector\_SRGB = 2   } |
|  | Gamma类型 更多... |
|  | |
| enum | CameraMoldEnum {     CommonCamera = 0x1,     SmartCamera = 0x2,     DalsaCamera = 0x3   } |
|  | 相机类型 更多... |
|  | |
| enum | ElectricalLevelEnum {     High = 1,     Low = 2   } |
|  | 电平类型 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| CameraInfoList | GetCameraInfoList () |
|  | 获取相机信息列表 更多... |
|  | |
| string | GetChosenCameraSN () |
|  | 获取相机SN 更多... |
|  | |
| void | SetChosenCameraSN (string value) |
|  | 设置相机SN 更多... |
|  | |
| Public 成员函数 继承自 CModuleParamBase | |
| int | GetParamValue (String strName, ref String strValue) |
|  | 获取参数值 更多... |
|  | |
| int | SetParamValue (String strName, String strValue) |
|  | 设置参数值 更多... |
|  | |
| int | GetBinaryData (String strName, IntPtr pBinData, uint nMemSize, ref uint nDataLen) |
|  | 获取二进制数据 更多... |
|  | |
| int | SetBinaryData (String strName, IntPtr pBinData, uint nDataLen) |
|  | 设置二进制数据 更多... |
|  | |
| void | SetInputInt (String strName, int[] anIntVal) |
|  | 设置整型输入 更多... |
|  | |
| void | SetInputFloat (String strName, float[] anFloatVal) |
|  | 设置浮点型输入 更多... |
|  | |
| void | SetInputString (String strName, InputStringData[] astStrData) |
|  | 设置字符串型输入 更多... |
|  | |
| void | SetInputImage (InputImageData stImageData) |
|  | 设置图像型输入 更多... |
|  | |
| void | SetInputBytes (String strName, BytesData stBytesData) |
|  | 设置二进制数据型输入 更多... |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| int | Width |
|  | 图像宽度 更多... |
|  | |
| int | Height |
|  | 图像高度 更多... |
|  | |
| double | ExposureTime |
|  | 曝光时间 更多... |
|  | |
| int | PixelFormat |
|  | 像素格式 更多... |
|  | |
| int | TriggerSource |
|  | 触发源（value范围从0开始，可参考GlobalCameraModuleAlgorithmTab.xml中的TriggerSource参数） 更多... |
|  | |
| double | TriggerDelay |
|  | 触发延迟(us) 更多... |
|  | |
| double | ConditionalTriggerNumber |
|  | 条件触发数量 更多... |
|  | |
| double | ConditionalTriggerTimeOut |
|  | 条件触发延时 更多... |
|  | |
| double | Gain |
|  | 增益(dB) 更多... |
|  | |
| bool | GammaEnable |
|  | Gamma使能 更多... |
|  | |
| GammaSelectorEnum | GammaSelector |
|  | 选择器 更多... |
|  | |
| CameraMoldEnum | CameraMold |
|  | 相机类型 更多... |
|  | |
| ElectricalLevelEnum | ElectricalLevel |
|  | 电平类型 更多... |
|  | |

## 详细描述

全局相机参数

## 成员枚举类型说明

## ◆ GammaSelectorEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum GammaSelectorEnum | | strong |

Gamma类型

| 枚举值 | |
| --- | --- |
| GammaSelector\_USER | USER |
| GammaSelector\_SRGB | SRGB |

## ◆ CameraMoldEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CameraMoldEnum | | strong |

相机类型

| 枚举值 | |
| --- | --- |
| CommonCamera | 普通相机 |
| SmartCamera | 智能相机 |
| DalsaCamera | 线阵相机 |

## ◆ ElectricalLevelEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ElectricalLevelEnum | | strong |

电平类型

| 枚举值 | |
| --- | --- |
| High | 高电平有效 |
| Low | 低电平有效 |

## 成员函数说明

## ◆ GetCameraInfoList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CameraInfoList GetCameraInfoList | ( |  | ) |  |

获取相机信息列表

## ◆ GetChosenCameraSN()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| string GetChosenCameraSN | ( |  | ) |  |

获取相机SN

## ◆ SetChosenCameraSN()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetChosenCameraSN | ( | string | *value* | ) |  |

设置相机SN

## 类成员变量说明

## ◆ Width

|  |
| --- |
| int Width |

图像宽度

## ◆ Height

|  |
| --- |
| int Height |

图像高度

## ◆ ExposureTime

|  |
| --- |
| double ExposureTime |

曝光时间

## ◆ PixelFormat

|  |
| --- |
| int PixelFormat |

像素格式

## ◆ TriggerSource

|  |
| --- |
| int TriggerSource |

触发源（value范围从0开始，可参考GlobalCameraModuleAlgorithmTab.xml中的TriggerSource参数）

## ◆ TriggerDelay

|  |
| --- |
| double TriggerDelay |

触发延迟(us)

## ◆ ConditionalTriggerNumber

|  |
| --- |
| double ConditionalTriggerNumber |

条件触发数量

## ◆ ConditionalTriggerTimeOut

|  |
| --- |
| double ConditionalTriggerTimeOut |

条件触发延时

## ◆ Gain

|  |
| --- |
| double Gain |

增益(dB)

## ◆ GammaEnable

|  |
| --- |
| bool GammaEnable |

Gamma使能

## ◆ GammaSelector

|  |
| --- |
| GammaSelectorEnum GammaSelector |

选择器

## ◆ CameraMold

|  |
| --- |
| CameraMoldEnum CameraMold |

相机类型

## ◆ ElectricalLevel

|  |
| --- |
| ElectricalLevelEnum ElectricalLevel |

电平类型
