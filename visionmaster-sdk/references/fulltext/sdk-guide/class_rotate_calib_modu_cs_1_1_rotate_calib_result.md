<!-- src:class_rotate_calib_modu_cs_1_1_rotate_calib_result.html -->
<!-- path:接口函数 > 标定 > 旋转标定 > RotateCalibResult -->
# RotateCalibResult类 参考 标定 » 旋转标定

旋转标定结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | remainCount `[get]` |
|  | 剩余标定次数 更多... |
|  | |
| PointF | RotAxisPoint `[get]` |
|  | 旋转轴图像点 更多... |
|  | |
| PointF | RotPhysicalPoint `[get]` |
|  | 旋转中心物理点 更多... |
|  | |
| float | RotError `[get]` |
|  | 旋转像素平均误差 更多... |
|  | |
| float | RotWorldError `[get]` |
|  | 旋转真实平均误差 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

旋转标定结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ remainCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int remainCount | | get |

剩余标定次数

## ◆ RotAxisPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF RotAxisPoint | | get |

旋转轴图像点

## ◆ RotPhysicalPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF RotPhysicalPoint | | get |

旋转中心物理点

## ◆ RotError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotError | | get |

旋转像素平均误差

## ◆ RotWorldError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotWorldError | | get |

旋转真实平均误差
