<!-- src:class_i_m_v_s_shade_correct_modu_cs_1_1_shade_correct_param.html -->
<!-- path:接口函数 > 图像处理 > 阴影校正 > ShadeCorrectParam -->
# ShadeCorrectParam类 参考 图像处理 » 阴影校正

阴影校正参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | DirectionEnum {     X = 0x1,     Y = 0x2,     XY = 0x3   } |
|  | 方向 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ShadeCorrectRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | Ratio `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | Gain `[get, set]` |
|  | 增益，范围：[0,100] 更多... |
|  | |
| int | Offset `[get, set]` |
|  | 亮度校正补偿，范围：[0,255] 更多... |
|  | |
| int | Noise `[get, set]` |
|  | 噪声，范围：[0,255] 更多... |
|  | |
| DirectionEnum | Direction `[get, set]` |
|  | 方向 更多... |
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

阴影校正参数

## 成员枚举类型说明

## ◆ DirectionEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DirectionEnum | | strong |

方向

| 枚举值 | |
| --- | --- |
| X | X |
| Y | Y |
| XY | XY |

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
| |  | | --- | | ShadeCorrectRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ Ratio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Ratio | | getset |

滤波尺寸，范围：[1,50]

## ◆ Gain

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Gain | | getset |

增益，范围：[0,100]

## ◆ Offset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Offset | | getset |

亮度校正补偿，范围：[0,255]

## ◆ Noise

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Noise | | getset |

噪声，范围：[0,255]

## ◆ Direction

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DirectionEnum Direction | | getset |

方向
