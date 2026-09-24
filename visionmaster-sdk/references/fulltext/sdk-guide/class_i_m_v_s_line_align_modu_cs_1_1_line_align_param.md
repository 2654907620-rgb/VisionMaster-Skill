<!-- src:class_i_m_v_s_line_align_modu_cs_1_1_line_align_param.html -->
<!-- path:接口函数 > 运算 > 线对位 > LineAlignParam -->
# LineAlignParam类 参考 运算 » 线对位

线对位参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | AlignModeEnum {     Open = 0,     Close = 1   } |
|  | 对位形状 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< Line > | TargetLineInput1 `[set]` |
|  | 目标线输入1 更多... |
|  | |
| List< float > | TargetLineAngle1 `[set]` |
|  | 目标线角度1 更多... |
|  | |
| List< Line > | ObjectLineInput1 `[set]` |
|  | 对象线输入1 更多... |
|  | |
| List< float > | ObjectLineAngle1 `[set]` |
|  | 对象线角度1 更多... |
|  | |
| List< Line > | TargetLineInput2 `[set]` |
|  | 目标线输入2 更多... |
|  | |
| List< float > | TargetLineAngle2 `[set]` |
|  | 目标线角度2 更多... |
|  | |
| List< Line > | ObjectLineInput2 `[set]` |
|  | 对象线输入2 更多... |
|  | |
| List< float > | ObjectLineAngle2 `[set]` |
|  | 对象线角度2 更多... |
|  | |
| List< Line > | TargetLineInput3 `[set]` |
|  | 目标线输入3 更多... |
|  | |
| List< float > | TargetLineAngle3 `[set]` |
|  | 目标线角度3 更多... |
|  | |
| List< Line > | ObjectLineInput3 `[set]` |
|  | 对象线输入3 更多... |
|  | |
| List< float > | ObjectLineAngle3 `[set]` |
|  | 对象线角度3 更多... |
|  | |
| List< Line > | TargetLineInput4 `[set]` |
|  | 目标线输入4 更多... |
|  | |
| List< float > | TargetLineAngle4 `[set]` |
|  | 目标线角度4 更多... |
|  | |
| List< Line > | ObjectLineInput4 `[set]` |
|  | 对象线输入4 更多... |
|  | |
| List< float > | ObjectLineAngle4 `[set]` |
|  | 对象线角度4 更多... |
|  | |
| List< Line > | TargetLineInput5 `[set]` |
|  | 目标线输入5 更多... |
|  | |
| List< float > | TargetLineAngle5 `[set]` |
|  | 目标线角度5 更多... |
|  | |
| List< Line > | ObjectLineInput5 `[set]` |
|  | 对象线输入5 更多... |
|  | |
| List< float > | ObjectLineAngle5 `[set]` |
|  | 对象线角度5 更多... |
|  | |
| List< Line > | TargetLineInput6 `[set]` |
|  | 目标线输入6 更多... |
|  | |
| List< float > | TargetLineAngle6 `[set]` |
|  | 目标线角度6 更多... |
|  | |
| List< Line > | ObjectLineInput6 `[set]` |
|  | 对象线输入6 更多... |
|  | |
| List< float > | ObjectLineAngle6 `[set]` |
|  | 对象线角度6 更多... |
|  | |
| List< Line > | TargetLineInput7 `[set]` |
|  | 目标线输入7 更多... |
|  | |
| List< float > | TargetLineAngle7 `[set]` |
|  | 目标线角度7 更多... |
|  | |
| List< Line > | ObjectLineInput7 `[set]` |
|  | 对象线输入7 更多... |
|  | |
| List< float > | ObjectLineAngle7 `[set]` |
|  | 对象线角度7 更多... |
|  | |
| List< Line > | TargetLineInput8 `[set]` |
|  | 目标线输入8 更多... |
|  | |
| List< float > | TargetLineAngle8 `[set]` |
|  | 目标线角度8 更多... |
|  | |
| List< Line > | ObjectLineInput8 `[set]` |
|  | 对象线输入8 更多... |
|  | |
| List< float > | ObjectLineAngle8 `[set]` |
|  | 对象线角度8 更多... |
|  | |
| AlignModeEnum | AlignMode `[get, set]` |
|  | 对位形状 更多... |
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

线对位参数

## 成员枚举类型说明

## ◆ AlignModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AlignModeEnum | | strong |

对位形状

| 枚举值 | |
| --- | --- |
| Open | 开 |
| Close | 闭 |

## 属性说明

## ◆ TargetLineInput1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput1 | | set |

目标线输入1

**备注**

仅当次执行起效

## ◆ TargetLineAngle1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle1 | | set |

目标线角度1

**备注**

仅当次执行起效

## ◆ ObjectLineInput1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput1 | | set |

对象线输入1

**备注**

仅当次执行起效

## ◆ ObjectLineAngle1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle1 | | set |

对象线角度1

**备注**

仅当次执行起效

## ◆ TargetLineInput2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput2 | | set |

目标线输入2

**备注**

仅当次执行起效

## ◆ TargetLineAngle2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle2 | | set |

目标线角度2

**备注**

仅当次执行起效

## ◆ ObjectLineInput2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput2 | | set |

对象线输入2

**备注**

仅当次执行起效

## ◆ ObjectLineAngle2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle2 | | set |

对象线角度2

**备注**

仅当次执行起效

## ◆ TargetLineInput3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput3 | | set |

目标线输入3

**备注**

仅当次执行起效

## ◆ TargetLineAngle3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle3 | | set |

目标线角度3

**备注**

仅当次执行起效

## ◆ ObjectLineInput3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput3 | | set |

对象线输入3

**备注**

仅当次执行起效

## ◆ ObjectLineAngle3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle3 | | set |

对象线角度3

**备注**

仅当次执行起效

## ◆ TargetLineInput4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput4 | | set |

目标线输入4

**备注**

仅当次执行起效

## ◆ TargetLineAngle4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle4 | | set |

目标线角度4

**备注**

仅当次执行起效

## ◆ ObjectLineInput4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput4 | | set |

对象线输入4

**备注**

仅当次执行起效

## ◆ ObjectLineAngle4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle4 | | set |

对象线角度4

**备注**

仅当次执行起效

## ◆ TargetLineInput5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput5 | | set |

目标线输入5

**备注**

仅当次执行起效

## ◆ TargetLineAngle5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle5 | | set |

目标线角度5

**备注**

仅当次执行起效

## ◆ ObjectLineInput5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput5 | | set |

对象线输入5

**备注**

仅当次执行起效

## ◆ ObjectLineAngle5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle5 | | set |

对象线角度5

**备注**

仅当次执行起效

## ◆ TargetLineInput6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput6 | | set |

目标线输入6

**备注**

仅当次执行起效

## ◆ TargetLineAngle6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle6 | | set |

目标线角度6

**备注**

仅当次执行起效

## ◆ ObjectLineInput6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput6 | | set |

对象线输入6

**备注**

仅当次执行起效

## ◆ ObjectLineAngle6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle6 | | set |

对象线角度6

**备注**

仅当次执行起效

## ◆ TargetLineInput7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput7 | | set |

目标线输入7

**备注**

仅当次执行起效

## ◆ TargetLineAngle7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle7 | | set |

目标线角度7

**备注**

仅当次执行起效

## ◆ ObjectLineInput7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput7 | | set |

对象线输入7

**备注**

仅当次执行起效

## ◆ ObjectLineAngle7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle7 | | set |

对象线角度7

**备注**

仅当次执行起效

## ◆ TargetLineInput8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> TargetLineInput8 | | set |

目标线输入8

**备注**

仅当次执行起效

## ◆ TargetLineAngle8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetLineAngle8 | | set |

目标线角度8

**备注**

仅当次执行起效

## ◆ ObjectLineInput8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> ObjectLineInput8 | | set |

对象线输入8

**备注**

仅当次执行起效

## ◆ ObjectLineAngle8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectLineAngle8 | | set |

对象线角度8

**备注**

仅当次执行起效

## ◆ AlignMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AlignModeEnum AlignMode | | getset |

对位形状
