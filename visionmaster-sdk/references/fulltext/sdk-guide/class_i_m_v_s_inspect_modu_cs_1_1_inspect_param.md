<!-- src:class_i_m_v_s_inspect_modu_cs_1_1_inspect_param.html -->
<!-- path:接口函数 > 缺陷检测 > 异常检测 > InspectParam -->
# InspectParam类 参考 缺陷检测 » 异常检测

异常检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | MatchPolarityEnum {     No = 0x0,     Yes = 0x1   } |
|  | 匹配极性 更多... |
|  | |
| enum | RangeScaleTypeEnum {     ScaleRange = 0x0,     ScaleRangeXY = 0x1   } |
|  | 尺度范围类型 更多... |
|  | |
| enum | MatchThresholdFlagEnum {     AutoThreshold = 0x0,     ModelThreshold = 0x1,     ManualThreshold = 0x2   } |
|  | 阈值类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| double | InspectScore `[get, set]` |
|  | 分数阈值，范围：[0.01,0.99] 更多... |
|  | |
| int | DownSampleRate `[get, set]` |
|  | 下采样率，范围：[10,100] 更多... |
|  | |
| double | MatchMinScore `[get, set]` |
|  | 最小匹配分数，范围：[0.1,1.0] 更多... |
|  | |
| MatchPolarityEnum | MatchPolarity `[get, set]` |
|  | 匹配极性 更多... |
|  | |
| int | MatchAngleStart `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | MatchAngleEnd `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| RangeScaleTypeEnum | RangeScaleType `[get, set]` |
|  | 尺度范围类型 更多... |
|  | |
| double | ScaleStart `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleEnd `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleXStart `[get, set]` |
|  | X尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleXEnd `[get, set]` |
|  | X尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleYStart `[get, set]` |
|  | Y尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleYEnd `[get, set]` |
|  | Y尺度范围，范围：[0.1,10] 更多... |
|  | |
| MatchThresholdFlagEnum | MatchThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | MatchThreshold `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| int | MatchExtentRate `[get, set]` |
|  | 延拓阈值，范围：[0,90] 更多... |
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

异常检测参数

## 成员枚举类型说明

## ◆ MatchPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MatchPolarityEnum | | strong |

匹配极性

| 枚举值 | |
| --- | --- |
| No | 不考虑极性 |
| Yes | 考虑极性 |

## ◆ RangeScaleTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RangeScaleTypeEnum | | strong |

尺度范围类型

| 枚举值 | |
| --- | --- |
| ScaleRange | 尺度范围 |
| ScaleRangeXY | 尺度范围XY |

## ◆ MatchThresholdFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MatchThresholdFlagEnum | | strong |

阈值类型

| 枚举值 | |
| --- | --- |
| AutoThreshold | 自动阈值 |
| ModelThreshold | 模板阈值 |
| ManualThreshold | 手动阈值 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InspectScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double InspectScore | | getset |

分数阈值，范围：[0.01,0.99]

## ◆ DownSampleRate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DownSampleRate | | getset |

下采样率，范围：[10,100]

## ◆ MatchMinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchMinScore | | getset |

最小匹配分数，范围：[0.1,1.0]

## ◆ MatchPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchPolarityEnum MatchPolarity | | getset |

匹配极性

## ◆ MatchAngleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchAngleStart | | getset |

角度范围，范围：[-180,180]

## ◆ MatchAngleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchAngleEnd | | getset |

角度范围，范围：[-180,180]

## ◆ RangeScaleType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RangeScaleTypeEnum RangeScaleType | | getset |

尺度范围类型

## ◆ ScaleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleStart | | getset |

尺度范围，范围：[0.1,10]

## ◆ ScaleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleEnd | | getset |

尺度范围，范围：[0.1,10]

## ◆ ScaleXStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleXStart | | getset |

X尺度范围，范围：[0.1,10]

## ◆ ScaleXEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleXEnd | | getset |

X尺度范围，范围：[0.1,10]

## ◆ ScaleYStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleYStart | | getset |

Y尺度范围，范围：[0.1,10]

## ◆ ScaleYEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleYEnd | | getset |

Y尺度范围，范围：[0.1,10]

## ◆ MatchThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchThresholdFlagEnum MatchThresholdFlag | | getset |

阈值类型

## ◆ MatchThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchThreshold | | getset |

边缘阈值，范围：[1,255]

## ◆ MatchExtentRate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchExtentRate | | getset |

延拓阈值，范围：[0,90]
