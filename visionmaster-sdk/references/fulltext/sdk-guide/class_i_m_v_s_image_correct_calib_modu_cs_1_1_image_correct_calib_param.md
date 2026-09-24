<!-- src:class_i_m_v_s_image_correct_calib_modu_cs_1_1_image_correct_calib_param.html -->
<!-- path:接口函数 > 图像处理 > 畸变校正 > ImageCorrectCalibParam -->
# ImageCorrectCalibParam类 参考 图像处理 » 畸变校正

畸变校正参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CorrectModelEnum {     CorrectModelLinear = 0x1,     CorrectModelRadial = 0x2,     CorrectModelPersRadial = 0x3   } |
|  | 校正模式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| string | CalibPath `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| CorrectModelEnum | CorrectModel `[get, set]` |
|  | 校正模式 更多... |
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

畸变校正参数

## 成员枚举类型说明

## ◆ CorrectModelEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CorrectModelEnum | | strong |

校正模式

| 枚举值 | |
| --- | --- |
| CorrectModelLinear | 透视畸变校正 |
| CorrectModelRadial | 径向畸变校正 |
| CorrectModelPersRadial | 径向透视畸变校正 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ CalibPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPath | | getset |

标定文件路径

## ◆ CorrectModel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CorrectModelEnum CorrectModel | | getset |

校正模式
