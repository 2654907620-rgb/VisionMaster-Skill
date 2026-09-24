<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE7_xB1_xBB_xE5_x9E_x8B.html -->
<!-- path:编程引导 > 事件 > 事件类型 -->
# 事件类型

事件类型具体请见下表。

| 接口 | 类型 | C# 事件 | 描述 |
| --- | --- | --- | --- |
| **方案** | 流程工作状态 | OnWorkStatusEvent | 反馈流程执行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 加密狗状态 | OnDongleEvent | 反馈加密狗状态，在加密狗插拔等状态变更时触发 |
| 开始加载方案 | OnSolutionLoadBeginEvent | 反馈方案加载开始，方案加载期间其他大多数接口不支持调用，可用于屏蔽其他接口的调用 |
| 方案加载结束 | OnSolutionLoadEndEvent | 反馈方案加载结束，方案加载期间其他大多数接口不支持调用，可用于恢复其他接口的调用 |
| 模块方案加载进度 | OnSolutionLoadProgressEvent | 反馈方案加载的百分比进度，可用于粗略显示加载进度条 |
| 服务状态回调（VM单进程版本不触发此事件） | OnServerStatusEvent | 反馈服务进程状态，服务断线或崩溃时触发一次，单进程版本不触发 |
| 代理崩溃（VM单进程版本不触发此事件） | OnProxyCrashEvent | 反馈代理进程状态，代理断线或崩溃时触发一次，单进程版本不触发 |
| 流程解注册状态信息 | OnProcedureUnRegisterEvent | 反馈流程删除状态，每个流程被删除时触发一次 |
| 方案加载时模块错误警告信息 | OnModelLoadWarnEvent | 反馈方案加载中的警告，每个模块若由于系统环境等因素加载失败时触发一次 |
| 连续执行开始状态信息 | OnProcessStatusStartEvent | 反馈流程连续执行状态，每个流程开始连续执行时触发一次 |
| 连续执行结束状态信息 | OnProcessStatusStopEvent | 反馈流程连续执行状态，每个流程停止连续执行时触发一次 |
| 模块结果信息回调 | OnModuleResultCallbackEvent | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |
| 接收数据回调 | OnCommunicationRecvCallBackEvent | 反馈通信接收到的数据，每个通信设备接收到数据时触发一次 |
| 通信状态回调 | OnCommunicationStatusCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| 相机取图结束信息回调 | OnCameraCollectCallBackEvent | 反馈相机取图信息，每个全局相机每次取图结束时触发一次 |
| 相机取图开始信息回调 | OnCameraCollectStartCallBackEvent | 反馈相机取图信息，每个全局相机每次取图开始时触发一次 |
| 相机连接状态信息回调 | OnCameraConnectStatusCallBackEvent | 反馈相机连接状态信息，每个相机上下线及创建链接触发一次，可在回调中拿到相机相对应状态的数值 |
| 创建相机时模块信息回调 | OnGlobalCameraModuleAddedEvent | 反馈模块信息，创建全局相机模块时触发一次 |
| 删除相机时模块信息回调 | OnGlobalCameraModuleDeletedEvent | 反馈模块信息，删除全局相机模块时触发一次 |
| 通信连接状态回调 | OnCommuConnectCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| **流程** | 流程开始执行状态回调 | OnWorkBeginStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 流程执行结束状态回调 | OnWorkEndStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| **Group** | IO重命名事件 | OnModuleIONameChanged | 反馈Group输入输出设置修改，每个输入/输出名称修改时触发一次 |
| 显示IO重命名事件 | OnModuleDisplayParamNameChanged | 反馈Group显示设置修改，每个显示名称修改时触发一次 |
| **模块** | 模块结果回调 | ModuleResultCallBackArrived | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |
