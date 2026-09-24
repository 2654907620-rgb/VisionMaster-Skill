<!-- src:class_data_queue_module_cs_1_1_data_queue_param.html -->
<!-- path:接口函数 > 全局模块 > 数据队列 > DataQueueParam -->
# DataQueueParam类 参考 全局模块 » 数据队列

数据队列参数类
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoClearData () |
|  | 清空 更多... |
|  | |
| Public 成员函数 继承自 CModuleParamBase | |
| int | GetParamValue (String strName, ref String strValue) |
|  | 获取参数值 更多... |
|  | |
| int | SetParamValue (String strName, String strValue) |
|  | 设置参数值 更多... |
|  | |
| int | GetBinaryData (String strName, IntPtr pBinData, uint nMemSize, ref uint nDataLen) |
|  | 获取二进制数据 更多... |
|  | |
| int | SetBinaryData (String strName, IntPtr pBinData, uint nDataLen) |
|  | 设置二进制数据 更多... |
|  | |
| void | SetInputInt (String strName, int[] anIntVal) |
|  | 设置整型输入 更多... |
|  | |
| void | SetInputFloat (String strName, float[] anFloatVal) |
|  | 设置浮点型输入 更多... |
|  | |
| void | SetInputString (String strName, InputStringData[] astStrData) |
|  | 设置字符串型输入 更多... |
|  | |
| void | SetInputImage (InputImageData stImageData) |
|  | 设置图像型输入 更多... |
|  | |
| void | SetInputBytes (String strName, BytesData stBytesData) |
|  | 设置二进制数据型输入 更多... |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| bool | AsynchronousTrigger |
|  | 异步触发 更多... |
|  | |

## 详细描述

数据队列参数类

## 成员函数说明

## ◆ DoClearData()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoClearData | ( |  | ) |  |

清空

## 类成员变量说明

## ◆ AsynchronousTrigger

|  |
| --- |
| bool AsynchronousTrigger |

异步触发
