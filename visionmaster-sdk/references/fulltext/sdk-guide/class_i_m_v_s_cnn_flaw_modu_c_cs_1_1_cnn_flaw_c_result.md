<!-- src:class_i_m_v_s_cnn_flaw_modu_c_cs_1_1_cnn_flaw_c_result.html -->
<!-- path:接口函数 > 深度学习 > DL图像分割CPU > CnnFlawCResult -->
# CnnFlawCResult类 参考 深度学习 » DL图像分割CPU

DL图像分割 CPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | ScoreHistogram `[get]` |
|  | 概率直方图 更多... |
|  | |
| int | MinScore `[get]` |
|  | 最小分数 更多... |
|  | |
| ImageBaseData | ClassImageData `[get]` |
|  | 类别图 更多... |
|  | |
| List< string > | ClassName `[get]` |
|  | 类别名称 更多... |
|  | |
| List< int > | GrayValue `[get]` |
|  | 灰度值 更多... |
|  | |
| ImageBaseData | ScoreImageData `[get]` |
|  | 缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw1ScoreImageData `[get]` |
|  | 输出类别中第1个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw2ScoreImageData `[get]` |
|  | 输出类别中第2个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw3ScoreImageData `[get]` |
|  | 输出类别中第3个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw4ScoreImageData `[get]` |
|  | 输出类别中第4个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw5ScoreImageData `[get]` |
|  | 输出类别中第5个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw6ScoreImageData `[get]` |
|  | 输出类别中第6个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw7ScoreImageData `[get]` |
|  | 输出类别中第7个类别对应的缺陷概率图 更多... |
|  | |
| ImageBaseData | Flaw8ScoreImageData `[get]` |
|  | 输出类别中第8个类别对应的缺陷概率图 更多... |
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

DL图像分割 CPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ ScoreHistogram

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ScoreHistogram | | get |

概率直方图

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinScore | | get |

最小分数

## ◆ ClassImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ClassImageData | | get |

类别图

## ◆ ClassName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassName | | get |

类别名称

## ◆ GrayValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> GrayValue | | get |

灰度值

## ◆ ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ScoreImageData | | get |

缺陷概率图

## ◆ Flaw1ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw1ScoreImageData | | get |

输出类别中第1个类别对应的缺陷概率图

## ◆ Flaw2ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw2ScoreImageData | | get |

输出类别中第2个类别对应的缺陷概率图

## ◆ Flaw3ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw3ScoreImageData | | get |

输出类别中第3个类别对应的缺陷概率图

## ◆ Flaw4ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw4ScoreImageData | | get |

输出类别中第4个类别对应的缺陷概率图

## ◆ Flaw5ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw5ScoreImageData | | get |

输出类别中第5个类别对应的缺陷概率图

## ◆ Flaw6ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw6ScoreImageData | | get |

输出类别中第6个类别对应的缺陷概率图

## ◆ Flaw7ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw7ScoreImageData | | get |

输出类别中第7个类别对应的缺陷概率图

## ◆ Flaw8ScoreImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData Flaw8ScoreImageData | | get |

输出类别中第8个类别对应的缺陷概率图

## ◆ DetectROIs

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> DetectROIs | | get |

检测区域
