<!-- src:class_i_m_v_s_ocr_modu_cs_1_1_ocr_param.html -->
<!-- path:接口函数 > 识别 > 字符识别 > OcrParam -->
# OcrParam类 参考 识别 » 字符识别

字符识别参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | PolarityEnum {     DarkOnBright = 0x1,     BrightOnDark = 0x2   } |
|  | 字符极性 更多... |
|  | |
| enum | WidthTypeEnum {     Changable = 0x0,     Aequilatus = 0x1   } |
|  | 宽度类型 更多... |
|  | |
| enum | IgnoreBorderFragmentEnableEnum {     Tab\_No = 0x0,     Tab\_Yes = 0x1   } |
|  | 忽略边框 更多... |
|  | |
| enum | ClassMethodEnum {     NearestDistance = 0x1,     WeightHighest = 0x2,     RateFastest = 0x3   } |
|  | 分类方法 更多... |
|  | |
| enum | StrokeFilterEnableEnum {     No = 0x0,     Yes = 0x1   } |
|  | 字宽滤波使能 更多... |
|  | |
| enum | SimilarFunEnum {     Euclid = 0x1,     Cosine = 0x2   } |
|  | 相似度类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| OcrRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| bool | FontFilterEnable `[get, set]` |
|  | 启用字符过滤 更多... |
|  | |
| int | FontFilterNum `[get, set]` |
|  | 识别字符个数，范围：[1,50] 更多... |
|  | |
| string | FontFilterInfo `[get, set]` |
|  | 字符过滤信息 更多... |
|  | |
| PolarityEnum | Polarity `[get, set]` |
|  | 字符极性 更多... |
|  | |
| int | MinCharWidth `[get, set]` |
|  | 字符宽度范围，范围：[1,512] 更多... |
|  | |
| int | MaxCharWidth `[get, set]` |
|  | 字符宽度范围，范围：[1,512] 更多... |
|  | |
| WidthTypeEnum | WidthType `[get, set]` |
|  | 宽度类型 更多... |
|  | |
| int | MinCharHeight `[get, set]` |
|  | 字符高度范围，范围：[1,512] 更多... |
|  | |
| int | MaxCharHeight `[get, set]` |
|  | 字符高度范围，范围：[1,512] 更多... |
|  | |
| int | BinaryCoef `[get, set]` |
|  | 二值化系数，范围：[1,99] 更多... |
|  | |
| int | MinCharArea `[get, set]` |
|  | 片段面积范围，范围：[0,100000] 更多... |
|  | |
| int | MaxCharArea `[get, set]` |
|  | 片段面积范围，范围：[0,100000] 更多... |
|  | |
| int | AcceptThreshold `[get, set]` |
|  | 合格阈值，范围：[0,100] 更多... |
|  | |
| int | MainLineDistThresh `[get, set]` |
|  | 距离阈值，范围：[0,100] 更多... |
|  | |
| IgnoreBorderFragmentEnableEnum | IgnoreBorderFragmentEnable `[get, set]` |
|  | 忽略边框 更多... |
|  | |
| int | OrientHalfRange `[get, set]` |
|  | 主方向范围，范围：[0,45] 更多... |
|  | |
| int | SlantHalfRange `[get, set]` |
|  | 倾斜角范围，范围：[0,45] 更多... |
|  | |
| int | MinInterCharGap `[get, set]` |
|  | 字符最小间隙，范围：[0,1000] 更多... |
|  | |
| int | MinInterTextGap `[get, set]` |
|  | 行间最小间隙，范围：[0,1000] 更多... |
|  | |
| int | MaxLengthWidthRatio `[get, set]` |
|  | 最大宽高比，范围：[1,1000] 更多... |
|  | |
| ClassMethodEnum | ClassMethod `[get, set]` |
|  | 分类方法 更多... |
|  | |
| StrokeFilterEnableEnum | StrokeFilterEnable `[get, set]` |
|  | 字宽滤波使能 更多... |
|  | |
| int | MinStrokeWidth `[get, set]` |
|  | 笔画宽度范围，范围：[1,64] 更多... |
|  | |
| int | MaxStrokeWidth `[get, set]` |
|  | 笔画宽度范围，范围：[1,64] 更多... |
|  | |
| SimilarFunEnum | SimilarFun `[get, set]` |
|  | 相似度类型 更多... |
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

字符识别参数

## 成员枚举类型说明

## ◆ PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PolarityEnum | | strong |

字符极性

| 枚举值 | |
| --- | --- |
| DarkOnBright | 白底黑字 |
| BrightOnDark | 黑底白字 |

## ◆ WidthTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum WidthTypeEnum | | strong |

宽度类型

| 枚举值 | |
| --- | --- |
| Changable | 可变类型 |
| Aequilatus | 等宽类型 |

## ◆ IgnoreBorderFragmentEnableEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum IgnoreBorderFragmentEnableEnum | | strong |

忽略边框

| 枚举值 | |
| --- | --- |
| Tab\_No | 否 |
| Tab\_Yes | 是 |

## ◆ ClassMethodEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ClassMethodEnum | | strong |

分类方法

| 枚举值 | |
| --- | --- |
| NearestDistance | 距离最近 |
| WeightHighest | 权重最高 |
| RateFastest | 频率最高 |

## ◆ StrokeFilterEnableEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum StrokeFilterEnableEnum | | strong |

字宽滤波使能

| 枚举值 | |
| --- | --- |
| No | 不使能 |
| Yes | 使能 |

## ◆ SimilarFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SimilarFunEnum | | strong |

相似度类型

| 枚举值 | |
| --- | --- |
| Euclid | 欧式距离 |
| Cosine | 余弦距离 |

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
| |  | | --- | | OcrRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FontFilterEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FontFilterEnable | | getset |

启用字符过滤

## ◆ FontFilterNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FontFilterNum | | getset |

识别字符个数，范围：[1,50]

## ◆ FontFilterInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FontFilterInfo | | getset |

字符过滤信息

## ◆ Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarityEnum Polarity | | getset |

字符极性

## ◆ MinCharWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinCharWidth | | getset |

字符宽度范围，范围：[1,512]

## ◆ MaxCharWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxCharWidth | | getset |

字符宽度范围，范围：[1,512]

## ◆ WidthType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WidthTypeEnum WidthType | | getset |

宽度类型

## ◆ MinCharHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinCharHeight | | getset |

字符高度范围，范围：[1,512]

## ◆ MaxCharHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxCharHeight | | getset |

字符高度范围，范围：[1,512]

## ◆ BinaryCoef

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BinaryCoef | | getset |

二值化系数，范围：[1,99]

## ◆ MinCharArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinCharArea | | getset |

片段面积范围，范围：[0,100000]

## ◆ MaxCharArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxCharArea | | getset |

片段面积范围，范围：[0,100000]

## ◆ AcceptThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int AcceptThreshold | | getset |

合格阈值，范围：[0,100]

## ◆ MainLineDistThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MainLineDistThresh | | getset |

距离阈值，范围：[0,100]

## ◆ IgnoreBorderFragmentEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IgnoreBorderFragmentEnableEnum IgnoreBorderFragmentEnable | | getset |

忽略边框

## ◆ OrientHalfRange

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OrientHalfRange | | getset |

主方向范围，范围：[0,45]

## ◆ SlantHalfRange

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SlantHalfRange | | getset |

倾斜角范围，范围：[0,45]

## ◆ MinInterCharGap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinInterCharGap | | getset |

字符最小间隙，范围：[0,1000]

## ◆ MinInterTextGap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinInterTextGap | | getset |

行间最小间隙，范围：[0,1000]

## ◆ MaxLengthWidthRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxLengthWidthRatio | | getset |

最大宽高比，范围：[1,1000]

## ◆ ClassMethod

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ClassMethodEnum ClassMethod | | getset |

分类方法

## ◆ StrokeFilterEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | StrokeFilterEnableEnum StrokeFilterEnable | | getset |

字宽滤波使能

## ◆ MinStrokeWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinStrokeWidth | | getset |

笔画宽度范围，范围：[1,64]

## ◆ MaxStrokeWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxStrokeWidth | | getset |

笔画宽度范围，范围：[1,64]

## ◆ SimilarFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SimilarFunEnum SimilarFun | | getset |

相似度类型

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
