<!-- src:class_i_m_v_s_line_edge_pair_insp_modu_cs_1_1_line_edge_pair_insp_result.html -->
<!-- path:接口函数 > 缺陷检测 > 直线对缺陷检测 > LineEdgePairInspResult -->
# LineEdgePairInspResult类 参考 缺陷检测 » 直线对缺陷检测

直线对缺陷检测结果
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
| List< PointF > | Edge0Point `[get]` |
|  | 边缘0轮廓点 更多... |
|  | |
| List< int > | Edge0PointStatus `[get]` |
|  | 边缘0轮廓点状态 更多... |
|  | |
| int | Edge0PointNum `[get]` |
|  | 边缘0轮廓点数 更多... |
|  | |
| List< int > | Edge0PointNums `[get]` |
|  | ROI边缘0轮廓点数 更多... |
|  | |
| List< PointF > | Edge1Point `[get]` |
|  | 边缘1轮廓点 更多... |
|  | |
| List< int > | Edge1PointStatus `[get]` |
|  | 边缘1轮廓点状态 更多... |
|  | |
| int | Edge1PointNum `[get]` |
|  | 边缘1轮廓点数 更多... |
|  | |
| List< int > | Edge1PointNums `[get]` |
|  | ROI边缘1轮廓点数 更多... |
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
| List< Line > | StandardLine `[get]` |
|  | 标准直线 更多... |
|  | |
| float | StandardLineAngle `[get]` |
|  | 标准直线角度 更多... |
|  | |
| List< DefectFixture > | DefectGeneralInfos `[get]` |
|  | 缺陷综合信息 更多... |
|  | |
| List< PointF > | MinEdgePoint0s `[get]` |
|  | 最小边缘点0 更多... |
|  | |
| List< int > | MinEdgePolarity0s `[get]` |
|  | 最小边缘点0极性 更多... |
|  | |
| List< PointF > | MinEdgePoint1s `[get]` |
|  | 最小边缘点1 更多... |
|  | |
| List< int > | MinEdgePolarity1s `[get]` |
|  | 最小边缘点1极性 更多... |
|  | |
| List< float > | MinEdgeScores `[get]` |
|  | 最小边缘分数 更多... |
|  | |
| List< float > | MinEdgeDistances `[get]` |
|  | 最小边缘距离 更多... |
|  | |
| List< int > | MinEdgeStatuses `[get]` |
|  | 最小边缘状态 更多... |
|  | |
| List< PointF > | MaxEdgePoint0s `[get]` |
|  | 最大边缘点0 更多... |
|  | |
| List< int > | MaxEdgePolarity0s `[get]` |
|  | 最大边缘点0极性 更多... |
|  | |
| List< PointF > | MaxEdgePoint1s `[get]` |
|  | 最大边缘点1 更多... |
|  | |
| List< int > | MaxEdgePolarity1s `[get]` |
|  | 最大边缘点1极性 更多... |
|  | |
| List< float > | MaxEdgeScores `[get]` |
|  | 最大边缘分数 更多... |
|  | |
| List< float > | MaxEdgeDistances `[get]` |
|  | 最大边缘距离 更多... |
|  | |
| List< int > | MaxEdgeStatuses `[get]` |
|  | 最大边缘状态 更多... |
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
| RectBox | ROI `[get]` |
|  | 检测区域（弃用） 更多... |
|  | |
| DefectFixture | DefectGeneralInfo `[get]` |
|  | 缺陷综合信息（弃用） 更多... |
|  | |
| PointF | MinEdgePoint0 `[get]` |
|  | 最小边缘点0（弃用） 更多... |
|  | |
| int | MinEdgePolarity0 `[get]` |
|  | 最小边缘点0极性（弃用） 更多... |
|  | |
| PointF | MinEdgePoint1 `[get]` |
|  | 最小边缘点1（弃用） 更多... |
|  | |
| int | MinEdgePolarity1 `[get]` |
|  | 最小边缘点1极性（弃用） 更多... |
|  | |
| float | MinEdgeScore `[get]` |
|  | 最小边缘分数（弃用） 更多... |
|  | |
| float | MinEdgeDistance `[get]` |
|  | 最小边缘距离（弃用） 更多... |
|  | |
| int | MinEdgeStatus `[get]` |
|  | 最小边缘状态（弃用） 更多... |
|  | |
| PointF | MaxEdgePoint0 `[get]` |
|  | 最大边缘点0（弃用） 更多... |
|  | |
| int | MaxEdgePolarity0 `[get]` |
|  | 最大边缘点0极性（弃用） 更多... |
|  | |
| PointF | MaxEdgePoint1 `[get]` |
|  | 最大边缘点1（弃用） 更多... |
|  | |
| int | MaxEdgePolarity1 `[get]` |
|  | 最大边缘点1极性（弃用） 更多... |
|  | |
| float | MaxEdgeScore `[get]` |
|  | 最大边缘分数（弃用） 更多... |
|  | |
| float | MaxEdgeDistance `[get]` |
|  | 最大边缘距离（弃用） 更多... |
|  | |
| int | MaxEdgeStatus `[get]` |
|  | 最大边缘状态（弃用） 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

直线对缺陷检测结果

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

## ◆ Edge0Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Edge0Point | | get |

边缘0轮廓点

## ◆ Edge0PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge0PointStatus | | get |

边缘0轮廓点状态

## ◆ Edge0PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge0PointNum | | get |

边缘0轮廓点数

## ◆ Edge0PointNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge0PointNums | | get |

ROI边缘0轮廓点数

## ◆ Edge1Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Edge1Point | | get |

边缘1轮廓点

## ◆ Edge1PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointStatus | | get |

边缘1轮廓点状态

## ◆ Edge1PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge1PointNum | | get |

边缘1轮廓点数

## ◆ Edge1PointNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointNums | | get |

ROI边缘1轮廓点数

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

## ◆ StandardLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> StandardLine | | get |

标准直线

## ◆ StandardLineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float StandardLineAngle | | get |

标准直线角度

## ◆ DefectGeneralInfos

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<DefectFixture> DefectGeneralInfos | | get |

缺陷综合信息

## ◆ MinEdgePoint0s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MinEdgePoint0s | | get |

最小边缘点0

## ◆ MinEdgePolarity0s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MinEdgePolarity0s | | get |

最小边缘点0极性

## ◆ MinEdgePoint1s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MinEdgePoint1s | | get |

最小边缘点1

## ◆ MinEdgePolarity1s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MinEdgePolarity1s | | get |

最小边缘点1极性

## ◆ MinEdgeScores

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MinEdgeScores | | get |

最小边缘分数

## ◆ MinEdgeDistances

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MinEdgeDistances | | get |

最小边缘距离

## ◆ MinEdgeStatuses

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MinEdgeStatuses | | get |

最小边缘状态

## ◆ MaxEdgePoint0s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MaxEdgePoint0s | | get |

最大边缘点0

## ◆ MaxEdgePolarity0s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MaxEdgePolarity0s | | get |

最大边缘点0极性

## ◆ MaxEdgePoint1s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MaxEdgePoint1s | | get |

最大边缘点1

## ◆ MaxEdgePolarity1s

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MaxEdgePolarity1s | | get |

最大边缘点1极性

## ◆ MaxEdgeScores

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MaxEdgeScores | | get |

最大边缘分数

## ◆ MaxEdgeDistances

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MaxEdgeDistances | | get |

最大边缘距离

## ◆ MaxEdgeStatuses

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MaxEdgeStatuses | | get |

最大边缘状态

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

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域（弃用）

## ◆ DefectGeneralInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DefectFixture DefectGeneralInfo | | get |

缺陷综合信息（弃用）

## ◆ MinEdgePoint0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF MinEdgePoint0 | | get |

最小边缘点0（弃用）

## ◆ MinEdgePolarity0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinEdgePolarity0 | | get |

最小边缘点0极性（弃用）

## ◆ MinEdgePoint1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF MinEdgePoint1 | | get |

最小边缘点1（弃用）

## ◆ MinEdgePolarity1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinEdgePolarity1 | | get |

最小边缘点1极性（弃用）

## ◆ MinEdgeScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MinEdgeScore | | get |

最小边缘分数（弃用）

## ◆ MinEdgeDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MinEdgeDistance | | get |

最小边缘距离（弃用）

## ◆ MinEdgeStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinEdgeStatus | | get |

最小边缘状态（弃用）

## ◆ MaxEdgePoint0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF MaxEdgePoint0 | | get |

最大边缘点0（弃用）

## ◆ MaxEdgePolarity0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxEdgePolarity0 | | get |

最大边缘点0极性（弃用）

## ◆ MaxEdgePoint1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF MaxEdgePoint1 | | get |

最大边缘点1（弃用）

## ◆ MaxEdgePolarity1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxEdgePolarity1 | | get |

最大边缘点1极性（弃用）

## ◆ MaxEdgeScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MaxEdgeScore | | get |

最大边缘分数（弃用）

## ◆ MaxEdgeDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MaxEdgeDistance | | get |

最大边缘距离（弃用）

## ◆ MaxEdgeStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxEdgeStatus | | get |

最大边缘状态（弃用）
