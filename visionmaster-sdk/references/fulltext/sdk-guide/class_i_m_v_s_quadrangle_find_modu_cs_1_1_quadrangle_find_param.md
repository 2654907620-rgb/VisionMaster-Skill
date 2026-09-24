<!-- src:class_i_m_v_s_quadrangle_find_modu_cs_1_1_quadrangle_find_param.html -->
<!-- path:接口函数 > 定位 > 四边形查找 > QuadrangleFindParam -->
# QuadrangleFindParam类 参考 定位 » 四边形查找

四边形查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FindMode0Enum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型1 更多... |
|  | |
| enum | EdgePolarity0Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性1 更多... |
|  | |
| enum | InitType0Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合1 更多... |
|  | |
| enum | FitFun0Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式1 更多... |
|  | |
| enum | FindMode1Enum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型2 更多... |
|  | |
| enum | EdgePolarity1Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性2 更多... |
|  | |
| enum | InitType1Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合2 更多... |
|  | |
| enum | FitFun1Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式2 更多... |
|  | |
| enum | FindMode2Enum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型3 更多... |
|  | |
| enum | EdgePolarity2Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性3 更多... |
|  | |
| enum | InitType2Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合3 更多... |
|  | |
| enum | FitFun2Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式3 更多... |
|  | |
| enum | FindMode3Enum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型4 更多... |
|  | |
| enum | EdgePolarity3Enum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性4 更多... |
|  | |
| enum | InitType3Enum {     ALS = 0x1,     LLS = 0x2   } |
|  | 初始拟合4 更多... |
|  | |
| enum | FitFun3Enum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式4 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| QuadrangleFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FindMode0Enum | FindMode0 `[get, set]` |
|  | 边缘类型1 更多... |
|  | |
| EdgePolarity0Enum | EdgePolarity0 `[get, set]` |
|  | 边缘极性1 更多... |
|  | |
| int | EdgeThreshold0 `[get, set]` |
|  | 边缘阈值1，范围：[1,255] 更多... |
|  | |
| int | KernelSize0 `[get, set]` |
|  | 滤波尺寸1，范围：[1,50] 更多... |
|  | |
| int | CaliperNum0 `[get, set]` |
|  | 卡尺数量1，范围：[2,1000] 更多... |
|  | |
| int | RejectNum0 `[get, set]` |
|  | 剔除点数1，范围：[0,998] 更多... |
|  | |
| int | RejectDist0 `[get, set]` |
|  | 剔除距离1，范围：[1,1000] 更多... |
|  | |
| int | RegionWidth0 `[get, set]` |
|  | 投影宽度1，范围：[1,100] 更多... |
|  | |
| InitType0Enum | InitType0 `[get, set]` |
|  | 初始拟合1 更多... |
|  | |
| FitFun0Enum | FitFun0 `[get, set]` |
|  | 拟合方式1 更多... |
|  | |
| FindMode1Enum | FindMode1 `[get, set]` |
|  | 边缘类型2 更多... |
|  | |
| EdgePolarity1Enum | EdgePolarity1 `[get, set]` |
|  | 边缘极性2 更多... |
|  | |
| int | EdgeThreshold1 `[get, set]` |
|  | 边缘阈值2，范围：[1,255] 更多... |
|  | |
| int | KernelSize1 `[get, set]` |
|  | 滤波尺寸2，范围：[1,50] 更多... |
|  | |
| int | CaliperNum1 `[get, set]` |
|  | 卡尺数量2，范围：[2,1000] 更多... |
|  | |
| int | RejectNum1 `[get, set]` |
|  | 剔除点数2，范围：[0,998] 更多... |
|  | |
| int | RejectDist1 `[get, set]` |
|  | 剔除距离2，范围：[1,1000] 更多... |
|  | |
| int | RegionWidth1 `[get, set]` |
|  | 投影宽度2，范围：[1,100] 更多... |
|  | |
| InitType1Enum | InitType1 `[get, set]` |
|  | 初始拟合2 更多... |
|  | |
| FitFun1Enum | FitFun1 `[get, set]` |
|  | 拟合方式2 更多... |
|  | |
| FindMode2Enum | FindMode2 `[get, set]` |
|  | 边缘类型3 更多... |
|  | |
| EdgePolarity2Enum | EdgePolarity2 `[get, set]` |
|  | 边缘极性3 更多... |
|  | |
| int | EdgeThreshold2 `[get, set]` |
|  | 边缘阈值3，范围：[1,255] 更多... |
|  | |
| int | KernelSize2 `[get, set]` |
|  | 滤波尺寸3，范围：[1,50] 更多... |
|  | |
| int | CaliperNum2 `[get, set]` |
|  | 卡尺数量3，范围：[2,1000] 更多... |
|  | |
| int | RejectNum2 `[get, set]` |
|  | 剔除点数3，范围：[0,998] 更多... |
|  | |
| int | RejectDist2 `[get, set]` |
|  | 剔除距离3，范围：[1,1000] 更多... |
|  | |
| int | RegionWidth2 `[get, set]` |
|  | 投影宽度3，范围：[1,100] 更多... |
|  | |
| InitType2Enum | InitType2 `[get, set]` |
|  | 初始拟合3 更多... |
|  | |
| FitFun2Enum | FitFun2 `[get, set]` |
|  | 拟合方式3 更多... |
|  | |
| FindMode3Enum | FindMode3 `[get, set]` |
|  | 边缘类型4 更多... |
|  | |
| EdgePolarity3Enum | EdgePolarity3 `[get, set]` |
|  | 边缘极性4 更多... |
|  | |
| int | EdgeThreshold3 `[get, set]` |
|  | 边缘阈值4，范围：[1,255] 更多... |
|  | |
| int | KernelSize3 `[get, set]` |
|  | 滤波尺寸4，范围：[1,50] 更多... |
|  | |
| int | CaliperNum3 `[get, set]` |
|  | 卡尺数量4，范围：[2,1000] 更多... |
|  | |
| int | RejectNum3 `[get, set]` |
|  | 剔除点数4，范围：[0,998] 更多... |
|  | |
| int | RejectDist3 `[get, set]` |
|  | 剔除距离4，范围：[1,1000] 更多... |
|  | |
| int | RegionWidth3 `[get, set]` |
|  | 投影宽度4，范围：[1,100] 更多... |
|  | |
| InitType3Enum | InitType3 `[get, set]` |
|  | 初始拟合4 更多... |
|  | |
| FitFun3Enum | FitFun3 `[get, set]` |
|  | 拟合方式4 更多... |
|  | |
| bool | CentralPointXLimitEnable `[get, set]` |
|  | 中心点X判断 更多... |
|  | |
| double | CentralPointXLimitLow `[get, set]` |
|  | 中心点X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CentralPointXLimitHigh `[get, set]` |
|  | 中心点X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CentralPointYLimitEnable `[get, set]` |
|  | 中心点Y判断 更多... |
|  | |
| double | CentralPointYLimitLow `[get, set]` |
|  | 中心点Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CentralPointYLimitHigh `[get, set]` |
|  | 中心点Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | AngleLimitFirstEnable `[get, set]` |
|  | 直线1角度判断 更多... |
|  | |
| double | AngleLimitFirstLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitFirstHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | AngleLimitSecondEnable `[get, set]` |
|  | 直线2角度判断 更多... |
|  | |
| double | AngleLimitSecondLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitSecondHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | AngleLimitThirdEnable `[get, set]` |
|  | 直线3角度判断 更多... |
|  | |
| double | AngleLimitThirdLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitThirdHigh `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | AngleLimitFourthEnable `[get, set]` |
|  | 直线4角度判断 更多... |
|  | |
| double | AngleLimitFourthLow `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitFourthHigh `[get, set]` |
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

四边形查找参数

## 成员枚举类型说明

## ◆ FindMode0Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode0Enum | | strong |

边缘类型1

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePolarity0Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity0Enum | | strong |

边缘极性1

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType0Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType0Enum | | strong |

初始拟合1

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun0Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun0Enum | | strong |

拟合方式1

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ FindMode1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode1Enum | | strong |

边缘类型2

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePolarity1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity1Enum | | strong |

边缘极性2

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType1Enum | | strong |

初始拟合2

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun1Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun1Enum | | strong |

拟合方式2

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ FindMode2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode2Enum | | strong |

边缘类型3

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePolarity2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity2Enum | | strong |

边缘极性3

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType2Enum | | strong |

初始拟合3

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun2Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun2Enum | | strong |

拟合方式3

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ FindMode3Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindMode3Enum | | strong |

边缘类型4

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePolarity3Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarity3Enum | | strong |

边缘极性4

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitType3Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitType3Enum | | strong |

初始拟合4

| 枚举值 | |
| --- | --- |
| ALS | 全局 |
| LLS | 局部 |

## ◆ FitFun3Enum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FitFun3Enum | | strong |

拟合方式4

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
| |  | | --- | | QuadrangleFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FindMode0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode0Enum FindMode0 | | getset |

边缘类型1

## ◆ EdgePolarity0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity0Enum EdgePolarity0 | | getset |

边缘极性1

## ◆ EdgeThreshold0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold0 | | getset |

边缘阈值1，范围：[1,255]

## ◆ KernelSize0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize0 | | getset |

滤波尺寸1，范围：[1,50]

## ◆ CaliperNum0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperNum0 | | getset |

卡尺数量1，范围：[2,1000]

## ◆ RejectNum0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum0 | | getset |

剔除点数1，范围：[0,998]

## ◆ RejectDist0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist0 | | getset |

剔除距离1，范围：[1,1000]

## ◆ RegionWidth0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth0 | | getset |

投影宽度1，范围：[1,100]

## ◆ InitType0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType0Enum InitType0 | | getset |

初始拟合1

## ◆ FitFun0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun0Enum FitFun0 | | getset |

拟合方式1

## ◆ FindMode1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode1Enum FindMode1 | | getset |

边缘类型2

## ◆ EdgePolarity1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity1Enum EdgePolarity1 | | getset |

边缘极性2

## ◆ EdgeThreshold1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold1 | | getset |

边缘阈值2，范围：[1,255]

## ◆ KernelSize1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize1 | | getset |

滤波尺寸2，范围：[1,50]

## ◆ CaliperNum1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperNum1 | | getset |

卡尺数量2，范围：[2,1000]

## ◆ RejectNum1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum1 | | getset |

剔除点数2，范围：[0,998]

## ◆ RejectDist1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist1 | | getset |

剔除距离2，范围：[1,1000]

## ◆ RegionWidth1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth1 | | getset |

投影宽度2，范围：[1,100]

## ◆ InitType1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType1Enum InitType1 | | getset |

初始拟合2

## ◆ FitFun1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun1Enum FitFun1 | | getset |

拟合方式2

## ◆ FindMode2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode2Enum FindMode2 | | getset |

边缘类型3

## ◆ EdgePolarity2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity2Enum EdgePolarity2 | | getset |

边缘极性3

## ◆ EdgeThreshold2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold2 | | getset |

边缘阈值3，范围：[1,255]

## ◆ KernelSize2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize2 | | getset |

滤波尺寸3，范围：[1,50]

## ◆ CaliperNum2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperNum2 | | getset |

卡尺数量3，范围：[2,1000]

## ◆ RejectNum2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum2 | | getset |

剔除点数3，范围：[0,998]

## ◆ RejectDist2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist2 | | getset |

剔除距离3，范围：[1,1000]

## ◆ RegionWidth2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth2 | | getset |

投影宽度3，范围：[1,100]

## ◆ InitType2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType2Enum InitType2 | | getset |

初始拟合3

## ◆ FitFun2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun2Enum FitFun2 | | getset |

拟合方式3

## ◆ FindMode3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindMode3Enum FindMode3 | | getset |

边缘类型4

## ◆ EdgePolarity3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarity3Enum EdgePolarity3 | | getset |

边缘极性4

## ◆ EdgeThreshold3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold3 | | getset |

边缘阈值4，范围：[1,255]

## ◆ KernelSize3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize3 | | getset |

滤波尺寸4，范围：[1,50]

## ◆ CaliperNum3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperNum3 | | getset |

卡尺数量4，范围：[2,1000]

## ◆ RejectNum3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum3 | | getset |

剔除点数4，范围：[0,998]

## ◆ RejectDist3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist3 | | getset |

剔除距离4，范围：[1,1000]

## ◆ RegionWidth3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth3 | | getset |

投影宽度4，范围：[1,100]

## ◆ InitType3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitType3Enum InitType3 | | getset |

初始拟合4

## ◆ FitFun3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFun3Enum FitFun3 | | getset |

拟合方式4

## ◆ CentralPointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CentralPointXLimitEnable | | getset |

中心点X判断

## ◆ CentralPointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentralPointXLimitLow | | getset |

中心点X范围，范围：[-99999,99999]

## ◆ CentralPointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentralPointXLimitHigh | | getset |

中心点X范围，范围：[-99999,99999]

## ◆ CentralPointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CentralPointYLimitEnable | | getset |

中心点Y判断

## ◆ CentralPointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentralPointYLimitLow | | getset |

中心点Y范围，范围：[-99999,99999]

## ◆ CentralPointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentralPointYLimitHigh | | getset |

中心点Y范围，范围：[-99999,99999]

## ◆ AngleLimitFirstEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitFirstEnable | | getset |

直线1角度判断

## ◆ AngleLimitFirstLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitFirstLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitFirstHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitFirstHigh | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitSecondEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitSecondEnable | | getset |

直线2角度判断

## ◆ AngleLimitSecondLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitSecondLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitSecondHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitSecondHigh | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitThirdEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitThirdEnable | | getset |

直线3角度判断

## ◆ AngleLimitThirdLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitThirdLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitThirdHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitThirdHigh | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitFourthEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitFourthEnable | | getset |

直线4角度判断

## ◆ AngleLimitFourthLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitFourthLow | | getset |

角度范围，范围：[-180,180]

## ◆ AngleLimitFourthHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitFourthHigh | | getset |

角度范围，范围：[-180,180]
