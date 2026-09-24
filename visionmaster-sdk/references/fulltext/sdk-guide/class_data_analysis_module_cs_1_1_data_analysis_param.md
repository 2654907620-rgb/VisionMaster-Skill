<!-- src:class_data_analysis_module_cs_1_1_data_analysis_param.html -->
<!-- path:接口函数 > 通信 > 协议解析 > DataAnalysisParam -->
# DataAnalysisParam类 参考 通信 » 协议解析

协议解析参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | AnalysisTypeEnum {     TxtAnalytic = 0x0,     ScriptAnalytic = 0x1,     ByteAnalytic = 0x2   } |
|  | 方式选择 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< string > | Analysis `[set]` |
|  | 解析数据 更多... |
|  | |
| AnalysisTypeEnum | AnalysisType `[get, set]` |
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

协议解析参数

## 成员枚举类型说明

## ◆ AnalysisTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AnalysisTypeEnum | | strong |

方式选择

| 枚举值 | |
| --- | --- |
| TxtAnalytic | 文本解析 |
| ScriptAnalytic | 脚本解析 |
| ByteAnalytic | 字节解析 |

## 属性说明

## ◆ Analysis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Analysis | | set |

解析数据

**备注**

仅当次执行起效

## ◆ AnalysisType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AnalysisTypeEnum AnalysisType | | getset |

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
