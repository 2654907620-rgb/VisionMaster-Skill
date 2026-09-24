<!-- src:class_save_image_cs_1_1_save_image_param.html -->
<!-- path:接口函数 > 采集 > 输出图像 > SaveImageParam -->
# SaveImageParam类 参考 采集 » 输出图像

输出图像参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | ImageSaveConditionEnum {     ALL = 0x0,     OK = 0x1,     NG = 0x2,     NONE = 0x3   } |
|  | 保存条件 更多... |
|  | |
| enum | ImageSaveTypeEnum {     OverWrite = 0x0,     NoSave = 0x1   } |
|  | 存储方式 更多... |
|  | |
| enum | DiskUnitEnum {     MByte = 0x0,     GByte = 0x1   } |
|  | 存储单位 更多... |
|  | |
| enum | ImageTypeEnum {     BMP = 0x0,     JPEG = 0x1,     PNG = 0x2   } |
|  | 保存格式 更多... |
|  | |
| enum | CodingFormatEnum {     UTF8 = 0x0,     UNICODE = 0x1   } |
|  | 编码格式 更多... |
|  | |
| enum | PixelFormatEnum {     RGB24 = 0x0,     MONO8 = 0x1   } |
|  | 像素格式 更多... |
|  | |
| enum | GraphRateTypeEnum {     MatchImage = 0x0,     MatchView = 0x1,     CustomRate = 0x2   } |
|  | 图形倍率类型 更多... |
|  | |
| enum | LineTypeEnum {     FourConnectedLine = 0x0,     EightConnectedLine = 0x1,     AntialiasedLine = 0x2   } |
|  | 线型 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageBaseData | InputImage `[set]` |
|  | 输入图像 更多... |
|  | |
| bool | OutputEnable `[get, set]` |
|  | 输出使能 更多... |
|  | |
| bool | SaveImageEnable `[get, set]` |
|  | 存图使能 更多... |
|  | |
| bool | ImageSaveTrigger `[get, set]` |
|  | 触发保存 更多... |
|  | |
| ImageSaveConditionEnum | ImageSaveCondition `[get, set]` |
|  | 保存条件 更多... |
|  | |
| bool | DebugInfoSave `[get, set]` |
|  | 调试保存 更多... |
|  | |
| bool | GenerateDir `[get, set]` |
|  | 生成目录 更多... |
|  | |
| bool | SynchronousStorage `[get, set]` |
|  | 同步存储(弃用) 更多... |
|  | |
| int | StorageInterval `[get, set]` |
|  | 存图间隔，范围：[1,10] 更多... |
|  | |
| bool | RenderImgEnable `[get, set]` |
|  | 保存渲染图 更多... |
|  | |
| string | RenderImgPath `[get, set]` |
|  | 渲染图路径 更多... |
|  | |
| string | RenderOKPath `[get, set]` |
|  | 渲染OK路径 更多... |
|  | |
| string | RenderNGPath `[get, set]` |
|  | 渲染NG路径 更多... |
|  | |
| int | RenderImgCache `[get, set]` |
|  | 渲染图缓存，范围：[1,20] 更多... |
|  | |
| bool | OriginImgEnable `[get, set]` |
|  | 保存原图 更多... |
|  | |
| string | OriginImgPath `[get, set]` |
|  | 原图路径 更多... |
|  | |
| string | OriginOKPath `[get, set]` |
|  | 原图OK路径 更多... |
|  | |
| string | OriginNGPath `[get, set]` |
|  | 原图NG路径 更多... |
|  | |
| int | OriginImgCache `[get, set]` |
|  | 原图缓存，范围：[1,20] 更多... |
|  | |
| ImageSaveTypeEnum | ImageSaveType `[get, set]` |
|  | 存储方式 更多... |
|  | |
| int | DiskFreespace `[get, set]` |
|  | 磁盘剩余空间，范围：[1,1024] 更多... |
|  | |
| DiskUnitEnum | DiskUnit `[get, set]` |
|  | 存储单位 更多... |
|  | |
| int | ImageMemoryDay `[get, set]` |
|  | 最大保存天数，范围：[1,500] 更多... |
|  | |
| ImageTypeEnum | ImageType `[get, set]` |
|  | 保存格式 更多... |
|  | |
| int | ImageCompressionRation `[get, set]` |
|  | 图片压缩质量，范围：[1,100] 更多... |
|  | |
| bool | FTPEnable `[get, set]` |
|  | 启用FTP 更多... |
|  | |
| bool | ConnectEnable `[get, set]` |
|  | 连接 更多... |
|  | |
| string | ServerIP `[get, set]` |
|  | 服务器IP 更多... |
|  | |
| int | ServerPort `[get, set]` |
|  | 服务器端口，范围：[1,65535] 更多... |
|  | |
| string | UserName `[get, set]` |
|  | 用户名 更多... |
|  | |
| string | Password `[get, set]` |
|  | 密码 更多... |
|  | |
| CodingFormatEnum | CodingFormat `[get, set]` |
|  | 编码格式 更多... |
|  | |
| string | FTPPath `[get, set]` |
|  | FTP路径 更多... |
|  | |
| PixelFormatEnum | PixelFormat `[get, set]` |
|  | 像素格式 更多... |
|  | |
| GraphRateTypeEnum | GraphRateType `[get, set]` |
|  | 图形倍率类型 更多... |
|  | |
| int | LineWidthRate `[get, set]` |
|  | 线宽倍率，范围：[1,16] 更多... |
|  | |
| int | FontSizeRate `[get, set]` |
|  | 字宽倍率，范围：[1,16] 更多... |
|  | |
| LineTypeEnum | LineType `[get, set]` |
|  | 线型 更多... |
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

输出图像参数

## 成员枚举类型说明

## ◆ ImageSaveConditionEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageSaveConditionEnum | | strong |

保存条件

| 枚举值 | |
| --- | --- |
| ALL | 全部保存 |
| OK | OK时保存 |
| NG | NG时保存 |
| NONE | 不保存 |

## ◆ ImageSaveTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageSaveTypeEnum | | strong |

存储方式

| 枚举值 | |
| --- | --- |
| OverWrite | 覆盖存储 |
| NoSave | 停止存储 |

## ◆ DiskUnitEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DiskUnitEnum | | strong |

存储单位

| 枚举值 | |
| --- | --- |
| MByte | MB |
| GByte | GB |

## ◆ ImageTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum ImageTypeEnum | | strong |

保存格式

| 枚举值 | |
| --- | --- |
| BMP | BMP |
| JPEG | JPEG |
| PNG | PNG |

## ◆ CodingFormatEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum CodingFormatEnum | | strong |

编码格式

| 枚举值 | |
| --- | --- |
| UTF8 | UTF8 |
| UNICODE | UNICODE |

## ◆ PixelFormatEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PixelFormatEnum | | strong |

像素格式

| 枚举值 | |
| --- | --- |
| RGB24 | RGB24 |
| MONO8 | MONO8 |

## ◆ GraphRateTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum GraphRateTypeEnum | | strong |

图形倍率类型

| 枚举值 | |
| --- | --- |
| MatchImage | 原图尺寸 |
| MatchView | 界面尺寸 |
| CustomRate | 自定义倍率 |

## ◆ LineTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LineTypeEnum | | strong |

线型

| 枚举值 | |
| --- | --- |
| FourConnectedLine | 4连通线 |
| EightConnectedLine | 8连通线 |
| AntialiasedLine | 抗锯齿线 |

## 属性说明

## ◆ InputImage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageBaseData InputImage | | set |

输入图像

**备注**

仅当次执行起效

## ◆ OutputEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OutputEnable | | getset |

输出使能

## ◆ SaveImageEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveImageEnable | | getset |

存图使能

## ◆ ImageSaveTrigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ImageSaveTrigger | | getset |

触发保存

## ◆ ImageSaveCondition

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSaveConditionEnum ImageSaveCondition | | getset |

保存条件

## ◆ DebugInfoSave

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool DebugInfoSave | | getset |

调试保存

## ◆ GenerateDir

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool GenerateDir | | getset |

生成目录

## ◆ SynchronousStorage

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SynchronousStorage | | getset |

同步存储(弃用)

## ◆ StorageInterval

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int StorageInterval | | getset |

存图间隔，范围：[1,10]

## ◆ RenderImgEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RenderImgEnable | | getset |

保存渲染图

## ◆ RenderImgPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string RenderImgPath | | getset |

渲染图路径

## ◆ RenderOKPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string RenderOKPath | | getset |

渲染OK路径

## ◆ RenderNGPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string RenderNGPath | | getset |

渲染NG路径

## ◆ RenderImgCache

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RenderImgCache | | getset |

渲染图缓存，范围：[1,20]

## ◆ OriginImgEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool OriginImgEnable | | getset |

保存原图

## ◆ OriginImgPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string OriginImgPath | | getset |

原图路径

## ◆ OriginOKPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string OriginOKPath | | getset |

原图OK路径

## ◆ OriginNGPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string OriginNGPath | | getset |

原图NG路径

## ◆ OriginImgCache

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OriginImgCache | | getset |

原图缓存，范围：[1,20]

## ◆ ImageSaveType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSaveTypeEnum ImageSaveType | | getset |

存储方式

## ◆ DiskFreespace

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int DiskFreespace | | getset |

磁盘剩余空间，范围：[1,1024]

## ◆ DiskUnit

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DiskUnitEnum DiskUnit | | getset |

存储单位

## ◆ ImageMemoryDay

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageMemoryDay | | getset |

最大保存天数，范围：[1,500]

## ◆ ImageType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageTypeEnum ImageType | | getset |

保存格式

## ◆ ImageCompressionRation

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ImageCompressionRation | | getset |

图片压缩质量，范围：[1,100]

## ◆ FTPEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool FTPEnable | | getset |

启用FTP

## ◆ ConnectEnable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ConnectEnable | | getset |

连接

## ◆ ServerIP

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string ServerIP | | getset |

服务器IP

## ◆ ServerPort

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ServerPort | | getset |

服务器端口，范围：[1,65535]

## ◆ UserName

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string UserName | | getset |

用户名

## ◆ Password

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string Password | | getset |

密码

## ◆ CodingFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CodingFormatEnum CodingFormat | | getset |

编码格式

## ◆ FTPPath

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string FTPPath | | getset |

FTP路径

## ◆ PixelFormat

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PixelFormatEnum PixelFormat | | getset |

像素格式

## ◆ GraphRateType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | GraphRateTypeEnum GraphRateType | | getset |

图形倍率类型

## ◆ LineWidthRate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int LineWidthRate | | getset |

线宽倍率，范围：[1,16]

## ◆ FontSizeRate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FontSizeRate | | getset |

字宽倍率，范围：[1,16]

## ◆ LineType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | LineTypeEnum LineType | | getset |

线型
