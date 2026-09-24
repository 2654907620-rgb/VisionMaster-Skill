<!-- src:class_geometry_create_cs_1_1_geometry_create_param.html -->
<!-- path:接口函数 > 图形生成 > 几何创建 > GeometryCreateParam -->
# GeometryCreateParam类 参考 图形生成 » 几何创建

几何创建参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| List< Line > | InputLine `[set]` |
|  | 输入直线 更多... |
|  | |
| List< Annulus > | InputCircle `[set]` |
|  | 输入圆 更多... |
|  | |
| List< RectBox > | InputBox `[set]` |
|  | 输入Box 更多... |
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

几何创建参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ InputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine | | set |

输入直线

**备注**

仅当次执行起效

## ◆ InputCircle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> InputCircle | | set |

输入圆

**备注**

仅当次执行起效

## ◆ InputBox

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> InputBox | | set |

输入Box

**备注**

仅当次执行起效
