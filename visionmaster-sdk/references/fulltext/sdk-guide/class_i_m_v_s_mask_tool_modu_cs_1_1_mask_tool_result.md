<!-- src:class_i_m_v_s_mask_tool_modu_cs_1_1_mask_tool_result.html -->
<!-- path:接口函数 > 图像处理 > 掩膜工具 > MaskToolResult -->
# MaskToolResult类 参考 图像处理 » 掩膜工具

掩膜工具结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get, set]` |
|  | 模块状态 更多... |
|  | |
| ImageBaseData | OutputImage `[get, set]` |
|  | 输出图像 更多... |
|  | |
| ImageBaseData | OutputMask `[get, set]` |
|  | 输出掩膜 更多... |
|  | |
| ImageBaseData | OutputMaskCalcImage `[get, set]` |
|  | 掩膜运算图像 更多... |
|  | |
| List< RectBox > | ROIsBox `[get, set]` |
|  | 检测区域 更多... |
|  | |
| List< Annulus > | ROIAnnuluss `[get, set]` |
|  | ROI圆弧 更多... |
|  | |
| List< int > | BlindPolygonPointNum `[get, set]` |
|  | 多边形点数 更多... |
|  | |
| List< PointF > | BlindPolygonPoints `[get, set]` |
|  | 多边形点集 更多... |
|  | |
| List< string > | BlindPolygonString `[get, set]` |
|  | 屏蔽区 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

掩膜工具结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | getset |

模块状态

## ◆ OutputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputImage | | getset |

输出图像

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | getset |

输出掩膜

## ◆ OutputMaskCalcImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMaskCalcImage | | getset |

掩膜运算图像

## ◆ ROIsBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROIsBox | | getset |

检测区域

## ◆ ROIAnnuluss

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> ROIAnnuluss | | getset |

ROI圆弧

## ◆ BlindPolygonPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BlindPolygonPointNum | | getset |

多边形点数

## ◆ BlindPolygonPoints

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> BlindPolygonPoints | | getset |

多边形点集

## ◆ BlindPolygonString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> BlindPolygonString | | getset |

屏蔽区
