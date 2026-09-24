<!-- src:class_i_m_v_s_image_math_modu_cs_1_1_image_math_param.html -->
<!-- path:接口函数 > 图像处理 > 图像运算 > ImageMathParam -->
# ImageMathParam类 参考 图像处理 » 图像运算

图像运算参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ArithmeticTypeEnum {     Add = 0x1,     Sub = 0x2,     AbsDiff = 0x3,     Max = 0x4,     Min = 0x5,     Average = 0x6,     And = 0x7,     Or = 0x8,     Xor = 0x9,     BiImgLinear = 0xA,     SingleImgLinear = 0xB,     ADDC = 0xC,     SUBC = 0xD,     CSUB = 0xE,     MUL = 0xF,     DIV = 0x10,     DIVC = 0x11,     CDIV = 0x12,     ANDC = 0x13,     ORC = 0x14,     XORC = 0x15,     MAXC = 0x16,     MINC = 0x17,     AVGC = 0x18,     ABS\_DIFFC = 0x19,     ANDNOT = 0x1A,     ORNOT = 0x1B,     ANDNOTC = 0x1C,     ORNOTC = 0x1D,     SUB\_GREATER\_EQ\_BIN = 0x1E,     SUB\_LESS\_EQ\_BIN = 0x1F   } |
|  | 运算类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage1 `[set]` |
|  | 输入图像1 更多... |
|  | |
| ImageBaseData | InputImage2 `[set]` |
|  | 输入图像2 更多... |
|  | |
| double | ImageWeight1 `[get, set]` |
|  | 图像权重1，范围：[0,255] 更多... |
|  | |
| double | ImageOffset1 `[get, set]` |
|  | 图像补偿1，范围：[-255,255] 更多... |
|  | |
| double | ImageWeight2 `[get, set]` |
|  | 图像权重2，范围：[0,255] 更多... |
|  | |
| double | ImageOffset2 `[get, set]` |
|  | 图像补偿2，范围：[-255,255] 更多... |
|  | |
| ImageMathRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| ArithmeticTypeEnum | ArithmeticType `[get, set]` |
|  | 运算类型 更多... |
|  | |
| double | ImageK1 `[get, set]` |
|  | 运算权重1，范围：[0,255] 更多... |
|  | |
| double | ImageK2 `[get, set]` |
|  | 运算权重2，范围：[0,255] 更多... |
|  | |
| double | ImageC `[get, set]` |
|  | 运算补偿，范围：[-255,255] 更多... |
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

图像运算参数

## 成员枚举类型说明

## ◆ ArithmeticTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ArithmeticTypeEnum | | strong |

运算类型

| 枚举值 | |
| --- | --- |
| Add | 图像加 |
| Sub | 图像减 |
| AbsDiff | 图像绝对差 |
| Max | 两者最大值 |
| Min | 两者最小值 |
| Average | 两者均值 |
| And | 图像与 |
| Or | 图像或 |
| Xor | 图像异或 |
| BiImgLinear | k1\*I1+k2\*I2+C |
| SingleImgLinear | k1\*I1+C |
| ADDC | I1+C |
| SUBC | I1-C |
| CSUB | C-I1 |
| MUL | 两幅图像乘 |
| DIV | 两幅图像除 |
| DIVC | I1/C |
| CDIV | C/I1 |
| ANDC | I1&&C |
| ORC | I1||C |
| XORC | I1^C |
| MAXC | 图像和常数最大值 |
| MINC | 图像和常数最小值 |
| AVGC | 图像和常数均值 |
| ABS\_DIFFC | |I1-C| |
| ANDNOT | 两幅图像与非 |
| ORNOT | 两幅图像或非 |
| ANDNOTC | !(I1&&C) |
| ORNOTC | !(I1||C) |
| SUB\_GREATER\_EQ\_BIN | (I1-(I2 + C))>=0?255:0 |
| SUB\_LESS\_EQ\_BIN | (I1-(I2 + C))>=0?0:255 |

## 属性说明

## ◆ InputImage1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage1 | | set |

输入图像1

**备注**

仅当次执行起效

## ◆ InputImage2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage2 | | set |

输入图像2

**备注**

仅当次执行起效

## ◆ ImageWeight1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageWeight1 | | getset |

图像权重1，范围：[0,255]

## ◆ ImageOffset1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageOffset1 | | getset |

图像补偿1，范围：[-255,255]

## ◆ ImageWeight2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageWeight2 | | getset |

图像权重2，范围：[0,255]

## ◆ ImageOffset2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageOffset2 | | getset |

图像补偿2，范围：[-255,255]

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageMathRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ ArithmeticType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ArithmeticTypeEnum ArithmeticType | | getset |

运算类型

## ◆ ImageK1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageK1 | | getset |

运算权重1，范围：[0,255]

## ◆ ImageK2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageK2 | | getset |

运算权重2，范围：[0,255]

## ◆ ImageC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ImageC | | getset |

运算补偿，范围：[-255,255]
