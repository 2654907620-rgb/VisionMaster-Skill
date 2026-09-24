<!-- src:class_i_m_v_s_line_edge_insp_modu_cs_1_1_line_edge_insp_param.html -->
<!-- path:接口函数 > 缺陷检测 > 直线边缘缺陷检测 > LineEdgeInspParam -->
# LineEdgeInspParam类 参考 缺陷检测 » 直线边缘缺陷检测

直线边缘缺陷检测参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FindModeEnum {     Best = 0x1,     First = 0x2,     Last = 0x3   } |
|  | 边缘类型 更多... |
|  | |
| enum | EdgePolarityEnum {     B2W = 0x1,     W2B = 0x2,     All = 0x3   } |
|  | 边缘极性 更多... |
|  | |
| enum | FlawPolarityEnableEnum {     All = 0x0,     RightBottom = 0x1,     LeftTop = 0x2   } |
|  | 缺陷极性 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< Line > | InputLine `[set]` |
|  | 输入直线 更多... |
|  | |
| bool | StandardInput `[get, set]` |
|  | 标准输入 更多... |
|  | |
| LineEdgeInspRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| FindModeEnum | FindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | HalfKernelSize `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | EdgeStrength `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| int | CaliperHeight `[get, set]` |
|  | 卡尺高度，范围：[1,1500] 更多... |
|  | |
| int | CaliperWidth `[get, set]` |
|  | 卡尺宽度，范围：[1,500] 更多... |
|  | |
| int | CaliperDistTraj `[get, set]` |
|  | 卡尺间距，范围：[1,1000] 更多... |
|  | |
| FlawPolarityEnableEnum | FlawPolarityEnable `[get, set]` |
|  | 缺陷极性 更多... |
|  | |
| int | RoughMinDis `[get, set]` |
|  | 缺陷距离阈值，范围：[0,10000] 更多... |
|  | |
| bool | SizeEnable `[get, set]` |
|  | 缺陷尺寸使能 更多... |
|  | |
| int | RoughMinSize `[get, set]` |
|  | 缺陷尺寸阈值，范围：[0,100000] 更多... |
|  | |
| bool | AreaEnable `[get, set]` |
|  | 缺陷面积使能 更多... |
|  | |
| int | RoughMinArea `[get, set]` |
|  | 缺陷面积阈值，范围：[0,1000000] 更多... |
|  | |
| int | LineCaliperNum `[get, set]` |
|  | 卡尺数量，范围：[2,1000] 更多... |
|  | |
| int | FitRejectNum `[get, set]` |
|  | 剔除点数，范围：[0,998] 更多... |
|  | |
| int | FitRejectDist `[get, set]` |
|  | 剔除阈值，范围：[1,15000] 更多... |
|  | |
| int | TrackDistTol `[get, set]` |
|  | 追踪容忍度，范围：[0,100] 更多... |
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

直线边缘缺陷检测参数

## 成员枚举类型说明

## ◆ FindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| First | 第一条 |
| Last | 最后一条 |

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| B2W | 从黑到白 |
| W2B | 从白到黑 |
| All | 任意极性 |

## ◆ FlawPolarityEnableEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FlawPolarityEnableEnum | | strong |

缺陷极性

| 枚举值 | |
| --- | --- |
| All | 轨迹两侧缺陷 |
| RightBottom | 轨迹右侧缺陷 |
| LeftTop | 轨迹左侧缺陷 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine | | set |

输入直线

**备注**

仅当次执行起效

## ◆ StandardInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool StandardInput | | getset |

标准输入

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | LineEdgeInspRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ FindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FindModeEnum FindMode | | getset |

边缘类型

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘极性

## ◆ HalfKernelSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int HalfKernelSize | | getset |

滤波尺寸，范围：[1,50]

## ◆ EdgeStrength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeStrength | | getset |

边缘阈值，范围：[1,255]

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

## ◆ CaliperDistTraj

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CaliperDistTraj | | getset |

卡尺间距，范围：[1,1000]

## ◆ FlawPolarityEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FlawPolarityEnableEnum FlawPolarityEnable | | getset |

缺陷极性

## ◆ RoughMinDis

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMinDis | | getset |

缺陷距离阈值，范围：[0,10000]

## ◆ SizeEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SizeEnable | | getset |

缺陷尺寸使能

## ◆ RoughMinSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMinSize | | getset |

缺陷尺寸阈值，范围：[0,100000]

## ◆ AreaEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AreaEnable | | getset |

缺陷面积使能

## ◆ RoughMinArea

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RoughMinArea | | getset |

缺陷面积阈值，范围：[0,1000000]

## ◆ LineCaliperNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineCaliperNum | | getset |

卡尺数量，范围：[2,1000]

## ◆ FitRejectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitRejectNum | | getset |

剔除点数，范围：[0,998]

## ◆ FitRejectDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitRejectDist | | getset |

剔除阈值，范围：[1,15000]

## ◆ TrackDistTol

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TrackDistTol | | getset |

追踪容忍度，范围：[0,100]
