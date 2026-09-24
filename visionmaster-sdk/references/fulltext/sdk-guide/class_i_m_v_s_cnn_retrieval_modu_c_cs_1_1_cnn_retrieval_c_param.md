<!-- src:class_i_m_v_s_cnn_retrieval_modu_c_cs_1_1_cnn_retrieval_c_param.html -->
<!-- path:接口函数 > 深度学习 > DL图像检索CPU > CnnRetrievalCParam -->
# CnnRetrievalCParam类 参考 深度学习 » DL图像检索CPU

DL图像检索 CPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnRetrievalCRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| string | LoadGalleryFilePath `[get, set]` |
|  | Gallery路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| int | TopClsK `[get, set]` |
|  | 前K个类别，范围：[1,10] 更多... |
|  | |
| double | MinSimilarity `[get, set]` |
|  | 最小相似度，范围：[0.01,1.0] 更多... |
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

DL图像检索 CPU参数

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
| |  | | --- | | CnnRetrievalCRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ LoadModelPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadModelPath | | getset |

模型文件路径

## ◆ LoadGalleryFilePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadGalleryFilePath | | getset |

Gallery路径

## ◆ SaveModelDataEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveModelDataEnable | | getset |

方案存模型

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
