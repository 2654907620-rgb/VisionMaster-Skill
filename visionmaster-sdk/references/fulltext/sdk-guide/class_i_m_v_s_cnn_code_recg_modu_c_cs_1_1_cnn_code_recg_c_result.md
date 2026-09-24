<!-- src:class_i_m_v_s_cnn_code_recg_modu_c_cs_1_1_cnn_code_recg_c_result.html -->
<!-- path:接口函数 > 识别 > DL读码CPU > CnnCodeRecgCResult -->
# CnnCodeRecgCResult类 参考 识别 » DL读码CPU

DL读码 CPU结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | CodeNum `[get]` |
|  | 码个数 更多... |
|  | |
| List< int > | CodeStatus `[get]` |
|  | 码状态 更多... |
|  | |
| List< string > | CodeStr `[get]` |
|  | 编码信息 更多... |
|  | |
| List< int > | CodeType `[get]` |
|  | 码类型 更多... |
|  | |
| List< float > | PPM `[get]` |
|  | PPM 更多... |
|  | |
| List< PointF > | CornerPoint `[get]` |
|  | 码角点（弃用） 更多... |
|  | |
| List< PointF > | CodeCornerPoint `[get]` |
|  | 码角点 更多... |
|  | |
| List< float > | CodeAngle `[get]` |
|  | 码角度 更多... |
|  | |
| List< int > | CodeMirrorFlag `[get]` |
|  | 码镜像标志 更多... |
|  | |
| List< RectBox > | Rect `[get]` |
|  | 矩形框 更多... |
|  | |
| List< int > | CodeRowNum `[get]` |
|  | 码行号 更多... |
|  | |
| List< int > | CodeColumnNum `[get]` |
|  | 码列号 更多... |
|  | |
| RectBox | ROI `[get]` |
|  | 检测区域 更多... |
|  | |
| List< int > | OverQuality `[get]` |
|  | 总质量等级 更多... |
|  | |
| List< int > | Decode `[get]` |
|  | 译码评分 更多... |
|  | |
| List< int > | SymbolContrast `[get]` |
|  | 符号对比度 更多... |
|  | |
| List< int > | Modulation `[get]` |
|  | 模块均匀性 更多... |
|  | |
| List< float > | ScScore `[get]` |
|  | 符号对比度分数 更多... |
|  | |
| List< float > | ModScore `[get]` |
|  | 模块均匀性分数 更多... |
|  | |
| List< int > | FixedPatternDamage `[get]` |
|  | 固定程度 更多... |
|  | |
| List< int > | Axial `[get]` |
|  | 轴向不均匀性 更多... |
|  | |
| List< int > | Grid `[get]` |
|  | 网格不均匀性 更多... |
|  | |
| List< int > | UnusedErrorCorrection `[get]` |
|  | 未使用纠错 更多... |
|  | |
| List< int > | PrintGrowthHor `[get]` |
|  | 水平打印伸缩 更多... |
|  | |
| List< int > | PrintGrowthVer `[get]` |
|  | 垂直打印伸缩 更多... |
|  | |
| List< int > | RmGrade `[get]` |
|  | 反射率余量 更多... |
|  | |
| List< float > | FpdScore `[get]` |
|  | 固定程度分数 更多... |
|  | |
| List< float > | AnScore `[get]` |
|  | 码轴规整性分数 更多... |
|  | |
| List< float > | GnScore `[get]` |
|  | 网格均匀性分数 更多... |
|  | |
| List< float > | UecScore `[get]` |
|  | 未使用纠错分数 更多... |
|  | |
| List< float > | PghScore `[get]` |
|  | 水平打印伸缩分数 更多... |
|  | |
| List< float > | PgvScore `[get]` |
|  | 垂直打印伸缩分数 更多... |
|  | |
| List< float > | RmScore `[get]` |
|  | 反射率余量分数 更多... |
|  | |
| List< int > | EdgeDetermination `[get]` |
|  | 边缘确定度 更多... |
|  | |
| List< int > | MinReflectance `[get]` |
|  | 最小反射率 更多... |
|  | |
| List< int > | MinEdgeContrast `[get]` |
|  | 最小边缘对比度 更多... |
|  | |
| List< int > | Decodability `[get]` |
|  | 可译码性 更多... |
|  | |
| List< int > | Defects `[get]` |
|  | 缺陷度 更多... |
|  | |
| List< int > | QuietZone `[get]` |
|  | 静区 更多... |
|  | |
| List< float > | EdgeScore `[get]` |
|  | 边缘确定度分数 更多... |
|  | |
| List< float > | MinrScore `[get]` |
|  | 最小反射率分数 更多... |
|  | |
| List< float > | MineScore `[get]` |
|  | 最小边缘对比度分数 更多... |
|  | |
| List< float > | DcdScore `[get]` |
|  | 可译码性分数 更多... |
|  | |
| List< float > | DefScore `[get]` |
|  | 缺陷分数 更多... |
|  | |
| List< float > | QzScore `[get]` |
|  | 静区分数 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

DL读码 CPU结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ CodeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CodeNum | | get |

码个数

## ◆ CodeStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CodeStatus | | get |

码状态

## ◆ CodeStr

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> CodeStr | | get |

编码信息

## ◆ CodeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CodeType | | get |

码类型

## ◆ PPM

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> PPM | | get |

PPM

## ◆ CornerPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CornerPoint | | get |

码角点（弃用）

## ◆ CodeCornerPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CodeCornerPoint | | get |

码角点

## ◆ CodeAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> CodeAngle | | get |

码角度

## ◆ CodeMirrorFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CodeMirrorFlag | | get |

码镜像标志

## ◆ Rect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> Rect | | get |

矩形框

## ◆ CodeRowNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CodeRowNum | | get |

码行号

## ◆ CodeColumnNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> CodeColumnNum | | get |

码列号

## ◆ ROI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectBox ROI | | get |

检测区域

## ◆ OverQuality

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> OverQuality | | get |

总质量等级

## ◆ Decode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Decode | | get |

译码评分

## ◆ SymbolContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> SymbolContrast | | get |

符号对比度

## ◆ Modulation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Modulation | | get |

模块均匀性

## ◆ ScScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ScScore | | get |

符号对比度分数

## ◆ ModScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ModScore | | get |

模块均匀性分数

## ◆ FixedPatternDamage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> FixedPatternDamage | | get |

固定程度

## ◆ Axial

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Axial | | get |

轴向不均匀性

## ◆ Grid

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Grid | | get |

网格不均匀性

## ◆ UnusedErrorCorrection

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> UnusedErrorCorrection | | get |

未使用纠错

## ◆ PrintGrowthHor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> PrintGrowthHor | | get |

水平打印伸缩

## ◆ PrintGrowthVer

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> PrintGrowthVer | | get |

垂直打印伸缩

## ◆ RmGrade

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RmGrade | | get |

反射率余量

## ◆ FpdScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> FpdScore | | get |

固定程度分数

## ◆ AnScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> AnScore | | get |

码轴规整性分数

## ◆ GnScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> GnScore | | get |

网格均匀性分数

## ◆ UecScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> UecScore | | get |

未使用纠错分数

## ◆ PghScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> PghScore | | get |

水平打印伸缩分数

## ◆ PgvScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> PgvScore | | get |

垂直打印伸缩分数

## ◆ RmScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> RmScore | | get |

反射率余量分数

## ◆ EdgeDetermination

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> EdgeDetermination | | get |

边缘确定度

## ◆ MinReflectance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MinReflectance | | get |

最小反射率

## ◆ MinEdgeContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> MinEdgeContrast | | get |

最小边缘对比度

## ◆ Decodability

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Decodability | | get |

可译码性

## ◆ Defects

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Defects | | get |

缺陷度

## ◆ QuietZone

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> QuietZone | | get |

静区

## ◆ EdgeScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> EdgeScore | | get |

边缘确定度分数

## ◆ MinrScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MinrScore | | get |

最小反射率分数

## ◆ MineScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> MineScore | | get |

最小边缘对比度分数

## ◆ DcdScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DcdScore | | get |

可译码性分数

## ◆ DefScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> DefScore | | get |

缺陷分数

## ◆ QzScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> QzScore | | get |

静区分数
