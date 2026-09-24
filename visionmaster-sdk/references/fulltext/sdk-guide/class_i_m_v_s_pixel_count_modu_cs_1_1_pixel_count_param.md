<!-- src:class_i_m_v_s_pixel_count_modu_cs_1_1_pixel_count_param.html -->
<!-- path:接口函数 > 弃用 > 像素统计 > PixelCountParam -->
# PixelCountParam类 参考 弃用 » 像素统计

像素统计参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| PixelCountRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | LowThresh `[get, set]` |
|  | 低阈值，范围：[0,255] 更多... |
|  | |
| int | HighThresh `[get, set]` |
|  | 高阈值，范围：[0,255] 更多... |
|  | |
| bool | CountLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | CountLimitLow `[get, set]` |
|  | 数量范围，范围：[0,999999999] 更多... |
|  | |
| int | CountLimitHigh `[get, set]` |
|  | 数量范围，范围：[0,999999999] 更多... |
|  | |
| bool | RatioLimitEnable `[get, set]` |
|  | 比率判断 更多... |
|  | |
| double | RatioLimitLow `[get, set]` |
|  | 比率范围，范围：[0,1] 更多... |
|  | |
| double | RatioLimitHigh `[get, set]` |
|  | 比率范围，范围：[0,1] 更多... |
|  | |
| bool | BinaryEnable `[get, set]` |
|  | 输出图像 更多... |
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

像素统计参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PixelCountRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ LowThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LowThresh | | getset |

低阈值，范围：[0,255]

## ◆ HighThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HighThresh | | getset |

高阈值，范围：[0,255]

## ◆ CountLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CountLimitEnable | | getset |

数量判断

## ◆ CountLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountLimitLow | | getset |

数量范围，范围：[0,999999999]

## ◆ CountLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountLimitHigh | | getset |

数量范围，范围：[0,999999999]

## ◆ RatioLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RatioLimitEnable | | getset |

比率判断

## ◆ RatioLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RatioLimitLow | | getset |

比率范围，范围：[0,1]

## ◆ RatioLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RatioLimitHigh | | getset |

比率范围，范围：[0,1]

## ◆ BinaryEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BinaryEnable | | getset |

输出图像
