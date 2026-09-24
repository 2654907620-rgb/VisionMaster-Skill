<!-- src:class_vm_params_config_with_render_control.html -->
<!-- path:接口函数 > 控件 > 参数配置带渲染控件 > VmParamsConfigWithRenderControl -->
# VmParamsConfigWithRenderControl类 参考 控件 » 参数配置带渲染控件

参数配置带渲染控件
更多...

继承自 UserControl .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | UpdateView () |
|  | 刷新 更多... |
|  | |
| void | DrawShape (object shape) |
|  | 绘制图形（立刻绘制） 更多... |
|  | |
| void | AddShape (object shape) |
|  | 添加图形 更多... |
|  | |
| bool | SetBackgroundImage (IVmIO io) |
|  | 设置背景图 更多... |
|  | |
| void | EnlargeView (int index=1) |
|  | 放大视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1 更多... |
|  | |
| void | ShrinkView (int index=1) |
|  | 缩小视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1 更多... |
|  | |
| void | InitView (int index=1) |
|  | 还原视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1 更多... |
|  | |
| void | ClearDisplayView (int index=1) |
|  | 清空渲染显示区域（包括图像和图形），双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1 更多... |
|  | |
| void | SaveOriginalImage (string fileName, int index=1, int jpgQuality=95) |
|  | 保存原图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1 更多... |
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
| string | GetSelectedImageDisplayName (int index=1) |
|  | 获取当前选中图像名称 更多... |
|  | |
| void | SetRenderCondition (RenderSatus status) |
|  | 设置渲染条件 更多... |
|  | |
| void | SetParamTabEditable (bool isEditable) |
|  | 流程、Group参数页中的添加、删除、编辑按钮是否可见 更多... |
|  | |
| void | SetMultiImageButtonVisible (bool isVisible) |
|  | 多画面切换按钮是否可见 更多... |
|  | |
| void | Dispose () |
|  | 释放资源 更多... |
|  | |
| List< string > | GetParamTabNames () |
|  | 获取所有Tab名称 更多... |
|  | |
| bool | SetParamTabVisible (string tabName, bool isVisible) |
|  | Tab页是否可见 更多... |
|  | |
| void | SetRenderToolbarVisible (bool isVisible) |
|  | 工具栏是否可见 更多... |
|  | |
| List< string > | GetImageViewList () |
|  | 获取可显示的图像名称列表 更多... |
|  | |
| void | SetImageView (string displayImageName) |
|  | 设置图像显示 更多... |
|  | |
| void | SwitchBackgroundImage (string backgroundImageName) |
|  | 当图像堆叠时，切换背景图像 更多... |
|  | |
| void | AddStackImage (string displayImageName) |
|  | 设置堆叠显示的图像 更多... |
|  | |
| void | RemoveStackImage (string displayImageName) |
|  | 移除堆叠显示的图像 更多... |
|  | |
| void | SetParamConfigUIWidth (int paramConfigUIWidth) |
|  | 设置参数配置页面的宽度 更多... |
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
| bool | ROIVisible `[get, set]` |
|  | 是否显示ROI 更多... |
|  | |
| bool | CoordinateInfoVisible `[get, set]` |
|  | 是否显示坐标信息 更多... |
|  | |
| bool | MultiImageButtonVisible `[get, set]` |
|  | 多画面切换按钮是否可见 更多... |
|  | |

## 详细描述

参数配置带渲染控件

## 成员函数说明

## ◆ UpdateView()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void UpdateView | ( |  | ) |  |

刷新

## ◆ DrawShape()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void DrawShape | ( | object | *shape* | ) |  |

绘制图形（立刻绘制）

**备注**

            传入图形可使用VMControls.WPF中名称以Ex结尾的图形结构体

## ◆ AddShape()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void AddShape | ( | object | *shape* | ) |  |

添加图形

**备注**

            在下次刷新渲染时自动绘制

传入图形可使用VMControls.WPF中名称以Ex结尾的图形结构体

## ◆ SetBackgroundImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool SetBackgroundImage | ( | IVmIO | *io* | ) |  |

设置背景图

## ◆ EnlargeView()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void EnlargeView | ( | int | *index* = `1` | ) |  |

放大视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1

## ◆ ShrinkView()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ShrinkView | ( | int | *index* = `1` | ) |  |

缩小视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1

## ◆ InitView()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void InitView | ( | int | *index* = `1` | ) |  |

还原视图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1

## ◆ ClearDisplayView()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ClearDisplayView | ( | int | *index* = `1` | ) |  |

清空渲染显示区域（包括图像和图形），双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1

## ◆ SaveOriginalImage()

|  |  |  |  |
| --- | --- | --- | --- |
| void SaveOriginalImage | ( | string | *fileName*, |
|  |  | int | *index* = `1`, |
|  |  | int | *jpgQuality* = `95` |
|  | ) |  |  |

保存原图，双画面显示时可指定操作某个画面，默认为右侧输出画面，index从左到右为0，1

参数
:   |  |  |
    | --- | --- |
    | fileName | 图片路径 |
    | index | 图片索引 |
    | jpgQuality | 图片质量，范围[1，100]，数值越大质量越高，默认值95 |

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
    | jpgQuality | 图片质量，范围[1，100]，数值越大质量越高，默认值95 |

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

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| string GetSelectedImageDisplayName | ( | int | *index* = `1` | ) |  |

获取当前选中图像名称

参数
:   |  |  |
    | --- | --- |
    | index | 图片索引 |

## ◆ SetRenderCondition()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRenderCondition | ( | RenderSatus | *status* | ) |  |

设置渲染条件

参数
:   |  |  |
    | --- | --- |
    | status | 模块状态 |

**备注**

            当设置条件status和模块状态值一致时才刷新

## ◆ SetParamTabEditable()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetParamTabEditable | ( | bool | *isEditable* | ) |  |

流程、Group参数页中的添加、删除、编辑按钮是否可见

参数
:   |  |  |
    | --- | --- |
    | isEditable | 是否可见，true表示按钮可见 |

## ◆ SetMultiImageButtonVisible()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetMultiImageButtonVisible | ( | bool | *isVisible* | ) |  |

多画面切换按钮是否可见

参数
:   |  |  |
    | --- | --- |
    | isVisible | 是否按钮显示 |

## ◆ Dispose()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void Dispose | ( |  | ) |  |

释放资源

## ◆ GetParamTabNames()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<string> GetParamTabNames | ( |  | ) |  |

获取所有Tab名称

## ◆ SetParamTabVisible()

|  |  |  |  |
| --- | --- | --- | --- |
| bool SetParamTabVisible | ( | string | *tabName*, |
|  |  | bool | *isVisible* |
|  | ) |  |  |

Tab页是否可见

参数
:   |  |  |
    | --- | --- |
    | tabName | tab页名称 |
    | isVisible | 是否可见 |

## ◆ SetRenderToolbarVisible()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRenderToolbarVisible | ( | bool | *isVisible* | ) |  |

工具栏是否可见

参数
:   |  |  |
    | --- | --- |
    | isVisible | 是否可见 |

## ◆ GetImageViewList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<string> GetImageViewList | ( |  | ) |  |

获取可显示的图像名称列表

## ◆ SetImageView()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetImageView | ( | string | *displayImageName* | ) |  |

设置图像显示

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

设置堆叠显示的图像

参数
:   |  |  |
    | --- | --- |
    | displayImageName | 图像名称 |

## ◆ RemoveStackImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void RemoveStackImage | ( | string | *displayImageName* | ) |  |

移除堆叠显示的图像

参数
:   |  |  |
    | --- | --- |
    | displayImageName | 图像名称 |

## ◆ SetParamConfigUIWidth()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetParamConfigUIWidth | ( | int | *paramConfigUIWidth* | ) |  |

设置参数配置页面的宽度

参数
:   |  |  |
    | --- | --- |
    | paramConfigUIWidth | 参数配置页面宽度 |

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

## ◆ ROIVisible

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool ROIVisible | | getset |

是否显示ROI

## ◆ CoordinateInfoVisible

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CoordinateInfoVisible | | getset |

是否显示坐标信息

## ◆ MultiImageButtonVisible

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool MultiImageButtonVisible | | getset |

多画面切换按钮是否可见
