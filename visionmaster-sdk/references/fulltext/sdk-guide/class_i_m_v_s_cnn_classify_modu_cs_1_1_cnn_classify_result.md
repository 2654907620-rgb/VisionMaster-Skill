<!-- src:class_i_m_v_s_cnn_classify_modu_cs_1_1_cnn_classify_result.html -->
<!-- path:接口函数 > 深度学习 > DL分类GPU > CnnClassifyResult -->
# CnnClassifyResult类 参考 深度学习 » DL分类GPU

DL分类 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | ClassNums `[get]` |
|  | 类别个数 更多... |
|  | |
| List< float > | Confidences `[get]` |
|  | 置信度 更多... |
|  | |
| List< int > | ClassLabels `[get]` |
|  | 类别标签 更多... |
|  | |
| List< float > | ClassProbs `[get]` |
|  | 类别概率 更多... |
|  | |
| List< string > | ClassNames `[get]` |
|  | 类别名称 更多... |
|  | |
| List< int > | ClassRoiIndexs `[get]` |
|  | ROI序号 更多... |
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

DL分类 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ClassNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassNums | | get |

类别个数

## ◆ Confidences

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Confidences | | get |

置信度

## ◆ ClassLabels

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassLabels | | get |

类别标签

## ◆ ClassProbs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ClassProbs | | get |

类别概率

## ◆ ClassNames

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassNames | | get |

类别名称

## ◆ ClassRoiIndexs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassRoiIndexs | | get |

ROI序号

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | get |

检测区域
