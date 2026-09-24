<!-- src:class_i_m_v_s_cnn_register_segment_modu_c_cs_1_1_cnn_register_segment_c_result.html -->
<!-- path:接口函数 > 边缘学习 > 注册分割CPU > CnnRegisterSegmentCResult -->
# CnnRegisterSegmentCResult类 参考 边缘学习 » 注册分割CPU

注册分割 CPU结果
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
| List< float > | ObjArea `[get]` |
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
| ImageBaseData | ClassImage `[get]` |
|  | 类别图 更多... |
|  | |
| ImageBaseData | OutRenderImage `[get]` |
|  | 输出渲染图 更多... |
|  | |
| List< RectBox > | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< PointF > | ContourPoint `[get]` |
|  | 轮廓点 更多... |
|  | |
| List< int > | ContourNum `[get]` |
|  | 轮廓点个数 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

注册分割 CPU结果

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
| |  | | --- | | List<float> ObjArea | | get |

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

## ◆ ClassImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ClassImage | | get |

类别图

## ◆ OutRenderImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutRenderImage | | get |

输出渲染图

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域

## ◆ ContourPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ContourPoint | | get |

轮廓点

## ◆ ContourNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ContourNum | | get |

轮廓点个数
