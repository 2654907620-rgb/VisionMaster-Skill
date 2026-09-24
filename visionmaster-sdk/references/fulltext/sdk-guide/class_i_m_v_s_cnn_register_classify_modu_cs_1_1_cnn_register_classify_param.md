<!-- src:class_i_m_v_s_cnn_register_classify_modu_cs_1_1_cnn_register_classify_param.html -->
<!-- path:接口函数 > 边缘学习 > 注册分类GPU > CnnRegisterClassifyParam -->
# CnnRegisterClassifyParam类 参考 边缘学习 » 注册分类GPU

注册分类 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| uint | GetResultCheckNum () |
|  | 获取动态参数组的数量以进行结果判断 更多... |
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
| CnnRegisterClassifyRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | BatchProcessEnable `[get, set]` |
|  | 批处理使能 更多... |
|  | |
| int | BatchProcessingLevel `[get, set]` |
|  | 批处理等级，范围：[1,32] 更多... |
|  | |
| int | TopClsK `[get, set]` |
|  | 前K个类别，范围：[1,10] 更多... |
|  | |
| double | MinSimilarity `[get, set]` |
|  | 最小相似度，范围：[0.01,1.0] 更多... |
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
| bool | SimilarityLimitEnable `[get, set]` |
|  | 相似度判断 更多... |
|  | |
| double | SimilarityLimitLow `[get, set]` |
|  | 相似度范围，范围：[0.0,1.0] 更多... |
|  | |
| double | SimilarityLimitHigh `[get, set]` |
|  | 相似度范围，范围：[0.0,1.0] 更多... |
|  | |
| bool | ImageIndexLimitEnable `[get, set]` |
|  | 图像索引判断 更多... |
|  | |
| int | ImageIndexLimitLow `[get, set]` |
|  | 图像索引范围，范围：[0,1000] 更多... |
|  | |
| int | ImageIndexLimitHigh `[get, set]` |
|  | 图像索引范围，范围：[0,1000] 更多... |
|  | |
| bool | CategoryNameLimitEnable `[get, set]` |
|  | 类别名称判断 更多... |
|  | |
| string | CategoryNameLimit `[get, set]` |
|  | 类别名称 更多... |
|  | |
| string | LoadGalleryFilePath `[get, set]` |
|  | Gallery路径(弃用) 更多... |
|  | |

## 详细描述

注册分类 GPU参数

## 成员函数说明

## ◆ GetResultCheckNum()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uint GetResultCheckNum | ( |  | ) |  |

获取动态参数组的数量以进行结果判断

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
| |  | | --- | | CnnRegisterClassifyRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ BatchProcessEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BatchProcessEnable | | getset |

批处理使能

## ◆ BatchProcessingLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BatchProcessingLevel | | getset |

批处理等级，范围：[1,32]

## ◆ TopClsK

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TopClsK | | getset |

前K个类别，范围：[1,10]

## ◆ MinSimilarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinSimilarity | | getset |

最小相似度，范围：[0.01,1.0]

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

## ◆ ImageIndexLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ImageIndexLimitEnable | | getset |

图像索引判断

## ◆ ImageIndexLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageIndexLimitLow | | getset |

图像索引范围，范围：[0,1000]

## ◆ ImageIndexLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageIndexLimitHigh | | getset |

图像索引范围，范围：[0,1000]

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

## ◆ LoadGalleryFilePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadGalleryFilePath | | getset |

Gallery路径(弃用)
