<!-- src:class_branch_string_cpm_l_cs_1_1_branch_string_param.html -->
<!-- path:接口函数 > 逻辑工具 > 分支字符 > BranchStringParam -->
# BranchStringParam类 参考 逻辑工具 » 分支字符

分支字符参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| BranchStringItemParam | GetBranchStrItemParam (int branchID) |
|  | 获取分支模块单项配置参数 更多... |
|  | |
| List< BranchStringItemParam > | GetBranchStrItemParamList () |
|  | 获取所有分支字符项 更多... |
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
| 属性 | |
| List< string > | StringA `[set]` |
|  | 输入文本 更多... |
|  | |

## 详细描述

分支字符参数

## 成员函数说明

## ◆ GetBranchStrItemParam()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| BranchStringItemParam GetBranchStrItemParam | ( | int | *branchID* | ) |  |

获取分支模块单项配置参数

参数
:   |  |  |
    | --- | --- |
    | branchID | 分支模块ID |

返回
:   配置参数项

## ◆ GetBranchStrItemParamList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<BranchStringItemParam> GetBranchStrItemParamList | ( |  | ) |  |

获取所有分支字符项

返回
:   所有分支字符项

## 属性说明

## ◆ StringA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> StringA | | set |

输入文本

**备注**

仅当次执行起效
