<!-- src:class_i_m_v_s_camera_map_modu_cs_1_1_camera_map_param.html -->
<!-- path:接口函数 > 标定 > 相机映射 > CameraMapParam -->
# CameraMapParam类 参考 标定 » 相机映射

相机映射参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | HomoFreedomEnum {     Perspective = 0x1,     Affine = 0x2,     Similarity = 0x3   } |
|  | 自由度 更多... |
|  | |
| enum | WeightFunEnum {     LeastSqure = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 权重函数 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoSaveFile (string value) |
|  | 生成标定文件 更多... |
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
| List< PointF > | TargetPointInput1 `[set]` |
|  | 目标点输入1 更多... |
|  | |
| List< PointF > | ObjectPointInput1 `[set]` |
|  | 对象点输入1 更多... |
|  | |
| List< PointF > | TargetPointInput2 `[set]` |
|  | 目标点输入2 更多... |
|  | |
| List< PointF > | ObjectPointInput2 `[set]` |
|  | 对象点输入2 更多... |
|  | |
| List< PointF > | TargetPointInput3 `[set]` |
|  | 目标点输入3 更多... |
|  | |
| List< PointF > | ObjectPointInput3 `[set]` |
|  | 对象点输入3 更多... |
|  | |
| List< PointF > | TargetPointInput4 `[set]` |
|  | 目标点输入4 更多... |
|  | |
| List< PointF > | ObjectPointInput4 `[set]` |
|  | 对象点输入4 更多... |
|  | |
| List< PointF > | TargetPointInput5 `[set]` |
|  | 目标点输入5 更多... |
|  | |
| List< PointF > | ObjectPointInput5 `[set]` |
|  | 对象点输入5 更多... |
|  | |
| List< PointF > | TargetPointInput6 `[set]` |
|  | 目标点输入6 更多... |
|  | |
| List< PointF > | ObjectPointInput6 `[set]` |
|  | 对象点输入6 更多... |
|  | |
| List< PointF > | TargetPointInput7 `[set]` |
|  | 目标点输入7 更多... |
|  | |
| List< PointF > | ObjectPointInput7 `[set]` |
|  | 对象点输入7 更多... |
|  | |
| List< PointF > | TargetPointInput8 `[set]` |
|  | 目标点输入8 更多... |
|  | |
| List< PointF > | ObjectPointInput8 `[set]` |
|  | 对象点输入8 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| HomoFreedomEnum | HomoFreedom `[get, set]` |
|  | 自由度 更多... |
|  | |
| WeightFunEnum | WeightFun `[get, set]` |
|  | 权重函数 更多... |
|  | |
| int | WeightFactor `[get, set]` |
|  | 权重系数，范围：[1,200] 更多... |
|  | |

## 详细描述

相机映射参数

## 成员枚举类型说明

## ◆ HomoFreedomEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum HomoFreedomEnum | | strong |

自由度

| 枚举值 | |
| --- | --- |
| Perspective | 缩放、旋转、纵横比、倾斜、平移及透射 |
| Affine | 缩放、旋转、纵横比、倾斜及平移 |
| Similarity | 缩放、旋转及平移 |

## ◆ WeightFunEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum WeightFunEnum | | strong |

权重函数

| 枚举值 | |
| --- | --- |
| LeastSqure | 最小二乘 |
| Huber | Huber |
| Tukey | Tukey |

## 成员函数说明

## ◆ DoSaveFile()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int DoSaveFile | ( | string | *value* | ) |  |

生成标定文件

## 属性说明

## ◆ TargetPointInput1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput1 | | set |

目标点输入1

**备注**

仅当次执行起效

## ◆ ObjectPointInput1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput1 | | set |

对象点输入1

**备注**

仅当次执行起效

## ◆ TargetPointInput2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput2 | | set |

目标点输入2

**备注**

仅当次执行起效

## ◆ ObjectPointInput2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput2 | | set |

对象点输入2

**备注**

仅当次执行起效

## ◆ TargetPointInput3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput3 | | set |

目标点输入3

**备注**

仅当次执行起效

## ◆ ObjectPointInput3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput3 | | set |

对象点输入3

**备注**

仅当次执行起效

## ◆ TargetPointInput4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput4 | | set |

目标点输入4

**备注**

仅当次执行起效

## ◆ ObjectPointInput4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput4 | | set |

对象点输入4

**备注**

仅当次执行起效

## ◆ TargetPointInput5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput5 | | set |

目标点输入5

**备注**

仅当次执行起效

## ◆ ObjectPointInput5

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput5 | | set |

对象点输入5

**备注**

仅当次执行起效

## ◆ TargetPointInput6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput6 | | set |

目标点输入6

**备注**

仅当次执行起效

## ◆ ObjectPointInput6

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput6 | | set |

对象点输入6

**备注**

仅当次执行起效

## ◆ TargetPointInput7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput7 | | set |

目标点输入7

**备注**

仅当次执行起效

## ◆ ObjectPointInput7

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput7 | | set |

对象点输入7

**备注**

仅当次执行起效

## ◆ TargetPointInput8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TargetPointInput8 | | set |

目标点输入8

**备注**

仅当次执行起效

## ◆ ObjectPointInput8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ObjectPointInput8 | | set |

对象点输入8

**备注**

仅当次执行起效

## ◆ CalibPathName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPathName | | getset |

标定文件路径

## ◆ RefreshFileEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RefreshFileEnable | | getset |

更新文件

## ◆ HomoFreedom

|  |  |  |
| --- | --- | --- |
| |  | | --- | | HomoFreedomEnum HomoFreedom | | getset |

自由度

## ◆ WeightFun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WeightFunEnum WeightFun | | getset |

权重函数

## ◆ WeightFactor

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int WeightFactor | | getset |

权重系数，范围：[1,200]
