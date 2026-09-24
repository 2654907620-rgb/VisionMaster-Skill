<!-- src:class_i_m_v_s_circle_edge_insp_modu_cs_1_1_circle_edge_insp_result.html -->
<!-- path:接口函数 > 缺陷检测 > 圆弧边缘缺陷检测 > CircleEdgeInspResult -->
# CircleEdgeInspResult类 参考 缺陷检测 » 圆弧边缘缺陷检测

圆弧边缘缺陷检测结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | FlawNum `[get]` |
|  | 缺陷个数 更多... |
|  | |
| List< int > | FlawNums `[get]` |
|  | ROI缺陷个数 更多... |
|  | |
| List< Annulus > | DetectROIAnnulus `[get]` |
|  | 检测圆弧 更多... |
|  | |
| List< RectBox > | FlawRect `[get]` |
|  | 缺陷框 更多... |
|  | |
| List< int > | FlawRectIndex `[get]` |
|  | 缺陷框索引 更多... |
|  | |
| List< float > | DefectSize `[get]` |
|  | 缺陷尺寸 更多... |
|  | |
| List< float > | DefectArea `[get]` |
|  | 缺陷面积 更多... |
|  | |
| List< int > | CaliperStart `[get]` |
|  | 卡尺起始值 更多... |
|  | |
| List< int > | CaliperEnd `[get]` |
|  | 卡尺终止值 更多... |
|  | |
| List< int > | DefectType `[get]` |
|  | 缺陷类型 更多... |
|  | |
| List< RectBox > | DetectROIs `[get]` |
|  | 检测区域 更多... |
|  | |
| List< PointF > | EdgePoints `[get]` |
|  | 边缘点 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< int > | EdgePointNums `[get]` |
|  | ROI边缘点个数 更多... |
|  | |
| List< PointF > | CaliperPoint `[get]` |
|  | 卡尺点 更多... |
|  | |
| List< int > | CalipIdeaPointStatus `[get]` |
|  | 理想卡尺点状态 更多... |
|  | |
| int | CalipIdeaPointNum `[get]` |
|  | 理想卡尺点数量 更多... |
|  | |
| List< int > | CalipIdeaPointNums `[get]` |
|  | ROI理想卡尺点数量 更多... |
|  | |
| Circle | StandardCircle `[get]` |
|  | 标准圆 更多... |
|  | |
| Annulus | StandardAnnulus `[get]` |
|  | 标准圆环 更多... |
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

圆弧边缘缺陷检测结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ FlawNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FlawNum | | get |

缺陷个数

## ◆ FlawNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> FlawNums | | get |

ROI缺陷个数

## ◆ DetectROIAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> DetectROIAnnulus | | get |

检测圆弧

## ◆ FlawRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> FlawRect | | get |

缺陷框

## ◆ FlawRectIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> FlawRectIndex | | get |

缺陷框索引

## ◆ DefectSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DefectSize | | get |

缺陷尺寸

## ◆ DefectArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DefectArea | | get |

缺陷面积

## ◆ CaliperStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CaliperStart | | get |

卡尺起始值

## ◆ CaliperEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CaliperEnd | | get |

卡尺终止值

## ◆ DefectType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> DefectType | | get |

缺陷类型

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | get |

检测区域

## ◆ EdgePoints

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgePoints | | get |

边缘点

## ◆ EdgePointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointStatus | | get |

轮廓点状态

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ EdgePointNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointNums | | get |

ROI边缘点个数

## ◆ CaliperPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CaliperPoint | | get |

卡尺点

## ◆ CalipIdeaPointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CalipIdeaPointStatus | | get |

理想卡尺点状态

## ◆ CalipIdeaPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalipIdeaPointNum | | get |

理想卡尺点数量

## ◆ CalipIdeaPointNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CalipIdeaPointNums | | get |

ROI理想卡尺点数量

## ◆ StandardCircle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Circle StandardCircle | | get |

标准圆

## ◆ StandardAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Annulus StandardAnnulus | | get |

标准圆环

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
