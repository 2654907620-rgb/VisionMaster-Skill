<!-- src:class_i_m_v_s_rect_find_modu_cs_1_1_rect_find_result.html -->
<!-- path:接口函数 > 定位 > 矩形检测 > RectFindResult -->
# RectFindResult类 参考 定位 » 矩形检测

矩形检测结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | DetectStatus `[get]` |
|  | 检测状态 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| RectBox | RectBox `[get]` |
|  | 矩形框 更多... |
|  | |
| List< PointF > | ContourPoint `[get]` |
|  | 轮廓点 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
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

矩形检测结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ DetectStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DetectStatus | | get |

检测状态

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜

## ◆ RectBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox RectBox | | get |

矩形框

## ◆ ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ContourPoint | | get |

轮廓点

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ EdgePointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointStatus | | get |

轮廓点状态

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

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
