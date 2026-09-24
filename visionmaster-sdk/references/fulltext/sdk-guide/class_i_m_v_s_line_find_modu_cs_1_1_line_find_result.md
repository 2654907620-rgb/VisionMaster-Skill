<!-- src:class_i_m_v_s_line_find_modu_cs_1_1_line_find_result.html -->
<!-- path:接口函数 > 定位 > 直线查找 > LineFindResult -->
# LineFindResult类 参考 定位 » 直线查找

直线查找结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| Line | OutputLine `[get]` |
|  | 输出直线 更多... |
|  | |
| PointF | Midpoint `[get]` |
|  | 中点 更多... |
|  | |
| float | LineAngle `[get]` |
|  | 直线角度 更多... |
|  | |
| float | LineFitError `[get]` |
|  | 拟合误差 更多... |
|  | |
| List< PointF > | LinearContourPoint `[get]` |
|  | 直线轮廓点 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< RectBox > | CaliperBox `[get]` |
|  | 卡尺框 更多... |
|  | |
| List< RectBox > | DetectCaliperBox `[get]` |
|  | 卡尺框检测区 更多... |
|  | |
| List< int > | BlindPolygonPointNum `[get]` |
|  | 多边形点数 更多... |
|  | |
| List< PointF > | BlindPolygonPoints `[get]` |
|  | 多边形点集 更多... |
|  | |
| List< string > | BlindPolygonString `[get]` |
|  | 屏蔽区字符串 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

直线查找结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ OutputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line OutputLine | | get |

输出直线

## ◆ Midpoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF Midpoint | | get |

中点

## ◆ LineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineAngle | | get |

直线角度

## ◆ LineFitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineFitError | | get |

拟合误差

## ◆ LinearContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> LinearContourPoint | | get |

直线轮廓点

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ EdgePointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointStatus | | get |

轮廓点状态

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ CaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CaliperBox | | get |

卡尺框

## ◆ DetectCaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectCaliperBox | | get |

卡尺框检测区

## ◆ BlindPolygonPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BlindPolygonPointNum | | get |

多边形点数

## ◆ BlindPolygonPoints

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> BlindPolygonPoints | | get |

多边形点集

## ◆ BlindPolygonString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> BlindPolygonString | | get |

屏蔽区字符串
