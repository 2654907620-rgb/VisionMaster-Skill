<!-- src:class_i_m_v_s_n_point_calib_modu_cs_1_1_n_point_calib_param.html -->
<!-- path:接口函数 > 标定 > N点标定 > NPointCalibParam -->
# NPointCalibParam类 参考 标定 » N点标定

N点标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | CalibPointGetEnum {     TriggerAcquisition = 0x0,     ManualInput = 0x1   } |
|  | 标定点获取 更多... |
|  | |
| enum | MoveFirstTypeEnum {     XFirst = 0x1,     YFirst = 0x2   } |
|  | 移动优先 更多... |
|  | |
| enum | CameraModeEnum {     CameraStaticUp = 0x1,     CameraStaticDown = 0x2,     CameraMove = 0x3   } |
|  | 相机模式 更多... |
|  | |
| enum | HomoFreedomEnum {     Perspective = 0x1,     Affine = 0x2,     Similarity = 0x3   } |
|  | 自由度 更多... |
|  | |
| enum | WeightFunEnum {     LeastSqure = 0x1,     Huber = 0x2,     Tukey = 0x3   } |
|  | 权重函数 更多... |
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
| List< string > | TeachFlagInput `[set]` |
|  | 外部触发字符 更多... |
|  | |
| CalibPointGetEnum | CalibPointGet `[get, set]` |
|  | 标定点获取 更多... |
|  | |
| int | CalibPointTotalNum `[get, set]` |
|  | 平移次数，范围：[4,16] 更多... |
|  | |
| int | RotPointTotalNum `[get, set]` |
|  | 旋转次数，范围：[0,16] 更多... |
|  | |
| bool | TeachEnable `[get, set]` |
|  | 示教 更多... |
|  | |
| string | TeachFlag `[get, set]` |
|  | 外部触发字符 更多... |
|  | |
| double | BasePointX `[get, set]` |
|  | 基准点X，范围：[-9999999.0,9999999.0] 更多... |
|  | |
| double | BasePointY `[get, set]` |
|  | 基准点Y，范围：[-9999999.0,9999999.0] 更多... |
|  | |
| double | MoveAlignX `[get, set]` |
|  | 偏移X，范围：[-99999.0,99999.0] 更多... |
|  | |
| double | MoveAlignY `[get, set]` |
|  | 偏移Y，范围：[-99999.0,99999.0] 更多... |
|  | |
| MoveFirstTypeEnum | MoveFirstType `[get, set]` |
|  | 移动优先 更多... |
|  | |
| int | ChangeDirectionMoveTime `[get, set]` |
|  | 换向移动次数，范围：[1,16] 更多... |
|  | |
| double | BaseAngle `[get, set]` |
|  | 基准角度，范围：[-180.0,180.0] 更多... |
|  | |
| double | MoveAngle `[get, set]` |
|  | 角度偏移，范围：[-180.0,180.0] 更多... |
|  | |
| bool | UseRelativeCoordinates `[get, set]` |
|  | 使用相对坐标 更多... |
|  | |
| int | CalibOrigin `[get, set]` |
|  | 标定原点，范围：[0,15] 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| CameraModeEnum | CameraMode `[get, set]` |
|  | 相机模式 更多... |
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
| int | DistThreshold `[get, set]` |
|  | 距离阈值，范围：[1,100] 更多... |
|  | |
| int | SampleRatio `[get, set]` |
|  | 采样率，范围：[1,100] 更多... |
|  | |

## 详细描述

N点标定参数

## 成员枚举类型说明

## ◆ CalibPointGetEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibPointGetEnum | | strong |

标定点获取

| 枚举值 | |
| --- | --- |
| TriggerAcquisition | 触发获取 |
| ManualInput | 手动输入 |

## ◆ MoveFirstTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MoveFirstTypeEnum | | strong |

移动优先

| 枚举值 | |
| --- | --- |
| XFirst | X优先 |
| YFirst | Y优先 |

## ◆ CameraModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CameraModeEnum | | strong |

相机模式

| 枚举值 | |
| --- | --- |
| CameraStaticUp | 相机静止上相机位 |
| CameraStaticDown | 相机静止下相机位 |
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

## ◆ TeachFlagInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> TeachFlagInput | | set |

外部触发字符

**备注**

仅当次执行起效

## ◆ CalibPointGet

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibPointGetEnum CalibPointGet | | getset |

标定点获取

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

## ◆ TeachEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TeachEnable | | getset |

示教

## ◆ TeachFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string TeachFlag | | getset |

外部触发字符

## ◆ BasePointX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BasePointX | | getset |

基准点X，范围：[-9999999.0,9999999.0]

## ◆ BasePointY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BasePointY | | getset |

基准点Y，范围：[-9999999.0,9999999.0]

## ◆ MoveAlignX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MoveAlignX | | getset |

偏移X，范围：[-99999.0,99999.0]

## ◆ MoveAlignY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MoveAlignY | | getset |

偏移Y，范围：[-99999.0,99999.0]

## ◆ MoveFirstType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MoveFirstTypeEnum MoveFirstType | | getset |

移动优先

## ◆ ChangeDirectionMoveTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ChangeDirectionMoveTime | | getset |

换向移动次数，范围：[1,16]

## ◆ BaseAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double BaseAngle | | getset |

基准角度，范围：[-180.0,180.0]

## ◆ MoveAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double MoveAngle | | getset |

角度偏移，范围：[-180.0,180.0]

## ◆ UseRelativeCoordinates

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UseRelativeCoordinates | | getset |

使用相对坐标

## ◆ CalibOrigin

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibOrigin | | getset |

标定原点，范围：[0,15]

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

## ◆ DistThreshold

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DistThreshold | | getset |

距离阈值，范围：[1,100]

## ◆ SampleRatio

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SampleRatio | | getset |

采样率，范围：[1,100]
