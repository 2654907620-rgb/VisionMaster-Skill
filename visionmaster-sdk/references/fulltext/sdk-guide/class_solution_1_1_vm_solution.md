<!-- src:class_solution_1_1_vm_solution.html -->
<!-- path:接口函数 > 方案 > VmSolution -->
# VmSolution类 参考 方案

方案
更多...

|  |  |
| --- | --- |
| Public 类型 | |
| enum | LogLevelConfig {     trace = 0x0,     debug = 0x1,     info = 0x2,     warn = 0x3,     err = 0x4,     critical = 0x5,     off = 0x6   } |
|  | 日志等级枚举。 更多... |
|  | |

|  |  |
| --- | --- |
| Public 成员函数 | |
| bool | HasPassword (string path) |
|  | 方案是否含有密码 更多... |
|  | |
| string | GetSolutionVersion (string strPath, string strPassWord) |
|  | 获取当前方案版本 更多... |
|  | |
| void | Import () |
|  | 加载方案 更多... |
|  | |
| void | Import (string path, string password) |
|  | 加载方案 更多... |
|  | |
| void | Load (string path, string password=null) |
|  | 加载方案 更多... |
|  | |
| void | Export (string path, string password) |
|  | 保存方案 更多... |
|  | |
| void | SaveAs (string path, string password=null) |
|  | 保存方案 更多... |
|  | |
| void | Save () |
|  | 保存方案 更多... |
|  | |
| void | Export (string path, bool bDisplayProgress) |
|  | 保存方案 更多... |
|  | |
| void | CloseSolution () |
|  | 关闭方案 更多... |
|  | |
| void | DeleteOneProcedure (string strProcedureName) |
|  | 删除流程 更多... |
|  | |
| void | DisableModulesCallback () |
|  | 禁用所有模块结果回调 更多... |
|  | |
| void | EnableModulesCallback () |
|  | 启用所有模块结果回调 更多... |
|  | |
| void | SetModuleResultBuffer (bool bBufferEnable, uint nBufferNum) |
|  | 设置模块结果缓存配置 更多... |
|  | |
| void | GetModuleResultBuffer (ref bool bBufferEnable, ref uint nBufferNum) |
|  | 获取模块结果缓存配置 更多... |
|  | |
| void | ClearHistoryResultData () |
|  | 清空方案内所有历史结果数据 更多... |
|  | |
| void | SetLogConfig (LogLevelConfig enLogLevel) |
|  | 实时日志调整 更多... |
|  | |
| void | CloseLogConfig () |
|  | 关闭日志配置（日志恢复默认等级） 更多... |
|  | |
| bool | IsSolModifyInfo () |
|  | 判断方案是否修改 更多... |
|  | |
| void | DisableProcedure (string strProcessName) |
|  | 禁用一个流程 更多... |
|  | |
| void | EnableProcedure (string strProcessName) |
|  | 启用一个流程 更多... |
|  | |
| bool | IsProcedureDisable (string strProcessName) |
|  | 流程是否禁用 更多... |
|  | |
| ProcessInfoList | GetAllProcedureList () |
|  | 获取当前方案中所有流程列表 更多... |
|  | |
| void | GetAllProcedureObjects (ref List< VmProcedure > procedures) |
|  | 获取当前方案中所有流程对象 更多... |
|  | |
| ModuleInfoList | GetAllModuleList () |
|  | 获取当前方案中所有模块列表 更多... |
|  | |
| void | SetRunInterval (uint nMillSecond) |
|  | 设置连续运行时间间隔 更多... |
|  | |
| uint | GetModuleCount () |
|  | 获取当前方案中模块总数 更多... |
|  | |
| void | SyncRun () |
|  | 同步执行一次 更多... |
|  | |
| override void | Run () |
|  | 执行一次 更多... |
|  | |
| override void | Dispose () |
|  | 释放所有资源，仅在退出程序前执行一次，避免在析构函数中调用 更多... |
|  | |

|  |  |
| --- | --- |
| 静态 Public 成员函数 | |
| static void | GetDongleInfo () |
|  | 获取加密狗信息，目前仅用于校验加密狗 更多... |
|  | |
| static void | CreatSolInstance () |
|  | 创建空方案 更多... |
|  | |

|  |  |
| --- | --- |
| Public 属性 | |
| override bool | ContinuousRunEnable |
|  | 连续运行/停止执行标志 更多... |
|  | |
| string | SolutionPath |
|  | 方案路径 更多... |
|  | |
| bool | IsHasPassword |
|  | 当前方案路径是否包含密码 更多... |
|  | |

|  |  |
| --- | --- |
| 静态 Public 属性 | |
| static VmSolution | Instance |
|  | 方案单例 更多... |
|  | |

|  |  |
| --- | --- |
| 事件 | |
| static WorkStatusCallBack | OnWorkStatusEvent |
|  | 流程工作状态 更多... |
|  | |
| static DongleCallBack | OnDongleEvent |
|  | 加密狗状态 更多... |
|  | |
| static ModuleSolutionLoadBeginCallBack | OnSolutionLoadBeginEvent |
|  | 开始加载方案 更多... |
|  | |
| static ModuleSolutionLoadEndCallBack | OnSolutionLoadEndEvent |
|  | 方案加载结束 更多... |
|  | |
| static ModuleSolutionLoadProcessCallBack | OnSolutionLoadProgressEvent |
|  | 模块方案加载进度 更多... |
|  | |
| static ServerStatusCallBack | OnServerStatusEvent |
|  | 服务状态回调 更多... |
|  | |
| static ProxyCrashNotice | OnProxyCrashEvent |
|  | 代理崩溃 更多... |
|  | |
| static ProcedureUnRegisterCallBack | OnProcedureUnRegisterEvent |
|  | 流程解注册状态信息 更多... |
|  | |
| static ModelLoadWarn | OnModelLoadWarnEvent |
|  | 方案加载时模块错误警告信息 更多... |
|  | |
| static ModuleStartContinuouslyProcessStatusCallBack | OnProcessStatusStartEvent |
|  | 连续执行开始状态信息 更多... |
|  | |
| static ModuleStopRunProcessStatusCallBack | OnProcessStatusStopEvent |
|  | 连续执行结束状态信息 更多... |
|  | |
| static ModuleResultExDataCallBack | OnModuleResultCallbackEvent |
|  | 模块结果信息回调 更多... |
|  | |
| static CommunicationDataCallBack | OnCommunicationRecvCallBackEvent |
|  | 接收数据回调 更多... |
|  | |
| static CommunicationDataCallBack | OnCommunicationStatusCallBackEvent |
|  | 通信状态回调（状态 设备ID（1字节）） 更多... |
|  | |
| static CameraCollectCallBack | OnCameraCollectStartCallBackEvent |
|  | 相机取图开始信息回调 更多... |
|  | |
| static CameraCollectCallBack | OnCameraCollectCallBackEvent |
|  | 相机取图结束信息回调 更多... |
|  | |
| static CameraConnectStatusCallBack | OnCameraConnectStatusCallBackEvent |
|  | 相机连接状态回调 更多... |
|  | |
| static ModuleInfoCallBack | OnGlobalCameraModuleAddedEvent |
|  | 相机模块添加事件 更多... |
|  | |
| static ModuleInfoCallBack | OnGlobalCameraModuleDeletedEvent |
|  | 相机模块删除事件 更多... |
|  | |
| static CommuConnectCallBack | OnCommuConnectCallBackEvent |
|  | 通信连接状态回调 更多... |
|  | |

## 详细描述

方案

## 成员枚举类型说明

## ◆ LogLevelConfig

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LogLevelConfig | | strong |

日志等级枚举。

| 枚举值 | |
| --- | --- |
| trace |  |
| debug | 最详细的日志级别 |
| info | 调试信息 |
| warn | 普通信息 |
| err | 警告信息 |
| critical | 错误信息 |
| off | 严重错误 |

## 成员函数说明

## ◆ GetDongleInfo()

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  | | --- | --- | --- | --- | --- | | static void GetDongleInfo | ( |  | ) |  | | static |

获取加密狗信息，目前仅用于校验加密狗

## ◆ CreatSolInstance()

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  | | --- | --- | --- | --- | --- | | static void CreatSolInstance | ( |  | ) |  | | static |

创建空方案

## ◆ HasPassword()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool HasPassword | ( | string | *path* | ) |  |

方案是否含有密码

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |

返回
:   有密码，返回true；无密码，返回false

## ◆ GetSolutionVersion()

|  |  |  |  |
| --- | --- | --- | --- |
| string GetSolutionVersion | ( | string | *strPath*, |
|  |  | string | *strPassWord* |
|  | ) |  |  |

获取当前方案版本

返回
:   方案版本号

## ◆ Import() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void Import | ( |  | ) |  |

加载方案

## ◆ Import() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| void Import | ( | string | *path*, |
|  |  | string | *password* |
|  | ) |  |  |

加载方案

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |
    | password | 密码 |

**备注**

            弃用，推荐 Load(string path, string password = null)

## ◆ Load()

|  |  |  |  |
| --- | --- | --- | --- |
| void Load | ( | string | *path*, |
|  |  | string | *password* = `null` |
|  | ) |  |  |

加载方案

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |
    | password | 密码 |

## ◆ Export() [1/2]

|  |  |  |  |
| --- | --- | --- | --- |
| void Export | ( | string | *path*, |
|  |  | string | *password* |
|  | ) |  |  |

保存方案

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |
    | password | 密码 |

**备注**

            弃用，推荐 SaveAs(string path, string password = null)

## ◆ SaveAs()

|  |  |  |  |
| --- | --- | --- | --- |
| void SaveAs | ( | string | *path*, |
|  |  | string | *password* = `null` |
|  | ) |  |  |

保存方案

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |
    | password | 密码 |

## ◆ Save()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void Save | ( |  | ) |  |

保存方案

**备注**

            保存使用最新路径和密码

## ◆ Export() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| void Export | ( | string | *path*, |
|  |  | bool | *bDisplayProgress* |
|  | ) |  |  |

保存方案

参数
:   |  |  |
    | --- | --- |
    | path | 方案路径 |
    | bDisplayProgress | 是否显示进度 |

## ◆ CloseSolution()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void CloseSolution | ( |  | ) |  |

关闭方案

## ◆ DeleteOneProcedure()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void DeleteOneProcedure | ( | string | *strProcedureName* | ) |  |

删除流程

参数
:   |  |  |
    | --- | --- |
    | strProcedureName | 流程名 |

## ◆ DisableModulesCallback()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void DisableModulesCallback | ( |  | ) |  |

禁用所有模块结果回调

**备注**

            禁用后要把需要的模块回调使能单独打开 CxxxTool.EnableResultCallback() ，否则无法再回调函数中拿到模块结果

## ◆ EnableModulesCallback()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void EnableModulesCallback | ( |  | ) |  |

启用所有模块结果回调

**备注**

            方案加载后，默认已启用所有模块回调

## ◆ SetModuleResultBuffer()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetModuleResultBuffer | ( | bool | *bBufferEnable*, |
|  |  | uint | *nBufferNum* |
|  | ) |  |  |

设置模块结果缓存配置

参数
:   |  |  |
    | --- | --- |
    | bBufferEnable | 缓存使能 |
    | nBufferNum | 缓存结果数量 |

## ◆ GetModuleResultBuffer()

|  |  |  |  |
| --- | --- | --- | --- |
| void GetModuleResultBuffer | ( | ref bool | *bBufferEnable*, |
|  |  | ref uint | *nBufferNum* |
|  | ) |  |  |

获取模块结果缓存配置

参数
:   |  |  |
    | --- | --- |
    | bBufferEnable | 缓存使能 |
    | nBufferNum | 缓存结果数量 |

## ◆ ClearHistoryResultData()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void ClearHistoryResultData | ( |  | ) |  |

清空方案内所有历史结果数据

**备注**

调用该接口不会清除模块结果缓存中的数据。

## ◆ SetLogConfig()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetLogConfig | ( | LogLevelConfig | *enLogLevel* | ) |  |

实时日志调整

## ◆ CloseLogConfig()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void CloseLogConfig | ( |  | ) |  |

关闭日志配置（日志恢复默认等级）

## ◆ IsSolModifyInfo()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| bool IsSolModifyInfo | ( |  | ) |  |

判断方案是否修改

返回
:   方案修改，返回true；方案未修改，返回false

## ◆ DisableProcedure()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void DisableProcedure | ( | string | *strProcessName* | ) |  |

禁用一个流程

参数
:   |  |  |
    | --- | --- |
    | strProcessName | 流程名称 |

## ◆ EnableProcedure()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void EnableProcedure | ( | string | *strProcessName* | ) |  |

启用一个流程

参数
:   |  |  |
    | --- | --- |
    | strProcessName | 流程名称 |

## ◆ IsProcedureDisable()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool IsProcedureDisable | ( | string | *strProcessName* | ) |  |

流程是否禁用

参数
:   |  |  |
    | --- | --- |
    | strProcessName | 流程名称 |

返回
:   流程禁用，返回true；流程启用，返回false

## ◆ GetAllProcedureList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ProcessInfoList GetAllProcedureList | ( |  | ) |  |

获取当前方案中所有流程列表

返回
:   流程列表

## ◆ GetAllProcedureObjects()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void GetAllProcedureObjects | ( | ref List< VmProcedure > | *procedures* | ) |  |

获取当前方案中所有流程对象

参数
:   |  |  |
    | --- | --- |
    | procedures | 流程对象列表 |

## ◆ GetAllModuleList()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ModuleInfoList GetAllModuleList | ( |  | ) |  |

获取当前方案中所有模块列表

返回
:   模块列表

## ◆ SetRunInterval()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetRunInterval | ( | uint | *nMillSecond* | ) |  |

设置连续运行时间间隔

参数
:   |  |  |
    | --- | --- |
    | nMillSecond | 时间间隔 |

## ◆ GetModuleCount()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| uint GetModuleCount | ( |  | ) |  |

获取当前方案中模块总数

返回
:   模块总数

## ◆ SyncRun()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| void SyncRun | ( |  | ) |  |

同步执行一次

## ◆ Run()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| override void Run | ( |  | ) |  |

执行一次

## ◆ Dispose()

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| override void Dispose | ( |  | ) |  |

释放所有资源，仅在退出程序前执行一次，避免在析构函数中调用

## 类成员变量说明

## ◆ Instance

|  |  |  |
| --- | --- | --- |
| |  | | --- | | VmSolution Instance | | static |

方案单例

## ◆ ContinuousRunEnable

|  |
| --- |
| override bool ContinuousRunEnable |

连续运行/停止执行标志

## ◆ SolutionPath

|  |
| --- |
| string SolutionPath |

方案路径

## ◆ IsHasPassword

|  |
| --- |
| bool IsHasPassword |

当前方案路径是否包含密码

## 事件说明

## ◆ OnWorkStatusEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | WorkStatusCallBack OnWorkStatusEvent | | static |

流程工作状态

## ◆ OnDongleEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | DongleCallBack OnDongleEvent | | static |

加密狗状态

## ◆ OnSolutionLoadBeginEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleSolutionLoadBeginCallBack OnSolutionLoadBeginEvent | | static |

开始加载方案

## ◆ OnSolutionLoadEndEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleSolutionLoadEndCallBack OnSolutionLoadEndEvent | | static |

方案加载结束

## ◆ OnSolutionLoadProgressEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleSolutionLoadProcessCallBack OnSolutionLoadProgressEvent | | static |

模块方案加载进度

## ◆ OnServerStatusEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ServerStatusCallBack OnServerStatusEvent | | static |

服务状态回调

## ◆ OnProxyCrashEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ProxyCrashNotice OnProxyCrashEvent | | static |

代理崩溃

## ◆ OnProcedureUnRegisterEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ProcedureUnRegisterCallBack OnProcedureUnRegisterEvent | | static |

流程解注册状态信息

## ◆ OnModelLoadWarnEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModelLoadWarn OnModelLoadWarnEvent | | static |

方案加载时模块错误警告信息

## ◆ OnProcessStatusStartEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleStartContinuouslyProcessStatusCallBack OnProcessStatusStartEvent | | static |

连续执行开始状态信息

## ◆ OnProcessStatusStopEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleStopRunProcessStatusCallBack OnProcessStatusStopEvent | | static |

连续执行结束状态信息

## ◆ OnModuleResultCallbackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleResultExDataCallBack OnModuleResultCallbackEvent | | static |

模块结果信息回调

## ◆ OnCommunicationRecvCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CommunicationDataCallBack OnCommunicationRecvCallBackEvent | | static |

接收数据回调

**备注**

            设备ID（1字节） AddressID（1字节） 数据

## ◆ OnCommunicationStatusCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CommunicationDataCallBack OnCommunicationStatusCallBackEvent | | static |

通信状态回调（状态 设备ID（1字节））

## ◆ OnCameraCollectStartCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CameraCollectCallBack OnCameraCollectStartCallBackEvent | | static |

相机取图开始信息回调

## ◆ OnCameraCollectCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CameraCollectCallBack OnCameraCollectCallBackEvent | | static |

相机取图结束信息回调

## ◆ OnCameraConnectStatusCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CameraConnectStatusCallBack OnCameraConnectStatusCallBackEvent | | static |

相机连接状态回调

## ◆ OnGlobalCameraModuleAddedEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleInfoCallBack OnGlobalCameraModuleAddedEvent | | static |

相机模块添加事件

## ◆ OnGlobalCameraModuleDeletedEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | ModuleInfoCallBack OnGlobalCameraModuleDeletedEvent | | static |

相机模块删除事件

## ◆ OnCommuConnectCallBackEvent

|  |  |  |
| --- | --- | --- |
| |  | | --- | | CommuConnectCallBack OnCommuConnectCallBackEvent | | static |

通信连接状态回调
