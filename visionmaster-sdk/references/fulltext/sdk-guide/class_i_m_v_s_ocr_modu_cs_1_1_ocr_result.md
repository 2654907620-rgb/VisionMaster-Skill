<!-- src:class_i_m_v_s_ocr_modu_cs_1_1_ocr_result.html -->
<!-- path:接口函数 > 识别 > 字符识别 > OcrResult -->
# OcrResult类 参考 识别 » 字符识别

字符识别结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | RecognitionResultNum `[get]` |
|  | 识别结果数量 更多... |
|  | |
| int | CharNum `[get]` |
|  | 字符个数 更多... |
|  | |
| List< string > | Text `[get]` |
|  | 字符信息 更多... |
|  | |
| List< string > | SecondText `[get]` |
|  | 候选字符 更多... |
|  | |
| List< float > | CharScore `[get]` |
|  | 字符分数 更多... |
|  | |
| List< RectBox > | CharRect `[get]` |
|  | 字符框 更多... |
|  | |
| List< float > | CharBoxSkew `[get]` |
|  | 字符矩形倾斜度 更多... |
|  | |
| List< RectBox > | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< string > | Char0 `[get]` |
|  | 第一字符 更多... |
|  | |
| List< float > | Char0Score `[get]` |
|  | 第一字符得分 更多... |
|  | |
| List< string > | Char1 `[get]` |
|  | 第二字符 更多... |
|  | |
| List< float > | Char1Score `[get]` |
|  | 第二字符得分 更多... |
|  | |
| List< float > | Confidence `[get]` |
|  | 置信度 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

字符识别结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ RecognitionResultNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RecognitionResultNum | | get |

识别结果数量

## ◆ CharNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CharNum | | get |

字符个数

## ◆ Text

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Text | | get |

字符信息

## ◆ SecondText

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> SecondText | | get |

候选字符

## ◆ CharScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CharScore | | get |

字符分数

## ◆ CharRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> CharRect | | get |

字符框

## ◆ CharBoxSkew

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CharBoxSkew | | get |

字符矩形倾斜度

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域

## ◆ Char0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Char0 | | get |

第一字符

## ◆ Char0Score

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Char0Score | | get |

第一字符得分

## ◆ Char1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Char1 | | get |

第二字符

## ◆ Char1Score

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Char1Score | | get |

第二字符得分

## ◆ Confidence

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Confidence | | get |

置信度
