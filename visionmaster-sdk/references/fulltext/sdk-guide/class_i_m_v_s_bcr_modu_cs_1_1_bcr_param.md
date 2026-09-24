<!-- src:class_i_m_v_s_bcr_modu_cs_1_1_bcr_param.html -->
<!-- path:接口函数 > 识别 > 条码识别 > BcrParam -->
# BcrParam类 参考 识别 » 条码识别

条码识别参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| BcrRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | CODE39 `[get, set]` |
|  | CODE39码 更多... |
|  | |
| bool | CODE128 `[get, set]` |
|  | CODE128码 更多... |
|  | |
| bool | CODABAR `[get, set]` |
|  | 库得巴码 更多... |
|  | |
| bool | EAN `[get, set]` |
|  | EAN码 更多... |
|  | |
| bool | ITF25 `[get, set]` |
|  | 交替25码 更多... |
|  | |
| bool | CODE93 `[get, set]` |
|  | CODE93码 更多... |
|  | |
| int | BarNum `[get, set]` |
|  | 条码个数，范围：[1,200] 更多... |
|  | |
| int | PreSampleLevel `[get, set]` |
|  | 降采样系数，范围：[1,8] 更多... |
|  | |
| int | LocWinSize `[get, set]` |
|  | 检测窗口大小，范围：[4,5] 更多... |
|  | |
| int | SegQuietW `[get, set]` |
|  | 静区宽度，范围：[0,200] 更多... |
|  | |
| int | DfkMinSize `[get, set]` |
|  | 去伪过滤尺寸，范围：[0,4000] 更多... |
|  | |
| int | DfkMaxSize `[get, set]` |
|  | 去伪过滤尺寸，范围：[0,4000] 更多... |
|  | |
| int | WaitingTime `[get, set]` |
|  | 超时退出时间，范围：[0,5000] 更多... |
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

条码识别参数

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
| |  | | --- | | BcrRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ CODE39

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CODE39 | | getset |

CODE39码

## ◆ CODE128

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CODE128 | | getset |

CODE128码

## ◆ CODABAR

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CODABAR | | getset |

库得巴码

## ◆ EAN

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EAN | | getset |

EAN码

## ◆ ITF25

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ITF25 | | getset |

交替25码

## ◆ CODE93

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CODE93 | | getset |

CODE93码

## ◆ BarNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BarNum | | getset |

条码个数，范围：[1,200]

## ◆ PreSampleLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PreSampleLevel | | getset |

降采样系数，范围：[1,8]

## ◆ LocWinSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LocWinSize | | getset |

检测窗口大小，范围：[4,5]

## ◆ SegQuietW

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SegQuietW | | getset |

静区宽度，范围：[0,200]

## ◆ DfkMinSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DfkMinSize | | getset |

去伪过滤尺寸，范围：[0,4000]

## ◆ DfkMaxSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DfkMaxSize | | getset |

去伪过滤尺寸，范围：[0,4000]

## ◆ WaitingTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WaitingTime | | getset |

超时退出时间，范围：[0,5000]

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
