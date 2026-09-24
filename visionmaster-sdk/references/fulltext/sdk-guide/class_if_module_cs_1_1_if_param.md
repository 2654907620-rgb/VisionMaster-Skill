<!-- src:class_if_module_cs_1_1_if_param.html -->
<!-- path:接口函数 > 逻辑工具 > 条件检测 > IfParam -->
# IfParam类 参考 逻辑工具 » 条件检测

条件检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | LogicalModeEnum {     And = 0x1,     Or = 0x2   } |
|  | 逻辑处理模式 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| IfItemParam | GetIfItemParam (string strName) |
|  | 获取条件项参数（最大值/最小值等） 更多... |
|  | |
| ParamItem | GetDynamicParam (String strName) |
|  | 获取动态参数项（单例模式） 更多... |
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
| LogicalModeEnum | LogicalMode `[get, set]` |
|  | 逻辑处理模式 更多... |
|  | |

## 详细描述

条件检测参数

## 成员枚举类型说明

## ◆ LogicalModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LogicalModeEnum | | strong |

逻辑处理模式

| 枚举值 | |
| --- | --- |
| And | 全部 |
| Or | 任意 |

## 成员函数说明

## ◆ GetIfItemParam()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IfItemParam GetIfItemParam | ( | string | *strName* | ) |  |

获取条件项参数（最大值/最小值等）

参数
:   |  |  |
    | --- | --- |
    | strName | 条件项名称 |

返回
:   条件项参数

## ◆ GetDynamicParam()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ParamItem GetDynamicParam | ( | String | *strName* | ) |  |

获取动态参数项（单例模式）

参数
:   |  |  |
    | --- | --- |
    | strName | 参数名称 |

返回
:   参数项

**备注**

参数名称为"界面变量名\_参数用途" 如"int0\_Max"

## 属性说明

## ◆ LogicalMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | LogicalModeEnum LogicalMode | | getset |

逻辑处理模式
