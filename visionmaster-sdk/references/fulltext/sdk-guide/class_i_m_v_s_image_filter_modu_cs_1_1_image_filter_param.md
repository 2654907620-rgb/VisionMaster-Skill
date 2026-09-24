<!-- src:class_i_m_v_s_image_filter_modu_cs_1_1_image_filter_param.html -->
<!-- path:接口函数 > 图像处理 > 图像滤波 > ImageFilterParam -->
# ImageFilterParam类 参考 图像处理 » 图像滤波

图像滤波参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FilterTypeEnum {     Gaussian = 0x1,     Median = 0x2,     Mean = 0x3,     Invert = 0x4,     Edge = 0x5   } |
|  | 图像滤波类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageFilterRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FilterTypeEnum | FilterType `[get, set]` |
|  | 图像滤波类型 更多... |
|  | |
| int | KernelWidth `[get, set]` |
|  | 滤波核宽度，范围：[1,101] 更多... |
|  | |
| int | KernelHeight `[get, set]` |
|  | 滤波核高度，范围：[1,101] 更多... |
|  | |
| int | GaussKernelSize `[get, set]` |
|  | 高斯滤波核，范围：[1,101] 更多... |
|  | |
| int | EdegLowThreshold `[get, set]` |
|  | 边缘阈值范围，范围：[0,255] 更多... |
|  | |
| int | EdegHighThreshold `[get, set]` |
|  | 边缘阈值范围，范围：[0,255] 更多... |
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

图像滤波参数

## 成员枚举类型说明

## ◆ FilterTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FilterTypeEnum | | strong |

图像滤波类型

| 枚举值 | |
| --- | --- |
| Gaussian | 高斯 |
| Median | 中值 |
| Mean | 均值 |
| Invert | 取反 |
| Edge | 边缘提取 |

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
| |  | | --- | | ImageFilterRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FilterType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FilterTypeEnum FilterType | | getset |

图像滤波类型

## ◆ KernelWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelWidth | | getset |

滤波核宽度，范围：[1,101]

## ◆ KernelHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelHeight | | getset |

滤波核高度，范围：[1,101]

## ◆ GaussKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GaussKernelSize | | getset |

高斯滤波核，范围：[1,101]

## ◆ EdegLowThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdegLowThreshold | | getset |

边缘阈值范围，范围：[0,255]

## ◆ EdegHighThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdegHighThreshold | | getset |

边缘阈值范围，范围：[0,255]
