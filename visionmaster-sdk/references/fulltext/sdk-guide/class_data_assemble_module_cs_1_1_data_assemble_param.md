<!-- src:class_data_assemble_module_cs_1_1_data_assemble_param.html -->
<!-- path:接口函数 > 通信 > 协议组装 > DataAssembleParam -->
# DataAssembleParam类 参考 通信 » 协议组装

协议组装参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | AssembleTypeEnum {     TxtAssemble = 0x0,     ScriptAssemble = 0x1   } |
|  | 方式选择 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| AssembleTypeEnum | AssembleType `[get, set]` |
|  | 方式选择 更多... |
|  | |
| string | Separator `[get, set]` |
|  | 分隔符 更多... |
|  | |
| string | PyScriptPath `[get, set]` |
|  | 路径选择 更多... |
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

协议组装参数

## 成员枚举类型说明

## ◆ AssembleTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AssembleTypeEnum | | strong |

方式选择

| 枚举值 | |
| --- | --- |
| TxtAssemble | 文本组装 |
| ScriptAssemble | 脚本组装 |

## 属性说明

## ◆ AssembleType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AssembleTypeEnum AssembleType | | getset |

方式选择

## ◆ Separator

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string Separator | | getset |

分隔符

## ◆ PyScriptPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string PyScriptPath | | getset |

路径选择
