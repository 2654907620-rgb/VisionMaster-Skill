<!-- src:class_image_source_module_cs_1_1_image_source_result.html -->
<!-- path:接口函数 > 采集 > 图像源 > ImageSourceResult -->
# ImageSourceResult类 参考 采集 » 图像源

图像源结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | ImageData `[get]` |
|  | 图像 更多... |
|  | |
| ImageBaseData | ImageDataMono8 `[get]` |
|  | 灰度图像 更多... |
|  | |
| ImageBaseData | ImageData2 `[get]` |
|  | 图像2 更多... |
|  | |
| ImageBaseData | ImageData3 `[get]` |
|  | 图像3 更多... |
|  | |
| ImageBaseData | ImageData4 `[get]` |
|  | 图像4 更多... |
|  | |
| int | ImageCount `[get]` |
|  | 图像数量 更多... |
|  | |
| string | CurImagePath `[get]` |
|  | 当前图像路径 更多... |
|  | |
| string | CurImageName `[get]` |
|  | 当前图像名称 更多... |
|  | |
| int | FrameNum `[get]` |
|  | 帧号 更多... |
|  | |
| int | LostFrameCount `[get]` |
|  | 丢帧数 更多... |
|  | |
| int | LostPacketCount `[get]` |
|  | 丢包数 更多... |
|  | |
| int | GetCameraFailCount `[get]` |
|  | 相机获取失败次数 更多... |
|  | |
| int | SNCode `[get]` |
|  | SN码 更多... |
|  | |
| int | ImageNum `[get]` |
|  | 取图数量，范围：[1,4] 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

图像源结果

## 属性说明

## ◆ ImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ImageData | | get |

图像

## ◆ ImageDataMono8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ImageDataMono8 | | get |

灰度图像

## ◆ ImageData2

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ImageData2 | | get |

图像2

## ◆ ImageData3

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ImageData3 | | get |

图像3

## ◆ ImageData4

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData ImageData4 | | get |

图像4

## ◆ ImageCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageCount | | get |

图像数量

## ◆ CurImagePath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CurImagePath | | get |

当前图像路径

## ◆ CurImageName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CurImageName | | get |

当前图像名称

## ◆ FrameNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FrameNum | | get |

帧号

## ◆ LostFrameCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LostFrameCount | | get |

丢帧数

## ◆ LostPacketCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LostPacketCount | | get |

丢包数

## ◆ GetCameraFailCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int GetCameraFailCount | | get |

相机获取失败次数

## ◆ SNCode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int SNCode | | get |

SN码

## ◆ ImageNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageNum | | get |

取图数量，范围：[1,4]
