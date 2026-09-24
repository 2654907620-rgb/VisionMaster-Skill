<!-- src:class_i_m_v_s_ocr_dl_modu_c_cs_1_1_ocr_dl_c_result.html -->
<!-- path:接口函数 > 识别 > DL字符识别CPU > OcrDlCResult -->
# OcrDlCResult类 参考 识别 » DL字符识别CPU

DL字符识别 CPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | ROIStatus `[get]` |
|  | 检测区域状态 更多... |
|  | |
| List< string > | RoiSeq `[get]` |
|  | 检测序号 更多... |
|  | |
| List< int > | CharNum `[get]` |
|  | 字符个数 更多... |
|  | |
| List< float > | TextConf `[get]` |
|  | 字符串置信度 更多... |
|  | |
| List< string > | Text `[get]` |
|  | 字符信息 更多... |
|  | |
| List< string > | CharConf `[get]` |
|  | 字符置信度 更多... |
|  | |
| List< string > | OptimalTextOfROI `[get]` |
|  | 最佳字符串信息 更多... |
|  | |
| List< int > | CharNumOfROI `[get]` |
|  | 最优字符个数 更多... |
|  | |
| List< float > | TextConfOfROI `[get]` |
|  | 最优字符串置信度 更多... |
|  | |
| int | RoiNum `[get]` |
|  | 检测区域个数 更多... |
|  | |
| string | ModelFlag `[get]` |
|  | 模型标识 更多... |
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

DL字符识别 CPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ROIStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ROIStatus | | get |

检测区域状态

## ◆ RoiSeq

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> RoiSeq | | get |

检测序号

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

## ◆ Text

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Text | | get |

字符信息

## ◆ CharConf

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> CharConf | | get |

字符置信度

## ◆ OptimalTextOfROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> OptimalTextOfROI | | get |

最佳字符串信息

## ◆ CharNumOfROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CharNumOfROI | | get |

最优字符个数

## ◆ TextConfOfROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TextConfOfROI | | get |

最优字符串置信度

## ◆ RoiNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoiNum | | get |

检测区域个数

## ◆ ModelFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string ModelFlag | | get |

模型标识

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域
