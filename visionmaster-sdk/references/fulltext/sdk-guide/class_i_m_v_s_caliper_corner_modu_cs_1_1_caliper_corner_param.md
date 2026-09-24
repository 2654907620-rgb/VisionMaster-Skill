<!-- src:class_i_m_v_s_caliper_corner_modu_cs_1_1_caliper_corner_param.html -->
<!-- path:接口函数 > 定位 > 边缘交点 > CaliperCornerParam -->
# CaliperCornerParam类 参考 定位 » 边缘交点

边缘交点参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | Edge0TypeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘1类型 更多... |
|  | |
| enum | Edge0PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘1极性 更多... |
|  | |
| enum | Edge1TypeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘2类型 更多... |
|  | |
| enum | Edge1PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘2极性 更多... |
|  | |
| enum | FitInitTypeEnum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合 更多... |
|  | |
| enum | FitFunEnum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CaliperCornerRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| Edge0TypeEnum | Edge0Type `[get, set]` |
|  | 边缘1类型 更多... |
|  | |
| Edge0PolarityEnum | Edge0Polarity `[get, set]` |
|  | 边缘1极性 更多... |
|  | |
| Edge1TypeEnum | Edge1Type `[get, set]` |
|  | 边缘2类型 更多... |
|  | |
| Edge1PolarityEnum | Edge1Polarity `[get, set]` |
|  | 边缘2极性 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| int | CaliperNum `[get, set]` |
|  | 卡尺数量，范围：[2,1000] 更多... |
|  | |
| int | KernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | ProjectLen `[get, set]` |
|  | 投影宽度，范围：[1,100] 更多... |
|  | |
| int | RejectNum `[get, set]` |
|  | 剔除点数，范围：[0,100] 更多... |
|  | |
| int | RejectDist `[get, set]` |
|  | 剔除距离，范围：[1,1000] 更多... |
|  | |
| FitInitTypeEnum | FitInitType `[get, set]` |
|  | 初始拟合 更多... |
|  | |
| FitFunEnum | FitFun `[get, set]` |
|  | 拟合方式 更多... |
|  | |
| bool | CornerPointXLimitEnable `[get, set]` |
|  | 交点X判断 更多... |
|  | |
| double | CornerPointXLimitLow `[get, set]` |
|  | 交点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CornerPointXLimitHigh `[get, set]` |
|  | 交点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CornerPointYLimitEnable `[get, set]` |
|  | 交点Y判断 更多... |
|  | |
| double | CornerPointYLimitLow `[get, set]` |
|  | 交点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CornerPointYLimitHigh `[get, set]` |
|  | 交点Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CornerAngleLimitEnable `[get, set]` |
|  | 交点角度判断 更多... |
|  | |
| double | CornerAngleLimitLow `[get, set]` |
|  | 交点角度范围，范围：[-180,180] 更多... |
|  | |
| double | CornerAngleLimitHigh `[get, set]` |
|  | 交点角度范围，范围：[-180,180] 更多... |
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

边缘交点参数

## 成员枚举类型说明

## ◆ Edge0TypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge0TypeEnum | | strong |

边缘1类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ Edge0PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge0PolarityEnum | | strong |

边缘1极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ Edge1TypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge1TypeEnum | | strong |

边缘2类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ Edge1PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge1PolarityEnum | | strong |

边缘2极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ FitInitTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitInitTypeEnum | | strong |

初始拟合

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFunEnum | | strong |

拟合方式

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

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
| |  | | --- | | CaliperCornerRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ Edge0Type

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge0TypeEnum Edge0Type | | getset |

边缘1类型

## ◆ Edge0Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge0PolarityEnum Edge0Polarity | | getset |

边缘1极性

## ◆ Edge1Type

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge1TypeEnum Edge1Type | | getset |

边缘2类型

## ◆ Edge1Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge1PolarityEnum Edge1Polarity | | getset |

边缘2极性

## ◆ EdgeStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeStrength | | getset |

边缘阈值，范围：[0,255]

## ◆ CaliperNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperNum | | getset |

卡尺数量，范围：[2,1000]

## ◆ KernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ ProjectLen

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ProjectLen | | getset |

投影宽度，范围：[1,100]

## ◆ RejectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum | | getset |

剔除点数，范围：[0,100]

## ◆ RejectDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist | | getset |

剔除距离，范围：[1,1000]

## ◆ FitInitType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitInitTypeEnum FitInitType | | getset |

初始拟合

## ◆ FitFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFunEnum FitFun | | getset |

拟合方式

## ◆ CornerPointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CornerPointXLimitEnable | | getset |

交点X判断

## ◆ CornerPointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerPointXLimitLow | | getset |

交点X范围，范围：[-99999,99999]

## ◆ CornerPointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerPointXLimitHigh | | getset |

交点X范围，范围：[-99999,99999]

## ◆ CornerPointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CornerPointYLimitEnable | | getset |

交点Y判断

## ◆ CornerPointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerPointYLimitLow | | getset |

交点Y范围，范围：[-99999,99999]

## ◆ CornerPointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerPointYLimitHigh | | getset |

交点Y范围，范围：[-99999,99999]

## ◆ CornerAngleLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CornerAngleLimitEnable | | getset |

交点角度判断

## ◆ CornerAngleLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerAngleLimitLow | | getset |

交点角度范围，范围：[-180,180]

## ◆ CornerAngleLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CornerAngleLimitHigh | | getset |

交点角度范围，范围：[-180,180]
