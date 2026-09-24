<!-- src:class_i_m_v_s_cnn_register_presence_detect_modu_c_cs_1_1_cnn_register_presence_detect_c_result.html -->
<!-- path:接口函数 > 边缘学习 > 有无检测CPU > CnnRegisterPresenceDetectCResult -->
# CnnRegisterPresenceDetectCResult类 参考 边缘学习 » 有无检测CPU

有无检测 CPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get, set]` |
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
| int | ObjNum `[get, set]` |
|  | 目标个数 更多... |
|  | |
| List< int > | ObjClass `[get, set]` |
|  | 目标类别 更多... |
|  | |
| List< float > | ObjConf `[get, set]` |
|  | 目标置信度 更多... |
|  | |
| List< int > | ObjStatus `[get, set]` |
|  | 目标状态 更多... |
|  | |
| List< string > | ClassName `[get, set]` |
|  | 类别名称 更多... |
|  | |
| List< string > | LabelColor `[get, set]` |
|  | 标签颜色 更多... |
|  | |
| List< RectBox > | TargetInfoRect `[get, set]` |
|  | 目标信息矩形 更多... |
|  | |
| List< float > | ObjArea `[get, set]` |
|  | 目标面积 更多... |
|  | |
| List< RectBox > | ROI `[get, set]` |
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

有无检测 CPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | getset |

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
| |  | | --- | | int ObjNum | | getset |

目标个数

## ◆ ObjClass

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjClass | | getset |

目标类别

## ◆ ObjConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjConf | | getset |

目标置信度

## ◆ ObjStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjStatus | | getset |

目标状态

## ◆ ClassName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassName | | getset |

类别名称

## ◆ LabelColor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> LabelColor | | getset |

标签颜色

## ◆ TargetInfoRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> TargetInfoRect | | getset |

目标信息矩形

## ◆ ObjArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjArea | | getset |

目标面积

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | getset |

检测区域
