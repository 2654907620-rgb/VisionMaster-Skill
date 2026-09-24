<!-- src:class_vm_comprehensive_config_with_render_control.html -->
<!-- path:接口函数 > 控件 > 综合配置控件 > VmComprehensiveConfigWithRenderControl -->
# VmComprehensiveConfigWithRenderControl类 参考 控件 » 综合配置控件

综合配置控件
更多...

继承自 UserControl .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | ChangeImageComboBoxVisibility (bool isImageComboBoxVisible) |
|  | 控制图层选择控件显示隐藏 更多... |
|  | |
| void | Dispose () |
|  | 释放资源 更多... |
|  | |
| List< string > | GetParamTabNames () |
|  | 获取所有Tab名称 更多... |
|  | |
| void | SetParamTabVisible (string tabName, bool isVisible) |
|  | Tab页是否可见 更多... |
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
| 属性 | |
| IVmModule | SolutionSource `[get, set]` |
|  | 数据源方案 更多... |
|  | |

## 详细描述

综合配置控件

## 成员函数说明

## ◆ ChangeImageComboBoxVisibility()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ChangeImageComboBoxVisibility | ( | bool | *isImageComboBoxVisible* | ) |  |

控制图层选择控件显示隐藏

参数
:   |  |  |
    | --- | --- |
    | isImageComboBoxVisible | 是否可见 |

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
| void SetParamTabVisible | ( | string | *tabName*, |
|  |  | bool | *isVisible* |
|  | ) |  |  |

Tab页是否可见

参数
:   |  |  |
    | --- | --- |
    | tabName | tab页名称 |
    | isVisible | 是否可见 |

带参数配置的控件如果绑定同一个数据源，调用此接口会同步更新“与tabName对应的参数配置Tab页”的显示隐藏

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

## ◆ SolutionSource

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IVmModule SolutionSource | | getset |

数据源方案
