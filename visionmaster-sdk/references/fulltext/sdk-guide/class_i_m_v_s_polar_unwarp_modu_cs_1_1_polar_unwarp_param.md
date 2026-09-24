<!-- src:class_i_m_v_s_polar_unwarp_modu_cs_1_1_polar_unwarp_param.html -->
<!-- path:接口函数 > 图像处理 > 圆环展开 > PolarUnwarpParam -->
# PolarUnwarpParam类 参考 图像处理 » 圆环展开

圆环展开参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | AngleDirTypeEnum {     AntiClockWise = 0x1,     ClockWise = 0x2   } |
|  | 角度方向 更多... |
|  | |
| enum | RadiusDirTypeEnum {     InnerToOuter = 0x1,     OuterToInner = 0x2   } |
|  | 半径方向 更多... |
|  | |
| enum | InterpolationEnum {     Neareast = 0x1,     Bilinear = 0x2   } |
|  | 插值方法 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| PolarUnwarpRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| AngleDirTypeEnum | AngleDirType `[get, set]` |
|  | 角度方向 更多... |
|  | |
| RadiusDirTypeEnum | RadiusDirType `[get, set]` |
|  | 半径方向 更多... |
|  | |
| InterpolationEnum | Interpolation `[get, set]` |
|  | 插值方法 更多... |
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

圆环展开参数

## 成员枚举类型说明

## ◆ AngleDirTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum AngleDirTypeEnum | | strong |

角度方向

| 枚举值 | |
| --- | --- |
| AntiClockWise | 逆时针 |
| ClockWise | 顺时针 |

## ◆ RadiusDirTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RadiusDirTypeEnum | | strong |

半径方向

| 枚举值 | |
| --- | --- |
| InnerToOuter | 从内往外 |
| OuterToInner | 从外往内 |

## ◆ InterpolationEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InterpolationEnum | | strong |

插值方法

| 枚举值 | |
| --- | --- |
| Neareast | 最近邻 |
| Bilinear | 双线性 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarUnwarpRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ AngleDirType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | AngleDirTypeEnum AngleDirType | | getset |

角度方向

## ◆ RadiusDirType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RadiusDirTypeEnum RadiusDirType | | getset |

半径方向

## ◆ Interpolation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InterpolationEnum Interpolation | | getset |

插值方法
