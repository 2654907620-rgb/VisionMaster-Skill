<!-- src:class_i_m_v_s_geometric_transform_modu_cs_1_1_geometric_transform_param.html -->
<!-- path:接口函数 > 图像处理 > 几何变换 > GeometricTransformParam -->
# GeometricTransformParam类 参考 图像处理 » 几何变换

几何变换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | MirrorOrientationEnum {     NoMirror = 0x0,     Horizontal = 0x1,     Vertical = 0x2,     HoriAndVert = 0x3   } |
|  | 镜像方向 更多... |
|  | |
| enum | RotateAngleEnum {     ZeroQuarter = 0x0,     OneQuarter = 0x1,     TwoQuarter = 0x2,     ThreeQuarter = 0x3   } |
|  | 旋转角度 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| MirrorOrientationEnum | MirrorOrientation `[get, set]` |
|  | 镜像方向 更多... |
|  | |
| RotateAngleEnum | RotateAngle `[get, set]` |
|  | 旋转角度 更多... |
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

几何变换参数

## 成员枚举类型说明

## ◆ MirrorOrientationEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MirrorOrientationEnum | | strong |

镜像方向

| 枚举值 | |
| --- | --- |
| NoMirror | 无 |
| Horizontal | 水平 |
| Vertical | 垂直 |
| HoriAndVert | 水平垂直 |

## ◆ RotateAngleEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RotateAngleEnum | | strong |

旋转角度

| 枚举值 | |
| --- | --- |
| ZeroQuarter | 0 |
| OneQuarter | 90 |
| TwoQuarter | 180 |
| ThreeQuarter | 270 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ MirrorOrientation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MirrorOrientationEnum MirrorOrientation | | getset |

镜像方向

## ◆ RotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RotateAngleEnum RotateAngle | | getset |

旋转角度
