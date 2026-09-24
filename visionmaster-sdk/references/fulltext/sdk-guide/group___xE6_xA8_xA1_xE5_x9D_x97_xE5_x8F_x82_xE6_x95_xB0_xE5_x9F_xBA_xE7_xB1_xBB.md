<!-- src:group___xE6_xA8_xA1_xE5_x9D_x97_xE5_x8F_x82_xE6_x95_xB0_xE5_x9F_xBA_xE7_xB1_xBB.html -->
<!-- path:接口函数 > 公共模块 > 模块参数基类 -->
# 模块参数基类 公共模块

模块参数基类包含一些公共方法。
更多...

|  |  |
| --- | --- |
| 类 | |
| struct | InputStringData |
|  | 字符串类型 更多... |
|  | |
| class | ImageName |
|  | 图像信息名称 更多... |
|  | |
| class | InputImageData |
|  | 图像数据类型 更多... |
|  | |
| struct | BytesData |
|  | 二进制数据类型 更多... |
|  | |
| struct | RoiPoint |
|  | 点ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiBox |
|  | 矩形ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiAnnulus |
|  | 圆环ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiPolygon |
|  | 多边形ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiLineCaliper |
|  | 直线卡尺ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiCircleCaliper |
|  | 圆形卡尺ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| struct | RoiSectorCaliper |
|  | 圆弧卡尺ROI（归一化数据，即把数据映射到目标区域范围之内处理） 更多... |
|  | |
| class | CModuleParamBase |
|  | 模块参数基类 更多... |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | ImagePixelFormat {     IMAGE\_PIXEL\_FORMAT\_NULL = 0,     IMAGE\_PIXEL\_FORMAT\_MONO8 = 1,     IMAGE\_PIXEL\_FORMAT\_RGB24 = 2,     IMAGE\_PIXEL\_FORMAT\_RGB24\_P3 = 3   } |
|  | 图像像素格式 更多... |
|  | |
| enum | RoiType {     ROI\_TYPE\_IMAGE = 1,     ROI\_TYPE\_BOX = 2,     ROI\_TYPE\_ANNULUS = 3,     ROI\_TYPE\_POLYGON = 4,     ROI\_TYPE\_LINECALIPER = 5,     ROI\_TYPE\_CIRCLECALIPER = 6,     ROI\_TYPE\_SECTORCALIPER = 10   } |
|  | ROI形状类型 更多... |
|  | |

## 详细描述

模块参数基类包含一些公共方法。

## 枚举类型说明

## ◆ ImagePixelFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImagePixelFormat | | strong |

图像像素格式

| 枚举值 | |
| --- | --- |
| IMAGE\_PIXEL\_FORMAT\_NULL | 未知 |
| IMAGE\_PIXEL\_FORMAT\_MONO8 | MONO8 |
| IMAGE\_PIXEL\_FORMAT\_RGB24 | RGB24 C3 |
| IMAGE\_PIXEL\_FORMAT\_RGB24\_P3 | RGB24 P3 |

## ◆ RoiType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RoiType | | strong |

ROI形状类型

| 枚举值 | |
| --- | --- |
| ROI\_TYPE\_IMAGE | 全图ROI |
| ROI\_TYPE\_BOX | 矩形ROI |
| ROI\_TYPE\_ANNULUS | 圆环ROI |
| ROI\_TYPE\_POLYGON | 多边形ROI |
| ROI\_TYPE\_LINECALIPER | 直线卡尺ROI |
| ROI\_TYPE\_CIRCLECALIPER | 圆形卡尺ROI |
| ROI\_TYPE\_SECTORCALIPER | 圆弧卡尺ROI |
