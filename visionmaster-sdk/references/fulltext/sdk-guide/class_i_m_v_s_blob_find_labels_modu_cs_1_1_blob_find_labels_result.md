<!-- src:class_i_m_v_s_blob_find_labels_modu_cs_1_1_blob_find_labels_result.html -->
<!-- path:接口函数 > 定位 > Blob标签分析 > BlobFindLabelsResult -->
# BlobFindLabelsResult类 参考 定位 » Blob标签分析

Blob标签分析结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< int > | BlobStatus `[get]` |
|  | 单体状态 更多... |
|  | |
| int | BlobNum `[get]` |
|  | Blob个数 更多... |
|  | |
| List< float > | Area `[get]` |
|  | 面积 更多... |
|  | |
| float | TotalArea `[get]` |
|  | 总面积 更多... |
|  | |
| List< PointF > | CentroidPoint `[get]` |
|  | 质心点 更多... |
|  | |
| List< RectBox > | MinBoudingRect `[get]` |
|  | 最小外接矩形 更多... |
|  | |
| List< float > | BlobAngle `[get]` |
|  | 主轴角度 更多... |
|  | |
| List< float > | Perimeter `[get]` |
|  | 周长 更多... |
|  | |
| List< float > | LongAxis `[get]` |
|  | 长轴 更多... |
|  | |
| List< float > | ShortAxis `[get]` |
|  | 短轴 更多... |
|  | |
| List< float > | AxisRatio `[get]` |
|  | 轴比（短轴/长轴） 更多... |
|  | |
| List< float > | Circularity `[get]` |
|  | 圆形度 更多... |
|  | |
| List< float > | Rectangularity `[get]` |
|  | 矩形度 更多... |
|  | |
| List< float > | Score `[get]` |
|  | 分数 更多... |
|  | |
| ImageBaseData | BlobBinImage `[get]` |
|  | 二值化图像 更多... |
|  | |
| ImageBaseData | BlobBlockImage `[get]` |
|  | Blob图像 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| List< RectBox > | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< Annulus > | ROIAnnulus `[get]` |
|  | ROI圆弧 更多... |
|  | |
| MatchOutline | ContourInfo `[get]` |
|  | 轮廓信息 更多... |
|  | |
| int | ContourNum `[get]` |
|  | 轮廓点个数 更多... |
|  | |
| List< string > | ClassLabel `[get]` |
|  | 类别标签 更多... |
|  | |
| List< int > | LabelValue `[get]` |
|  | 灰度值 更多... |
|  | |
| List< int > | BlindPolygonPointNum `[get]` |
|  | 多边形点数 更多... |
|  | |
| List< PointF > | BlindPolygonPoints `[get]` |
|  | 多边形点集 更多... |
|  | |
| List< string > | BlindPolygonString `[get]` |
|  | 屏蔽区字符串 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

Blob标签分析结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ BlobStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BlobStatus | | get |

单体状态

## ◆ BlobNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BlobNum | | get |

Blob个数

## ◆ Area

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Area | | get |

面积

## ◆ TotalArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TotalArea | | get |

总面积

## ◆ CentroidPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CentroidPoint | | get |

质心点

## ◆ MinBoudingRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MinBoudingRect | | get |

最小外接矩形

## ◆ BlobAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> BlobAngle | | get |

主轴角度

## ◆ Perimeter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Perimeter | | get |

周长

## ◆ LongAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> LongAxis | | get |

长轴

## ◆ ShortAxis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ShortAxis | | get |

短轴

## ◆ AxisRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> AxisRatio | | get |

轴比（短轴/长轴）

## ◆ Circularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Circularity | | get |

圆形度

## ◆ Rectangularity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Rectangularity | | get |

矩形度

## ◆ Score

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> Score | | get |

分数

## ◆ BlobBinImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData BlobBinImage | | get |

二值化图像

## ◆ BlobBlockImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData BlobBlockImage | | get |

Blob图像

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> ROI | | get |

检测区域

## ◆ ROIAnnulus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Annulus> ROIAnnulus | | get |

ROI圆弧

## ◆ ContourInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MatchOutline ContourInfo | | get |

轮廓信息

## ◆ ContourNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ContourNum | | get |

轮廓点个数

## ◆ ClassLabel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> ClassLabel | | get |

类别标签

## ◆ LabelValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> LabelValue | | get |

灰度值

## ◆ BlindPolygonPointNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BlindPolygonPointNum | | get |

多边形点数

## ◆ BlindPolygonPoints

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> BlindPolygonPoints | | get |

多边形点集

## ◆ BlindPolygonString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> BlindPolygonString | | get |

屏蔽区字符串
