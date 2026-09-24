<!-- src:class_i_m_v_s_surface_defect_filter_modu_cs_1_1_surface_defect_filter_param.html -->
<!-- path:接口函数 > 缺陷检测 > 表面缺陷滤波 > SurfaceDefectFilterParam -->
# SurfaceDefectFilterParam类 参考 缺陷检测 » 表面缺陷滤波

表面缺陷滤波参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FilterModeEnum {     Precision = 0x1,     Fast = 0x2   } |
|  | 滤波模式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| SurfaceDefectFilterRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FilterModeEnum | FilterMode `[get, set]` |
|  | 滤波模式 更多... |
|  | |
| int | KerWidth `[get, set]` |
|  | 滤波核宽度，范围：[3,51] 更多... |
|  | |
| int | KerHeight `[get, set]` |
|  | 滤波核高度，范围：[3,51] 更多... |
|  | |
| int | KerNum `[get, set]` |
|  | 核的数量，范围：[1,180] 更多... |
|  | |
| int | Sigma `[get, set]` |
|  | 标准差，范围：[10,500] 更多... |
|  | |
| int | Offset `[get, set]` |
|  | 偏移，范围：[0,100000] 更多... |
|  | |
| double | Weight0 `[get, set]` |
|  | 0度权重，范围：[-10.0,10.0] 更多... |
|  | |
| double | Weight1 `[get, set]` |
|  | 30度权重，范围：[-10.0,10.0] 更多... |
|  | |
| double | Weight2 `[get, set]` |
|  | 60度权重，范围：[-10.0,10.0] 更多... |
|  | |
| double | Weight3 `[get, set]` |
|  | 90度权重，范围：[-10.0,10.0] 更多... |
|  | |
| double | Weight4 `[get, set]` |
|  | 120度权重，范围：[-10.0,10.0] 更多... |
|  | |
| double | Weight5 `[get, set]` |
|  | 150度权重，范围：[-10.0,10.0] 更多... |
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

表面缺陷滤波参数

## 成员枚举类型说明

## ◆ FilterModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FilterModeEnum | | strong |

滤波模式

| 枚举值 | |
| --- | --- |
| Precision | 高精度 |
| Fast | 快速 |

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
| |  | | --- | | SurfaceDefectFilterRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FilterMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FilterModeEnum FilterMode | | getset |

滤波模式

## ◆ KerWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KerWidth | | getset |

滤波核宽度，范围：[3,51]

## ◆ KerHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KerHeight | | getset |

滤波核高度，范围：[3,51]

## ◆ KerNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KerNum | | getset |

核的数量，范围：[1,180]

## ◆ Sigma

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Sigma | | getset |

标准差，范围：[10,500]

## ◆ Offset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Offset | | getset |

偏移，范围：[0,100000]

## ◆ Weight0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight0 | | getset |

0度权重，范围：[-10.0,10.0]

## ◆ Weight1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight1 | | getset |

30度权重，范围：[-10.0,10.0]

## ◆ Weight2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight2 | | getset |

60度权重，范围：[-10.0,10.0]

## ◆ Weight3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight3 | | getset |

90度权重，范围：[-10.0,10.0]

## ◆ Weight4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight4 | | getset |

120度权重，范围：[-10.0,10.0]

## ◆ Weight5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Weight5 | | getset |

150度权重，范围：[-10.0,10.0]
