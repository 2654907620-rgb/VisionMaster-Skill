<!-- src:class_i_m_v_s_color_transform_modu_cs_1_1_color_transform_param.html -->
<!-- path:接口函数 > 颜色处理 > 颜色转换 > ColorTransformParam -->
# ColorTransformParam类 参考 颜色处理 » 颜色转换

颜色转换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ColorTransformTypeEnum {     RGB2GRAY = 0x1,     RGB2HSV = 0x2,     RGB2HSI = 0x3,     RGB2YUV = 0x4   } |
|  | 转换类型 更多... |
|  | |
| enum | ShowChannelEnum {     FirstChannel = 0x0,     SecondChannel = 0x1,     ThirdChannel = 0x2   } |
|  | 显示通道 更多... |
|  | |
| enum | RGB2GrayTypeEnum {     GeneralRatio = 0x1,     AverageRatio = 0x2,     ChannelMin = 0x3,     ChannelMax = 0x4,     UserRatio = 0x5,     RChannel = 0x6,     BChannel = 0x7,     GChannel = 0x8,     SetRatioNs = 0x9   } |
|  | 转换比例 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ColorTransformTypeEnum | ColorTransformType `[get, set]` |
|  | 转换类型 更多... |
|  | |
| ShowChannelEnum | ShowChannel `[get, set]` |
|  | 显示通道 更多... |
|  | |
| RGB2GrayTypeEnum | RGB2GrayType `[get, set]` |
|  | 转换比例 更多... |
|  | |
| int | Rratio `[get, set]` |
|  | R转换比例，范围：[0,100] 更多... |
|  | |
| int | Gratio `[get, set]` |
|  | G转换比例，范围：[0,100] 更多... |
|  | |
| int | Bratio `[get, set]` |
|  | B转换比例，范围：[0,100] 更多... |
|  | |
| double | RRatioNs `[get, set]` |
|  | R转换比例，范围：[-1000,1000] 更多... |
|  | |
| double | GRatioNs `[get, set]` |
|  | G转换比例，范围：[-1000,1000] 更多... |
|  | |
| double | BRatioNs `[get, set]` |
|  | B转换比例，范围：[-1000,1000] 更多... |
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

颜色转换参数

## 成员枚举类型说明

## ◆ ColorTransformTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ColorTransformTypeEnum | | strong |

转换类型

| 枚举值 | |
| --- | --- |
| RGB2GRAY | RGB转灰度 |
| RGB2HSV | RGB转HSV |
| RGB2HSI | RGB转HSI |
| RGB2YUV | RGB转YUV |

## ◆ ShowChannelEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ShowChannelEnum | | strong |

显示通道

| 枚举值 | |
| --- | --- |
| FirstChannel | 第一通道 |
| SecondChannel | 第二通道 |
| ThirdChannel | 第三通道 |

## ◆ RGB2GrayTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RGB2GrayTypeEnum | | strong |

转换比例

| 枚举值 | |
| --- | --- |
| GeneralRatio | 通用转换比例 |
| AverageRatio | 平均转换比例 |
| ChannelMin | 通道最小值 |
| ChannelMax | 通道最大值 |
| UserRatio | 自设转换比例 |
| RChannel | R通道 |
| BChannel | B通道 |
| GChannel | G通道 |
| SetRatioNs | 无约束转换比例 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ ColorTransformType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ColorTransformTypeEnum ColorTransformType | | getset |

转换类型

## ◆ ShowChannel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ShowChannelEnum ShowChannel | | getset |

显示通道

## ◆ RGB2GrayType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RGB2GrayTypeEnum RGB2GrayType | | getset |

转换比例

## ◆ Rratio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Rratio | | getset |

R转换比例，范围：[0,100]

## ◆ Gratio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Gratio | | getset |

G转换比例，范围：[0,100]

## ◆ Bratio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Bratio | | getset |

B转换比例，范围：[0,100]

## ◆ RRatioNs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RRatioNs | | getset |

R转换比例，范围：[-1000,1000]

## ◆ GRatioNs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double GRatioNs | | getset |

G转换比例，范围：[-1000,1000]

## ◆ BRatioNs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BRatioNs | | getset |

B转换比例，范围：[-1000,1000]
