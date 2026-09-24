<!-- src:class_i_m_v_s_rect_find_modu_cs_1_1_rect_find_param.html -->
<!-- path:接口函数 > 定位 > 矩形检测 > RectFindParam -->
# RectFindParam类 参考 定位 » 矩形检测

矩形检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgeTypeEnum {     Widest = 0x1,     Narrowest = 0x2,     Strongest = 0x3,     Worst = 0x4,     First = 0x5,     Last = 0x6,     Nearest = 0x7,     Farthest = 0x8   } |
|  | 边缘对类型 更多... |
|  | |
| enum | EdgeUpPolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 上边缘极性 更多... |
|  | |
| enum | EdgeDownPolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 下边缘极性 更多... |
|  | |
| enum | EdgeLeftPolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 左边缘极性 更多... |
|  | |
| enum | EdgeRightPolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 右边缘极性 更多... |
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
| RectFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| EdgeTypeEnum | EdgeType `[get, set]` |
|  | 边缘对类型 更多... |
|  | |
| EdgeUpPolarityEnum | EdgeUpPolarity `[get, set]` |
|  | 上边缘极性 更多... |
|  | |
| EdgeDownPolarityEnum | EdgeDownPolarity `[get, set]` |
|  | 下边缘极性 更多... |
|  | |
| EdgeLeftPolarityEnum | EdgeLeftPolarity `[get, set]` |
|  | 左边缘极性 更多... |
|  | |
| EdgeRightPolarityEnum | EdgeRightPolarity `[get, set]` |
|  | 右边缘极性 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| int | CaliperNum `[get, set]` |
|  | 卡尺数量，范围：[2,1000] 更多... |
|  | |
| int | IdeaWidth `[get, set]` |
|  | 理想宽度，范围：[1,10000] 更多... |
|  | |
| int | IdeaHeight `[get, set]` |
|  | 理想高度，范围：[1,10000] 更多... |
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
| bool | AngleLimitEnable `[get, set]` |
|  | 角度判断 更多... |
|  | |
| double | AngleLimitLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | CenterXLimitEnable `[get, set]` |
|  | 中心X判断 更多... |
|  | |
| double | CenterXLimitLow `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterXLimitHigh `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CenterYLimitEnable `[get, set]` |
|  | 中心Y判断 更多... |
|  | |
| double | CenterYLimitLow `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterYLimitHigh `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | RectHeightLimitEnable `[get, set]` |
|  | 高度判断 更多... |
|  | |
| double | RectHeightLimitLow `[get, set]` |
|  | 高度范围，范围：[1,99999] 更多... |
|  | |
| double | RectHeightLimitHigh `[get, set]` |
|  | 高度范围，范围：[1,99999] 更多... |
|  | |
| bool | RectWidthLimitEnable `[get, set]` |
|  | 宽度判断 更多... |
|  | |
| double | RectWidthLimitLow `[get, set]` |
|  | 宽度范围，范围：[1,99999] 更多... |
|  | |
| double | RectWidthLimitHigh `[get, set]` |
|  | 宽度范围，范围：[1,99999] 更多... |
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

矩形检测参数

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

## ◆ EdgeUpPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeUpPolarityEnum | | strong |

上边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ EdgeDownPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeDownPolarityEnum | | strong |

下边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ EdgeLeftPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeLeftPolarityEnum | | strong |

左边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ EdgeRightPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeRightPolarityEnum | | strong |

右边缘极性

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
| |  | | --- | | RectFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeTypeEnum EdgeType | | getset |

边缘对类型

## ◆ EdgeUpPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeUpPolarityEnum EdgeUpPolarity | | getset |

上边缘极性

## ◆ EdgeDownPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeDownPolarityEnum EdgeDownPolarity | | getset |

下边缘极性

## ◆ EdgeLeftPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeLeftPolarityEnum EdgeLeftPolarity | | getset |

左边缘极性

## ◆ EdgeRightPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeRightPolarityEnum EdgeRightPolarity | | getset |

右边缘极性

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

理想宽度，范围：[1,10000]

## ◆ IdeaHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int IdeaHeight | | getset |

理想高度，范围：[1,10000]

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

## ◆ CenterXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterXLimitEnable | | getset |

中心X判断

## ◆ CenterXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitLow | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitHigh | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterYLimitEnable | | getset |

中心Y判断

## ◆ CenterYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitLow | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ CenterYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitHigh | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ RectHeightLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RectHeightLimitEnable | | getset |

高度判断

## ◆ RectHeightLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectHeightLimitLow | | getset |

高度范围，范围：[1,99999]

## ◆ RectHeightLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectHeightLimitHigh | | getset |

高度范围，范围：[1,99999]

## ◆ RectWidthLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RectWidthLimitEnable | | getset |

宽度判断

## ◆ RectWidthLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectWidthLimitLow | | getset |

宽度范围，范围：[1,99999]

## ◆ RectWidthLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectWidthLimitHigh | | getset |

宽度范围，范围：[1,99999]
