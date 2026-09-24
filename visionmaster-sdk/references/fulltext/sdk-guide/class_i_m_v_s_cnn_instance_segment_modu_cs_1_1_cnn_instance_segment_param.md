<!-- src:class_i_m_v_s_cnn_instance_segment_modu_cs_1_1_cnn_instance_segment_param.html -->
<!-- path:接口函数 > 深度学习 > DL实例分割GPU > CnnInstanceSegmentParam -->
# CnnInstanceSegmentParam类 参考 深度学习 » DL实例分割GPU

DL实例分割 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnInstanceSegmentRoiManager | ModuRoiManager `[get]` |
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
| int | MaxObjNum `[get, set]` |
|  | 最大查找个数，范围：[1,255] 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 目标框置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | MaxOverlap `[get, set]` |
|  | 目标框重叠率，范围：[0.01,1.0] 更多... |
|  | |
| double | MaskThresh `[get, set]` |
|  | 掩膜置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | MaskOverlap `[get, set]` |
|  | 掩膜重叠率，范围：[0.01,1.0] 更多... |
|  | |
| bool | OutFilterEnable `[get, set]` |
|  | 边缘筛选使能 更多... |
|  | |
| double | OutFilterScore `[get, set]` |
|  | 最小边缘分数，范围：[0.01,1.0] 更多... |
|  | |
| bool | RenderMaskEnable `[get, set]` |
|  | 渲染输出图像 更多... |
|  | |
| bool | DiffClassNMSEnable `[get, set]` |
|  | 不同类别过滤 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 个数判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 个数范围，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 个数范围，范围：[0,99999] 更多... |
|  | |
| bool | ScoreLimitEnable `[get, set]` |
|  | 置信度判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 置信度范围，范围：[0,1] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 置信度范围，范围：[0,1] 更多... |
|  | |
| bool | ClassLimitEnable `[get, set]` |
|  | 类别号判断 更多... |
|  | |
| int | ClassLimitLow `[get, set]` |
|  | 类别号范围，范围：[0,99999] 更多... |
|  | |
| int | ClassLimitHigh `[get, set]` |
|  | 类别号范围，范围：[0,99999] 更多... |
|  | |
| bool | CategoryNameLimitEnable `[get, set]` |
|  | 类别名称判断 更多... |
|  | |
| string | CategoryNameLimit `[get, set]` |
|  | 类别名称 更多... |
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

DL实例分割 GPU参数

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
| |  | | --- | | CnnInstanceSegmentRoiManager ModuRoiManager | | get |

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

## ◆ MaxObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxObjNum | | getset |

最大查找个数，范围：[1,255]

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

目标框置信度，范围：[0.01,1.0]

## ◆ MaxOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxOverlap | | getset |

目标框重叠率，范围：[0.01,1.0]

## ◆ MaskThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaskThresh | | getset |

掩膜置信度，范围：[0.01,1.0]

## ◆ MaskOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaskOverlap | | getset |

掩膜重叠率，范围：[0.01,1.0]

## ◆ OutFilterEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutFilterEnable | | getset |

边缘筛选使能

## ◆ OutFilterScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double OutFilterScore | | getset |

最小边缘分数，范围：[0.01,1.0]

## ◆ RenderMaskEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RenderMaskEnable | | getset |

渲染输出图像

## ◆ DiffClassNMSEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DiffClassNMSEnable | | getset |

不同类别过滤

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

个数判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

个数范围，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

个数范围，范围：[0,99999]

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

置信度判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

置信度范围，范围：[0,1]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

置信度范围，范围：[0,1]

## ◆ ClassLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ClassLimitEnable | | getset |

类别号判断

## ◆ ClassLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ClassLimitLow | | getset |

类别号范围，范围：[0,99999]

## ◆ ClassLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ClassLimitHigh | | getset |

类别号范围，范围：[0,99999]

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
