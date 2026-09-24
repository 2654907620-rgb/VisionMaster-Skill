<!-- src:class_i_m_v_s_cnn_code_recg_modu_cs_1_1_cnn_code_recg_param.html -->
<!-- path:接口函数 > 识别 > DL读码GPU > CnnCodeRecgParam -->
# CnnCodeRecgParam类 参考 识别 » DL读码GPU

DL读码 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CodePolarityEnum {     dark = 0x0,     bright = 0x1,     both = 0x2   } |
|  | 极性 更多... |
|  | |
| enum | DiscreteFlagEnum {     continuous = 0x0,     discrete = 0x1,     allmode = 0x2   } |
|  | 边缘类型 更多... |
|  | |
| enum | MirrorModeEnum {     Off = 0x0,     On = 0x1,     Both = 0x2   } |
|  | 镜像模式 更多... |
|  | |
| enum | DistortionFlagEnum {     Off = 0x0,     On = 0x1   } |
|  | QR畸变 更多... |
|  | |
| enum | RectangleEnum {     Square = 0x0,     Rectangle = 0x1,     AllMode = 0x2   } |
|  | DM码类型 更多... |
|  | |
| enum | StandardTypeEnum {     ISO15415 = 0x1,     ISO29158 = 0x2   } |
|  | ISO标准 更多... |
|  | |
| enum | MirrorEnum {     Off = 0x0,     On = 0x1,     Both = 0x2   } |
|  | 镜像模式 更多... |
|  | |
| enum | ClassificationTypeEnum {     process\_type\_one = 0x1,     process\_type\_two = 0x2   } |
|  | 评级处理类型 更多... |
|  | |
| enum | VerifyLabelTypeEnum {     ISO\_Mode = 0x1,     HIK\_Mode = 0x2   } |
|  | 评级模式 更多... |
|  | |
| enum | PolarityEnum {     dark = 0x0,     bright = 0x1,     both = 0x2   } |
|  | 极性 更多... |
|  | |
| enum | EdgeFeatureEnum {     continuous = 0x0,     discrete = 0x1   } |
|  | 边缘类型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnCodeRecgRoiManager | ModuRoiManager `[get]` |
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
| bool | EAN8 `[get, set]` |
|  | EAN8码 更多... |
|  | |
| bool | EAN13 `[get, set]` |
|  | EAN13码 更多... |
|  | |
| bool | UPCA `[get, set]` |
|  | UPCA码 更多... |
|  | |
| bool | UPCE `[get, set]` |
|  | UPCE码 更多... |
|  | |
| bool | ITF25 `[get, set]` |
|  | 交替25码 更多... |
|  | |
| bool | CODE93 `[get, set]` |
|  | CODE93码 更多... |
|  | |
| bool | MATRIX25 `[get, set]` |
|  | MATRIX25码 更多... |
|  | |
| bool | MSI `[get, set]` |
|  | MSI码 更多... |
|  | |
| bool | CHINAPOST `[get, set]` |
|  | CNPOST码 更多... |
|  | |
| bool | CODE11 `[get, set]` |
|  | CODE11码 更多... |
|  | |
| bool | INDUSTRIAL25 `[get, set]` |
|  | IND25码 更多... |
|  | |
| bool | ITF14 `[get, set]` |
|  | ITF14码 更多... |
|  | |
| int | BarCodeNum `[get, set]` |
|  | 条码个数，范围：[1,200] 更多... |
|  | |
| bool | QRCode `[get, set]` |
|  | QR码 更多... |
|  | |
| bool | DMCode `[get, set]` |
|  | DataMatrix码 更多... |
|  | |
| int | LocCodeNum `[get, set]` |
|  | 二维码个数，范围：[1,200] 更多... |
|  | |
| bool | PDF417Code `[get, set]` |
|  | PDF417码 更多... |
|  | |
| int | LocSDCodeNum `[get, set]` |
|  | 堆叠码个数，范围：[1,200] 更多... |
|  | |
| CodePolarityEnum | CodePolarity `[get, set]` |
|  | 极性（弃用） 更多... |
|  | |
| DiscreteFlagEnum | DiscreteFlag `[get, set]` |
|  | 边缘类型（弃用） 更多... |
|  | |
| int | SampleLevel `[get, set]` |
|  | 降采样倍数（弃用），范围：[1,6] , Range:[1,6] 更多... |
|  | |
| MirrorModeEnum | MirrorMode `[get, set]` |
|  | 镜像模式（弃用） 更多... |
|  | |
| DistortionFlagEnum | DistortionFlag `[get, set]` |
|  | QR畸变（弃用） 更多... |
|  | |
| RectangleEnum | Rectangle `[get, set]` |
|  | DM码类型（弃用） 更多... |
|  | |
| int | WaitingTime `[get, set]` |
|  | 超时退出时间，范围：[0,5000] 更多... |
|  | |
| bool | PerfMode `[get, set]` |
|  | 高性能模式 更多... |
|  | |
| bool | ArrangeFlag `[get, set]` |
|  | 码行列号 更多... |
|  | |
| int | ArrangeRowNum `[get, set]` |
|  | 行数量，范围：[1,200] 更多... |
|  | |
| int | ArrangeColumnNum `[get, set]` |
|  | 列数量，范围：[1,200] 更多... |
|  | |
| bool | GradeFlag `[get, set]` |
|  | 码等级 更多... |
|  | |
| StandardTypeEnum | StandardType `[get, set]` |
|  | ISO标准 更多... |
|  | |
| MirrorEnum | Mirror `[get, set]` |
|  | 镜像模式（弃用） 更多... |
|  | |
| ClassificationTypeEnum | ClassificationType `[get, set]` |
|  | 评级处理类型 更多... |
|  | |
| int | Aperture `[get, set]` |
|  | 孔径尺寸，范围：[10,100]（弃用） 更多... |
|  | |
| double | StdAperture `[get, set]` |
|  | 标准孔径，范围：[0.01,100]（弃用） 更多... |
|  | |
| double | SystemMag `[get, set]` |
|  | 成像放大率，范围：[1,10000]（弃用） 更多... |
|  | |
| VerifyLabelTypeEnum | VerifyLabelType `[get, set]` |
|  | 评级模式 更多... |
|  | |
| PolarityEnum | Polarity `[get, set]` |
|  | 极性 更多... |
|  | |
| int | SymbolRows `[get, set]` |
|  | 二维码行数，范围：[10,57] 更多... |
|  | |
| int | SymbolCols `[get, set]` |
|  | 二维码列数，范围：[10,57] 更多... |
|  | |
| EdgeFeatureEnum | EdgeFeature `[get, set]` |
|  | 边缘类型（弃用） 更多... |
|  | |
| bool | DecodeFlag `[get, set]` |
|  | 译码评分 更多... |
|  | |
| bool | EdgeDeterminationFlag `[get, set]` |
|  | 边缘确定度 更多... |
|  | |
| bool | SymbolContrastFlag `[get, set]` |
|  | 符号对比度 更多... |
|  | |
| bool | MinReflectanceFlag `[get, set]` |
|  | 最小反射率 更多... |
|  | |
| bool | MinEdgeContrastFlag `[get, set]` |
|  | 边缘对比度 更多... |
|  | |
| bool | ModulationFlag `[get, set]` |
|  | 模块均匀性 更多... |
|  | |
| bool | DecodabilityFlag `[get, set]` |
|  | 可译码性 更多... |
|  | |
| bool | DefectsFlag `[get, set]` |
|  | 缺陷度 更多... |
|  | |
| bool | QuietZoneFlag `[get, set]` |
|  | 静区（弃用） 更多... |
|  | |
| int | DecodabilityThrA `[get, set]` |
|  | 可译码性A，范围：[0,100] 更多... |
|  | |
| int | DecodabilityThrB `[get, set]` |
|  | 可译码性B，范围：[0,100] 更多... |
|  | |
| int | DecodabilityThrC `[get, set]` |
|  | 可译码性C，范围：[0,100] 更多... |
|  | |
| int | DecodabilityThrD `[get, set]` |
|  | 可译码性D，范围：[0,100] 更多... |
|  | |
| int | DefectsThrA `[get, set]` |
|  | 缺陷度A，范围：[0,100] 更多... |
|  | |
| int | DefectsThrB `[get, set]` |
|  | 缺陷度B，范围：[0,100] 更多... |
|  | |
| int | DefectsThrC `[get, set]` |
|  | 缺陷度C，范围：[0,100] 更多... |
|  | |
| int | DefectsThrD `[get, set]` |
|  | 缺陷度D，范围：[0,100] 更多... |
|  | |
| int | MinReflectanceThrA `[get, set]` |
|  | 最小反射率A，范围：[0,100] 更多... |
|  | |
| int | MinEdgeContrastThrA `[get, set]` |
|  | 边缘对比度A，范围：[0,100] 更多... |
|  | |
| int | ModulationThrA `[get, set]` |
|  | 模块均匀性A，范围：[0,100] 更多... |
|  | |
| int | ModulationThrB `[get, set]` |
|  | 模块均匀性B，范围：[0,100] 更多... |
|  | |
| int | ModulationThrC `[get, set]` |
|  | 模块均匀性C，范围：[0,100] 更多... |
|  | |
| int | ModulationThrD `[get, set]` |
|  | 模块均匀性D，范围：[0,100] 更多... |
|  | |
| int | SymbolContrastThrA `[get, set]` |
|  | 对比度A，范围：[0,100] 更多... |
|  | |
| int | SymbolContrastThrB `[get, set]` |
|  | 对比度B，范围：[0,100] 更多... |
|  | |
| int | SymbolContrastThrC `[get, set]` |
|  | 对比度C，范围：[0,100] 更多... |
|  | |
| int | SymbolContrastThrD `[get, set]` |
|  | 对比度D，范围：[0,100] 更多... |
|  | |
| bool | ApertureEnable `[get, set]` |
|  | 孔径设置（弃用） 更多... |
|  | |
| int | ApertureIn `[get, set]` |
|  | 孔径尺寸，范围：[1,100]（弃用） 更多... |
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

DL读码 GPU参数

## 成员枚举类型说明

## ◆ CodePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CodePolarityEnum | | strong |

极性

| 枚举值 | |
| --- | --- |
| dark | 白底黑码 |
| bright | 黑底白码 |
| both | 任意 |

## ◆ DiscreteFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DiscreteFlagEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| continuous | 连续型 |
| discrete | 离散型 |
| allmode | 兼容模式 |

## ◆ MirrorModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MirrorModeEnum | | strong |

镜像模式

| 枚举值 | |
| --- | --- |
| Off | 非镜像 |
| On | 镜像 |
| Both | 任意 |

## ◆ DistortionFlagEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DistortionFlagEnum | | strong |

QR畸变

| 枚举值 | |
| --- | --- |
| Off | 非畸变 |
| On | 畸变 |

## ◆ RectangleEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum RectangleEnum | | strong |

DM码类型

| 枚举值 | |
| --- | --- |
| Square | 正方形 |
| Rectangle | 长方形 |
| AllMode | 兼容模式 |

## ◆ StandardTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum StandardTypeEnum | | strong |

ISO标准

| 枚举值 | |
| --- | --- |
| ISO15415 | ISO15415 |
| ISO29158 | ISO29158 |

## ◆ MirrorEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MirrorEnum | | strong |

镜像模式

| 枚举值 | |
| --- | --- |
| Off | 非镜像 |
| On | 镜像 |
| Both | 任意 |

## ◆ ClassificationTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ClassificationTypeEnum | | strong |

评级处理类型

| 枚举值 | |
| --- | --- |
| process\_type\_one | 处理类型1 |
| process\_type\_two | 处理类型2 |

## ◆ VerifyLabelTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum VerifyLabelTypeEnum | | strong |

评级模式

| 枚举值 | |
| --- | --- |
| ISO\_Mode | ISO模式 |
| HIK\_Mode | HIK模式 |

## ◆ PolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PolarityEnum | | strong |

极性

| 枚举值 | |
| --- | --- |
| dark | 白底黑码 |
| bright | 黑底白码 |
| both | 任意 |

## ◆ EdgeFeatureEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgeFeatureEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| continuous | 连续型 |
| discrete | 离散型 |

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
| |  | | --- | | CnnCodeRecgRoiManager ModuRoiManager | | get |

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

## ◆ EAN8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EAN8 | | getset |

EAN8码

## ◆ EAN13

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EAN13 | | getset |

EAN13码

## ◆ UPCA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UPCA | | getset |

UPCA码

## ◆ UPCE

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UPCE | | getset |

UPCE码

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

## ◆ MATRIX25

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MATRIX25 | | getset |

MATRIX25码

## ◆ MSI

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MSI | | getset |

MSI码

## ◆ CHINAPOST

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CHINAPOST | | getset |

CNPOST码

## ◆ CODE11

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CODE11 | | getset |

CODE11码

## ◆ INDUSTRIAL25

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool INDUSTRIAL25 | | getset |

IND25码

## ◆ ITF14

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ITF14 | | getset |

ITF14码

## ◆ BarCodeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int BarCodeNum | | getset |

条码个数，范围：[1,200]

## ◆ QRCode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool QRCode | | getset |

QR码

## ◆ DMCode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DMCode | | getset |

DataMatrix码

## ◆ LocCodeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LocCodeNum | | getset |

二维码个数，范围：[1,200]

## ◆ PDF417Code

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PDF417Code | | getset |

PDF417码

## ◆ LocSDCodeNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LocSDCodeNum | | getset |

堆叠码个数，范围：[1,200]

## ◆ CodePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CodePolarityEnum CodePolarity | | getset |

极性（弃用）

## ◆ DiscreteFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DiscreteFlagEnum DiscreteFlag | | getset |

边缘类型（弃用）

## ◆ SampleLevel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SampleLevel | | getset |

降采样倍数（弃用），范围：[1,6] , Range:[1,6]

## ◆ MirrorMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MirrorModeEnum MirrorMode | | getset |

镜像模式（弃用）

## ◆ DistortionFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DistortionFlagEnum DistortionFlag | | getset |

QR畸变（弃用）

## ◆ Rectangle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | RectangleEnum Rectangle | | getset |

DM码类型（弃用）

## ◆ WaitingTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WaitingTime | | getset |

超时退出时间，范围：[0,5000]

## ◆ PerfMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool PerfMode | | getset |

高性能模式

## ◆ ArrangeFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ArrangeFlag | | getset |

码行列号

## ◆ ArrangeRowNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ArrangeRowNum | | getset |

行数量，范围：[1,200]

## ◆ ArrangeColumnNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ArrangeColumnNum | | getset |

列数量，范围：[1,200]

## ◆ GradeFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GradeFlag | | getset |

码等级

## ◆ StandardType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | StandardTypeEnum StandardType | | getset |

ISO标准

## ◆ Mirror

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MirrorEnum Mirror | | getset |

镜像模式（弃用）

## ◆ ClassificationType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ClassificationTypeEnum ClassificationType | | getset |

评级处理类型

## ◆ Aperture

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Aperture | | getset |

孔径尺寸，范围：[10,100]（弃用）

## ◆ StdAperture

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double StdAperture | | getset |

标准孔径，范围：[0.01,100]（弃用）

## ◆ SystemMag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SystemMag | | getset |

成像放大率，范围：[1,10000]（弃用）

## ◆ VerifyLabelType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | VerifyLabelTypeEnum VerifyLabelType | | getset |

评级模式

## ◆ Polarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PolarityEnum Polarity | | getset |

极性

## ◆ SymbolRows

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolRows | | getset |

二维码行数，范围：[10,57]

## ◆ SymbolCols

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolCols | | getset |

二维码列数，范围：[10,57]

## ◆ EdgeFeature

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgeFeatureEnum EdgeFeature | | getset |

边缘类型（弃用）

## ◆ DecodeFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DecodeFlag | | getset |

译码评分

## ◆ EdgeDeterminationFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool EdgeDeterminationFlag | | getset |

边缘确定度

## ◆ SymbolContrastFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SymbolContrastFlag | | getset |

符号对比度

## ◆ MinReflectanceFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MinReflectanceFlag | | getset |

最小反射率

## ◆ MinEdgeContrastFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MinEdgeContrastFlag | | getset |

边缘对比度

## ◆ ModulationFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ModulationFlag | | getset |

模块均匀性

## ◆ DecodabilityFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DecodabilityFlag | | getset |

可译码性

## ◆ DefectsFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DefectsFlag | | getset |

缺陷度

## ◆ QuietZoneFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool QuietZoneFlag | | getset |

静区（弃用）

## ◆ DecodabilityThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DecodabilityThrA | | getset |

可译码性A，范围：[0,100]

## ◆ DecodabilityThrB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DecodabilityThrB | | getset |

可译码性B，范围：[0,100]

## ◆ DecodabilityThrC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DecodabilityThrC | | getset |

可译码性C，范围：[0,100]

## ◆ DecodabilityThrD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DecodabilityThrD | | getset |

可译码性D，范围：[0,100]

## ◆ DefectsThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DefectsThrA | | getset |

缺陷度A，范围：[0,100]

## ◆ DefectsThrB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DefectsThrB | | getset |

缺陷度B，范围：[0,100]

## ◆ DefectsThrC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DefectsThrC | | getset |

缺陷度C，范围：[0,100]

## ◆ DefectsThrD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DefectsThrD | | getset |

缺陷度D，范围：[0,100]

## ◆ MinReflectanceThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinReflectanceThrA | | getset |

最小反射率A，范围：[0,100]

## ◆ MinEdgeContrastThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MinEdgeContrastThrA | | getset |

边缘对比度A，范围：[0,100]

## ◆ ModulationThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModulationThrA | | getset |

模块均匀性A，范围：[0,100]

## ◆ ModulationThrB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModulationThrB | | getset |

模块均匀性B，范围：[0,100]

## ◆ ModulationThrC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModulationThrC | | getset |

模块均匀性C，范围：[0,100]

## ◆ ModulationThrD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModulationThrD | | getset |

模块均匀性D，范围：[0,100]

## ◆ SymbolContrastThrA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolContrastThrA | | getset |

对比度A，范围：[0,100]

## ◆ SymbolContrastThrB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolContrastThrB | | getset |

对比度B，范围：[0,100]

## ◆ SymbolContrastThrC

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolContrastThrC | | getset |

对比度C，范围：[0,100]

## ◆ SymbolContrastThrD

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SymbolContrastThrD | | getset |

对比度D，范围：[0,100]

## ◆ ApertureEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ApertureEnable | | getset |

孔径设置（弃用）

## ◆ ApertureIn

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ApertureIn | | getset |

孔径尺寸，范围：[1,100]（弃用）

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
