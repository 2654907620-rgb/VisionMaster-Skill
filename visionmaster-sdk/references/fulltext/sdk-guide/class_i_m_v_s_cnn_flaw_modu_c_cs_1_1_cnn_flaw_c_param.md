<!-- src:class_i_m_v_s_cnn_flaw_modu_c_cs_1_1_cnn_flaw_c_param.html -->
<!-- path:接口函数 > 深度学习 > DL图像分割CPU > CnnFlawCParam -->
# CnnFlawCParam类 参考 深度学习 » DL图像分割CPU

DL图像分割 CPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | AlgRunModeEnum {     HpMode = 0x0,     FastMode = 0x1   } |
|  | 运行模式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnFlawCRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | RoiFromModelEnable `[get, set]` |
|  | 获取模型ROI 更多... |
|  | |
| bool | CutViaROIEnable `[get, set]` |
|  | 按ROI裁图 更多... |
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
| int | SampleInterval `[get, set]` |
|  | 采样系数，范围：[1,6] 更多... |
|  | |
| AlgRunModeEnum | AlgRunMode `[get, set]` |
|  | 运行模式 更多... |
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

DL图像分割 CPU参数

## 成员枚举类型说明

## ◆ AlgRunModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AlgRunModeEnum | | strong |

运行模式

| 枚举值 | |
| --- | --- |
| HpMode | 高性能模式 |
| FastMode | 极速模式 |

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
| |  | | --- | | CnnFlawCRoiManager ModuRoiManager | | get |

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

## ◆ RoiFromModelEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RoiFromModelEnable | | getset |

获取模型ROI

## ◆ CutViaROIEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CutViaROIEnable | | getset |

按ROI裁图

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

## ◆ SampleInterval

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SampleInterval | | getset |

采样系数，范围：[1,6]

## ◆ AlgRunMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AlgRunModeEnum AlgRunMode | | getset |

运行模式

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinScore | | getset |

最小分数，范围：[0,255]
