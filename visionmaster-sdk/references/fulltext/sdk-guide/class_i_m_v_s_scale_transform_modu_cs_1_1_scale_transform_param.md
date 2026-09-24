<!-- src:class_i_m_v_s_scale_transform_modu_cs_1_1_scale_transform_param.html -->
<!-- path:接口函数 > 运算 > 单位转换 > ScaleTransformParam -->
# ScaleTransformParam类 参考 运算 » 单位转换

单位转换参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< float > | ImageDist `[set]` |
|  | 像素间距 更多... |
|  | |
| List< int > | RefreshSignal `[set]` |
|  | 刷新信号 更多... |
|  | |
| List< float > | PixelEquivalentCorrectInfo `[set]` |
|  | 像素当量修正系数 更多... |
|  | |
| string | LoadCalibPath `[get, set]` |
|  | 加载标定文件 更多... |
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

单位转换参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ ImageDist

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ImageDist | | set |

像素间距

**备注**

仅当次执行起效

## ◆ RefreshSignal

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshSignal | | set |

刷新信号

**备注**

仅当次执行起效

## ◆ PixelEquivalentCorrectInfo

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> PixelEquivalentCorrectInfo | | set |

像素当量修正系数

**备注**

仅当次执行起效

## ◆ LoadCalibPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string LoadCalibPath | | getset |

加载标定文件
