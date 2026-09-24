<!-- src:class_i_m_v_s_edge_pair_pos_trend_analy_modu_cs_1_1_edge_pair_pos_trend_analy_result.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘对位置趋势分析 > EdgePairPosTrendAnalyResult -->
# EdgePairPosTrendAnalyResult类 参考 缺陷检测 » 边缘对位置趋势分析

边缘对位置趋势分析结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | EdgePairNum `[get]` |
|  | 边缘对个数 更多... |
|  | |
| int | EdgePairPosDetectCount `[get]` |
|  | 边缘对提取总数 更多... |
|  | |
| float | EdgePairPosMinDistance `[get]` |
|  | 边缘对最小距离 更多... |
|  | |
| Line | MinDistMatchedLine `[get]` |
|  | 最小距离拟合直线 更多... |
|  | |
| float | EdgePairPosMaxDistance `[get]` |
|  | 边缘对最大距离 更多... |
|  | |
| Line | MaxDistMatchedLine `[get]` |
|  | 最大距离拟合直线 更多... |
|  | |
| float | EdgePairPosAverageDistance `[get]` |
|  | 边缘对平均距离 更多... |
|  | |
| int | SelEdgePairPosCount `[get]` |
|  | 目标边缘对总数 更多... |
|  | |
| float | SelEdgePairPosMinDistance `[get]` |
|  | 目标边缘对最小距离 更多... |
|  | |
| float | SelEdgePairPosMaxDistance `[get]` |
|  | 目标边缘对最大距离 更多... |
|  | |
| float | SelEdgePairPosAverageDistance `[get]` |
|  | 目标边缘对平均距离 更多... |
|  | |
| int | EdgePairPosCaliperCount `[get]` |
|  | 卡尺数量 更多... |
|  | |
| List< PointF > | RunParam\_EdgePoint0 `[get]` |
|  | 边缘点0 更多... |
|  | |
| List< PointF > | RunParam\_EdgePoint1 `[get]` |
|  | 边缘点1 更多... |
|  | |
| List< PointF > | EdgeMiddlePoint `[get]` |
|  | 边缘中点 更多... |
|  | |
| List< int > | EdgeMiddlePointStatus `[get]` |
|  | 边缘中点状态 更多... |
|  | |
| List< float > | Edge\_Score `[get]` |
|  | 边缘得分 更多... |
|  | |
| List< int > | Edge0\_Polarity `[get]` |
|  | 边缘0极性 更多... |
|  | |
| List< int > | Edge1\_Polarity `[get]` |
|  | 边缘1极性 更多... |
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

边缘对位置趋势分析结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ EdgePairNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePairNum | | get |

边缘对个数

## ◆ EdgePairPosDetectCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePairPosDetectCount | | get |

边缘对提取总数

## ◆ EdgePairPosMinDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePairPosMinDistance | | get |

边缘对最小距离

## ◆ MinDistMatchedLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line MinDistMatchedLine | | get |

最小距离拟合直线

## ◆ EdgePairPosMaxDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePairPosMaxDistance | | get |

边缘对最大距离

## ◆ MaxDistMatchedLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line MaxDistMatchedLine | | get |

最大距离拟合直线

## ◆ EdgePairPosAverageDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EdgePairPosAverageDistance | | get |

边缘对平均距离

## ◆ SelEdgePairPosCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SelEdgePairPosCount | | get |

目标边缘对总数

## ◆ SelEdgePairPosMinDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePairPosMinDistance | | get |

目标边缘对最小距离

## ◆ SelEdgePairPosMaxDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePairPosMaxDistance | | get |

目标边缘对最大距离

## ◆ SelEdgePairPosAverageDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float SelEdgePairPosAverageDistance | | get |

目标边缘对平均距离

## ◆ EdgePairPosCaliperCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePairPosCaliperCount | | get |

卡尺数量

## ◆ RunParam\_EdgePoint0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> RunParam\_EdgePoint0 | | get |

边缘点0

## ◆ RunParam\_EdgePoint1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> RunParam\_EdgePoint1 | | get |

边缘点1

## ◆ EdgeMiddlePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgeMiddlePoint | | get |

边缘中点

## ◆ EdgeMiddlePointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeMiddlePointStatus | | get |

边缘中点状态

## ◆ Edge\_Score

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Edge\_Score | | get |

边缘得分

## ◆ Edge0\_Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge0\_Polarity | | get |

边缘0极性

## ◆ Edge1\_Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1\_Polarity | | get |

边缘1极性

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
