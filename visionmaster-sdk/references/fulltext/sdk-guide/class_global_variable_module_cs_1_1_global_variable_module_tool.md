<!-- src:class_global_variable_module_cs_1_1_global_variable_module_tool.html -->
<!-- path:接口函数 > 全局模块 > 全局变量 > GlobalVariableModuleTool -->
# GlobalVariableModuleTool类 参考 全局模块 » 全局变量

全局变量
更多...

继承自 VmModule , 以及 IVarModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetGlobalVar (string strParam, string strVal) |
|  | 设置全局变量 更多... |
|  | |
| string | GetGlobalVar (string strParam) |
|  | 获取全局变量 更多... |
|  | |
| List< GlobalVarInfo > | GetAllGlobalVar () |
|  | 获取所有全局变量 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |
| Public 成员函数 继承自 IVarModule | |
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

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 属性 继承自 VmModule | |
| ModuResultMemoryTypeEnum | ModuResultMemType |
|  | 模块结果内存管理类型 更多... |
|  | |

## 详细描述

全局变量

## 成员函数说明

## ◆ SetGlobalVar()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetGlobalVar | ( | string | *strParam*, |
|  |  | string | *strVal* |
|  | ) |  |  |

设置全局变量

## ◆ GetGlobalVar()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| string GetGlobalVar | ( | string | *strParam* | ) |  |

获取全局变量

## ◆ GetAllGlobalVar()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<GlobalVarInfo> GetAllGlobalVar | ( |  | ) |  |

获取所有全局变量
