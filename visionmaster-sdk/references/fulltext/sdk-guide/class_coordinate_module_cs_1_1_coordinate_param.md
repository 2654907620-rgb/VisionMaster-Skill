<!-- src:class_coordinate_module_cs_1_1_coordinate_param.html -->
<!-- path:接口函数 > 标定 > 坐标系 > CoordinateParam -->
# CoordinateParam类 参考 标定 » 坐标系

坐标系参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CordinateCreateEnum {     Draw = 0x0,     Subscribe = 0x1   } |
|  | 坐标系创建 更多... |
|  | |
| enum | InputWayEnum {     ByPoint = 0x0,     ByCoordinate = 0x1,     ByMatrix = 0x2   } |
|  | 输入方式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< float > | CalibMatrix `[set]` |
|  | 标定矩阵 更多... |
|  | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | SrcInputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| List< float > | SrcAngle `[set]` |
|  | SrcAngle 更多... |
|  | |
| CordinateCreateEnum | CordinateCreate `[get, set]` |
|  | 坐标系创建 更多... |
|  | |
| InputWayEnum | InputWay `[get, set]` |
|  | 输入方式 更多... |
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

坐标系参数

## 成员枚举类型说明

## ◆ CordinateCreateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CordinateCreateEnum | | strong |

坐标系创建

| 枚举值 | |
| --- | --- |
| Draw | 绘制 |
| Subscribe | 订阅 |

## ◆ InputWayEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InputWayEnum | | strong |

输入方式

| 枚举值 | |
| --- | --- |
| ByPoint | 按点 |
| ByCoordinate | 按坐标 |
| ByMatrix | 按矩阵 |

## 属性说明

## ◆ CalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibMatrix | | set |

标定矩阵

**备注**

仅当次执行起效

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ SrcInputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> SrcInputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ SrcAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SrcAngle | | set |

SrcAngle

## ◆ CordinateCreate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CordinateCreateEnum CordinateCreate | | getset |

坐标系创建

## ◆ InputWay

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InputWayEnum InputWay | | getset |

输入方式
