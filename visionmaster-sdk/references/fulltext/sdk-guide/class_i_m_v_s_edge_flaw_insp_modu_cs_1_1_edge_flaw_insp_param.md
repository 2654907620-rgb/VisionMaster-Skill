<!-- src:class_i_m_v_s_edge_flaw_insp_modu_cs_1_1_edge_flaw_insp_param.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘模型缺陷检测 > EdgeFlawInspParam -->
# EdgeFlawInspParam类 参考 缺陷检测 » 边缘模型缺陷检测

边缘模型缺陷检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EdgePointFindModeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型 更多... |
|  | |
| enum | EdgePointPolarityEnum {     B2W = 0x1,     W2B = 0x2,     All = 0x3   } |
|  | 边缘极性 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| EdgePointFindModeEnum | EdgePointFindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePointPolarityEnum | EdgePointPolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘强度，范围：[1,255] 更多... |
|  | |
| int | CaliperHeight `[get, set]` |
|  | 卡尺高度，范围：[1,1500] 更多... |
|  | |
| int | CaliperWidth `[get, set]` |
|  | 卡尺宽度，范围：[1,500] 更多... |
|  | |
| int | LenThresh `[get, set]` |
|  | 缺陷长度阈值，范围：[1,10000] 更多... |
|  | |
| bool | OffsetEnable `[get, set]` |
|  | 位置缺陷使能 更多... |
|  | |
| int | OffsetThresh `[get, set]` |
|  | 位置偏移阈值，范围：[1,10000] 更多... |
|  | |
| bool | CrackEnable `[get, set]` |
|  | 断裂缺陷使能 更多... |
|  | |
| bool | GradEnable `[get, set]` |
|  | 阶梯缺陷使能 更多... |
|  | |
| int | GradThresh `[get, set]` |
|  | 阶梯偏离高度，范围：[1,10000] 更多... |
|  | |
| int | GradLen `[get, set]` |
|  | 最小阶梯长度，范围：[1,10000] 更多... |
|  | |
| bool | GrayTrackEnable `[get, set]` |
|  | 灰度辅助检测 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | GrayTrackDistol `[get, set]` |
|  | 追踪容忍，范围：[0,100] 更多... |
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

边缘模型缺陷检测参数

## 成员枚举类型说明

## ◆ EdgePointFindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePointFindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePointPolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePointPolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| B2W | 从黑到白 |
| W2B | 从白到黑 |
| All | 任意极性 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ EdgePointFindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePointFindModeEnum EdgePointFindMode | | getset |

边缘类型

## ◆ EdgePointPolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePointPolarityEnum EdgePointPolarity | | getset |

边缘极性

## ◆ EdgeStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeStrength | | getset |

边缘强度，范围：[1,255]

## ◆ CaliperHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperHeight | | getset |

卡尺高度，范围：[1,1500]

## ◆ CaliperWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperWidth | | getset |

卡尺宽度，范围：[1,500]

## ◆ LenThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LenThresh | | getset |

缺陷长度阈值，范围：[1,10000]

## ◆ OffsetEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OffsetEnable | | getset |

位置缺陷使能

## ◆ OffsetThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OffsetThresh | | getset |

位置偏移阈值，范围：[1,10000]

## ◆ CrackEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CrackEnable | | getset |

断裂缺陷使能

## ◆ GradEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GradEnable | | getset |

阶梯缺陷使能

## ◆ GradThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GradThresh | | getset |

阶梯偏离高度，范围：[1,10000]

## ◆ GradLen

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GradLen | | getset |

最小阶梯长度，范围：[1,10000]

## ◆ GrayTrackEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GrayTrackEnable | | getset |

灰度辅助检测

## ◆ HalfKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalfKernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ GrayTrackDistol

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayTrackDistol | | getset |

追踪容忍，范围：[0,100]
