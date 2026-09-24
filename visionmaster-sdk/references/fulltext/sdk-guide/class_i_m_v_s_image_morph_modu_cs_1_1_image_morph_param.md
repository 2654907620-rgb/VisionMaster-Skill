<!-- src:class_i_m_v_s_image_morph_modu_cs_1_1_image_morph_param.html -->
<!-- path:接口函数 > 图像处理 > 形态学处理 > ImageMorphParam -->
# ImageMorphParam类 参考 图像处理 » 形态学处理

形态学处理参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | MorphTypeEnum {     Dilate = 0x1,     Erode = 0x2,     Open = 0x3,     Close = 0x4   } |
|  | 形态学类型 更多... |
|  | |
| enum | MorphShapeEnum {     Rectange = 0x0,     Ellipse = 0x1,     Crosss = 0x2   } |
|  | 形态学形状 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageMorphRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| MorphTypeEnum | MorphType `[get, set]` |
|  | 形态学类型 更多... |
|  | |
| MorphShapeEnum | MorphShape `[get, set]` |
|  | 形态学形状 更多... |
|  | |
| int | MorphIterNum `[get, set]` |
|  | 迭代次数，范围：[0,10] 更多... |
|  | |
| int | KernelWidth `[get, set]` |
|  | 核宽度，范围：[1,51] 更多... |
|  | |
| int | KernelHeight `[get, set]` |
|  | 核高度，范围：[1,51] 更多... |
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

形态学处理参数

## 成员枚举类型说明

## ◆ MorphTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MorphTypeEnum | | strong |

形态学类型

| 枚举值 | |
| --- | --- |
| Dilate | 膨胀 |
| Erode | 腐蚀 |
| Open | 开 |
| Close | 闭 |

## ◆ MorphShapeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MorphShapeEnum | | strong |

形态学形状

| 枚举值 | |
| --- | --- |
| Rectange | 矩形 |
| Ellipse | 椭圆 |
| Crosss | 十字 |

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
| |  | | --- | | ImageMorphRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ MorphType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MorphTypeEnum MorphType | | getset |

形态学类型

## ◆ MorphShape

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MorphShapeEnum MorphShape | | getset |

形态学形状

## ◆ MorphIterNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MorphIterNum | | getset |

迭代次数，范围：[0,10]

## ◆ KernelWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelWidth | | getset |

核宽度，范围：[1,51]

## ◆ KernelHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelHeight | | getset |

核高度，范围：[1,51]
