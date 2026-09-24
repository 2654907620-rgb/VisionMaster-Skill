<!-- src:class_translation_calib_modu_cs_1_1_translation_calib_param.html -->
<!-- path:接口函数 > 标定 > 平移旋转标定 > TranslationCalibParam -->
# TranslationCalibParam类 参考 标定 » 平移旋转标定

平移旋转标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CalibTypeEnum {     TransCalib = 0x0,     TransAndRotateCalib = 0x1   } |
|  | 标定类型 更多... |
|  | |
| enum | CalibPointGetEnum {     TriggerAcquisition = 0x0,     ManualInput = 0x1   } |
|  | 标定点获取 更多... |
|  | |
| enum | CameraModeEnum {     CameraStatic = 0x1,     CameraMove = 0x3   } |
|  | 相机模式 更多... |
|  | |
| enum | HomoFreedomEnum {     Perspective = 0x1,     Affine = 0x2,     Similarity = 0x3   } |
|  | 自由度 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoClearPoint () |
|  | 清空标定点 更多... |
|  | |
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
| List< PointF > | ImagePoint `[set]` |
|  | 图像点 更多... |
|  | |
| List< PointF > | PhysicalPoint `[set]` |
|  | 物理点 更多... |
|  | |
| List< float > | ImageRotateAngle `[set]` |
|  | 图像角度 更多... |
|  | |
| List< float > | WorldRotateAngle `[set]` |
|  | 物理角度 更多... |
|  | |
| List< string > | Trigger `[set]` |
|  | 外部输入字符 更多... |
|  | |
| List< string > | TeachFlag `[set]` |
|  | 外部触发字符 更多... |
|  | |
| CalibTypeEnum | CalibType `[get, set]` |
|  | 标定类型 更多... |
|  | |
| CalibPointGetEnum | CalibPointGet `[get, set]` |
|  | 标定点获取 更多... |
|  | |
| CameraModeEnum | CameraMode `[get, set]` |
|  | 相机模式 更多... |
|  | |
| HomoFreedomEnum | HomoFreedom `[get, set]` |
|  | 自由度 更多... |
|  | |
| int | CalibPointTotalNum `[get, set]` |
|  | 平移次数，范围：[4,16] 更多... |
|  | |
| int | RotPointTotalNum `[get, set]` |
|  | 旋转次数，范围：[0,16] 更多... |
|  | |
| bool | UnionCalibEnable `[get, set]` |
|  | 组合标定 更多... |
|  | |
| bool | TeachEnable `[get, set]` |
|  | 示教 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |

## 详细描述

平移旋转标定参数

## 成员枚举类型说明

## ◆ CalibTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibTypeEnum | | strong |

标定类型

| 枚举值 | |
| --- | --- |
| TransCalib | 平移标定 |
| TransAndRotateCalib | 平移旋转标定 |

## ◆ CalibPointGetEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibPointGetEnum | | strong |

标定点获取

| 枚举值 | |
| --- | --- |
| TriggerAcquisition | 触发获取 |
| ManualInput | 手动输入 |

## ◆ CameraModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CameraModeEnum | | strong |

相机模式

| 枚举值 | |
| --- | --- |
| CameraStatic | 相机静止 |
| CameraMove | 相机运动 |

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

## 成员函数说明

## ◆ DoClearPoint()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoClearPoint | ( |  | ) |  |

清空标定点

## ◆ DoSaveFile()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int DoSaveFile | ( | string | *value* | ) |  |

生成标定文件

## 属性说明

## ◆ ImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> ImagePoint | | set |

图像点

**备注**

仅当次执行起效

## ◆ PhysicalPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> PhysicalPoint | | set |

物理点

**备注**

仅当次执行起效

## ◆ ImageRotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ImageRotateAngle | | set |

图像角度

**备注**

仅当次执行起效

## ◆ WorldRotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> WorldRotateAngle | | set |

物理角度

**备注**

仅当次执行起效

## ◆ Trigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> Trigger | | set |

外部输入字符

**备注**

仅当次执行起效

## ◆ TeachFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> TeachFlag | | set |

外部触发字符

**备注**

仅当次执行起效

## ◆ CalibType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibTypeEnum CalibType | | getset |

标定类型

## ◆ CalibPointGet

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibPointGetEnum CalibPointGet | | getset |

标定点获取

## ◆ CameraMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CameraModeEnum CameraMode | | getset |

相机模式

## ◆ HomoFreedom

|  |  |  |
| --- | --- | --- |
| |  | | --- | | HomoFreedomEnum HomoFreedom | | getset |

自由度

## ◆ CalibPointTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibPointTotalNum | | getset |

平移次数，范围：[4,16]

## ◆ RotPointTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotPointTotalNum | | getset |

旋转次数，范围：[0,16]

## ◆ UnionCalibEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UnionCalibEnable | | getset |

组合标定

## ◆ TeachEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TeachEnable | | getset |

示教

## ◆ RefreshFileEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RefreshFileEnable | | getset |

更新文件

## ◆ CalibPathName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CalibPathName | | getset |

标定文件路径
