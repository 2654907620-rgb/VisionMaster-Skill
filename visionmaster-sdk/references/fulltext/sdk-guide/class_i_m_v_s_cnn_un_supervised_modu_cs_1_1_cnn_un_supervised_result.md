<!-- src:class_i_m_v_s_cnn_un_supervised_modu_cs_1_1_cnn_un_supervised_result.html -->
<!-- path:接口函数 > 深度学习 > DL无监督分割GPU > CnnUnSupervisedResult -->
# CnnUnSupervisedResult类 参考 深度学习 » DL无监督分割GPU

DL无监督分割 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| ImageBaseData | ProbabilityImageData `[get]` |
|  | 概率图数据 更多... |
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

DL无监督分割 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ProbabilityImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ProbabilityImageData | | get |

概率图数据

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | get |

检测区域
