<!-- src:class_i_m_v_s_map_calib_modu_cs_1_1_map_calib_result.html -->
<!-- path:接口函数 > 标定 > 映射标定 > MapCalibResult -->
# MapCalibResult类 参考 标定 » 映射标定

映射标定结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | CalibStatus `[get]` |
|  | 标定状态 更多... |
|  | |
| float | XRatio `[get]` |
|  | X方向比例 更多... |
|  | |
| float | YRatio `[get]` |
|  | Y方向比例 更多... |
|  | |
| float | MapError `[get]` |
|  | 映射误差 更多... |
|  | |
| List< PointF > | CurrentCornersPoint `[get]` |
|  | 当前角点 更多... |
|  | |
| List< PointF > | ObjectCornersPoint `[get]` |
|  | 目标角点 更多... |
|  | |
| List< PointF > | ProjectionCornersPoint `[get]` |
|  | 映射角点 更多... |
|  | |
| int | CurCornersPointNum `[get]` |
|  | 当前角点数 更多... |
|  | |
| int | ObjCornersPointNum `[get]` |
|  | 目标角点数 更多... |
|  | |
| int | ProCornersPointNum `[get]` |
|  | 映射角点数 更多... |
|  | |
| List< RectBox > | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| int | CalibStatus1 `[get]` |
|  | 图像1标定状态 更多... |
|  | |
| int | CalibStatus2 `[get]` |
|  | 图像2标定状态 更多... |
|  | |
| float | PixelScale1 `[get]` |
|  | 单像素精度1 更多... |
|  | |
| float | PixelScale2 `[get]` |
|  | 单像素精度2 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

映射标定结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ CalibStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibStatus | | get |

标定状态

## ◆ XRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float XRatio | | get |

X方向比例

## ◆ YRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float YRatio | | get |

Y方向比例

## ◆ MapError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MapError | | get |

映射误差

## ◆ CurrentCornersPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CurrentCornersPoint | | get |

当前角点

## ◆ ObjectCornersPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectCornersPoint | | get |

目标角点

## ◆ ProjectionCornersPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ProjectionCornersPoint | | get |

映射角点

## ◆ CurCornersPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CurCornersPointNum | | get |

当前角点数

## ◆ ObjCornersPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjCornersPointNum | | get |

目标角点数

## ◆ ProCornersPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ProCornersPointNum | | get |

映射角点数

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域

## ◆ CalibStatus1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibStatus1 | | get |

图像1标定状态

## ◆ CalibStatus2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibStatus2 | | get |

图像2标定状态

## ◆ PixelScale1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float PixelScale1 | | get |

单像素精度1

## ◆ PixelScale2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float PixelScale2 | | get |

单像素精度2
