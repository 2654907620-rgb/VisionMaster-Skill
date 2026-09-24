<!-- src:class_i_m_v_s_edge_width_find_modu_cs_1_1_edge_width_find_result.html -->
<!-- path:接口函数 > 测量 > 间距检测 > EdgeWidthFindResult -->
# EdgeWidthFindResult类 参考 测量 » 间距检测

间距检测结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | EdgeStatus `[get]` |
|  | 边缘状态 更多... |
|  | |
| int | CaliperEdgeNum `[get]` |
|  | 边缘个数 更多... |
|  | |
| List< float > | CaliperEdgePairWidth `[get]` |
|  | 测量宽度 更多... |
|  | |
| List< float > | CaliperEdgeScore `[get]` |
|  | 分数 更多... |
|  | |
| List< int > | CaliperEdge0Polarity `[get]` |
|  | 边缘0极性 更多... |
|  | |
| List< float > | CaliperEdge0Bias `[get]` |
|  | 边缘0位置 更多... |
|  | |
| List< PointF > | EdgePoint0 `[get]` |
|  | 边缘点0 更多... |
|  | |
| List< int > | CaliperEdge1Polarity `[get]` |
|  | 边缘1极性 更多... |
|  | |
| List< float > | CaliperEdge1Bias `[get]` |
|  | 边缘1位置 更多... |
|  | |
| List< PointF > | EdgePoint1 `[get]` |
|  | 边缘点1 更多... |
|  | |
| List< PointF > | Line0StartPoint `[get]` |
|  | 直线0起点 更多... |
|  | |
| List< PointF > | Line0EndPoint `[get]` |
|  | 直线0终点 更多... |
|  | |
| List< float > | Line0Angle `[get]` |
|  | 直线0角度 更多... |
|  | |
| List< PointF > | Line1StartPoint `[get]` |
|  | 直线1起点 更多... |
|  | |
| List< PointF > | Line1EndPoint `[get]` |
|  | 直线1终点 更多... |
|  | |
| List< float > | Line1Angle `[get]` |
|  | 直线1角度 更多... |
|  | |
| List< Annulus > | Annulus0 `[get]` |
|  | 圆弧0 更多... |
|  | |
| List< Annulus > | Annulus1 `[get]` |
|  | 圆弧1 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| Annulus | ROIAnnulus `[get]` |
|  | ROI圆弧 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

间距检测结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ EdgeStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeStatus | | get |

边缘状态

## ◆ CaliperEdgeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperEdgeNum | | get |

边缘个数

## ◆ CaliperEdgePairWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CaliperEdgePairWidth | | get |

测量宽度

## ◆ CaliperEdgeScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CaliperEdgeScore | | get |

分数

## ◆ CaliperEdge0Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CaliperEdge0Polarity | | get |

边缘0极性

## ◆ CaliperEdge0Bias

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CaliperEdge0Bias | | get |

边缘0位置

## ◆ EdgePoint0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgePoint0 | | get |

边缘点0

## ◆ CaliperEdge1Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CaliperEdge1Polarity | | get |

边缘1极性

## ◆ CaliperEdge1Bias

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CaliperEdge1Bias | | get |

边缘1位置

## ◆ EdgePoint1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgePoint1 | | get |

边缘点1

## ◆ Line0StartPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line0StartPoint | | get |

直线0起点

## ◆ Line0EndPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line0EndPoint | | get |

直线0终点

## ◆ Line0Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Line0Angle | | get |

直线0角度

## ◆ Line1StartPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line1StartPoint | | get |

直线1起点

## ◆ Line1EndPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line1EndPoint | | get |

直线1终点

## ◆ Line1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Line1Angle | | get |

直线1角度

## ◆ Annulus0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> Annulus0 | | get |

圆弧0

## ◆ Annulus1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> Annulus1 | | get |

圆弧1

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
