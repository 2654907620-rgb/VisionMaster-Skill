<!-- src:class_vm_render_control.html -->
<!-- path:接口函数 > 控件 > 渲染控件 > VmRenderControl -->
# VmRenderControl类 参考 控件 » 渲染控件

渲染控件
更多...

继承自 UserControl .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | UpdateVMResultShow () |
|  | 刷新 更多... |
|  | |
| void | DrawShape (object shape) |
|  | 绘制图形（立刻绘制） 更多... |
|  | |
| void | AddShape (object shape) |
|  | 添加图形（在下次刷新渲染时自动绘制） 更多... |
|  | |
| bool | SetBackgroundImage (IVmIO io) |
|  | 设置背景图 更多... |
|  | |
| void | EnlargeView () |
|  | 放大视图 更多... |
|  | |
| void | ShrinkView () |
|  | 缩小视图 更多... |
|  | |
| void | InitView () |
|  | 还原视图 更多... |
|  | |
| void | ClearDisplayView () |
|  | 清空渲染显示区域（包括图像和图形） 更多... |
|  | |
| void | SaveOriginalImage (string fileName, int jpgQuality=95) |
|  | 保存原图 更多... |
|  | |
| void | SaveRenderedImage (string fileName, int jpgQuality=95) |
|  | 保存渲染图 更多... |
|  | |
| void | SetBackground (string value) |
|  | 设置控件背景 更多... |
|  | |
| void | SetRenderInterval (int pMillseconds) |
|  | 设置渲染间隔(ms) 更多... |
|  | |
| void | ChangeImageComboBoxVisibility (bool isImageComboBoxVisible) |
|  | 控制图层选择控件显示隐藏 更多... |
|  | |
| string | GetSelectedImageDisplayName () |
|  | 获取当前选中图像名称 更多... |
|  | |
| void | SetRenderCondition (RenderSatus status) |
|  | 设置渲染条件（当设置条件status和模块状态值一致时才刷新） 更多... |
|  | |
| void | Dispose () |
|  | 释放资源 更多... |
|  | |
| void | SetRenderToolbarVisible (bool isVisible) |
|  | 工具栏是否可见 更多... |
|  | |
| List< string > | GetDisplayableImageNameList () |
|  | 获取可显示的图像名称列表 更多... |
|  | |
| void | SetSelectedImage (string displayImageName) |
|  | 选择一张图像作为显示图像 更多... |
|  | |
| void | SwitchBackgroundImage (string backgroundImageName) |
|  | 当图像堆叠时，切换背景图像 更多... |
|  | |
| void | AddStackImage (string displayImageName) |
|  | 添加一张图像，进行图像堆叠。最新添加的图像显示在最顶层 更多... |
|  | |
| void | RemoveStackImage (string displayImageName) |
|  | 指定图像名称，将其从当前堆叠显示的图像中删除 更多... |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static int | ConvertColor (byte bR, byte bG, byte bB) |
|  | 将rgb格式的颜色转换为渲染控件可接受的数值，每个参数范围均为0-255 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| IVmModule | ModuleSource `[get, set]` |
|  | 数据源模块 更多... |
|  | |
| IImageData | ImageSource `[get, set]` |
|  | 图像源 更多... |
|  | |
| bool | CoordinateInfoVisible `[get, set]` |
|  | 是否显示坐标信息 更多... |
|  | |

## 详细描述

渲染控件

## 成员函数说明

## ◆ UpdateVMResultShow()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void UpdateVMResultShow | ( |  | ) |  |

刷新

## ◆ DrawShape()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void DrawShape | ( | object | *shape* | ) |  |

绘制图形（立刻绘制）

参数
:   |  |  |
    | --- | --- |
    | shape | 图形对象 |

**备注**

            传入图形可使用VMControls.WPF中名称以Ex结尾的图形结构体

## ◆ AddShape()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void AddShape | ( | object | *shape* | ) |  |

添加图形（在下次刷新渲染时自动绘制）

参数
:   |  |  |
    | --- | --- |
    | shape | 图形对象 |

**备注**

            传入图形可使用VMControls.WPF中名称以Ex结尾的图形结构体

## ◆ SetBackgroundImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool SetBackgroundImage | ( | IVmIO | *io* | ) |  |

设置背景图

## ◆ EnlargeView()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void EnlargeView | ( |  | ) |  |

放大视图

## ◆ ShrinkView()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ShrinkView | ( |  | ) |  |

缩小视图

## ◆ InitView()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void InitView | ( |  | ) |  |

还原视图

## ◆ ClearDisplayView()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearDisplayView | ( |  | ) |  |

清空渲染显示区域（包括图像和图形）

## ◆ SaveOriginalImage()

|  |  |  |  |
| --- | --- | --- | --- |
| void SaveOriginalImage | ( | string | *fileName*, |
|  |  | int | *jpgQuality* = `95` |
|  | ) |  |  |

保存原图

参数
:   |  |  |
    | --- | --- |
    | fileName | 图片路径 |
    | jpgQuality | 图片质量，范围[1,100]，数值越大质量越高，默认值95 |

## ◆ SaveRenderedImage()

|  |  |  |  |
| --- | --- | --- | --- |
| void SaveRenderedImage | ( | string | *fileName*, |
|  |  | int | *jpgQuality* = `95` |
|  | ) |  |  |

保存渲染图

参数
:   |  |  |
    | --- | --- |
    | fileName | 图片路径 |
    | jpgQuality | 图片质量，范围[1,100]，数值越大质量越高，默认值95 |

## ◆ SetBackground()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetBackground | ( | string | *value* | ) |  |

设置控件背景

参数
:   |  |  |
    | --- | --- |
    | value | 颜色字符串 |

**备注**

            参数为尺寸小于100\*100的图像绝对路径或#+16进制数表示的颜色字符串

## ◆ ConvertColor()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | static int ConvertColor | ( | byte | *bR*, | |  |  | byte | *bG*, | |  |  | byte | *bB* | |  | ) |  |  | | static |

将rgb格式的颜色转换为渲染控件可接受的数值，每个参数范围均为0-255

参数
:   |  |  |
    | --- | --- |
    | bR | R分量 |
    | bG | G分量 |
    | bB | B分量 |

返回
:   16进制颜色码

## ◆ SetRenderInterval()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRenderInterval | ( | int | *pMillseconds* | ) |  |

设置渲染间隔(ms)

参数
:   |  |  |
    | --- | --- |
    | pMillseconds | 渲染间隔 |

**备注**

            用于减低渲染频率。设置后，执行结束触发渲染时先校验距离上一次渲染的时间是否已超过设置的间隔时间，已超过则正常渲染，未超过则跳过此次渲染

## ◆ ChangeImageComboBoxVisibility()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ChangeImageComboBoxVisibility | ( | bool | *isImageComboBoxVisible* | ) |  |

控制图层选择控件显示隐藏

参数
:   |  |  |
    | --- | --- |
    | isImageComboBoxVisible | 是否可见 |

## ◆ GetSelectedImageDisplayName()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| string GetSelectedImageDisplayName | ( |  | ) |  |

获取当前选中图像名称

## ◆ SetRenderCondition()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRenderCondition | ( | RenderSatus | *status* | ) |  |

设置渲染条件（当设置条件status和模块状态值一致时才刷新）

参数
:   |  |  |
    | --- | --- |
    | status | 模块状态 |

## ◆ Dispose()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void Dispose | ( |  | ) |  |

释放资源

## ◆ SetRenderToolbarVisible()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRenderToolbarVisible | ( | bool | *isVisible* | ) |  |

工具栏是否可见

参数
:   |  |  |
    | --- | --- |
    | isVisible | 是否可见 |

## ◆ GetDisplayableImageNameList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<string> GetDisplayableImageNameList | ( |  | ) |  |

获取可显示的图像名称列表

## ◆ SetSelectedImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetSelectedImage | ( | string | *displayImageName* | ) |  |

选择一张图像作为显示图像

参数
:   |  |  |
    | --- | --- |
    | displayImageName | 显示的图像名称 |

## ◆ SwitchBackgroundImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SwitchBackgroundImage | ( | string | *backgroundImageName* | ) |  |

当图像堆叠时，切换背景图像

参数
:   |  |  |
    | --- | --- |
    | backgroundImageName | 背景图像名称 |

## ◆ AddStackImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void AddStackImage | ( | string | *displayImageName* | ) |  |

添加一张图像，进行图像堆叠。最新添加的图像显示在最顶层

参数
:   |  |  |
    | --- | --- |
    | displayImageName | 图像名称 |

## ◆ RemoveStackImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void RemoveStackImage | ( | string | *displayImageName* | ) |  |

指定图像名称，将其从当前堆叠显示的图像中删除

参数
:   |  |  |
    | --- | --- |
    | displayImageName | 图像名称 |

## 属性说明

## ◆ ModuleSource

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IVmModule ModuleSource | | getset |

数据源模块

## ◆ ImageSource

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IImageData ImageSource | | getset |

图像源

## ◆ CoordinateInfoVisible

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CoordinateInfoVisible | | getset |

是否显示坐标信息
