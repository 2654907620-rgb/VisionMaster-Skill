<!-- src:class_i_m_v_s_circle_find_modu_cs_1_1_circle_find_result.html -->
<!-- path:接口函数 > 定位 > 圆查找 > CircleFindResult -->
# CircleFindResult类 参考 定位 » 圆查找

圆查找结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| Circle | OutputCircle `[get]` |
|  | 输出圆 更多... |
|  | |
| Annulus | OutputCircleAnnulus `[get]` |
|  | 输出圆环 更多... |
|  | |
| float | FitError `[get]` |
|  | 拟合误差 更多... |
|  | |
| List< PointF > | CircleCoutourPoint `[get]` |
|  | 圆轮廓点 更多... |
|  | |
| List< int > | EdgePointStatus `[get]` |
|  | 轮廓点状态 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| Annulus | ROIAnnulus `[get]` |
|  | ROI圆弧 更多... |
|  | |
| List< RectBox > | CaliperBox `[get]` |
|  | 卡尺框 更多... |
|  | |
| List< RectBox > | DetectCaliperBox `[get]` |
|  | 卡尺框检测区 更多... |
|  | |
| Annulus | OutputAnnulus `[get]` |
|  | 输出圆弧 更多... |
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

圆查找结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ OutputCircle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Circle OutputCircle | | get |

输出圆

## ◆ OutputCircleAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Annulus OutputCircleAnnulus | | get |

输出圆环

## ◆ FitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float FitError | | get |

拟合误差

## ◆ CircleCoutourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CircleCoutourPoint | | get |

圆轮廓点

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

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ ROIAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Annulus ROIAnnulus | | get |

ROI圆弧

## ◆ CaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CaliperBox | | get |

卡尺框

## ◆ DetectCaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectCaliperBox | | get |

卡尺框检测区

## ◆ OutputAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Annulus OutputAnnulus | | get |

输出圆弧

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
