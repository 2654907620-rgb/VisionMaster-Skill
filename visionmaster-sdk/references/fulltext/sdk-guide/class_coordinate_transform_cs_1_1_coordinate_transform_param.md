<!-- src:class_coordinate_transform_cs_1_1_coordinate_transform_param.html -->
<!-- path:接口函数 > 运算 > 坐标转换 > CoordinateTransformParam -->
# CoordinateTransformParam类 参考 运算 » 坐标转换

坐标转换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< PointF > | DicingPoint `[set]` |
|  | 划片中心点 更多... |
|  | |
| List< float > | DicingImageWidth `[set]` |
|  | 划片宽 更多... |
|  | |
| List< float > | DicingImageHeight `[set]` |
|  | 划片高 更多... |
|  | |
| List< PointF > | SrcInputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| bool | CorrectEnable `[get, set]` |
|  | 坐标转换使能 更多... |
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

坐标转换参数

## 属性说明

## ◆ DicingPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> DicingPoint | | set |

划片中心点

**备注**

仅当次执行起效

## ◆ DicingImageWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DicingImageWidth | | set |

划片宽

**备注**

仅当次执行起效

## ◆ DicingImageHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DicingImageHeight | | set |

划片高

**备注**

仅当次执行起效

## ◆ SrcInputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> SrcInputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ CorrectEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CorrectEnable | | getset |

坐标转换使能
