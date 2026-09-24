<!-- src:class_i_m_v_s_target_track_modu_cs_1_1_target_track_param.html -->
<!-- path:接口函数 > 定位 > 目标跟踪 > TargetTrackParam -->
# TargetTrackParam类 参考 定位 » 目标跟踪

目标跟踪参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< RectBox > | InputBOX `[set]` |
|  | 输入Box 更多... |
|  | |
| double | TrackSpeedX `[get, set]` |
|  | X方向速度，范围：[0.01,2.00] 更多... |
|  | |
| double | TrackSpeedY `[get, set]` |
|  | Y方向速度，范围：[0.01,2.00] 更多... |
|  | |
| int | FrameNum `[get, set]` |
|  | 允许缺帧数，范围：[0,5] 更多... |
|  | |
| int | TrackOverlap `[get, set]` |
|  | 轨迹重叠率，范围：[1,100] 更多... |
|  | |
| bool | CountNumLimitEnable `[get, set]` |
|  | 计数总数判断 更多... |
|  | |
| int | CountNumLimitLow `[get, set]` |
|  | 计数总数范围，范围：[0,99999] 更多... |
|  | |
| int | CountNumLimitHigh `[get, set]` |
|  | 计数总数范围，范围：[0,99999] 更多... |
|  | |
| bool | ObjNumLimitEnable `[get, set]` |
|  | 目标数判断 更多... |
|  | |
| int | ObjNumLimitLow `[get, set]` |
|  | 目标数范围，范围：[0,99999] 更多... |
|  | |
| int | ObjNumLimitHigh `[get, set]` |
|  | 目标数范围，范围：[0,99999] 更多... |
|  | |
| bool | SingleCountLimitEnable `[get, set]` |
|  | 单帧计数判断 更多... |
|  | |
| int | SingleCountLimitLow `[get, set]` |
|  | 单帧计数范围，范围：[0,99999] 更多... |
|  | |
| int | SingleCountLimitHigh `[get, set]` |
|  | 单帧计数范围，范围：[0,99999] 更多... |
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

目标跟踪参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputBOX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> InputBOX | | set |

输入Box

**备注**

仅当次执行起效

## ◆ TrackSpeedX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double TrackSpeedX | | getset |

X方向速度，范围：[0.01,2.00]

## ◆ TrackSpeedY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double TrackSpeedY | | getset |

Y方向速度，范围：[0.01,2.00]

## ◆ FrameNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FrameNum | | getset |

允许缺帧数，范围：[0,5]

## ◆ TrackOverlap

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TrackOverlap | | getset |

轨迹重叠率，范围：[1,100]

## ◆ CountNumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CountNumLimitEnable | | getset |

计数总数判断

## ◆ CountNumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountNumLimitLow | | getset |

计数总数范围，范围：[0,99999]

## ◆ CountNumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CountNumLimitHigh | | getset |

计数总数范围，范围：[0,99999]

## ◆ ObjNumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ObjNumLimitEnable | | getset |

目标数判断

## ◆ ObjNumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjNumLimitLow | | getset |

目标数范围，范围：[0,99999]

## ◆ ObjNumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ObjNumLimitHigh | | getset |

目标数范围，范围：[0,99999]

## ◆ SingleCountLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SingleCountLimitEnable | | getset |

单帧计数判断

## ◆ SingleCountLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SingleCountLimitLow | | getset |

单帧计数范围，范围：[0,99999]

## ◆ SingleCountLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SingleCountLimitHigh | | getset |

单帧计数范围，范围：[0,99999]
