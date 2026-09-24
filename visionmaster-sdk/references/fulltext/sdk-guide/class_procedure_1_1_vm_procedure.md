<!-- src:class_procedure_1_1_vm_procedure.html -->
<!-- path:接口函数 > 流程 > VmProcedure -->
# VmProcedure类 参考 流程

流程
更多...

|  |  |
| --- | --- |
| Public 成员函数 | |
| override string | SaveAs (string strPath, string strPassword=null) |
|  | 导出流程 更多... |
|  | |
| void | ExportProcess (string strPath, string strPassword="") |
|  | 导出流程 更多... |
|  | |
| void | SetContinousRunInterval (uint nInterval) |
|  | 设置流程时间间隔 更多... |
|  | |
| void | Run () |
|  | 执行一次 更多... |
|  | |
| void | Run (bool bIsRespondToUI) |
|  | 执行一次 更多... |
|  | |
| void | Run (string strCommand, bool bIsWait=true, bool bIsRespondToUI=true) |
|  | 执行一次带触发字符串 更多... |
|  | |
| void | Run (string strCommand, ref uint nExecuteCount, bool bIsWait=true, bool bIsRespondToUI=true) |
|  | 执行一次带执行次数 更多... |
|  | |
| void | RunP2P (uint nTimeout, bool bIsRespondToUI=true) |
|  | 执行一次点对点模式 更多... |
|  | |
| uint | GetIsExecuteNormal () |
|  | 获取流程内模块是否全部执行正常 更多... |
|  | |
| ModuRunErrorInfo [] | GetModuErrorInfoList () |
|  | 获取流程内模块运行错误信息 更多... |
|  | |
| void | ClearHistoryResultData () |
|  | CH: 清空流程内所有历史结果数据 | EN: Clear All History Result Data in Procedure 更多... |
|  | |
| ModuleInfoList | GetAllModuleList () |
|  | 获取当前流程中所有模块列表 更多... |
|  | |
| ModuleInfoList | GetFirstLayerModuleTree () |
|  | 获取第一层级对象内部的模块树 更多... |
|  | |
| IntResultInfo | GetIntOutputResult (string strParam) |
|  | 获取整型配置导出结果 更多... |
|  | |
| FloatResultInfo | GetFloatOutputResult (string strParam) |
|  | 获取浮点型配置导出结果 更多... |
|  | |
| StringResultInfo | GetStringOutputResult (string strParam) |
|  | 获取字符串型配置导出结果 更多... |
|  | |
| ImageResultInfo | GetImageOutputResult (string strParam) |
|  | 获取图像型配置导出结果 更多... |
|  | |
| PointsetResultInfo | GetPointsetOutputResult (string strParam) |
|  | 获取点集型配置导出结果 更多... |
|  | |
| void | SetProcedureRunPolicy (ProcedureRunPolicy stPrcRunPolicy) |
|  | 设置流程运行策略 更多... |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static VmProcedure | Load (string strPath, string strPassword="", bool bIsOverrideGlobal=true) |
|  | 导入流程 更多... |
|  | |
| static VmProcedure | ImportProcess (string strPath, string strPassword="") |
|  | 导入流程 更多... |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| ProcedureResult | ModuResult |
|  | 模块结果对象 更多... |
|  | |
| override bool | ContinousRunEnable |
|  | 连续运行/停止执行标志 更多... |
|  | |
| bool | IsEnabled |
|  | 流程禁用/启用 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| ProcedureParam | ModuParams `[get, set]` |
|  | 模块参数对象 更多... |
|  | |
| IVarModule | LocalVariable `[get]` |
|  | 局部变量对象 更多... |
|  | |

## 详细描述

流程

## 成员函数说明

## ◆ Load()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | static VmProcedure Load | ( | string | *strPath*, | |  |  | string | *strPassword* = `""`, | |  |  | bool | *bIsOverrideGlobal* = `true` | |  | ) |  |  | | static |

导入流程

参数
:   |  |  |
    | --- | --- |
    | strPath | 路径 |
    | strPassword | 密码(预留) |
    | bIsOverrideGlobal | 是否覆盖全局模块，true:覆盖全局模块,false:忽略全局模块 |

返回

## ◆ SaveAs()

|  |  |  |  |
| --- | --- | --- | --- |
| override string SaveAs | ( | string | *strPath*, |
|  |  | string | *strPassword* = `null` |
|  | ) |  |  |

导出流程

参数
:   |  |  |
    | --- | --- |
    | strPath | 路径 |
    | strPassword | 密码(预留) |

返回

## ◆ ImportProcess()

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  | | --- | --- | --- | --- | | static VmProcedure ImportProcess | ( | string | *strPath*, | |  |  | string | *strPassword* = `""` | |  | ) |  |  | | static |

导入流程

参数
:   |  |  |
    | --- | --- |
    | strPath | 流程路径 |
    | strPassword | 流程密码 |

返回
:   流程对象

**备注**

弃用，推荐使用 Load() 接口。

## ◆ ExportProcess()

|  |  |  |  |
| --- | --- | --- | --- |
| void ExportProcess | ( | string | *strPath*, |
|  |  | string | *strPassword* = `""` |
|  | ) |  |  |

导出流程

参数
:   |  |  |
    | --- | --- |
    | strPath | 流程路径 |
    | strPassword | 流程密码 |

**备注**

弃用，推荐使用 SaveAs() 接口。

## ◆ SetContinousRunInterval()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetContinousRunInterval | ( | uint | *nInterval* | ) |  |

设置流程时间间隔

参数
:   |  |  |
    | --- | --- |
    | nInterval | 时间间隔（ms） |

## ◆ Run() [1/4]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void Run | ( |  | ) |  |

执行一次

## ◆ Run() [2/4]

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void Run | ( | bool | *bIsRespondToUI* | ) |  |

执行一次

参数
:   |  |  |
    | --- | --- |
    | bIsRespondToUI | 接口执行期间是否尝试响应界面操作，在UI线程中设置为true可避免阻塞界面，在非UI线程中设置为false可减小耗时波动 |

## ◆ Run() [3/4]

|  |  |  |  |
| --- | --- | --- | --- |
| void Run | ( | string | *strCommand*, |
|  |  | bool | *bIsWait* = `true`, |
|  |  | bool | *bIsRespondToUI* = `true` |
|  | ) |  |  |

执行一次带触发字符串

参数
:   |  |  |
    | --- | --- |
    | strCommand | 触发字符串 |
    | bIsWait | 是否等待执行结束 |
    | bIsRespondToUI | 接口执行期间是否尝试响应界面操作，在UI线程中设置为true可避免阻塞界面，在非UI线程中设置为false可减小耗时波动 |

## ◆ Run() [4/4]

|  |  |  |  |
| --- | --- | --- | --- |
| void Run | ( | string | *strCommand*, |
|  |  | ref uint | *nExecuteCount*, |
|  |  | bool | *bIsWait* = `true`, |
|  |  | bool | *bIsRespondToUI* = `true` |
|  | ) |  |  |

执行一次带执行次数

参数
:   |  |  |
    | --- | --- |
    | strCommand | 触发字符串 |
    | nExecuteCount | 执行次数 |
    | bIsWait | 是否等待执行结束 |
    | bIsRespondToUI | 接口执行期间是否尝试响应界面操作，在UI线程中设置为true可避免阻塞界面，在非UI线程中设置为false可减小耗时波动 |

## ◆ RunP2P()

|  |  |  |  |
| --- | --- | --- | --- |
| void RunP2P | ( | uint | *nTimeout*, |
|  |  | bool | *bIsRespondToUI* = `true` |
|  | ) |  |  |

执行一次点对点模式

参数
:   |  |  |
    | --- | --- |
    | nTimeout | 超时时间 |
    | bIsRespondToUI | 接口执行期间是否尝试响应界面操作，在UI线程中设置为true可避免阻塞界面，在非UI线程中设置为false可减小耗时波动 |

## ◆ GetIsExecuteNormal()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uint GetIsExecuteNormal | ( |  | ) |  |

获取流程内模块是否全部执行正常

返回
:   是否正常 1正常 0异常 默认为1

## ◆ GetModuErrorInfoList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ModuRunErrorInfo [] GetModuErrorInfoList | ( |  | ) |  |

获取流程内模块运行错误信息

返回
:   错误信息数组，数量上限16个

## ◆ ClearHistoryResultData()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearHistoryResultData | ( |  | ) |  |

CH: 清空流程内所有历史结果数据 | EN: Clear All History Result Data in Procedure

## ◆ GetAllModuleList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ModuleInfoList GetAllModuleList | ( |  | ) |  |

获取当前流程中所有模块列表

返回
:   模块列表

## ◆ GetFirstLayerModuleTree()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ModuleInfoList GetFirstLayerModuleTree | ( |  | ) |  |

获取第一层级对象内部的模块树

返回
:   模块列表

## ◆ GetIntOutputResult()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| IntResultInfo GetIntOutputResult | ( | string | *strParam* | ) |  |

获取整型配置导出结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 配置参数 |

返回
:   整型结果

**备注**

            弃用，推荐 ProcedureResult.GetOutputFloat(string strParam)

## ◆ GetFloatOutputResult()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| FloatResultInfo GetFloatOutputResult | ( | string | *strParam* | ) |  |

获取浮点型配置导出结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 配置参数 |

返回
:   浮点型结果

**备注**

            弃用，推荐 ProcedureResult.GetOutputFloat(string strParam)

## ◆ GetStringOutputResult()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| StringResultInfo GetStringOutputResult | ( | string | *strParam* | ) |  |

获取字符串型配置导出结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 配置参数 |

返回
:   字符串型结果

**备注**

            弃用，推荐 ProcedureResult.GetOutputString(string strParam)

## ◆ GetImageOutputResult()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| ImageResultInfo GetImageOutputResult | ( | string | *strParam* | ) |  |

获取图像型配置导出结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 配置参数 |

返回
:   图像型结果

## ◆ GetPointsetOutputResult()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| PointsetResultInfo GetPointsetOutputResult | ( | string | *strParam* | ) |  |

获取点集型配置导出结果

参数
:   |  |  |
    | --- | --- |
    | strParam | 配置参数 |

返回
:   点集型结果

## ◆ SetProcedureRunPolicy()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetProcedureRunPolicy | ( | ProcedureRunPolicy | *stPrcRunPolicy* | ) |  |

设置流程运行策略

参数
:   |  |  |
    | --- | --- |
    | stPrcRunPolicy | 运行策略信息 |

## 类成员变量说明

## ◆ ModuResult

|  |
| --- |
| ProcedureResult ModuResult |

模块结果对象

## ◆ ContinousRunEnable

|  |
| --- |
| override bool ContinousRunEnable |

连续运行/停止执行标志

## ◆ IsEnabled

|  |
| --- |
| bool IsEnabled |

流程禁用/启用

## 属性说明

## ◆ ModuParams

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ProcedureParam ModuParams | | getset |

模块参数对象

## ◆ LocalVariable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | IVarModule LocalVariable | | get |

局部变量对象
