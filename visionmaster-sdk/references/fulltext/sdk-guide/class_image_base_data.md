<!-- src:class_image_base_data.html -->
<!-- path:接口函数 > 公共模块 > 模块结果基类 > ImageBaseData -->
# ImageBaseData类 参考 公共模块 » 模块结果基类

图像数据
更多...

继承自 ImageBaseData\_Base .

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | ImageBaseData (Bitmap bitmap) |
|  | Bitmap转图像数据，目前只支持Format8bppIndexed和Format24bppRgb两种格式 更多... |
|  | |
| Bitmap | ToBitmap () |
|  | 图像数据转Bitmap，目前只支持Format8bppIndexed和Format24bppRgb两种格式 更多... |
|  | |
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

|  |  |
| --- | --- |
| 属性 | |
| int | Pixelformat `[get, set]` |
|  | 图像像素格式 可选参数：ImvsSdkDefine.IMVS\_IMG\_FORMAT\_MONO8 | ImvsSdkDefine.IMVS\_IMG\_FORMAT\_RGB24 更多... |
|  | |
| byte [] | ImageData `[get, set]` |
|  | 图像数据：byte[] 更多... |
|  | |
| IntPtr | ImageDataPtr `[get, set]` |
|  | 图像数据：IntPtr 更多... |
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

## 详细描述

图像数据

## 构造及析构函数说明

## ◆ ImageBaseData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageBaseData | ( | Bitmap | *bitmap* | ) |  |

Bitmap转图像数据，目前只支持Format8bppIndexed和Format24bppRgb两种格式

## 成员函数说明

## ◆ ToBitmap()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Bitmap ToBitmap | ( |  | ) |  |

图像数据转Bitmap，目前只支持Format8bppIndexed和Format24bppRgb两种格式

## 属性说明

## ◆ Pixelformat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Pixelformat | | getset |

图像像素格式 可选参数：ImvsSdkDefine.IMVS\_IMG\_FORMAT\_MONO8 | ImvsSdkDefine.IMVS\_IMG\_FORMAT\_RGB24

## ◆ ImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | byte [] ImageData | | getset |

图像数据：byte[]

## ◆ ImageDataPtr

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IntPtr ImageDataPtr | | getset |

图像数据：IntPtr
