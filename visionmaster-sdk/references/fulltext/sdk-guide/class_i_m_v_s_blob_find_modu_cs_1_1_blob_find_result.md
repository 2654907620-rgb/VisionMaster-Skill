<!-- src:class_i_m_v_s_blob_find_modu_cs_1_1_blob_find_result.html -->
<!-- path:接口函数 > 定位 > Blob分析 > BlobFindResult -->
# BlobFindResult类 参考 定位 » Blob分析

Blob分析结果
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
| List< float > | MinGrayValue `[get]` |
|  | 最小灰度值 更多... |
|  | |
| List< float > | MaxGrayValue `[get]` |
|  | 最大灰度值 更多... |
|  | |
| List< float > | GrayContrast `[get]` |
|  | 对比度 更多... |
|  | |
| List< RectBox > | MaxAreaInnerRect `[get]` |
|  | 最大内接矩形 更多... |
|  | |
| List< RectI > | BlobRect `[get]` |
|  | Blob矩形框 更多... |
|  | |
| List< float > | BlobRectUpLeftX `[get]` |
|  | blob矩形左上点X 更多... |
|  | |
| List< float > | BlobRectUpLeftY `[get]` |
|  | blob矩形左上点Y 更多... |
|  | |
| List< float > | BlobRectBottomRightX `[get]` |
|  | blob矩形右下点X 更多... |
|  | |
| List< float > | BlobRectBottomRightY `[get]` |
|  | blob矩形右下点Y 更多... |
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
| List< float > | Circularity `[get]` |
|  | 圆形度 更多... |
|  | |
| List< float > | Rectangularity `[get]` |
|  | 矩形度 更多... |
|  | |
| List< float > | Score `[get]` |
|  | 分数 更多... |
|  | |
| ImageBaseData | BinaryImageComb `[get]` |
|  | 二值化图像数据 更多... |
|  | |
| ImageBaseData | BlobImageComb `[get]` |
|  | Blob图像数据 更多... |
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
| List< int > | BlindPolygonPointNum `[get]` |
|  | 多边形点数 更多... |
|  | |
| List< PointF > | BlindPolygonPoints `[get]` |
|  | 多边形点集 更多... |
|  | |
| List< string > | BlindPolygonString `[get]` |
|  | 屏蔽区字符串 更多... |
|  | |
| ImageBaseData | OutputMask `[get]` |
|  | 输出掩膜 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

Blob分析结果

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

## ◆ MinGrayValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MinGrayValue | | get |

最小灰度值

## ◆ MaxGrayValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MaxGrayValue | | get |

最大灰度值

## ◆ GrayContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> GrayContrast | | get |

对比度

## ◆ MaxAreaInnerRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> MaxAreaInnerRect | | get |

最大内接矩形

## ◆ BlobRect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectI> BlobRect | | get |

Blob矩形框

## ◆ BlobRectUpLeftX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> BlobRectUpLeftX | | get |

blob矩形左上点X

## ◆ BlobRectUpLeftY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> BlobRectUpLeftY | | get |

blob矩形左上点Y

## ◆ BlobRectBottomRightX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> BlobRectBottomRightX | | get |

blob矩形右下点X

## ◆ BlobRectBottomRightY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> BlobRectBottomRightY | | get |

blob矩形右下点Y

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

## ◆ BinaryImageComb

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData BinaryImageComb | | get |

二值化图像数据

## ◆ BlobImageComb

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData BlobImageComb | | get |

Blob图像数据

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

## ◆ OutputMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData OutputMask | | get |

输出掩膜
