<!-- src:class_branch_module___s_t_d_cs_1_1_branch_param.html -->
<!-- path:接口函数 > 逻辑工具 > 分支模块 > BranchParam -->
# BranchParam类 参考 逻辑工具 » 分支模块

分支模块参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | IndexUserSetEnum {     IndexByValue = 0,     IndexByBit = 1   } |
|  | 索引选择 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< int > | Inputint `[set]` |
|  | 结果标志 更多... |
|  | |
| IndexUserSetEnum | IndexUserSet `[get, set]` |
|  | 索引选择 更多... |
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

分支模块参数

## 成员枚举类型说明

## ◆ IndexUserSetEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum IndexUserSetEnum | | strong |

索引选择

| 枚举值 | |
| --- | --- |
| IndexByValue | 按值索引 |
| IndexByBit | 按位索引 |

## 属性说明

## ◆ Inputint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Inputint | | set |

结果标志

**备注**

仅当次执行起效

## ◆ IndexUserSet

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IndexUserSetEnum IndexUserSet | | getset |

索引选择
