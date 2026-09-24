<!-- src:class_i_m_v_s_ellipse_find_modu_cs_1_1_ellipse_find_param.html -->
<!-- path:接口函数 > 定位 > 椭圆查找 > EllipseFindParam -->
# EllipseFindParam类 参考 定位 » 椭圆查找

椭圆查找参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | EllipseFindModeEnum {     Best = 0x1,     Largest = 0x2,     SMALLEST = 0x3   } |
|  | 边缘类型 更多... |
|  | |
| enum | EdgePolarityEnum {     BlackToWhite = 0x1,     WhiteToBlack = 0x2,     Both = 0x3   } |
|  | 边缘极性 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| EllipseFindRoiManager | ModuRoiManager `[get]` |
|  | ROI管理器 更多... |
|  | |
| double | ScaleInside `[get, set]` |
|  | 缩放范围，范围：[0.1,2] 更多... |
|  | |
| double | ScaleOutside `[get, set]` |
|  | 缩放范围，范围：[0.1,2] 更多... |
|  | |
| EllipseFindModeEnum | EllipseFindMode `[get, set]` |
|  | 边缘类型 更多... |
|  | |
| EdgePolarityEnum | EdgePolarity `[get, set]` |
|  | 边缘极性 更多... |
|  | |
| int | EdgeThresh `[get, set]` |
|  | 边缘阈值，范围：[1,255] 更多... |
|  | |
| int | RaysNum `[get, set]` |
|  | 卡尺数量，范围：[6,1000] 更多... |
|  | |
| int | EdgeWidth `[get, set]` |
|  | 滤波尺寸，范围：[1,50] 更多... |
|  | |
| int | RegionWidth `[get, set]` |
|  | 投影宽度，范围：[1,100] 更多... |
|  | |
| int | FitErrorTolerance `[get, set]` |
|  | 误差容忍度，范围：[1,200] 更多... |
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

椭圆查找参数

## 成员枚举类型说明

## ◆ EllipseFindModeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EllipseFindModeEnum | | strong |

边缘类型

| 枚举值 | |
| --- | --- |
| Best | 最强 |
| Largest | 最后一条 |
| SMALLEST | 第一条 |

## ◆ EdgePolarityEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum EdgePolarityEnum | | strong |

边缘极性

| 枚举值 | |
| --- | --- |
| BlackToWhite | 从黑到白 |
| WhiteToBlack | 从白到黑 |
| Both | 任意极性 |

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
| |  | | --- | | EllipseFindRoiManager ModuRoiManager | | get |

ROI管理器

## ◆ ScaleInside

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleInside | | getset |

缩放范围，范围：[0.1,2]

## ◆ ScaleOutside

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double ScaleOutside | | getset |

缩放范围，范围：[0.1,2]

## ◆ EllipseFindMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EllipseFindModeEnum EllipseFindMode | | getset |

边缘类型

## ◆ EdgePolarity

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePolarityEnum EdgePolarity | | getset |

边缘极性

## ◆ EdgeThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeThresh | | getset |

边缘阈值，范围：[1,255]

## ◆ RaysNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RaysNum | | getset |

卡尺数量，范围：[6,1000]

## ◆ EdgeWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int EdgeWidth | | getset |

滤波尺寸，范围：[1,50]

## ◆ RegionWidth

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RegionWidth | | getset |

投影宽度，范围：[1,100]

## ◆ FitErrorTolerance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FitErrorTolerance | | getset |

误差容忍度，范围：[1,200]
