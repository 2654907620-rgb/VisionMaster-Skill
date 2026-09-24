<!-- src:class_image_acquisition_module_cs_1_1_image_acquisition_param.html -->
<!-- path:接口函数 > 采集 > 多图采集 > ImageAcquisitionParam -->
# ImageAcquisitionParam类 参考 采集 » 多图采集

多图采集参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ImageSourceTypeEnum {     LocalImage = 0x1,     Camera = 0x2   } |
|  | 图像源 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetImageDirPath (String strDirPath) |
|  | 设置图像文件夹路径 更多... |
|  | |
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

|  |  |
| --- | --- |
| 属性 | |
| ImageSourceTypeEnum | ImageSourceType `[get, set]` |
|  | 图像源 更多... |
|  | |
| int | Interval `[get, set]` |
|  | 取图间隔，范围：[0,1000] 更多... |
|  | |
| int | ImageCount `[get, set]` |
|  | 取图数量，范围：[3,8] 更多... |
|  | |
| string | ImageDir `[get, set]` |
|  | 图像路径（弃用） 更多... |
|  | |

## 详细描述

多图采集参数

## 成员枚举类型说明

## ◆ ImageSourceTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageSourceTypeEnum | | strong |

图像源

| 枚举值 | |
| --- | --- |
| LocalImage | 本地图像 |
| Camera | 相机 |

## 成员函数说明

## ◆ SetImageDirPath()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetImageDirPath | ( | String | *strDirPath* | ) |  |

设置图像文件夹路径

参数
:   |  |  |
    | --- | --- |
    | strDirPath | 文件夹路径 |

## 属性说明

## ◆ ImageSourceType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSourceTypeEnum ImageSourceType | | getset |

图像源

## ◆ Interval

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Interval | | getset |

取图间隔，范围：[0,1000]

## ◆ ImageCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageCount | | getset |

取图数量，范围：[3,8]

## ◆ ImageDir

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string ImageDir | | getset |

图像路径（弃用）
