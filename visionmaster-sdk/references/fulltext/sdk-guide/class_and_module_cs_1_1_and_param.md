<!-- src:class_and_module_cs_1_1_and_param.html -->
<!-- path:接口函数 > 逻辑工具 > 逻辑 > AndParam -->
# AndParam类 参考 逻辑工具 » 逻辑

逻辑参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | LogicalModeEnum {     And = 0x1,     Or = 0x2,     Not = 0x5,     AndNot = 0x3,     OrNot = 0x4   } |
|  | 逻辑处理模式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| LogicalModeEnum | LogicalMode `[get, set]` |
|  | 逻辑处理模式 更多... |
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

逻辑参数

## 成员枚举类型说明

## ◆ LogicalModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LogicalModeEnum | | strong |

逻辑处理模式

| 枚举值 | |
| --- | --- |
| And | 与 |
| Or | 或 |
| Not | 非 |
| AndNot | 与非 |
| OrNot | 或非 |

## 属性说明

## ◆ LogicalMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | LogicalModeEnum LogicalMode | | getset |

逻辑处理模式
