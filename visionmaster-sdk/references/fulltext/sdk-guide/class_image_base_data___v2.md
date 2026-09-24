<!-- src:class_image_base_data___v2.html -->
<!-- path:接口函数 > 公共模块 > 模块结果基类 > ImageBaseData_V2 -->
# ImageBaseData_V2类 参考 公共模块 » 模块结果基类

图像数据V2
更多...

继承自 ImageBaseData\_Base .

|  |  |
| --- | --- |
| 属性 | |
| VMPixelFormat | Pixelformat `[get, set]` |
|  | 图像像素格式 更多... |
|  | |
| IntPtr | ImageData `[get, set]` |
|  | 图像数据 更多... |
|  | |
| 属性 继承自 ImageBaseData\_Base | |
| uint | DataLen `[get, set]` |
|  | 图像数据长度 更多... |
|  | |
| int | Width `[get, set]` |
|  | 图像宽度 更多... |
|  | |
| int | Height `[get, set]` |
|  | 图像高度 更多... |
|  | |
| 属性 继承自 IBaseData | |
| IMVS\_MODULE\_BASE\_DATA\_TYPE | BaseDataType `[get]` |
|  | 数据类型 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 成员函数 继承自 ImageBaseData\_Base | |
| byte [][] | GetDataForMVDConvertSC () |
|  | 获取数据用于赋值算子图像 更多... |
|  | |
| void | SetDataForMVDConvertSC (byte[][] inputCommon) |
|  | 设置算子数据用于赋值图像 更多... |
|  | |
| Public 成员函数 继承自 IBaseData | |
| byte [] | GetDataForMVDConvert () |
|  | 获取数据用于赋值算子图形 更多... |
|  | |
| void | SetDataForMVDConvert (byte[] inputCommon) |
|  | 设置算子数据用于赋值图形 更多... |
|  | |

## 详细描述

图像数据V2

## 属性说明

## ◆ Pixelformat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | VMPixelFormat Pixelformat | | getset |

图像像素格式

## ◆ ImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IntPtr ImageData | | getset |

图像数据
