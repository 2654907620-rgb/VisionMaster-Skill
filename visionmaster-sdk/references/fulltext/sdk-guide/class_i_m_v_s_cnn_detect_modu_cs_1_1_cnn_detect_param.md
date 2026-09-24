<!-- src:class_i_m_v_s_cnn_detect_modu_cs_1_1_cnn_detect_param.html -->
<!-- path:接口函数 > 深度学习 > DL目标检测GPU > CnnDetectParam -->
# CnnDetectParam类 参考 深度学习 » DL目标检测GPU

DL目标检测 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | SortObjectModeEnum {     XCoordinate = 0x1,     YCoordinate = 0x2,     Confidence = 0x3   } |
|  | 目标排序 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnDetectRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | RoiFromModelEnable `[get, set]` |
|  | 获取模型ROI 更多... |
|  | |
| bool | CutViaROIEnable `[get, set]` |
|  | 按ROI裁图 更多... |
|  | |
| int | MaxObjNum `[get, set]` |
|  | 最大查找个数，范围：[1,1000] 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | MaxOverlap `[get, set]` |
|  | 最大重叠率，范围：[0,1.0] 更多... |
|  | |
| SortObjectModeEnum | SortObjectMode `[get, set]` |
|  | 目标排序 更多... |
|  | |
| bool | BatchProcessEnable `[get, set]` |
|  | 批处理使能 更多... |
|  | |
| int | BatchProcessingLevel `[get, set]` |
|  | 批处理等级，范围：[1,32] 更多... |
|  | |
| bool | SODEnable `[get, set]` |
|  | 小目标模式 更多... |
|  | |
| int | XSlidingWinNumOfSOD `[get, set]` |
|  | 横向滑窗数，范围：[1,16] , Range:[1,16] 更多... |
|  | |
| int | YSlidingWinNumOfSOD `[get, set]` |
|  | 纵向滑窗数，范围：[1,16] , Range:[1,16] 更多... |
|  | |
| double | SlidingWinOverlap `[get, set]` |
|  | 滑窗重叠率，范围：[0,0.6] 更多... |
|  | |
| bool | OutRoiFilterEnable `[get, set]` |
|  | 边缘筛选使能 更多... |
|  | |
| double | MinEdgeScore `[get, set]` |
|  | 最小边缘分数，范围：[0.01,1.0] 更多... |
|  | |
| bool | AngleEnable `[get, set]` |
|  | 角度使能 更多... |
|  | |
| int | StartAngle `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| int | EndAngle `[get, set]` |
|  | 角度范围，范围：[-180,180] 更多... |
|  | |
| bool | WidthEnable `[get, set]` |
|  | 宽度使能 更多... |
|  | |
| int | MinWidth `[get, set]` |
|  | 宽度范围，范围：[1,4000] 更多... |
|  | |
| int | MaxWidth `[get, set]` |
|  | 宽度范围，范围：[1,4000] 更多... |
|  | |
| bool | HeightEnable `[get, set]` |
|  | 高度使能 更多... |
|  | |
| int | MinHeight `[get, set]` |
|  | 高度范围，范围：[1,4000] 更多... |
|  | |
| int | MaxHeight `[get, set]` |
|  | 高度范围，范围：[1,4000] 更多... |
|  | |
| bool | DiffClassNMSEnable `[get, set]` |
|  | 不同类别过滤 更多... |
|  | |
| bool | AreaEnable `[get, set]` |
|  | 面积使能 更多... |
|  | |
| int | MinArea `[get, set]` |
|  | 面积范围，范围：[1,16000000] 更多... |
|  | |
| int | MaxArea `[get, set]` |
|  | 面积范围，范围：[1,16000000] 更多... |
|  | |
| bool | WHRatioEnable `[get, set]` |
|  | 长短边比使能 更多... |
|  | |
| double | MinWHRatio `[get, set]` |
|  | 长短边比范围，范围：[1,100] 更多... |
|  | |
| double | MaxWHRatio `[get, set]` |
|  | 长短边比范围，范围：[1,100] 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 个数判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 个数范围，范围：[0,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 个数范围，范围：[0,99999] 更多... |
|  | |
| bool | ScoreLimitEnable `[get, set]` |
|  | 置信度判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 置信度范围，范围：[0,1] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 置信度范围，范围：[0,1] 更多... |
|  | |
| bool | ClassLimitEnable `[get, set]` |
|  | 类别号判断 更多... |
|  | |
| int | ClassLimitLow `[get, set]` |
|  | 类别号范围，范围：[0,99999] 更多... |
|  | |
| int | ClassLimitHigh `[get, set]` |
|  | 类别号范围，范围：[0,99999] 更多... |
|  | |
| bool | CategoryNameLimitEnable `[get, set]` |
|  | 类别名称判断 更多... |
|  | |
| string | CategoryNameLimit `[get, set]` |
|  | 类别名称 更多... |
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

DL目标检测 GPU参数

## 成员枚举类型说明

## ◆ SortObjectModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SortObjectModeEnum | | strong |

目标排序

| 枚举值 | |
| --- | --- |
| XCoordinate | 按中心点X坐标升序 |
| YCoordinate | 按中心点Y坐标升序 |
| Confidence | 按最小分数降序 |

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
| |  | | --- | | CnnDetectRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ LoadModelPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadModelPath | | getset |

模型文件路径

## ◆ SaveModelDataEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveModelDataEnable | | getset |

方案存模型

## ◆ RoiFromModelEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RoiFromModelEnable | | getset |

获取模型ROI

## ◆ CutViaROIEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CutViaROIEnable | | getset |

按ROI裁图

## ◆ MaxObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxObjNum | | getset |

最大查找个数，范围：[1,1000]

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小置信度，范围：[0.01,1.0]

## ◆ MaxOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxOverlap | | getset |

最大重叠率，范围：[0,1.0]

## ◆ SortObjectMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortObjectModeEnum SortObjectMode | | getset |

目标排序

## ◆ BatchProcessEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BatchProcessEnable | | getset |

批处理使能

## ◆ BatchProcessingLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BatchProcessingLevel | | getset |

批处理等级，范围：[1,32]

## ◆ SODEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SODEnable | | getset |

小目标模式

## ◆ XSlidingWinNumOfSOD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int XSlidingWinNumOfSOD | | getset |

横向滑窗数，范围：[1,16] , Range:[1,16]

## ◆ YSlidingWinNumOfSOD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int YSlidingWinNumOfSOD | | getset |

纵向滑窗数，范围：[1,16] , Range:[1,16]

## ◆ SlidingWinOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SlidingWinOverlap | | getset |

滑窗重叠率，范围：[0,0.6]

## ◆ OutRoiFilterEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutRoiFilterEnable | | getset |

边缘筛选使能

## ◆ MinEdgeScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinEdgeScore | | getset |

最小边缘分数，范围：[0.01,1.0]

## ◆ AngleEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AngleEnable | | getset |

角度使能

## ◆ StartAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int StartAngle | | getset |

角度范围，范围：[-180,180]

## ◆ EndAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EndAngle | | getset |

角度范围，范围：[-180,180]

## ◆ WidthEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool WidthEnable | | getset |

宽度使能

## ◆ MinWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinWidth | | getset |

宽度范围，范围：[1,4000]

## ◆ MaxWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxWidth | | getset |

宽度范围，范围：[1,4000]

## ◆ HeightEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool HeightEnable | | getset |

高度使能

## ◆ MinHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinHeight | | getset |

高度范围，范围：[1,4000]

## ◆ MaxHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxHeight | | getset |

高度范围，范围：[1,4000]

## ◆ DiffClassNMSEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DiffClassNMSEnable | | getset |

不同类别过滤

## ◆ AreaEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AreaEnable | | getset |

面积使能

## ◆ MinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinArea | | getset |

面积范围，范围：[1,16000000]

## ◆ MaxArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxArea | | getset |

面积范围，范围：[1,16000000]

## ◆ WHRatioEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool WHRatioEnable | | getset |

长短边比使能

## ◆ MinWHRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinWHRatio | | getset |

长短边比范围，范围：[1,100]

## ◆ MaxWHRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxWHRatio | | getset |

长短边比范围，范围：[1,100]

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

个数判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

个数范围，范围：[0,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

个数范围，范围：[0,99999]

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

置信度判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

置信度范围，范围：[0,1]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

置信度范围，范围：[0,1]

## ◆ ClassLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ClassLimitEnable | | getset |

类别号判断

## ◆ ClassLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ClassLimitLow | | getset |

类别号范围，范围：[0,99999]

## ◆ ClassLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ClassLimitHigh | | getset |

类别号范围，范围：[0,99999]

## ◆ CategoryNameLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CategoryNameLimitEnable | | getset |

类别名称判断

## ◆ CategoryNameLimit

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CategoryNameLimit | | getset |

类别名称
