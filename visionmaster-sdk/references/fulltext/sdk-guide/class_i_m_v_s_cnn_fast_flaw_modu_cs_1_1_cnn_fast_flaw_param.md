<!-- src:class_i_m_v_s_cnn_fast_flaw_modu_cs_1_1_cnn_fast_flaw_param.html -->
<!-- path:接口函数 > 深度学习 > DL快速图像分割GPU > CnnFastFlawParam -->
# CnnFastFlawParam类 参考 深度学习 » DL快速图像分割GPU

DL快速图像分割 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnFastFlawRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | CutViaROIEnable `[get, set]` |
|  | 按ROI裁图 更多... |
|  | |
| bool | BatchProcessEnable `[get, set]` |
|  | 批处理使能 更多... |
|  | |
| int | BatchProcessingLevel `[get, set]` |
|  | 批处理等级，范围：[1,32] 更多... |
|  | |
| bool | SODEnable `[get, set]` |
|  | 小目标模式 更多... |
|  | |
| int | XSlidingWinNumOfSOD `[get, set]` |
|  | 横向滑窗数，范围：[1,16] , Range:[1,16] 更多... |
|  | |
| int | YSlidingWinNumOfSOD `[get, set]` |
|  | 纵向滑窗数，范围：[1,16] , Range:[1,16] 更多... |
|  | |
| double | SlidingWinOverlap `[get, set]` |
|  | 滑窗重叠率，范围：[0,0.6] 更多... |
|  | |
| int | MinScore `[get, set]` |
|  | 最小分数，范围：[0,255] 更多... |
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

DL快速图像分割 GPU参数

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
| |  | | --- | | CnnFastFlawRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ LoadModelPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadModelPath | | getset |

模型文件路径

## ◆ SaveModelDataEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveModelDataEnable | | getset |

方案存模型

## ◆ CutViaROIEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CutViaROIEnable | | getset |

按ROI裁图

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

## ◆ SODEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SODEnable | | getset |

小目标模式

## ◆ XSlidingWinNumOfSOD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int XSlidingWinNumOfSOD | | getset |

横向滑窗数，范围：[1,16] , Range:[1,16]

## ◆ YSlidingWinNumOfSOD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int YSlidingWinNumOfSOD | | getset |

纵向滑窗数，范围：[1,16] , Range:[1,16]

## ◆ SlidingWinOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SlidingWinOverlap | | getset |

滑窗重叠率，范围：[0,0.6]

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinScore | | getset |

最小分数，范围：[0,255]
