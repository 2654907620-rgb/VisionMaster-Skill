<!-- src:class_i_m_v_s_edge_width_find_modu_cs_1_1_edge_width_find_param.html -->
<!-- path:接口函数 > 测量 > 间距检测 > EdgeWidthFindParam -->
# EdgeWidthFindParam类 参考 测量 » 间距检测

间距检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | Edge0PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘0极性 更多... |
|  | |
| enum | Edge1PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘1极性 更多... |
|  | |
| enum | SortTypeEnum {     ScoreDescend = 0x0,     ScoreAscend = 0x1,     OrientForward = 0x2,     OrientBackward = 0x3   } |
|  | 排序方式 更多... |
|  | |
| enum | FindModeEnum {     Widest = 0x1,     Narrowest = 0x2,     Strongest = 0x3,     Worst = 0x4,     First = 0x5,     Last = 0x6,     Nearest = 0x7,     Farthest = 0x8,     All = 0x9   } |
|  | 边缘对类型 更多... |
|  | |
| enum | FindOrientEnum {     UpToDown = 0x1,     LeftToRight = 0x2   } |
|  | 查找方向 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| EdgeWidthFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | ContrastTH `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| Edge0PolarityEnum | Edge0Polarity `[get, set]` |
|  | 边缘0极性 更多... |
|  | |
| Edge1PolarityEnum | Edge1Polarity `[get, set]` |
|  | 边缘1极性 更多... |
|  | |
| int | Maximum `[get, set]` |
|  | 最大结果数，范围：[1,1000] 更多... |
|  | |
| SortTypeEnum | SortType `[get, set]` |
|  | 排序方式 更多... |
|  | |
| FindModeEnum | FindMode `[get, set]` |
|  | 边缘对类型 更多... |
|  | |
| int | IdeaWidth `[get, set]` |
|  | 理想间距，范围：[1,10000] 更多... |
|  | |
| FindOrientEnum | FindOrient `[get, set]` |
|  | 查找方向 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小边缘分数，范围：[0,1.0] 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 数量判断，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 数量判断，范围：[0,99999] 更多... |
|  | |
| bool | EdgeWidthLimitEnable `[get, set]` |
|  | 宽度判断 更多... |
|  | |
| double | EdgeWidthLimitLow `[get, set]` |
|  | 宽度判断，范围：[0.1,99999] 更多... |
|  | |
| double | EdgeWidthLimitHigh `[get, set]` |
|  | 宽度判断，范围：[0.1,99999] 更多... |
|  | |
| bool | Edge0PointXLimitEnable `[get, set]` |
|  | 边缘点0X判断 更多... |
|  | |
| double | Edge0PointXLimitLow `[get, set]` |
|  | 边缘点0X范围，范围：[0,99999] 更多... |
|  | |
| double | Edge0PointXLimitHigh `[get, set]` |
|  | 边缘点0X范围，范围：[0,99999] 更多... |
|  | |
| bool | Edge0PointYLimitEnable `[get, set]` |
|  | 边缘点0Y判断 更多... |
|  | |
| double | Edge0PointYLimitLow `[get, set]` |
|  | 边缘点0Y范围，范围：[0,99999] 更多... |
|  | |
| double | Edge0PointYLimitHigh `[get, set]` |
|  | 边缘点0Y范围，范围：[0,99999] 更多... |
|  | |
| bool | Edge1PointXLimitEnable `[get, set]` |
|  | 边缘点1X判断 更多... |
|  | |
| double | Edge1PointXLimitLow `[get, set]` |
|  | 边缘点1X范围，范围：[0,99999] 更多... |
|  | |
| double | Edge1PointXLimitHigh `[get, set]` |
|  | 边缘点1X范围，范围：[0,99999] 更多... |
|  | |
| bool | Edge1PointYLimitEnable `[get, set]` |
|  | 边缘点1Y判断 更多... |
|  | |
| double | Edge1PointYLimitLow `[get, set]` |
|  | 边缘点1Y范围，范围：[0,99999] 更多... |
|  | |
| double | Edge1PointYLimitHigh `[get, set]` |
|  | 边缘点1Y范围，范围：[0,99999] 更多... |
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

间距检测参数

## 成员枚举类型说明

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

## ◆ SortTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortTypeEnum | | strong |

排序方式

| 枚举值 | |
| --- | --- |
| ScoreDescend | 分数降序 |
| ScoreAscend | 分数升序 |
| OrientForward | 方向正向 |
| OrientBackward | 方向逆向 |

## ◆ FindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindModeEnum | | strong |

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
| All | 全部 |

## ◆ FindOrientEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindOrientEnum | | strong |

查找方向

| 枚举值 | |
| --- | --- |
| UpToDown | 纵向投影或径向投影 |
| LeftToRight | 横向投影或环向投影 |

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
| |  | | --- | | EdgeWidthFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ HalfKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalfKernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ ContrastTH

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastTH | | getset |

边缘阈值，范围：[0,255]

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

## ◆ Maximum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Maximum | | getset |

最大结果数，范围：[1,1000]

## ◆ SortType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortTypeEnum SortType | | getset |

排序方式

## ◆ FindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindModeEnum FindMode | | getset |

边缘对类型

## ◆ IdeaWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int IdeaWidth | | getset |

理想间距，范围：[1,10000]

## ◆ FindOrient

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindOrientEnum FindOrient | | getset |

查找方向

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小边缘分数，范围：[0,1.0]

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

数量判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

数量判断，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

数量判断，范围：[0,99999]

## ◆ EdgeWidthLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgeWidthLimitEnable | | getset |

宽度判断

## ◆ EdgeWidthLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgeWidthLimitLow | | getset |

宽度判断，范围：[0.1,99999]

## ◆ EdgeWidthLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgeWidthLimitHigh | | getset |

宽度判断，范围：[0.1,99999]

## ◆ Edge0PointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge0PointXLimitEnable | | getset |

边缘点0X判断

## ◆ Edge0PointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointXLimitLow | | getset |

边缘点0X范围，范围：[0,99999]

## ◆ Edge0PointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointXLimitHigh | | getset |

边缘点0X范围，范围：[0,99999]

## ◆ Edge0PointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge0PointYLimitEnable | | getset |

边缘点0Y判断

## ◆ Edge0PointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointYLimitLow | | getset |

边缘点0Y范围，范围：[0,99999]

## ◆ Edge0PointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointYLimitHigh | | getset |

边缘点0Y范围，范围：[0,99999]

## ◆ Edge1PointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge1PointXLimitEnable | | getset |

边缘点1X判断

## ◆ Edge1PointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointXLimitLow | | getset |

边缘点1X范围，范围：[0,99999]

## ◆ Edge1PointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointXLimitHigh | | getset |

边缘点1X范围，范围：[0,99999]

## ◆ Edge1PointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge1PointYLimitEnable | | getset |

边缘点1Y判断

## ◆ Edge1PointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointYLimitLow | | getset |

边缘点1Y范围，范围：[0,99999]

## ◆ Edge1PointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointYLimitHigh | | getset |

边缘点1Y范围，范围：[0,99999]
