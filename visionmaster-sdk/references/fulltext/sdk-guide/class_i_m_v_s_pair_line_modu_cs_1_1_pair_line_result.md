<!-- src:class_i_m_v_s_pair_line_modu_cs_1_1_pair_line_result.html -->
<!-- path:接口函数 > 定位 > 平行线查找 > PairLineResult -->
# PairLineResult类 参考 定位 » 平行线查找

平行线查找结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | DetectStatus `[get]` |
|  | 检测状态 更多... |
|  | |
| float | LineWidth `[get]` |
|  | 直线宽度 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| Line | EdgeLine0 `[get]` |
|  | 边缘直线0 更多... |
|  | |
| float | Line0Angle `[get]` |
|  | 直线0角度 更多... |
|  | |
| Line | EdgeLine1 `[get]` |
|  | 边缘直线1 更多... |
|  | |
| float | Line1Angle `[get]` |
|  | 直线1角度 更多... |
|  | |
| Line | EdgeMidLine `[get]` |
|  | 边缘中线 更多... |
|  | |
| float | LineMidAngle `[get]` |
|  | 中线角度 更多... |
|  | |
| List< PointF > | Line0ContourPoint `[get]` |
|  | 直线0轮廓点 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< int > | Edge0PointStatus `[get]` |
|  | 边缘0轮廓点状态 更多... |
|  | |
| List< PointF > | Line1ContourPoint `[get]` |
|  | 直线1轮廓点 更多... |
|  | |
| List< int > | Edge1PointStatus `[get]` |
|  | 边缘1轮廓点状态 更多... |
|  | |
| List< PointF > | MidLineCoutourPoint `[get]` |
|  | 中线轮廓点 更多... |
|  | |
| List< int > | EdgeMidPointStatus `[get]` |
|  | 中线轮廓点状态 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
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

平行线查找结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ DetectStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DetectStatus | | get |

检测状态

## ◆ LineWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineWidth | | get |

直线宽度

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜

## ◆ EdgeLine0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine0 | | get |

边缘直线0

## ◆ Line0Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line0Angle | | get |

直线0角度

## ◆ EdgeLine1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine1 | | get |

边缘直线1

## ◆ Line1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line1Angle | | get |

直线1角度

## ◆ EdgeMidLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeMidLine | | get |

边缘中线

## ◆ LineMidAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineMidAngle | | get |

中线角度

## ◆ Line0ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line0ContourPoint | | get |

直线0轮廓点

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ Edge0PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge0PointStatus | | get |

边缘0轮廓点状态

## ◆ Line1ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line1ContourPoint | | get |

直线1轮廓点

## ◆ Edge1PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointStatus | | get |

边缘1轮廓点状态

## ◆ MidLineCoutourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MidLineCoutourPoint | | get |

中线轮廓点

## ◆ EdgeMidPointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeMidPointStatus | | get |

中线轮廓点状态

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

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
