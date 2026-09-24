<!-- src:class_i_m_v_s_color_extract_modu_cs_1_1_color_extract_param.html -->
<!-- path:接口函数 > 颜色处理 > 颜色抽取 > ColorExtractParam -->
# ColorExtractParam类 参考 颜色处理 » 颜色抽取

颜色抽取参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ColorExtractRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | AreaLimitEnable `[get, set]` |
|  | 颜色面积判断 更多... |
|  | |
| double | AreaLimitLow `[get, set]` |
|  | 面积范围，范围：[0,9999999] 更多... |
|  | |
| double | AreaLimitHigh `[get, set]` |
|  | 面积范围，范围：[0,9999999] 更多... |
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

颜色抽取参数

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
| |  | | --- | | ColorExtractRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ AreaLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AreaLimitEnable | | getset |

颜色面积判断

## ◆ AreaLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AreaLimitLow | | getset |

面积范围，范围：[0,9999999]

## ◆ AreaLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AreaLimitHigh | | getset |

面积范围，范围：[0,9999999]
