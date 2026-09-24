<!-- src:class_i_m_v_s_image_sharpness_modu_cs_1_1_image_sharpness_param.html -->
<!-- path:接口函数 > 图像处理 > 清晰度评估 > ImageSharpnessParam -->
# ImageSharpnessParam类 参考 图像处理 » 清晰度评估

清晰度评估参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | SharpnessModeEnum {     AutoCoreeMode = 0x1,     SquaredGrad = 0x2   } |
|  | 评价模式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageSharpnessRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| SharpnessModeEnum | SharpnessMode `[get, set]` |
|  | 评价模式 更多... |
|  | |
| int | NoiseLevel `[get, set]` |
|  | 噪声等级，范围：[0,32] 更多... |
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

清晰度评估参数

## 成员枚举类型说明

## ◆ SharpnessModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SharpnessModeEnum | | strong |

评价模式

| 枚举值 | |
| --- | --- |
| AutoCoreeMode | 自相关 |
| SquaredGrad | 梯度平方 |

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
| |  | | --- | | ImageSharpnessRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ SharpnessMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SharpnessModeEnum SharpnessMode | | getset |

评价模式

## ◆ NoiseLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NoiseLevel | | getset |

噪声等级，范围：[0,32]
