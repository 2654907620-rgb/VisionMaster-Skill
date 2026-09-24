<!-- src:class_i_m_v_s_image_resize_modu_cs_1_1_image_resize_param.html -->
<!-- path:接口函数 > 图像处理 > 图像缩放 > ImageResizeParam -->
# ImageResizeParam类 参考 图像处理 » 图像缩放

图像缩放参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | InterTypeEnum {     Neareast = 0x1,     Bilinear = 0x2,     Cubic = 0x4   } |
|  | 插值类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageResizeRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | WidthValue `[get, set]` |
|  | 输出图像宽度，范围：[8,65000] 更多... |
|  | |
| int | HeightValue `[get, set]` |
|  | 输出图像高度，范围：[8,65000] 更多... |
|  | |
| InterTypeEnum | InterType `[get, set]` |
|  | 插值类型 更多... |
|  | |
| bool | AntiAliasing `[get, set]` |
|  | 抗混叠 更多... |
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

图像缩放参数

## 成员枚举类型说明

## ◆ InterTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InterTypeEnum | | strong |

插值类型

| 枚举值 | |
| --- | --- |
| Neareast | 最近邻 |
| Bilinear | 双线性 |
| Cubic | 双三次 |

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
| |  | | --- | | ImageResizeRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ WidthValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WidthValue | | getset |

输出图像宽度，范围：[8,65000]

## ◆ HeightValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HeightValue | | getset |

输出图像高度，范围：[8,65000]

## ◆ InterType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InterTypeEnum InterType | | getset |

插值类型

## ◆ AntiAliasing

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AntiAliasing | | getset |

抗混叠
