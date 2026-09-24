<!-- src:class_i_m_v_s_ocr_dl_modu_cs_1_1_ocr_dl_param.html -->
<!-- path:接口函数 > 识别 > DL字符识别GPU > OcrDlParam -->
# OcrDlParam类 参考 识别 » DL字符识别GPU

DL字符识别 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| OcrDlRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| string | LoadModelPath `[get, set]` |
|  | 模型文件路径 更多... |
|  | |
| bool | SaveModelDataEnable `[get, set]` |
|  | 方案存模型 更多... |
|  | |
| bool | FontFilterEnable `[get, set]` |
|  | 启用字符校验（仅对手绘模式下的ROI-1有效） 更多... |
|  | |
| int | FontFilterNum `[get, set]` |
|  | 识别字符个数，范围：[1,32]（仅对手绘模式下的ROI-1有效） 更多... |
|  | |
| string | FontFilterInfo `[get, set]` |
|  | 字符过滤信息（仅对手绘模式下的ROI-1有效） 更多... |
|  | |
| double | MinConfidence `[get, set]` |
|  | 最小置信度，范围：[0.01,1.0] 更多... |
|  | |
| double | FlipMinScore `[get, set]` |
|  | 最小翻转分数，范围：[0.0,1.0] 更多... |
|  | |
| int | TextLineNum `[get, set]` |
|  | 最大文本行查找个数，范围：[1,5] 更多... |
|  | |
| bool | BatchProcessEnable `[get, set]` |
|  | 批处理使能 更多... |
|  | |
| int | BatchProcessingLevel `[get, set]` |
|  | 批处理等级，范围：[1,32] 更多... |
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

DL字符识别 GPU参数

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
| |  | | --- | | OcrDlRoiManager ModuRoiManager | | get |

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

启用字符校验（仅对手绘模式下的ROI-1有效）

## ◆ FontFilterNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FontFilterNum | | getset |

识别字符个数，范围：[1,32]（仅对手绘模式下的ROI-1有效）

## ◆ FontFilterInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FontFilterInfo | | getset |

字符过滤信息（仅对手绘模式下的ROI-1有效）

## ◆ MinConfidence

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MinConfidence | | getset |

最小置信度，范围：[0.01,1.0]

## ◆ FlipMinScore

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double FlipMinScore | | getset |

最小翻转分数，范围：[0.0,1.0]

## ◆ TextLineNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TextLineNum | | getset |

最大文本行查找个数，范围：[1,5]

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
