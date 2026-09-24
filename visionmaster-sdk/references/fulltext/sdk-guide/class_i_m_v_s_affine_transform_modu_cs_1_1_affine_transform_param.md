<!-- src:class_i_m_v_s_affine_transform_modu_cs_1_1_affine_transform_param.html -->
<!-- path:接口函数 > 图像处理 > 仿射变换 > AffineTransformParam -->
# AffineTransformParam类 参考 图像处理 » 仿射变换

仿射变换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | TransformationTypeEnum {     CropZoom = 0x1,     Mirror = 0x2,     Translation = 0x3   } |
|  | 仿射变换类型 更多... |
|  | |
| enum | InterpolationEnum {     Neareast = 0x1,     Bilinear = 0x2   } |
|  | 插值方法 更多... |
|  | |
| enum | ExtensionTypeEnum {     Constant = 0x1,     Copy = 0x2   } |
|  | 填充方式 更多... |
|  | |
| enum | MirrorOrientationEnum {     Horizontal = 0x1,     Vertical = 0x2,     HoriAndVert = 0x3   } |
|  | 镜像方向 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| AffineTransformRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| TransformationTypeEnum | TransformationType `[get, set]` |
|  | 仿射变换类型 更多... |
|  | |
| double | Scale `[get, set]` |
|  | 尺度，范围：[0.1,10.0] 更多... |
|  | |
| double | Aspect `[get, set]` |
|  | 宽高比，范围：[0.1,2.0] 更多... |
|  | |
| InterpolationEnum | Interpolation `[get, set]` |
|  | 插值方法 更多... |
|  | |
| ExtensionTypeEnum | ExtensionType `[get, set]` |
|  | 填充方式 更多... |
|  | |
| int | ExtensionValue `[get, set]` |
|  | 填充值，范围：[0,255] 更多... |
|  | |
| MirrorOrientationEnum | MirrorOrientation `[get, set]` |
|  | 镜像方向 更多... |
|  | |
| double | RotateAngle `[get, set]` |
|  | 旋转角度，范围：[0.0,360.0] 更多... |
|  | |
| int | MoveXValue `[get, set]` |
|  | X移动距离，范围：[-30000,30000] 更多... |
|  | |
| int | MoveYValue `[get, set]` |
|  | Y移动距离，范围：[-20000,20000] 更多... |
|  | |
| bool | LockOutputImageSize `[get, set]` |
|  | 锁定输出尺寸 更多... |
|  | |
| int | WidthValue `[get, set]` |
|  | 宽度，范围：[8,30000] 更多... |
|  | |
| int | HeightValue `[get, set]` |
|  | 高度，范围：[8,20000] 更多... |
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

仿射变换参数

## 成员枚举类型说明

## ◆ TransformationTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum TransformationTypeEnum | | strong |

仿射变换类型

| 枚举值 | |
| --- | --- |
| CropZoom | 裁剪缩放 |
| Mirror | 镜像 |
| Translation | 平移 |

## ◆ InterpolationEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InterpolationEnum | | strong |

插值方法

| 枚举值 | |
| --- | --- |
| Neareast | 最近邻 |
| Bilinear | 双线性 |

## ◆ ExtensionTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ExtensionTypeEnum | | strong |

填充方式

| 枚举值 | |
| --- | --- |
| Constant | 常数 |
| Copy | 邻近复制 |

## ◆ MirrorOrientationEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MirrorOrientationEnum | | strong |

镜像方向

| 枚举值 | |
| --- | --- |
| Horizontal | 水平 |
| Vertical | 垂直 |
| HoriAndVert | 水平垂直 |

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
| |  | | --- | | AffineTransformRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ TransformationType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | TransformationTypeEnum TransformationType | | getset |

仿射变换类型

## ◆ Scale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Scale | | getset |

尺度，范围：[0.1,10.0]

## ◆ Aspect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Aspect | | getset |

宽高比，范围：[0.1,2.0]

## ◆ Interpolation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InterpolationEnum Interpolation | | getset |

插值方法

## ◆ ExtensionType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ExtensionTypeEnum ExtensionType | | getset |

填充方式

## ◆ ExtensionValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExtensionValue | | getset |

填充值，范围：[0,255]

## ◆ MirrorOrientation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MirrorOrientationEnum MirrorOrientation | | getset |

镜像方向

## ◆ RotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RotateAngle | | getset |

旋转角度，范围：[0.0,360.0]

## ◆ MoveXValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MoveXValue | | getset |

X移动距离，范围：[-30000,30000]

## ◆ MoveYValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MoveYValue | | getset |

Y移动距离，范围：[-20000,20000]

## ◆ LockOutputImageSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LockOutputImageSize | | getset |

锁定输出尺寸

## ◆ WidthValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WidthValue | | getset |

宽度，范围：[8,30000]

## ◆ HeightValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HeightValue | | getset |

高度，范围：[8,20000]
