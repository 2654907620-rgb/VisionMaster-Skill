<!-- src:class_i_m_v_s_color_recognition_modu_cs_1_1_color_recognition_param.html -->
<!-- path:接口函数 > 颜色处理 > 颜色识别 > ColorRecognitionParam -->
# ColorRecognitionParam类 参考 颜色处理 » 颜色识别

颜色识别参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | KnnDistanceEnum {     EuclideanDistance = 0x1,     ManhattanDistance = 0x2,     IntersectDistance = 0x3,     EarthmoversDistance = 0x4   } |
|  | KNN距离 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ColorRecognitionRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | KnnK `[get, set]` |
|  | K值，范围：[1,100] 更多... |
|  | |
| KnnDistanceEnum | KnnDistance `[get, set]` |
|  | KNN距离 更多... |
|  | |
| bool | ColorType `[get, set]` |
|  | 识别类别 更多... |
|  | |
| string | TopTypeName `[get, set]` |
|  | 最佳匹配名称 更多... |
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

颜色识别参数

## 成员枚举类型说明

## ◆ KnnDistanceEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum KnnDistanceEnum | | strong |

KNN距离

| 枚举值 | |
| --- | --- |
| EuclideanDistance | 欧式距离 |
| ManhattanDistance | 曼哈顿距离 |
| IntersectDistance | 相交距离 |
| EarthmoversDistance | 偏移距离 |

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
| |  | | --- | | ColorRecognitionRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ KnnK

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KnnK | | getset |

K值，范围：[1,100]

## ◆ KnnDistance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | KnnDistanceEnum KnnDistance | | getset |

KNN距离

## ◆ ColorType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ColorType | | getset |

识别类别

## ◆ TopTypeName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string TopTypeName | | getset |

最佳匹配名称
