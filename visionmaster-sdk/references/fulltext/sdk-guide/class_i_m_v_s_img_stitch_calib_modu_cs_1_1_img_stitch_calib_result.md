<!-- src:class_i_m_v_s_img_stitch_calib_modu_cs_1_1_img_stitch_calib_result.html -->
<!-- path:接口函数 > 图像处理 > 图像拼接 > ImgStitchCalibResult -->
# ImgStitchCalibResult类 参考 图像处理 » 图像拼接

图像拼接结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | CurNum `[get]` |
|  | 当前图像个数 更多... |
|  | |
| int | TotalNum `[get]` |
|  | 图像总个数 更多... |
|  | |
| ImageBaseData | StitchImageComb `[get]` |
|  | 拼接图像数据 更多... |
|  | |
| List< RectBox > | MinBoudingRect `[get]` |
|  | 最小外接矩形 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

图像拼接结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ CurNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CurNum | | get |

当前图像个数

## ◆ TotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TotalNum | | get |

图像总个数

## ◆ StitchImageComb

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData StitchImageComb | | get |

拼接图像数据

## ◆ MinBoudingRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MinBoudingRect | | get |

最小外接矩形
