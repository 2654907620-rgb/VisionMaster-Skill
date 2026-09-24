<!-- src:class_py_shell_module_cs_1_1_py_shell_param.html -->
<!-- path:接口函数 > 逻辑工具 > Python脚本 > PyShellParam -->
# PyShellParam类 参考 逻辑工具 » Python脚本

Python脚本参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetInputImage\_V2 (String strParamName, ImageBaseData stImageData) |
|  | 设置动态输入图像数据 更多... |
|  | |
| new void | SetInputBytes (String strName, BytesData stBytesData) |
|  | 设置二进制数据 更多... |
|  | |
| new void | SetInputString (String strName, InputStringData[] astStrData) |
|  | 设置String数据 更多... |
|  | |
| new void | SetInputInt (String strName, int[] anIntVal) |
|  | 设置Int数据 更多... |
|  | |
| new void | SetInputFloat (String strName, float[] anFloatVal) |
|  | 设置Float数据 更多... |
|  | |
| void | SetInputBox (string strParamName, List< RectBox > stRoiBox) |
|  | 设置动态输入矩形框数据 更多... |
|  | |
| void | SetInputAnnulus (string strParamName, List< Annulus > stAnnulus) |
|  | 设置动态输入圆环ROI数据 更多... |
|  | |
| void | SetInputEllipse (string strParamName, List< Ellipse > stEllipse) |
|  | 设置动态输入椭圆形数据 更多... |
|  | |
| void | SetInputLine (string strParamName, List< Line > stLine) |
|  | 设置动态输入线型数据 更多... |
|  | |
| void | SetInputPoint (string strParamName, List< PointF > stPointF) |
|  | 设置动态输入点型数据 更多... |
|  | |
| void | SetInputFixture (string strParamName, Fixture stFixture) |
|  | 设置动态输入位置修正数据 更多... |
|  | |
| void | SetInputRect (string strParamName, List< RectF > stRectF) |
|  | 设置动态输入矩形数据 更多... |
|  | |
| void | SetInputPolygon (string strParamName, List< Polygon > stPolygon) |
|  | 设置动态输入多边形数据 更多... |
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

Python脚本参数

## 成员函数说明

## ◆ SetInputImage\_V2()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputImage\_V2 | ( | String | *strParamName*, |
|  |  | ImageBaseData | *stImageData* |
|  | ) |  |  |

设置动态输入图像数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stImageData | 图像数据 |

**备注**

仅当次执行起效

## ◆ SetInputBytes()

|  |  |  |  |
| --- | --- | --- | --- |
| new void SetInputBytes | ( | String | *strName*, |
|  |  | BytesData | *stBytesData* |
|  | ) |  |  |

设置二进制数据

参数
:   |  |  |
    | --- | --- |
    | strName | 输入名称 |
    | stBytesData | 二进制数据 |

**备注**

仅当次执行起效

## ◆ SetInputString()

|  |  |  |  |
| --- | --- | --- | --- |
| new void SetInputString | ( | String | *strName*, |
|  |  | InputStringData [] | *astStrData* |
|  | ) |  |  |

设置String数据

参数
:   |  |  |
    | --- | --- |
    | strName | 输入名称 |
    | astStrData | string数据 |

**备注**

仅当次执行起效

## ◆ SetInputInt()

|  |  |  |  |
| --- | --- | --- | --- |
| new void SetInputInt | ( | String | *strName*, |
|  |  | int [] | *anIntVal* |
|  | ) |  |  |

设置Int数据

参数
:   |  |  |
    | --- | --- |
    | strName | 输入名称 |
    | anIntVal | int数据 |

**备注**

仅当次执行起效

## ◆ SetInputFloat()

|  |  |  |  |
| --- | --- | --- | --- |
| new void SetInputFloat | ( | String | *strName*, |
|  |  | float [] | *anFloatVal* |
|  | ) |  |  |

设置Float数据

参数
:   |  |  |
    | --- | --- |
    | strName | 输入名称 |
    | anFloatVal | float数据 |

**备注**

仅当次执行起效

## ◆ SetInputBox()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputBox | ( | string | *strParamName*, |
|  |  | List< RectBox > | *stRoiBox* |
|  | ) |  |  |

设置动态输入矩形框数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stRoiBox | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputAnnulus()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputAnnulus | ( | string | *strParamName*, |
|  |  | List< Annulus > | *stAnnulus* |
|  | ) |  |  |

设置动态输入圆环ROI数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stAnnulus | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputEllipse()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputEllipse | ( | string | *strParamName*, |
|  |  | List< Ellipse > | *stEllipse* |
|  | ) |  |  |

设置动态输入椭圆形数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stEllipse | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputLine()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputLine | ( | string | *strParamName*, |
|  |  | List< Line > | *stLine* |
|  | ) |  |  |

设置动态输入线型数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stLine | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputPoint()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputPoint | ( | string | *strParamName*, |
|  |  | List< PointF > | *stPointF* |
|  | ) |  |  |

设置动态输入点型数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stPointF | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputFixture()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputFixture | ( | string | *strParamName*, |
|  |  | Fixture | *stFixture* |
|  | ) |  |  |

设置动态输入位置修正数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stFixture | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputRect()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputRect | ( | string | *strParamName*, |
|  |  | List< RectF > | *stRectF* |
|  | ) |  |  |

设置动态输入矩形数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stRectF | 输入数据 |

**备注**

仅当次执行起效

## ◆ SetInputPolygon()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputPolygon | ( | string | *strParamName*, |
|  |  | List< Polygon > | *stPolygon* |
|  | ) |  |  |

设置动态输入多边形数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 输入名称 |
    | stPolygon | 输入数据 |

**备注**

仅当次执行起效
