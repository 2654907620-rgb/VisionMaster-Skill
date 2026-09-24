<!-- src:class_i_m_v_s_cnn_fast_flaw_modu_cs_1_1_cnn_fast_flaw_result.html -->
<!-- path:接口函数 > 深度学习 > DL快速图像分割GPU > CnnFastFlawResult -->
# CnnFastFlawResult类 参考 深度学习 » DL快速图像分割GPU

DL快速图像分割 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< string > | ClassName `[get]` |
|  | 类别名称 更多... |
|  | |
| List< int > | GrayValue `[get]` |
|  | 灰度值 更多... |
|  | |
| int | MinScore `[get]` |
|  | 最小分数 更多... |
|  | |
| ImageBaseData | ClassImageData `[get]` |
|  | 类别图 更多... |
|  | |
| List< RectBox > | DetectROIs `[get]` |
|  | 检测区域 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

DL快速图像分割 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ClassName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassName | | get |

类别名称

## ◆ GrayValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> GrayValue | | get |

灰度值

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinScore | | get |

最小分数

## ◆ ClassImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ClassImageData | | get |

类别图

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | get |

检测区域
