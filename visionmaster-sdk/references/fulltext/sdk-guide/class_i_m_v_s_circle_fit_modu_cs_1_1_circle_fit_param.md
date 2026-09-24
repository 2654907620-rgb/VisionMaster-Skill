<!-- src:class_i_m_v_s_circle_fit_modu_cs_1_1_circle_fit_param.html -->
<!-- path:接口函数 > 图形生成 > 圆拟合 > CircleFitParam -->
# CircleFitParam类 参考 图形生成 » 圆拟合

圆拟合参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | InitTypeEnum {     Global = 0x1,     Exhaustion = 0x2   } |
|  | 初始化类型 更多... |
|  | |
| enum | WeightFuncEnum {     LeastSquare = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 权重函数 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | InputFittingPoint `[set]` |
|  | 输入拟合点 更多... |
|  | |
| int | RejectNum `[get, set]` |
|  | 剔除点数，范围：[0,100] 更多... |
|  | |
| int | RejectDist `[get, set]` |
|  | 剔除距离，范围：[1,1000] 更多... |
|  | |
| InitTypeEnum | InitType `[get, set]` |
|  | 初始化类型 更多... |
|  | |
| WeightFuncEnum | WeightFunc `[get, set]` |
|  | 权重函数 更多... |
|  | |
| int | MaxIters `[get, set]` |
|  | 最大迭代次数，范围：[1,100] 更多... |
|  | |
| bool | NumLimitEnable `[get, set]` |
|  | 匹配点数判断 更多... |
|  | |
| int | NumLimitLow `[get, set]` |
|  | 拟合点数范围，范围：[0,100] 更多... |
|  | |
| int | NumLimitHigh `[get, set]` |
|  | 拟合点数范围，范围：[0,100] 更多... |
|  | |
| bool | RadiusLimitEnable `[get, set]` |
|  | 半径判断 更多... |
|  | |
| double | RadiusLimitLow `[get, set]` |
|  | 半径范围，范围：[0,99999] 更多... |
|  | |
| double | RadiusLimitHigh `[get, set]` |
|  | 半径范围，范围：[0,99999] 更多... |
|  | |
| bool | CenterXLimitEnable `[get, set]` |
|  | 中心X判断 更多... |
|  | |
| double | CenterXLimitLow `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterXLimitHigh `[get, set]` |
|  | 中心X范围，范围：[-99999,99999] 更多... |
|  | |
| bool | CenterYLimitEnable `[get, set]` |
|  | 中心Y判断 更多... |
|  | |
| double | CenterYLimitLow `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| double | CenterYLimitHigh `[get, set]` |
|  | 中心Y范围，范围：[-99999,99999] 更多... |
|  | |
| bool | ScoreLimitEnable `[get, set]` |
|  | 拟合误差判断 更多... |
|  | |
| double | ScoreLimitLow `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
|  | |
| double | ScoreLimitHigh `[get, set]` |
|  | 拟合误差范围，范围：[0,9999] 更多... |
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

圆拟合参数

## 成员枚举类型说明

## ◆ InitTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum InitTypeEnum | | strong |

初始化类型

| 枚举值 | |
| --- | --- |
| Global | 全局法 |
| Exhaustion | 局部最优 |

## ◆ WeightFuncEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum WeightFuncEnum | | strong |

权重函数

| 枚举值 | |
| --- | --- |
| LeastSquare | 最小二乘 |
| Huber | Huber函数 |
| Tukey | Tukey函数 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputFittingPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> InputFittingPoint | | set |

输入拟合点

**备注**

仅当次执行起效

## ◆ RejectNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectNum | | getset |

剔除点数，范围：[0,100]

## ◆ RejectDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RejectDist | | getset |

剔除距离，范围：[1,1000]

## ◆ InitType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InitTypeEnum InitType | | getset |

初始化类型

## ◆ WeightFunc

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WeightFuncEnum WeightFunc | | getset |

权重函数

## ◆ MaxIters

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxIters | | getset |

最大迭代次数，范围：[1,100]

## ◆ NumLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool NumLimitEnable | | getset |

匹配点数判断

## ◆ NumLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitLow | | getset |

拟合点数范围，范围：[0,100]

## ◆ NumLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumLimitHigh | | getset |

拟合点数范围，范围：[0,100]

## ◆ RadiusLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RadiusLimitEnable | | getset |

半径判断

## ◆ RadiusLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RadiusLimitLow | | getset |

半径范围，范围：[0,99999]

## ◆ RadiusLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double RadiusLimitHigh | | getset |

半径范围，范围：[0,99999]

## ◆ CenterXLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterXLimitEnable | | getset |

中心X判断

## ◆ CenterXLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitLow | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterXLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterXLimitHigh | | getset |

中心X范围，范围：[-99999,99999]

## ◆ CenterYLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CenterYLimitEnable | | getset |

中心Y判断

## ◆ CenterYLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitLow | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ CenterYLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double CenterYLimitHigh | | getset |

中心Y范围，范围：[-99999,99999]

## ◆ ScoreLimitEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ScoreLimitEnable | | getset |

拟合误差判断

## ◆ ScoreLimitLow

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitLow | | getset |

拟合误差范围，范围：[0,9999]

## ◆ ScoreLimitHigh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScoreLimitHigh | | getset |

拟合误差范围，范围：[0,9999]
