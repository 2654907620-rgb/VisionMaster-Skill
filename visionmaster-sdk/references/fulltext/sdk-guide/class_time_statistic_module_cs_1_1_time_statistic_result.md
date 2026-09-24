<!-- src:class_time_statistic_module_cs_1_1_time_statistic_result.html -->
<!-- path:接口函数 > 逻辑工具 > 耗时统计 > TimeStatisticResult -->
# TimeStatisticResult类 参考 逻辑工具 » 耗时统计

耗时统计结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| FloatDataArray | GetOutputFloat (string strParam) |
|  | 获取浮点型输出 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| float | Time `[get]` |
|  | 耗时（ms）（弃用） 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

耗时统计结果

## 成员函数说明

## ◆ GetOutputFloat()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatDataArray GetOutputFloat | ( | string | *strParam* | ) |  |

获取浮点型输出

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

## ◆ Time

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Time | | get |

耗时（ms）（弃用）
