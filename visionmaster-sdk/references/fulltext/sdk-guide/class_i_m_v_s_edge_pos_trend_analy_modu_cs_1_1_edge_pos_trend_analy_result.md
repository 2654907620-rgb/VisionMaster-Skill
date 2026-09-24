<!-- src:class_i_m_v_s_edge_pos_trend_analy_modu_cs_1_1_edge_pos_trend_analy_result.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘位置趋势分析 > EdgePosTrendAnalyResult -->
# EdgePosTrendAnalyResult类 参考 缺陷检测 » 边缘位置趋势分析

边缘位置趋势分析结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| int | EdgePosDetectCount `[get]` |
|  | 边缘点提取总数 更多... |
|  | |
| float | EdgePosMinDistance `[get]` |
|  | 边缘点最小距离 更多... |
|  | |
| PointF | EdgePosMinDistIndexPoint `[get]` |
|  | 最小距离索引点 更多... |
|  | |
| float | EdgePosMaxDistance `[get]` |
|  | 边缘点最大距离 更多... |
|  | |
| PointF | EdgePosMaxDistIndexPoint `[get]` |
|  | 最大距离索引点 更多... |
|  | |
| float | EdgePosAverageDistance `[get]` |
|  | 边缘点平均距离 更多... |
|  | |
| int | SelEdgePosCount `[get]` |
|  | 目标边缘点总数 更多... |
|  | |
| float | SelEdgePosMinDistance `[get]` |
|  | 目标边缘点最小距离 更多... |
|  | |
| float | SelEdgePosMaxDistance `[get]` |
|  | 目标边缘点最大距离 更多... |
|  | |
| float | SelEdgePosAverageDistance `[get]` |
|  | 目标边缘点平均距离 更多... |
|  | |
| int | EdgePosCaliperCount `[get]` |
|  | 卡尺数量 更多... |
|  | |
| List< PointF > | RunParam\_EdgePoint `[get]` |
|  | 边缘点 更多... |
|  | |
| List< float > | Edge\_Score `[get]` |
|  | 边缘得分 更多... |
|  | |
| List< int > | EdgePolarity `[get]` |
|  | 边缘极性 更多... |
|  | |
| List< float > | EdgeDist `[get]` |
|  | 边缘距离 更多... |
|  | |
| List< int > | Edge\_Point\_Search\_Status `[get]` |
|  | 边缘点查找状态 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

边缘位置趋势分析结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ EdgePosDetectCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePosDetectCount | | get |

边缘点提取总数

## ◆ EdgePosMinDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePosMinDistance | | get |

边缘点最小距离

## ◆ EdgePosMinDistIndexPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF EdgePosMinDistIndexPoint | | get |

最小距离索引点

## ◆ EdgePosMaxDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePosMaxDistance | | get |

边缘点最大距离

## ◆ EdgePosMaxDistIndexPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF EdgePosMaxDistIndexPoint | | get |

最大距离索引点

## ◆ EdgePosAverageDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePosAverageDistance | | get |

边缘点平均距离

## ◆ SelEdgePosCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SelEdgePosCount | | get |

目标边缘点总数

## ◆ SelEdgePosMinDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePosMinDistance | | get |

目标边缘点最小距离

## ◆ SelEdgePosMaxDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePosMaxDistance | | get |

目标边缘点最大距离

## ◆ SelEdgePosAverageDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePosAverageDistance | | get |

目标边缘点平均距离

## ◆ EdgePosCaliperCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePosCaliperCount | | get |

卡尺数量

## ◆ RunParam\_EdgePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> RunParam\_EdgePoint | | get |

边缘点

## ◆ Edge\_Score

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Edge\_Score | | get |

边缘得分

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePolarity | | get |

边缘极性

## ◆ EdgeDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgeDist | | get |

边缘距离

## ◆ Edge\_Point\_Search\_Status

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge\_Point\_Search\_Status | | get |

边缘点查找状态

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域
