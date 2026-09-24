<!-- src:class_i_m_v_s_single_point_align_modu_cs_1_1_single_point_align_param.html -->
<!-- path:接口函数 > 运算 > 单点对位 > SinglePointAlignParam -->
# SinglePointAlignParam类 参考 运算 » 单点对位

单点对位参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< PointF > | TargetPointInput `[set]` |
|  | 目标点输入 更多... |
|  | |
| List< float > | TargetAngle `[set]` |
|  | 目标角度 更多... |
|  | |
| List< PointF > | ObjectPointInput `[set]` |
|  | 对象点输入 更多... |
|  | |
| List< float > | ObjectAngle `[set]` |
|  | 对象角度 更多... |
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

单点对位参数

## 属性说明

## ◆ TargetPointInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput | | set |

目标点输入

**备注**

仅当次执行起效

## ◆ TargetAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TargetAngle | | set |

目标角度

**备注**

仅当次执行起效

## ◆ ObjectPointInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput | | set |

对象点输入

**备注**

仅当次执行起效

## ◆ ObjectAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjectAngle | | set |

对象角度

**备注**

仅当次执行起效
