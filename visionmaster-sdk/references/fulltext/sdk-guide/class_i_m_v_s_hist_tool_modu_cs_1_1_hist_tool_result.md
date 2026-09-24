<!-- src:class_i_m_v_s_hist_tool_modu_cs_1_1_hist_tool_result.html -->
<!-- path:接口函数 > 测量 > 直方图工具 > HistToolResult -->
# HistToolResult类 参考 测量 » 直方图工具

直方图工具结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | Count `[get]` |
|  | 像素数量 更多... |
|  | |
| int | LumMin `[get]` |
|  | 最小值 更多... |
|  | |
| int | LumMax `[get]` |
|  | 最大值 更多... |
|  | |
| int | LumMedian `[get]` |
|  | 中值 更多... |
|  | |
| int | LumMode `[get]` |
|  | 峰值 更多... |
|  | |
| float | LumMean `[get]` |
|  | 均值 更多... |
|  | |
| float | LumStd `[get]` |
|  | 标准差 更多... |
|  | |
| float | HistContrast `[get]` |
|  | 对比度 更多... |
|  | |
| List< int > | LumHistogram `[get]` |
|  | 直方图 更多... |
|  | |
| List< int > | CumHistogram `[get]` |
|  | 累积直方图 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| Annulus | ROIAnnulus `[get]` |
|  | ROI圆弧 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

直方图工具结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ Count

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Count | | get |

像素数量

## ◆ LumMin

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LumMin | | get |

最小值

## ◆ LumMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LumMax | | get |

最大值

## ◆ LumMedian

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LumMedian | | get |

中值

## ◆ LumMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LumMode | | get |

峰值

## ◆ LumMean

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LumMean | | get |

均值

## ◆ LumStd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LumStd | | get |

标准差

## ◆ HistContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float HistContrast | | get |

对比度

## ◆ LumHistogram

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> LumHistogram | | get |

直方图

## ◆ CumHistogram

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CumHistogram | | get |

累积直方图

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ ROIAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Annulus ROIAnnulus | | get |

ROI圆弧

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜
