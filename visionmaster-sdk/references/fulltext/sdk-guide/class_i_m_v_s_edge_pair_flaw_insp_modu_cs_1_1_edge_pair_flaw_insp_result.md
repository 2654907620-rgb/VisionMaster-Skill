<!-- src:class_i_m_v_s_edge_pair_flaw_insp_modu_cs_1_1_edge_pair_flaw_insp_result.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘对模型缺陷检测 > EdgePairFlawInspResult -->
# EdgePairFlawInspResult类 参考 缺陷检测 » 边缘对模型缺陷检测

边缘对模型缺陷检测结果
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
| int | WidthPairNum `[get]` |
|  | 边缘对个数 更多... |
|  | |
| float | MaxWidth `[get]` |
|  | 最大宽度 更多... |
|  | |
| float | MinWidth `[get]` |
|  | 最小宽度 更多... |
|  | |
| float | AvgWidth `[get]` |
|  | 平均宽度 更多... |
|  | |
| List< float > | EdgePairWidth `[get]` |
|  | 边缘对宽度 更多... |
|  | |
| List< RectBox > | CaliperBox `[get]` |
|  | 卡尺框 更多... |
|  | |
| List< RectBox > | DefectBox `[get]` |
|  | 缺陷框 更多... |
|  | |
| List< int > | DefectCaliperStart `[get]` |
|  | 缺陷卡尺起始索引 更多... |
|  | |
| List< int > | DefectCaliperEnd `[get]` |
|  | 缺陷卡尺终止索引 更多... |
|  | |
| List< int > | DefectType `[get]` |
|  | 缺陷类型 更多... |
|  | |
| List< float > | FlawLen `[get]` |
|  | 缺陷长度 更多... |
|  | |
| List< PointF > | Edge0Point `[get]` |
|  | 边缘0轮廓点 更多... |
|  | |
| List< PointF > | Edge1Point `[get]` |
|  | 边缘1轮廓点 更多... |
|  | |
| List< PointF > | EdgeMiddlePoint `[get]` |
|  | 边缘中点 更多... |
|  | |
| List< int > | Edge0PointStatus `[get]` |
|  | 边缘0轮廓点状态 更多... |
|  | |
| List< int > | Edge1PointStatus `[get]` |
|  | 边缘1轮廓点状态 更多... |
|  | |
| List< int > | EdgeMiddlePointStatus `[get]` |
|  | 边缘中点状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< PointF > | IdeaEdge0Point `[get]` |
|  | 理想边缘0边缘点 更多... |
|  | |
| List< PointF > | IdeaEdge1Point `[get]` |
|  | 理想边缘1边缘点 更多... |
|  | |
| List< PointF > | CalTrajPoint `[get]` |
|  | 优化轨迹点 更多... |
|  | |
| List< PointF > | IdeaTrajPoint `[get]` |
|  | 理想轨迹点 更多... |
|  | |
| List< RectBox > | IdeaTrajCaliper `[get]` |
|  | 理想轨迹卡尺 更多... |
|  | |
| List< int > | CalTrajFlag `[get]` |
|  | 优化轨迹状态 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

边缘对模型缺陷检测结果

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

## ◆ WidthPairNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WidthPairNum | | get |

边缘对个数

## ◆ MaxWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MaxWidth | | get |

最大宽度

## ◆ MinWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MinWidth | | get |

最小宽度

## ◆ AvgWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float AvgWidth | | get |

平均宽度

## ◆ EdgePairWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgePairWidth | | get |

边缘对宽度

## ◆ CaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CaliperBox | | get |

卡尺框

## ◆ DefectBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DefectBox | | get |

缺陷框

## ◆ DefectCaliperStart

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> DefectCaliperStart | | get |

缺陷卡尺起始索引

## ◆ DefectCaliperEnd

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> DefectCaliperEnd | | get |

缺陷卡尺终止索引

## ◆ DefectType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> DefectType | | get |

缺陷类型

## ◆ FlawLen

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> FlawLen | | get |

缺陷长度

## ◆ Edge0Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Edge0Point | | get |

边缘0轮廓点

## ◆ Edge1Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Edge1Point | | get |

边缘1轮廓点

## ◆ EdgeMiddlePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgeMiddlePoint | | get |

边缘中点

## ◆ Edge0PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge0PointStatus | | get |

边缘0轮廓点状态

## ◆ Edge1PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointStatus | | get |

边缘1轮廓点状态

## ◆ EdgeMiddlePointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeMiddlePointStatus | | get |

边缘中点状态

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ IdeaEdge0Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> IdeaEdge0Point | | get |

理想边缘0边缘点

## ◆ IdeaEdge1Point

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> IdeaEdge1Point | | get |

理想边缘1边缘点

## ◆ CalTrajPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalTrajPoint | | get |

优化轨迹点

## ◆ IdeaTrajPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> IdeaTrajPoint | | get |

理想轨迹点

## ◆ IdeaTrajCaliper

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> IdeaTrajCaliper | | get |

理想轨迹卡尺

## ◆ CalTrajFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CalTrajFlag | | get |

优化轨迹状态
