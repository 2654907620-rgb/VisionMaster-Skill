<!-- src:class_i_m_v_s_hist_tool_modu_cs_1_1_hist_tool_param.html -->
<!-- path:接口函数 > 测量 > 直方图工具 > HistToolParam -->
# HistToolParam类 参考 测量 » 直方图工具

直方图工具参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| HistToolRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | CountLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | CountLimitLow `[get, set]` |
|  | 数量范围，范围：[0,999999999] 更多... |
|  | |
| int | CountLimitHigh `[get, set]` |
|  | 数量范围，范围：[0,999999999] 更多... |
|  | |
| bool | MaxValueLimitEnable `[get, set]` |
|  | 最大值判断 更多... |
|  | |
| int | MaxValueLimitLow `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| int | MaxValueLimitHigh `[get, set]` |
|  | 最大值范围，范围：[0,255] 更多... |
|  | |
| bool | MinValueLimitEnable `[get, set]` |
|  | 最小值判断 更多... |
|  | |
| int | MinValueLimitLow `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| int | MinValueLimitHigh `[get, set]` |
|  | 最小值范围，范围：[0,255] 更多... |
|  | |
| bool | MeanLimitEnable `[get, set]` |
|  | 均值判断 更多... |
|  | |
| double | MeanLimitLow `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| double | MeanLimitHigh `[get, set]` |
|  | 均值范围，范围：[0,255] 更多... |
|  | |
| bool | StdLimitEnable `[get, set]` |
|  | 标准差判断 更多... |
|  | |
| double | StdLimitLow `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| double | StdLimitHigh `[get, set]` |
|  | 标准差范围，范围：[0,255] 更多... |
|  | |
| bool | MedianValueLimitEnable `[get, set]` |
|  | 中值判断 更多... |
|  | |
| int | MedianValueLimitLow `[get, set]` |
|  | 中值范围，范围：[0,255] 更多... |
|  | |
| int | MedianValueLimitHigh `[get, set]` |
|  | 中值范围，范围：[0,255] 更多... |
|  | |
| bool | ModeValueLimitEnable `[get, set]` |
|  | 峰值判断 更多... |
|  | |
| int | ModeValueLimitLow `[get, set]` |
|  | 峰值范围，范围：[0,255] 更多... |
|  | |
| int | ModeValueLimitHigh `[get, set]` |
|  | 峰值范围，范围：[0,255] 更多... |
|  | |
| bool | ContrastLimitEnable `[get, set]` |
|  | 对比度判断 更多... |
|  | |
| double | ContrastLimitLow `[get, set]` |
|  | 对比度范围，范围：[0,255] 更多... |
|  | |
| double | ContrastLimitHigh `[get, set]` |
|  | 对比度范围，范围：[0,255] 更多... |
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

直方图工具参数

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
| |  | | --- | | HistToolRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ CountLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CountLimitEnable | | getset |

数量判断

## ◆ CountLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountLimitLow | | getset |

数量范围，范围：[0,999999999]

## ◆ CountLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountLimitHigh | | getset |

数量范围，范围：[0,999999999]

## ◆ MaxValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MaxValueLimitEnable | | getset |

最大值判断

## ◆ MaxValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxValueLimitLow | | getset |

最大值范围，范围：[0,255]

## ◆ MaxValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxValueLimitHigh | | getset |

最大值范围，范围：[0,255]

## ◆ MinValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MinValueLimitEnable | | getset |

最小值判断

## ◆ MinValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinValueLimitLow | | getset |

最小值范围，范围：[0,255]

## ◆ MinValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinValueLimitHigh | | getset |

最小值范围，范围：[0,255]

## ◆ MeanLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MeanLimitEnable | | getset |

均值判断

## ◆ MeanLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MeanLimitLow | | getset |

均值范围，范围：[0,255]

## ◆ MeanLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MeanLimitHigh | | getset |

均值范围，范围：[0,255]

## ◆ StdLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool StdLimitEnable | | getset |

标准差判断

## ◆ StdLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double StdLimitLow | | getset |

标准差范围，范围：[0,255]

## ◆ StdLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double StdLimitHigh | | getset |

标准差范围，范围：[0,255]

## ◆ MedianValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MedianValueLimitEnable | | getset |

中值判断

## ◆ MedianValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MedianValueLimitLow | | getset |

中值范围，范围：[0,255]

## ◆ MedianValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MedianValueLimitHigh | | getset |

中值范围，范围：[0,255]

## ◆ ModeValueLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ModeValueLimitEnable | | getset |

峰值判断

## ◆ ModeValueLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModeValueLimitLow | | getset |

峰值范围，范围：[0,255]

## ◆ ModeValueLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModeValueLimitHigh | | getset |

峰值范围，范围：[0,255]

## ◆ ContrastLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ContrastLimitEnable | | getset |

对比度判断

## ◆ ContrastLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ContrastLimitLow | | getset |

对比度范围，范围：[0,255]

## ◆ ContrastLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ContrastLimitHigh | | getset |

对比度范围，范围：[0,255]
