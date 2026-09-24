<!-- src:class_i_m_v_s_multi_image_fusion_modu_cs_1_1_multi_image_fusion_param.html -->
<!-- path:接口函数 > 图像处理 > 多图融合 > MultiImageFusionParam -->
# MultiImageFusionParam类 参考 图像处理 » 多图融合

多图融合参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ResultTypeEnum {     Albedo = 0x1,     Shade = 0x2,     All = 0x3   } |
|  | 输出图像类型 更多... |
|  | |
| enum | DirEnhanceTypeEnum {     None = 0x0,     XDirection = 0x1,     YDirection = 0x2   } |
|  | 方向增强类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< int > | ImageCount `[set]` |
|  | 图像数量 更多... |
|  | |
| ImageBaseData | InImage0 `[set]` |
|  | 输入图像0 更多... |
|  | |
| List< float > | InImage0Distribution `[set]` |
|  | 分布角0 更多... |
|  | |
| List< float > | InImage0Irradiation `[set]` |
|  | 照射角0 更多... |
|  | |
| ImageBaseData | InImage1 `[set]` |
|  | 输入图像1 更多... |
|  | |
| List< float > | InImage1Distribution `[set]` |
|  | 分布角1 更多... |
|  | |
| List< float > | InImage1Irradiation `[set]` |
|  | 照射角1 更多... |
|  | |
| ImageBaseData | InImage2 `[set]` |
|  | 输入图像2 更多... |
|  | |
| List< float > | InImage2Distribution `[set]` |
|  | 分布角2 更多... |
|  | |
| List< float > | InImage2Irradiation `[set]` |
|  | 照射角2 更多... |
|  | |
| ImageBaseData | InImage3 `[set]` |
|  | 输入图像3 更多... |
|  | |
| List< float > | InImage3Distribution `[set]` |
|  | 分布角3 更多... |
|  | |
| List< float > | InImage3Irradiation `[set]` |
|  | 照射角3 更多... |
|  | |
| ImageBaseData | InImage4 `[set]` |
|  | 输入图像4 更多... |
|  | |
| List< float > | InImage4Distribution `[set]` |
|  | 分布角4 更多... |
|  | |
| List< float > | InImage4Irradiation `[set]` |
|  | 照射角4 更多... |
|  | |
| ImageBaseData | InImage5 `[set]` |
|  | 输入图像5 更多... |
|  | |
| List< float > | InImage5Distribution `[set]` |
|  | 分布角5 更多... |
|  | |
| List< float > | InImage5Irradiation `[set]` |
|  | 照射角5 更多... |
|  | |
| ImageBaseData | InImage6 `[set]` |
|  | 输入图像6 更多... |
|  | |
| List< float > | InImage6Distribution `[set]` |
|  | 分布角6 更多... |
|  | |
| List< float > | InImage6Irradiation `[set]` |
|  | 照射角6 更多... |
|  | |
| ImageBaseData | InImage7 `[set]` |
|  | 输入图像7 更多... |
|  | |
| List< float > | InImage7Distribution `[set]` |
|  | 分布角7 更多... |
|  | |
| List< float > | InImage7Irradiation `[set]` |
|  | 照射角7 更多... |
|  | |
| ResultTypeEnum | ResultType `[get, set]` |
|  | 输出图像类型 更多... |
|  | |
| int | KernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| bool | EnhanceEnable `[get, set]` |
|  | 增强使能 更多... |
|  | |
| int | Brightness `[get, set]` |
|  | 背景亮度，范围：[0,255] 更多... |
|  | |
| int | ContrastCoef `[get, set]` |
|  | 对比系数，范围：[1,1000] 更多... |
|  | |
| int | HalationRemoveLevel `[get, set]` |
|  | 光晕去除等级，范围：[0,8] 更多... |
|  | |
| DirEnhanceTypeEnum | DirEnhanceType `[get, set]` |
|  | 方向增强类型 更多... |
|  | |
| int | DirEnhanceLevel `[get, set]` |
|  | 方向增强等级，范围：[1,255] 更多... |
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

多图融合参数

## 成员枚举类型说明

## ◆ ResultTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ResultTypeEnum | | strong |

输出图像类型

| 枚举值 | |
| --- | --- |
| Albedo | 反射 |
| Shade | 阴影 |
| All | 全部 |

## ◆ DirEnhanceTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DirEnhanceTypeEnum | | strong |

方向增强类型

| 枚举值 | |
| --- | --- |
| None | 无 |
| XDirection | X方向 |
| YDirection | Y方向 |

## 属性说明

## ◆ ImageCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ImageCount | | set |

图像数量

**备注**

仅当次执行起效

## ◆ InImage0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage0 | | set |

输入图像0

**备注**

仅当次执行起效

## ◆ InImage0Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage0Distribution | | set |

分布角0

**备注**

仅当次执行起效

## ◆ InImage0Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage0Irradiation | | set |

照射角0

**备注**

仅当次执行起效

## ◆ InImage1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage1 | | set |

输入图像1

**备注**

仅当次执行起效

## ◆ InImage1Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage1Distribution | | set |

分布角1

**备注**

仅当次执行起效

## ◆ InImage1Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage1Irradiation | | set |

照射角1

**备注**

仅当次执行起效

## ◆ InImage2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage2 | | set |

输入图像2

**备注**

仅当次执行起效

## ◆ InImage2Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage2Distribution | | set |

分布角2

**备注**

仅当次执行起效

## ◆ InImage2Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage2Irradiation | | set |

照射角2

**备注**

仅当次执行起效

## ◆ InImage3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage3 | | set |

输入图像3

**备注**

仅当次执行起效

## ◆ InImage3Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage3Distribution | | set |

分布角3

**备注**

仅当次执行起效

## ◆ InImage3Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage3Irradiation | | set |

照射角3

**备注**

仅当次执行起效

## ◆ InImage4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage4 | | set |

输入图像4

**备注**

仅当次执行起效

## ◆ InImage4Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage4Distribution | | set |

分布角4

**备注**

仅当次执行起效

## ◆ InImage4Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage4Irradiation | | set |

照射角4

**备注**

仅当次执行起效

## ◆ InImage5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage5 | | set |

输入图像5

**备注**

仅当次执行起效

## ◆ InImage5Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage5Distribution | | set |

分布角5

**备注**

仅当次执行起效

## ◆ InImage5Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage5Irradiation | | set |

照射角5

**备注**

仅当次执行起效

## ◆ InImage6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage6 | | set |

输入图像6

**备注**

仅当次执行起效

## ◆ InImage6Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage6Distribution | | set |

分布角6

**备注**

仅当次执行起效

## ◆ InImage6Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage6Irradiation | | set |

照射角6

**备注**

仅当次执行起效

## ◆ InImage7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InImage7 | | set |

输入图像7

**备注**

仅当次执行起效

## ◆ InImage7Distribution

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage7Distribution | | set |

分布角7

**备注**

仅当次执行起效

## ◆ InImage7Irradiation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InImage7Irradiation | | set |

照射角7

**备注**

仅当次执行起效

## ◆ ResultType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ResultTypeEnum ResultType | | getset |

输出图像类型

## ◆ KernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ EnhanceEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EnhanceEnable | | getset |

增强使能

## ◆ Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Brightness | | getset |

背景亮度，范围：[0,255]

## ◆ ContrastCoef

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastCoef | | getset |

对比系数，范围：[1,1000]

## ◆ HalationRemoveLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalationRemoveLevel | | getset |

光晕去除等级，范围：[0,8]

## ◆ DirEnhanceType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DirEnhanceTypeEnum DirEnhanceType | | getset |

方向增强类型

## ◆ DirEnhanceLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DirEnhanceLevel | | getset |

方向增强等级，范围：[1,255]
