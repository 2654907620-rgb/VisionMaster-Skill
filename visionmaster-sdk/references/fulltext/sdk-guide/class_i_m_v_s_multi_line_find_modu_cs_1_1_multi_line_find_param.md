<!-- src:class_i_m_v_s_multi_line_find_modu_cs_1_1_multi_line_find_param.html -->
<!-- path:接口函数 > 定位 > 多直线查找 > MultiLineFindParam -->
# MultiLineFindParam类 参考 定位 » 多直线查找

多直线查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgePolarityEnum {     DarkToBright = 1,     BrightToDark = 2,     Mixed = 3,     Either = 4   } |
|  | 直线边缘极性 更多... |
|  | |
| enum | LineFitFunEnum {     LS = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 拟合方式 更多... |
|  | |
| enum | SortTypeEnum {     InGroupPtNumDscend = 0x1,     RhoAscend = 0x2,     RhoDscend = 0x3   } |
|  | 排序类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| MultiLineFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | GradientFieldSize `[get, set]` |
|  | 滤波核半宽，范围：[1,50] 更多... |
|  | |
| int | ProjectionLength `[get, set]` |
|  | 投影长度，范围：[3,100] 更多... |
|  | |
| int | EdgeThreshold `[get, set]` |
|  | 绝对边缘阈值，范围：[0,255] 更多... |
|  | |
| int | NormalContrast `[get, set]` |
|  | 相对边缘阈值，范围：[0,100] 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 直线边缘极性 更多... |
|  | |
| int | EdgeAngleTolerance `[get, set]` |
|  | 边缘角度容忍，范围：[0,90] 更多... |
|  | |
| int | EdgeDistTolerance `[get, set]` |
|  | 边缘距离容忍，范围：[0,100] 更多... |
|  | |
| int | LineMaxNum `[get, set]` |
|  | 多线最大条数，范围：[1,1000] 更多... |
|  | |
| int | LineCoverage `[get, set]` |
|  | 覆盖率阈值，范围：[0,100] 更多... |
|  | |
| int | LineRotationTolerance `[get, set]` |
|  | 旋转角度容忍，范围：[0,90] 更多... |
|  | |
| LineFitFunEnum | LineFitFun `[get, set]` |
|  | 拟合方式 更多... |
|  | |
| SortTypeEnum | SortType `[get, set]` |
|  | 排序类型 更多... |
|  | |
| int | EdgesNumMax `[get, set]` |
|  | 边缘点数限制最大值，范围：[1,9999999] 更多... |
|  | |
| bool | EdgePointsNumLimitEnable `[get, set]` |
|  | 边缘点数判断 更多... |
|  | |
| int | EdgePointsNumLimitLow `[get, set]` |
|  | 边缘点数范围，范围：[2,99999] 更多... |
|  | |
| int | EdgePointsNumLimitHigh `[get, set]` |
|  | 边缘点数范围，范围：[2,99999] 更多... |
|  | |
| bool | LineNumLimitEnable `[get, set]` |
|  | 直线数量判断 更多... |
|  | |
| int | LineNumLimitLow `[get, set]` |
|  | 直线数量范围，范围：[1,99999] 更多... |
|  | |
| int | LineNumLimitHigh `[get, set]` |
|  | 直线数量范围，范围：[1,99999] 更多... |
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

多直线查找参数

## 成员枚举类型说明

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

直线边缘极性

| 枚举值 | |
| --- | --- |
| DarkToBright | 由黑到白 |
| BrightToDark | 由白到黑 |
| Mixed | 任意(同一条线段中点集有两种极性点) |
| Either | 黑到白或白到黑(同一条线段中点集有一种极性点) |

## ◆ LineFitFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LineFitFunEnum | | strong |

拟合方式

| 枚举值 | |
| --- | --- |
| LS | 最小二乘 |
| Huber | huber |
| Tukey | tukey |

## ◆ SortTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortTypeEnum | | strong |

排序类型

| 枚举值 | |
| --- | --- |
| InGroupPtNumDscend | 得分 |
| RhoAscend | ROI方向排序 |
| RhoDscend | ROI反方向排序 |

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
| |  | | --- | | MultiLineFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ GradientFieldSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GradientFieldSize | | getset |

滤波核半宽，范围：[1,50]

## ◆ ProjectionLength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ProjectionLength | | getset |

投影长度，范围：[3,100]

## ◆ EdgeThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThreshold | | getset |

绝对边缘阈值，范围：[0,255]

## ◆ NormalContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NormalContrast | | getset |

相对边缘阈值，范围：[0,100]

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

直线边缘极性

## ◆ EdgeAngleTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeAngleTolerance | | getset |

边缘角度容忍，范围：[0,90]

## ◆ EdgeDistTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeDistTolerance | | getset |

边缘距离容忍，范围：[0,100]

## ◆ LineMaxNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineMaxNum | | getset |

多线最大条数，范围：[1,1000]

## ◆ LineCoverage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineCoverage | | getset |

覆盖率阈值，范围：[0,100]

## ◆ LineRotationTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineRotationTolerance | | getset |

旋转角度容忍，范围：[0,90]

## ◆ LineFitFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | LineFitFunEnum LineFitFun | | getset |

拟合方式

## ◆ SortType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortTypeEnum SortType | | getset |

排序类型

## ◆ EdgesNumMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgesNumMax | | getset |

边缘点数限制最大值，范围：[1,9999999]

## ◆ EdgePointsNumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgePointsNumLimitEnable | | getset |

边缘点数判断

## ◆ EdgePointsNumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointsNumLimitLow | | getset |

边缘点数范围，范围：[2,99999]

## ◆ EdgePointsNumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePointsNumLimitHigh | | getset |

边缘点数范围，范围：[2,99999]

## ◆ LineNumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LineNumLimitEnable | | getset |

直线数量判断

## ◆ LineNumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineNumLimitLow | | getset |

直线数量范围，范围：[1,99999]

## ◆ LineNumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineNumLimitHigh | | getset |

直线数量范围，范围：[1,99999]
