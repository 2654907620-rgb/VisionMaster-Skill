<!-- src:class_vm_params_with_render_form.html -->
<!-- path:接口函数 > 控件 > 参数配置带渲染弹出控件 > VmParamsWithRenderForm -->
# VmParamsWithRenderForm类 参考 控件 » 参数配置带渲染弹出控件

参数配置带渲染弹出控件
更多...

继承自 Form .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | UpdateView () |
|  | 刷新 更多... |
|  | |
| void | DrawShape (object shape) |
|  | 绘制形状 更多... |
|  | |
| bool | SetBackgroundImage (IVmIO io) |
|  | 设置背景图 更多... |
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

## 详细描述

参数配置带渲染弹出控件

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

绘制形状

## ◆ SetBackgroundImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool SetBackgroundImage | ( | IVmIO | *io* | ) |  |

设置背景图

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
