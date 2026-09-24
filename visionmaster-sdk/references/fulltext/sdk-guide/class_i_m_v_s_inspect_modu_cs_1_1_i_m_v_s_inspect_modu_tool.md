<!-- src:class_i_m_v_s_inspect_modu_cs_1_1_i_m_v_s_inspect_modu_tool.html -->
<!-- path:接口函数 > 缺陷检测 > 异常检测 > IMVSInspectModuTool -->
# IMVSInspectModuTool类 参考 缺陷检测 » 异常检测

异常检测工具
更多...

继承自 VmModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | Run () |
|  | 模块自执行 更多... |
|  | |
| void | ImportModelData (string strPath) |
|  | 导入数据 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| InspectResult | ModuResult `[get]` |
|  | 模块结果对象 更多... |
|  | |
| InspectParam | ModuParams `[get, set]` |
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

异常检测工具

## 成员函数说明

## ◆ Run()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| new void Run | ( |  | ) |  |

模块自执行

## ◆ ImportModelData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ImportModelData | ( | string | *strPath* | ) |  |

导入数据

## 属性说明

## ◆ ModuResult

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InspectResult ModuResult | | get |

模块结果对象

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | InspectParam ModuParams | | getset |

模块参数对象
