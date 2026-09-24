<!-- src:class_i_m_v_s_mark_find_modu_cs_1_1_mark_find_result.html -->
<!-- path:接口函数 > 定位 > 图形定位 > MarkFindResult -->
# MarkFindResult类 参考 定位 » 图形定位

图形定位结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | MatchStatus `[get]` |
|  | 匹配状态 更多... |
|  | |
| List< int > | LineStatus `[get]` |
|  | 直线状态 更多... |
|  | |
| int | MatchNum `[get]` |
|  | 匹配个数 更多... |
|  | |
| List< RectBox > | MatchRect `[get]` |
|  | 匹配框 更多... |
|  | |
| List< PointF > | MatchPoint `[get]` |
|  | 匹配点 更多... |
|  | |
| List< Line > | OutputLine `[get]` |
|  | 输出直线 更多... |
|  | |
| List< float > | LineAngle `[get]` |
|  | 直线角度 更多... |
|  | |
| List< float > | MatchScaleX `[get]` |
|  | 尺度X 更多... |
|  | |
| List< float > | MatchScaleY `[get]` |
|  | 尺度Y 更多... |
|  | |
| List< float > | MatchScore `[get]` |
|  | 分数 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| MatchOutline | MatchOutline `[get]` |
|  | 匹配轮廓信息 更多... |
|  | |
| int | MatchOutlineNum `[get]` |
|  | 匹配轮廓点个数 更多... |
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

图形定位结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ MatchStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MatchStatus | | get |

匹配状态

## ◆ LineStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> LineStatus | | get |

直线状态

## ◆ MatchNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchNum | | get |

匹配个数

## ◆ MatchRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MatchRect | | get |

匹配框

## ◆ MatchPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> MatchPoint | | get |

匹配点

## ◆ OutputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> OutputLine | | get |

输出直线

## ◆ LineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> LineAngle | | get |

直线角度

## ◆ MatchScaleX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MatchScaleX | | get |

尺度X

## ◆ MatchScaleY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MatchScaleY | | get |

尺度Y

## ◆ MatchScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MatchScore | | get |

分数

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ MatchOutline

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchOutline MatchOutline | | get |

匹配轮廓信息

## ◆ MatchOutlineNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MatchOutlineNum | | get |

匹配轮廓点个数

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
