<!-- src:class_data_set_module_cs_1_1_data_set_result.html -->
<!-- path:接口函数 > 逻辑工具 > 数据集合 > DataSetResult -->
# DataSetResult类 参考 逻辑工具 » 数据集合

数据集合结果
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

数据集合结果

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

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态
