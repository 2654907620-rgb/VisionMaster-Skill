<!-- src:class_data_queue_module_cs_1_1_data_queue_module_tool.html -->
<!-- path:接口函数 > 全局模块 > 数据队列 > DataQueueModuleTool -->
# DataQueueModuleTool类 参考 全局模块 » 数据队列

数据队列
更多...

继承自 VmModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetIntData (IntValue stVal) |
|  | 设置整型数据 更多... |
|  | |
| void | SetFloatData (FloatValue stVal) |
|  | 设置浮点型数据 更多... |
|  | |
| void | SetStringData (StringValue stVal) |
|  | 设置字符串型数据 更多... |
|  | |
| IntValue | GetIntData (int nIndex) |
|  | 获取指定索引的整型数据 更多... |
|  | |
| FloatValue | GetFloatData (int nIndex) |
|  | 获取指定索引的浮点型数据 更多... |
|  | |
| StringValue | GetStringData (int nIndex) |
|  | 获取指定索引的字符串型数据 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| DataQueueParam | ModuParams `[get, set]` |
|  | 模块参数对象 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 属性 继承自 VmModule | |
| ModuResultMemoryTypeEnum | ModuResultMemType |
|  | 模块结果内存管理类型 更多... |
|  | |

## 详细描述

数据队列

## 成员函数说明

## ◆ SetIntData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetIntData | ( | IntValue | *stVal* | ) |  |

设置整型数据

## ◆ SetFloatData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetFloatData | ( | FloatValue | *stVal* | ) |  |

设置浮点型数据

## ◆ SetStringData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetStringData | ( | StringValue | *stVal* | ) |  |

设置字符串型数据

## ◆ GetIntData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntValue GetIntData | ( | int | *nIndex* | ) |  |

获取指定索引的整型数据

## ◆ GetFloatData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatValue GetFloatData | ( | int | *nIndex* | ) |  |

获取指定索引的浮点型数据

## ◆ GetStringData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringValue GetStringData | ( | int | *nIndex* | ) |  |

获取指定索引的字符串型数据

## 属性说明

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DataQueueParam ModuParams | | getset |

模块参数对象
