<!-- src:class_i_m_v_s2d_bcr_modu_cs_1_1_bcr2d_param.html -->
<!-- path:接口函数 > 识别 > 二维码识别 > Bcr2dParam -->
# Bcr2dParam类 参考 识别 » 二维码识别

二维码识别参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | PolarityEnum {     dark = 0x0,     bright = 0x1,     both = 0x2   } |
|  | 极性 更多... |
|  | |
| enum | EdgeTypeEnum {     continuous = 0x0,     discrete = 0x1,     allmode = 0x2   } |
|  | 边缘类型 更多... |
|  | |
| enum | MirrorEnum {     Off = 0x0,     On = 0x1,     Both = 0x2   } |
|  | 镜像模式 更多... |
|  | |
| enum | DistortionFlagEnum {     Off = 0x0,     On = 0x1   } |
|  | QR畸变 更多... |
|  | |
| enum | AppModeEnum {     Normal = 0x0,     ProMode = 0x1,     FastMode = 0x2   } |
|  | 应用模式 更多... |
|  | |
| enum | RectangleEnum {     Square = 0x0,     Rectangle = 0x1,     AllMode = 0x2   } |
|  | DM码类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| Bcr2dRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | QRCode `[get, set]` |
|  | QR码 更多... |
|  | |
| bool | DMCode `[get, set]` |
|  | DataMatrix码 更多... |
|  | |
| int | LocCodeNum `[get, set]` |
|  | 二维码个数，范围：[1,1000] 更多... |
|  | |
| PolarityEnum | Polarity `[get, set]` |
|  | 极性 更多... |
|  | |
| EdgeTypeEnum | EdgeType `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| int | SampleLevel `[get, set]` |
|  | 降采样倍数，范围：[1,8] 更多... |
|  | |
| int | MinBarSize `[get, set]` |
|  | 码宽范围，范围：[40,1000] 更多... |
|  | |
| int | MaxBarSize `[get, set]` |
|  | 码宽范围，范围：[40,1000] 更多... |
|  | |
| MirrorEnum | Mirror `[get, set]` |
|  | 镜像模式 更多... |
|  | |
| DistortionFlagEnum | DistortionFlag `[get, set]` |
|  | QR畸变 更多... |
|  | |
| int | WaitingTime `[get, set]` |
|  | 超时退出时间，范围：[0,5000] 更多... |
|  | |
| AppModeEnum | AppMode `[get, set]` |
|  | 应用模式 更多... |
|  | |
| RectangleEnum | Rectangle `[get, set]` |
|  | DM码类型 更多... |
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
| bool | VerifyEnable `[get, set]` |
|  | 字符验证 更多... |
|  | |
| bool | NumVerifyEnable `[get, set]` |
|  | 数字集 更多... |
|  | |
| bool | SmallAlphabetVerify `[get, set]` |
|  | 小写字母集 更多... |
|  | |
| bool | BigAlphabetVerify `[get, set]` |
|  | 大写字母集 更多... |
|  | |
| bool | SpecialCharVerify `[get, set]` |
|  | 特殊字符集 更多... |
|  | |
| bool | UserStringVerify `[get, set]` |
|  | 用户字符验证 更多... |
|  | |
| string | UserString `[get, set]` |
|  | 用户字符 更多... |
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

二维码识别参数

## 成员枚举类型说明

## ◆ PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PolarityEnum | | strong |

极性

| 枚举值 | |
| --- | --- |
| dark | 白底黑码 |
| bright | 黑底白码 |
| both | 任意 |

## ◆ EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeTypeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| continuous | 连续型 |
| discrete | 离散型 |
| allmode | 兼容模式 |

## ◆ MirrorEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MirrorEnum | | strong |

镜像模式

| 枚举值 | |
| --- | --- |
| Off | 非镜像 |
| On | 镜像 |
| Both | 任意 |

## ◆ DistortionFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DistortionFlagEnum | | strong |

QR畸变

| 枚举值 | |
| --- | --- |
| Off | 非畸变 |
| On | 畸变 |

## ◆ AppModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AppModeEnum | | strong |

应用模式

| 枚举值 | |
| --- | --- |
| Normal | 普通模式 |
| ProMode | 专家模式 |
| FastMode | 极速模式 |

## ◆ RectangleEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RectangleEnum | | strong |

DM码类型

| 枚举值 | |
| --- | --- |
| Square | 正方形 |
| Rectangle | 长方形 |
| AllMode | 兼容模式 |

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
| |  | | --- | | Bcr2dRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ QRCode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool QRCode | | getset |

QR码

## ◆ DMCode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DMCode | | getset |

DataMatrix码

## ◆ LocCodeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LocCodeNum | | getset |

二维码个数，范围：[1,1000]

## ◆ Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarityEnum Polarity | | getset |

极性

## ◆ EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeTypeEnum EdgeType | | getset |

边缘类型

## ◆ SampleLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SampleLevel | | getset |

降采样倍数，范围：[1,8]

## ◆ MinBarSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinBarSize | | getset |

码宽范围，范围：[40,1000]

## ◆ MaxBarSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxBarSize | | getset |

码宽范围，范围：[40,1000]

## ◆ Mirror

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MirrorEnum Mirror | | getset |

镜像模式

## ◆ DistortionFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DistortionFlagEnum DistortionFlag | | getset |

QR畸变

## ◆ WaitingTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WaitingTime | | getset |

超时退出时间，范围：[0,5000]

## ◆ AppMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AppModeEnum AppMode | | getset |

应用模式

## ◆ Rectangle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectangleEnum Rectangle | | getset |

DM码类型

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

## ◆ VerifyEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool VerifyEnable | | getset |

字符验证

## ◆ NumVerifyEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumVerifyEnable | | getset |

数字集

## ◆ SmallAlphabetVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SmallAlphabetVerify | | getset |

小写字母集

## ◆ BigAlphabetVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BigAlphabetVerify | | getset |

大写字母集

## ◆ SpecialCharVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SpecialCharVerify | | getset |

特殊字符集

## ◆ UserStringVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UserStringVerify | | getset |

用户字符验证

## ◆ UserString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string UserString | | getset |

用户字符
