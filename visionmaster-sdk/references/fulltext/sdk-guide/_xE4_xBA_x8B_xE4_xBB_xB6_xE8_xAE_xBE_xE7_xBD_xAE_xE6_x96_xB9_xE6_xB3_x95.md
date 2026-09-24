<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:编程引导 > 事件 > 事件设置方法 -->
# 事件设置方法

事件设置方法的示例代码如下，仅供参考。

```
using System;
using System.Text;
using VM.Core;
using VM.PlatformSDKCS;
using IMVSCircleFindModuCs;
using IMVSGroupCs;

namespace VM.Test
{
 public class EventTest
    {
 static void Main()
        {
 try
            {
                EventClass eventClass = new EventClass();

 // 初始化订阅方案事件
                eventClass.InitSubscribeSolutionEvent();

 // 加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
                if (null == vmProcedure) return;

 // 初始化订阅流程事件
                eventClass.InitSubscribeProcedureEvent(vmProcedure);

                IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                if (null == groupTool) return;

 // 初始化订阅Group事件
                eventClass.InitSubscribeGroupEvent(groupTool);

                IMVSCircleFindModuTool circleFindModule = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                if (null == circleFindModule) return;

 // 初始化订阅模块事件
                eventClass.InitSubscribeModuleEvent(circleFindModule);

 // 退出程序前释放所有资源，注意避免在析构函数中调用
                VmSolution.Instance?.Dispose();
            }
 catch (VmException vmex)
            {
 throw vmex;
            }
 catch (Exception ex)
            {
 throw ex;
            }
        }
    }

 public class EventClass
    {
 // 初始化订阅方案事件
 public void InitSubscribeSolutionEvent()
        {
 // 流程工作状态
            VmSolution.OnWorkStatusEvent += Handle_OnWorkStatusEvent;

 // 加密狗状态
            VmSolution.OnDongleEvent += Handle_OnDongleEvent;

 // 开始加载方案
            VmSolution.OnSolutionLoadBeginEvent += Handle_OnSolutionLoadBeginEvent;

 // 方案加载结束
            VmSolution.OnSolutionLoadEndEvent += Handle_OnSolutionLoadEndEvent;

 // 模块方案加载进度
            VmSolution.OnSolutionLoadProgressEvent += Handle_OnSolutionLoadProgressEvent;

 // 服务状态回调，VM单进程版本不触发此事件
            VmSolution.OnServerStatusEvent += Handle_OnServerStatusEvent;

 // 代理崩溃，VM单进程版本不触发此事件
            VmSolution.OnProxyCrashEvent += Handle_OnProxyCrashEvent;

 // 流程解注册状态信息
            VmSolution.OnProcedureUnRegisterEvent += Handle_OnProcedureUnRegisterEvent;

 // 方案加载时模块错误警告信息
            VmSolution.OnModelLoadWarnEvent += Handle_OnModelLoadWarnEvent;

 // 连续执行开始状态信息
            VmSolution.OnProcessStatusStartEvent += Handle_OnProcessStatusStartEvent;

 // 连续执行结束状态信息
            VmSolution.OnProcessStatusStopEvent += Handle_OnProcessStatusStopEvent;

 // 模块结果信息回调
            VmSolution.OnModuleResultCallbackEvent += Handle_OnModuleResultCallbackEvent;

 // 接收数据回调（设备ID（1字节） AddressID（1字节） 数据）
            VmSolution.OnCommunicationRecvCallBackEvent += Handle_OnCommunicationRecvCallBackEvent;

 // 通信状态回调（状态 设备ID（1字节））
            VmSolution.OnCommunicationStatusCallBackEvent += Handle_OnCommunicationStatusCallBackEvent;

 // 相机取图结束信息回调
            VmSolution.OnCameraCollectCallBackEvent += Handle_OnCameraCollectCallBackEvent;

 // 相机取图开始信息回调
            VmSolution.OnCameraCollectStartCallBackEvent += Handle_OnCameraCollectStartCallBackEvent;

 // 通信连接状态回调
            VmSolution.OnCommuConnectCallBackEvent += Handle_OnCommuConnectCallBackEvent;

 // 相机连接状态回调
            VmSolution.OnCameraConnectStatusCallBackEvent += Handle_OnCameraConnectStatusCallBackEvent;

 // 相机模块添加事件
            VmSolution.OnGlobalCameraModuleAddedEvent += Handle_OnGlobalCameraModuleAddedEvent;

 // 相机模块删除事件
            VmSolution.OnGlobalCameraModuleDeletedEvent += Handle_OnGlobalCameraModuleDeletedEvent;
        }

 // 初始化订阅流程事件
 public void InitSubscribeProcedureEvent(VmProcedure vmProcedure)
        {
 // 流程开始执行状态回调
            vmProcedure.OnWorkBeginStatusCallBack += Handle_OnWorkBeginStatusCallBack;

 // 流程执行结束状态回调
            vmProcedure.OnWorkEndStatusCallBack += Handle_OnWorkEndStatusCallBack;
        }

 // 初始化订阅Group事件
 public void InitSubscribeGroupEvent(IMVSGroupTool groupModuTool)
        {
 // IO重命名事件
            groupModuTool.OnModuleIONameChanged += Handle_OnModuleIONameChanged;

 // 显示IO重命名事件
            groupModuTool.OnModuleDisplayParamNameChanged += Handle_OnModuleDisplayParamNameChanged;
        }

 // 初始化订阅模块事件
 public void InitSubscribeModuleEvent(VmModule vmModule)
        {
 // 模块结果回调
            vmModule.ModuleResultCallBackArrived += Handle_ModuleResultCallBackArrived;
        }

 // Solution 方案回调函数
 private void Handle_OnWorkStatusEvent(ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo)
        {
 // 获取流程ID，多个流程时用于区分流程
            uint processID = workStatusInfo.nProcessID;

 // 获取流程状态，1运行开始，0运行结束
            uint workStatus = workStatusInfo.nWorkStatus;

 // 获取流程耗时，仅在运行结束时有效
 float processTime = workStatusInfo.fProcessTime;
        }
 private void Handle_OnDongleEvent(ImvsSdkDefine.IMVS_DONGLE_INFO moduleInfo)
        {
 // 获取加密狗状态，正常时为0，异常时为错误码
 int dongleStatus = moduleInfo.nDongleStatus;

 // 获取加密狗型号
 byte[] bytDongleType = moduleInfo.strDongleType;
 string str = Encoding.UTF8.GetString(bytDongleType).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadBeginEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_BEGEIN_INFO solutionLoadBeginInfo)
        {
 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadBeginInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');

        }
 private void Handle_OnSolutionLoadEndEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO solutionLoadEndInfo)
        {
 // 获取加载方案状态，正常时为0，异常时为错误码
            uint status = solutionLoadEndInfo.nStatus;

 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadEndInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadProgressEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_PROCESS_INFO solutionLoadProcessInfo)
        {
 // 获取加载方案的百分比进度，取值范围0~100
            uint process = solutionLoadProcessInfo.nProcess;

        }
 private void Handle_OnServerStatusEvent(ImvsSdkDefine.IMVS_SERVER_INFO moduleInfo)
        {
 // 获取服务进程状态，单进程版本不触发
            uint serverStatus = moduleInfo.nServerStatus;

        }
 private void Handle_OnProxyCrashEvent(ImvsSdkDefine.IMVS_PROXY_CRASH_SP_INFO proxyCrashInfoo)
        {
 // 获取代理进程状态，单进程版本不触发
 int hasSolStatu = proxyCrashInfoo.nHasSolStatu;

        }
 private void Handle_OnProcedureUnRegisterEvent(ImvsSdkDefine.IMVS_PROCEDURE_UNREGISTER_INFO procedureUnregisterInfo)
        {
 // 获取删除流程ID
            uint processID = procedureUnregisterInfo.nProcessID;

 // 获取删除流程名称
 byte[] strProcessName = procedureUnregisterInfo.strProcessName;
 string str = Encoding.UTF8.GetString(strProcessName).TrimEnd('\0');
        }
 private void Handle_OnModelLoadWarnEvent(ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO_LIST loadModuleInfoList)
        {
 // 获取加载方案时，加载失败模块的信息，包括模块ID/名称等
            uint moduleNum = loadModuleInfoList.nModuleNum;
 VM.PlatformSDKCS.ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO[] astLoadModuErrInfo = loadModuleInfoList.astLoadModuErrInfo;
        }
 private void Handle_OnProcessStatusStartEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_START_CONTINUOUSLY_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnProcessStatusStopEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_STOP_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnModuleResultCallbackEvent(ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data moduleResultExInfo)
        {
 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = moduleResultExInfo.nErrorCode;

 // 获取流程/Group/模块ID
            uint moduleID = moduleResultExInfo.nModuleID;

 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = moduleResultExInfo.fModuleTime;

 // 获取流程/Group/模块算法耗时
 float algorithmTime = moduleResultExInfo.fAlgorithmTime;

 // 获取流程/Group/模块运行结果数据
 int resultNum = moduleResultExInfo.nResultNum;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data[] pInfo = moduleResultExInfo.pInfo;
 if (resultNum > 0)
            {
 // 获取其中一个结果数据
                ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data pTmpData = pInfo[0];
 // 获取结果数据名称
 string str = pTmpData.strParamName;
            }
        }
 private void Handle_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 获取接收该数据的设备的类型
 int type = reportDataInfo.nType;

 // 获取接收的数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCommunicationStatusCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 该事件使用较复杂，建议使用事件OnCommuConnectCallBackEvent
 // 获取通信状态变更的设备的类型
 int type = reportDataInfo.nType;

 // 获取通信状态变更数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCameraConnectStatusCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_CONNECT_STATUS_INFO cameraConnectStatusInfo)
        {
 // 获取相机ID
 int cameraID = cameraConnectStatusInfo->nCameraID;

 // 获取相机连接状态
 int connectStatus = cameraConnectStatusInfo->nConnectStatus;

 // 获取相机SN
 byte[] strCameraSN = cameraConnectStatusInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnGlobalCameraModuleAddedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnGlobalCameraModuleDeletedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnCameraCollectCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图结束的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图结束的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCameraCollectStartCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图开始的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图开始的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCommuConnectCallBackEvent(ImvsSdkDefine.IMVS_COMMUNICATION_CONNECT_INFO connectCollectInfo)
        {
 // 获取通信状态变更后的状态，连接为1，断开为0
            uint deviceStatus = connectCollectInfo.nDeviceStatus;

 // 获取通信状态变更的设备ID
            uint deviceID = connectCollectInfo.nDeviceID;
        }

 // Procedure 流程回调函数
 private void Handle_OnWorkBeginStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;
        }
 private void Handle_OnWorkEndStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;

 // 获取流程耗时
 float processTime = data.fProcessTime;
        }

 // Group 组合模块回调函数
 private void Handle_OnModuleIONameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }
 private void Handle_OnModuleDisplayParamNameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }

 // Module 模块回调函数
 private void Handle_ModuleResultCallBackArrived(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data data = (ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data)eventArgs.Value;

 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = data.nErrorCode;
 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = data.fModuleTime;
 // 获取流程/Group/模块算法耗时
 float algorithmTime = data.fAlgorithmTime;

 // 获取运行结果数据
            if (data.nResultNum > 0)
            {
 // 获取其中一个结果数据的名称
 string str = data.pInfo[0].strParamName;
            }
        }
    }
}
```
