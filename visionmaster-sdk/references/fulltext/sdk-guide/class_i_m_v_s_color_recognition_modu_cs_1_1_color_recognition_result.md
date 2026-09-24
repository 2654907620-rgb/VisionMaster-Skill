<!-- src:class_i_m_v_s_color_recognition_modu_cs_1_1_color_recognition_result.html -->
<!-- path:接口函数 > 颜色处理 > 颜色识别 > ColorRecognitionResult -->
# ColorRecognitionResult类 参考 颜色处理 » 颜色识别

颜色识别结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| float | Confidence `[get]` |
|  | 置信度 更多... |
|  | |
| string | TopTypeName `[get]` |
|  | 最佳匹配名称 更多... |
|  | |
| float | TopScore `[get]` |
|  | 最佳分数 更多... |
|  | |
| List< string > | ColorTypeName `[get]` |
|  | 类别名 更多... |
|  | |
| List< float > | ColorScore `[get]` |
|  | 分数 更多... |
|  | |
| List< float > | ModelHData `[get]` |
|  | 模型H通道数据 更多... |
|  | |
| List< float > | ModelSData `[get]` |
|  | 模型S通道数据 更多... |
|  | |
| List< float > | ModelIData `[get]` |
|  | 模型I通道数据 更多... |
|  | |
| List< float > | SampleHData `[get]` |
|  | 样本H通道数据 更多... |
|  | |
| List< float > | SampleSData `[get]` |
|  | 样本S通道数据 更多... |
|  | |
| List< float > | SampleIData `[get]` |
|  | 样本I通道数据 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< int > | BlindPolygonPointNum `[get]` |
|  | 多边形点数 更多... |
|  | |
| List< PointF > | BlindPolygonPoints `[get]` |
|  | 多边形点集 更多... |
|  | |
| List< string > | BlindPolygonString `[get]` |
|  | 屏蔽区字符串 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

颜色识别结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ Confidence

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Confidence | | get |

置信度

## ◆ TopTypeName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string TopTypeName | | get |

最佳匹配名称

## ◆ TopScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TopScore | | get |

最佳分数

## ◆ ColorTypeName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ColorTypeName | | get |

类别名

## ◆ ColorScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ColorScore | | get |

分数

## ◆ ModelHData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ModelHData | | get |

模型H通道数据

## ◆ ModelSData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ModelSData | | get |

模型S通道数据

## ◆ ModelIData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ModelIData | | get |

模型I通道数据

## ◆ SampleHData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SampleHData | | get |

样本H通道数据

## ◆ SampleSData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SampleSData | | get |

样本S通道数据

## ◆ SampleIData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SampleIData | | get |

样本I通道数据

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ BlindPolygonPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BlindPolygonPointNum | | get |

多边形点数

## ◆ BlindPolygonPoints

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> BlindPolygonPoints | | get |

多边形点集

## ◆ BlindPolygonString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> BlindPolygonString | | get |

屏蔽区字符串
