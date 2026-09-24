<!-- src:class_i_m_v_s_inspect_modu_cs_1_1_inspect_result.html -->
<!-- path:接口函数 > 缺陷检测 > 异常检测 > InspectResult -->
# InspectResult类 参考 缺陷检测 » 异常检测

异常检测结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | InspectStatus `[get]` |
|  | 对比状态 更多... |
|  | |
| string | InspectLabel `[get]` |
|  | 标签 更多... |
|  | |
| float | InspectScore `[get]` |
|  | 分数 更多... |
|  | |
| int | DetectRoiNum `[get]` |
|  | 检测区域个数 更多... |
|  | |
| RectBox | InspROI `[get]` |
|  | 检测区域 更多... |
|  | |
| RectBox | DefectBox `[get]` |
|  | 缺陷框 更多... |
|  | |
| int | MatchStatus `[get]` |
|  | 匹配状态 更多... |
|  | |
| RectBox | MatchRect `[get]` |
|  | 匹配框 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

异常检测结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ InspectStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int InspectStatus | | get |

对比状态

## ◆ InspectLabel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string InspectLabel | | get |

标签

## ◆ InspectScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float InspectScore | | get |

分数

## ◆ DetectRoiNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DetectRoiNum | | get |

检测区域个数

## ◆ InspROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox InspROI | | get |

检测区域

## ◆ DefectBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox DefectBox | | get |

缺陷框

## ◆ MatchStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchStatus | | get |

匹配状态

## ◆ MatchRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox MatchRect | | get |

匹配框
