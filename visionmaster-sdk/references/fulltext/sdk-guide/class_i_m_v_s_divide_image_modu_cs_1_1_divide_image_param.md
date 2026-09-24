<!-- src:class_i_m_v_s_divide_image_modu_cs_1_1_divide_image_param.html -->
<!-- path:接口函数 > 拆分组合 > 划片拆分 > DivideImageParam -->
# DivideImageParam类 参考 拆分组合 » 划片拆分

划片拆分参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| DivideImageRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| int | NumX `[get, set]` |
|  | X方向划片数，范围：[1,50] 更多... |
|  | |
| int | NumY `[get, set]` |
|  | Y方向划片数，范围：[1,50] 更多... |
|  | |
| int | OverlaprateX `[get, set]` |
|  | X方向重叠率，范围：[0,100] 更多... |
|  | |
| int | OverlaprateY `[get, set]` |
|  | Y方向重叠率，范围：[0,100] 更多... |
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

划片拆分参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DivideImageRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ NumX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumX | | getset |

X方向划片数，范围：[1,50]

## ◆ NumY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int NumY | | getset |

Y方向划片数，范围：[1,50]

## ◆ OverlaprateX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OverlaprateX | | getset |

X方向重叠率，范围：[0,100]

## ◆ OverlaprateY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OverlaprateY | | getset |

Y方向重叠率，范围：[0,100]
