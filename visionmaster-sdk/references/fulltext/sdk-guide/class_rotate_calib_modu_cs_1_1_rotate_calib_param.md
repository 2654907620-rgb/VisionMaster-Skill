<!-- src:class_rotate_calib_modu_cs_1_1_rotate_calib_param.html -->
<!-- path:接口函数 > 标定 > 旋转标定 > RotateCalibParam -->
# RotateCalibParam类 参考 标定 » 旋转标定

旋转标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< PointF > | ImagePoint `[set]` |
|  | 图像点 更多... |
|  | |
| List< float > | WorldRotateAngle `[set]` |
|  | 物理角度 更多... |
|  | |
| List< int > | RotNum `[set]` |
|  | 旋转次数 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| bool | RevOutputFlag `[get, set]` |
|  | 反向纠正 更多... |
|  | |
| string | FilePath `[get, set]` |
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

旋转标定参数

## 属性说明

## ◆ ImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ImagePoint | | set |

图像点

**备注**

仅当次执行起效

## ◆ WorldRotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> WorldRotateAngle | | set |

物理角度

**备注**

仅当次执行起效

## ◆ RotNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RotNum | | set |

旋转次数

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ RevOutputFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RevOutputFlag | | getset |

反向纠正

## ◆ FilePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FilePath | | getset |

加载标定文件
