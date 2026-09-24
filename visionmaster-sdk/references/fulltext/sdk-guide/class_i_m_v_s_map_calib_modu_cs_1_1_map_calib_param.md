<!-- src:class_i_m_v_s_map_calib_modu_cs_1_1_map_calib_param.html -->
<!-- path:接口函数 > 标定 > 映射标定 > MapCalibParam -->
# MapCalibParam类 参考 标定 » 映射标定

映射标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | InputTypeEnum {     InputImage = 0x1,     InputFile = 0x2   } |
|  | 输入方式 更多... |
|  | |
| enum | CalibBoardTypeEnum {     TypeHKI = 0x7,     TypeHKII = 0x6,     TypeHKIV2 = 0x9,     TypeHKIIV2 = 0x8   } |
|  | 标定板类型 更多... |
|  | |
| enum | HomoFreedomEnum {     Perspective = 0x1,     Affine = 0x2,     Similarity = 0x3   } |
|  | 自由度 更多... |
|  | |
| enum | WeightFunEnum {     LeastSqure = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 权重函数 更多... |
|  | |
| enum | FilterStatusEnum {     FilterStateTure = 0x1,     FilterStateFalse = 0x2   } |
|  | 中值滤波状态 更多... |
|  | |
| enum | SubpixelWinAutoEnum {     SubpixelWinSizeAuto = 0x1,     SubpixelWinSizeUser = 0x2   } |
|  | 亚像素窗口 更多... |
|  | |
| enum | FilterStatus2Enum {     FilterStateTure = 0x1,     FilterStateFalse = 0x2   } |
|  | 中值滤波状态 更多... |
|  | |
| enum | SubpixelWinAuto2Enum {     SubpixelWinSizeAuto = 0x1,     SubpixelWinSizeUser = 0x2   } |
|  | 亚像素窗口 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoSaveFile (string value) |
|  | 生成标定文件 更多... |
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
| ImageBaseData | InputImage1 `[set]` |
|  | 输入图像1 更多... |
|  | |
| ImageBaseData | InputImage2 `[set]` |
|  | 输入图像2 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| List< PointF > | PhysicalPoint `[set]` |
|  | 物理点 更多... |
|  | |
| List< float > | WorldRotateAngle `[set]` |
|  | 物理角度 更多... |
|  | |
| List< string > | Trigger `[set]` |
|  | 外部输入字符 更多... |
|  | |
| List< string > | TeachFlagInput `[set]` |
|  | 外部触发字符 更多... |
|  | |
| InputTypeEnum | InputType `[get, set]` |
|  | 输入方式 更多... |
|  | |
| bool | TeachEnable `[get, set]` |
|  | 示教 更多... |
|  | |
| string | TeachFlag `[get, set]` |
|  | 外部触发字符 更多... |
|  | |
| string | CalibPath0 `[get, set]` |
|  | 标定文件1 更多... |
|  | |
| string | CalibPath1 `[get, set]` |
|  | 标定文件2 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| CalibBoardTypeEnum | CalibBoardType `[get, set]` |
|  | 标定板类型 更多... |
|  | |
| HomoFreedomEnum | HomoFreedom `[get, set]` |
|  | 自由度 更多... |
|  | |
| WeightFunEnum | WeightFun `[get, set]` |
|  | 权重函数 更多... |
|  | |
| int | WeightFactor `[get, set]` |
|  | 权重系数，范围：[1,200] 更多... |
|  | |
| int | GrayContrast `[get, set]` |
|  | 灰度对比度，范围：[1,255]（弃用） 更多... |
|  | |
| FilterStatusEnum | FilterStatus `[get, set]` |
|  | 中值滤波状态 更多... |
|  | |
| SubpixelWinAutoEnum | SubpixelWinAuto `[get, set]` |
|  | 亚像素窗口（弃用） 更多... |
|  | |
| int | SubPixelWindowSize `[get, set]` |
|  | 设置窗口大小，范围：[3,150]（弃用） 更多... |
|  | |
| int | GrayContrast2 `[get, set]` |
|  | 灰度对比度，范围：[1,255]（弃用） 更多... |
|  | |
| FilterStatus2Enum | FilterStatus2 `[get, set]` |
|  | 中值滤波状态 更多... |
|  | |
| SubpixelWinAuto2Enum | SubpixelWinAuto2 `[get, set]` |
|  | 亚像素窗口（弃用） 更多... |
|  | |
| int | SubPixelWindowSize2 `[get, set]` |
|  | 设置窗口大小，范围：[3,150]（弃用） 更多... |
|  | |

## 详细描述

映射标定参数

## 成员枚举类型说明

## ◆ InputTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InputTypeEnum | | strong |

输入方式

| 枚举值 | |
| --- | --- |
| InputImage | 图像输入 |
| InputFile | 文件输入 |

## ◆ CalibBoardTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibBoardTypeEnum | | strong |

标定板类型

| 枚举值 | |
| --- | --- |
| TypeHKI | 海康标定板I型 |
| TypeHKII | 海康标定板II型 |
| TypeHKIV2 | 海康I型扩展 |
| TypeHKIIV2 | 海康II型扩展 |

## ◆ HomoFreedomEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum HomoFreedomEnum | | strong |

自由度

| 枚举值 | |
| --- | --- |
| Perspective | 缩放、旋转、纵横比、倾斜、平移及透射 |
| Affine | 缩放、旋转、纵横比、倾斜及平移 |
| Similarity | 缩放、旋转及平移 |

## ◆ WeightFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum WeightFunEnum | | strong |

权重函数

| 枚举值 | |
| --- | --- |
| LeastSqure | 最小二乘 |
| Huber | Huber |
| Tukey | Tukey |

## ◆ FilterStatusEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FilterStatusEnum | | strong |

中值滤波状态

| 枚举值 | |
| --- | --- |
| FilterStateTure | 执行滤波 |
| FilterStateFalse | 无滤波 |

## ◆ SubpixelWinAutoEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SubpixelWinAutoEnum | | strong |

亚像素窗口

| 枚举值 | |
| --- | --- |
| SubpixelWinSizeAuto | 自适应 |
| SubpixelWinSizeUser | 设置值 |

## ◆ FilterStatus2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FilterStatus2Enum | | strong |

中值滤波状态

| 枚举值 | |
| --- | --- |
| FilterStateTure | 执行滤波 |
| FilterStateFalse | 无滤波 |

## ◆ SubpixelWinAuto2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SubpixelWinAuto2Enum | | strong |

亚像素窗口

| 枚举值 | |
| --- | --- |
| SubpixelWinSizeAuto | 自适应 |
| SubpixelWinSizeUser | 设置值 |

## 成员函数说明

## ◆ DoSaveFile()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int DoSaveFile | ( | string | *value* | ) |  |

生成标定文件

## 属性说明

## ◆ InputImage1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage1 | | set |

输入图像1

**备注**

仅当次执行起效

## ◆ InputImage2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage2 | | set |

输入图像2

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ PhysicalPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> PhysicalPoint | | set |

物理点

**备注**

仅当次执行起效

## ◆ WorldRotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> WorldRotateAngle | | set |

物理角度

**备注**

仅当次执行起效

## ◆ Trigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Trigger | | set |

外部输入字符

**备注**

仅当次执行起效

## ◆ TeachFlagInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> TeachFlagInput | | set |

外部触发字符

**备注**

仅当次执行起效

## ◆ InputType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InputTypeEnum InputType | | getset |

输入方式

## ◆ TeachEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TeachEnable | | getset |

示教

## ◆ TeachFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string TeachFlag | | getset |

外部触发字符

## ◆ CalibPath0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPath0 | | getset |

标定文件1

## ◆ CalibPath1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPath1 | | getset |

标定文件2

## ◆ CalibPathName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPathName | | getset |

标定文件路径

## ◆ RefreshFileEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RefreshFileEnable | | getset |

更新文件

## ◆ CalibBoardType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibBoardTypeEnum CalibBoardType | | getset |

标定板类型

## ◆ HomoFreedom

|  |  |  |
| --- | --- | --- |
| |  | | --- | | HomoFreedomEnum HomoFreedom | | getset |

自由度

## ◆ WeightFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WeightFunEnum WeightFun | | getset |

权重函数

## ◆ WeightFactor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WeightFactor | | getset |

权重系数，范围：[1,200]

## ◆ GrayContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayContrast | | getset |

灰度对比度，范围：[1,255]（弃用）

## ◆ FilterStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FilterStatusEnum FilterStatus | | getset |

中值滤波状态

## ◆ SubpixelWinAuto

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SubpixelWinAutoEnum SubpixelWinAuto | | getset |

亚像素窗口（弃用）

## ◆ SubPixelWindowSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SubPixelWindowSize | | getset |

设置窗口大小，范围：[3,150]（弃用）

## ◆ GrayContrast2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayContrast2 | | getset |

灰度对比度，范围：[1,255]（弃用）

## ◆ FilterStatus2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FilterStatus2Enum FilterStatus2 | | getset |

中值滤波状态

## ◆ SubpixelWinAuto2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SubpixelWinAuto2Enum SubpixelWinAuto2 | | getset |

亚像素窗口（弃用）

## ◆ SubPixelWindowSize2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SubPixelWindowSize2 | | getset |

设置窗口大小，范围：[3,150]（弃用）
