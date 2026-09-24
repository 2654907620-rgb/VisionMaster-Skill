<!-- src:class_i_m_v_s_fast_feature_match_modu_cs_1_1_fast_feature_match_param.html -->
<!-- path:接口函数 > 定位 > 快速匹配 > FastFeatureMatchParam -->
# FastFeatureMatchParam类 参考 定位 » 快速匹配

快速匹配参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | PolarityEnum {     No = 0x0,     Yes = 0x1   } |
|  | 匹配极性 更多... |
|  | |
| enum | SortTypeEnum {     Score = 0x2,     Angle = 0x3,     X = 0x4,     Y = 0x5,     XY = 0x6,     YX = 0x7   } |
|  | 排序类型 更多... |
|  | |
| enum | MatchThresholdFlagEnum {     Auto = 0x0,     Model = 0x1,     Manual = 0x2   } |
|  | 阈值类型 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | GetModelStatus (int index) |
|  | 获取单个模板选择状态 更多... |
|  | |
| void | SetModelStatus (int index, bool value) |
|  | 设置单个模板选择状态 更多... |
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
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| FastFeatureMatchRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | UseMatchAllMode `[get, set]` |
|  | 全部搜索模式 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小匹配分数，范围：[0,1.0] 更多... |
|  | |
| int | MaxMatchNum `[get, set]` |
|  | 最大匹配个数，范围：[1,50000] 更多... |
|  | |
| PolarityEnum | Polarity `[get, set]` |
|  | 匹配极性 更多... |
|  | |
| int | AngleStart `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | AngleEnd `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | ScaleStart `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | ScaleEnd `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| int | MaxOverlap `[get, set]` |
|  | 最大重叠率，范围：[0,100] 更多... |
|  | |
| SortTypeEnum | SortType `[get, set]` |
|  | 排序类型 更多... |
|  | |
| MatchThresholdFlagEnum | MatchThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | MatchThresholdHigh `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| bool | SpotterFlag `[get, set]` |
|  | 是否考虑噪点 更多... |
|  | |
| int | MatchExtentRate `[get, set]` |
|  | 延拓阈值，范围：[0,90] 更多... |
|  | |
| int | TimeOut `[get, set]` |
|  | 超时控制，范围：[0,10000] 更多... |
|  | |
| bool | OutLineEnable `[get, set]` |
|  | 轮廓使能 更多... |
|  | |
| bool | OKWhenNumIsZero `[get, set]` |
|  | 忽略匹配个数 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
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
| bool | ScaleLimitEnable `[get, set]` |
|  | 尺度判断 更多... |
|  | |
| double | ScaleLimitLow `[get, set]` |
|  | 尺度范围，范围：[0.0,10] 更多... |
|  | |
| double | ScaleLimitHigh `[get, set]` |
|  | 尺度范围，范围：[0.0,10] 更多... |
|  | |
| bool | ScoreLimitEnable `[get, set]` |
|  | 分数判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 分数范围，范围：[0,1] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 分数范围，范围：[0,1] 更多... |
|  | |
| bool | MatchPointXLimitEnable `[get, set]` |
|  | 匹配点X判断 更多... |
|  | |
| double | MatchPointXLimitLow `[get, set]` |
|  | 匹配点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | MatchPointXLimitHigh `[get, set]` |
|  | 匹配点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | MatchPointYLimitEnable `[get, set]` |
|  | 匹配点Y判断 更多... |
|  | |
| double | MatchPointYLimitLow `[get, set]` |
|  | 匹配点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | MatchPointYLimitHigh `[get, set]` |
|  | 匹配点Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | BoxPointXLimitEnable `[get, set]` |
|  | 中心点X判断 更多... |
|  | |
| double | BoxPointXLimitLow `[get, set]` |
|  | 中心点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | BoxPointXLimitHigh `[get, set]` |
|  | 中心点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | BoxPointYLimitEnable `[get, set]` |
|  | 中心点Y判断 更多... |
|  | |
| double | BoxPointYLimitLow `[get, set]` |
|  | 中心点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | BoxPointYLimitHigh `[get, set]` |
|  | 中心点Y范围，范围：[-99999,99999] 更多... |
|  | |

## 详细描述

快速匹配参数

## 成员枚举类型说明

## ◆ PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PolarityEnum | | strong |

匹配极性

| 枚举值 | |
| --- | --- |
| No | 不考虑极性 |
| Yes | 考虑极性 |

## ◆ SortTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortTypeEnum | | strong |

排序类型

| 枚举值 | |
| --- | --- |
| Score | 按分数降序排序 |
| Angle | 按角度降序排序 |
| X | 按X由小到大排序 |
| Y | 按Y由小到大排序 |
| XY | X由小到大，Y由小到大 |
| YX | Y由小到大，X由小到大 |

## ◆ MatchThresholdFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MatchThresholdFlagEnum | | strong |

阈值类型

| 枚举值 | |
| --- | --- |
| Auto | 自动阈值 |
| Model | 模板阈值 |
| Manual | 手动阈值 |

## 成员函数说明

## ◆ GetModelStatus()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool GetModelStatus | ( | int | *index* | ) |  |

获取单个模板选择状态

## ◆ SetModelStatus()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetModelStatus | ( | int | *index*, |
|  |  | bool | *value* |
|  | ) |  |  |

设置单个模板选择状态

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
| |  | | --- | | FastFeatureMatchRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ UseMatchAllMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UseMatchAllMode | | getset |

全部搜索模式

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小匹配分数，范围：[0,1.0]

## ◆ MaxMatchNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxMatchNum | | getset |

最大匹配个数，范围：[1,50000]

## ◆ Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarityEnum Polarity | | getset |

匹配极性

## ◆ AngleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int AngleStart | | getset |

角度范围，范围：[-180,180]

## ◆ AngleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int AngleEnd | | getset |

角度范围，范围：[-180,180]

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

## ◆ MaxOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxOverlap | | getset |

最大重叠率，范围：[0,100]

## ◆ SortType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortTypeEnum SortType | | getset |

排序类型

## ◆ MatchThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchThresholdFlagEnum MatchThresholdFlag | | getset |

阈值类型

## ◆ MatchThresholdHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchThresholdHigh | | getset |

边缘阈值，范围：[1,255]

## ◆ SpotterFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SpotterFlag | | getset |

是否考虑噪点

## ◆ MatchExtentRate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchExtentRate | | getset |

延拓阈值，范围：[0,90]

## ◆ TimeOut

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TimeOut | | getset |

超时控制，范围：[0,10000]

## ◆ OutLineEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutLineEnable | | getset |

轮廓使能

## ◆ OKWhenNumIsZero

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OKWhenNumIsZero | | getset |

忽略匹配个数

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

数量判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

数量范围，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

数量范围，范围：[0,99999]

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

## ◆ ScaleLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScaleLimitEnable | | getset |

尺度判断

## ◆ ScaleLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleLimitLow | | getset |

尺度范围，范围：[0.0,10]

## ◆ ScaleLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleLimitHigh | | getset |

尺度范围，范围：[0.0,10]

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

分数判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

分数范围，范围：[0,1]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

分数范围，范围：[0,1]

## ◆ MatchPointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MatchPointXLimitEnable | | getset |

匹配点X判断

## ◆ MatchPointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchPointXLimitLow | | getset |

匹配点X范围，范围：[-99999,99999]

## ◆ MatchPointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchPointXLimitHigh | | getset |

匹配点X范围，范围：[-99999,99999]

## ◆ MatchPointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MatchPointYLimitEnable | | getset |

匹配点Y判断

## ◆ MatchPointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchPointYLimitLow | | getset |

匹配点Y范围，范围：[-99999,99999]

## ◆ MatchPointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchPointYLimitHigh | | getset |

匹配点Y范围，范围：[-99999,99999]

## ◆ BoxPointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BoxPointXLimitEnable | | getset |

中心点X判断

## ◆ BoxPointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxPointXLimitLow | | getset |

中心点X范围，范围：[-99999,99999]

## ◆ BoxPointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxPointXLimitHigh | | getset |

中心点X范围，范围：[-99999,99999]

## ◆ BoxPointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BoxPointYLimitEnable | | getset |

中心点Y判断

## ◆ BoxPointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxPointYLimitLow | | getset |

中心点Y范围，范围：[-99999,99999]

## ◆ BoxPointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxPointYLimitHigh | | getset |

中心点Y范围，范围：[-99999,99999]
