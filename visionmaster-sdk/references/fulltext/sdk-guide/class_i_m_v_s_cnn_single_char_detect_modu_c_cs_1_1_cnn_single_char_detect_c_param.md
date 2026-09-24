<!-- src:class_i_m_v_s_cnn_single_char_detect_modu_c_cs_1_1_cnn_single_char_detect_c_param.html -->
<!-- path:接口函数 > 识别 > DL单字符检测CPU > CnnSingleCharDetectCParam -->
# CnnSingleCharDetectCParam类 参考 识别 » DL单字符检测CPU

DL单字符检测 CPU参数
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
| CnnSingleCharDetectCRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | FontFilterEnable `[get, set]` |
|  | 启用字符过滤 更多... |
|  | |
| int | FontFilterNum `[get, set]` |
|  | 识别字符个数，范围：[1,32] 更多... |
|  | |
| string | FontFilterInfo `[get, set]` |
|  | 字符过滤信息 更多... |
|  | |
| int | MaxObjNum `[get, set]` |
|  | 最大查找个数，范围：[1,100] 更多... |
|  | |
| double | MinScore `[get, set]` |
|  | 最小置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | MaxOverlap `[get, set]` |
|  | 最大重叠率，范围：[0.01,1.0] 更多... |
|  | |
| SortObjectModeEnum | SortObjectMode `[get, set]` |
|  | 目标排序 更多... |
|  | |
| bool | OutRoiFilterEnable `[get, set]` |
|  | 边缘筛选使能 更多... |
|  | |
| double | MinEdgeScore `[get, set]` |
|  | 最小边缘分数，范围：[0.01,1.0] 更多... |
|  | |
| bool | WidthEnable `[get, set]` |
|  | 文本宽度使能 更多... |
|  | |
| int | MinWidth `[get, set]` |
|  | 宽度范围，范围：[1,4000] 更多... |
|  | |
| int | MaxWidth `[get, set]` |
|  | 宽度范围，范围：[1,4000] 更多... |
|  | |
| bool | HeightEnable `[get, set]` |
|  | 文本高度使能 更多... |
|  | |
| int | MinHeight `[get, set]` |
|  | 高度范围，范围：[1,4000] 更多... |
|  | |
| int | MaxHeight `[get, set]` |
|  | 高度范围，范围：[1,4000] 更多... |
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
| bool | VerifyEnable `[get, set]` |
|  | 字符验证 更多... |
|  | |
| bool | NumVerifyEnable `[get, set]` |
|  | 数字集 更多... |
|  | |
| bool | SmallAlphabetVerify `[get, set]` |
|  | 小写字母集 更多... |
|  | |
| bool | BigAlphabetVerify `[get, set]` |
|  | 大写字母集 更多... |
|  | |
| bool | SpecialCharVerify `[get, set]` |
|  | 特殊字符集 更多... |
|  | |
| bool | UserStringVerify `[get, set]` |
|  | 用户字符验证 更多... |
|  | |
| string | UserString `[get, set]` |
|  | 用户字符 更多... |
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

DL单字符检测 CPU参数

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
| Confidence | 按置信度降序 |

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
| |  | | --- | | CnnSingleCharDetectCRoiManager ModuRoiManager | | get |

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

## ◆ FontFilterEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FontFilterEnable | | getset |

启用字符过滤

## ◆ FontFilterNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FontFilterNum | | getset |

识别字符个数，范围：[1,32]

## ◆ FontFilterInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FontFilterInfo | | getset |

字符过滤信息

## ◆ MaxObjNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxObjNum | | getset |

最大查找个数，范围：[1,100]

## ◆ MinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinScore | | getset |

最小置信度，范围：[0.01,1.0]

## ◆ MaxOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MaxOverlap | | getset |

最大重叠率，范围：[0.01,1.0]

## ◆ SortObjectMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SortObjectModeEnum SortObjectMode | | getset |

目标排序

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

## ◆ WidthEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool WidthEnable | | getset |

文本宽度使能

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

文本高度使能

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

## ◆ VerifyEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool VerifyEnable | | getset |

字符验证

## ◆ NumVerifyEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumVerifyEnable | | getset |

数字集

## ◆ SmallAlphabetVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SmallAlphabetVerify | | getset |

小写字母集

## ◆ BigAlphabetVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool BigAlphabetVerify | | getset |

大写字母集

## ◆ SpecialCharVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SpecialCharVerify | | getset |

特殊字符集

## ◆ UserStringVerify

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UserStringVerify | | getset |

用户字符验证

## ◆ UserString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string UserString | | getset |

用户字符
