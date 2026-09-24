<!-- src:class_i_m_v_s_cnn_single_char_detect_modu_cs_1_1_cnn_single_char_detect_result.html -->
<!-- path:接口函数 > 识别 > DL单字符检测GPU > CnnSingleCharDetectResult -->
# CnnSingleCharDetectResult类 参考 识别 » DL单字符检测GPU

DL单字符检测 GPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | TextLineNum `[get]` |
|  | 文本行个数 更多... |
|  | |
| List< int > | TextLineStatus `[get]` |
|  | 文本行状态 更多... |
|  | |
| List< float > | CharConf `[get]` |
|  | 字符置信度 更多... |
|  | |
| List< int > | MarkStatus `[get]` |
|  | 字符状态 更多... |
|  | |
| List< string > | Text `[get]` |
|  | 字符信息 更多... |
|  | |
| List< string > | StringInfo `[get]` |
|  | 字符串信息 更多... |
|  | |
| List< int > | CharNum `[get]` |
|  | 字符个数 更多... |
|  | |
| List< float > | TextConf `[get]` |
|  | 字符串置信度 更多... |
|  | |
| List< string > | RoiSeq `[get]` |
|  | 检测序号 更多... |
|  | |
| List< RectBox > | CharInfoRect `[get]` |
|  | 字符信息矩形 更多... |
|  | |
| List< RectBox > | TextBox `[get]` |
|  | 文本框信息 更多... |
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

DL单字符检测 GPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ TextLineNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TextLineNum | | get |

文本行个数

## ◆ TextLineStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> TextLineStatus | | get |

文本行状态

## ◆ CharConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CharConf | | get |

字符置信度

## ◆ MarkStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MarkStatus | | get |

字符状态

## ◆ Text

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Text | | get |

字符信息

## ◆ StringInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> StringInfo | | get |

字符串信息

## ◆ CharNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CharNum | | get |

字符个数

## ◆ TextConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TextConf | | get |

字符串置信度

## ◆ RoiSeq

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> RoiSeq | | get |

检测序号

## ◆ CharInfoRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CharInfoRect | | get |

字符信息矩形

## ◆ TextBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> TextBox | | get |

文本框信息

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域
