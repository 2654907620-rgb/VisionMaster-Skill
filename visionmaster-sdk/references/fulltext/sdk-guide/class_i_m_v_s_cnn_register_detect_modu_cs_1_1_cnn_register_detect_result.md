<!-- src:class_i_m_v_s_cnn_register_detect_modu_cs_1_1_cnn_register_detect_result.html -->
<!-- path:接口函数 > 边缘学习 > 注册检测GPU > CnnRegisterDetectResult -->
# CnnRegisterDetectResult类 参考 边缘学习 » 注册检测GPU

注册检测 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | LabelTypeTotalCount `[get, set]` |
|  | 结果类别总数 更多... |
|  | |
| List< string > | LabelTypeName `[get, set]` |
|  | 结果类别名称 更多... |
|  | |
| List< int > | LabelTypeCount `[get, set]` |
|  | 结果类别个数 更多... |
|  | |
| int | ObjNum `[get]` |
|  | 目标个数 更多... |
|  | |
| List< int > | ObjClass `[get]` |
|  | 目标类别 更多... |
|  | |
| List< float > | ObjConf `[get]` |
|  | 目标置信度 更多... |
|  | |
| List< int > | ObjStatus `[get, set]` |
|  | 目标状态 更多... |
|  | |
| List< string > | ClassName `[get]` |
|  | 类别名称 更多... |
|  | |
| List< RectBox > | TargetInfoRect `[get]` |
|  | 目标信息矩形 更多... |
|  | |
| List< float > | ObjArea `[get]` |
|  | 目标面积 更多... |
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

注册检测 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ LabelTypeTotalCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LabelTypeTotalCount | | getset |

结果类别总数

## ◆ LabelTypeName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> LabelTypeName | | getset |

结果类别名称

## ◆ LabelTypeCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> LabelTypeCount | | getset |

结果类别个数

## ◆ ObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjNum | | get |

目标个数

## ◆ ObjClass

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjClass | | get |

目标类别

## ◆ ObjConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjConf | | get |

目标置信度

## ◆ ObjStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjStatus | | getset |

目标状态

## ◆ ClassName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassName | | get |

类别名称

## ◆ TargetInfoRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> TargetInfoRect | | get |

目标信息矩形

## ◆ ObjArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjArea | | get |

目标面积

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域
