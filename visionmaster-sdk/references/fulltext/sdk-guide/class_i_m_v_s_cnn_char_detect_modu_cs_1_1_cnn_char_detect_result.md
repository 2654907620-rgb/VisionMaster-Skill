<!-- src:class_i_m_v_s_cnn_char_detect_modu_cs_1_1_cnn_char_detect_result.html -->
<!-- path:接口函数 > 识别 > DL字符定位GPU > CnnCharDetectResult -->
# CnnCharDetectResult类 参考 识别 » DL字符定位GPU

DL字符定位 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | ObjNum `[get]` |
|  | 目标个数 更多... |
|  | |
| List< float > | ObjConf `[get]` |
|  | 目标置信度（弃用，推荐使用ObjectScore替代） 更多... |
|  | |
| List< float > | ObjectScore `[get, set]` |
|  | 目标分数 更多... |
|  | |
| List< int > | ObjStatus `[get]` |
|  | 目标状态 更多... |
|  | |
| List< RectBox > | TargetInfoRect `[get]` |
|  | 目标信息矩形 更多... |
|  | |
| RectBox | ROI `[get]` |
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

DL字符定位 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjNum | | get |

目标个数

## ◆ ObjConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjConf | | get |

目标置信度（弃用，推荐使用ObjectScore替代）

## ◆ ObjectScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectScore | | getset |

目标分数

## ◆ ObjStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjStatus | | get |

目标状态

## ◆ TargetInfoRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> TargetInfoRect | | get |

目标信息矩形

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域
