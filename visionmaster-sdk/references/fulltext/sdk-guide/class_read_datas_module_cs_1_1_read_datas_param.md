<!-- src:class_read_datas_module_cs_1_1_read_datas_param.html -->
<!-- path:接口函数 > 通信 > 接收数据 > ReadDatasParam -->
# ReadDatasParam类 参考 通信 » 接收数据

接收数据参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| int | RowNum `[get, set]` |
|  | 获取行数，范围：[1,256] 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
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

## 详细描述

接收数据参数

## 属性说明

## ◆ RowNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RowNum | | getset |

获取行数，范围：[1,256]
