<!-- src:class_i_m_v_s_cnn_register_multiclass_classification_modu_c_cs_1_1_i_m_v_s_cnn_register_multiclass_classification_modu_c_tool.html -->
<!-- path:接口函数 > 边缘学习 > 多类别分类CPU > IMVSCnnRegisterMulticlassClassificationModuCTool -->
# IMVSCnnRegisterMulticlassClassificationModuCTool类 参考 边缘学习 » 多类别分类CPU

多类别分类 CPU工具
更多...

继承自 VmModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | Run () |
|  | 模块自执行 更多... |
|  | |
| void | ExportModelData (string strPath) |
|  | 导出数据 更多... |
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
| CnnRegisterMulticlassClassificationCResult | ModuResult `[get]` |
|  | 模块结果对象 更多... |
|  | |
| CnnRegisterMulticlassClassificationCParam | ModuParams `[get, set]` |
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

多类别分类 CPU工具

## 成员函数说明

## ◆ Run()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| new void Run | ( |  | ) |  |

模块自执行

## ◆ ExportModelData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ExportModelData | ( | string | *strPath* | ) |  |

导出数据

## ◆ ImportModelData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ImportModelData | ( | string | *strPath* | ) |  |

导入数据

## 属性说明

## ◆ ModuResult

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CnnRegisterMulticlassClassificationCResult ModuResult | | get |

模块结果对象

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CnnRegisterMulticlassClassificationCParam ModuParams | | getset |

模块参数对象
