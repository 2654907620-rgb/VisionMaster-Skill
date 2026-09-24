<!-- src:class_shell_module_cs_1_1_shell_result.html -->
<!-- path:接口函数 > 逻辑工具 > 脚本 > ShellResult -->
# ShellResult类 参考 逻辑工具 » 脚本

脚本结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| IntDataArray | GetOutputInt (string strParam) |
|  | 获取整型结果 更多... |
|  | |
| FloatDataArray | GetOutputFloat (string strParam) |
|  | 获取浮点型结果 更多... |
|  | |
| StringDataArray | GetOutputString (string strParam) |
|  | 获取字符串型结果 更多... |
|  | |
| StringDataArray | GetOutputByteArray (string strParam) |
|  | 获取二进制数据型输出 更多... |
|  | |
| ImageDataArray | GetOutputImage (string strParam) |
|  | 获取图像型结果 更多... |
|  | |
| ImageBaseData | GetOutputImageV2 (string strParam) |
|  | 获取图像型结果 更多... |
|  | |
| List< PointF > | GetOutputPointArray (string strParam) |
|  | 获取点输出集合 更多... |
|  | |
| List< Line > | GetOutputLineArray (string strParam) |
|  | 获取直线输出集合 更多... |
|  | |
| List< Circle > | GetOutputCircleArray (string strParam) |
|  | 获取圆输出集合(弃用) 更多... |
|  | |
| List< RectBox > | GetOutputBoxArray (string strParam) |
|  | 获取带角度矩形输出集合 更多... |
|  | |
| List< RectF > | GetOutputRectArray (string strParam) |
|  | 获取无角度矩形(浮点型)输出集合 更多... |
|  | |
| List< Fixture > | GetOutputFixtureArray (string strParam) |
|  | 获取位置修正输出集合 更多... |
|  | |
| List< Annulus > | GetOutputAnnulusArray (string strParam) |
|  | 获取圆环输出集合 更多... |
|  | |
| List< Polygon > | GetOutputPolygonArray (string strParam) |
|  | 获取多边形输出集合 更多... |
|  | |
| List< Ellipse > | GetOutputEllipseArray (string strParam) |
|  | 获取椭圆输出集合 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| string | ResultShow `[get]` |
|  | 结果显示（废弃） 更多... |
|  | |
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

脚本结果

## 成员函数说明

## ◆ GetOutputInt()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntDataArray GetOutputInt | ( | string | *strParam* | ) |  |

获取整型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputFloat()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatDataArray GetOutputFloat | ( | string | *strParam* | ) |  |

获取浮点型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputString()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringDataArray GetOutputString | ( | string | *strParam* | ) |  |

获取字符串型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputByteArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringDataArray GetOutputByteArray | ( | string | *strParam* | ) |  |

获取二进制数据型输出

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageDataArray GetOutputImage | ( | string | *strParam* | ) |  |

获取图像型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputImageV2()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageBaseData GetOutputImageV2 | ( | string | *strParam* | ) |  |

获取图像型结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputPointArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<PointF> GetOutputPointArray | ( | string | *strParam* | ) |  |

获取点输出集合

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

获取直线输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputCircleArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Circle> GetOutputCircleArray | ( | string | *strParam* | ) |  |

获取圆输出集合(弃用)

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

获取带角度矩形输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputRectArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectF> GetOutputRectArray | ( | string | *strParam* | ) |  |

获取无角度矩形(浮点型)输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputFixtureArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Fixture> GetOutputFixtureArray | ( | string | *strParam* | ) |  |

获取位置修正输出集合

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

获取圆环输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## ◆ GetOutputPolygonArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Polygon> GetOutputPolygonArray | ( | string | *strParam* | ) |  |

获取多边形输出集合

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

获取椭圆输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 结果名称 |

返回
:   结果数据

## 属性说明

## ◆ ResultShow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string ResultShow | | get |

结果显示（废弃）

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态
