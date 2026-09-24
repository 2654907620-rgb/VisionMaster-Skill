<!-- src:class_i_m_v_s_p2_l_measure_modu_cs_1_1_p2_l_measure_param.html -->
<!-- path:接口函数 > 测量 > 点线测量 > P2LMeasureParam -->
# P2LMeasureParam类 参考 测量 » 点线测量

点线测量参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ChooseCoordinateEnum {     ImageCor = 0x1,     SpecCor = 0x2   } |
|  | 坐标系选择 更多... |
|  | |
| enum | OutputAngleRangeEnum {     RangeSegment = 0x0,     RangeLinear = 0x1   } |
|  | 输出角度范围 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| List< Line > | InputLine `[set]` |
|  | 输入直线 更多... |
|  | |
| List< float > | CalibMatrix `[set]` |
|  | 标定矩阵 更多... |
|  | |
| ChooseCoordinateEnum | ChooseCoordinate `[get, set]` |
|  | 坐标系选择 更多... |
|  | |
| OutputAngleRangeEnum | OutputAngleRange `[get, set]` |
|  | 输出角度范围 更多... |
|  | |
| bool | AngleLimitEnable `[get, set]` |
|  | 角度判断 更多... |
|  | |
| double | AngleLimitLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | DistPerpendLimitEnable `[get, set]` |
|  | 垂直距离判断 更多... |
|  | |
| double | DistPerpendLimitLow `[get, set]` |
|  | 垂直距离范围，范围：[0,99999] 更多... |
|  | |
| double | DistPerpendLimitHigh `[get, set]` |
|  | 垂直距离范围，范围：[0,99999] 更多... |
|  | |
| bool | ProjXLimitEnable `[get, set]` |
|  | 垂点X判断 更多... |
|  | |
| double | ProjXLimitLow `[get, set]` |
|  | 垂点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | ProjXLimitHigh `[get, set]` |
|  | 垂点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | ProjYLimitEnable `[get, set]` |
|  | 垂点Y判断 更多... |
|  | |
| double | ProjYLimitLow `[get, set]` |
|  | 垂点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | ProjYLimitHigh `[get, set]` |
|  | 垂点Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | DistMinLimitEnable `[get, set]` |
|  | 最近距离判断 更多... |
|  | |
| double | DistMinLimitLow `[get, set]` |
|  | 最近距离范围，范围：[0,99999] 更多... |
|  | |
| double | DistMinLimitHigh `[get, set]` |
|  | 最近距离范围，范围：[0,99999] 更多... |
|  | |
| bool | DistMaxLimitEnable `[get, set]` |
|  | 最远距离判断 更多... |
|  | |
| double | DistMaxLimitLow `[get, set]` |
|  | 最远距离范围，范围：[0,99999] 更多... |
|  | |
| double | DistMaxLimitHigh `[get, set]` |
|  | 最远距离范围，范围：[0,99999] 更多... |
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

点线测量参数

## 成员枚举类型说明

## ◆ ChooseCoordinateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ChooseCoordinateEnum | | strong |

坐标系选择

| 枚举值 | |
| --- | --- |
| ImageCor | 图像坐标系 |
| SpecCor | 特定坐标系 |

## ◆ OutputAngleRangeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum OutputAngleRangeEnum | | strong |

输出角度范围

| 枚举值 | |
| --- | --- |
| RangeSegment | -90°-90° |
| RangeLinear | -180°-180° |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ InputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine | | set |

输入直线

**备注**

仅当次执行起效

## ◆ CalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibMatrix | | set |

标定矩阵

**备注**

仅当次执行起效

## ◆ ChooseCoordinate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ChooseCoordinateEnum ChooseCoordinate | | getset |

坐标系选择

## ◆ OutputAngleRange

|  |  |  |
| --- | --- | --- |
| |  | | --- | | OutputAngleRangeEnum OutputAngleRange | | getset |

输出角度范围

## ◆ AngleLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitEnable | | getset |

角度判断

## ◆ AngleLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitHigh | | getset |

角度范围，范围：[-180,180]

## ◆ DistPerpendLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistPerpendLimitEnable | | getset |

垂直距离判断

## ◆ DistPerpendLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistPerpendLimitLow | | getset |

垂直距离范围，范围：[0,99999]

## ◆ DistPerpendLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistPerpendLimitHigh | | getset |

垂直距离范围，范围：[0,99999]

## ◆ ProjXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ProjXLimitEnable | | getset |

垂点X判断

## ◆ ProjXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProjXLimitLow | | getset |

垂点X范围，范围：[-99999,99999]

## ◆ ProjXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProjXLimitHigh | | getset |

垂点X范围，范围：[-99999,99999]

## ◆ ProjYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ProjYLimitEnable | | getset |

垂点Y判断

## ◆ ProjYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProjYLimitLow | | getset |

垂点Y范围，范围：[-99999,99999]

## ◆ ProjYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProjYLimitHigh | | getset |

垂点Y范围，范围：[-99999,99999]

## ◆ DistMinLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistMinLimitEnable | | getset |

最近距离判断

## ◆ DistMinLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistMinLimitLow | | getset |

最近距离范围，范围：[0,99999]

## ◆ DistMinLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistMinLimitHigh | | getset |

最近距离范围，范围：[0,99999]

## ◆ DistMaxLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistMaxLimitEnable | | getset |

最远距离判断

## ◆ DistMaxLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistMaxLimitLow | | getset |

最远距离范围，范围：[0,99999]

## ◆ DistMaxLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistMaxLimitHigh | | getset |

最远距离范围，范围：[0,99999]
