<!-- src:class_i_m_v_s_machine_learning_classifier_modu_cs_1_1_machine_learning_classifier_param.html -->
<!-- path:接口函数 > 识别 > ML分类 > MachineLearningClassifierParam -->
# MachineLearningClassifierParam类 参考 识别 » ML分类

ML分类参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ClassifyTypeEnum {     SVM = 0x0,     RF = 0x1   } |
|  | 分类器类型（弃用） 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| MachineLearningClassifierRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径(跨机模式下仅支持远端路径) 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 个数判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 个数范围，范围：[1,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 个数范围，范围：[1,99999] 更多... |
|  | |
| bool | LabelNameLimitEnable `[get, set]` |
|  | 标签名判断 更多... |
|  | |
| string | LabelNameLimit `[get, set]` |
|  | 标签名 更多... |
|  | |
| int | SvmMaxIter `[get, set]` |
|  | |
| int | SvmEsp `[get, set]` |
|  | 最小迭代误差，范围：[1,100000]（弃用） 更多... |
|  | |
| ClassifyTypeEnum | ClassifyType `[get, set]` |
|  | 分类器类型（弃用） 更多... |
|  | |
| bool | TextureFeature `[get, set]` |
|  | 纹理特征（弃用） 更多... |
|  | |
| bool | HogFeature `[get, set]` |
|  | HOG（弃用） 更多... |
|  | |
| bool | LbpFeature `[get, set]` |
|  | LBP（弃用） 更多... |
|  | |
| bool | GlcmFeature `[get, set]` |
|  | GLCM（弃用） 更多... |
|  | |
| bool | EdgeFeature `[get, set]` |
|  | 边缘密度（弃用） 更多... |
|  | |
| bool | PolarFeature `[get, set]` |
|  | 极坐标投影（弃用） 更多... |
|  | |
| bool | GrayFeature `[get, set]` |
|  | 灰度特征（弃用） 更多... |
|  | |
| bool | GrayRangeFeature `[get, set]` |
|  | 灰度范围（弃用） 更多... |
|  | |
| bool | GrayMeanFeature `[get, set]` |
|  | 灰度均值（弃用） 更多... |
|  | |
| bool | GrayDeviationFeature `[get, set]` |
|  | 灰度方差（弃用） 更多... |
|  | |
| bool | GrayEntropyFeature `[get, set]` |
|  | 灰度能量（弃用） 更多... |
|  | |
| bool | GrayAnisotropyFeature `[get, set]` |
|  | 各向异性（弃用） 更多... |
|  | |
| bool | GrayProjHorFeature `[get, set]` |
|  | 水平投影（弃用） 更多... |
|  | |
| bool | GrayProjVertFeature `[get, set]` |
|  | 垂直投影（弃用） 更多... |
|  | |
| bool | GrayHis `[get, set]` |
|  | 灰度直方图（弃用） 更多... |
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

ML分类参数

## 成员枚举类型说明

## ◆ ClassifyTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ClassifyTypeEnum | | strong |

分类器类型（弃用）

| 枚举值 | |
| --- | --- |
| SVM | SVM分类器 |
| RF | RF分类器 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MachineLearningClassifierRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ LoadModelPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadModelPath | | getset |

模型文件路径(跨机模式下仅支持远端路径)

## ◆ SaveModelDataEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveModelDataEnable | | getset |

方案存模型

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

个数判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

个数范围，范围：[1,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

个数范围，范围：[1,99999]

## ◆ LabelNameLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LabelNameLimitEnable | | getset |

标签名判断

## ◆ LabelNameLimit

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LabelNameLimit | | getset |

标签名

## ◆ SvmMaxIter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SvmMaxIter | | getset |

最大迭代次数，范围：[10,100000]（弃用）

## ◆ SvmEsp

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SvmEsp | | getset |

最小迭代误差，范围：[1,100000]（弃用）

## ◆ ClassifyType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ClassifyTypeEnum ClassifyType | | getset |

分类器类型（弃用）

## ◆ TextureFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TextureFeature | | getset |

纹理特征（弃用）

## ◆ HogFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool HogFeature | | getset |

HOG（弃用）

## ◆ LbpFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LbpFeature | | getset |

LBP（弃用）

## ◆ GlcmFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GlcmFeature | | getset |

GLCM（弃用）

## ◆ EdgeFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgeFeature | | getset |

边缘密度（弃用）

## ◆ PolarFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PolarFeature | | getset |

极坐标投影（弃用）

## ◆ GrayFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayFeature | | getset |

灰度特征（弃用）

## ◆ GrayRangeFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayRangeFeature | | getset |

灰度范围（弃用）

## ◆ GrayMeanFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayMeanFeature | | getset |

灰度均值（弃用）

## ◆ GrayDeviationFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayDeviationFeature | | getset |

灰度方差（弃用）

## ◆ GrayEntropyFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayEntropyFeature | | getset |

灰度能量（弃用）

## ◆ GrayAnisotropyFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayAnisotropyFeature | | getset |

各向异性（弃用）

## ◆ GrayProjHorFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayProjHorFeature | | getset |

水平投影（弃用）

## ◆ GrayProjVertFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayProjVertFeature | | getset |

垂直投影（弃用）

## ◆ GrayHis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayHis | | getset |

灰度直方图（弃用）
