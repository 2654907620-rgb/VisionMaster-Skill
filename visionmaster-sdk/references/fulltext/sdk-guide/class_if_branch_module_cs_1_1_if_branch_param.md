<!-- src:class_if_branch_module_cs_1_1_if_branch_param.html -->
<!-- path:接口函数 > 逻辑工具 > 条件分支 > IfBranchParam -->
# IfBranchParam类 参考 逻辑工具 » 条件分支

条件分支参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | BranchStateEnum {     BranchState\_OK = 0x1,     BranchState\_NG = 0x2   } |
|  | 条件判断 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | GetIntMinValue (string strName) |
|  | 获取整型条件项的最小值 更多... |
|  | |
| void | SetIntMinValue (string strName, int nMin) |
|  | 设置整型条件项的最小值 更多... |
|  | |
| double | GetFloatMinValue (string strName) |
|  | 获取浮点条件项的最小值 更多... |
|  | |
| void | SetFloatMinValue (string strName, double dMin) |
|  | 设置浮点条件项的最小值 更多... |
|  | |
| int | GetIntMaxValue (string strName) |
|  | 获取整型条件项的最大值 更多... |
|  | |
| void | SetIntMaxValue (string strName, int nMax) |
|  | 设置整型条件项的最大值 更多... |
|  | |
| double | GetFloatMaxValue (string strName) |
|  | 获取浮点条件项的最大值 更多... |
|  | |
| void | SetFloatMaxValue (string strName, double dMax) |
|  | 设置浮点条件项的最大值 更多... |
|  | |
| BranchStateEnum | GetStateValue (string strName) |
|  | 获取条件项判断选项 更多... |
|  | |
| void | SetStateValue (string strName, BranchStateEnum eState) |
|  | 设置条件项判断选项 更多... |
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

## 详细描述

条件分支参数

## 成员枚举类型说明

## ◆ BranchStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum BranchStateEnum | | strong |

条件判断

| 枚举值 | |
| --- | --- |
| BranchState\_OK | OK |
| BranchState\_NG | NG |

## 成员函数说明

## ◆ GetIntMinValue()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int GetIntMinValue | ( | string | *strName* | ) |  |

获取整型条件项的最小值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项最小值

## ◆ SetIntMinValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetIntMinValue | ( | string | *strName*, |
|  |  | int | *nMin* |
|  | ) |  |  |

设置整型条件项的最小值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |
    | nMin | 条件项值 |

## ◆ GetFloatMinValue()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| double GetFloatMinValue | ( | string | *strName* | ) |  |

获取浮点条件项的最小值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项最小值

## ◆ SetFloatMinValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetFloatMinValue | ( | string | *strName*, |
|  |  | double | *dMin* |
|  | ) |  |  |

设置浮点条件项的最小值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |
    | dMin | 条件项值 |

## ◆ GetIntMaxValue()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int GetIntMaxValue | ( | string | *strName* | ) |  |

获取整型条件项的最大值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项最大值

## ◆ SetIntMaxValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetIntMaxValue | ( | string | *strName*, |
|  |  | int | *nMax* |
|  | ) |  |  |

设置整型条件项的最大值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |
    | nMax | 条件项值 |

## ◆ GetFloatMaxValue()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| double GetFloatMaxValue | ( | string | *strName* | ) |  |

获取浮点条件项的最大值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项最大值

## ◆ SetFloatMaxValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetFloatMaxValue | ( | string | *strName*, |
|  |  | double | *dMax* |
|  | ) |  |  |

设置浮点条件项的最大值

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |
    | dMax | 条件项值 |

## ◆ GetStateValue()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| BranchStateEnum GetStateValue | ( | string | *strName* | ) |  |

获取条件项判断选项

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项判断选项

## ◆ SetStateValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetStateValue | ( | string | *strName*, |
|  |  | BranchStateEnum | *eState* |
|  | ) |  |  |

设置条件项判断选项

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |
    | eState | 条件项中的判断项 |
