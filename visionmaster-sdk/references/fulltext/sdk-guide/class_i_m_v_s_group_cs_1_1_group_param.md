<!-- src:class_i_m_v_s_group_cs_1_1_group_param.html -->
<!-- path:接口函数 > 逻辑工具 > Group > GroupParam -->
# GroupParam类 参考 逻辑工具 » Group

Group参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | DataTypeEnum {     Int = 0x1,     Float = 0x2,     String = 0x3   } |
|  | 数据类型 更多... |
|  | |
| enum | CmpTypeEnum {     GT = 0x1,     LT = 0x2,     EQ = 0x3,     NE = 0x4,     GE = 0x5,     LE = 0x6   } |
|  | 比较运算 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | SetInputInt (String strName, int[] anIntVal) |
|  | 设置Int数据 更多... |
|  | |
| new void | SetInputFloat (String strName, float[] anFloatVal) |
|  | 设置Float数据 更多... |
|  | |
| new void | SetInputString (String strName, InputStringData[] astStrData) |
|  | 设置String数据 更多... |
|  | |
| override void | SetInputImage (InputImageData stImageData) |
|  | 设置动态输入图像数据，弃用，推荐 SetInputImage\_V2() 更多... |
|  | |
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
|  | 获取所有输出名称信息（CONTOURPOINTS、POINTSET、小写的image，这三种类型不支持） 更多... |
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
| Public 属性 | |
| bool | EnableLoop |
|  | 循环使能 更多... |
|  | |
| int | LoopTimeGap |
|  | 循环间隔(ms) 更多... |
|  | |
| bool | EnableBreak |
|  | 中断循环 更多... |
|  | |
| DataTypeEnum | DataType |
|  | 数据类型 更多... |
|  | |
| CmpTypeEnum | CmpType |
|  | 比较运算 更多... |
|  | |

## 详细描述

Group参数

## 成员枚举类型说明

## ◆ DataTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DataTypeEnum | | strong |

数据类型

| 枚举值 | |
| --- | --- |
| Int | int |
| Float | float |
| String | string |

## ◆ CmpTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CmpTypeEnum | | strong |

比较运算

| 枚举值 | |
| --- | --- |
| GT | > |
| LT | < |
| EQ | = |
| NE | != |
| GE | >= |
| LE | <= |

## 成员函数说明

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
    | strName | 参数名称 |
    | anIntVal | int型数组 |

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
    | strName | 参数名称 |
    | anFloatVal | Float型数组 |

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
    | strName | 参数名称 |
    | astStrData | InputStringData结构体数组 |

**备注**

            仅当次执行起效

## ◆ SetInputImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| override void SetInputImage | ( | InputImageData | *stImageData* | ) |  |

设置动态输入图像数据，弃用，推荐 SetInputImage\_V2()

参数
:   |  |  |
    | --- | --- |
    | stImageData | InputImageData类型数据 |

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

获取所有输出名称信息（CONTOURPOINTS、POINTSET、小写的image，这三种类型不支持）

## 类成员变量说明

## ◆ EnableLoop

|  |
| --- |
| bool EnableLoop |

循环使能

## ◆ LoopTimeGap

|  |
| --- |
| int LoopTimeGap |

循环间隔(ms)

## ◆ EnableBreak

|  |
| --- |
| bool EnableBreak |

中断循环

## ◆ DataType

|  |
| --- |
| DataTypeEnum DataType |

数据类型

## ◆ CmpType

|  |
| --- |
| CmpTypeEnum CmpType |

比较运算
