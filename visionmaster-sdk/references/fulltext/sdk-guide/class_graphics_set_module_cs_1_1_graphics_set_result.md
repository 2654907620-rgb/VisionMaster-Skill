<!-- src:class_graphics_set_module_cs_1_1_graphics_set_result.html -->
<!-- path:接口函数 > 逻辑工具 > 图形收集 > GraphicsSetResult -->
# GraphicsSetResult类 参考 逻辑工具 » 图形收集

图形收集结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| List< PointF > | GetOutputPointArray (string strParam) |
|  | 获取点数据 更多... |
|  | |
| List< Line > | GetOutputLineArray (string strParam) |
|  | 获取线数据 更多... |
|  | |
| List< RectBox > | GetOutputBoxArray (string strParam) |
|  | 获取矩形数据 更多... |
|  | |
| List< Annulus > | GetOutputAnnulusArray (string strParam) |
|  | 获取圆弧数据 更多... |
|  | |
| List< Ellipse > | GetOutputEllipseArray (string strParam) |
|  | 获取椭圆数据 更多... |
|  | |
| IntDataArray? | GetOutputInt (string strParam) |
|  | 获取输出状态 更多... |
|  | |
| StringDataArray? | GetOutputString (string strParam) |
|  | 获取字符串型结果 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

图形收集结果

## 成员函数说明

## ◆ GetOutputPointArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<PointF> GetOutputPointArray | ( | string | *strParam* | ) |  |

获取点数据

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputLineArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Line> GetOutputLineArray | ( | string | *strParam* | ) |  |

获取线数据

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputBoxArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectBox> GetOutputBoxArray | ( | string | *strParam* | ) |  |

获取矩形数据

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputAnnulusArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Annulus> GetOutputAnnulusArray | ( | string | *strParam* | ) |  |

获取圆弧数据

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputEllipseArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Ellipse> GetOutputEllipseArray | ( | string | *strParam* | ) |  |

获取椭圆数据

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputInt()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntDataArray? GetOutputInt | ( | string | *strParam* | ) |  |

获取输出状态

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

**备注**

结果为空时nValueNum为0且pIntVal和nReserved为null

## ◆ GetOutputString()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringDataArray? GetOutputString | ( | string | *strParam* | ) |  |

获取字符串型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

**备注**

结果为空时nValueNum为0且astStringVal和nReserved为null

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态
