<!-- src:class_image_base_data___base.html -->
<!-- path:接口函数 > 公共模块 > 模块结果基类 > ImageBaseData_Base -->
# ImageBaseData_Base类 参考 公共模块 » 模块结果基类

图像基本数据
更多...

继承自 IBaseData .

被 ImageBaseData , 以及 ImageBaseData\_V2 继承.

|  |  |
| --- | --- |
| Public 成员函数 | |
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

图像基本数据

## 成员函数说明

## ◆ GetDataForMVDConvertSC()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| byte [][] GetDataForMVDConvertSC | ( |  | ) |  |

获取数据用于赋值算子图像

## ◆ SetDataForMVDConvertSC()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetDataForMVDConvertSC | ( | byte | *inputCommon*[][] | ) |  |

设置算子数据用于赋值图像

## 属性说明

## ◆ DataLen

|  |  |  |
| --- | --- | --- |
| |  | | --- | | uint DataLen | | getset |

图像数据长度

## ◆ Width

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Width | | getset |

图像宽度

## ◆ Height

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Height | | getset |

图像高度
