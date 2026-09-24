<!-- src:class_i_m_v_s_calib_transform_modu_cs_1_1_calib_transform_param.html -->
<!-- path:接口函数 > 运算 > 标定转换 > CalibTransformParam -->
# CalibTransformParam类 参考 运算 » 标定转换

标定转换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CoordTypeEnum {     ImageCoord = 0x0,     PhysicalCoord = 0x1   } |
|  | 坐标类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| List< float > | ImagePointA `[set]` |
|  | 图像角度 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| List< float > | CalibMatrix `[set]` |
|  | 标定矩阵 更多... |
|  | |
| CoordTypeEnum | CoordType `[get, set]` |
|  | 坐标类型 更多... |
|  | |
| string | LoadCalibPath `[get, set]` |
|  | 加载标定文件 更多... |
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

标定转换参数

## 成员枚举类型说明

## ◆ CoordTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CoordTypeEnum | | strong |

坐标类型

| 枚举值 | |
| --- | --- |
| ImageCoord | 图像坐标 |
| PhysicalCoord | 物理坐标 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ ImagePointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ImagePointA | | set |

图像角度

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ CalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibMatrix | | set |

标定矩阵

**备注**

仅当次执行起效

## ◆ CoordType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CoordTypeEnum CoordType | | getset |

坐标类型

## ◆ LoadCalibPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadCalibPath | | getset |

加载标定文件
