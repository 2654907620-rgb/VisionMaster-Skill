<!-- src:class_i_m_v_s_pair_line_modu_cs_1_1_pair_line_param.html -->
<!-- path:接口函数 > 定位 > 平行线查找 > PairLineParam -->
# PairLineParam类 参考 定位 » 平行线查找

平行线查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgeTypeEnum {     Widest = 0x1,     Narrowest = 0x2,     Strongest = 0x3,     Worst = 0x4,     First = 0x5,     Last = 0x6,     Nearest = 0x7,     Farthest = 0x8   } |
|  | 边缘对类型 更多... |
|  | |
| enum | Edge0PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘0极性 更多... |
|  | |
| enum | Edge1PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘1极性 更多... |
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
| PairLineRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| EdgeTypeEnum | EdgeType `[get, set]` |
|  | 边缘对类型 更多... |
|  | |
| Edge0PolarityEnum | Edge0Polarity `[get, set]` |
|  | 边缘0极性 更多... |
|  | |
| Edge1PolarityEnum | Edge1Polarity `[get, set]` |
|  | 边缘1极性 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| int | CaliperNum `[get, set]` |
|  | 卡尺数量，范围：[2,1000] 更多... |
|  | |
| int | IdeaWidth `[get, set]` |
|  | 理想间距，范围：[1,10000] 更多... |
|  | |
| int | AngleTol `[get, set]` |
|  | 最大角度差，范围：[0,180] 更多... |
|  | |
| int | RejectNum `[get, set]` |
|  | 剔除点数，范围：[0,100] 更多... |
|  | |
| int | RejectDist `[get, set]` |
|  | 剔除距离，范围：[1,1000] 更多... |
|  | |
| int | KernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | ProjectLen `[get, set]` |
|  | 投影宽度，范围：[1,100] 更多... |
|  | |
| FitInitTypeEnum | FitInitType `[get, set]` |
|  | 初始拟合 更多... |
|  | |
| FitFunEnum | FitFun `[get, set]` |
|  | 拟合方式 更多... |
|  | |
| bool | LineWidthLimitEnable `[get, set]` |
|  | 线对宽度 更多... |
|  | |
| double | LineWidthLimitLow `[get, set]` |
|  | 宽度范围，范围：[0,9999] 更多... |
|  | |
| double | LineWidthLimitHigh `[get, set]` |
|  | 宽度范围，范围：[0,9999] 更多... |
|  | |
| bool | Angle0LimitEnable `[get, set]` |
|  | 直线0角度 更多... |
|  | |
| double | Angle0LimitLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | Angle0LimitHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | Angle1LimitEnable `[get, set]` |
|  | 直线1角度 更多... |
|  | |
| double | Angle1LimitLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | Angle1LimitHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
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

平行线查找参数

## 成员枚举类型说明

## ◆ EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeTypeEnum | | strong |

边缘对类型

| 枚举值 | |
| --- | --- |
| Widest | 最宽 |
| Narrowest | 最窄 |
| Strongest | 最强 |
| Worst | 最弱 |
| First | 第一对 |
| Last | 最后一对 |
| Nearest | 最接近 |
| Farthest | 最不接近 |

## ◆ Edge0PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge0PolarityEnum | | strong |

边缘0极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ Edge1PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Edge1PolarityEnum | | strong |

边缘1极性

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
| |  | | --- | | PairLineRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeTypeEnum EdgeType | | getset |

边缘对类型

## ◆ Edge0Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge0PolarityEnum Edge0Polarity | | getset |

边缘0极性

## ◆ Edge1Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge1PolarityEnum Edge1Polarity | | getset |

边缘1极性

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

## ◆ IdeaWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int IdeaWidth | | getset |

理想间距，范围：[1,10000]

## ◆ AngleTol

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int AngleTol | | getset |

最大角度差，范围：[0,180]

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

## ◆ LineWidthLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LineWidthLimitEnable | | getset |

线对宽度

## ◆ LineWidthLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LineWidthLimitLow | | getset |

宽度范围，范围：[0,9999]

## ◆ LineWidthLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LineWidthLimitHigh | | getset |

宽度范围，范围：[0,9999]

## ◆ Angle0LimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Angle0LimitEnable | | getset |

直线0角度

## ◆ Angle0LimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Angle0LimitLow | | getset |

角度范围，范围：[-180,180]

## ◆ Angle0LimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Angle0LimitHigh | | getset |

角度范围，范围：[-180,180]

## ◆ Angle1LimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Angle1LimitEnable | | getset |

直线1角度

## ◆ Angle1LimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Angle1LimitLow | | getset |

角度范围，范围：[-180,180]

## ◆ Angle1LimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Angle1LimitHigh | | getset |

角度范围，范围：[-180,180]
