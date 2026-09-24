<!-- src:class_i_m_v_s_cnn_register_segment_modu_cs_1_1_cnn_register_segment_param.html -->
<!-- path:接口函数 > 边缘学习 > 注册分割GPU > CnnRegisterSegmentParam -->
# CnnRegisterSegmentParam类 参考 边缘学习 » 注册分割GPU

注册分割 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnRegisterSegmentRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | BatchProcessEnable `[get, set]` |
|  | 批处理使能 更多... |
|  | |
| int | BatchProcessingLevel `[get, set]` |
|  | 批处理等级，范围：[1,32] 更多... |
|  | |
| int | MaxObjNum `[get, set]` |
|  | 最大查找个数，范围：[1,1000] 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | MaxOverlap `[get, set]` |
|  | 最大重叠率，范围：[0.01,1.0] 更多... |
|  | |
| int | MaskThresh `[get, set]` |
|  | 掩膜阈值，范围：[1,100] 更多... |
|  | |
| bool | AreaEnable `[get, set]` |
|  | 面积使能 更多... |
|  | |
| int | MinArea `[get, set]` |
|  | 面积范围，范围：[1,16000000] 更多... |
|  | |
| int | MaxArea `[get, set]` |
|  | 面积范围，范围：[1,16000000] 更多... |
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

注册分割 GPU参数

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
| |  | | --- | | CnnRegisterSegmentRoiManager ModuRoiManager | | get |

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

## ◆ MaxObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxObjNum | | getset |

最大查找个数，范围：[1,1000]

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小置信度，范围：[0.01,1.0]

## ◆ MaxOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxOverlap | | getset |

最大重叠率，范围：[0.01,1.0]

## ◆ MaskThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaskThresh | | getset |

掩膜阈值，范围：[1,100]

## ◆ AreaEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AreaEnable | | getset |

面积使能

## ◆ MinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinArea | | getset |

面积范围，范围：[1,16000000]

## ◆ MaxArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxArea | | getset |

面积范围，范围：[1,16000000]

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
