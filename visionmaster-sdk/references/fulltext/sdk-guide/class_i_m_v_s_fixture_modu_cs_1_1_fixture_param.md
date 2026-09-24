<!-- src:class_i_m_v_s_fixture_modu_cs_1_1_fixture_param.html -->
<!-- path:接口函数 > 定位 > 位置修正 > FixtureParam -->
# FixtureParam类 参考 定位 » 位置修正

位置修正参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoFixtureInit () |
|  | 创建基准 更多... |
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
| List< PointF > | Origin `[set]` |
|  | 原点 更多... |
|  | |
| List< float > | InAngle `[set]` |
|  | 角度 更多... |
|  | |
| List< float > | MatchScaleX `[set]` |
|  | 尺度X 更多... |
|  | |
| List< float > | MatchScaleY `[set]` |
|  | 尺度Y 更多... |
|  | |

## 详细描述

位置修正参数

## 成员函数说明

## ◆ DoFixtureInit()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoFixtureInit | ( |  | ) |  |

创建基准

## 属性说明

## ◆ Origin

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> Origin | | set |

原点

**备注**

仅当次执行起效

## ◆ InAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> InAngle | | set |

角度

**备注**

仅当次执行起效

## ◆ MatchScaleX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MatchScaleX | | set |

尺度X

**备注**

仅当次执行起效

## ◆ MatchScaleY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MatchScaleY | | set |

尺度Y

**备注**

仅当次执行起效
