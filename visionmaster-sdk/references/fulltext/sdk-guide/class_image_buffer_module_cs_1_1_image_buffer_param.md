<!-- src:class_image_buffer_module_cs_1_1_image_buffer_param.html -->
<!-- path:接口函数 > 采集 > 缓存图像 > ImageBufferParam -->
# ImageBufferParam类 参考 采集 » 缓存图像

缓存图像参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| List< int > | RefreshFlag `[set]` |
|  | 刷新标志 更多... |
|  | |
| List< int > | BufferCount `[set]` |
|  | 缓存数量 更多... |
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

缓存图像参数

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ RefreshFlag

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> RefreshFlag | | set |

刷新标志

**备注**

仅当次执行起效

## ◆ BufferCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> BufferCount | | set |

缓存数量

**备注**

仅当次执行起效
