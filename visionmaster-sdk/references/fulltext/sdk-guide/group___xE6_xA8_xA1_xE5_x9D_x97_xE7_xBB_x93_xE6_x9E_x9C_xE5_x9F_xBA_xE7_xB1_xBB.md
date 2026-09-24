<!-- src:group___xE6_xA8_xA1_xE5_x9D_x97_xE7_xBB_x93_xE6_x9E_x9C_xE5_x9F_xBA_xE7_xB1_xBB.html -->
<!-- path:接口函数 > 公共模块 > 模块结果基类 -->
# 模块结果基类 公共模块

模块结果基类包含一些公共方法。
更多...

|  |  |
| --- | --- |
| 类 | |
| interface | IBaseData |
|  | 图形/图像数据基础功能接口 更多... |
|  | |
| class | ImageBaseData\_Base |
|  | 图像基本数据 更多... |
|  | |
| class | ImageBaseData\_V2 |
|  | 图像数据V2 更多... |
|  | |
| class | ImageBaseData |
|  | 图像数据 更多... |
|  | |
| class | PointF |
|  | 浮点型点 更多... |
|  | |
| class | PointI |
|  | 整型点 更多... |
|  | |
| class | RectI |
|  | 整型矩形框 更多... |
|  | |
| class | RectBox |
|  | 矩形框 更多... |
|  | |
| class | Line |
|  | 直线 更多... |
|  | |
| class | Circle |
|  | 圆 更多... |
|  | |
| class | Annulus |
|  | 圆弧信息 更多... |
|  | |
| class | DefectFixture |
|  | 缺陷综合信息 更多... |
|  | |
| struct | MatchPoint |
|  | 匹配点 更多... |
|  | |
| class | MatchOutline |
|  | 匹配轮廓信息 更多... |
|  | |
| class | Posture |
|  | 位姿信息 更多... |
|  | |
| class | RectF |
|  | 浮点型矩形框 更多... |
|  | |
| class | Polygon |
|  | 多边形 更多... |
|  | |
| class | ClassInfo |
|  | 类别信息 更多... |
|  | |
| class | PixelImage |
|  | 类别信息图像 更多... |
|  | |
| struct | StringData |
|  | 字符串信息 更多... |
|  | |
| struct | ByteArrayData |
|  | 二进制数据信息 更多... |
|  | |
| struct | IntDataArray |
|  | 整型数组信息 更多... |
|  | |
| struct | FloatDataArray |
|  | 浮点型数组信息 更多... |
|  | |
| struct | StringDataArray |
|  | 字符串型数组信息 更多... |
|  | |
| struct | ImageDataArray |
|  | 图像型数组信息 更多... |
|  | |
| struct | ByteDataArray |
|  | 二进制型数组信息 更多... |
|  | |
| struct | ModuInfo |
|  | 单个模块信息结构 更多... |
|  | |
| struct | ModuleInfoList |
|  | 模块信息列表结构 更多... |
|  | |
| struct | GroupModuInfo |
|  | Group模块信息结构 更多... |
|  | |
| struct | GroupModuInfoList |
|  | Group模块信息列表结构 更多... |
|  | |
| struct | IntResultInfo |
|  | 整型结果数据信息结构 更多... |
|  | |
| struct | FloatResultInfo |
|  | 浮点型结果数据信息结构 更多... |
|  | |
| struct | StringValueInfo |
|  | 字符串数据 更多... |
|  | |
| struct | StringResultInfo |
|  | 字符串型结果数据信息结构 更多... |
|  | |
| struct | BaseDataInfo |
|  | 基本数据类型 更多... |
|  | |
| struct | ImageResultInfo |
|  | 图像类型结果数据信息结构 更多... |
|  | |
| struct | PointsetResultInfo |
|  | 点集类型结果数据信息结构 更多... |
|  | |
| struct | ProcessInfo |
|  | 流程信息结构 更多... |
|  | |
| struct | ProcessInfoList |
|  | 流程信息列表结构 更多... |
|  | |
| struct | ProcedureRunPolicy |
|  | 用户自定义流程运行策略信息结构 更多... |
|  | |
| class | CModuleResultBase |
|  | 模块结果基类 更多... |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | IMVS\_MODULE\_BASE\_DATA\_TYPE {     IMVS\_BASE\_TYPE\_UNDEFINED = 0,     IMVS\_BASE\_TYPE\_IMAGE\_DATA = 1,     IMVS\_GRAP\_TYPE\_POINT\_F = 2,     IMVS\_GRAP\_TYPE\_RECT\_I = 3,     IMVS\_GRAP\_TYPE\_RECT\_BOX = 4,     IMVS\_GRAP\_TYPE\_LINE = 5,     IMVS\_GRAP\_TYPE\_CIRCLE = 6,     IMVS\_GRAP\_TYPE\_ANNULUS = 7,     IMVS\_GRAP\_TYPE\_DEFECT\_FIXTURE = 8,     IMVS\_GRAP\_TYPE\_MATCHOUTLINE = 9,     IMVS\_GRAP\_TYPE\_RECT\_F = 10,     IMVS\_GRAP\_TYPE\_FIXTURE = 11,     IMVS\_GRAP\_TYPE\_POLYGON = 12,     IMVS\_GRAP\_TYPE\_INT = 13,     IMVS\_GRAP\_TYPE\_FLOAT = 14,     IMVS\_GRAP\_TYPE\_STRING = 15,     IMVS\_GRAP\_TYPE\_POINTSET = 16,     IMVS\_GRAP\_TYPE\_BYTE = 17,     IMVS\_GRAP\_TYPE\_POINT\_I = 18,     IMVS\_GRAP\_TYPE\_CONTOURPOINTS = 19,     IMVS\_GRAP\_TYPE\_CLASSINFO = 20,     IMVS\_GRAP\_TYPE\_PIXELIMAGE = 21,     IMVS\_GRAP\_TYPE\_POSTURE = 22,     IMVS\_GRAP\_TYPE\_ELLIPSE = 23   } |
|  | 图像数据类型 更多... |
|  | |
| enum | VMPixelFormat {     VM\_PIXEL\_NULL = 0,     VM\_PIXEL\_MONO\_08 = ImvsSdkDefine.IMVS\_IMG\_FORMAT\_MONO8,     VM\_PIXEL\_RGB24\_C3 = ImvsSdkDefine.IMVS\_IMG\_FORMAT\_RGB24,     VM\_PIXEL\_RGB24\_P3 = ImvsSdkDefine.IMVS\_IMG\_FORMAT\_RGB24\_P3   } |
|  | 图像像素格式 更多... |
|  | |

## 详细描述

模块结果基类包含一些公共方法。

## 枚举类型说明

## ◆ IMVS\_MODULE\_BASE\_DATA\_TYPE

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum IMVS\_MODULE\_BASE\_DATA\_TYPE | | strong |

图像数据类型

| 枚举值 | |
| --- | --- |
| IMVS\_BASE\_TYPE\_UNDEFINED | 无效数据 |
| IMVS\_BASE\_TYPE\_IMAGE\_DATA | 图像数据 |
| IMVS\_GRAP\_TYPE\_POINT\_F | 浮点型点 |
| IMVS\_GRAP\_TYPE\_RECT\_I | 矩形 |
| IMVS\_GRAP\_TYPE\_RECT\_BOX | 矩形框 |
| IMVS\_GRAP\_TYPE\_LINE | 直线 |
| IMVS\_GRAP\_TYPE\_CIRCLE | 圆形 |
| IMVS\_GRAP\_TYPE\_ANNULUS | 圆弧 |
| IMVS\_GRAP\_TYPE\_DEFECT\_FIXTURE | 缺陷检测修正信息 |
| IMVS\_GRAP\_TYPE\_MATCHOUTLINE | 轮廓点 |
| IMVS\_GRAP\_TYPE\_RECT\_F | 不带角度的矩形 |
| IMVS\_GRAP\_TYPE\_FIXTURE | 位置修正 |
| IMVS\_GRAP\_TYPE\_POLYGON | 多边形 |
| IMVS\_GRAP\_TYPE\_INT | 整型 |
| IMVS\_GRAP\_TYPE\_FLOAT | 浮点型 |
| IMVS\_GRAP\_TYPE\_STRING | 字符串型 |
| IMVS\_GRAP\_TYPE\_POINTSET | 点集 |
| IMVS\_GRAP\_TYPE\_BYTE | 二进制 |
| IMVS\_GRAP\_TYPE\_POINT\_I | 点 |
| IMVS\_GRAP\_TYPE\_CONTOURPOINTS | 轮廓点 |
| IMVS\_GRAP\_TYPE\_CLASSINFO | 类别信息 |
| IMVS\_GRAP\_TYPE\_PIXELIMAGE | 带有类别信息的图像 |
| IMVS\_GRAP\_TYPE\_POSTURE | 位姿 |
| IMVS\_GRAP\_TYPE\_ELLIPSE | 椭圆 |

## ◆ VMPixelFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum VMPixelFormat | | strong |

图像像素格式

| 枚举值 | |
| --- | --- |
| VM\_PIXEL\_NULL | NULL |
| VM\_PIXEL\_MONO\_08 | MONO8 |
| VM\_PIXEL\_RGB24\_C3 | RGB24 C3 |
| VM\_PIXEL\_RGB24\_P3 | RGB24 P3 |
