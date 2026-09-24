<!-- src:class_i_m_v_s_line_find_modu_cs_1_1_line_find_param.html -->
<!-- path:接口函数 > 定位 > 直线查找 > LineFindParam -->
# LineFindParam类 参考 定位 » 直线查找

直线查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FindModeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3,     Mid = 0x4   } |
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
| LineFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FindModeEnum | FindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| int | KernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | RayNum `[get, set]` |
|  | 卡尺数量，范围：[2,1000] 更多... |
|  | |
| bool | RevertFindOrient `[get, set]` |
|  | 直线查找反向 更多... |
|  | |
| bool | AngleNormalization `[get, set]` |
|  | 角度归一化 更多... |
|  | |
| bool | LineAngleEnable `[get, set]` |
|  | 角度使能 更多... |
|  | |
| double | ExpectAngle `[get, set]` |
|  | 期望直线角度，范围：[-180,180] 更多... |
|  | |
| double | RotateTolerance `[get, set]` |
|  | 角度旋转容忍，范围：[0,180] 更多... |
|  | |
| int | RejectNum `[get, set]` |
|  | 剔除点数，范围：[0,998] 更多... |
|  | |
| int | RejectDist `[get, set]` |
|  | 剔除距离，范围：[1,1000] 更多... |
|  | |
| int | RegionWidth `[get, set]` |
|  | 投影宽度，范围：[1,100] 更多... |
|  | |
| InitTypeEnum | InitType `[get, set]` |
|  | 初始拟合 更多... |
|  | |
| FitFunEnum | FitFun `[get, set]` |
|  | 拟合方式 更多... |
|  | |
| bool | FitPointsLimitEnable `[get, set]` |
|  | 匹配点数判断 更多... |
|  | |
| int | FitPointsLimitLow `[get, set]` |
|  | 拟合点数范围，范围：[2,99999] 更多... |
|  | |
| int | FitPointsLimitHigh `[get, set]` |
|  | 拟合点数范围，范围：[2,99999] 更多... |
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
| bool | ScoreLimitEnable `[get, set]` |
|  | 拟合误差判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
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

直线查找参数

## 成员枚举类型说明

## ◆ FindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |
| Mid | 接近中线 |

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
| |  | | --- | | LineFindRoiManager ModuRoiManager | | get |

ROI管理器

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

## ◆ EdgeStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeStrength | | getset |

边缘阈值，范围：[1,255]

## ◆ KernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int KernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ RayNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RayNum | | getset |

卡尺数量，范围：[2,1000]

## ◆ RevertFindOrient

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RevertFindOrient | | getset |

直线查找反向

## ◆ AngleNormalization

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleNormalization | | getset |

角度归一化

## ◆ LineAngleEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LineAngleEnable | | getset |

角度使能

## ◆ ExpectAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ExpectAngle | | getset |

期望直线角度，范围：[-180,180]

## ◆ RotateTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RotateTolerance | | getset |

角度旋转容忍，范围：[0,180]

## ◆ RejectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum | | getset |

剔除点数，范围：[0,998]

## ◆ RejectDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist | | getset |

剔除距离，范围：[1,1000]

## ◆ RegionWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth | | getset |

投影宽度，范围：[1,100]

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

## ◆ FitPointsLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FitPointsLimitEnable | | getset |

匹配点数判断

## ◆ FitPointsLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitPointsLimitLow | | getset |

拟合点数范围，范围：[2,99999]

## ◆ FitPointsLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitPointsLimitHigh | | getset |

拟合点数范围，范围：[2,99999]

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

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

拟合误差判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

拟合误差范围，范围：[0,9999]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

拟合误差范围，范围：[0,9999]
