<!-- src:class_single_point_map_align_modu_cs_1_1_single_point_map_align_param.html -->
<!-- path:接口函数 > 运算 > 单点映射对位 > SinglePointMapAlignParam -->
# SinglePointMapAlignParam类 参考 运算 » 单点映射对位

单点映射对位参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< PointF > | ObjImagePoint `[set]` |
|  | 对象像素点 更多... |
|  | |
| List< float > | ObjImagePointA `[set]` |
|  | 对象图像角度 更多... |
|  | |
| List< PointF > | TarImagePoint `[set]` |
|  | 目标像素点 更多... |
|  | |
| List< PointF > | TarImageLineS `[set]` |
|  | 目标像素直线起点 更多... |
|  | |
| List< PointF > | TarImageLineE `[set]` |
|  | 目标像素直线终点 更多... |
|  | |
| List< PointF > | TeachPoint `[set]` |
|  | 示教物理点 更多... |
|  | |
| List< float > | TeachPointA `[set]` |
|  | 示教角度 更多... |
|  | |
| List< float > | NPointCalibMatrix `[set]` |
|  | N点标定矩阵 更多... |
|  | |
| List< float > | MapCalibMatrix `[set]` |
|  | 映射标定矩阵 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| string | FilePath `[get, set]` |
|  | N点标定文件 更多... |
|  | |
| string | FilePathMap `[get, set]` |
|  | 映射标定文件 更多... |
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

单点映射对位参数

## 属性说明

## ◆ ObjImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjImagePoint | | set |

对象像素点

**备注**

仅当次执行起效

## ◆ ObjImagePointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ObjImagePointA | | set |

对象图像角度

**备注**

仅当次执行起效

## ◆ TarImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TarImagePoint | | set |

目标像素点

**备注**

仅当次执行起效

## ◆ TarImageLineS

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TarImageLineS | | set |

目标像素直线起点

**备注**

仅当次执行起效

## ◆ TarImageLineE

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TarImageLineE | | set |

目标像素直线终点

**备注**

仅当次执行起效

## ◆ TeachPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TeachPoint | | set |

示教物理点

**备注**

仅当次执行起效

## ◆ TeachPointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TeachPointA | | set |

示教角度

**备注**

仅当次执行起效

## ◆ NPointCalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> NPointCalibMatrix | | set |

N点标定矩阵

**备注**

仅当次执行起效

## ◆ MapCalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MapCalibMatrix | | set |

映射标定矩阵

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ FilePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FilePath | | getset |

N点标定文件

## ◆ FilePathMap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FilePathMap | | getset |

映射标定文件
