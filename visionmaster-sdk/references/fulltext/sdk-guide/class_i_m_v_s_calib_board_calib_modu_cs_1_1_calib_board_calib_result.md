<!-- src:class_i_m_v_s_calib_board_calib_modu_cs_1_1_calib_board_calib_result.html -->
<!-- path:接口函数 > 标定 > 标定板标定 > CalibBoardCalibResult -->
# CalibBoardCalibResult类 参考 标定 » 标定板标定

标定板标定结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| float | EstimationError `[get]` |
|  | 标定误差 更多... |
|  | |
| float | Scale `[get]` |
|  | 尺度 更多... |
|  | |
| List< PointF > | CalibrationPoint `[get]` |
|  | 标定点 更多... |
|  | |
| PointF | CalibrationOrigin `[get]` |
|  | 标定原点 更多... |
|  | |
| PointF | PosXVector `[get]` |
|  | 坐标X向量 更多... |
|  | |
| PointF | PosYVector `[get]` |
|  | 坐标Y向量 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| int | CalibPointNum `[get]` |
|  | 标定点数 更多... |
|  | |
| float | TranslateX `[get]` |
|  | 平移X 更多... |
|  | |
| float | TranslateY `[get]` |
|  | 平移Y 更多... |
|  | |
| float | Rotate `[get]` |
|  | 旋转 更多... |
|  | |
| float | Skew `[get]` |
|  | 斜切 更多... |
|  | |
| float | Aspect `[get]` |
|  | 宽高比 更多... |
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

标定板标定结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ EstimationError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EstimationError | | get |

标定误差

## ◆ Scale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Scale | | get |

尺度

## ◆ CalibrationPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalibrationPoint | | get |

标定点

## ◆ CalibrationOrigin

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF CalibrationOrigin | | get |

标定原点

## ◆ PosXVector

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF PosXVector | | get |

坐标X向量

## ◆ PosYVector

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF PosYVector | | get |

坐标Y向量

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ CalibPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibPointNum | | get |

标定点数

## ◆ TranslateX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TranslateX | | get |

平移X

## ◆ TranslateY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TranslateY | | get |

平移Y

## ◆ Rotate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Rotate | | get |

旋转

## ◆ Skew

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Skew | | get |

斜切

## ◆ Aspect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Aspect | | get |

宽高比

## ◆ PixelPrecision

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float PixelPrecision | | get |

像素精度
