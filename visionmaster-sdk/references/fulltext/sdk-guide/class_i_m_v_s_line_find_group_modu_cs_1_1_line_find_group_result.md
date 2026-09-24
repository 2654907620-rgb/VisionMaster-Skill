<!-- src:class_i_m_v_s_line_find_group_modu_cs_1_1_line_find_group_result.html -->
<!-- path:接口函数 > 定位 > 直线查找组合 > LineFindGroupResult -->
# LineFindGroupResult类 参考 定位 » 直线查找组合

直线查找组合结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| Line | OutputLine `[get]` |
|  | 输出直线 更多... |
|  | |
| float | LineAngle `[get]` |
|  | 直线角度 更多... |
|  | |
| List< PointF > | OutputFittingPoint `[get]` |
|  | 输出拟合点 更多... |
|  | |
| float | LineFitScore `[get]` |
|  | 拟合误差 更多... |
|  | |
| int | LineFitStatus `[get]` |
|  | 拟合状态 更多... |
|  | |
| int | FitPointNum `[get]` |
|  | 拟合点数 更多... |
|  | |
| List< float > | FitDist `[get]` |
|  | 拟合距离 更多... |
|  | |
| List< int > | FitUsedPoint `[get]` |
|  | 匹配点 更多... |
|  | |
| int | FitUsedPointNum `[get]` |
|  | 匹配点数 更多... |
|  | |
| List< RectBox > | MinBoudingRect `[get]` |
|  | 最小外接矩形 更多... |
|  | |
| List< RectBox > | DetectCaliperBox `[get]` |
|  | 卡尺框检测区 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

直线查找组合结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ OutputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line OutputLine | | get |

输出直线

## ◆ LineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineAngle | | get |

直线角度

## ◆ OutputFittingPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> OutputFittingPoint | | get |

输出拟合点

## ◆ LineFitScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineFitScore | | get |

拟合误差

## ◆ LineFitStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineFitStatus | | get |

拟合状态

## ◆ FitPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitPointNum | | get |

拟合点数

## ◆ FitDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> FitDist | | get |

拟合距离

## ◆ FitUsedPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> FitUsedPoint | | get |

匹配点

## ◆ FitUsedPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitUsedPointNum | | get |

匹配点数

## ◆ MinBoudingRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MinBoudingRect | | get |

最小外接矩形

## ◆ DetectCaliperBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectCaliperBox | | get |

卡尺框检测区
