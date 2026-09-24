<!-- src:class_vm_params_config_control.html -->
<!-- path:接口函数 > 控件 > 参数配置控件 > VmParamsConfigControl -->
# VmParamsConfigControl类 参考 控件 » 参数配置控件

参数配置控件
更多...

继承自 UserControl .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | UpdateAllItem () |
|  | 更新所有项 更多... |
|  | |
| void | UpdataTab (int index) |
|  | 更新Tab页 更多... |
|  | |
| void | SetParamTabEditable (bool isEditable) |
|  | 流程、Group参数页中的添加、删除、编辑按钮是否可见 更多... |
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

|  |  |
| --- | --- |
| 属性 | |
| IVmModule | ModuleSource `[get, set]` |
|  | 数据源模块 更多... |
|  | |

## 详细描述

参数配置控件

## 成员函数说明

## ◆ UpdateAllItem()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void UpdateAllItem | ( |  | ) |  |

更新所有项

## ◆ UpdataTab()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void UpdataTab | ( | int | *index* | ) |  |

更新Tab页

参数
:   |  |  |
    | --- | --- |
    | index | 页序号 |

## ◆ SetParamTabEditable()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetParamTabEditable | ( | bool | *isEditable* | ) |  |

流程、Group参数页中的添加、删除、编辑按钮是否可见

参数
:   |  |  |
    | --- | --- |
    | isEditable | 是否可见，true表示按钮可见 |

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

## 属性说明

## ◆ ModuleSource

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IVmModule ModuleSource | | getset |

数据源模块
