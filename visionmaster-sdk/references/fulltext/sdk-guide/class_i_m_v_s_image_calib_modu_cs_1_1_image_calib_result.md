<!-- src:class_i_m_v_s_image_calib_modu_cs_1_1_image_calib_result.html -->
<!-- path:接口函数 > 标定 > 畸变标定 > ImageCalibResult -->
# ImageCalibResult类 参考 标定 » 畸变标定

畸变标定结果
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
| int | CalibPointNum `[get]` |
|  | 标定点数 更多... |
|  | |
| List< PointF > | CalibrationPoint `[get]` |
|  | 标定点 更多... |
|  | |
| List< float > | CalibPointStatus `[get]` |
|  | 标定点状态 更多... |
|  | |
| float | EvaluationError `[get]` |
|  | 评估误差 更多... |
|  | |
| float | CalibPointError `[get]` |
|  | 标定点评估误差 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| ImageBaseData | PostCorrectionImage `[get]` |
|  | 矫正后的图像 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

畸变标定结果

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

## ◆ CalibPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibPointNum | | get |

标定点数

## ◆ CalibrationPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalibrationPoint | | get |

标定点

## ◆ CalibPointStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibPointStatus | | get |

标定点状态

## ◆ EvaluationError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float EvaluationError | | get |

评估误差

## ◆ CalibPointError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float CalibPointError | | get |

标定点评估误差

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ PostCorrectionImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData PostCorrectionImage | | get |

矫正后的图像
