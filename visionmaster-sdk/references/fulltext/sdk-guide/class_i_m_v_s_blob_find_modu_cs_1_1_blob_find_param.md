<!-- src:class_i_m_v_s_blob_find_modu_cs_1_1_blob_find_param.html -->
<!-- path:接口函数 > 定位 > Blob分析 > BlobFindParam -->
# BlobFindParam类 参考 定位 » Blob分析

Blob分析参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ThresholdTypeEnum {     BinaryImage = 0x1,     SingleThreshold = 2,     DoubleThreshold = 3,     AutoThreshold = 4,     FixedSoftThreshold = 5,     RelativeSoftThreshold = 6   } |
|  | 阈值方式 更多... |
|  | |
| enum | PolarityEnum {     DarkOnBright = 0,     BrightOnDark = 1   } |
|  | 极性 更多... |
|  | |
| enum | BlobContourTypeEnum {     NoneContour = 0,     NoneSequentialContour = 1,     SequentialContour = 2   } |
|  | 输出轮廓类型 更多... |
|  | |
| enum | SortFeatureEnum {     SortFeatureArea = 0x1,     SortFeaturePerimeter = 0x2,     SortFeatureCircularity = 0x3,     SortFeatureRect = 0x4,     SortFeatureCentroidX = 0x5,     SortFeatureCentroidY = 0x6,     SortFeatureBoxAngle = 0x7,     SortFeatureBoxWidth = 0x8,     SortFeatureBoxHeight = 0x9,     SortFeatureRectX = 0xA,     SortFeatureRectY = 0xB,     SortFeatureAxisAngle = 0xC,     SortFeatureAxisRatio = 0xD   } |
|  | 排序特征 更多... |
|  | |
| enum | SortModeEnum {     SortModeAscend = 0x1,     SortModeDecend = 0x2,     SortModeNotSort = 0x3   } |
|  | 排序方式 更多... |
|  | |
| enum | ConnectivityEnum {     Connected\_8 = 0x8,     Connected\_4 = 0x4   } |
|  | 连通性 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| BlobFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| ThresholdTypeEnum | ThresholdType `[get, set]` |
|  | 阈值方式 更多... |
|  | |
| PolarityEnum | Polarity `[get, set]` |
|  | 极性 更多... |
|  | |
| int | LowThreshold `[get, set]` |
|  | 低阈值，范围：[0,255] 更多... |
|  | |
| int | HightThreshold `[get, set]` |
|  | 高阈值，范围：[0,255] 更多... |
|  | |
| int | LowSoftThreshold `[get, set]` |
|  | 阈值范围，范围：[0,255] 更多... |
|  | |
| int | HightSoftThreshold `[get, set]` |
|  | 阈值范围，范围：[0,255] 更多... |
|  | |
| int | Softness `[get, set]` |
|  | 软阈值柔和度，范围：[0,254] 更多... |
|  | |
| int | SoftLeftRatio `[get, set]` |
|  | 低尾部比例，范围：[0,100] 更多... |
|  | |
| int | SoftRightRatio `[get, set]` |
|  | 高尾部比例，范围：[0,100] 更多... |
|  | |
| int | SoftLowRatio `[get, set]` |
|  | 低阈值比例，范围：[0,100] 更多... |
|  | |
| int | SoftHighRatio `[get, set]` |
|  | 高阈值比例，范围：[0,100] 更多... |
|  | |
| int | FindNum `[get, set]` |
|  | 查找个数，范围：[1,20000] 更多... |
|  | |
| int | HoleMinArea `[get, set]` |
|  | 填充面积阈值，范围：[0,999999999] 更多... |
|  | |
| bool | SelectByArea `[get, set]` |
|  | 面积使能 更多... |
|  | |
| int | MinArea `[get, set]` |
|  | 面积范围，范围：[1,999999999] 更多... |
|  | |
| int | MaxArea `[get, set]` |
|  | 面积范围，范围：[1,999999999] 更多... |
|  | |
| BlobContourTypeEnum | BlobContourType `[get, set]` |
|  | 输出轮廓类型 更多... |
|  | |
| bool | BolbImageEnable `[get, set]` |
|  | Blob图像输出 更多... |
|  | |
| bool | BinaryImageEnable `[get, set]` |
|  | 二值化图输出 更多... |
|  | |
| bool | SelectByHistInfo `[get, set]` |
|  | 直方图信息输出 更多... |
|  | |
| bool | SelectByBoxAngle `[get, set]` |
|  | 角度使能 更多... |
|  | |
| int | MinBoxAngle `[get, set]` |
|  | 角度范围，范围：[-9000,9000] 更多... |
|  | |
| int | MaxBoxAngle `[get, set]` |
|  | 角度范围，范围：[-9000,9000] 更多... |
|  | |
| bool | SelectByRectWidth `[get, set]` |
|  | RECT宽使能 更多... |
|  | |
| int | MinRectWidth `[get, set]` |
|  | RECT宽范围，范围：[1,1000000] 更多... |
|  | |
| int | MaxRectWidth `[get, set]` |
|  | RECT宽范围，范围：[1,1000000] 更多... |
|  | |
| bool | SelectByRectHeight `[get, set]` |
|  | RECT高使能 更多... |
|  | |
| int | MinRectHeight `[get, set]` |
|  | RECT高范围，范围：[1,1000000] 更多... |
|  | |
| int | MaxRectHeight `[get, set]` |
|  | RECT高范围，范围：[1,1000000] 更多... |
|  | |
| bool | SelectByPerimeter `[get, set]` |
|  | 周长使能 更多... |
|  | |
| int | MinPerimeter `[get, set]` |
|  | 周长范围，范围：[1,999999999] 更多... |
|  | |
| int | MaxPerimeter `[get, set]` |
|  | 周长范围，范围：[1,999999999] 更多... |
|  | |
| bool | SelectByShortAxis `[get, set]` |
|  | 短轴使能 更多... |
|  | |
| int | MinShortAxis `[get, set]` |
|  | 短轴范围，范围：[1,999999999] 更多... |
|  | |
| int | MaxShortAxis `[get, set]` |
|  | 短轴范围，范围：[1,999999999] 更多... |
|  | |
| bool | SelectByLongAxis `[get, set]` |
|  | 长轴使能 更多... |
|  | |
| int | MinLongAxis `[get, set]` |
|  | 长轴范围，范围：[1,999999999] 更多... |
|  | |
| int | MaxLongAxis `[get, set]` |
|  | 长轴范围，范围：[1,999999999] 更多... |
|  | |
| bool | SelectByCircularuty `[get, set]` |
|  | 圆形度使能 更多... |
|  | |
| double | MinCircularity `[get, set]` |
|  | 圆形度范围，范围：[0,1] 更多... |
|  | |
| double | MaxCircularity `[get, set]` |
|  | 圆形度范围，范围：[0,1] 更多... |
|  | |
| bool | SelectByRectangularity `[get, set]` |
|  | 矩形度使能 更多... |
|  | |
| double | MinRectangularity `[get, set]` |
|  | 矩形度范围，范围：[0,1] 更多... |
|  | |
| double | MaxRectangularity `[get, set]` |
|  | 矩形度范围，范围：[0,1] 更多... |
|  | |
| bool | SelectByCentraBias `[get, set]` |
|  | 质心偏移使能 更多... |
|  | |
| double | MinCenterBias `[get, set]` |
|  | 质心偏移范围，范围：[0,9999999.99] 更多... |
|  | |
| double | MaxCenterBias `[get, set]` |
|  | 质心偏移范围，范围：[0,9999999.99] 更多... |
|  | |
| bool | AxisRatioEnable `[get, set]` |
|  | 轴比范围 更多... |
|  | |
| double | MinAxisRatio `[get, set]` |
|  | 轴比范围，范围：[0.01,1] 更多... |
|  | |
| double | MaxAxisRatio `[get, set]` |
|  | 轴比范围，范围：[0.01,1] 更多... |
|  | |
| SortFeatureEnum | SortFeature `[get, set]` |
|  | 排序特征 更多... |
|  | |
| SortModeEnum | SortMode `[get, set]` |
|  | 排序方式 更多... |
|  | |
| ConnectivityEnum | Connectivity `[get, set]` |
|  | 连通性 更多... |
|  | |
| int | MaxAreaInnerRectNum `[get, set]` |
|  | 最大内接矩形输出数量，范围：[0,10] 更多... |
|  | |
| int | OverlapRatio `[get, set]` |
|  | 最小重叠率，范围：[0,100] 更多... |
|  | |
| bool | MaxOutPixelNumEnable `[get, set]` |
|  | 像素超界使能 更多... |
|  | |
| int | MaxOutPixelNum `[get, set]` |
|  | 最大超界像素，范围：[0,9000000] 更多... |
|  | |
| bool | OKWhenNumIsZero `[get, set]` |
|  | Blob个数为0 更多... |
|  | |
| bool | BlobNumLimitEnable `[get, set]` |
|  | Blob个数判断 更多... |
|  | |
| int | BlobNumLimitLow `[get, set]` |
|  | Blob个数范围，范围：[0,99999] 更多... |
|  | |
| int | BlobNumLimitHigh `[get, set]` |
|  | Blob个数范围，范围：[0,99999] 更多... |
|  | |
| bool | BlobAreaLimitEnable `[get, set]` |
|  | Blob面积判断 更多... |
|  | |
| double | BlobAreaLimitLow `[get, set]` |
|  | Blob面积范围，范围：[1,999999999] 更多... |
|  | |
| double | BlobAreaLimitHigh `[get, set]` |
|  | Blob面积范围，范围：[1,999999999] 更多... |
|  | |
| bool | BlobTotalAreaLimitEnable `[get, set]` |
|  | Blob总面积 更多... |
|  | |
| double | BlobTotalAreaLimitLow `[get, set]` |
|  | 总面积范围，范围：[1,999999999] 更多... |
|  | |
| double | BlobTotalAreaLimitHigh `[get, set]` |
|  | 总面积范围，范围：[1,999999999] 更多... |
|  | |
| bool | CentroidXLimitEnable `[get, set]` |
|  | 质心X判断 更多... |
|  | |
| double | CentroidXLimitLow `[get, set]` |
|  | 质心X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CentroidXLimitHigh `[get, set]` |
|  | 质心X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CentroidYLimitEnable `[get, set]` |
|  | 质心Y判断 更多... |
|  | |
| double | CentroidYLimitLow `[get, set]` |
|  | 质心Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CentroidYLimitHigh `[get, set]` |
|  | 质心Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | AngleLimitEnable `[get, set]` |
|  | Box角度判断 更多... |
|  | |
| double | AngleLimitLow `[get, set]` |
|  | Box角度范围，范围：[-180,180] 更多... |
|  | |
| double | AngleLimitHigh `[get, set]` |
|  | Box角度范围，范围：[-180,180] 更多... |
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
| bool | BoxHeightLimitEnable `[get, set]` |
|  | Box高度判断 更多... |
|  | |
| double | BoxHeightLimitLow `[get, set]` |
|  | Box高度范围，范围：[1,99999] 更多... |
|  | |
| double | BoxHeightLimitHigh `[get, set]` |
|  | Box高度范围，范围：[1,99999] 更多... |
|  | |
| bool | BoxWidthLimitEnable `[get, set]` |
|  | Box宽度判断 更多... |
|  | |
| double | BoxWidthLimitLow `[get, set]` |
|  | Box宽度范围，范围：[1,99999] 更多... |
|  | |
| double | BoxWidthLimitHigh `[get, set]` |
|  | Box宽度范围，范围：[1,99999] 更多... |
|  | |
| bool | PerimeterLimitEnable `[get, set]` |
|  | 周长判断 更多... |
|  | |
| double | PerimeterLimitLow `[get, set]` |
|  | 周长范围，范围：[1,999999999] 更多... |
|  | |
| double | PerimeterLimitHigh `[get, set]` |
|  | 周长范围，范围：[1,999999999] 更多... |
|  | |
| bool | LongAxisLimitEnable `[get, set]` |
|  | 长轴判断 更多... |
|  | |
| double | LongAxisLimitLow `[get, set]` |
|  | 长轴范围，范围：[1,999999999] 更多... |
|  | |
| double | LongAxisLimitHigh `[get, set]` |
|  | 长轴范围，范围：[1,999999999] 更多... |
|  | |
| bool | ShortAxisLimitEnable `[get, set]` |
|  | 短轴判断 更多... |
|  | |
| double | ShortAxisLimitLow `[get, set]` |
|  | 短轴范围，范围：[1,999999999] 更多... |
|  | |
| double | ShortAxisLimitHigh `[get, set]` |
|  | 短轴范围，范围：[1,999999999] 更多... |
|  | |
| bool | CircularityLimitEnable `[get, set]` |
|  | 圆形度判断 更多... |
|  | |
| double | CircularityLimitLow `[get, set]` |
|  | 圆形度范围，范围：[0,1] 更多... |
|  | |
| double | CircularityLimitHigh `[get, set]` |
|  | 圆形度范围，范围：[0,1] 更多... |
|  | |
| bool | RectangularityLimitEnable `[get, set]` |
|  | 矩形度判断 更多... |
|  | |
| double | RectangularityLimitLow `[get, set]` |
|  | 矩形度范围，范围：[0,1] 更多... |
|  | |
| double | RectangularityLimitHigh `[get, set]` |
|  | 矩形度范围，范围：[0,1] 更多... |
|  | |
| bool | BolbOutLineEnable `[get, set]` |
|  | 轮廓输出使能(废弃) 更多... |
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

Blob分析参数

## 成员枚举类型说明

## ◆ ThresholdTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ThresholdTypeEnum | | strong |

阈值方式

| 枚举值 | |
| --- | --- |
| BinaryImage | 不进行二值化 |
| SingleThreshold | 单阈值 |
| DoubleThreshold | 双阈值 |
| AutoThreshold | 自动阈值 |
| FixedSoftThreshold | 软阈值（固定） |
| RelativeSoftThreshold | 软阈值（相对） |

## ◆ PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PolarityEnum | | strong |

极性

| 枚举值 | |
| --- | --- |
| DarkOnBright | 亮于背景 |
| BrightOnDark | 暗于背景 |

## ◆ BlobContourTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum BlobContourTypeEnum | | strong |

输出轮廓类型

| 枚举值 | |
| --- | --- |
| NoneContour | 不输出轮廓 |
| NoneSequentialContour | 输出无序轮廓 |
| SequentialContour | 输出有序轮廓 |

## ◆ SortFeatureEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortFeatureEnum | | strong |

排序特征

| 枚举值 | |
| --- | --- |
| SortFeatureArea | 面积 |
| SortFeaturePerimeter | 周长 |
| SortFeatureCircularity | 圆形度 |
| SortFeatureRect | 矩形度 |
| SortFeatureCentroidX | 连通域中心x |
| SortFeatureCentroidY | 连通域中心y |
| SortFeatureBoxAngle | box角度 |
| SortFeatureBoxWidth | box宽 |
| SortFeatureBoxHeight | box高 |
| SortFeatureRectX | 矩形左上顶点x |
| SortFeatureRectY | 矩形左上顶点y |
| SortFeatureAxisAngle | 二阶中心距主轴角度 |
| SortFeatureAxisRatio | 轴比(box短轴/box长轴) |

## ◆ SortModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortModeEnum | | strong |

排序方式

| 枚举值 | |
| --- | --- |
| SortModeAscend | 升序 |
| SortModeDecend | 降序 |
| SortModeNotSort | 不排序 |

## ◆ ConnectivityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ConnectivityEnum | | strong |

连通性

| 枚举值 | |
| --- | --- |
| Connected\_8 | 8连通 |
| Connected\_4 | 4连通 |

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
| |  | | --- | | BlobFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ ThresholdType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ThresholdTypeEnum ThresholdType | | getset |

阈值方式

## ◆ Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarityEnum Polarity | | getset |

极性

## ◆ LowThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LowThreshold | | getset |

低阈值，范围：[0,255]

## ◆ HightThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HightThreshold | | getset |

高阈值，范围：[0,255]

## ◆ LowSoftThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LowSoftThreshold | | getset |

阈值范围，范围：[0,255]

## ◆ HightSoftThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HightSoftThreshold | | getset |

阈值范围，范围：[0,255]

## ◆ Softness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Softness | | getset |

软阈值柔和度，范围：[0,254]

## ◆ SoftLeftRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SoftLeftRatio | | getset |

低尾部比例，范围：[0,100]

## ◆ SoftRightRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SoftRightRatio | | getset |

高尾部比例，范围：[0,100]

## ◆ SoftLowRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SoftLowRatio | | getset |

低阈值比例，范围：[0,100]

## ◆ SoftHighRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SoftHighRatio | | getset |

高阈值比例，范围：[0,100]

## ◆ FindNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FindNum | | getset |

查找个数，范围：[1,20000]

## ◆ HoleMinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HoleMinArea | | getset |

填充面积阈值，范围：[0,999999999]

## ◆ SelectByArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByArea | | getset |

面积使能

## ◆ MinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinArea | | getset |

面积范围，范围：[1,999999999]

## ◆ MaxArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxArea | | getset |

面积范围，范围：[1,999999999]

## ◆ BlobContourType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | BlobContourTypeEnum BlobContourType | | getset |

输出轮廓类型

## ◆ BolbImageEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BolbImageEnable | | getset |

Blob图像输出

## ◆ BinaryImageEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BinaryImageEnable | | getset |

二值化图输出

## ◆ SelectByHistInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByHistInfo | | getset |

直方图信息输出

## ◆ SelectByBoxAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByBoxAngle | | getset |

角度使能

## ◆ MinBoxAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinBoxAngle | | getset |

角度范围，范围：[-9000,9000]

## ◆ MaxBoxAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxBoxAngle | | getset |

角度范围，范围：[-9000,9000]

## ◆ SelectByRectWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByRectWidth | | getset |

RECT宽使能

## ◆ MinRectWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinRectWidth | | getset |

RECT宽范围，范围：[1,1000000]

## ◆ MaxRectWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxRectWidth | | getset |

RECT宽范围，范围：[1,1000000]

## ◆ SelectByRectHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByRectHeight | | getset |

RECT高使能

## ◆ MinRectHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinRectHeight | | getset |

RECT高范围，范围：[1,1000000]

## ◆ MaxRectHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxRectHeight | | getset |

RECT高范围，范围：[1,1000000]

## ◆ SelectByPerimeter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByPerimeter | | getset |

周长使能

## ◆ MinPerimeter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinPerimeter | | getset |

周长范围，范围：[1,999999999]

## ◆ MaxPerimeter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxPerimeter | | getset |

周长范围，范围：[1,999999999]

## ◆ SelectByShortAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByShortAxis | | getset |

短轴使能

## ◆ MinShortAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinShortAxis | | getset |

短轴范围，范围：[1,999999999]

## ◆ MaxShortAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxShortAxis | | getset |

短轴范围，范围：[1,999999999]

## ◆ SelectByLongAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByLongAxis | | getset |

长轴使能

## ◆ MinLongAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinLongAxis | | getset |

长轴范围，范围：[1,999999999]

## ◆ MaxLongAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxLongAxis | | getset |

长轴范围，范围：[1,999999999]

## ◆ SelectByCircularuty

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByCircularuty | | getset |

圆形度使能

## ◆ MinCircularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinCircularity | | getset |

圆形度范围，范围：[0,1]

## ◆ MaxCircularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxCircularity | | getset |

圆形度范围，范围：[0,1]

## ◆ SelectByRectangularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByRectangularity | | getset |

矩形度使能

## ◆ MinRectangularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinRectangularity | | getset |

矩形度范围，范围：[0,1]

## ◆ MaxRectangularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxRectangularity | | getset |

矩形度范围，范围：[0,1]

## ◆ SelectByCentraBias

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SelectByCentraBias | | getset |

质心偏移使能

## ◆ MinCenterBias

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinCenterBias | | getset |

质心偏移范围，范围：[0,9999999.99]

## ◆ MaxCenterBias

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxCenterBias | | getset |

质心偏移范围，范围：[0,9999999.99]

## ◆ AxisRatioEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AxisRatioEnable | | getset |

轴比范围

## ◆ MinAxisRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinAxisRatio | | getset |

轴比范围，范围：[0.01,1]

## ◆ MaxAxisRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxAxisRatio | | getset |

轴比范围，范围：[0.01,1]

## ◆ SortFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortFeatureEnum SortFeature | | getset |

排序特征

## ◆ SortMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortModeEnum SortMode | | getset |

排序方式

## ◆ Connectivity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ConnectivityEnum Connectivity | | getset |

连通性

## ◆ MaxAreaInnerRectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxAreaInnerRectNum | | getset |

最大内接矩形输出数量，范围：[0,10]

## ◆ OverlapRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OverlapRatio | | getset |

最小重叠率，范围：[0,100]

## ◆ MaxOutPixelNumEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MaxOutPixelNumEnable | | getset |

像素超界使能

## ◆ MaxOutPixelNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxOutPixelNum | | getset |

最大超界像素，范围：[0,9000000]

## ◆ OKWhenNumIsZero

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OKWhenNumIsZero | | getset |

Blob个数为0

## ◆ BlobNumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BlobNumLimitEnable | | getset |

Blob个数判断

## ◆ BlobNumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlobNumLimitLow | | getset |

Blob个数范围，范围：[0,99999]

## ◆ BlobNumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlobNumLimitHigh | | getset |

Blob个数范围，范围：[0,99999]

## ◆ BlobAreaLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BlobAreaLimitEnable | | getset |

Blob面积判断

## ◆ BlobAreaLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BlobAreaLimitLow | | getset |

Blob面积范围，范围：[1,999999999]

## ◆ BlobAreaLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BlobAreaLimitHigh | | getset |

Blob面积范围，范围：[1,999999999]

## ◆ BlobTotalAreaLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BlobTotalAreaLimitEnable | | getset |

Blob总面积

## ◆ BlobTotalAreaLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BlobTotalAreaLimitLow | | getset |

总面积范围，范围：[1,999999999]

## ◆ BlobTotalAreaLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BlobTotalAreaLimitHigh | | getset |

总面积范围，范围：[1,999999999]

## ◆ CentroidXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CentroidXLimitEnable | | getset |

质心X判断

## ◆ CentroidXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentroidXLimitLow | | getset |

质心X范围，范围：[-99999,99999]

## ◆ CentroidXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentroidXLimitHigh | | getset |

质心X范围，范围：[-99999,99999]

## ◆ CentroidYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CentroidYLimitEnable | | getset |

质心Y判断

## ◆ CentroidYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentroidYLimitLow | | getset |

质心Y范围，范围：[-99999,99999]

## ◆ CentroidYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CentroidYLimitHigh | | getset |

质心Y范围，范围：[-99999,99999]

## ◆ AngleLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleLimitEnable | | getset |

Box角度判断

## ◆ AngleLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitLow | | getset |

Box角度范围，范围：[-180,180]

## ◆ AngleLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double AngleLimitHigh | | getset |

Box角度范围，范围：[-180,180]

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

## ◆ BoxHeightLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BoxHeightLimitEnable | | getset |

Box高度判断

## ◆ BoxHeightLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxHeightLimitLow | | getset |

Box高度范围，范围：[1,99999]

## ◆ BoxHeightLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxHeightLimitHigh | | getset |

Box高度范围，范围：[1,99999]

## ◆ BoxWidthLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BoxWidthLimitEnable | | getset |

Box宽度判断

## ◆ BoxWidthLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxWidthLimitLow | | getset |

Box宽度范围，范围：[1,99999]

## ◆ BoxWidthLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BoxWidthLimitHigh | | getset |

Box宽度范围，范围：[1,99999]

## ◆ PerimeterLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PerimeterLimitEnable | | getset |

周长判断

## ◆ PerimeterLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double PerimeterLimitLow | | getset |

周长范围，范围：[1,999999999]

## ◆ PerimeterLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double PerimeterLimitHigh | | getset |

周长范围，范围：[1,999999999]

## ◆ LongAxisLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LongAxisLimitEnable | | getset |

长轴判断

## ◆ LongAxisLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LongAxisLimitLow | | getset |

长轴范围，范围：[1,999999999]

## ◆ LongAxisLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LongAxisLimitHigh | | getset |

长轴范围，范围：[1,999999999]

## ◆ ShortAxisLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ShortAxisLimitEnable | | getset |

短轴判断

## ◆ ShortAxisLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ShortAxisLimitLow | | getset |

短轴范围，范围：[1,999999999]

## ◆ ShortAxisLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ShortAxisLimitHigh | | getset |

短轴范围，范围：[1,999999999]

## ◆ CircularityLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CircularityLimitEnable | | getset |

圆形度判断

## ◆ CircularityLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CircularityLimitLow | | getset |

圆形度范围，范围：[0,1]

## ◆ CircularityLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CircularityLimitHigh | | getset |

圆形度范围，范围：[0,1]

## ◆ RectangularityLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RectangularityLimitEnable | | getset |

矩形度判断

## ◆ RectangularityLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectangularityLimitLow | | getset |

矩形度范围，范围：[0,1]

## ◆ RectangularityLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RectangularityLimitHigh | | getset |

矩形度范围，范围：[0,1]

## ◆ BolbOutLineEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BolbOutLineEnable | | getset |

轮廓输出使能(废弃)
