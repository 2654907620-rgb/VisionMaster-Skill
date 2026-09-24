<!-- src:class_i_m_v_s_multi_line_find_modu_cs_1_1_multi_line_find_result.html -->
<!-- path:接口函数 > 定位 > 多直线查找 > MultiLineFindResult -->
# MultiLineFindResult类 参考 定位 » 多直线查找

多直线查找结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | LineNum `[get]` |
|  | 直线个数 更多... |
|  | |
| int | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< Line > | LinesInfo `[get]` |
|  | 直线段信息 更多... |
|  | |
| List< float > | LineAngle `[get]` |
|  | 直线角度 更多... |
|  | |
| List< float > | LineFitError `[get]` |
|  | 拟合误差 更多... |
|  | |
| List< float > | LineIntensity `[get]` |
|  | 直线对比度强度 更多... |
|  | |
| List< float > | CoverageScore `[get]` |
|  | 覆盖率分数 更多... |
|  | |
| List< int > | InliersNum `[get]` |
|  | 在群点数量 更多... |
|  | |
| List< int > | LineIndex `[get]` |
|  | 线段索引 更多... |
|  | |
| List< PointF > | EdgesInfo `[get]` |
|  | 边缘点信息 更多... |
|  | |
| List< int > | EdgePolarity `[get]` |
|  | 边缘极性 更多... |
|  | |
| List< float > | EdgeMagnitude `[get]` |
|  | 梯度幅值 更多... |
|  | |
| List< float > | EdgeOrientation `[get]` |
|  | 梯度方向 更多... |
|  | |
| List< float > | EdgeDist `[get]` |
|  | 边缘距离 更多... |
|  | |
| List< int > | EdgeStatus `[get]` |
|  | 边缘状态 更多... |
|  | |
| List< int > | EdgeCaliperIndex `[get]` |
|  | 投影区域索引 更多... |
|  | |
| List< int > | EdgeLineIndex `[get]` |
|  | 所属线段索引 更多... |
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

多直线查找结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ LineNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineNum | | get |

直线个数

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointNum | | get |

边缘点个数

## ◆ LinesInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> LinesInfo | | get |

直线段信息

## ◆ LineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> LineAngle | | get |

直线角度

## ◆ LineFitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> LineFitError | | get |

拟合误差

## ◆ LineIntensity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> LineIntensity | | get |

直线对比度强度

## ◆ CoverageScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CoverageScore | | get |

覆盖率分数

## ◆ InliersNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InliersNum | | get |

在群点数量

## ◆ LineIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> LineIndex | | get |

线段索引

## ◆ EdgesInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> EdgesInfo | | get |

边缘点信息

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePolarity | | get |

边缘极性

## ◆ EdgeMagnitude

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgeMagnitude | | get |

梯度幅值

## ◆ EdgeOrientation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgeOrientation | | get |

梯度方向

## ◆ EdgeDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgeDist | | get |

边缘距离

## ◆ EdgeStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeStatus | | get |

边缘状态

## ◆ EdgeCaliperIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeCaliperIndex | | get |

投影区域索引

## ◆ EdgeLineIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeLineIndex | | get |

所属线段索引

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
