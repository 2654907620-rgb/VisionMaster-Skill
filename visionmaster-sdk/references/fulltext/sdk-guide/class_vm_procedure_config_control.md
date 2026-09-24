<!-- src:class_vm_procedure_config_control.html -->
<!-- path:接口函数 > 控件 > 流程配置控件 > VmProcedureConfigControl -->
# VmProcedureConfigControl类 参考 控件 » 流程配置控件

流程配置控件
更多...

继承自 UserControl .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | BindSingleProcedure (string name) |
|  | 根据流程名称绑定单流程 更多... |
|  | |
| void | BindMultiProcedure () |
|  | 绑定多流程 更多... |
|  | |
| void | LockWorkArea () |
|  | 锁定工作区 更多... |
|  | |
| void | UnlockWorkArea () |
|  | 解除锁定工作区 更多... |
|  | |
| void | SetParamTabEditable (bool isEditable) |
|  | 流程、Group参数页中的添加、删除、编辑按钮是否可见 更多... |
|  | |
| void | Dispose () |
|  | 释放资源 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| IntPtr | WinformHandle `[get, set]` |
|  | Winform窗口句柄 更多... |
|  | |

## 详细描述

流程配置控件

## 成员函数说明

## ◆ BindSingleProcedure()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void BindSingleProcedure | ( | string | *name* | ) |  |

根据流程名称绑定单流程

## ◆ BindMultiProcedure()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void BindMultiProcedure | ( |  | ) |  |

绑定多流程

## ◆ LockWorkArea()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void LockWorkArea | ( |  | ) |  |

锁定工作区

## ◆ UnlockWorkArea()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void UnlockWorkArea | ( |  | ) |  |

解除锁定工作区

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

## 属性说明

## ◆ WinformHandle

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IntPtr WinformHandle | | getset |

Winform窗口句柄
