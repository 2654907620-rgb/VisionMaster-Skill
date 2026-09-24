<!-- src:_xE6_x8E_xA5_xE6_x94_xB6_xE5_x92_x8C_xE5_x8F_x91_xE9_x80_x81_xE6_x95_xB0_xE6_x8D_xAE_xE7_x9A_x84_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:常见问题 > 全局模块控件中的通信管理如何接收和发送数据？ -->
# 全局通信：接收和发送数据的方法

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**二次开发中，全局模块控件中的通信管理如何接收和发送数据？

## 解决方法

* 通过 GetReadData() 接口接收数据，通过 SetInt() 或 SetString() 接口发送整型或字符串数据。代码如下：

  ```
  CommManagerModuleTool commTool = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];   //“通信管理1”是指当前运行的通信设备
  if(null !=null)
  {
      commTool.SetString(2, "abcd");                  //发送字符串型数据，接口函数SetString中的设备号2为通信管理中自动生成的设备序号
   int[] aIntVal = new int[3];
      aIntVal[0] = 10;
      aIntVal[1] = 11;
      aIntVal[2] = 12;
      commTool.SetInt(1, aIntVal, 0);                 //发送整型数据
   byte[] btData = null;
      commTool.GetReadData(2, ref btData);            //接收数据
  }
  ```
* 通过回调接收数据，代码如下：

  ```
  //添加HikExternalCall.dll引用，引用属性【复制到本地】改为false
  using HikExternalCall.Common;

  //注册回调函数，通讯接受事件回调
  VmSolution.OnCommunicationRecvCallBackEvent += VmSolution_OnCommunicationRecvCallBackEvent;
  private void VmSolution_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
  {
   string strMsg;
   try
      {
   int nType = reportDataInfo.nType;

   byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pData, reportDataInfo.nLen);
   int len = btarr.Length;
   string ID = btarr[0].ToString();
   byte[] vs = new byte[len - 2];
          Array.Copy(btarr, 2, vs, 0, len - 2);
   string ReceiveData = System.Text.Encoding.Default.GetString(vs);    //数据
          strMsg = ID + "号设备接受到：" + ReceiveData;
      }
   catch (VmException ex)
      {
         strMsg = "读取通信数据失败. Error Code: " + Convert.ToString(ex.errorCode, 16);
      }
  }

  //发送字符串数据
  public void SendCommDeviceData(int Num, string SendMessage)
  {
      CommManagerModuleTool commManagerModule = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];
   string strMsg;
   try
      {
   //获取通讯的连接状态
          if (commManagerModule.bIsDeviceConnect(Num))
          {
              commManagerModule.SetString(Num, SendMessage);              //给连接VM通讯的设备发送
              strMsg = "发送信号：" + SendMessage + "给" + Num + "号通讯设备";
          }
   else
          {
              strMsg = Num + "号通讯设备未打开";
          }
      }
   catch (Exception ex)
      {
          strMsg = "发送信号失败";
   return;
      }
  }
  ```
