<!-- src:class_i_m_v_s_mark_insp_modu_v_a_cs_1_1_mark_insp_v_a_result.html -->
<!-- path:接口函数 > 缺陷检测 > 字符缺陷检测VA > MarkInspVAResult -->
# MarkInspVAResult类 参考 缺陷检测 » 字符缺陷检测VA

字符缺陷检测结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | MatchStatus `[get]` |
|  | 匹配状态 更多... |
|  | |
| List< int > | MarkStatus `[get]` |
|  | 字符状态 更多... |
|  | |
| int | MarkBoxNum `[get]` |
|  | 字符框个数 更多... |
|  | |
| List< RectBox > | MarkBox `[get]` |
|  | 字符框 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| RectBox | MatchRect `[get]` |
|  | 匹配框 更多... |
|  | |
| int | FlawNum `[get]` |
|  | 缺陷个数 更多... |
|  | |
| List< RectBox > | FlawBox `[get]` |
|  | 缺陷框 更多... |
|  | |
| ImageBaseData | MarkFlawImage `[get]` |
|  | 缺陷图像 更多... |
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
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

字符缺陷检测结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ MatchStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchStatus | | get |

匹配状态

## ◆ MarkStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MarkStatus | | get |

字符状态

## ◆ MarkBoxNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MarkBoxNum | | get |

字符框个数

## ◆ MarkBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MarkBox | | get |

字符框

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ MatchRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox MatchRect | | get |

匹配框

## ◆ FlawNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FlawNum | | get |

缺陷个数

## ◆ FlawBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> FlawBox | | get |

缺陷框

## ◆ MarkFlawImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData MarkFlawImage | | get |

缺陷图像

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

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜
