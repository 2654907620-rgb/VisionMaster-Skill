<!-- src:class_i_m_v_s_target_track_modu_cs_1_1_target_track_result.html -->
<!-- path:接口函数 > 定位 > 目标跟踪 > TargetTrackResult -->
# TargetTrackResult类 参考 定位 » 目标跟踪

目标跟踪结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | ObjNumOut `[get]` |
|  | 目标数 更多... |
|  | |
| int | CountTotalNum `[get]` |
|  | 计数总数 更多... |
|  | |
| int | SingleNum `[get]` |
|  | 单帧计数 更多... |
|  | |
| List< PointF > | PolyonContourPoint `[get]` |
|  | 多边形轮廓点 更多... |
|  | |
| List< PointF > | ObjIdPosition `[get]` |
|  | 目标Id位置 更多... |
|  | |
| List< int > | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| List< int > | ObjId `[get]` |
|  | 目标Id 更多... |
|  | |
| RectBox | TrackRect `[get]` |
|  | 检测区域 更多... |
|  | |
| float | TrackSpeedX `[get]` |
|  | X方向速度 更多... |
|  | |
| float | TrackSpeedY `[get]` |
|  | Y方向速度 更多... |
|  | |
| Line | TrackLine `[get]` |
|  | 检测线 更多... |
|  | |
| float | LineAngle `[get]` |
|  | 直线角度 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

目标跟踪结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ObjNumOut

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjNumOut | | get |

目标数

## ◆ CountTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountTotalNum | | get |

计数总数

## ◆ SingleNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SingleNum | | get |

单帧计数

## ◆ PolyonContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> PolyonContourPoint | | get |

多边形轮廓点

## ◆ ObjIdPosition

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjIdPosition | | get |

目标Id位置

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointNum | | get |

边缘点个数

## ◆ ObjId

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjId | | get |

目标Id

## ◆ TrackRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox TrackRect | | get |

检测区域

## ◆ TrackSpeedX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TrackSpeedX | | get |

X方向速度

## ◆ TrackSpeedY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TrackSpeedY | | get |

Y方向速度

## ◆ TrackLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Line TrackLine | | get |

检测线

## ◆ LineAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float LineAngle | | get |

直线角度
