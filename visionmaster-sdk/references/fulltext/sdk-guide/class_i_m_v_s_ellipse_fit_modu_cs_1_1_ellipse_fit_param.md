<!-- src:class_i_m_v_s_ellipse_fit_modu_cs_1_1_ellipse_fit_param.html -->
<!-- path:接口函数 > 图形生成 > 椭圆拟合 > EllipseFitParam -->
# EllipseFitParam类 参考 图形生成 » 椭圆拟合

椭圆拟合参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< PointF > | InputFittingPoint `[set]` |
|  | 输入拟合点 更多... |
|  | |
| int | ErrorTolerance `[get, set]` |
|  | 误差容忍度，范围：[1,200] 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 匹配点数判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 拟合点数范围，范围：[0,100] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 拟合点数范围，范围：[0,100] 更多... |
|  | |
| bool | CenterXLimitEnable `[get, set]` |
|  | 中心X判断 更多... |
|  | |
| double | CenterXLimitLow `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterXLimitHigh `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CenterYLimitEnable `[get, set]` |
|  | 中心Y判断 更多... |
|  | |
| double | CenterYLimitLow `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterYLimitHigh `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | ScoreLimitEnable `[get, set]` |
|  | 拟合误差判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
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

椭圆拟合参数

## 属性说明

## ◆ InputFittingPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputFittingPoint | | set |

输入拟合点

**备注**

仅当次执行起效

## ◆ ErrorTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ErrorTolerance | | getset |

误差容忍度，范围：[1,200]

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

匹配点数判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

拟合点数范围，范围：[0,100]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

拟合点数范围，范围：[0,100]

## ◆ CenterXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterXLimitEnable | | getset |

中心X判断

## ◆ CenterXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitLow | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitHigh | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterYLimitEnable | | getset |

中心Y判断

## ◆ CenterYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitLow | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ CenterYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitHigh | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

拟合误差判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

拟合误差范围，范围：[0,9999]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

拟合误差范围，范围：[0,9999]
