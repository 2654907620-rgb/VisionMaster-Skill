<!-- src:_xE8_x8E_xB7_xE5_x8F_x96_xE5_x85_xA8_xE5_xB1_x80_xE7_x9B_xB8_xE6_x9C_xBA_xE5_x88_x97_xE8_xA1_xA8b02deeb67251996558131b9bd4fcb156.html -->
<!-- path:常见问题 > 如何获取全局相机列表和设置相机参数？ -->
# 全局相机：获取全局相机列表和设置相机参数的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何获取方案中所有全局相机的连接状态，并设置全局相机的基本参数？例如：在流程运行时查看全局相机1和2的连接状态，并设置全局相机1的曝光和增益。

## 解决方法

1. **获取方案中所有全局相机的连接状态：**V4.2.1版本新增获取相机连接状态的API，通过调用 GlobalCameraTool 类中的 bIsCameraConnect( )可获取相机的连接状态。若需查看方案中所有全局相机模块的连接状态，可参考以下的代码。
   * 在程序初始化时，启动查看相机状态的线程：

     ```
     //获取流程中所有全局相机模块
     List<GlobalCameraModuleTool> glCameralist = new List<GlobalCameraModuleTool>();
     List<VmModule> vmModules = new List<VmModule>();
     VmSolution.Instance.GetAllModule(vmModules);
     foreach(VmModule module in vmModules)
     {
      if(module.GetType()==typeof(GlobalCameraModuleTool))
         {
             glCameralist.Add((GlobalCameraModuleTool)module);
         }
     }

     //启动全局相机连接状态监控线程
     Thread watchThread = new Thread(new ParameterizedThreadStart(CameraConnectionWatchDog));
     watchThread.IsBackground = true;
     watchThread.Start(glCameralist);
     ```
   * 查看相机连接状态的线程函数：

     ```
     public void CameraConnectionWatchDog(object obj)
     {
         List<GlobalCameraModuleTool> globalCameraToolList = (List<GlobalCameraModuleTool>)obj;
      bool[] isCameraConected = new bool[globalCameraToolList.Count];
      while (true)
         {
      try
             {
      //获取流程中所有已配置的连接状态
      foreach (var cameraTool in globalCameraToolList)
                 {
      if (cameraTool.bIsCameraConnect() == false)
                     {
                         MessageBox.Show(string.Format($"警告: {cameraTool.Name} 已经离线！"));
                     }
                 }
             }
      catch (VmException ex)
             {
                 MessageBox.Show("发生致命错误，错误码:" + ex.errorCode);
             }
             Thread.Sleep(2000);
         }
     }
     ```
2. **设置全局相机的参数：**通过调用 GlobalCameraParam 类的方法和属性设置。以设置全局相机1的曝光和增益为例，相关代码如下：

   ```
   GlobalCameraModuleTool cameraModuleTool = VmSolution.Instance["全局相机1"] as GlobalCameraModuleTool;
   GlobalCameraParam globalCameraParam = cameraModuleTool.ModuParams;
   globalCameraParam.ExposureTime = 5000;
   globalCameraParam.Gain = 5.0;
   ```

注意
:   全局相机使用时若没有添加引用的工具，需进行以下操作：

1. 手动添加 GlobalCameraModuleCs.dll 引用。
2. 将引用属性的“复制到本地”选项设置为False。
3. 在程序代码文件中添加命名空间的引用。

   ```
   using GlobalCameraModuleCsl;
   ```
