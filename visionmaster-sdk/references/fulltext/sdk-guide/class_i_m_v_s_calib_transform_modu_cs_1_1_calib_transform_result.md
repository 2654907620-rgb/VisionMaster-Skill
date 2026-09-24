<!-- src:class_i_m_v_s_calib_transform_modu_cs_1_1_calib_transform_result.html -->
<!-- path:接口函数 > 运算 > 标定转换 > CalibTransformResult -->
# CalibTransformResult类 参考 运算 » 标定转换

标定转换结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| List< PointF > | TransPoint `[get]` |
|  | 输出点 更多... |
|  | |
| List< float > | WorldPointA `[get]` |
|  | 转换角度 更多... |
|  | |
| float | PixelScale `[get]` |
|  | 单像素精度 更多... |
|  | |
| float | TranslateX `[get]` |
|  | 平移X 更多... |
|  | |
| float | TranslateY `[get]` |
|  | 平移Y 更多... |
|  | |
| float | Rotate `[get]` |
|  | 旋转 更多... |
|  | |
| float | Scale `[get]` |
|  | 尺度 更多... |
|  | |
| float | Skew `[get]` |
|  | 斜切 更多... |
|  | |
| float | Aspect `[get]` |
|  | 宽高比 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

标定转换结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ TransPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> TransPoint | | get |

输出点

## ◆ WorldPointA

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> WorldPointA | | get |

转换角度

## ◆ PixelScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float PixelScale | | get |

单像素精度

## ◆ TranslateX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TranslateX | | get |

平移X

## ◆ TranslateY

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TranslateY | | get |

平移Y

## ◆ Rotate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Rotate | | get |

旋转

## ◆ Scale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Scale | | get |

尺度

## ◆ Skew

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Skew | | get |

斜切

## ◆ Aspect

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float Aspect | | get |

宽高比
