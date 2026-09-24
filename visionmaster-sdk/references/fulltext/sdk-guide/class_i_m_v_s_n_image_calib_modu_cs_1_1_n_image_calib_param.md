<!-- src:class_i_m_v_s_n_image_calib_modu_cs_1_1_n_image_calib_param.html -->
<!-- path:接口函数 > 标定 > N图像标定 > NImageCalibParam -->
# NImageCalibParam类 参考 标定 » N图像标定

N图像标定参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | MoveFirstTypeEnum {     XFirst = 0x1,     YFirst = 0x2   } |
|  | 移动优先 更多... |
|  | |
| enum | CalibBoardTypeEnum {     TypeHKI = 0x7,     TypeHKII = 0x6,     TypeHKIV2 = 0x9,     TypeHKIIV2 = 0x8   } |
|  | 标定板类型 更多... |
|  | |
| enum | FilterStatusEnum {     FilterStateTure = 0x1,     FilterStateFalse = 0x2   } |
|  | 中值滤波状态 更多... |
|  | |
| enum | SubpixelWinAutoEnum {     SubpixelWinSizeAuto = 0x1,     SubpixelWinSizeUser = 0x2   } |
|  | 亚像素窗口（弃用） 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| int | DoSaveFile (string value) |
|  | 生成标定文件 更多... |
|  | |
| int | DoClearImage () |
|  | 清除图像 更多... |
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
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< PointF > | ImagePoint `[set]` |
|  | 图像点 更多... |
|  | |
| List< PointF > | PhysicalPoint `[set]` |
|  | 物理点 更多... |
|  | |
| List< PointF > | PhyPoint `[set]` |
|  | 外部输入字符 更多... |
|  | |
| List< float > | RotateAngle `[set]` |
|  | 旋转角度 更多... |
|  | |
| int | CalibPointTotalNum `[get, set]` |
|  | 平移次数，范围：[0,15] 更多... |
|  | |
| int | RotPointTotalNum `[get, set]` |
|  | 旋转次数，范围：[0,9] 更多... |
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
| bool | HomoFixEnable `[get, set]` |
|  | 矩阵修正 更多... |
|  | |
| bool | RefreshFileEnable `[get, set]` |
|  | 更新文件 更多... |
|  | |
| string | CalibPathName `[get, set]` |
|  | 标定文件路径 更多... |
|  | |
| bool | CareraMove `[get, set]` |
|  | 相机移动 更多... |
|  | |
| CalibBoardTypeEnum | CalibBoardType `[get, set]` |
|  | 标定板类型 更多... |
|  | |
| int | GrayContrast `[get, set]` |
|  | 灰度对比度，范围：[1,255]（弃用） 更多... |
|  | |
| FilterStatusEnum | FilterStatus `[get, set]` |
|  | 中值滤波状态 更多... |
|  | |
| SubpixelWinAutoEnum | SubpixelWinAuto `[get, set]` |
|  | 亚像素窗口 更多... |
|  | |
| int | SubPixelWindowSize `[get, set]` |
|  | 设置窗口大小，范围：[3,150]（弃用） 更多... |
|  | |

## 详细描述

N图像标定参数

## 成员枚举类型说明

## ◆ MoveFirstTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MoveFirstTypeEnum | | strong |

移动优先

| 枚举值 | |
| --- | --- |
| XFirst | X优先 |
| YFirst | Y优先 |

## ◆ CalibBoardTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CalibBoardTypeEnum | | strong |

标定板类型

| 枚举值 | |
| --- | --- |
| TypeHKI | 海康标定板I型 |
| TypeHKII | 海康标定板II型 |
| TypeHKIV2 | 海康I型扩展 |
| TypeHKIIV2 | 海康II型扩展 |

## ◆ FilterStatusEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FilterStatusEnum | | strong |

中值滤波状态

| 枚举值 | |
| --- | --- |
| FilterStateTure | 执行滤波 |
| FilterStateFalse | 无滤波 |

## ◆ SubpixelWinAutoEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SubpixelWinAutoEnum | | strong |

亚像素窗口（弃用）

| 枚举值 | |
| --- | --- |
| SubpixelWinSizeAuto | 自适应 |
| SubpixelWinSizeUser | 设置值 |

## 成员函数说明

## ◆ DoSaveFile()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| int DoSaveFile | ( | string | *value* | ) |  |

生成标定文件

## ◆ DoClearImage()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int DoClearImage | ( |  | ) |  |

清除图像

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

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

## ◆ PhyPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> PhyPoint | | set |

外部输入字符

**备注**

仅当次执行起效

## ◆ RotateAngle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> RotateAngle | | set |

旋转角度

**备注**

仅当次执行起效

## ◆ CalibPointTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibPointTotalNum | | getset |

平移次数，范围：[0,15]

## ◆ RotPointTotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotPointTotalNum | | getset |

旋转次数，范围：[0,9]

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

## ◆ HomoFixEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool HomoFixEnable | | getset |

矩阵修正

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

## ◆ CareraMove

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CareraMove | | getset |

相机移动

## ◆ CalibBoardType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CalibBoardTypeEnum CalibBoardType | | getset |

标定板类型

## ◆ GrayContrast

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GrayContrast | | getset |

灰度对比度，范围：[1,255]（弃用）

## ◆ FilterStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FilterStatusEnum FilterStatus | | getset |

中值滤波状态

## ◆ SubpixelWinAuto

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SubpixelWinAutoEnum SubpixelWinAuto | | getset |

亚像素窗口

## ◆ SubPixelWindowSize

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SubPixelWindowSize | | getset |

设置窗口大小，范围：[3,150]（弃用）
