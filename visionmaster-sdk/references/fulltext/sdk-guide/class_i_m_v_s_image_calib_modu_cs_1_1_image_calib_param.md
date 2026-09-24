<!-- src:class_i_m_v_s_image_calib_modu_cs_1_1_image_calib_param.html -->
<!-- path:接口函数 > 标定 > 畸变标定 > ImageCalibParam -->
# ImageCalibParam类 参考 标定 » 畸变标定

畸变标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CorrectModelEnum {     CorrectModelLinear = 0x1,     CorrectModelRadial = 0x2,     CorrectModelPersRadial = 0x3   } |
|  | 畸变类型 更多... |
|  | |
| enum | CalibBoardTypeEnum {     TypeChecker = 0x1,     TypeCircle = 0x2,     TypeHKI = 0x7,     TypeHKII = 0x6,     TypeHKIV2 = 0x9,     TypeHKIIV2 = 0x8   } |
|  | 标定板类型 更多... |
|  | |
| enum | HomoFreedomEnum {     Perspective = 0x1,     Affine = 0x2,     Similarity = 0x3   } |
|  | 自由度 更多... |
|  | |
| enum | FilterStatusEnum {     FilterStateTure = 0x1,     FilterStateFalse = 0x2   } |
|  | 中值滤波状态 更多... |
|  | |
| enum | SubpixelWinAutoEnum {     SubpixelWinSizeAuto = 0x1,     SubpixelWinSizeUser = 0x2   } |
|  | 亚像素窗口 更多... |
|  | |
| enum | CircleBoardCircleModeEnum {     CircleModeBlack = 0x1,     CircleModeWhite = 0x2   } |
|  | 圆点类型 更多... |
|  | |
| enum | CalibBoardWeightFunEnum {     LeastSqure = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 权重函数 更多... |
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
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | CorrectCenterPoint `[set]` |
|  | 校正中心点 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| CorrectModelEnum | CorrectModel `[get, set]` |
|  | 畸变类型 更多... |
|  | |
| bool | DistortionEvaluationEnable `[get, set]` |
|  | 矫正评估使能 更多... |
|  | |
| bool | OutputPostCorrectionEnable `[get, set]` |
|  | 输出矫正后数据使能 更多... |
|  | |
| double | PointErrorThreshold `[get, set]` |
|  | 评估误差阈值，范围：[0,10] 更多... |
|  | |
| CalibBoardTypeEnum | CalibBoardType `[get, set]` |
|  | 标定板类型 更多... |
|  | |
| HomoFreedomEnum | HomoFreedom `[get, set]` |
|  | 自由度 更多... |
|  | |
| int | GrayContrast `[get, set]` |
|  | 灰度对比度（弃用），范围：[1,255] , Range:[1,255] 更多... |
|  | |
| FilterStatusEnum | FilterStatus `[get, set]` |
|  | 中值滤波状态 更多... |
|  | |
| SubpixelWinAutoEnum | SubpixelWinAuto `[get, set]` |
|  | 亚像素窗口（弃用） 更多... |
|  | |
| int | SubPixelWindowSize `[get, set]` |
|  | 设置窗口大小（弃用），范围：[3,150] , Range:[3,150] 更多... |
|  | |
| int | Circularity `[get, set]` |
|  | 点圆度，范围：[20,100] 更多... |
|  | |
| int | EdgeThreshLow `[get, set]` |
|  | 边缘提取阈值，范围：[0,255] 更多... |
|  | |
| int | EdgeThreshHigh `[get, set]` |
|  | 边缘提取阈值，范围：[0,255] 更多... |
|  | |
| CircleBoardCircleModeEnum | CircleBoardCircleMode `[get, set]` |
|  | 圆点类型 更多... |
|  | |
| CalibBoardWeightFunEnum | CalibBoardWeightFun `[get, set]` |
|  | 权重函数 更多... |
|  | |
| int | WeightFactor `[get, set]` |
|  | 权重系数，范围：[1,200] 更多... |
|  | |
| int | DistThreshold `[get, set]` |
|  | 距离阈值，范围：[1,100] 更多... |
|  | |
| int | SampleRatio `[get, set]` |
|  | 采样率，范围：[1,100] 更多... |
|  | |

## 详细描述

畸变标定参数

## 成员枚举类型说明

## ◆ CorrectModelEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CorrectModelEnum | | strong |

畸变类型

| 枚举值 | |
| --- | --- |
| CorrectModelLinear | 透视畸变 |
| CorrectModelRadial | 径向畸变 |
| CorrectModelPersRadial | 径向透视畸变 |

## ◆ CalibBoardTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibBoardTypeEnum | | strong |

标定板类型

| 枚举值 | |
| --- | --- |
| TypeChecker | 棋盘格标定板 |
| TypeCircle | 圆标定板 |
| TypeHKI | 海康I型标定板 |
| TypeHKII | 海康II型标定板 |
| TypeHKIV2 | 海康扩展I型标定板 |
| TypeHKIIV2 | 海康扩展II型标定板 |

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

## ◆ CircleBoardCircleModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CircleBoardCircleModeEnum | | strong |

圆点类型

| 枚举值 | |
| --- | --- |
| CircleModeBlack | 白底黑圆 |
| CircleModeWhite | 黑底白圆 |

## ◆ CalibBoardWeightFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibBoardWeightFunEnum | | strong |

权重函数

| 枚举值 | |
| --- | --- |
| LeastSqure | 最小二乘 |
| Huber | Huber |
| Tukey | Tukey |

## 成员函数说明

## ◆ DoSaveFile()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int DoSaveFile | ( | string | *value* | ) |  |

生成标定文件

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ CorrectCenterPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CorrectCenterPoint | | set |

校正中心点

**备注**

仅当次执行起效

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

## ◆ CorrectModel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CorrectModelEnum CorrectModel | | getset |

畸变类型

## ◆ DistortionEvaluationEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistortionEvaluationEnable | | getset |

矫正评估使能

## ◆ OutputPostCorrectionEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutputPostCorrectionEnable | | getset |

输出矫正后数据使能

## ◆ PointErrorThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double PointErrorThreshold | | getset |

评估误差阈值，范围：[0,10]

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

## ◆ GrayContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayContrast | | getset |

灰度对比度（弃用），范围：[1,255] , Range:[1,255]

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

设置窗口大小（弃用），范围：[3,150] , Range:[3,150]

## ◆ Circularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Circularity | | getset |

点圆度，范围：[20,100]

## ◆ EdgeThreshLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshLow | | getset |

边缘提取阈值，范围：[0,255]

## ◆ EdgeThreshHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshHigh | | getset |

边缘提取阈值，范围：[0,255]

## ◆ CircleBoardCircleMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CircleBoardCircleModeEnum CircleBoardCircleMode | | getset |

圆点类型

## ◆ CalibBoardWeightFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibBoardWeightFunEnum CalibBoardWeightFun | | getset |

权重函数

## ◆ WeightFactor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WeightFactor | | getset |

权重系数，范围：[1,200]

## ◆ DistThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DistThreshold | | getset |

距离阈值，范围：[1,100]

## ◆ SampleRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SampleRatio | | getset |

采样率，范围：[1,100]
