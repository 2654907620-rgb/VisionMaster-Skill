<!-- src:class_i_m_v_s_cnn_instance_segment_modu_c_cs_1_1_cnn_instance_segment_c_result.html -->
<!-- path:接口函数 > 深度学习 > DL实例分割CPU > CnnInstanceSegmentCResult -->
# CnnInstanceSegmentCResult类 参考 深度学习 » DL实例分割CPU

DL实例分割 CPU结果
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
| List< int > | ObjClass `[get]` |
|  | 目标类别 更多... |
|  | |
| List< float > | ObjConf `[get]` |
|  | 目标置信度 更多... |
|  | |
| List< int > | ObjPixel `[get]` |
|  | 目标像素值 更多... |
|  | |
| List< int > | ObjArea `[get]` |
|  | 目标面积 更多... |
|  | |
| List< int > | ObjStatus `[get]` |
|  | 目标状态 更多... |
|  | |
| List< string > | ClassName `[get]` |
|  | 类别名称 更多... |
|  | |
| List< RectBox > | TargetInfoRect `[get]` |
|  | 目标信息矩形 更多... |
|  | |
| ImageBaseData | OutMaskImage `[get]` |
|  | 输出掩膜图 更多... |
|  | |
| ImageBaseData | OutRenderImage `[get]` |
|  | 输出渲染图 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< PointF > | PolyonContourPoint `[get]` |
|  | 多边形轮廓点 更多... |
|  | |
| List< int > | EdgePointNum `[get]` |
|  | 边缘点个数 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

DL实例分割 CPU结果

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

## ◆ ObjPixel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjPixel | | get |

目标像素值

## ◆ ObjArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjArea | | get |

目标面积

## ◆ ObjStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ObjStatus | | get |

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

## ◆ OutMaskImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutMaskImage | | get |

输出掩膜图

## ◆ OutRenderImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutRenderImage | | get |

输出渲染图

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ PolyonContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> PolyonContourPoint | | get |

多边形轮廓点

## ◆ EdgePointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgePointNum | | get |

边缘点个数
