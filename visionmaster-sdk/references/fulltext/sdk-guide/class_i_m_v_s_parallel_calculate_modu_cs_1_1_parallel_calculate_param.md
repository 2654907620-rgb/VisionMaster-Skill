<!-- src:class_i_m_v_s_parallel_calculate_modu_cs_1_1_parallel_calculate_param.html -->
<!-- path:接口函数 > 定位 > 平行线计算 > ParallelCalculateParam -->
# ParallelCalculateParam类 参考 定位 » 平行线计算

平行线计算参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | WayToChooseEnum {     PointLine = 0x0,     DistanceLine = 0x1   } |
|  | 方式选择 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InputPoint `[set]` |
|  | 输入点 更多... |
|  | |
| List< Line > | InputLine `[set]` |
|  | 输入直线 更多... |
|  | |
| WayToChooseEnum | WayToChoose `[get, set]` |
|  | 方式选择 更多... |
|  | |
| double | LineLength `[get, set]` |
|  | 间距，范围：[0,10000] 更多... |
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

平行线计算参数

## 成员枚举类型说明

## ◆ WayToChooseEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum WayToChooseEnum | | strong |

方式选择

| 枚举值 | |
| --- | --- |
| PointLine | 过直线外一点 |
| DistanceLine | 与直线相距一定距离 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputPoint | | set |

输入点

**备注**

仅当次执行起效

## ◆ InputLine

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<Line> InputLine | | set |

输入直线

**备注**

仅当次执行起效

## ◆ WayToChoose

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WayToChooseEnum WayToChoose | | getset |

方式选择

## ◆ LineLength

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double LineLength | | getset |

间距，范围：[0,10000]
