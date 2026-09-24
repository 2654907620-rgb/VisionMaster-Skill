<!-- src:class_i_m_v_s_cnn_register_multiclass_classification_modu_c_cs_1_1_cnn_register_multiclass_classification_c_result.html -->
<!-- path:接口函数 > 边缘学习 > 多类别分类CPU > CnnRegisterMulticlassClassificationCResult -->
# CnnRegisterMulticlassClassificationCResult类 参考 边缘学习 » 多类别分类CPU

多类别分类 CPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get, set]` |
|  | 模块状态 更多... |
|  | |
| int | ResultTotalCount `[get, set]` |
|  | 类别总数 更多... |
|  | |
| List< int > | ClassNums `[get, set]` |
|  | 类别个数 更多... |
|  | |
| List< float > | Similaritys `[get, set]` |
|  | 相似度 更多... |
|  | |
| List< string > | ClassNames `[get, set]` |
|  | 类别名称 更多... |
|  | |
| List< string > | LabelColor `[get, set]` |
|  | 标签颜色 更多... |
|  | |
| List< int > | ClassRoiIndexs `[get, set]` |
|  | ROI序号 更多... |
|  | |
| List< RectBox > | DetectROIs `[get, set]` |
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

多类别分类 CPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | getset |

模块状态

## ◆ ResultTotalCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ResultTotalCount | | getset |

类别总数

## ◆ ClassNums

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassNums | | getset |

类别个数

## ◆ Similaritys

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Similaritys | | getset |

相似度

## ◆ ClassNames

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassNames | | getset |

类别名称

## ◆ LabelColor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> LabelColor | | getset |

标签颜色

## ◆ ClassRoiIndexs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClassRoiIndexs | | getset |

ROI序号

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | getset |

检测区域
