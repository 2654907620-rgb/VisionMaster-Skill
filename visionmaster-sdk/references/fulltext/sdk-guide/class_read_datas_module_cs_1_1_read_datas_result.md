<!-- src:class_read_datas_module_cs_1_1_read_datas_result.html -->
<!-- path:接口函数 > 通信 > 接收数据 > ReadDatasResult -->
# ReadDatasResult类 参考 通信 » 接收数据

接收数据结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| IntDataArray | GetOutputInt (string strParam) |
|  | 整型结果 更多... |
|  | |
| FloatDataArray | GetOutputFloat (string strParam) |
|  | 浮点型结果 更多... |
|  | |
| StringDataArray | GetOutputString (string strParam) |
|  | 字符型结果 更多... |
|  | |
| ByteArrayData | GetOutputByteArray (string strParam) |
|  | 二进制数据结果 更多... |
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

接收数据结果

## 成员函数说明

## ◆ GetOutputInt()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntDataArray GetOutputInt | ( | string | *strParam* | ) |  |

整型结果

## ◆ GetOutputFloat()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatDataArray GetOutputFloat | ( | string | *strParam* | ) |  |

浮点型结果

## ◆ GetOutputString()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringDataArray GetOutputString | ( | string | *strParam* | ) |  |

字符型结果

## ◆ GetOutputByteArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ByteArrayData GetOutputByteArray | ( | string | *strParam* | ) |  |

二进制数据结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态
