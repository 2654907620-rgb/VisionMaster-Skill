<!-- src:class_image_source_module_cs_1_1_image_source_param.html -->
<!-- path:接口函数 > 采集 > 图像源 > ImageSourceParam -->
# ImageSourceParam类 参考 采集 » 图像源

图像源参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ImageSourceTypeEnum {     LocalImage = 0x1,     Camera = 0x2,     SDK = 0x3   } |
|  | 图像源 更多... |
|  | |
| enum | PixelFormatEnum {     MONO8 = 0x1,     RGB24 = 0x2   } |
|  | 像素格式 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< string > | TriggerString `[set]` |
|  | 触发字符 更多... |
|  | |
| List< string > | TriggerFilter `[set]` |
|  | 过滤字符 更多... |
|  | |
| List< float > | ExposureTimeInput `[set]` |
|  | 曝光时间 更多... |
|  | |
| List< float > | GainInput `[set]` |
|  | 增益时间 更多... |
|  | |
| List< int > | ClearTriggerValue `[set]` |
|  | 触发清空变量 更多... |
|  | |
| ImageSourceTypeEnum | ImageSourceType `[get, set]` |
|  | 图像源 更多... |
|  | |
| PixelFormatEnum | PixelFormat `[get, set]` |
|  | 像素格式 更多... |
|  | |
| int | Interval `[get, set]` |
|  | 取图间隔，范围：[0,1000] 更多... |
|  | |
| bool | SolSaveImageData `[get, set]` |
|  | 方案存图 更多... |
|  | |
| bool | ShowImageName `[get, set]` |
|  | 显示图像名称 更多... |
|  | |
| int | InitialSN `[get, set]` |
|  | SN初始值，范围：[0,100000] 更多... |
|  | |
| int | PathCache `[get, set]` |
|  | 图片缓存，范围：[0,5] 更多... |
|  | |
| bool | OutMono8 `[get, set]` |
|  | 输出Mono8 更多... |
|  | |
| bool | StitchEnable `[get, set]` |
|  | 拼接使能 更多... |
|  | |
| int | StitchStartHeight `[get, set]` |
|  | 起始高度，范围：[0,20000] 更多... |
|  | |
| int | StitchHeight `[get, set]` |
|  | 拼接高度，范围：[0,20000] 更多... |
|  | |
| bool | ClearTrigger `[get, set]` |
|  | 触发清空 更多... |
|  | |
| bool | AutoPlay `[get, set]` |
|  | 自动切换 更多... |
|  | |
| bool | AutoStop `[get, set]` |
|  | 最后一张停止 更多... |
|  | |
| bool | TriggerStringEnable `[get, set]` |
|  | 字符触发过滤 更多... |
|  | |
| bool | IsSubscribeFolderMode `[get, set]` |
|  | 订阅文件夹 更多... |
|  | |
| string | SubscribeFolderPath `[get, set]` |
|  | 图像路径 更多... |
|  | |
| bool | RefreshImage `[get, set]` |
|  | 更新缩略图 更多... |
|  | |
| bool | TriggerProcessRun `[get, set]` |
|  | 触发流程执行 更多... |
|  | |
| string | CameraName `[get, set]` |
|  | 关联相机 更多... |
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

图像源参数

## 成员枚举类型说明

## ◆ ImageSourceTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageSourceTypeEnum | | strong |

图像源

| 枚举值 | |
| --- | --- |
| LocalImage | 本地图像 |
| Camera | 相机 |
| SDK | SDK |

## ◆ PixelFormatEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PixelFormatEnum | | strong |

像素格式

| 枚举值 | |
| --- | --- |
| MONO8 | MONO8 |
| RGB24 | RGB24 |

## 属性说明

## ◆ TriggerString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> TriggerString | | set |

触发字符

**备注**

仅当次执行起效

## ◆ TriggerFilter

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> TriggerFilter | | set |

过滤字符

**备注**

仅当次执行起效

## ◆ ExposureTimeInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> ExposureTimeInput | | set |

曝光时间

**备注**

仅当次执行起效

## ◆ GainInput

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<float> GainInput | | set |

增益时间

**备注**

仅当次执行起效

## ◆ ClearTriggerValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> ClearTriggerValue | | set |

触发清空变量

**备注**

仅当次执行起效

## ◆ ImageSourceType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSourceTypeEnum ImageSourceType | | getset |

图像源

## ◆ PixelFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PixelFormatEnum PixelFormat | | getset |

像素格式

## ◆ Interval

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Interval | | getset |

取图间隔，范围：[0,1000]

## ◆ SolSaveImageData

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SolSaveImageData | | getset |

方案存图

## ◆ ShowImageName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ShowImageName | | getset |

显示图像名称

## ◆ InitialSN

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int InitialSN | | getset |

SN初始值，范围：[0,100000]

## ◆ PathCache

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int PathCache | | getset |

图片缓存，范围：[0,5]

## ◆ OutMono8

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutMono8 | | getset |

输出Mono8

## ◆ StitchEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool StitchEnable | | getset |

拼接使能

## ◆ StitchStartHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int StitchStartHeight | | getset |

起始高度，范围：[0,20000]

## ◆ StitchHeight

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int StitchHeight | | getset |

拼接高度，范围：[0,20000]

## ◆ ClearTrigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ClearTrigger | | getset |

触发清空

## ◆ AutoPlay

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AutoPlay | | getset |

自动切换

## ◆ AutoStop

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool AutoStop | | getset |

最后一张停止

## ◆ TriggerStringEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TriggerStringEnable | | getset |

字符触发过滤

## ◆ IsSubscribeFolderMode

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool IsSubscribeFolderMode | | getset |

订阅文件夹

## ◆ SubscribeFolderPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string SubscribeFolderPath | | getset |

图像路径

## ◆ RefreshImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RefreshImage | | getset |

更新缩略图

## ◆ TriggerProcessRun

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool TriggerProcessRun | | getset |

触发流程执行

## ◆ CameraName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CameraName | | getset |

关联相机
