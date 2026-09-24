<!-- src:class_i_m_v_s_edge_insp_group_modu_cs_1_1_edge_insp_group_result.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘组合缺陷检测 > EdgeInspGroupResult -->
# EdgeInspGroupResult类 参考 缺陷检测 » 边缘组合缺陷检测

边缘组合缺陷检测结果
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
| List< RectBox > | FlawRect `[get]` |
|  | 缺陷框 更多... |
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
| List< PointF > | EdgePoints `[get]` |
|  | 边缘点 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
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
| List< Circle > | StandardCircle `[get]` |
|  | 标准圆 更多... |
|  | |
| List< Annulus > | StandardAnnulus `[get]` |
|  | 标准圆环 更多... |
|  | |
| List< Line > | StandardLine `[get]` |
|  | 标准直线 更多... |
|  | |
| List< float > | StandardLineAngle `[get]` |
|  | 标准直线角度 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

边缘组合缺陷检测结果

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

## ◆ FlawRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> FlawRect | | get |

缺陷框

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

## ◆ StandardCircle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Circle> StandardCircle | | get |

标准圆

## ◆ StandardAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> StandardAnnulus | | get |

标准圆环

## ◆ StandardLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> StandardLine | | get |

标准直线

## ◆ StandardLineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> StandardLineAngle | | get |

标准直线角度
