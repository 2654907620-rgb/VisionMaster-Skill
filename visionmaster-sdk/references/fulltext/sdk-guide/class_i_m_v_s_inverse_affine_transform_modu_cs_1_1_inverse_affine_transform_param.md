<!-- src:class_i_m_v_s_inverse_affine_transform_modu_cs_1_1_inverse_affine_transform_param.html -->
<!-- path:接口函数 > 图像处理 > 逆仿射变换 > InverseAffineTransformParam -->
# InverseAffineTransformParam类 参考 图像处理 » 逆仿射变换

逆仿射变换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| ImageBaseData | InputImageBack `[set]` |
|  | 输入底图 更多... |
|  | |
| List< int > | Imagewidth `[set]` |
|  | 图像宽度 更多... |
|  | |
| List< int > | Imageheight `[set]` |
|  | 图像高度 更多... |
|  | |
| InverseAffineTransformRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
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

逆仿射变换参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ InputImageBack

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImageBack | | set |

输入底图

**备注**

仅当次执行起效

## ◆ Imagewidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Imagewidth | | set |

图像宽度

**备注**

仅当次执行起效

## ◆ Imageheight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> Imageheight | | set |

图像高度

**备注**

仅当次执行起效

## ◆ ModuRoiManager

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InverseAffineTransformRoiManager ModuRoiManager | | get |

ROI管理器
