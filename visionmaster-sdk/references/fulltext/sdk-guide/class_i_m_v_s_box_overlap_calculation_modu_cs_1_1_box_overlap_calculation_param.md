<!-- src:class_i_m_v_s_box_overlap_calculation_modu_cs_1_1_box_overlap_calculation_param.html -->
<!-- path:接口函数 > 拆分组合 > Box重叠 > BoxOverlapCalculationParam -->
# BoxOverlapCalculationParam类 参考 拆分组合 » Box重叠

Box重叠参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< RectBox > | InputBOX1 `[set]` |
|  | 区域1 更多... |
|  | |
| List< RectBox > | InputBOX2 `[set]` |
|  | 区域2 更多... |
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

Box重叠参数

## 属性说明

## ◆ InputBOX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> InputBOX1 | | set |

区域1

**备注**

仅当次执行起效

## ◆ InputBOX2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> InputBOX2 | | set |

区域2

**备注**

仅当次执行起效
