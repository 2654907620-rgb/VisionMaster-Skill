<!-- src:class_image_source_module_cs_1_1_image_source_module_tool.html -->
<!-- path:接口函数 > 采集 > 图像源 > ImageSourceModuleTool -->
# ImageSourceModuleTool类 参考 采集 » 图像源

图像源工具
更多...

继承自 VmModule , 以及 IImageSourceNode .

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | Run () |
|  | 模块自执行 更多... |
|  | |
| void | SetImagePath (string strPath) |
|  | 设置图像路径 更多... |
|  | |
| void | SetImageData (ImageBaseData stImgData, bool bIsWaitCopy=true) |
|  | 设置图像数据 更多... |
|  | |
| void | SetImageDataP2P (ImageBaseData stImgData, bool bIsWaitCopy=true) |
|  | 点对点设置图像数据 更多... |
|  | |
| void | AddInputImageByPath (string strPath) |
|  | 通过路径添加图像 更多... |
|  | |
| void | DeleteInputImageByPath (string strPath) |
|  | 通过路径删除图像 更多... |
|  | |
| void | ClearAllInputImage () |
|  | 清空所有输入图像 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ImageSourceResult | ModuResult `[get]` |
|  | 模块结果对象 更多... |
|  | |
| ImageSourceParam | ModuParams `[get, set]` |
|  | 模块参数对象 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 属性 继承自 VmModule | |
| ModuResultMemoryTypeEnum | ModuResultMemType |
|  | 模块结果内存管理类型 更多... |
|  | |

## 详细描述

图像源工具

## 成员函数说明

## ◆ Run()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| new void Run | ( |  | ) |  |

模块自执行

## ◆ SetImagePath()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetImagePath | ( | string | *strPath* | ) |  |

设置图像路径

参数
:   |  |  |
    | --- | --- |
    | strPath | 图像路径 |

**备注**

图像源需选择SDK模式

## ◆ SetImageData()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetImageData | ( | ImageBaseData | *stImgData*, |
|  |  | bool | *bIsWaitCopy* = `true` |
|  | ) |  |  |

设置图像数据

参数
:   |  |  |
    | --- | --- |
    | stImgData | 图像数据 |
    | bIsWaitCopy | 是否等待图像拷贝完成,如不等待,则在当次执行期间,避免释放该图像数据 |

**备注**

图像源需选择SDK模式

仅当次执行起效

## ◆ SetImageDataP2P()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetImageDataP2P | ( | ImageBaseData | *stImgData*, |
|  |  | bool | *bIsWaitCopy* = `true` |
|  | ) |  |  |

点对点设置图像数据

参数
:   |  |  |
    | --- | --- |
    | stImgData | 图像数据 |
    | bIsWaitCopy | 是否等待图像拷贝完成,如不等待,则在当次执行期间,避免释放该图像数据 |

**备注**

图像源需选择SDK模式

仅当次执行起效

## ◆ AddInputImageByPath()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void AddInputImageByPath | ( | string | *strPath* | ) |  |

通过路径添加图像

## ◆ DeleteInputImageByPath()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void DeleteInputImageByPath | ( | string | *strPath* | ) |  |

通过路径删除图像

## ◆ ClearAllInputImage()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearAllInputImage | ( |  | ) |  |

清空所有输入图像

## 属性说明

## ◆ ModuResult

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSourceResult ModuResult | | get |

模块结果对象

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ImageSourceParam ModuParams | | getset |

模块参数对象
