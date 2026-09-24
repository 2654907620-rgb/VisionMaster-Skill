<!-- src:class_i_m_v_s_cnn_register_multiclass_classification_modu_c_cs_1_1_cnn_register_multiclass_classification_c_param.html -->
<!-- path:接口函数 > 边缘学习 > 多类别分类CPU > CnnRegisterMulticlassClassificationCParam -->
# CnnRegisterMulticlassClassificationCParam类 参考 边缘学习 » 多类别分类CPU

多类别分类 CPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| uint | GetResultCheckNum () |
|  | CH: 获取动态参数组的数量以进行结果判断 | EN: Get the number of dynamic parameter groups to determine results 更多... |
|  | |
| ResultFilterItemParam | GetResultFilterItemParam (string strName) |
|  | 根据索引获取动态参数项以进行结果判断（单例模式） 更多... |
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
| CnnRegisterMulticlassClassificationCRoiManager | ModuRoiManager `[get, set]` |
|  | ROI管理器 更多... |
|  | |
| double | MinimumScore `[get, set]` |
|  | 最小评分，范围：[0,1.0] 更多... |
|  | |
| bool | SimilarityLimitEnable `[get, set]` |
|  | 相似度判断 更多... |
|  | |
| double | SimilarityLimitLow `[get, set]` |
|  | 相似度范围，范围：[0.0,1.0] 更多... |
|  | |
| double | SimilarityLimitHigh `[get, set]` |
|  | 相似度范围，范围：[0.0,1.0] 更多... |
|  | |
| bool | CategoryNameLimitEnable `[get, set]` |
|  | 类别名称判断 更多... |
|  | |
| string | CategoryNameLimit `[get, set]` |
|  | 类别名称 更多... |
|  | |

## 详细描述

多类别分类 CPU参数

## 成员函数说明

## ◆ GetResultCheckNum()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uint GetResultCheckNum | ( |  | ) |  |

CH: 获取动态参数组的数量以进行结果判断 | EN: Get the number of dynamic parameter groups to determine results

## ◆ GetResultFilterItemParam()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ResultFilterItemParam GetResultFilterItemParam | ( | string | *strName* | ) |  |

根据索引获取动态参数项以进行结果判断（单例模式）

参数
:   |  |  |
    | --- | --- |
    | strName | 参数名称即对应序号，如"1" 结果判断动态参数项 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CnnRegisterMulticlassClassificationCRoiManager ModuRoiManager | | getset |

ROI管理器

## ◆ MinimumScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinimumScore | | getset |

最小评分，范围：[0,1.0]

## ◆ SimilarityLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SimilarityLimitEnable | | getset |

相似度判断

## ◆ SimilarityLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SimilarityLimitLow | | getset |

相似度范围，范围：[0.0,1.0]

## ◆ SimilarityLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SimilarityLimitHigh | | getset |

相似度范围，范围：[0.0,1.0]

## ◆ CategoryNameLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CategoryNameLimitEnable | | getset |

类别名称判断

## ◆ CategoryNameLimit

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CategoryNameLimit | | getset |

类别名称
