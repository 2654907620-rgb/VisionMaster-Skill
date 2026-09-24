<!-- src:class_read_calib_file_modu_cs_1_1_read_calib_file_param.html -->
<!-- path:接口函数 > 标定 > 标定加载 > ReadCalibFileParam -->
# ReadCalibFileParam类 参考 标定 » 标定加载

标定加载参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| List< float > | SnapImagePointX1 `[set]` |
|  | 图像基准坐标X 更多... |
|  | |
| List< float > | SnapImagePointY1 `[set]` |
|  | 图像基准坐标Y 更多... |
|  | |
| List< float > | SnapImageR1 `[set]` |
|  | 图像基准坐标R 更多... |
|  | |
| List< float > | SnapWorldPointX1 `[set]` |
|  | 拍照基准坐标X 更多... |
|  | |
| List< float > | SnapWorldPointY1 `[set]` |
|  | 拍照基准坐标Y 更多... |
|  | |
| List< float > | SnapWorldR1 `[set]` |
|  | 拍照基准坐标R 更多... |
|  | |
| List< float > | TeachWorldPointX1 `[set]` |
|  | 示教坐标X 更多... |
|  | |
| List< float > | TeachWorldPointY1 `[set]` |
|  | 示教坐标Y 更多... |
|  | |
| List< float > | TeachWorldR1 `[set]` |
|  | 示教坐标R 更多... |
|  | |
| bool | SaveCalibDataEnable `[get, set]` |
|  | 方案存矩阵 更多... |
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

标定加载参数

## 属性说明

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ SnapImagePointX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapImagePointX1 | | set |

图像基准坐标X

**备注**

仅当次执行起效

## ◆ SnapImagePointY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapImagePointY1 | | set |

图像基准坐标Y

**备注**

仅当次执行起效

## ◆ SnapImageR1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapImageR1 | | set |

图像基准坐标R

**备注**

仅当次执行起效

## ◆ SnapWorldPointX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapWorldPointX1 | | set |

拍照基准坐标X

**备注**

仅当次执行起效

## ◆ SnapWorldPointY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapWorldPointY1 | | set |

拍照基准坐标Y

**备注**

仅当次执行起效

## ◆ SnapWorldR1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> SnapWorldR1 | | set |

拍照基准坐标R

**备注**

仅当次执行起效

## ◆ TeachWorldPointX1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TeachWorldPointX1 | | set |

示教坐标X

**备注**

仅当次执行起效

## ◆ TeachWorldPointY1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TeachWorldPointY1 | | set |

示教坐标Y

**备注**

仅当次执行起效

## ◆ TeachWorldR1

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> TeachWorldR1 | | set |

示教坐标R

**备注**

仅当次执行起效

## ◆ SaveCalibDataEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveCalibDataEnable | | getset |

方案存矩阵
