<!-- src:class_i_m_v_s_cnn_un_supervised_classify_modu_cs_1_1_cnn_un_supervised_classify_result.html -->
<!-- path:接口函数 > 深度学习 > DL无监督分类GPU > CnnUnSupervisedClassifyResult -->
# CnnUnSupervisedClassifyResult类 参考 深度学习 » DL无监督分类GPU

DL无监督分类 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< float > | Confidence `[get]` |
|  | 置信度 更多... |
|  | |
| List< int > | PredictStatus `[get]` |
|  | 预测状态 更多... |
|  | |
| int | RoiNum `[get]` |
|  | 检测区域个数 更多... |
|  | |
| List< int > | ClassRoiIndexs `[get]` |
|  | ROI序号 更多... |
|  | |
| List< RectBox > | ROI `[get]` |
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

DL无监督分类 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ Confidence

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Confidence | | get |

置信度

## ◆ PredictStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> PredictStatus | | get |

预测状态

## ◆ RoiNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoiNum | | get |

检测区域个数

## ◆ ClassRoiIndexs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassRoiIndexs | | get |

ROI序号

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域
