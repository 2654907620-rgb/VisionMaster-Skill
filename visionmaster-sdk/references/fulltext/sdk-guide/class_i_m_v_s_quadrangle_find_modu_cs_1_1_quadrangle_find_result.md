<!-- src:class_i_m_v_s_quadrangle_find_modu_cs_1_1_quadrangle_find_result.html -->
<!-- path:接口函数 > 定位 > 四边形查找 > QuadrangleFindResult -->
# QuadrangleFindResult类 参考 定位 » 四边形查找

四边形查找结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | LineStatusFirst `[get]` |
|  | 直线1状态 更多... |
|  | |
| int | LineStatusSecond `[get]` |
|  | 直线2状态 更多... |
|  | |
| int | LineStatusThird `[get]` |
|  | 直线3状态 更多... |
|  | |
| int | LineStatusFourth `[get]` |
|  | 直线4状态 更多... |
|  | |
| Line | EdgeLine1 `[get]` |
|  | 边缘直线1 更多... |
|  | |
| float | Line1Angle `[get]` |
|  | 直线1角度 更多... |
|  | |
| Line | EdgeLine2 `[get]` |
|  | 边缘直线2 更多... |
|  | |
| float | Line2Angle `[get]` |
|  | 直线2角度 更多... |
|  | |
| Line | EdgeLine3 `[get]` |
|  | 边缘直线3 更多... |
|  | |
| float | Line3Angle `[get]` |
|  | 直线3角度 更多... |
|  | |
| Line | EdgeLine4 `[get]` |
|  | 边缘直线4 更多... |
|  | |
| float | Line4Angle `[get]` |
|  | 直线4角度 更多... |
|  | |
| float | Line1FitError `[get]` |
|  | 直线1拟合误差 更多... |
|  | |
| float | Line2FitError `[get]` |
|  | 直线2拟合误差 更多... |
|  | |
| float | Line3FitError `[get]` |
|  | 直线3拟合误差 更多... |
|  | |
| float | Line4FitError `[get]` |
|  | 直线4拟合误差 更多... |
|  | |
| List< PointF > | Line1ContourPoint `[get]` |
|  | 直线1轮廓点 更多... |
|  | |
| int | Edge1PointNum `[get]` |
|  | 边缘1轮廓点数 更多... |
|  | |
| List< int > | Edge1PointStatus `[get]` |
|  | 边缘1轮廓点状态 更多... |
|  | |
| List< PointF > | Line2ContourPoint `[get]` |
|  | 直线2轮廓点 更多... |
|  | |
| int | Edge2PointNum `[get]` |
|  | 直线2轮廓点数 更多... |
|  | |
| List< int > | Edge2PointStatus `[get]` |
|  | 直线2轮廓点状态 更多... |
|  | |
| List< PointF > | Line3ContourPoint `[get]` |
|  | 直线3轮廓点 更多... |
|  | |
| int | Edge3PointNum `[get]` |
|  | 直线3轮廓点数 更多... |
|  | |
| List< int > | Edge3PointStatus `[get]` |
|  | 直线3轮廓点状态 更多... |
|  | |
| List< PointF > | Line4ContourPoint `[get]` |
|  | 直线4轮廓点 更多... |
|  | |
| int | Edge4PointNum `[get]` |
|  | 直线4轮廓点数 更多... |
|  | |
| List< int > | Edge4PointStatus `[get]` |
|  | 直线4轮廓点状态 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| RectBox | ROI1 `[get]` |
|  | 检测区域1 更多... |
|  | |
| RectBox | ROI2 `[get]` |
|  | 检测区域2 更多... |
|  | |
| RectBox | ROI3 `[get]` |
|  | 检测区域3 更多... |
|  | |
| RectBox | ROI4 `[get]` |
|  | 检测区域4 更多... |
|  | |
| Line | DiagonalLine1 `[get]` |
|  | 对角线1 更多... |
|  | |
| float | DiagonalLine1Angle `[get]` |
|  | 对角线1角度 更多... |
|  | |
| Line | DiagonalLine2 `[get]` |
|  | 对角线2 更多... |
|  | |
| float | DiagonalLine2Angle `[get]` |
|  | 对角线2角度 更多... |
|  | |
| Line | MedianLine1 `[get]` |
|  | 中点线1 更多... |
|  | |
| float | MedianLine1Angle `[get]` |
|  | 中点线1角度 更多... |
|  | |
| Line | MedianLine2 `[get]` |
|  | 中点线2 更多... |
|  | |
| float | MedianLine2Angle `[get]` |
|  | 中点线2角度 更多... |
|  | |
| float | LineIntersectionAngle1 `[get]` |
|  | 临边夹角1 更多... |
|  | |
| float | LineIntersectionAngle2 `[get]` |
|  | 临边夹角2 更多... |
|  | |
| float | LineIntersectionAngle3 `[get]` |
|  | 临边夹角3 更多... |
|  | |
| float | LineIntersectionAngle4 `[get]` |
|  | 临边夹角4 更多... |
|  | |
| PointF | Vertex1 `[get]` |
|  | 顶点1 更多... |
|  | |
| PointF | Vertex2 `[get]` |
|  | 顶点2 更多... |
|  | |
| PointF | Vertex3 `[get]` |
|  | 顶点3 更多... |
|  | |
| PointF | Vertex4 `[get]` |
|  | 顶点4 更多... |
|  | |
| PointF | DiagonalLineIntersection `[get]` |
|  | 对角线交点 更多... |
|  | |
| PointF | MedianLineIntersection `[get]` |
|  | 中点线交点 更多... |
|  | |
| PointF | CentralPoint `[get]` |
|  | 中心点 更多... |
|  | |
| PointF | AngleBisectorIntersection `[get]` |
|  | 对边角平分线交点 更多... |
|  | |
| Line | AngleBisector1 `[get]` |
|  | 对边角平分线1 更多... |
|  | |
| float | AngleBisector1Angle `[get]` |
|  | 对边角平分线1角度 更多... |
|  | |
| Line | AngleBisector2 `[get]` |
|  | 对边角平分线2 更多... |
|  | |
| float | AngleBisector2Angle `[get]` |
|  | 对边角平分线2角度 更多... |
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

四边形查找结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ LineStatusFirst

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineStatusFirst | | get |

直线1状态

## ◆ LineStatusSecond

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineStatusSecond | | get |

直线2状态

## ◆ LineStatusThird

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineStatusThird | | get |

直线3状态

## ◆ LineStatusFourth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineStatusFourth | | get |

直线4状态

## ◆ EdgeLine1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine1 | | get |

边缘直线1

## ◆ Line1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line1Angle | | get |

直线1角度

## ◆ EdgeLine2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine2 | | get |

边缘直线2

## ◆ Line2Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line2Angle | | get |

直线2角度

## ◆ EdgeLine3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine3 | | get |

边缘直线3

## ◆ Line3Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line3Angle | | get |

直线3角度

## ◆ EdgeLine4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line EdgeLine4 | | get |

边缘直线4

## ◆ Line4Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line4Angle | | get |

直线4角度

## ◆ Line1FitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line1FitError | | get |

直线1拟合误差

## ◆ Line2FitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line2FitError | | get |

直线2拟合误差

## ◆ Line3FitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line3FitError | | get |

直线3拟合误差

## ◆ Line4FitError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Line4FitError | | get |

直线4拟合误差

## ◆ Line1ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line1ContourPoint | | get |

直线1轮廓点

## ◆ Edge1PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge1PointNum | | get |

边缘1轮廓点数

## ◆ Edge1PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge1PointStatus | | get |

边缘1轮廓点状态

## ◆ Line2ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line2ContourPoint | | get |

直线2轮廓点

## ◆ Edge2PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge2PointNum | | get |

直线2轮廓点数

## ◆ Edge2PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge2PointStatus | | get |

直线2轮廓点状态

## ◆ Line3ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line3ContourPoint | | get |

直线3轮廓点

## ◆ Edge3PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge3PointNum | | get |

直线3轮廓点数

## ◆ Edge3PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge3PointStatus | | get |

直线3轮廓点状态

## ◆ Line4ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Line4ContourPoint | | get |

直线4轮廓点

## ◆ Edge4PointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Edge4PointNum | | get |

直线4轮廓点数

## ◆ Edge4PointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Edge4PointStatus | | get |

直线4轮廓点状态

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜

## ◆ ROI1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI1 | | get |

检测区域1

## ◆ ROI2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI2 | | get |

检测区域2

## ◆ ROI3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI3 | | get |

检测区域3

## ◆ ROI4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI4 | | get |

检测区域4

## ◆ DiagonalLine1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line DiagonalLine1 | | get |

对角线1

## ◆ DiagonalLine1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float DiagonalLine1Angle | | get |

对角线1角度

## ◆ DiagonalLine2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line DiagonalLine2 | | get |

对角线2

## ◆ DiagonalLine2Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float DiagonalLine2Angle | | get |

对角线2角度

## ◆ MedianLine1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line MedianLine1 | | get |

中点线1

## ◆ MedianLine1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MedianLine1Angle | | get |

中点线1角度

## ◆ MedianLine2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line MedianLine2 | | get |

中点线2

## ◆ MedianLine2Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MedianLine2Angle | | get |

中点线2角度

## ◆ LineIntersectionAngle1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineIntersectionAngle1 | | get |

临边夹角1

## ◆ LineIntersectionAngle2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineIntersectionAngle2 | | get |

临边夹角2

## ◆ LineIntersectionAngle3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineIntersectionAngle3 | | get |

临边夹角3

## ◆ LineIntersectionAngle4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineIntersectionAngle4 | | get |

临边夹角4

## ◆ Vertex1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF Vertex1 | | get |

顶点1

## ◆ Vertex2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF Vertex2 | | get |

顶点2

## ◆ Vertex3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF Vertex3 | | get |

顶点3

## ◆ Vertex4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF Vertex4 | | get |

顶点4

## ◆ DiagonalLineIntersection

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF DiagonalLineIntersection | | get |

对角线交点

## ◆ MedianLineIntersection

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF MedianLineIntersection | | get |

中点线交点

## ◆ CentralPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF CentralPoint | | get |

中心点

## ◆ AngleBisectorIntersection

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF AngleBisectorIntersection | | get |

对边角平分线交点

## ◆ AngleBisector1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line AngleBisector1 | | get |

对边角平分线1

## ◆ AngleBisector1Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float AngleBisector1Angle | | get |

对边角平分线1角度

## ◆ AngleBisector2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line AngleBisector2 | | get |

对边角平分线2

## ◆ AngleBisector2Angle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float AngleBisector2Angle | | get |

对边角平分线2角度

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
