<!-- src:_xE8_xAE_xBE_xE7_xBD_xAE_xE8_xBE_x93_xE5_x85_xA5_xE5_x9B_xBE_xE5_x83_x8F_xE3_x80_x81_xE5_x8F_x822a9f51fe6886ae7374f210fb286317fd.html -->
<!-- path:常见问题 > 如何设置模块输入图像、参数和ROI区域？ -->
# 模块操作：设置输入图像、参数和ROI区域的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何设置模块的输入图像、模块参数及ROI区域？

## 解决方法

VM模块的输入主要包含两部分：基本参数（图像输入、ROI区域）和运行参数。

除图像源模块以及无输入图像的模块以外，在SDK二次开发时，可通过代码修改模块的输入参数。以下内容以圆查找模块为例进行介绍。

1. 设置模块输入图像，添加相应的命名空间 IMVSCircleFindModuCs 。

   ```
   Mat matImagee = Cv2.ImRead("D:\\3.ProjectCode\\VM4.3\\1.bmp", ImreadModes.Grayscale);
   IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["流程3.圆查找1"] as IMVSCircleFindModuTool;  //实例化指定的模块工具
   ImageBaseData StImgbase = new ImageBaseData(matImagee.Data, (uint)(matImagee.Width * matImagee.Height), matImagee.Width, matImagee.Height, VMPixelFormat.VM_PIXEL_MONO_08);
   circleFindModuTool.ModuParams.InputImage = StImgbase;
   ```
2. 通过调用对象中 ModuParams 的属性设置模块运行参数。

   ```
   IMVSCircleFindModuTool circleFindModuTool = VmSolution.Instance["流程1.圆查找1"] as IMVSCircleFindModuTool;  //实例化指定的模块工具
   circleFindModuTool.ModuParams.EdgeThresh = 30;  //设置边缘阈值为30
   ```
3. 设置指定模块的ROI区域。

   ```
   IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
   RectBox rectBox = new RectBox(new VM.PlatformSDKCS.PointF(1000, 1000), 500, 500, 0);
   tool.ModuParams.ModuRoiManager.RoiRectangle = rectBox;      //代码设置ROI
   ```

注意
:   * 设置【基本参数】，参数配置窗口界面不会显示所设置的参数。此时若模块运行，则参数永久有效；若流程运行，则参数一次有效。
    * 设置【运行参数】，参数配置窗口界面会显示所设置的参数。此时模块和流程运行，参数均永久有效。
