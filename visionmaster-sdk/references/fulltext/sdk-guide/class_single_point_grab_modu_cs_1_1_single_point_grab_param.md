<!-- src:class_single_point_grab_modu_cs_1_1_single_point_grab_param.html -->
<!-- path:接口函数 > 运算 > 单点抓取 > SinglePointGrabParam -->
# SinglePointGrabParam类 参考 运算 » 单点抓取

单点抓取参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CalibTypeEnum {     TransCalib = 0x0,     TransAndRotateCalib = 0x1   } |
|  | 标定类型 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoBasicInit () |
|  | 创建基准 更多... |
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
| List< PointF > | ImagePoint `[set]` |
|  | 像素点 更多... |
|  | |
| List< float > | ImagePointA `[set]` |
|  | 图像角度 更多... |
|  | |
| List< PointF > | TeachPoint `[set]` |
|  | 示教物理点 更多... |
|  | |
| List< float > | TeachPointA `[set]` |
|  | 示教角度 更多... |
|  | |
| List< PointF > | TeachSnapPoint `[set]` |
|  | 示教拍照物理点 更多... |
|  | |
| List< float > | TeachSnapPointA `[set]` |
|  | 示教拍照角度 更多... |
|  | |
| List< float > | CalibMatrix `[set]` |
|  | 标定矩阵 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| List< float > | SnapPointDeltaAngle `[set]` |
|  | 旋转相对角度 更多... |
|  | |
| CalibTypeEnum | CalibType `[get, set]` |
|  | 标定类型 更多... |
|  | |
| bool | SnapPointRotateEnable `[get, set]` |
|  | 旋转拍照使能 更多... |
|  | |
| string | FilePath `[get, set]` |
|  | 加载标定文件 更多... |
|  | |

## 详细描述

单点抓取参数

## 成员枚举类型说明

## ◆ CalibTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibTypeEnum | | strong |

标定类型

| 枚举值 | |
| --- | --- |
| TransCalib | 平移标定 |
| TransAndRotateCalib | 平移旋转标定 |

## 成员函数说明

## ◆ DoBasicInit()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoBasicInit | ( |  | ) |  |

创建基准

## 属性说明

## ◆ ImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ImagePoint | | set |

像素点

**备注**

仅当次执行起效

## ◆ ImagePointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ImagePointA | | set |

图像角度

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

## ◆ TeachSnapPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TeachSnapPoint | | set |

示教拍照物理点

**备注**

仅当次执行起效

## ◆ TeachSnapPointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TeachSnapPointA | | set |

示教拍照角度

**备注**

仅当次执行起效

## ◆ CalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibMatrix | | set |

标定矩阵

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ SnapPointDeltaAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapPointDeltaAngle | | set |

旋转相对角度

**备注**

仅当次执行起效

## ◆ CalibType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibTypeEnum CalibType | | getset |

标定类型

## ◆ SnapPointRotateEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SnapPointRotateEnable | | getset |

旋转拍照使能

## ◆ FilePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FilePath | | getset |

加载标定文件
