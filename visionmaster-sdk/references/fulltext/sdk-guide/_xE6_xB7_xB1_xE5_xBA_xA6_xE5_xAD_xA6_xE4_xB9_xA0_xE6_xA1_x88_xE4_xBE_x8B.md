<!-- src:_xE6_xB7_xB1_xE5_xBA_xA6_xE5_xAD_xA6_xE4_xB9_xA0_xE6_xA1_x88_xE4_xBE_x8B.html -->
<!-- path:示例程序介绍 > 应用型示例程序 > 深度学习案例 -->
# 深度学习案例

## 一、应用场景

本案例作为VM二次开发的深度学习案例，适用场景为需要使用深度学习实现目标分类的场景。

## 二、搭建方案

示例方案路径：./PlatformSDKSampleCS/DeepLearningDemoCs/DeepLearningDemo.sol

### 方案思路

本演示案例为应用案例，软件和具体方案是强相关的。可加载设计好的方案，该演示方案为Demo文件夹下的DeepLearningDemo.sol方案。若导入其他案例提供的方案，则需进行相关配置方可运行出正确结果。

方案具体流程如下：

1. 在VisionTrain工具中打标训练深度学习模型文件，文件后缀为bin。
2. 在VisionMaster中拖拽图像源模块加载图像。
3. 拖拽DL分类C模块加载bin文件，实现模型预测任务。

注解
:   建议用格式化模块来组织需要输出的数据结果。

方案整体流程如下图所示。

### 耦合模块

方案的数据结果经过格式化模块汇总，并在流程“输出设置”中订阅，可在二次开发中拿流程输出结果，降低二次开发软件与具体模块的耦合性。

具体操作如下：

1. 点击流程图标旁边的小扳手图标进入流程配置窗口。
2. 通过输出设置配置流程输出结果参数，参数名为out，在二次开发中获取该参数就可以得到结果，具体如下图所示。
3. 通过显示设置配置方案的图像及渲染结果，用于在二次开发中绑定到渲染控件中显示，配置方式如下图所示。
4. 配置格式化模块内容。

   格式化模块必须配置正确。若使用时修改了案例自带的方案，特别是修改格式化模块订阅的数据，则必须参照案例自带的方案进行格式化模块配置，格式如下图所示。
   其中，主要包括检测结果、类别名称和类别准确率。具体格式为：[条件检测结果INT]，[数据项1]，[数据项2]

## 三、二次开发

### 运行逻辑

可在Visual Studio中直接调试运行本示例软件，也可在本工程Debug目录下双击DeepLearningDemoCs.exe 运行。DeepLearningDemo界面如下图所示。

**操作逻辑：**

1. 弹出软件运行界面后，在方案操作区域点击【选择方案】，选择完成后点击【加载方案】。
2. 在流程操作区域选择需要执行的流程名，点击【运行一次】或【连续执行】即可执行流程。

相关操作函数如下图所示。先选择方案函数和加载方案函数，再执行一次函数，最后流程执行回调函数（用于获取算法执行结果）。其中流程执行回调需要在构造函数中进行注册。

### 主要函数

本案例主要函数包括：方案加载、单次执行、连续执行、注册方案状态回调、获取结果、方案保存和渲染界面绑定。

* 方案加载

  ```
  VmSolution.Load(vmSolutionPath);            //参数为选择的方案路径
  VmSolution.Load(vmSolutionPath,”***”);      //参数为选择的方案路径，方案密码
  ```
* 单次执行：需要先实例化流程，然后调用VmProcedure类的Run成员函数执行算法流程。

  ```
  vmProcedure = (VmProcedure)VmSolution.Instance[comboProcedure.Text];    //实例化流程
  if(null == vmProcdure) return;
  vmProcedure.Run();      //流程执行接口
  ```
* 连续运行

  ```
  vmProcedure.ContinuousRunEnable = true;     //开启连续执行
  vmProcedure.ContinuousRunEnable = false;    //停止连续执行
  ```
* 方案状态回调

  ```
  VmSolution.OnWorkStatusEvent += VmSolution_OnWorkStatusEvent;   //注册方案状态回调
  private void VmSolution_OnWorkStatusEvent(VM.PlatformSDKCS.ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo) //回调函数实现
  {
   if (workStatusInfo.nWorkStatus == 0 && workStatusInfo.nProcessID == 10000)  //流程执行完毕，且为第一个流程
      {
   //获取结果
      }
  }
  ```
* 结果获取：流程执行完毕进入回调中取结果，首先在回调中实例化流程对象，然后调用ModuResult中的GetOutputString()接口来获取字符串结果，输入参数为变量名。

  ```
  VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance[“流程名称”];
  var vmResult = vmProcedure.ModuResult.GetOutputString(“out”)?.astStringVal[0].strValue;
  ```
* 方案保存

  ```
  VmSolution.Save();
  ```
* 渲染界面绑定

  ```
  vmRenderControl1.ModuleSource = (VmProcedure)VmSolution.Instance[“流程1”];
  ```

### 控件说明

本案例涉及3个控件，分别为VmRenderControl控件，VmMainViewConfigControl控件和VmGlobalToolControl控件。

* VmRenderControl控件：用于渲染图像数据。
* VmMainViewConfigControl控件：用于显示流程配置。
* VmGlobalToolControl控件：用于显示全局配置工具。
