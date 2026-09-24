<!-- src:class_i_m_v_s_group_cs_1_1_group_result.html -->
<!-- path:接口函数 > 逻辑工具 > Group > GroupResult -->
# GroupResult类 参考 逻辑工具 » Group

Group结果
更多...

|  |  |
| --- | --- |
| Public 成员函数 | |
| IntDataArray | GetOutputInt (string strParam) |
|  | 整型输出（结果为空时nValueNum为0且pIntVal和nReserved为null） 更多... |
|  | |
| FloatDataArray | GetOutputFloat (string strParam) |
|  | 浮点型结果（结果为空时nValueNum为0且pFloatVal和nReserved为null） 更多... |
|  | |
| StringDataArray | GetOutputString (string strParam) |
|  | 字符串型结果（结果为空时nValueNum为0且astStringVal和nReserved为null） 更多... |
|  | |
| ByteArrayData | GetOutputImage (string strParam) |
|  | 图像型结果（结果为空时nDataLen为0且pData和nReserved为null） 更多... |
|  | |
| MatchOutline | GetOutputPointset (string strParam) |
|  | |
| StringData | GetOutputByteArray (string strParam) |
|  | 二进制数据型结果（结果为空时strValue为null） 更多... |
|  | |
| ImageBaseData | GetOutputImageV2 (string strParam) |
|  | 获取图像结果（整个图像） 更多... |
|  | |
| List< PointF > | GetOutputPointArray (string strParam) |
|  | 获取点输出集合 更多... |
|  | |
| List< Line > | GetOutputLineArray (string strParam) |
|  | 获取直线输出集合 更多... |
|  | |
| List< Circle > | GetOutputCircleArray (string strParam) |
|  | 获取圆输出集合 更多... |
|  | |
| List< RectBox > | GetOutputBoxArray (string strParam) |
|  | 获取带角度矩形输出集合 更多... |
|  | |
| List< RectF > | GetOutputRectArray (string strParam) |
|  | 获取无角度矩形(浮点型)输出集合 更多... |
|  | |
| List< Fixture > | GetOutputFixtureArray (string strParam) |
|  | 获取位置修正输出集合 更多... |
|  | |
| List< Annulus > | GetOutputAnnulusArray (string strParam) |
|  | 获取圆环输出集合 更多... |
|  | |
| List< ClassInfo > | GetOutputClassInfoArray (string strParam) |
|  | 获取类别信息输出集合 更多... |
|  | |
| PixelImage | GetOutputPixelImage (string strParam) |
|  | 获取带类别信息的图 更多... |
|  | |
| List< Posture > | GetOutputPostureArray (string strParam) |
|  | 获取位姿集合 更多... |
|  | |
| List< Polygon > | GetOutputPolygonArray (string strParam) |
|  | 获取多边形输出集合 更多... |
|  | |
| List< Ellipse > | GetOutputEllipseArray (string strParam) |
|  | 获取椭圆输出集合 更多... |
|  | |
| List< VmDynamicIODefine.IoNameInfo > | GetAllOutputNameInfo () |
|  | 获取所有输出名称信息 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |

## 详细描述

Group结果

## 成员函数说明

## ◆ GetOutputInt()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntDataArray GetOutputInt | ( | string | *strParam* | ) |  |

整型输出（结果为空时nValueNum为0且pIntVal和nReserved为null）

## ◆ GetOutputFloat()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatDataArray GetOutputFloat | ( | string | *strParam* | ) |  |

浮点型结果（结果为空时nValueNum为0且pFloatVal和nReserved为null）

## ◆ GetOutputString()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringDataArray GetOutputString | ( | string | *strParam* | ) |  |

字符串型结果（结果为空时nValueNum为0且astStringVal和nReserved为null）

## ◆ GetOutputImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ByteArrayData GetOutputImage | ( | string | *strParam* | ) |  |

图像型结果（结果为空时nDataLen为0且pData和nReserved为null）

## ◆ GetOutputPointset()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| MatchOutline GetOutputPointset | ( | string | *strParam* | ) |  |

点集型结果

## ◆ GetOutputByteArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringData GetOutputByteArray | ( | string | *strParam* | ) |  |

二进制数据型结果（结果为空时strValue为null）

## ◆ GetOutputImageV2()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageBaseData GetOutputImageV2 | ( | string | *strParam* | ) |  |

获取图像结果（整个图像）

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputPointArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<PointF> GetOutputPointArray | ( | string | *strParam* | ) |  |

获取点输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputLineArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Line> GetOutputLineArray | ( | string | *strParam* | ) |  |

获取直线输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputCircleArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Circle> GetOutputCircleArray | ( | string | *strParam* | ) |  |

获取圆输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputBoxArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectBox> GetOutputBoxArray | ( | string | *strParam* | ) |  |

获取带角度矩形输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputRectArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<RectF> GetOutputRectArray | ( | string | *strParam* | ) |  |

获取无角度矩形(浮点型)输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputFixtureArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Fixture> GetOutputFixtureArray | ( | string | *strParam* | ) |  |

获取位置修正输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputAnnulusArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Annulus> GetOutputAnnulusArray | ( | string | *strParam* | ) |  |

获取圆环输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputClassInfoArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<ClassInfo> GetOutputClassInfoArray | ( | string | *strParam* | ) |  |

获取类别信息输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputPixelImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| PixelImage GetOutputPixelImage | ( | string | *strParam* | ) |  |

获取带类别信息的图

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

**备注**

            界面可根据类别信息将灰度图显示成彩图

## ◆ GetOutputPostureArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Posture> GetOutputPostureArray | ( | string | *strParam* | ) |  |

获取位姿集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputPolygonArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Polygon> GetOutputPolygonArray | ( | string | *strParam* | ) |  |

获取多边形输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetOutputEllipseArray()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| List<Ellipse> GetOutputEllipseArray | ( | string | *strParam* | ) |  |

获取椭圆输出集合

参数
:   |  |  |
    | --- | --- |
    | strParam | 参数名称 |

返回
:   输出结果

## ◆ GetAllOutputNameInfo()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<VmDynamicIODefine.IoNameInfo> GetAllOutputNameInfo | ( |  | ) |  |

获取所有输出名称信息

返回
:   输出信息

**备注**

            CONTOURPOINTS、POINTSET这两种类型不支持

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态
