<!-- src:class_i_m_v_s_cnn_classify_modu_cs_1_1_cnn_classify_param.html -->
<!-- path:接口函数 > 深度学习 > DL分类GPU > CnnClassifyParam -->
# CnnClassifyParam类 参考 深度学习 » DL分类GPU

DL分类 GPU参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| CnnClassifyRoiManager | ModuRoiManager `[get]` |
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
| int | TopClassK `[get, set]` |
|  | 前K个类别，范围：[1,100] 更多... |
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
|  | 个数范围，范围：[1,99999] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 个数范围，范围：[1,99999] 更多... |
|  | |
| bool | ProbLimitEnable `[get, set]` |
|  | 概率判断 更多... |
|  | |
| double | ProbLimitLow `[get, set]` |
|  | 概率范围，范围：[0.0,1.0] 更多... |
|  | |
| double | ProbLimitHigh `[get, set]` |
|  | 概率范围，范围：[0.0,1.0] 更多... |
|  | |
| bool | LabelLimitEnable `[get, set]` |
|  | 类别号判断 更多... |
|  | |
| int | LabelLimitLow `[get, set]` |
|  | 类别号范围，范围：[0,1000] 更多... |
|  | |
| int | LabelLimitHigh `[get, set]` |
|  | 类别号范围，范围：[0,1000] 更多... |
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

DL分类 GPU参数

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
| |  | | --- | | CnnClassifyRoiManager ModuRoiManager | | get |

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

## ◆ TopClassK

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TopClassK | | getset |

前K个类别，范围：[1,100]

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

个数范围，范围：[1,99999]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

个数范围，范围：[1,99999]

## ◆ ProbLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ProbLimitEnable | | getset |

概率判断

## ◆ ProbLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProbLimitLow | | getset |

概率范围，范围：[0.0,1.0]

## ◆ ProbLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ProbLimitHigh | | getset |

概率范围，范围：[0.0,1.0]

## ◆ LabelLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool LabelLimitEnable | | getset |

类别号判断

## ◆ LabelLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LabelLimitLow | | getset |

类别号范围，范围：[0,1000]

## ◆ LabelLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LabelLimitHigh | | getset |

类别号范围，范围：[0,1000]

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
