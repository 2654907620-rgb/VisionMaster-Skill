<!-- src:class_i_m_v_s_cnn_register_presence_detect_modu_cs_1_1_cnn_register_presence_detect_param.html -->
<!-- path:接口函数 > 边缘学习 > 有无检测GPU > CnnRegisterPresenceDetectParam -->
# CnnRegisterPresenceDetectParam类 参考 边缘学习 » 有无检测GPU

有无检测 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnRegisterPresenceDetectRoiManager | ModuRoiManager `[get, set]` |
|  | ROI管理器 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小置信度，范围：[0.01,1.0] 更多... |
|  | |
| bool | OutFilterEnable `[get, set]` |
|  | 边缘筛选使能 更多... |
|  | |
| double | OutFilterScore `[get, set]` |
|  | 最小边缘分数，范围：[0.01,1.0] 更多... |
|  | |
| bool | AreaEnable `[get, set]` |
|  | 面积使能 更多... |
|  | |
| int | MinArea `[get, set]` |
|  | 面积范围，范围：[1,1600000000] 更多... |
|  | |
| int | MaxArea `[get, set]` |
|  | 面积范围，范围：[1,1600000000] 更多... |
|  | |
| bool | WidthEnable `[get, set]` |
|  | 宽度使能 更多... |
|  | |
| int | MinWidth `[get, set]` |
|  | 宽度范围，范围：[1,40000] 更多... |
|  | |
| int | MaxWidth `[get, set]` |
|  | 宽度范围，范围：[1,40000] 更多... |
|  | |
| bool | HeightEnable `[get, set]` |
|  | 高度使能 更多... |
|  | |
| int | MinHeight `[get, set]` |
|  | 高度范围，范围：[1,40000] 更多... |
|  | |
| int | MaxHeight `[get, set]` |
|  | 高度范围，范围：[1,40000] 更多... |
|  | |
| bool | AngleEnable `[get, set]` |
|  | 角度使能 更多... |
|  | |
| int | StartAngle `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | EndAngle `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
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

有无检测 GPU参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CnnRegisterPresenceDetectRoiManager ModuRoiManager | | getset |

ROI管理器

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小置信度，范围：[0.01,1.0]

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

## ◆ AreaEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AreaEnable | | getset |

面积使能

## ◆ MinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinArea | | getset |

面积范围，范围：[1,1600000000]

## ◆ MaxArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxArea | | getset |

面积范围，范围：[1,1600000000]

## ◆ WidthEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool WidthEnable | | getset |

宽度使能

## ◆ MinWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinWidth | | getset |

宽度范围，范围：[1,40000]

## ◆ MaxWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxWidth | | getset |

宽度范围，范围：[1,40000]

## ◆ HeightEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool HeightEnable | | getset |

高度使能

## ◆ MinHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinHeight | | getset |

高度范围，范围：[1,40000]

## ◆ MaxHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxHeight | | getset |

高度范围，范围：[1,40000]

## ◆ AngleEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleEnable | | getset |

角度使能

## ◆ StartAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int StartAngle | | getset |

角度范围，范围：[-180,180]

## ◆ EndAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EndAngle | | getset |

角度范围，范围：[-180,180]

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
