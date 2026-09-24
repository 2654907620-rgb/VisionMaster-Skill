<!-- src:class_i_m_v_s_mark_insp_modu_cs_1_1_mark_insp_param.html -->
<!-- path:接口函数 > 弃用 > 字符缺陷检测 > MarkInspParam -->
# MarkInspParam类 参考 弃用 » 字符缺陷检测

字符缺陷检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | NormlizeTypeEnum {     Processless = 0x0,     HistEqualize = 0x1,     HistNormalize = 0x2,     StdDevNormalize = 0x3   } |
|  | 归一化类型 更多... |
|  | |
| enum | MarkModelTypeEnum {     MeanStdDev = 0x1,     Correlation = 0x2   } |
|  | 统计训练方法 更多... |
|  | |
| enum | FlawTypeEnum {     NonNormlize = 0x1,     HistEqual = 0x2,     HistMatch = 0x3   } |
|  | 缺陷类型 更多... |
|  | |
| enum | ExactThresholdFlagEnum {     AutoThreshold = 0x0,     ModelThreshold = 0x1,     ManualThreshold = 0x2   } |
|  | 阈值类型 更多... |
|  | |
| enum | MatchPolarityEnum {     No = 0x0,     Yes = 0x1   } |
|  | 匹配极性 更多... |
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
| MarkInspRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| NormlizeTypeEnum | NormlizeType `[get, set]` |
|  | 归一化类型 更多... |
|  | |
| double | NormLeftPercent `[get, set]` |
|  | 直方图比例，范围：[0.0,1] 更多... |
|  | |
| double | NormRightPercent `[get, set]` |
|  | 直方图比例，范围：[0.0,1] 更多... |
|  | |
| MarkModelTypeEnum | MarkModelType `[get, set]` |
|  | 统计训练方法 更多... |
|  | |
| int | CorreScore `[get, set]` |
|  | 相关分数阈值，范围：[0,100] 更多... |
|  | |
| int | BlockNumX `[get, set]` |
|  | 高度方向区块，范围：[1,5] 更多... |
|  | |
| int | BlockNumY `[get, set]` |
|  | 宽度方向区块，范围：[1,5] 更多... |
|  | |
| double | HighScale `[get, set]` |
|  | 高阈值比例，范围：[0.0,8.0] 更多... |
|  | |
| double | HighOffset `[get, set]` |
|  | 高阈值容忍，范围：[0.0,255.0] 更多... |
|  | |
| double | LowScale `[get, set]` |
|  | 低阈值比例，范围：[0.0,8.0] 更多... |
|  | |
| double | LowOffset `[get, set]` |
|  | 低阈值容忍，范围：[0.0,255.0] 更多... |
|  | |
| FlawTypeEnum | FlawType `[get, set]` |
|  | 缺陷类型 更多... |
|  | |
| bool | ToleranceFlag `[get, set]` |
|  | 容忍度开关 更多... |
|  | |
| int | ToleranceValue `[get, set]` |
|  | 容忍度数值，范围：[1,10] 更多... |
|  | |
| int | AreaThresh `[get, set]` |
|  | 面积大小阈值，范围：[1,1000] 更多... |
|  | |
| double | MatchMarkMinScore `[get, set]` |
|  | 最小匹配分数，范围：[0.1,1.0] 更多... |
|  | |
| int | MatchMarkAngleStart `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | MatchMarkAngleEnd `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| ExactThresholdFlagEnum | ExactThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | ExactThreshold `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| bool | MatchMarkRoughFlag `[get, set]` |
|  | 速度使能 更多... |
|  | |
| double | MatchMarkRoughThresh `[get, set]` |
|  | 速度阈值，范围：[0.1,1.0] 更多... |
|  | |
| bool | MatchCorrectFlag `[get, set]` |
|  | 位置纠正 更多... |
|  | |
| int | MatchToleranceX `[get, set]` |
|  | 宽度方向容忍，范围：[5,200] 更多... |
|  | |
| int | MatchToleranceY `[get, set]` |
|  | 高度方向容忍，范围：[5,200] 更多... |
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
| double | MatchScaleStart `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| double | MatchScaleEnd `[get, set]` |
|  | 尺度范围，范围：[0.1,10] 更多... |
|  | |
| MatchThresholdFlagEnum | MatchThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | MatchThreshold `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| bool | MatchRoughFlag `[get, set]` |
|  | 速度使能 更多... |
|  | |
| double | MatchRoughThresh `[get, set]` |
|  | 速度阈值，范围：[0.0,1.0] 更多... |
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

字符缺陷检测参数

## 成员枚举类型说明

## ◆ NormlizeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum NormlizeTypeEnum | | strong |

归一化类型

| 枚举值 | |
| --- | --- |
| Processless | 不处理 |
| HistEqualize | 直方图均衡化 |
| HistNormalize | 直方图归一化 |
| StdDevNormalize | 均值标准差归一化 |

## ◆ MarkModelTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MarkModelTypeEnum | | strong |

统计训练方法

| 枚举值 | |
| --- | --- |
| MeanStdDev | 均值标准差法 |
| Correlation | 相关法 |

## ◆ FlawTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FlawTypeEnum | | strong |

缺陷类型

| 枚举值 | |
| --- | --- |
| NonNormlize | 亮缺陷 |
| HistEqual | 暗缺陷 |
| HistMatch | 亮暗缺陷 |

## ◆ ExactThresholdFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ExactThresholdFlagEnum | | strong |

阈值类型

| 枚举值 | |
| --- | --- |
| AutoThreshold | 自动阈值 |
| ModelThreshold | 模板阈值 |
| ManualThreshold | 手动阈值 |

## ◆ MatchPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MatchPolarityEnum | | strong |

匹配极性

| 枚举值 | |
| --- | --- |
| No | 不考虑极性 |
| Yes | 考虑极性 |

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

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MarkInspRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ NormlizeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | NormlizeTypeEnum NormlizeType | | getset |

归一化类型

## ◆ NormLeftPercent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double NormLeftPercent | | getset |

直方图比例，范围：[0.0,1]

## ◆ NormRightPercent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double NormRightPercent | | getset |

直方图比例，范围：[0.0,1]

## ◆ MarkModelType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MarkModelTypeEnum MarkModelType | | getset |

统计训练方法

## ◆ CorreScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CorreScore | | getset |

相关分数阈值，范围：[0,100]

## ◆ BlockNumX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlockNumX | | getset |

高度方向区块，范围：[1,5]

## ◆ BlockNumY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlockNumY | | getset |

宽度方向区块，范围：[1,5]

## ◆ HighScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double HighScale | | getset |

高阈值比例，范围：[0.0,8.0]

## ◆ HighOffset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double HighOffset | | getset |

高阈值容忍，范围：[0.0,255.0]

## ◆ LowScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LowScale | | getset |

低阈值比例，范围：[0.0,8.0]

## ◆ LowOffset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LowOffset | | getset |

低阈值容忍，范围：[0.0,255.0]

## ◆ FlawType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FlawTypeEnum FlawType | | getset |

缺陷类型

## ◆ ToleranceFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ToleranceFlag | | getset |

容忍度开关

## ◆ ToleranceValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ToleranceValue | | getset |

容忍度数值，范围：[1,10]

## ◆ AreaThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int AreaThresh | | getset |

面积大小阈值，范围：[1,1000]

## ◆ MatchMarkMinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchMarkMinScore | | getset |

最小匹配分数，范围：[0.1,1.0]

## ◆ MatchMarkAngleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchMarkAngleStart | | getset |

角度范围，范围：[-180,180]

## ◆ MatchMarkAngleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchMarkAngleEnd | | getset |

角度范围，范围：[-180,180]

## ◆ ExactThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ExactThresholdFlagEnum ExactThresholdFlag | | getset |

阈值类型

## ◆ ExactThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExactThreshold | | getset |

边缘阈值，范围：[0,255]

## ◆ MatchMarkRoughFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MatchMarkRoughFlag | | getset |

速度使能

## ◆ MatchMarkRoughThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchMarkRoughThresh | | getset |

速度阈值，范围：[0.1,1.0]

## ◆ MatchCorrectFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MatchCorrectFlag | | getset |

位置纠正

## ◆ MatchToleranceX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchToleranceX | | getset |

宽度方向容忍，范围：[5,200]

## ◆ MatchToleranceY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchToleranceY | | getset |

高度方向容忍，范围：[5,200]

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

## ◆ MatchScaleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchScaleStart | | getset |

尺度范围，范围：[0.1,10]

## ◆ MatchScaleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchScaleEnd | | getset |

尺度范围，范围：[0.1,10]

## ◆ MatchThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchThresholdFlagEnum MatchThresholdFlag | | getset |

阈值类型

## ◆ MatchThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchThreshold | | getset |

边缘阈值，范围：[0,255]

## ◆ MatchRoughFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MatchRoughFlag | | getset |

速度使能

## ◆ MatchRoughThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MatchRoughThresh | | getset |

速度阈值，范围：[0.0,1.0]
