<!-- src:class_i_m_v_s_color_image_generation_modu_cs_1_1_color_image_generation_param.html -->
<!-- path:接口函数 > 颜色处理 > 彩图生成 > ColorImageGenerationParam -->
# ColorImageGenerationParam类 参考 颜色处理 » 彩图生成

彩图生成参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ImageFormatEnum {     RGBP3 = 200,     RGBC3 = 201   } |
|  | 输出图像格式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageBaseData | InputImage1 `[set]` |
|  | 输入图像1 更多... |
|  | |
| ImageBaseData | InputImage2 `[set]` |
|  | 输入图像2 更多... |
|  | |
| ImageFormatEnum | ImageFormat `[get, set]` |
|  | 输出图像格式 更多... |
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

彩图生成参数

## 成员枚举类型说明

## ◆ ImageFormatEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageFormatEnum | | strong |

输出图像格式

| 枚举值 | |
| --- | --- |
| RGBP3 | RGB P3 |
| RGBC3 | RGB C3 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputImage1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage1 | | set |

输入图像1

**备注**

仅当次执行起效

## ◆ InputImage2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage2 | | set |

输入图像2

**备注**

仅当次执行起效

## ◆ ImageFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageFormatEnum ImageFormat | | getset |

输出图像格式
