<!-- src:class_i_m_v_s_binary_modu_cs_1_1_image_binary_param.html -->
<!-- path:接口函数 > 图像处理 > 图像二值化 > ImageBinaryParam -->
# ImageBinaryParam类 参考 图像处理 » 图像二值化

图像二值化参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | NonROIPrcTypeEnum {     Zero = 0,     Src = 1   } |
|  | ROI外处理 更多... |
|  | |
| enum | BinaryTypeEnum {     HardThreshold = 0x1,     MeanThreshold = 0x2,     GaussianThreshold = 0x3,     Sauvola = 0x8,     OTSU = 0x4   } |
|  | 二值化类型 更多... |
|  | |
| enum | CompareTypeEnum {     GreaterEq = 0x0,     LessEq = 0x1,     Equal = 0x2,     NotEqual = 0x3   } |
|  | 比较类型 更多... |
|  | |
| enum | SauvolaSegTypeEnum {     Dark = 0x0,     Bright = 0x1   } |
|  | 分割类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageBinaryRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| NonROIPrcTypeEnum | NonROIPrcType `[get, set]` |
|  | ROI外处理 更多... |
|  | |
| BinaryTypeEnum | BinaryType `[get, set]` |
|  | 二值化类型 更多... |
|  | |
| int | LowThreshold `[get, set]` |
|  | 低阈值，范围：[0,255] 更多... |
|  | |
| int | HighThreshold `[get, set]` |
|  | 高阈值，范围：[0,255] 更多... |
|  | |
| int | KernelWidth `[get, set]` |
|  | 滤波核宽度，范围：[1,51] 更多... |
|  | |
| int | KernelHeight `[get, set]` |
|  | 滤波核高度，范围：[1,51] 更多... |
|  | |
| int | GaussKernelSize `[get, set]` |
|  | 高斯滤波核，范围：[1,51] 更多... |
|  | |
| double | GaussSigma `[get, set]` |
|  | 高斯标准差，范围：[0.1,100] 更多... |
|  | |
| CompareTypeEnum | CompareType `[get, set]` |
|  | 比较类型 更多... |
|  | |
| int | ThresholdOffset `[get, set]` |
|  | 阈值偏移量，范围：[-255,255] 更多... |
|  | |
| double | SauvolaAdjustCoef `[get, set]` |
|  | 校正系数，范围：[-1.0,1.0] 更多... |
|  | |
| double | SauvolaRange `[get, set]` |
|  | 动态范围，范围：[0.1,255] 更多... |
|  | |
| SauvolaSegTypeEnum | SauvolaSegType `[get, set]` |
|  | 分割类型 更多... |
|  | |
| int | SauvolaWinWidth `[get, set]` |
|  | 滤波核宽度，范围：[1,100] 更多... |
|  | |
| int | SauvolaWinHeight `[get, set]` |
|  | 滤波核高度，范围：[1,100] 更多... |
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

图像二值化参数

## 成员枚举类型说明

## ◆ NonROIPrcTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum NonROIPrcTypeEnum | | strong |

ROI外处理

| 枚举值 | |
| --- | --- |
| Zero | 黑色 |
| Src | 原图 |

## ◆ BinaryTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum BinaryTypeEnum | | strong |

二值化类型

| 枚举值 | |
| --- | --- |
| HardThreshold | 硬阈值二值化 |
| MeanThreshold | 均值二值化 |
| GaussianThreshold | 高斯二值化 |
| Sauvola | Sauvola二值化 |
| OTSU | 自动 |

## ◆ CompareTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CompareTypeEnum | | strong |

比较类型

| 枚举值 | |
| --- | --- |
| GreaterEq | 大于等于 |
| LessEq | 小于等于 |
| Equal | 等于 |
| NotEqual | 不等于 |

## ◆ SauvolaSegTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SauvolaSegTypeEnum | | strong |

分割类型

| 枚举值 | |
| --- | --- |
| Dark | 暗于背景 |
| Bright | 亮于背景 |

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
| |  | | --- | | ImageBinaryRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ NonROIPrcType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | NonROIPrcTypeEnum NonROIPrcType | | getset |

ROI外处理

## ◆ BinaryType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | BinaryTypeEnum BinaryType | | getset |

二值化类型

## ◆ LowThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LowThreshold | | getset |

低阈值，范围：[0,255]

## ◆ HighThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HighThreshold | | getset |

高阈值，范围：[0,255]

## ◆ KernelWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelWidth | | getset |

滤波核宽度，范围：[1,51]

## ◆ KernelHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelHeight | | getset |

滤波核高度，范围：[1,51]

## ◆ GaussKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GaussKernelSize | | getset |

高斯滤波核，范围：[1,51]

## ◆ GaussSigma

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double GaussSigma | | getset |

高斯标准差，范围：[0.1,100]

## ◆ CompareType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CompareTypeEnum CompareType | | getset |

比较类型

## ◆ ThresholdOffset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ThresholdOffset | | getset |

阈值偏移量，范围：[-255,255]

## ◆ SauvolaAdjustCoef

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SauvolaAdjustCoef | | getset |

校正系数，范围：[-1.0,1.0]

## ◆ SauvolaRange

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SauvolaRange | | getset |

动态范围，范围：[0.1,255]

## ◆ SauvolaSegType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SauvolaSegTypeEnum SauvolaSegType | | getset |

分割类型

## ◆ SauvolaWinWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SauvolaWinWidth | | getset |

滤波核宽度，范围：[1,100]

## ◆ SauvolaWinHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SauvolaWinHeight | | getset |

滤波核高度，范围：[1,100]
