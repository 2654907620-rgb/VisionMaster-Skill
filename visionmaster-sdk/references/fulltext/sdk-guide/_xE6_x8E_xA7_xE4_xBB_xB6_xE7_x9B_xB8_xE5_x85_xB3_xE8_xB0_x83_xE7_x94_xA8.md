<!-- src:_xE6_x8E_xA7_xE4_xBB_xB6_xE7_x9B_xB8_xE5_x85_xB3_xE8_xB0_x83_xE7_x94_xA8.html -->
<!-- path:编程引导 > 控件相关调用 -->
# 控件相关调用

控件相关调用主要包括流程配置控件、参数配置控件、渲染控件、全局模块控件、前端运行界面控件等接口调用。

此处呈现几个常用控件的界面，如下图所示。

## 接口调用流程

控件相关调用接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

控件相关调用示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using VMControls.WPF.Release;
using VMControls.Winform.Release;
using GlobalCameraModuleCs;
using IMVSCircleFindModuCs;
using IMVSGroupCs;

namespace VM.Test
{
 public class ControlsTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //注意Winform或WPF控件需要从不同库文件引用，控件接口相似，示例代码以Winform为例

                #region 1.流程配置控件
                VMControls.Winform.Release.VmProcedureConfigControl vmProcedureConfigControl = new VMControls.Winform.Release.VmProcedureConfigControl();

 //根据流程名称绑定显示某个流程，控件默认显示所有流程
                vmProcedureConfigControl.BindSingleProcedure("流程1");

 //控件恢复显示所有流程
                vmProcedureConfigControl.BindMultiProcedure();

 //锁定工作区，不允许编辑方案
                vmProcedureConfigControl.LockWorkArea();

 //解锁工作区，允许编辑方案
                vmProcedureConfigControl.UnlockWorkArea();

 //锁定参数配置页，不允许编辑流程/Group/模块的参数配置页
                vmProcedureConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数配置页
                vmProcedureConfigControl.SetParamTabEditable(true);

 //设置控件自适应属性
                vmProcedureConfigControl.AutoSize = true;

 // 释放控件资源
                vmProcedureConfigControl.Dispose();
                #endregion

                #region 2.参数配置控件
                VMControls.Winform.Release.VmParamsConfigControl vmParamsConfigControl = new VMControls.Winform.Release.VmParamsConfigControl();

 //绑定流程对象，可配置其参数
                VmProcedure paramsConfigCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlProcess;

 //绑定Group对象，可配置其参数
                IMVSGroupTool paramsConfigCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlGroup;

 //绑定模块对象，可配置其参数
                IMVSCircleFindModuTool paramsConfigCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmParamsConfigControl.ModuleSource = paramsConfigCtrlCircleTool;

 //锁定参数配置页，不允许编辑流程/Group/模块的参数
                vmParamsConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数
                vmParamsConfigControl.SetParamTabEditable(true);

 //获取绑定模块参数配置页面的所有Tab名称
                vmParamsConfigControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmParamsConfigControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmParamsConfigControl.SetParamTabVisible(tabName, true);

 // 释放控件资源
                vmParamsConfigControl.Dispose();

                #endregion

                #region 3.渲染控件
                VMControls.Winform.Release.VmRenderControl vmRenderControl = new VMControls.Winform.Release.VmRenderControl();

 //绑定流程对象，执行后自动显示其图形图像
                VmProcedure renderCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmRenderControl.ModuleSource = renderCtrlProcess;

 //绑定Group对象，执行后自动显示其图形图像
                IMVSGroupTool renderCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmRenderControl.ModuleSource = renderCtrlGroup;

 //绑定模块对象，执行后自动显示其图形图像
                IMVSCircleFindModuTool renderCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmRenderControl.ModuleSource = renderCtrlCircleTool;

 //绘制图像，若控件已绑定对象，需考虑执行前后的时序配合
 VM.PlatformSDKCS.ImageBaseData renderCtrlImage = new VM.PlatformSDKCS.ImageBaseData();
                vmRenderControl.ImageSource = renderCtrlImage;

 //绘制图形，若控件已绑定对象，需考虑执行前后的时序配合
                VMControls.WPF.TextEx renderCtrlText = new VMControls.WPF.TextEx();
                renderCtrlText.Content = "Hello";
                vmRenderControl.DrawShape(renderCtrlText);

 //添加图形，控件需绑定对象，执行前添加，执行后显示
 //注意添加后图形数据仅当次执行有效，执行完成后清空，再次执行需再次添加
                renderCtrlText.Content = "Hello";
                vmRenderControl.AddShape(renderCtrlText);

 //清空当前显示的图形图像
                vmRenderControl.ClearDisplayView();

 //使用文件路径设置控件显示区背景图
 //注意该图片的尺寸需小于100*100
                vmRenderControl.SetBackground("D:\\background.bmp");

 //使用RGB数值设置控件显示区背景色
 //需传入“#+16进制数”表示的颜色字符串
                vmRenderControl.SetBackground("#FF00FF");

 //使用文件路径保存当前显示的原始图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmRenderControl.SaveOriginalImage("D:\\save.bmp");

 //使用文件路径保存当前显示的渲染图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmRenderControl.SaveRenderedImage("D:\\save.bmp");

 //隐藏图层选择控件
                vmRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmRenderControl.SwitchBackgroundImage(backgroundImageName);

 // 释放控件资源
                vmRenderControl.Dispose();


                #endregion

                #region 4.全局模块控件
                VMControls.Winform.Release.VmGlobalToolControl vmGlobalToolControl = new VMControls.Winform.Release.VmGlobalToolControl();

 //打开全局变量
                vmGlobalToolControl.OpenGlobalVariable();

 //打开全局脚本
                vmGlobalToolControl.OpenGlobalScript();

 //打开相机管理
                vmGlobalToolControl.OpenGlobalCamera();

 //打开通信管理
                vmGlobalToolControl.OpenCommunicationManager();

 //打开全局触发
                vmGlobalToolControl.OpenGlobalTrigger();

 // 释放控件资源
                vmGlobalToolControl.Dispose();

                #endregion

                #region 5.前端运行界面控件
                VMControls.Winform.Release.VmFrontendControl vmFrontendControl = new VMControls.Winform.Release.VmFrontendControl();

 //当前方案已配置运行界面，使用控件进行加载显示
                vmFrontendControl.LoadFrontendSource();

 //控件主动自适应大小
                vmFrontendControl.AutoChangeSize();

 //锁定运行界面关联的流程/Group/模块参数配置页，不允许编辑流程/Group/模块的参数
                vmFrontendControl.SetParamTabEditable(false);

 //解锁运行界面关联的流程/Group/模块参数配置页，允许编辑流程/Group/模块的参数
                vmFrontendControl.SetParamTabEditable(true);

 // 释放控件资源
                vmFrontendControl.Dispose();

                #endregion

                #region 6.主界面配置控件相关操作
                VMControls.Winform.Release.VmMainViewConfigControl vmMainViewConfigControl = new VMControls.Winform.Release.VmMainViewConfigControl();

 //根据流程名称绑定显示某个流程，控件默认显示所有流程
                vmMainViewConfigControl.BindSingleProcedure("流程1");

 //控件恢复显示所有流程
                vmMainViewConfigControl.BindMultiProcedure();

 //锁定工作区，不允许编辑方案
                vmMainViewConfigControl.LockWorkArea();

 //解锁工作区，允许编辑方案
                vmMainViewConfigControl.UnlockWorkArea();

 //锁定参数配置页，不允许编辑流程/Group/模块的参数配置页
                vmMainViewConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数配置页
                vmMainViewConfigControl.SetParamTabEditable(true);

 // 释放控件资源
                vmMainViewConfigControl.Dispose();
                #endregion

                #region 7.独立Group控件
                VMControls.Winform.Release.VmSingleModuleSetConfigControl vmSingleModuleSetConfigControl = new VMControls.Winform.Release.VmSingleModuleSetConfigControl();

 //绑定独立Group对象
                IMVSGroupTool groupTool = IMVSGroupTool.LoadIndependentGroup("D:\\test.gro");
                vmSingleModuleSetConfigControl.ModuleSource = groupTool;

 //锁定参数配置页，不允许编辑Group/模块的参数
                vmSingleModuleSetConfigControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑Group/模块的参数
                vmSingleModuleSetConfigControl.SetParamTabEditable(true);

 // 释放控件资源
                vmSingleModuleSetConfigControl.Dispose();
                #endregion

                #region 8.实时取流控件相关操作
                VMControls.Winform.Release.VmRealTimeAcqControl vmRealTimeAcqControl = new VMControls.Winform.Release.VmRealTimeAcqControl();

 //绑定待取流模块，仅支持全局相机模块
                vmRealTimeAcqControl.ModuleSource = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"];

 //全局相机模块选中对应相机，开始实时取流
                vmRealTimeAcqControl.StartGrabbing();

 //停止实时取流
                vmRealTimeAcqControl.StopGrabbing();

 //设置功能按钮可见
                vmRealTimeAcqControl.ShowButton(true);

 // 释放控件资源
                vmRealTimeAcqControl.Dispose();
                #endregion

                #region 9.参数配置带渲染控件
                VMControls.Winform.Release.VmParamsConfigWithRenderControl vmParamsConfigWithRenderControl = new VMControls.Winform.Release.VmParamsConfigWithRenderControl();

 //绑定流程对象，可配置其参数，并在执行后自动显示其图形图像
                VmProcedure paramRenderCtrlProcess = (VmProcedure)VmSolution.Instance["流程1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlProcess;

 //绑定Group对象，可配置其参数，并在执行后自动显示其图形图像
 //注意点击控件的执行按钮，仅该对象会自执行一次，其余模块无动作
 //注意自执行前需使用流程执行、接口设置等方式填充完毕对象执行所需输入数据，不然会执行错误
                IMVSGroupTool paramRenderCtrlGroup = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlGroup;

 //绑定模块对象，可配置其参数，并在执行后自动显示其图形图像
 //注意点击控件的执行按钮，仅该对象会自执行一次，其余模块无动作
 //注意自执行前需使用流程执行、接口设置等方式填充完毕对象执行所需输入数据，不然会执行错误
                IMVSCircleFindModuTool paramRenderCtrlCircleTool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                vmParamsConfigWithRenderControl.ModuleSource = paramRenderCtrlCircleTool;

 //锁定参数配置页，不允许编辑流程/Group/模块的参数
                vmParamsConfigWithRenderControl.SetParamTabEditable(false);

 //解锁参数配置页，允许编辑流程/Group/模块的参数
                vmParamsConfigWithRenderControl.SetParamTabEditable(true);

 //显示单/双画面模式切换按钮，双画面模式下渲染功能相关接口需使用参数区分所需操作画面
                vmParamsConfigWithRenderControl.MultiImageButtonVisible = true;

 //绘制图像，若控件已绑定对象，需考虑执行前后的时序配合
 VM.PlatformSDKCS.ImageBaseData paramRenderCtrlImage = new VM.PlatformSDKCS.ImageBaseData();
                vmParamsConfigWithRenderControl.ImageSource = paramRenderCtrlImage;

 //绘制图形，若控件已绑定对象，需考虑执行前后的时序配合
                VMControls.WPF.TextEx paramRenderCtrlText = new VMControls.WPF.TextEx();
                paramRenderCtrlText.Content = "Hello";
                vmParamsConfigWithRenderControl.DrawShape(paramRenderCtrlText);

 //添加图形，控件需绑定对象，执行前添加，执行后显示
 //注意添加后图形数据仅当次执行有效，执行完成后清空，再次执行需再次添加
                vmParamsConfigWithRenderControl.AddShape(paramRenderCtrlText);

 //清空当前显示的图形图像
                vmParamsConfigWithRenderControl.ClearDisplayView();

 //使用文件路径设置控件显示区背景图
                vmParamsConfigWithRenderControl.SetBackground("D:\\background.bmp");

 //使用RGB数值设置控件显示区背景色
                vmParamsConfigWithRenderControl.SetBackground("#FF00FF");

 //使用文件路径保存当前显示的原始图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmParamsConfigWithRenderControl.SaveOriginalImage("D:\\save.bmp");

 //使用文件路径保存当前显示的渲染图，存图功能建议使用输出图像模块
 //注意控件显示为异步刷新，不能保证严格配合执行前后的时序
                vmParamsConfigWithRenderControl.SaveRenderedImage("D:\\save.bmp");

 //获取绑定模块参数配置页面的所有Tab名称
                vmParamsConfigWithRenderControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmParamsConfigWithRenderControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmParamsConfigWithRenderControl.SetParamTabVisible(tabName, true);

 //隐藏图层选择控件
                vmParamsConfigWithRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmParamsConfigWithRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmParamsConfigWithRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmParamsConfigWithRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmParamsConfigWithRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmParamsConfigWithRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmParamsConfigWithRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmParamsConfigWithRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmParamsConfigWithRenderControl.SwitchBackgroundImage(backgroundImageName);
 //调整参数配置页面宽度
                vmParamsConfigWithRenderControl.SetParamConfigUIWidth(500);

 //窗口式参数渲染控件和该控件相似，可直接作为窗口显示，仅支持Winform
                VMControls.Winform.Release.VmParamsWithRenderForm vmParamsWithRenderForm = new VMControls.Winform.Release.VmParamsWithRenderForm();

 // 释放控件资源
                vmParamsConfigWithRenderControl.Dispose();
                #endregion

                #region 9.综合配置控件
                VMControls.Winform.Release.VmComprehensiveConfigWithRenderControl vmComprehensiveConfigWithRenderControl = new VMControls.Winform.Release.VmComprehensiveConfigWithRenderControl();

 //绑定对象，可配置其参数，并在执行后自动显示其图形图像
                vmComprehensiveConfigWithRenderControl.ModuleSource = VmSolution.Instance;

 //获取综合模块参数配置页面的所有Tab名称
                vmComprehensiveConfigWithRenderControl.GetParamTabNames();

 //隐藏tabName对应的tab页
                vmComprehensiveConfigWithRenderControl.SetParamTabVisible(tabName, false);

 //显示tabName对应的tab页
                vmComprehensiveConfigWithRenderControl.SetParamTabVisible(tabName, true);

 //隐藏图层选择控件
                vmComprehensiveConfigWithRenderControl.ChangeImageComboBoxVisibility(false);

 //显示图层选择控件
                vmComprehensiveConfigWithRenderControl.ChangeImageComboBoxVisibility(true);

 //隐藏渲染图像显示处工具栏
                vmComprehensiveConfigWithRenderControl.SetRenderToolbarVisible(false);

 //显示渲染图像显示处工具栏
                vmComprehensiveConfigWithRenderControl.SetRenderToolbarVisible(true);

 //获取渲染图像处显示的图像名称列表
                vmComprehensiveConfigWithRenderControl.GetDisplayableImageNameList();

 //设置图像显示，传入已获取到的图像名称列表中的成员名称
                vmComprehensiveConfigWithRenderControl.SetSelectedImage(displayImageName);

 //设置堆叠显示的图像，传入已获取到的图像名称列表中的成员名称
                vmComprehensiveConfigWithRenderControl.AddStackImage(displayImageName);

 //移除堆叠显示的图像，传入已堆叠显示的图像名称
                vmComprehensiveConfigWithRenderControl.RemoveStackImage(displayImageName);

 //当图像堆叠时，切换背景图像，传入已堆叠显示的图像名称
                vmComprehensiveConfigWithRenderControl.SwitchBackgroundImage(backgroundImageName);

 //调整参数配置页面宽度
                vmComprehensiveConfigWithRenderControl.SetParamConfigUIWidth(500);
 // 释放控件资源
                vmComprehensiveConfigWithRenderControl.Dispose();
                #endregion

 //退出程序前释放所有资源，注意避免在析构函数中调用
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
}
```
