<!-- src:class_i_m_v_s_edge_pos_trend_analy_modu_cs_1_1_edge_pos_trend_analy_param.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘位置趋势分析 > EdgePosTrendAnalyParam -->
# EdgePosTrendAnalyParam类 参考 缺陷检测 » 边缘位置趋势分析

边缘位置趋势分析参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FindModeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型 更多... |
|  | |
| enum | EdgePolarityEnum {     B2W = 0x1,     W2B = 0x2,     All = 0x3   } |
|  | 边缘极性 更多... |
|  | |
| enum | DetechOrientEnum {     T2B = 0x1,     L2R = 0x2   } |
|  | 边缘查找方向 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| EdgePosTrendAnalyRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FindModeEnum | FindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| int | CaliperCount `[get, set]` |
|  | 卡尺数量，范围：[1,1000] 更多... |
|  | |
| DetechOrientEnum | DetechOrient `[get, set]` |
|  | 边缘查找方向 更多... |
|  | |
| int | ProjectionLength `[get, set]` |
|  | 卡尺宽度，范围：[1,500] 更多... |
|  | |
| int | DistLow `[get, set]` |
|  | 距离低阈值，范围：[0,10000] 更多... |
|  | |
| bool | DistHighIsAutoEnable `[get, set]` |
|  | 高阈值使能 更多... |
|  | |
| int | DistHigh `[get, set]` |
|  | 距离高阈值，范围：[1,10000] 更多... |
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

边缘位置趋势分析参数

## 成员枚举类型说明

## ◆ FindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条边缘 |
| Last | 最后一条边缘 |

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| B2W | 从黑到白 |
| W2B | 从白到黑 |
| All | 任意极性 |

## ◆ DetechOrientEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DetechOrientEnum | | strong |

边缘查找方向

| 枚举值 | |
| --- | --- |
| T2B | 从上到下 |
| L2R | 从左到右 |

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
| |  | | --- | | EdgePosTrendAnalyRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindModeEnum FindMode | | getset |

边缘类型

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘极性

## ◆ HalfKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalfKernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ EdgeStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeStrength | | getset |

边缘阈值，范围：[1,255]

## ◆ CaliperCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperCount | | getset |

卡尺数量，范围：[1,1000]

## ◆ DetechOrient

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DetechOrientEnum DetechOrient | | getset |

边缘查找方向

## ◆ ProjectionLength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ProjectionLength | | getset |

卡尺宽度，范围：[1,500]

## ◆ DistLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DistLow | | getset |

距离低阈值，范围：[0,10000]

## ◆ DistHighIsAutoEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistHighIsAutoEnable | | getset |

高阈值使能

## ◆ DistHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DistHigh | | getset |

距离高阈值，范围：[1,10000]
