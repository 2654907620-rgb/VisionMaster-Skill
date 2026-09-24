<!-- src:class_i_m_v_s_img_stitch_calib_modu_cs_1_1_img_stitch_calib_param.html -->
<!-- path:接口函数 > 图像处理 > 图像拼接 > ImgStitchCalibParam -->
# ImgStitchCalibParam类 参考 图像处理 » 图像拼接

图像拼接参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | InputTypeEnum {     SingleSource = 0x1,     MultipleSource = 0x2   } |
|  | 输入方式 更多... |
|  | |
| enum | StitchTypeEnum {     ModelStitch = 0x1,     HardStitch = 0x2   } |
|  | 拼接类型 更多... |
|  | |
| enum | StitchDirectionEnum {     XDirection = 0x1,     YDirection = 0x2   } |
|  | 拼接方向 更多... |
|  | |
| enum | MergeTypeEnum {     MergeMean = 0x1,     MergeMin = 0x2,     MergeMax = 0x3,     MergeUncover = 0x4   } |
|  | 融合模式 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoClearImage () |
|  | 清空图像 更多... |
|  | |
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

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage0 `[set]` |
|  | 输入图像0 更多... |
|  | |
| InputTypeEnum | InputType `[get, set]` |
|  | 输入方式 更多... |
|  | |
| StitchTypeEnum | StitchType `[get, set]` |
|  | 拼接类型 更多... |
|  | |
| int | ImageNum `[get, set]` |
|  | 拼接数目，范围：[2,100] 更多... |
|  | |
| int | HardImageNum `[get, set]` |
|  | 拼接数目，范围：[2,20] 更多... |
|  | |
| string | ImageMatrix `[get, set]` |
|  | 拼接方式，设置一个格式为mXn的字符串，m为行数，n为列数 更多... |
|  | |
| StitchDirectionEnum | StitchDirection `[get, set]` |
|  | 拼接方向 更多... |
|  | |
| MergeTypeEnum | MergeType `[get, set]` |
|  | 融合模式 更多... |
|  | |
| int | CutRatio `[get, set]` |
|  | 裁剪参数，范围：[0,25]（弃用） 更多... |
|  | |
| int | CutRatioX `[get, set]` |
|  | 裁剪X方向，范围：[0,25] 更多... |
|  | |
| int | CutRatioY `[get, set]` |
|  | 裁剪Y方向，范围：[0,25] 更多... |
|  | |
| bool | AutoClear `[get, set]` |
|  | 自动清空 更多... |
|  | |
| bool | AutoFill `[get, set]` |
|  | 自动填充 更多... |
|  | |

## 详细描述

图像拼接参数

## 成员枚举类型说明

## ◆ InputTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InputTypeEnum | | strong |

输入方式

| 枚举值 | |
| --- | --- |
| SingleSource | 单来源 |
| MultipleSource | 多来源 |

## ◆ StitchTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum StitchTypeEnum | | strong |

拼接类型

| 枚举值 | |
| --- | --- |
| ModelStitch | 模型拼接 |
| HardStitch | 硬拼接 |

## ◆ StitchDirectionEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum StitchDirectionEnum | | strong |

拼接方向

| 枚举值 | |
| --- | --- |
| XDirection | X方向 |
| YDirection | Y方向 |

## ◆ MergeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MergeTypeEnum | | strong |

融合模式

| 枚举值 | |
| --- | --- |
| MergeMean | 均值融合 |
| MergeMin | 最小值融合 |
| MergeMax | 最大值融合 |
| MergeUncover | 接尾融合 |

## 成员函数说明

## ◆ DoClearImage()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoClearImage | ( |  | ) |  |

清空图像

## 属性说明

## ◆ InputImage0

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage0 | | set |

输入图像0

**备注**

仅当次执行起效

## ◆ InputType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InputTypeEnum InputType | | getset |

输入方式

## ◆ StitchType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | StitchTypeEnum StitchType | | getset |

拼接类型

## ◆ ImageNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageNum | | getset |

拼接数目，范围：[2,100]

## ◆ HardImageNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HardImageNum | | getset |

拼接数目，范围：[2,20]

## ◆ ImageMatrix

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string ImageMatrix | | getset |

拼接方式，设置一个格式为mXn的字符串，m为行数，n为列数

## ◆ StitchDirection

|  |  |  |
| --- | --- | --- |
| |  | | --- | | StitchDirectionEnum StitchDirection | | getset |

拼接方向

## ◆ MergeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MergeTypeEnum MergeType | | getset |

融合模式

## ◆ CutRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CutRatio | | getset |

裁剪参数，范围：[0,25]（弃用）

## ◆ CutRatioX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CutRatioX | | getset |

裁剪X方向，范围：[0,25]

## ◆ CutRatioY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CutRatioY | | getset |

裁剪Y方向，范围：[0,25]

## ◆ AutoClear

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AutoClear | | getset |

自动清空

## ◆ AutoFill

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AutoFill | | getset |

自动填充
