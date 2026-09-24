<!-- src:class_i_m_v_s_image_normlize_modu_cs_1_1_image_normlize_param.html -->
<!-- path:接口函数 > 图像处理 > 图像归一化 > ImageNormlizeParam -->
# ImageNormlizeParam类 参考 图像处理 » 图像归一化

图像归一化参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | NormlizeTypeEnum {     HistEqual = 0x1,     HistMatch = 0x2,     MeanStd = 0x3   } |
|  | 归一化类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageNormlizeRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| NormlizeTypeEnum | NormlizeType `[get, set]` |
|  | 归一化类型 更多... |
|  | |
| double | MeanVal `[get, set]` |
|  | 均值，范围：[0,255] 更多... |
|  | |
| double | StdVal `[get, set]` |
|  | 标准差，范围：[0.0,255] 更多... |
|  | |
| double | LeftClipPercent `[get, set]` |
|  | 直方图比例，范围：[0.0,1] 更多... |
|  | |
| double | RightClipPercent `[get, set]` |
|  | 直方图比例，范围：[0.0,1] 更多... |
|  | |
| double | DstLeftPos `[get, set]` |
|  | 灰度值范围，范围：[0.0,255] 更多... |
|  | |
| double | DstRightPos `[get, set]` |
|  | 灰度值范围，范围：[0.0,255] 更多... |
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

图像归一化参数

## 成员枚举类型说明

## ◆ NormlizeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum NormlizeTypeEnum | | strong |

归一化类型

| 枚举值 | |
| --- | --- |
| HistEqual | 直方图均衡化 |
| HistMatch | 直方图归一化 |
| MeanStd | 均值标准差归一化 |

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
| |  | | --- | | ImageNormlizeRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ NormlizeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | NormlizeTypeEnum NormlizeType | | getset |

归一化类型

## ◆ MeanVal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MeanVal | | getset |

均值，范围：[0,255]

## ◆ StdVal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double StdVal | | getset |

标准差，范围：[0.0,255]

## ◆ LeftClipPercent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LeftClipPercent | | getset |

直方图比例，范围：[0.0,1]

## ◆ RightClipPercent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RightClipPercent | | getset |

直方图比例，范围：[0.0,1]

## ◆ DstLeftPos

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DstLeftPos | | getset |

灰度值范围，范围：[0.0,255]

## ◆ DstRightPos

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DstRightPos | | getset |

灰度值范围，范围：[0.0,255]
