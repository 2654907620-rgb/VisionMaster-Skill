<!-- src:interface_v_m_1_1_platform_s_d_k_c_s_1_1_i_var_module.html -->
<!-- path:接口函数 > 公共模块 > 变量公共接口 > IVarModule -->
# IVarModule接口 参考 公共模块 » 变量公共接口

变量公共接口
更多...

被 GlobalVariableModuleTool 继承.

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetVarInt (string varName, int[] intList) |
|  | 设置变量int类型数据 更多... |
|  | |
| void | SetVarFloat (string varName, float[] floatList) |
|  | 设置变量float类型数据 更多... |
|  | |
| void | SetVarString (string varName, string[] stringList) |
|  | 设置变量string类型数据 更多... |
|  | |
| void | SetVarByte (string varName, ByteArrayData stBytesData) |
|  | 设置变量byte类型数据 更多... |
|  | |
| void | SetVarImage (string varName, ImageBaseData stImageData) |
|  | 设置变量图像类型数据 更多... |
|  | |
| void | SetVarPoint (string varName, List< PointF > pointList) |
|  | 设置变量点类型数据 更多... |
|  | |
| void | SetVarBox (string varName, List< RectBox > stRoiBox) |
|  | 设置变量RectBox类型数据 更多... |
|  | |
| void | SetVarAnnulus (string varName, List< Annulus > stAnnulus) |
|  | 设置变量圆环类型数据 更多... |
|  | |
| void | SetVarEllipse (string varName, List< Ellipse > stEllipse) |
|  | 设置变量椭圆数据 更多... |
|  | |
| void | SetVarLine (string varName, List< Line > stLine) |
|  | 设置变量直线数据 更多... |
|  | |
| void | SetVarRect (string varName, List< RectF > stRectF) |
|  | 设置变量矩形数据 更多... |
|  | |
| void | SetVarFixture (string varName, List< Fixture > stFixture) |
|  | 设置变量位置修正数据 更多... |
|  | |
| void | SetVarPolygon (string varName, List< Polygon > stPolygon) |
|  | 设置变量多边形数据 更多... |
|  | |
| IntDataArray | GetVarInt (string varName) |
|  | 获取变量int类型数据 更多... |
|  | |
| FloatDataArray | GetVarFloat (string varName) |
|  | 获取变量float类型数据 更多... |
|  | |
| string [] | GetVarString (string varName) |
|  | 获取变量string类型数据 更多... |
|  | |
| ByteArrayData | GetVarByte (string varName) |
|  | 获取变量byte类型数据 更多... |
|  | |
| ImageBaseData | GetVarImage (string varName) |
|  | 获取变量图像类型数据 更多... |
|  | |
| List< PointF > | GetVarPoint (string varName) |
|  | 获取变量点类型数据 更多... |
|  | |
| List< Line > | GetVarLine (string varName) |
|  | 获取变量直线类型数据 更多... |
|  | |
| List< Ellipse > | GetVarEllipse (string varName) |
|  | 获取变量椭圆类型数据 更多... |
|  | |
| List< RectBox > | GetVarBox (string varName) |
|  | 获取变量Rectbox类型数据 更多... |
|  | |
| List< RectF > | GetVarRect (string varName) |
|  | 获取变量矩形类型数据 更多... |
|  | |
| List< Annulus > | GetVarAnnulus (string varName) |
|  | 获取变量圆环类型数据 更多... |
|  | |
| List< Fixture > | GetVarFixture (string varName) |
|  | 获取变量修正位置类型数据 更多... |
|  | |
| List< Polygon > | GetVarPolygon (string varName) |
|  | 获取变量多边形类型数据 更多... |
|  | |

## 详细描述

变量公共接口

## 成员函数说明

## ◆ SetVarInt()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarInt | ( | string | *varName*, |
|  |  | int [] | *intList* |
|  | ) |  |  |

设置变量int类型数据

## ◆ SetVarFloat()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarFloat | ( | string | *varName*, |
|  |  | float [] | *floatList* |
|  | ) |  |  |

设置变量float类型数据

## ◆ SetVarString()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarString | ( | string | *varName*, |
|  |  | string [] | *stringList* |
|  | ) |  |  |

设置变量string类型数据

## ◆ SetVarByte()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarByte | ( | string | *varName*, |
|  |  | ByteArrayData | *stBytesData* |
|  | ) |  |  |

设置变量byte类型数据

## ◆ SetVarImage()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarImage | ( | string | *varName*, |
|  |  | ImageBaseData | *stImageData* |
|  | ) |  |  |

设置变量图像类型数据

## ◆ SetVarPoint()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarPoint | ( | string | *varName*, |
|  |  | List< PointF > | *pointList* |
|  | ) |  |  |

设置变量点类型数据

## ◆ SetVarBox()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarBox | ( | string | *varName*, |
|  |  | List< RectBox > | *stRoiBox* |
|  | ) |  |  |

设置变量RectBox类型数据

## ◆ SetVarAnnulus()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarAnnulus | ( | string | *varName*, |
|  |  | List< Annulus > | *stAnnulus* |
|  | ) |  |  |

设置变量圆环类型数据

## ◆ SetVarEllipse()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarEllipse | ( | string | *varName*, |
|  |  | List< Ellipse > | *stEllipse* |
|  | ) |  |  |

设置变量椭圆数据

## ◆ SetVarLine()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarLine | ( | string | *varName*, |
|  |  | List< Line > | *stLine* |
|  | ) |  |  |

设置变量直线数据

## ◆ SetVarRect()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarRect | ( | string | *varName*, |
|  |  | List< RectF > | *stRectF* |
|  | ) |  |  |

设置变量矩形数据

## ◆ SetVarFixture()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarFixture | ( | string | *varName*, |
|  |  | List< Fixture > | *stFixture* |
|  | ) |  |  |

设置变量位置修正数据

## ◆ SetVarPolygon()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetVarPolygon | ( | string | *varName*, |
|  |  | List< Polygon > | *stPolygon* |
|  | ) |  |  |

设置变量多边形数据

## ◆ GetVarInt()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntDataArray GetVarInt | ( | string | *varName* | ) |  |

获取变量int类型数据

## ◆ GetVarFloat()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatDataArray GetVarFloat | ( | string | *varName* | ) |  |

获取变量float类型数据

## ◆ GetVarString()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| string [] GetVarString | ( | string | *varName* | ) |  |

获取变量string类型数据

## ◆ GetVarByte()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ByteArrayData GetVarByte | ( | string | *varName* | ) |  |

获取变量byte类型数据

## ◆ GetVarImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageBaseData GetVarImage | ( | string | *varName* | ) |  |

获取变量图像类型数据

## ◆ GetVarPoint()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<PointF> GetVarPoint | ( | string | *varName* | ) |  |

获取变量点类型数据

## ◆ GetVarLine()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Line> GetVarLine | ( | string | *varName* | ) |  |

获取变量直线类型数据

## ◆ GetVarEllipse()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Ellipse> GetVarEllipse | ( | string | *varName* | ) |  |

获取变量椭圆类型数据

## ◆ GetVarBox()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectBox> GetVarBox | ( | string | *varName* | ) |  |

获取变量Rectbox类型数据

## ◆ GetVarRect()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectF> GetVarRect | ( | string | *varName* | ) |  |

获取变量矩形类型数据

## ◆ GetVarAnnulus()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Annulus> GetVarAnnulus | ( | string | *varName* | ) |  |

获取变量圆环类型数据

## ◆ GetVarFixture()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Fixture> GetVarFixture | ( | string | *varName* | ) |  |

获取变量修正位置类型数据

## ◆ GetVarPolygon()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Polygon> GetVarPolygon | ( | string | *varName* | ) |  |

获取变量多边形类型数据
