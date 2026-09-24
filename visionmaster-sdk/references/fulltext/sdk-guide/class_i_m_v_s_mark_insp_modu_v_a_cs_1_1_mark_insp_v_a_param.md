<!-- src:class_i_m_v_s_mark_insp_modu_v_a_cs_1_1_mark_insp_v_a_param.html -->
<!-- path:接口函数 > 缺陷检测 > 字符缺陷检测VA > MarkInspVAParam -->
# MarkInspVAParam类 参考 缺陷检测 » 字符缺陷检测VA

字符缺陷检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FlawTypeEnum {     BrightDefect = 0x1,     DarkDefect = 0x2,     BothDefect = 0x3   } |
|  | 缺陷类型 更多... |
|  | |
| enum | ExactMatchMatchThresholdFlagEnum {     AutoThreshold = 0x0,     ModelThreshold = 0x1,     ManualThreshold = 0x2   } |
|  | 阈值类型 更多... |
|  | |
| enum | RoughMatchPolarityEnum {     No = 0x0,     Yes = 0x1   } |
|  | 匹配极性 更多... |
|  | |
| enum | RoughMatchMatchThresholdFlagEnum {     AutoThreshold = 0x0,     ModelThreshold = 0x1,     ManualThreshold = 0x2   } |
|  | 阈值类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InheritRunPoint `[set]` |
|  | 运行点 更多... |
|  | |
| List< float > | InheritRunAngle `[set]` |
|  | 运行角度 更多... |
|  | |
| List< float > | InheritRunScaleX `[set]` |
|  | 运行尺度X 更多... |
|  | |
| List< float > | InheritRunScaleY `[set]` |
|  | 运行尺度Y 更多... |
|  | |
| MarkInspVARoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FlawTypeEnum | FlawType `[get, set]` |
|  | 缺陷类型 更多... |
|  | |
| int | BrightThreshold `[get, set]` |
|  | 亮缺陷阈值，范围：[1,250] 更多... |
|  | |
| int | DarkThreshold `[get, set]` |
|  | 暗缺陷阈值，范围：[1,250] 更多... |
|  | |
| double | BrightVarScale `[get, set]` |
|  | 亮缺陷尺度，范围：[0.01,1] 更多... |
|  | |
| double | DarkVarScale `[get, set]` |
|  | 暗缺陷尺度，范围：[0.01,1] 更多... |
|  | |
| int | EdgeTolerance `[get, set]` |
|  | 边缘容忍度，范围：[0,10] 更多... |
|  | |
| int | BlobMinArea `[get, set]` |
|  | 面积大小阈值，范围：[1,9000000] 更多... |
|  | |
| double | ExactMatchMinScore `[get, set]` |
|  | 最小匹配分数，范围：[0.1,1.0] 更多... |
|  | |
| int | ExactMatchAngleStart `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | ExactMatchAngleEnd `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | ExactMatchScaleXStart `[get, set]` |
|  | X尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | ExactMatchScaleXEnd `[get, set]` |
|  | X尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | ExactMatchScaleYStart `[get, set]` |
|  | Y尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | ExactMatchScaleYEnd `[get, set]` |
|  | Y尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| ExactMatchMatchThresholdFlagEnum | ExactMatchMatchThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | ExactMatchMatchThresholdHigh `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| bool | ExactMatchCorrectFlag `[get, set]` |
|  | 位置纠正 更多... |
|  | |
| double | ExactMatchToleranceX `[get, set]` |
|  | 宽度方向容忍，范围：[0.01,10] 更多... |
|  | |
| double | ExactMatchToleranceY `[get, set]` |
|  | 高度方向容忍，范围：[0.01,10] 更多... |
|  | |
| double | RoughMatchMinScore `[get, set]` |
|  | 最小匹配分数，范围：[0.1,1.0] 更多... |
|  | |
| RoughMatchPolarityEnum | RoughMatchPolarity `[get, set]` |
|  | 匹配极性 更多... |
|  | |
| int | RoughMatchAngleStart `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | RoughMatchAngleEnd `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | RoughMatchScaleXStart `[get, set]` |
|  | X尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | RoughMatchScaleXEnd `[get, set]` |
|  | X尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | RoughMatchScaleYStart `[get, set]` |
|  | Y尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| double | RoughMatchScaleYEnd `[get, set]` |
|  | Y尺度范围，范围：[0.5,1.5] 更多... |
|  | |
| RoughMatchMatchThresholdFlagEnum | RoughMatchMatchThresholdFlag `[get, set]` |
|  | 阈值类型 更多... |
|  | |
| int | RoughMatchMatchThresholdHigh `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
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

## ◆ FlawTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FlawTypeEnum | | strong |

缺陷类型

| 枚举值 | |
| --- | --- |
| BrightDefect | 亮缺陷 |
| DarkDefect | 暗缺陷 |
| BothDefect | 亮暗缺陷 |

## ◆ ExactMatchMatchThresholdFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ExactMatchMatchThresholdFlagEnum | | strong |

阈值类型

| 枚举值 | |
| --- | --- |
| AutoThreshold | 自动阈值 |
| ModelThreshold | 模板阈值 |
| ManualThreshold | 手动阈值 |

## ◆ RoughMatchPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RoughMatchPolarityEnum | | strong |

匹配极性

| 枚举值 | |
| --- | --- |
| No | 不考虑极性 |
| Yes | 考虑极性 |

## ◆ RoughMatchMatchThresholdFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RoughMatchMatchThresholdFlagEnum | | strong |

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

## ◆ InheritRunPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InheritRunPoint | | set |

运行点

**备注**

仅当次执行起效

## ◆ InheritRunAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InheritRunAngle | | set |

运行角度

**备注**

仅当次执行起效

## ◆ InheritRunScaleX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InheritRunScaleX | | set |

运行尺度X

**备注**

仅当次执行起效

## ◆ InheritRunScaleY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InheritRunScaleY | | set |

运行尺度Y

**备注**

仅当次执行起效

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MarkInspVARoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FlawType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FlawTypeEnum FlawType | | getset |

缺陷类型

## ◆ BrightThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BrightThreshold | | getset |

亮缺陷阈值，范围：[1,250]

## ◆ DarkThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DarkThreshold | | getset |

暗缺陷阈值，范围：[1,250]

## ◆ BrightVarScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BrightVarScale | | getset |

亮缺陷尺度，范围：[0.01,1]

## ◆ DarkVarScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DarkVarScale | | getset |

暗缺陷尺度，范围：[0.01,1]

## ◆ EdgeTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeTolerance | | getset |

边缘容忍度，范围：[0,10]

## ◆ BlobMinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlobMinArea | | getset |

面积大小阈值，范围：[1,9000000]

## ◆ ExactMatchMinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchMinScore | | getset |

最小匹配分数，范围：[0.1,1.0]

## ◆ ExactMatchAngleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExactMatchAngleStart | | getset |

角度范围，范围：[-180,180]

## ◆ ExactMatchAngleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExactMatchAngleEnd | | getset |

角度范围，范围：[-180,180]

## ◆ ExactMatchScaleXStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchScaleXStart | | getset |

X尺度范围，范围：[0.5,1.5]

## ◆ ExactMatchScaleXEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchScaleXEnd | | getset |

X尺度范围，范围：[0.5,1.5]

## ◆ ExactMatchScaleYStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchScaleYStart | | getset |

Y尺度范围，范围：[0.5,1.5]

## ◆ ExactMatchScaleYEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchScaleYEnd | | getset |

Y尺度范围，范围：[0.5,1.5]

## ◆ ExactMatchMatchThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ExactMatchMatchThresholdFlagEnum ExactMatchMatchThresholdFlag | | getset |

阈值类型

## ◆ ExactMatchMatchThresholdHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExactMatchMatchThresholdHigh | | getset |

边缘阈值，范围：[1,255]

## ◆ ExactMatchCorrectFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ExactMatchCorrectFlag | | getset |

位置纠正

## ◆ ExactMatchToleranceX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchToleranceX | | getset |

宽度方向容忍，范围：[0.01,10]

## ◆ ExactMatchToleranceY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExactMatchToleranceY | | getset |

高度方向容忍，范围：[0.01,10]

## ◆ RoughMatchMinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RoughMatchMinScore | | getset |

最小匹配分数，范围：[0.1,1.0]

## ◆ RoughMatchPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RoughMatchPolarityEnum RoughMatchPolarity | | getset |

匹配极性

## ◆ RoughMatchAngleStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMatchAngleStart | | getset |

角度范围，范围：[-180,180]

## ◆ RoughMatchAngleEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMatchAngleEnd | | getset |

角度范围，范围：[-180,180]

## ◆ RoughMatchScaleXStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RoughMatchScaleXStart | | getset |

X尺度范围，范围：[0.5,1.5]

## ◆ RoughMatchScaleXEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RoughMatchScaleXEnd | | getset |

X尺度范围，范围：[0.5,1.5]

## ◆ RoughMatchScaleYStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RoughMatchScaleYStart | | getset |

Y尺度范围，范围：[0.5,1.5]

## ◆ RoughMatchScaleYEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RoughMatchScaleYEnd | | getset |

Y尺度范围，范围：[0.5,1.5]

## ◆ RoughMatchMatchThresholdFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RoughMatchMatchThresholdFlagEnum RoughMatchMatchThresholdFlag | | getset |

阈值类型

## ◆ RoughMatchMatchThresholdHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMatchMatchThresholdHigh | | getset |

边缘阈值，范围：[1,255]
