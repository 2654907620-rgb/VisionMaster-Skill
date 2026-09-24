<!-- src:class_i_m_v_s_caliper_modu_cs_1_1_caliper_param.html -->
<!-- path:接口函数 > 定位 > 卡尺工具 > CaliperParam -->
# CaliperParam类 参考 定位 » 卡尺工具

卡尺工具参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgeModeEnum {     SINGLE\_EDGE = 0x1,     EDGE\_PAIR = 0x2   } |
|  | 边缘模式 更多... |
|  | |
| enum | EdgePolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘0极性 更多... |
|  | |
| enum | Edge1PolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘1极性 更多... |
|  | |
| enum | SortTypeEnum {     ScoreDescend = 0x0,     ScoreAscend = 0x1,     OrientForward = 0x2,     OrientBackward = 0x3   } |
|  | 排序方式 更多... |
|  | |
| enum | ContrastDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型1 更多... |
|  | |
| enum | GrayscaleDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型2 更多... |
|  | |
| enum | PositionDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型3 更多... |
|  | |
| enum | PositionNegDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型4 更多... |
|  | |
| enum | PositionNormDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型 更多... |
|  | |
| enum | PositionNormNegDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型 更多... |
|  | |
| enum | SizeNormDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型 更多... |
|  | |
| enum | SizeDiffNormDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 曲线类型 更多... |
|  | |
| enum | SizeDiffNormAsymDropEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 左曲线类型 更多... |
|  | |
| enum | SizeDiffNormAsymDropHEnum {     Rise = 0x0,     Drop = 0x1   } |
|  | 右曲线类型 更多... |
|  | |
| enum | ProjectionTypeEnum {     ProjectionToHeight = 0x0,     ProjectionToWidth = 0x1   } |
|  | 投影方向 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CaliperRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| EdgeModeEnum | EdgeMode `[get, set]` |
|  | 边缘模式 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | ContrastTH `[get, set]` |
|  | 边缘阈值，范围：[0,255] 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘0极性 更多... |
|  | |
| Edge1PolarityEnum | Edge1Polarity `[get, set]` |
|  | 边缘1极性 更多... |
|  | |
| int | EdgePairWidth `[get, set]` |
|  | 边缘对宽度，范围：[1,10000] 更多... |
|  | |
| int | Maximum `[get, set]` |
|  | 最大结果数，范围：[1,1000] 更多... |
|  | |
| SortTypeEnum | SortType `[get, set]` |
|  | 排序方式 更多... |
|  | |
| bool | ContrastEnable `[get, set]` |
|  | 对比度 更多... |
|  | |
| bool | ContrastPairEnable `[get, set]` |
|  | 边缘对对比度 更多... |
|  | |
| ContrastDropEnum | ContrastDrop `[get, set]` |
|  | 曲线类型1 更多... |
|  | |
| int | ContrastX0 `[get, set]` |
|  | 起点，范围：[-100000,100000] 更多... |
|  | |
| int | ContrastX1 `[get, set]` |
|  | X中点，范围：[-100000,100000] 更多... |
|  | |
| int | ContrastXC `[get, set]` |
|  | 终点，范围：[-100000,100000] 更多... |
|  | |
| int | ContrastY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | ContrastY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | GrayscaleEnable `[get, set]` |
|  | 灰度 更多... |
|  | |
| GrayscaleDropEnum | GrayscaleDrop `[get, set]` |
|  | 曲线类型2 更多... |
|  | |
| int | GrayscaleX0 `[get, set]` |
|  | 起点，范围：[-100000,100000] 更多... |
|  | |
| int | GrayscaleX1 `[get, set]` |
|  | X中点，范围：[-100000,100000] 更多... |
|  | |
| int | GrayscaleXC `[get, set]` |
|  | 终点，范围：[-100000,100000] 更多... |
|  | |
| int | GrayscaleY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | GrayscaleY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | PositionEnable `[get, set]` |
|  | 位置 更多... |
|  | |
| PositionDropEnum | PositionDrop `[get, set]` |
|  | 曲线类型3 更多... |
|  | |
| int | PositionX0 `[get, set]` |
|  | 起点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionX1 `[get, set]` |
|  | X中点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionXC `[get, set]` |
|  | 终点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | PositionY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | PositionNegEnable `[get, set]` |
|  | 相对位置 更多... |
|  | |
| PositionNegDropEnum | PositionNegDrop `[get, set]` |
|  | 曲线类型4 更多... |
|  | |
| int | PositionNegX0 `[get, set]` |
|  | 起点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionNegX1 `[get, set]` |
|  | X中点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionNegXC `[get, set]` |
|  | 终点，范围：[-100000,100000] 更多... |
|  | |
| int | PositionNegY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | PositionNegY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | PositionNormEnable `[get, set]` |
|  | 归一位置 更多... |
|  | |
| PositionNormDropEnum | PositionNormDrop `[get, set]` |
|  | 曲线类型 更多... |
|  | |
| int | PositionNormX0 `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormX1 `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormXC `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | PositionNormY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | PositionNormNegEnable `[get, set]` |
|  | 归一相对位置 更多... |
|  | |
| PositionNormNegDropEnum | PositionNormNegDrop `[get, set]` |
|  | 曲线类型 更多... |
|  | |
| int | PositionNormNegX0 `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormNegX1 `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormNegXC `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | PositionNormNegY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | PositionNormNegY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | SizeNormEnable `[get, set]` |
|  | 间距 更多... |
|  | |
| SizeNormDropEnum | SizeNormDrop `[get, set]` |
|  | 曲线类型 更多... |
|  | |
| int | SizeNormX0 `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeNormX1 `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeNormXC `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeNormY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | SizeNormY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | SizeDiffNormEnable `[get, set]` |
|  | 间距差 更多... |
|  | |
| SizeDiffNormDropEnum | SizeDiffNormDrop `[get, set]` |
|  | 曲线类型 更多... |
|  | |
| int | SizeDiffNormX0 `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormX1 `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormXC `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | SizeDiffNormY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| bool | SizeDiffNormAsymEnable `[get, set]` |
|  | 相对间距差 更多... |
|  | |
| SizeDiffNormAsymDropEnum | SizeDiffNormAsymDrop `[get, set]` |
|  | 左曲线类型 更多... |
|  | |
| int | SizeDiffNormAsymX0 `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymX1 `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymXC `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymY0 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | SizeDiffNormAsymY1 `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| SizeDiffNormAsymDropHEnum | SizeDiffNormAsymDropH `[get, set]` |
|  | 右曲线类型 更多... |
|  | |
| int | SizeDiffNormAsymX0H `[get, set]` |
|  | 起点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymX1H `[get, set]` |
|  | X中点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymXCH `[get, set]` |
|  | 终点，范围：[-10000,10000] 更多... |
|  | |
| int | SizeDiffNormAsymY0H `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| int | SizeDiffNormAsymY1H `[get, set]` |
|  | Y计分，范围：[0,100] 更多... |
|  | |
| ProjectionTypeEnum | ProjectionType `[get, set]` |
|  | 投影方向 更多... |
|  | |
| bool | FuzzyedgeFlag `[get, set]` |
|  | 模糊边缘 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 数量判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 数量范围，范围：[0,99999] 更多... |
|  | |
| bool | EdgeWidthLimitEnable `[get, set]` |
|  | 宽度判断 更多... |
|  | |
| double | EdgeWidthLimitLow `[get, set]` |
|  | 宽度范围，范围：[0,99999] 更多... |
|  | |
| double | EdgeWidthLimitHigh `[get, set]` |
|  | 宽度范围，范围：[0,99999] 更多... |
|  | |
| bool | Edge0PointXLimitEnable `[get, set]` |
|  | 边缘点0X判断 更多... |
|  | |
| double | Edge0PointXLimitLow `[get, set]` |
|  | 边缘点0X范围，范围：[-99999,99999] 更多... |
|  | |
| double | Edge0PointXLimitHigh `[get, set]` |
|  | 边缘点0X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | Edge0PointYLimitEnable `[get, set]` |
|  | 边缘点0Y判断 更多... |
|  | |
| double | Edge0PointYLimitLow `[get, set]` |
|  | 边缘点0Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | Edge0PointYLimitHigh `[get, set]` |
|  | 边缘点0Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | Edge1PointXLimitEnable `[get, set]` |
|  | 边缘点1X判断 更多... |
|  | |
| double | Edge1PointXLimitLow `[get, set]` |
|  | 边缘点1X范围，范围：[-99999,99999] 更多... |
|  | |
| double | Edge1PointXLimitHigh `[get, set]` |
|  | 边缘点1X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | Edge1PointYLimitEnable `[get, set]` |
|  | 边缘点1Y判断 更多... |
|  | |
| double | Edge1PointYLimitLow `[get, set]` |
|  | 边缘点1Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | Edge1PointYLimitHigh `[get, set]` |
|  | 边缘点1Y范围，范围：[-99999,99999] 更多... |
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

卡尺工具参数

## 成员枚举类型说明

## ◆ EdgeModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeModeEnum | | strong |

边缘模式

| 枚举值 | |
| --- | --- |
| SINGLE\_EDGE | 单边缘 |
| EDGE\_PAIR | 边缘对 |

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

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

## ◆ ContrastDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ContrastDropEnum | | strong |

曲线类型1

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ GrayscaleDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum GrayscaleDropEnum | | strong |

曲线类型2

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ PositionDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PositionDropEnum | | strong |

曲线类型3

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ PositionNegDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PositionNegDropEnum | | strong |

曲线类型4

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ PositionNormDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PositionNormDropEnum | | strong |

曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ PositionNormNegDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PositionNormNegDropEnum | | strong |

曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ SizeNormDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SizeNormDropEnum | | strong |

曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ SizeDiffNormDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SizeDiffNormDropEnum | | strong |

曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ SizeDiffNormAsymDropEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SizeDiffNormAsymDropEnum | | strong |

左曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ SizeDiffNormAsymDropHEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SizeDiffNormAsymDropHEnum | | strong |

右曲线类型

| 枚举值 | |
| --- | --- |
| Rise | 递增 |
| Drop | 递减 |

## ◆ ProjectionTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ProjectionTypeEnum | | strong |

投影方向

| 枚举值 | |
| --- | --- |
| ProjectionToHeight | 从左到右 |
| ProjectionToWidth | 从上到下 |

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
| |  | | --- | | CaliperRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ EdgeMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeModeEnum EdgeMode | | getset |

边缘模式

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

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘0极性

## ◆ Edge1Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Edge1PolarityEnum Edge1Polarity | | getset |

边缘1极性

## ◆ EdgePairWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgePairWidth | | getset |

边缘对宽度，范围：[1,10000]

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

## ◆ ContrastEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ContrastEnable | | getset |

对比度

## ◆ ContrastPairEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ContrastPairEnable | | getset |

边缘对对比度

## ◆ ContrastDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ContrastDropEnum ContrastDrop | | getset |

曲线类型1

## ◆ ContrastX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastX0 | | getset |

起点，范围：[-100000,100000]

## ◆ ContrastX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastX1 | | getset |

X中点，范围：[-100000,100000]

## ◆ ContrastXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastXC | | getset |

终点，范围：[-100000,100000]

## ◆ ContrastY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastY0 | | getset |

Y计分，范围：[0,100]

## ◆ ContrastY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContrastY1 | | getset |

Y计分，范围：[0,100]

## ◆ GrayscaleEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayscaleEnable | | getset |

灰度

## ◆ GrayscaleDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | GrayscaleDropEnum GrayscaleDrop | | getset |

曲线类型2

## ◆ GrayscaleX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayscaleX0 | | getset |

起点，范围：[-100000,100000]

## ◆ GrayscaleX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayscaleX1 | | getset |

X中点，范围：[-100000,100000]

## ◆ GrayscaleXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayscaleXC | | getset |

终点，范围：[-100000,100000]

## ◆ GrayscaleY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayscaleY0 | | getset |

Y计分，范围：[0,100]

## ◆ GrayscaleY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayscaleY1 | | getset |

Y计分，范围：[0,100]

## ◆ PositionEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PositionEnable | | getset |

位置

## ◆ PositionDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PositionDropEnum PositionDrop | | getset |

曲线类型3

## ◆ PositionX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionX0 | | getset |

起点，范围：[-100000,100000]

## ◆ PositionX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionX1 | | getset |

X中点，范围：[-100000,100000]

## ◆ PositionXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionXC | | getset |

终点，范围：[-100000,100000]

## ◆ PositionY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionY0 | | getset |

Y计分，范围：[0,100]

## ◆ PositionY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionY1 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNegEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PositionNegEnable | | getset |

相对位置

## ◆ PositionNegDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PositionNegDropEnum PositionNegDrop | | getset |

曲线类型4

## ◆ PositionNegX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNegX0 | | getset |

起点，范围：[-100000,100000]

## ◆ PositionNegX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNegX1 | | getset |

X中点，范围：[-100000,100000]

## ◆ PositionNegXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNegXC | | getset |

终点，范围：[-100000,100000]

## ◆ PositionNegY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNegY0 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNegY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNegY1 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNormEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PositionNormEnable | | getset |

归一位置

## ◆ PositionNormDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PositionNormDropEnum PositionNormDrop | | getset |

曲线类型

## ◆ PositionNormX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormX0 | | getset |

起点，范围：[-10000,10000]

## ◆ PositionNormX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormX1 | | getset |

X中点，范围：[-10000,10000]

## ◆ PositionNormXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormXC | | getset |

终点，范围：[-10000,10000]

## ◆ PositionNormY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormY0 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNormY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormY1 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNormNegEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PositionNormNegEnable | | getset |

归一相对位置

## ◆ PositionNormNegDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PositionNormNegDropEnum PositionNormNegDrop | | getset |

曲线类型

## ◆ PositionNormNegX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormNegX0 | | getset |

起点，范围：[-10000,10000]

## ◆ PositionNormNegX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormNegX1 | | getset |

X中点，范围：[-10000,10000]

## ◆ PositionNormNegXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormNegXC | | getset |

终点，范围：[-10000,10000]

## ◆ PositionNormNegY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormNegY0 | | getset |

Y计分，范围：[0,100]

## ◆ PositionNormNegY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PositionNormNegY1 | | getset |

Y计分，范围：[0,100]

## ◆ SizeNormEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SizeNormEnable | | getset |

间距

## ◆ SizeNormDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SizeNormDropEnum SizeNormDrop | | getset |

曲线类型

## ◆ SizeNormX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeNormX0 | | getset |

起点，范围：[-10000,10000]

## ◆ SizeNormX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeNormX1 | | getset |

X中点，范围：[-10000,10000]

## ◆ SizeNormXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeNormXC | | getset |

终点，范围：[-10000,10000]

## ◆ SizeNormY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeNormY0 | | getset |

Y计分，范围：[0,100]

## ◆ SizeNormY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeNormY1 | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SizeDiffNormEnable | | getset |

间距差

## ◆ SizeDiffNormDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SizeDiffNormDropEnum SizeDiffNormDrop | | getset |

曲线类型

## ◆ SizeDiffNormX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormX0 | | getset |

起点，范围：[-10000,10000]

## ◆ SizeDiffNormX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormX1 | | getset |

X中点，范围：[-10000,10000]

## ◆ SizeDiffNormXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormXC | | getset |

终点，范围：[-10000,10000]

## ◆ SizeDiffNormY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormY0 | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormY1 | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormAsymEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SizeDiffNormAsymEnable | | getset |

相对间距差

## ◆ SizeDiffNormAsymDrop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SizeDiffNormAsymDropEnum SizeDiffNormAsymDrop | | getset |

左曲线类型

## ◆ SizeDiffNormAsymX0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymX0 | | getset |

起点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymX1 | | getset |

X中点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymXC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymXC | | getset |

终点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymY0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymY0 | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormAsymY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymY1 | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormAsymDropH

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SizeDiffNormAsymDropHEnum SizeDiffNormAsymDropH | | getset |

右曲线类型

## ◆ SizeDiffNormAsymX0H

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymX0H | | getset |

起点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymX1H

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymX1H | | getset |

X中点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymXCH

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymXCH | | getset |

终点，范围：[-10000,10000]

## ◆ SizeDiffNormAsymY0H

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymY0H | | getset |

Y计分，范围：[0,100]

## ◆ SizeDiffNormAsymY1H

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SizeDiffNormAsymY1H | | getset |

Y计分，范围：[0,100]

## ◆ ProjectionType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ProjectionTypeEnum ProjectionType | | getset |

投影方向

## ◆ FuzzyedgeFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FuzzyedgeFlag | | getset |

模糊边缘

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

数量判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

数量范围，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

数量范围，范围：[0,99999]

## ◆ EdgeWidthLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgeWidthLimitEnable | | getset |

宽度判断

## ◆ EdgeWidthLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgeWidthLimitLow | | getset |

宽度范围，范围：[0,99999]

## ◆ EdgeWidthLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double EdgeWidthLimitHigh | | getset |

宽度范围，范围：[0,99999]

## ◆ Edge0PointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge0PointXLimitEnable | | getset |

边缘点0X判断

## ◆ Edge0PointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointXLimitLow | | getset |

边缘点0X范围，范围：[-99999,99999]

## ◆ Edge0PointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointXLimitHigh | | getset |

边缘点0X范围，范围：[-99999,99999]

## ◆ Edge0PointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge0PointYLimitEnable | | getset |

边缘点0Y判断

## ◆ Edge0PointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointYLimitLow | | getset |

边缘点0Y范围，范围：[-99999,99999]

## ◆ Edge0PointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge0PointYLimitHigh | | getset |

边缘点0Y范围，范围：[-99999,99999]

## ◆ Edge1PointXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge1PointXLimitEnable | | getset |

边缘点1X判断

## ◆ Edge1PointXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointXLimitLow | | getset |

边缘点1X范围，范围：[-99999,99999]

## ◆ Edge1PointXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointXLimitHigh | | getset |

边缘点1X范围，范围：[-99999,99999]

## ◆ Edge1PointYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Edge1PointYLimitEnable | | getset |

边缘点1Y判断

## ◆ Edge1PointYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointYLimitLow | | getset |

边缘点1Y范围，范围：[-99999,99999]

## ◆ Edge1PointYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double Edge1PointYLimitHigh | | getset |

边缘点1Y范围，范围：[-99999,99999]
