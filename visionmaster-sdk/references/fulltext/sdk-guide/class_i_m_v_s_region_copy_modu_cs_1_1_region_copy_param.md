<!-- src:class_i_m_v_s_region_copy_modu_cs_1_1_region_copy_param.html -->
<!-- path:接口函数 > 图像处理 > 拷贝填充 > RegionCopyParam -->
# RegionCopyParam类 参考 图像处理 » 拷贝填充

拷贝填充参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | RegionTypeEnum {     Copy = 0x1,     Fill = 0x2   } |
|  | 处理类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| RegionCopyRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| RegionTypeEnum | RegionType `[get, set]` |
|  | 处理类型 更多... |
|  | |
| int | FillVal `[get, set]` |
|  | 区域内填充值，范围：[0,255] 更多... |
|  | |
| int | ExtFillVal `[get, set]` |
|  | 区域外填充值，范围：[0,255] 更多... |
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

拷贝填充参数

## 成员枚举类型说明

## ◆ RegionTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RegionTypeEnum | | strong |

处理类型

| 枚举值 | |
| --- | --- |
| Copy | 拷贝 |
| Fill | 填充 |

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
| |  | | --- | | RegionCopyRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ RegionType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RegionTypeEnum RegionType | | getset |

处理类型

## ◆ FillVal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FillVal | | getset |

区域内填充值，范围：[0,255]

## ◆ ExtFillVal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ExtFillVal | | getset |

区域外填充值，范围：[0,255]
