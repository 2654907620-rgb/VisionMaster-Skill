<!-- src:class_i_m_v_s_circle_find_modu_cs_1_1_circle_find_param.html -->
<!-- path:接口函数 > 定位 > 圆查找 > CircleFindParam -->
# CircleFindParam类 参考 定位 » 圆查找

圆查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FindModeEnum {     Best = 0x1,     Largest = 0x2,     SMALLEST = 0x3   } |
|  | 边缘类型 更多... |
|  | |
| enum | EdgePolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性 更多... |
|  | |
| enum | InitTypeEnum {     ALS = 0x1,     LLS = 0x2   } |
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
| CircleFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | MinRadius `[get, set]` |
|  | 扇环半径，范围：[1,10000] 更多... |
|  | |
| int | MaxRadius `[get, set]` |
|  | 扇环半径，范围：[1,10000] 更多... |
|  | |
| FindModeEnum | FindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | EdgeThresh `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| int | EdgeWidth `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | RadNum `[get, set]` |
|  | 卡尺数量，范围：[3,1000] 更多... |
|  | |
| int | RejectNum `[get, set]` |
|  | 剔除点数，范围：[0,997] 更多... |
|  | |
| bool | CoarseDetectFlag `[get, set]` |
|  | 初定位 更多... |
|  | |
| int | CCDSampleScale `[get, set]` |
|  | 下采样系数，范围：[1,8] 更多... |
|  | |
| int | CCDCircleThresh `[get, set]` |
|  | 圆定位敏感度，范围：[1,1000] 更多... |
|  | |
| int | RejectDist `[get, set]` |
|  | 剔除距离，范围：[1,1000] 更多... |
|  | |
| int | ProLength `[get, set]` |
|  | 投影宽度，范围：[1,500] 更多... |
|  | |
| InitTypeEnum | InitType `[get, set]` |
|  | 初始拟合 更多... |
|  | |
| FitFunEnum | FitFun `[get, set]` |
|  | 拟合方式 更多... |
|  | |
| bool | RadiusLimitEnable `[get, set]` |
|  | 半径判断 更多... |
|  | |
| double | RadiusLimitLow `[get, set]` |
|  | 半径判断，范围：[0,99999] 更多... |
|  | |
| double | RadiusLimitHigh `[get, set]` |
|  | 半径判断，范围：[0,99999] 更多... |
|  | |
| bool | CenterXLimitEnable `[get, set]` |
|  | 中心X判断 更多... |
|  | |
| double | CenterXLimitLow `[get, set]` |
|  | 中心X判断，范围：[-99999,99999] 更多... |
|  | |
| double | CenterXLimitHigh `[get, set]` |
|  | 中心X判断，范围：[-99999,99999] 更多... |
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
| bool | FitErrorLimitEnable `[get, set]` |
|  | 拟合误差判断 更多... |
|  | |
| double | FitErrorLimitLow `[get, set]` |
|  | 拟合误差范围，范围：[0,100.0] 更多... |
|  | |
| double | FitErrorLimitHigh `[get, set]` |
|  | 拟合误差范围，范围：[0,100.0] 更多... |
|  | |
| bool | FitPointsLimitEnable `[get, set]` |
|  | 匹配点数判断 更多... |
|  | |
| int | FitPointsLimitLow `[get, set]` |
|  | 拟合点数范围，范围：[3,99999] 更多... |
|  | |
| int | FitPointsLimitHigh `[get, set]` |
|  | 拟合点数范围，范围：[3,99999] 更多... |
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

圆查找参数

## 成员枚举类型说明

## ◆ FindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| Largest | 最后一条 |
| SMALLEST | 第一条 |

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

## ◆ InitTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitTypeEnum | | strong |

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
| |  | | --- | | CircleFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ MinRadius

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinRadius | | getset |

扇环半径，范围：[1,10000]

## ◆ MaxRadius

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxRadius | | getset |

扇环半径，范围：[1,10000]

## ◆ FindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindModeEnum FindMode | | getset |

边缘类型

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘极性

## ◆ EdgeThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThresh | | getset |

边缘阈值，范围：[0,255]

## ◆ EdgeWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeWidth | | getset |

滤波尺寸，范围：[1,50]

## ◆ RadNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RadNum | | getset |

卡尺数量，范围：[3,1000]

## ◆ RejectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum | | getset |

剔除点数，范围：[0,997]

## ◆ CoarseDetectFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CoarseDetectFlag | | getset |

初定位

## ◆ CCDSampleScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CCDSampleScale | | getset |

下采样系数，范围：[1,8]

## ◆ CCDCircleThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CCDCircleThresh | | getset |

圆定位敏感度，范围：[1,1000]

## ◆ RejectDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist | | getset |

剔除距离，范围：[1,1000]

## ◆ ProLength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ProLength | | getset |

投影宽度，范围：[1,500]

## ◆ InitType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitTypeEnum InitType | | getset |

初始拟合

## ◆ FitFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FitFunEnum FitFun | | getset |

拟合方式

## ◆ RadiusLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RadiusLimitEnable | | getset |

半径判断

## ◆ RadiusLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RadiusLimitLow | | getset |

半径判断，范围：[0,99999]

## ◆ RadiusLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RadiusLimitHigh | | getset |

半径判断，范围：[0,99999]

## ◆ CenterXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterXLimitEnable | | getset |

中心X判断

## ◆ CenterXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitLow | | getset |

中心X判断，范围：[-99999,99999]

## ◆ CenterXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitHigh | | getset |

中心X判断，范围：[-99999,99999]

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

## ◆ FitErrorLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FitErrorLimitEnable | | getset |

拟合误差判断

## ◆ FitErrorLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double FitErrorLimitLow | | getset |

拟合误差范围，范围：[0,100.0]

## ◆ FitErrorLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double FitErrorLimitHigh | | getset |

拟合误差范围，范围：[0,100.0]

## ◆ FitPointsLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FitPointsLimitEnable | | getset |

匹配点数判断

## ◆ FitPointsLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitPointsLimitLow | | getset |

拟合点数范围，范围：[3,99999]

## ◆ FitPointsLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitPointsLimitHigh | | getset |

拟合点数范围，范围：[3,99999]
