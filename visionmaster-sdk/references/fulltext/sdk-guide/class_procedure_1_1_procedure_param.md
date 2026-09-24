<!-- src:class_procedure_1_1_procedure_param.html -->
<!-- path:接口函数 > 流程 > ProcedureParam -->
# ProcedureParam类 参考 流程

流程参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetInputImage\_V2 (String strParamName, ImageBaseData stImageData) |
|  | 设置动态输入图像数据 更多... |
|  | |
| void | SetInputBox (string strParamName, List< RectBox > stRoiBox) |
|  | 设置动态输入矩形框数据 更多... |
|  | |
| void | SetInputAnnulus (string strParamName, List< Annulus > stAnnulus) |
|  | 设置动态输入圆环ROI数据 更多... |
|  | |
| void | SetInputCircle (string strParamName, List< Circle > stCircle) |
|  | 设置动态输入圆形数据 更多... |
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
| void | SetInputClassInfo (string strParamName, List< ClassInfo > stClassInfo) |
|  | 设置动态输入类别信息数据 更多... |
|  | |
| void | SetInputPixelImage (string strParamName, PixelImage stPixelImage) |
|  | 设置动态输入像素图像数据 更多... |
|  | |
| void | SetInputPolygon (string strParamName, List< Polygon > stPolygon) |
|  | 设置动态输入多边形数据 更多... |
|  | |
| void | SetInputPosture (string strParamName, List< Posture > stPosture) |
|  | 设置动态输入位姿数据 更多... |
|  | |
| void | SetInputEllipse (string strParamName, List< Ellipse > stEllipse) |
|  | 设置动态输入椭圆形数据 更多... |
|  | |
| List< VmDynamicIODefine.IoNameInfo > | GetAllInputNameInfo () |
|  | 获取所有输入名称信息（CONTOURPOINTS、POINTSET、小写的image，这三种类型不支持） 更多... |
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

流程参数

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
    | strParamName | 参数名称 |
    | stImageData | 输入数据 |

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
    | strParamName | 参数名称 |
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
    | strParamName | 参数名称 |
    | stAnnulus | 输入数据 |

**备注**

            仅当次执行起效

## ◆ SetInputCircle()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputCircle | ( | string | *strParamName*, |
|  |  | List< Circle > | *stCircle* |
|  | ) |  |  |

设置动态输入圆形数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 参数名称 |
    | stCircle | 输入数据 |

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
    | strParamName | 参数名称 |
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
    | strParamName | 参数名称 |
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
    | strParamName | 参数名称 |
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
    | strParamName | 参数名称 |
    | stRectF | 输入数据 |

**备注**

            仅当次执行起效

## ◆ SetInputClassInfo()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputClassInfo | ( | string | *strParamName*, |
|  |  | List< ClassInfo > | *stClassInfo* |
|  | ) |  |  |

设置动态输入类别信息数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 参数名称 |
    | stClassInfo | 输入数据 |

**备注**

            仅当次执行起效

## ◆ SetInputPixelImage()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputPixelImage | ( | string | *strParamName*, |
|  |  | PixelImage | *stPixelImage* |
|  | ) |  |  |

设置动态输入像素图像数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 参数名称 |
    | stPixelImage | 输入数据 |

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
    | strParamName | 参数名称 |
    | stPolygon | 输入数据 |

**备注**

            仅当次执行起效

## ◆ SetInputPosture()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputPosture | ( | string | *strParamName*, |
|  |  | List< Posture > | *stPosture* |
|  | ) |  |  |

设置动态输入位姿数据

参数
:   |  |  |
    | --- | --- |
    | strParamName | 参数名称 |
    | stPosture | 输入数据 |

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
    | strParamName | 参数名称 |
    | stEllipse | 输入数据 |

仅当次执行起效

## ◆ GetAllInputNameInfo()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<VmDynamicIODefine.IoNameInfo> GetAllInputNameInfo | ( |  | ) |  |

获取所有输入名称信息（CONTOURPOINTS、POINTSET、小写的image，这三种类型不支持）
