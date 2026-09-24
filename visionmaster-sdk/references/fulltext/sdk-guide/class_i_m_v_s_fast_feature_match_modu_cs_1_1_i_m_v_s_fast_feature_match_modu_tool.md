<!-- src:class_i_m_v_s_fast_feature_match_modu_cs_1_1_i_m_v_s_fast_feature_match_modu_tool.html -->
<!-- path:接口函数 > 定位 > 快速匹配 > IMVSFastFeatureMatchModuTool -->
# IMVSFastFeatureMatchModuTool类 参考 定位 » 快速匹配

快速匹配工具
更多...

继承自 VmModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | Run () |
|  | 模块自执行 更多... |
|  | |
| int | GetModelNum () |
|  | 获取模型数量 更多... |
|  | |
| void | ExportModelData (ImvsSdkDefine.IMVS\_EXPORT\_MODE\_DATA\_INFO[] exportInfo) |
|  | 导出数据 更多... |
|  | |
| void | ImportModelData (string[] strPaths) |
|  | 导入数据 更多... |
|  | |
| void | ClearModelData () |
|  | 清除所有模型数据 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| FastFeatureMatchResult | ModuResult `[get]` |
|  | 模块结果对象 更多... |
|  | |
| FastFeatureMatchParam | ModuParams `[get, set]` |
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

快速匹配工具

## 成员函数说明

## ◆ Run()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| new void Run | ( |  | ) |  |

模块自执行

## ◆ GetModelNum()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| int GetModelNum | ( |  | ) |  |

获取模型数量

## ◆ ExportModelData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ExportModelData | ( | ImvsSdkDefine.IMVS\_EXPORT\_MODE\_DATA\_INFO [] | *exportInfo* | ) |  |

导出数据

## ◆ ImportModelData()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void ImportModelData | ( | string [] | *strPaths* | ) |  |

导入数据

## ◆ ClearModelData()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearModelData | ( |  | ) |  |

清除所有模型数据

## 属性说明

## ◆ ModuResult

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FastFeatureMatchResult ModuResult | | get |

模块结果对象

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | FastFeatureMatchParam ModuParams | | getset |

模块参数对象
