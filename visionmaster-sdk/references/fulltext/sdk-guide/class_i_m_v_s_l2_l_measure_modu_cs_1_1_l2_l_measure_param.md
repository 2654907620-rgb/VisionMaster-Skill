<!-- src:class_i_m_v_s_l2_l_measure_modu_cs_1_1_l2_l_measure_param.html -->
<!-- path:接口函数 > 测量 > 线线测量 > L2LMeasureParam -->
# L2LMeasureParam类 参考 测量 » 线线测量

线线测量参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ChooseCoordinateEnum {     ImageCor = 0x1,     SpecCor = 0x2   } |
|  | 坐标系选择 更多... |
|  | |
| enum | FindMode1Enum {     Best = 0x1,     First = 0x2,     Last = 0x3,     Mid = 0x4   } |
|  | 边缘类型1 更多... |
|  | |
| enum | EdgePolarity1Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性1 更多... |
|  | |
| enum | InitType1Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合1 更多... |
|  | |
| enum | FitFun1Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式1 更多... |
|  | |
| enum | FindMode2Enum {     Best = 0x1,     First = 0x2,     Last = 0x3,     Mid = 0x4   } |
|  | 边缘类型2 更多... |
|  | |
| enum | EdgePolarity2Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性2 更多... |
|  | |
| enum | InitType2Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合2 更多... |
|  | |
| enum | FitFun2Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式2 更多... |
|  | |
| enum | OutputAngleRangeEnum {     RangeSegment = 0x0,     RangeLinear = 0x1   } |
|  | 输出角度范围 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< Line > | InputLine1 `[set]` |
|  | 输入直线1 更多... |
|  | |
| List< Line > | InputLine2 `[set]` |
|  | 输入直线2 更多... |
|  | |
| List< float > | CalibMatrix `[set]` |
|  | 标定矩阵 更多... |
|  | |
| ChooseCoordinateEnum | ChooseCoordinate `[get, set]` |
|  | 坐标系选择 更多... |
|  | |
| FindMode1Enum | FindMode1 `[get, set]` |
|  | 边缘类型1 更多... |
|  | |
| EdgePolarity1Enum | EdgePolarity1 `[get, set]` |
|  | 边缘极性1 更多... |
|  | |
| int | EdgeThreshold1 `[get, set]` |
|  | 边缘阈值1，范围：[1,255] 更多... |
|  | |
| int | KernelSize1 `[get, set]` |
|  | 滤波尺寸1，范围：[1,50] 更多... |
|  | |
| int | RejectNum1 `[get, set]` |
|  | 剔除点数1，范围：[0,998] 更多... |
|  | |
| int | RejectDist1 `[get, set]` |
|  | 剔除距离1，范围：[1,1000] 更多... |
|  | |
| InitType1Enum | InitType1 `[get, set]` |
|  | 初始拟合1 更多... |
|  | |
| FitFun1Enum | FitFun1 `[get, set]` |
|  | 拟合方式1 更多... |
|  | |
| FindMode2Enum | FindMode2 `[get, set]` |
|  | 边缘类型2 更多... |
|  | |
| EdgePolarity2Enum | EdgePolarity2 `[get, set]` |
|  | 边缘极性2 更多... |
|  | |
| int | EdgeThreshold2 `[get, set]` |
|  | 边缘阈值2，范围：[1,255] 更多... |
|  | |
| int | KernelSize2 `[get, set]` |
|  | 滤波尺寸2，范围：[1,50] 更多... |
|  | |
| int | RejectNum2 `[get, set]` |
|  | 剔除点数2，范围：[0,998] 更多... |
|  | |
| int | RejectDist2 `[get, set]` |
|  | 剔除距离2，范围：[1,1000] 更多... |
|  | |
| InitType2Enum | InitType2 `[get, set]` |
|  | 初始拟合2 更多... |
|  | |
| FitFun2Enum | FitFun2 `[get, set]` |
|  | 拟合方式2 更多... |
|  | |
| OutputAngleRangeEnum | OutputAngleRange `[get, set]` |
|  | 输出角度范围 更多... |
|  | |
| bool | AngleLimitEnable `[get, set]` |
|  | 角度判断 更多... |
|  | |
| double | AngleLimitLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | DistLimitEnable `[get, set]` |
|  | 距离判断 更多... |
|  | |
| double | DistLimitLow `[get, set]` |
|  | 距离范围，范围：[0,99999] 更多... |
|  | |
| double | DistLimitHigh `[get, set]` |
|  | 距离范围，范围：[0,99999] 更多... |
|  | |
| bool | InterXLimitEnable `[get, set]` |
|  | 交点X判断 更多... |
|  | |
| double | InterXLimitLow `[get, set]` |
|  | 交点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | InterXLimitHigh `[get, set]` |
|  | 交点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | InterYLimitEnable `[get, set]` |
|  | 交点Y判断 更多... |
|  | |
| double | InterYLimitLow `[get, set]` |
|  | 交点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | InterYLimitHigh `[get, set]` |
|  | 交点Y范围，范围：[-99999,99999] 更多... |
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

线线测量参数

## 成员枚举类型说明

## ◆ ChooseCoordinateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ChooseCoordinateEnum | | strong |

坐标系选择

| 枚举值 | |
| --- | --- |
| ImageCor | 图像坐标系 |
| SpecCor | 特定坐标系 |

## ◆ FindMode1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode1Enum | | strong |

边缘类型1

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |
| Mid | 接近中线 |

## ◆ EdgePolarity1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity1Enum | | strong |

边缘极性1

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType1Enum | | strong |

初始拟合1

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun1Enum | | strong |

拟合方式1

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ FindMode2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode2Enum | | strong |

边缘类型2

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |
| Mid | 接近中线 |

## ◆ EdgePolarity2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity2Enum | | strong |

边缘极性2

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType2Enum | | strong |

初始拟合2

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun2Enum | | strong |

拟合方式2

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ OutputAngleRangeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum OutputAngleRangeEnum | | strong |

输出角度范围

| 枚举值 | |
| --- | --- |
| RangeSegment | -90°-90° |
| RangeLinear | -180°-180° |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputLine1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine1 | | set |

输入直线1

**备注**

仅当次执行起效

## ◆ InputLine2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine2 | | set |

输入直线2

**备注**

仅当次执行起效

## ◆ CalibMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CalibMatrix | | set |

标定矩阵

**备注**

仅当次执行起效

## ◆ ChooseCoordinate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ChooseCoordinateEnum ChooseCoordinate | | getset |

坐标系选择

## ◆ FindMode1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode1Enum FindMode1 | | getset |

边缘类型1

## ◆ EdgePolarity1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity1Enum EdgePolarity1 | | getset |

边缘极性1

## ◆ EdgeThreshold1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold1 | | getset |

边缘阈值1，范围：[1,255]

## ◆ KernelSize1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize1 | | getset |

滤波尺寸1，范围：[1,50]

## ◆ RejectNum1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum1 | | getset |

剔除点数1，范围：[0,998]

## ◆ RejectDist1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist1 | | getset |

剔除距离1，范围：[1,1000]

## ◆ InitType1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType1Enum InitType1 | | getset |

初始拟合1

## ◆ FitFun1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun1Enum FitFun1 | | getset |

拟合方式1

## ◆ FindMode2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode2Enum FindMode2 | | getset |

边缘类型2

## ◆ EdgePolarity2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity2Enum EdgePolarity2 | | getset |

边缘极性2

## ◆ EdgeThreshold2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold2 | | getset |

边缘阈值2，范围：[1,255]

## ◆ KernelSize2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize2 | | getset |

滤波尺寸2，范围：[1,50]

## ◆ RejectNum2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum2 | | getset |

剔除点数2，范围：[0,998]

## ◆ RejectDist2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist2 | | getset |

剔除距离2，范围：[1,1000]

## ◆ InitType2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType2Enum InitType2 | | getset |

初始拟合2

## ◆ FitFun2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun2Enum FitFun2 | | getset |

拟合方式2

## ◆ OutputAngleRange

|  |  |  |
| --- | --- | --- |
| |  | | --- | | OutputAngleRangeEnum OutputAngleRange | | getset |

输出角度范围

## ◆ AngleLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitEnable | | getset |

角度判断

## ◆ AngleLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitHigh | | getset |

角度范围，范围：[-180,180]

## ◆ DistLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DistLimitEnable | | getset |

距离判断

## ◆ DistLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistLimitLow | | getset |

距离范围，范围：[0,99999]

## ◆ DistLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DistLimitHigh | | getset |

距离范围，范围：[0,99999]

## ◆ InterXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool InterXLimitEnable | | getset |

交点X判断

## ◆ InterXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double InterXLimitLow | | getset |

交点X范围，范围：[-99999,99999]

## ◆ InterXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double InterXLimitHigh | | getset |

交点X范围，范围：[-99999,99999]

## ◆ InterYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool InterYLimitEnable | | getset |

交点Y判断

## ◆ InterYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double InterYLimitLow | | getset |

交点Y范围，范围：[-99999,99999]

## ◆ InterYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double InterYLimitHigh | | getset |

交点Y范围，范围：[-99999,99999]
