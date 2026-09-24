<!-- src:class_i_m_v_s_image_enhance_modu_cs_1_1_image_enhance_param.html -->
<!-- path:接口函数 > 图像处理 > 图像增强 > ImageEnhanceParam -->
# ImageEnhanceParam类 参考 图像处理 » 图像增强

图像增强参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EnhanceTypeEnum {     Sharpen = 0x1,     Contrast = 0x2,     Gamma = 0x3,     BrightAdhust = 0x4   } |
|  | 图像增强类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageEnhanceRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| EnhanceTypeEnum | EnhanceType `[get, set]` |
|  | 图像增强类型 更多... |
|  | |
| int | SharpenStrength `[get, set]` |
|  | 锐化强度，范围：[0,1000] 更多... |
|  | |
| int | SharpenKernelSize `[get, set]` |
|  | 锐化核大小，范围：[1,51] 更多... |
|  | |
| int | ContrastFactor `[get, set]` |
|  | 对比度系数，范围：[1,10000] 更多... |
|  | |
| double | GammaVal `[get, set]` |
|  | Gamma，范围：[0,10] 更多... |
|  | |
| int | BrightGain `[get, set]` |
|  | 增益，范围：[0,100] 更多... |
|  | |
| int | BrightOffset `[get, set]` |
|  | 亮度校正补偿，范围：[-255,255] 更多... |
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

图像增强参数

## 成员枚举类型说明

## ◆ EnhanceTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EnhanceTypeEnum | | strong |

图像增强类型

| 枚举值 | |
| --- | --- |
| Sharpen | 锐化 |
| Contrast | 对比度 |
| Gamma | Gamma |
| BrightAdhust | 亮度校正 |

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
| |  | | --- | | ImageEnhanceRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ EnhanceType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EnhanceTypeEnum EnhanceType | | getset |

图像增强类型

## ◆ SharpenStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SharpenStrength | | getset |

锐化强度，范围：[0,1000]

## ◆ SharpenKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SharpenKernelSize | | getset |

锐化核大小，范围：[1,51]

## ◆ ContrastFactor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastFactor | | getset |

对比度系数，范围：[1,10000]

## ◆ GammaVal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double GammaVal | | getset |

Gamma，范围：[0,10]

## ◆ BrightGain

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BrightGain | | getset |

增益，范围：[0,100]

## ◆ BrightOffset

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BrightOffset | | getset |

亮度校正补偿，范围：[-255,255]
