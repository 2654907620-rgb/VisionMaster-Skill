<!-- src:class_i_m_v_s_peak_find_modu_cs_1_1_peak_find_param.html -->
<!-- path:接口函数 > 定位 > 顶点检测 > PeakFindParam -->
# PeakFindParam类 参考 定位 » 顶点检测

顶点检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgePolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| PeakFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | ContrastTH `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | ScanWidth `[get, set]` |
|  | 扫描宽度，范围：[1,100] 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
|  | |
| bool | EdgePointXLimitEnable `[get, set]` |
|  | 边缘点X判断 更多... |
|  | |
| double | EdgePointXLimitLow `[get, set]` |
|  | 边缘点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | EdgePointXLimitHigh `[get, set]` |
|  | 边缘点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | EdgePointYLimitEnable `[get, set]` |
|  | 边缘点Y判断 更多... |
|  | |
| double | EdgePointYLimitLow `[get, set]` |
|  | 边缘点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | EdgePointYLimitHigh `[get, set]` |
|  | 边缘点Y范围，范围：[-99999,99999] 更多... |
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

顶点检测参数

## 成员枚举类型说明

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

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
| |  | | --- | | PeakFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ HalfKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalfKernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ ContrastTH

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastTH | | getset |

边缘阈值，范围：[0,255]

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘极性

## ◆ ScanWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ScanWidth | | getset |

扫描宽度，范围：[1,100]

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

数量判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

数量范围，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

数量范围，范围：[0,99999]

## ◆ EdgePointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgePointXLimitEnable | | getset |

边缘点X判断

## ◆ EdgePointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgePointXLimitLow | | getset |

边缘点X范围，范围：[-99999,99999]

## ◆ EdgePointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgePointXLimitHigh | | getset |

边缘点X范围，范围：[-99999,99999]

## ◆ EdgePointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgePointYLimitEnable | | getset |

边缘点Y判断

## ◆ EdgePointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgePointYLimitLow | | getset |

边缘点Y范围，范围：[-99999,99999]

## ◆ EdgePointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgePointYLimitHigh | | getset |

边缘点Y范围，范围：[-99999,99999]
