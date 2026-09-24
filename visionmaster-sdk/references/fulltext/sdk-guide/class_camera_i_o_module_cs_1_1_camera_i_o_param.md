<!-- src:class_camera_i_o_module_cs_1_1_camera_i_o_param.html -->
<!-- path:接口函数 > 通信 > 相机IO通信 > CameraIOParam -->
# CameraIOParam类 参考 通信 » 相机IO通信

相机IO通信参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CameraTypeEnum {     CommonCamera = 0x1,     SmartCamera = 2,     DalsaCamera = 3   } |
|  | 相机类型 更多... |
|  | |
| enum | IOEnableElectricalLevelEnum {     High = 0x1,     Low = 2   } |
|  | 有效电平 更多... |
|  | |
| enum | IOOutTypeEnum {     Ok = 0x1,     Ng = 2   } |
|  | 输出类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| CameraTypeEnum | CameraType `[get, set]` |
|  | 相机类型 更多... |
|  | |
| bool | DurationTimeEnable `[get, set]` |
|  | 持续时间使能 更多... |
|  | |
| int | IODurationTime `[get, set]` |
|  | 持续时间，范围：[1,10000] 更多... |
|  | |
| IOEnableElectricalLevelEnum | IOEnableElectricalLevel `[get, set]` |
|  | 有效电平（弃用） 更多... |
|  | |
| IOOutTypeEnum | IOOutType `[get, set]` |
|  | 输出类型 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
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

## 详细描述

相机IO通信参数

## 成员枚举类型说明

## ◆ CameraTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CameraTypeEnum | | strong |

相机类型

| 枚举值 | |
| --- | --- |
| CommonCamera | 普通相机 |
| SmartCamera | 智能相机 |
| DalsaCamera | 线阵相机 |

## ◆ IOEnableElectricalLevelEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum IOEnableElectricalLevelEnum | | strong |

有效电平

| 枚举值 | |
| --- | --- |
| High | 高电平有效 |
| Low | 低电平有效 |

## ◆ IOOutTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum IOOutTypeEnum | | strong |

输出类型

| 枚举值 | |
| --- | --- |
| Ok | OK时输出 |
| Ng | NG时输出 |

## 属性说明

## ◆ CameraType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CameraTypeEnum CameraType | | getset |

相机类型

## ◆ DurationTimeEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DurationTimeEnable | | getset |

持续时间使能

## ◆ IODurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int IODurationTime | | getset |

持续时间，范围：[1,10000]

## ◆ IOEnableElectricalLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IOEnableElectricalLevelEnum IOEnableElectricalLevel | | getset |

有效电平（弃用）

## ◆ IOOutType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IOOutTypeEnum IOOutType | | getset |

输出类型
