<!-- src:class_i_m_v_s_group_cs_1_1_i_m_v_s_group_tool.html -->
<!-- path:接口函数 > 逻辑工具 > Group > IMVSGroupTool -->
# IMVSGroupTool类 参考 逻辑工具 » Group

Group工具
更多...

继承自 IMVSGroup .

|  |  |
| --- | --- |
| Public 成员函数 | |
| new void | Run (bool bIsRespondToUI=true) |
|  | 自执行一次 更多... |
|  | |
| void | ExportGroup (string strGroPath, string strPassword=null) |
|  | 保存Group至文件，弃用，推荐 SaveAs() 更多... |
|  | |
| string | SaveAs (string strGroPath, string strPassword=null) |
|  | 保存Group至文件（不支持导出方案中Group相关的连接订阅信息） 更多... |
|  | |
| GroupModuInfoList | GetAllModuleList () |
|  | 获取所有模块信息列表 更多... |
|  | |
| List< AllInOutParamList > | GetInputParamList () |
|  | 获取输入参数列表 更多... |
|  | |
| List< AllInOutParamList > | GetOutputParamList () |
|  | 获取输出参数列表 更多... |
|  | |
| void | ClearModuHistoryRes () |
|  | 清空历史结果缓存数据 更多... |
|  | |
| ModuRunErrorInfo [] | GetModuErrorInfoList () |
|  | 获取Group内模块运行错误信息 更多... |
|  | |
| void | DisableGroup () |
|  | 禁用Group 更多... |
|  | |
| void | EnableGroup () |
|  | 启用Group 更多... |
|  | |
| void | DestroyGroup () |
|  | 销毁独立Group 更多... |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static IMVSGroupTool | ImportGroup (string strPath, string strPassword="") |
|  | 导入独立Group，弃用，推荐使用 LoadIndependentGroup() 更多... |
|  | |
| static IMVSGroupTool | LoadIndependentGroup (string strPath, string strPassword="") |
|  | 导入独立Group 更多... |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| GroupResult | ModuResult |
|  | 模块结果对象 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| GroupParam | ModuParams `[get, set]` |
|  | 模块参数对象 更多... |
|  | |
| IVarModule | LocalVariable `[get]` |
|  | 局部变量对象 更多... |
|  | |

## 详细描述

Group工具

## 成员函数说明

## ◆ Run()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| new void Run | ( | bool | *bIsRespondToUI* = `true` | ) |  |

自执行一次

参数
:   |  |  |
    | --- | --- |
    | bIsRespondToUI | 接口执行期间是否尝试响应界面操作，在UI线程中设置为true可避免阻塞界面，在非UI线程中设置为false可减小耗时波动 |

**备注**

            只支持独立Group

## ◆ ExportGroup()

|  |  |  |  |
| --- | --- | --- | --- |
| void ExportGroup | ( | string | *strGroPath*, |
|  |  | string | *strPassword* = `null` |
|  | ) |  |  |

保存Group至文件，弃用，推荐 SaveAs()

## ◆ SaveAs()

|  |  |  |  |
| --- | --- | --- | --- |
| string SaveAs | ( | string | *strGroPath*, |
|  |  | string | *strPassword* = `null` |
|  | ) |  |  |

保存Group至文件（不支持导出方案中Group相关的连接订阅信息）

参数
:   |  |  |
    | --- | --- |
    | strGroPath | 路径 |
    | strPassword | 密码 |

返回

## ◆ GetAllModuleList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| GroupModuInfoList GetAllModuleList | ( |  | ) |  |

获取所有模块信息列表

## ◆ GetInputParamList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<AllInOutParamList> GetInputParamList | ( |  | ) |  |

获取输入参数列表

## ◆ GetOutputParamList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| List<AllInOutParamList> GetOutputParamList | ( |  | ) |  |

获取输出参数列表

## ◆ ClearModuHistoryRes()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearModuHistoryRes | ( |  | ) |  |

清空历史结果缓存数据

## ◆ GetModuErrorInfoList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ModuRunErrorInfo [] GetModuErrorInfoList | ( |  | ) |  |

获取Group内模块运行错误信息

返回
:   错误信息数组，数量上限16个

## ◆ DisableGroup()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void DisableGroup | ( |  | ) |  |

禁用Group

## ◆ EnableGroup()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void EnableGroup | ( |  | ) |  |

启用Group

## ◆ ImportGroup()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | static IMVSGroupTool ImportGroup | ( | string | *strPath*, | |  |  | string | *strPassword* = `""` | |  | ) |  |  | | static |

导入独立Group，弃用，推荐使用 LoadIndependentGroup()

## ◆ LoadIndependentGroup()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | static IMVSGroupTool LoadIndependentGroup | ( | string | *strPath*, | |  |  | string | *strPassword* = `""` | |  | ) |  |  | | static |

导入独立Group

## ◆ DestroyGroup()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void DestroyGroup | ( |  | ) |  |

销毁独立Group

## 类成员变量说明

## ◆ ModuResult

|  |
| --- |
| GroupResult ModuResult |

模块结果对象

## 属性说明

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | GroupParam ModuParams | | getset |

模块参数对象

## ◆ LocalVariable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IVarModule LocalVariable | | get |

局部变量对象
