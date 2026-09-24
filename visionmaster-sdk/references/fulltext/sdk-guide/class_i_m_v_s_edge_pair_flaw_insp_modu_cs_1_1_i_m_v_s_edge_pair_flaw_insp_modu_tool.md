<!-- src:class_i_m_v_s_edge_pair_flaw_insp_modu_cs_1_1_i_m_v_s_edge_pair_flaw_insp_modu_tool.html -->
<!-- path:接口函数 > 缺陷检测 > 边缘对模型缺陷检测 > IMVSEdgePairFlawInspModuTool -->
# IMVSEdgePairFlawInspModuTool类 参考 缺陷检测 » 边缘对模型缺陷检测

边缘对模型缺陷检测工具
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
| EdgePairFlawInspResult | ModuResult `[get]` |
|  | 模块结果对象 更多... |
|  | |
| EdgePairFlawInspParam | ModuParams `[get, set]` |
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

边缘对模型缺陷检测工具

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
| |  | | --- | | EdgePairFlawInspResult ModuResult | | get |

模块结果对象

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | EdgePairFlawInspParam ModuParams | | getset |

模块参数对象
