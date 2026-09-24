<!-- src:class_i_m_v_s_edge_flaw_insp_modu_cs_1_1_edge_flaw_insp_result.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘模型缺陷检测 > EdgeFlawInspResult -->
# EdgeFlawInspResult类 参考 缺陷检测 » 边缘模型缺陷检测

边缘模型缺陷检测结果
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
| List< RectBox > | DefectBox `[get]` |
|  | 缺陷框 更多... |
|  | |
| List< RectBox > | CaliperBox `[get]` |
|  | 卡尺框 更多... |
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
| List< PointF > | EdgePoint `[get]` |
|  | 边缘点 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< PointF > | CaliperIdeaPoint `[get]` |
|  | 理想卡尺点 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

边缘模型缺陷检测结果

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

## ◆ DefectBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DefectBox | | get |

缺陷框

## ◆ CaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CaliperBox | | get |

卡尺框

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

## ◆ EdgePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgePoint | | get |

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

## ◆ CaliperIdeaPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CaliperIdeaPoint | | get |

理想卡尺点
