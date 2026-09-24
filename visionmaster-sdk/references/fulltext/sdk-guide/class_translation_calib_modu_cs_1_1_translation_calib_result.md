<!-- src:class_translation_calib_modu_cs_1_1_translation_calib_result.html -->
<!-- path:接口函数 > 标定 > 平移旋转标定 > TranslationCalibResult -->
# TranslationCalibResult类 参考 标定 » 平移旋转标定

平移旋转标定结果
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
| int | IsRightCoorA `[get]` |
|  | 坐标系左右手一致性 更多... |
|  | |
| int | CalibCurIndex `[get]` |
|  | 当前标定点 更多... |
|  | |
| int | CalibTotalNum `[get]` |
|  | 标定点总数 更多... |
|  | |
| List< PointF > | CalibImagePoint `[get]` |
|  | 标定图像点 更多... |
|  | |
| List< PointF > | CalibPhysicalPoint `[get]` |
|  | 标定物理点 更多... |
|  | |
| float | TransError `[get]` |
|  | 平移像素平均误差 更多... |
|  | |
| float | RotError `[get]` |
|  | 旋转像素平均误差 更多... |
|  | |
| PointF | RotAxisPoint `[get]` |
|  | 旋转轴图像点 更多... |
|  | |
| PointF | RotPhysicalPoint `[get]` |
|  | 旋转中心物理点 更多... |
|  | |
| int | RotDirectionState `[get]` |
|  | 角度旋转一致性 更多... |
|  | |
| float | TransEstMax `[get]` |
|  | 平移像素最大误差 更多... |
|  | |
| float | TransErrMaxPtsNum `[get]` |
|  | 平移像素最大误差对应点数 更多... |
|  | |
| float | TransWorldError `[get]` |
|  | 平移估计真实误差 更多... |
|  | |
| float | TransErrWorldMax `[get]` |
|  | 平移像素真实最大误差 更多... |
|  | |
| float | RotErrMax `[get]` |
|  | 旋转像素最大误差 更多... |
|  | |
| int | RotErrMaxPtsNum `[get]` |
|  | 旋转像素最大误差对应点数 更多... |
|  | |
| float | RotWorldError `[get]` |
|  | 旋转真实平均误差 更多... |
|  | |
| float | RotErrWorldMax `[get]` |
|  | 旋转真实最大误差 更多... |
|  | |
| float | Scale `[get]` |
|  | 尺度 更多... |
|  | |
| float | DeltaX `[get]` |
|  | x偏移 更多... |
|  | |
| float | DeltaY `[get]` |
|  | y偏移 更多... |
|  | |
| float | Rotate `[get]` |
|  | 旋转 更多... |
|  | |
| float | Tilt `[get]` |
|  | 倾斜量 更多... |
|  | |
| float | DirectionRatio `[get]` |
|  | Y方向和X方向的比例 更多... |
|  | |
| float | PixelPrecision `[get]` |
|  | 像素精度 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

平移旋转标定结果

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

## ◆ IsRightCoorA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int IsRightCoorA | | get |

坐标系左右手一致性

## ◆ CalibCurIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibCurIndex | | get |

当前标定点

## ◆ CalibTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibTotalNum | | get |

标定点总数

## ◆ CalibImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalibImagePoint | | get |

标定图像点

## ◆ CalibPhysicalPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalibPhysicalPoint | | get |

标定物理点

## ◆ TransError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransError | | get |

平移像素平均误差

## ◆ RotError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotError | | get |

旋转像素平均误差

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

## ◆ RotDirectionState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotDirectionState | | get |

角度旋转一致性

## ◆ TransEstMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransEstMax | | get |

平移像素最大误差

## ◆ TransErrMaxPtsNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransErrMaxPtsNum | | get |

平移像素最大误差对应点数

## ◆ TransWorldError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransWorldError | | get |

平移估计真实误差

## ◆ TransErrWorldMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransErrWorldMax | | get |

平移像素真实最大误差

## ◆ RotErrMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotErrMax | | get |

旋转像素最大误差

## ◆ RotErrMaxPtsNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotErrMaxPtsNum | | get |

旋转像素最大误差对应点数

## ◆ RotWorldError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotWorldError | | get |

旋转真实平均误差

## ◆ RotErrWorldMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotErrWorldMax | | get |

旋转真实最大误差

## ◆ Scale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Scale | | get |

尺度

## ◆ DeltaX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float DeltaX | | get |

x偏移

## ◆ DeltaY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float DeltaY | | get |

y偏移

## ◆ Rotate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Rotate | | get |

旋转

## ◆ Tilt

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Tilt | | get |

倾斜量

## ◆ DirectionRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float DirectionRatio | | get |

Y方向和X方向的比例

## ◆ PixelPrecision

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float PixelPrecision | | get |

像素精度
