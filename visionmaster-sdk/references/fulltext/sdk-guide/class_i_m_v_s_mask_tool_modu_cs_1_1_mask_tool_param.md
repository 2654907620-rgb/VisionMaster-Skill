<!-- src:class_i_m_v_s_mask_tool_modu_cs_1_1_mask_tool_param.html -->
<!-- path:接口函数 > 图像处理 > 掩膜工具 > MaskToolParam -->
# MaskToolParam类 参考 图像处理 » 掩膜工具

掩膜工具参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | FillTypeEnum {     WhiteInBlackOut = 0,     BlackInWhiteOut = 1   } |
|  | 填充方式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| MaskToolRoiManager | ModuRoiManager `[get, set]` |
|  | ROI管理器 更多... |
|  | |
| bool | UseInputImgAsMask `[get, set]` |
|  | 使用输入图 更多... |
|  | |
| bool | InputImgFillInRoi `[get, set]` |
|  | 图在ROI内 更多... |
|  | |
| FillTypeEnum | FillType `[get, set]` |
|  | 填充方式 更多... |
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

掩膜工具参数

## 成员枚举类型说明

## ◆ FillTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum FillTypeEnum | | strong |

填充方式

| 枚举值 | |
| --- | --- |
| WhiteInBlackOut | 内白外黑 |
| BlackInWhiteOut | 内黑外白 |

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
| |  | | --- | | MaskToolRoiManager ModuRoiManager | | getset |

ROI管理器

## ◆ UseInputImgAsMask

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool UseInputImgAsMask | | getset |

使用输入图

## ◆ InputImgFillInRoi

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool InputImgFillInRoi | | getset |

图在ROI内

## ◆ FillType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FillTypeEnum FillType | | getset |

填充方式
