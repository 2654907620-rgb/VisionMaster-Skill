<!-- src:class_i_m_v_s_caliper_corner_modu_cs_1_1_caliper_corner_result.html -->
<!-- path:接口函数 > 定位 > 边缘交点 > CaliperCornerResult -->
# CaliperCornerResult类 参考 定位 » 边缘交点

边缘交点结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| PointF | CaliperCorner `[get]` |
|  | 边缘交点 更多... |
|  | |
| float | CornerAngle `[get]` |
|  | 边缘交点角度 更多... |
|  | |
| Line | EdgeLine1 `[get]` |
|  | 边缘直线1 更多... |
|  | |
| float | Line1Angle `[get]` |
|  | 直线1角度 更多... |
|  | |
| Line | EdgeLine2 `[get]` |
|  | 边缘直线2 更多... |
|  | |
| float | Line2Angle `[get]` |
|  | 直线2角度 更多... |
|  | |
| List< PointF > | Line1ContourPoint `[get]` |
|  | 直线1轮廓点 更多... |
|  | |
| int | Edge1PointNum `[get]` |
|  | 边缘1轮廓点数 更多... |
|  | |
| List< int > | Edge1PointStatus `[get]` |
|  | 边缘1轮廓点状态 更多... |
|  | |
| List< PointF > | Line2ContourPoint `[get]` |
|  | 直线2轮廓点 更多... |
|  | |
| int | Edge2PointNum `[get]` |
|  | 直线2轮廓点数 更多... |
|  | |
| List< int > | Edge2PointStatus `[get]` |
|  | 直线2轮廓点状态 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| RectBox | ROI1 `[get]` |
|  | 检测区域1 更多... |
|  | |
| RectBox | ROI2 `[get]` |
|  | 检测区域2 更多... |
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

边缘交点结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ CaliperCorner

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF CaliperCorner | | get |

边缘交点

## ◆ CornerAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float CornerAngle | | get |

边缘交点角度

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

## ◆ EdgeLine2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine2 | | get |

边缘直线2

## ◆ Line2Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line2Angle | | get |

直线2角度

## ◆ Line1ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line1ContourPoint | | get |

直线1轮廓点

## ◆ Edge1PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge1PointNum | | get |

边缘1轮廓点数

## ◆ Edge1PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointStatus | | get |

边缘1轮廓点状态

## ◆ Line2ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line2ContourPoint | | get |

直线2轮廓点

## ◆ Edge2PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge2PointNum | | get |

直线2轮廓点数

## ◆ Edge2PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge2PointStatus | | get |

直线2轮廓点状态

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜

## ◆ ROI1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI1 | | get |

检测区域1

## ◆ ROI2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI2 | | get |

检测区域2

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
