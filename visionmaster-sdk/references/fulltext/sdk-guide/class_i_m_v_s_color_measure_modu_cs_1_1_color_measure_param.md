<!-- src:class_i_m_v_s_color_measure_modu_cs_1_1_color_measure_param.html -->
<!-- path:接口函数 > 颜色处理 > 颜色测量 > ColorMeasureParam -->
# ColorMeasureParam类 参考 颜色处理 » 颜色测量

颜色测量参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ColorSpaceEnum {     RGB = 0x1,     HSV = 0x2,     HSI = 0x3   } |
|  | 颜色空间 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ColorMeasureRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| ColorSpaceEnum | ColorSpace `[get, set]` |
|  | 颜色空间 更多... |
|  | |
| bool | C1MaxValueLimitEnable `[get, set]` |
|  | 通道1最大值 更多... |
|  | |
| int | C1MaxValueLimitLow `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| int | C1MaxValueLimitHigh `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| bool | C1MinValueLimitEnable `[get, set]` |
|  | 通道1最小值 更多... |
|  | |
| int | C1MinValueLimitLow `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| int | C1MinValueLimitHigh `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| bool | C1MeanLimitEnable `[get, set]` |
|  | 通道1均值 更多... |
|  | |
| double | C1MeanLimitLow `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| double | C1MeanLimitHigh `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| bool | C1StdLimitEnable `[get, set]` |
|  | 通道1标准差 更多... |
|  | |
| double | C1StdLimitLow `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| double | C1StdLimitHigh `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| bool | C2MaxValueLimitEnable `[get, set]` |
|  | 通道2最大值 更多... |
|  | |
| int | C2MaxValueLimitLow `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| int | C2MaxValueLimitHigh `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| bool | C2MinValueLimitEnable `[get, set]` |
|  | 通道2最小值 更多... |
|  | |
| int | C2MinValueLimitLow `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| int | C2MinValueLimitHigh `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| bool | C2MeanLimitEnable `[get, set]` |
|  | 通道2均值 更多... |
|  | |
| double | C2MeanLimitLow `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| double | C2MeanLimitHigh `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| bool | C2StdLimitEnable `[get, set]` |
|  | 通道2标准差 更多... |
|  | |
| double | C2StdLimitLow `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| double | C2StdLimitHigh `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| bool | C3MaxValueLimitEnable `[get, set]` |
|  | 通道3最大值 更多... |
|  | |
| int | C3MaxValueLimitLow `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| int | C3MaxValueLimitHigh `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| bool | C3MinValueLimitEnable `[get, set]` |
|  | 通道3最小值 更多... |
|  | |
| int | C3MinValueLimitLow `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| int | C3MinValueLimitHigh `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| bool | C3MeanLimitEnable `[get, set]` |
|  | 通道3均值 更多... |
|  | |
| double | C3MeanLimitLow `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| double | C3MeanLimitHigh `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| bool | C3StdLimitEnable `[get, set]` |
|  | 通道3标准差 更多... |
|  | |
| double | C3StdLimitLow `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| double | C3StdLimitHigh `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
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

颜色测量参数

## 成员枚举类型说明

## ◆ ColorSpaceEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ColorSpaceEnum | | strong |

颜色空间

| 枚举值 | |
| --- | --- |
| RGB | RGB |
| HSV | HSV |
| HSI | HSI |

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
| |  | | --- | | ColorMeasureRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ ColorSpace

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ColorSpaceEnum ColorSpace | | getset |

颜色空间

## ◆ C1MaxValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C1MaxValueLimitEnable | | getset |

通道1最大值

## ◆ C1MaxValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C1MaxValueLimitLow | | getset |

最大值范围，范围：[0,255]

## ◆ C1MaxValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C1MaxValueLimitHigh | | getset |

最大值范围，范围：[0,255]

## ◆ C1MinValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C1MinValueLimitEnable | | getset |

通道1最小值

## ◆ C1MinValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C1MinValueLimitLow | | getset |

最小值范围，范围：[0,255]

## ◆ C1MinValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C1MinValueLimitHigh | | getset |

最小值范围，范围：[0,255]

## ◆ C1MeanLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C1MeanLimitEnable | | getset |

通道1均值

## ◆ C1MeanLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C1MeanLimitLow | | getset |

均值范围，范围：[0,255]

## ◆ C1MeanLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C1MeanLimitHigh | | getset |

均值范围，范围：[0,255]

## ◆ C1StdLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C1StdLimitEnable | | getset |

通道1标准差

## ◆ C1StdLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C1StdLimitLow | | getset |

标准差范围，范围：[0,255]

## ◆ C1StdLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C1StdLimitHigh | | getset |

标准差范围，范围：[0,255]

## ◆ C2MaxValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C2MaxValueLimitEnable | | getset |

通道2最大值

## ◆ C2MaxValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C2MaxValueLimitLow | | getset |

最大值范围，范围：[0,255]

## ◆ C2MaxValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C2MaxValueLimitHigh | | getset |

最大值范围，范围：[0,255]

## ◆ C2MinValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C2MinValueLimitEnable | | getset |

通道2最小值

## ◆ C2MinValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C2MinValueLimitLow | | getset |

最小值范围，范围：[0,255]

## ◆ C2MinValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C2MinValueLimitHigh | | getset |

最小值范围，范围：[0,255]

## ◆ C2MeanLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C2MeanLimitEnable | | getset |

通道2均值

## ◆ C2MeanLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C2MeanLimitLow | | getset |

均值范围，范围：[0,255]

## ◆ C2MeanLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C2MeanLimitHigh | | getset |

均值范围，范围：[0,255]

## ◆ C2StdLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C2StdLimitEnable | | getset |

通道2标准差

## ◆ C2StdLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C2StdLimitLow | | getset |

标准差范围，范围：[0,255]

## ◆ C2StdLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C2StdLimitHigh | | getset |

标准差范围，范围：[0,255]

## ◆ C3MaxValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C3MaxValueLimitEnable | | getset |

通道3最大值

## ◆ C3MaxValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C3MaxValueLimitLow | | getset |

最大值范围，范围：[0,255]

## ◆ C3MaxValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C3MaxValueLimitHigh | | getset |

最大值范围，范围：[0,255]

## ◆ C3MinValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C3MinValueLimitEnable | | getset |

通道3最小值

## ◆ C3MinValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C3MinValueLimitLow | | getset |

最小值范围，范围：[0,255]

## ◆ C3MinValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int C3MinValueLimitHigh | | getset |

最小值范围，范围：[0,255]

## ◆ C3MeanLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C3MeanLimitEnable | | getset |

通道3均值

## ◆ C3MeanLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C3MeanLimitLow | | getset |

均值范围，范围：[0,255]

## ◆ C3MeanLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C3MeanLimitHigh | | getset |

均值范围，范围：[0,255]

## ◆ C3StdLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool C3StdLimitEnable | | getset |

通道3标准差

## ◆ C3StdLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C3StdLimitLow | | getset |

标准差范围，范围：[0,255]

## ◆ C3StdLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double C3StdLimitHigh | | getset |

标准差范围，范围：[0,255]
