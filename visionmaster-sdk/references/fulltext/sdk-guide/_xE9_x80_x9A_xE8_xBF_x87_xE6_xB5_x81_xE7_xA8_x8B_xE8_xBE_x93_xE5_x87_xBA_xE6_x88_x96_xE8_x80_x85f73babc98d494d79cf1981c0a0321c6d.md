<!-- src:_xE9_x80_x9A_xE8_xBF_x87_xE6_xB5_x81_xE7_xA8_x8B_xE8_xBE_x93_xE5_x87_xBA_xE6_x88_x96_xE8_x80_x85f73babc98d494d79cf1981c0a0321c6d.html -->
<!-- path:常见问题 > 如何通过流程输出或者模块输出获取数据结果？ -->
# 数据结果：通过流程输出或者模块输出获取数据结果的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何通过二次开发获取流程输出或模块输出中的数据结果？

## 解决方法

获取数据结果可通过流程输出或模块输出两种方式。推荐使用流程输出，更符合高内聚低耦合的思想。

* **通过流程输出获取数据结果**
  1. 完成流程配置中的输出设置，如下图所示。
  2. 通过代码获取整型、浮点型、字符串型数据。

     ```
     VmProcedure vmprocess = (VmProcedure)VmSolution.Instance["流程1"];
     var moduResult = vmprocess.ModuResult;
     string str = moduResult.GetOutputInt("out").pIntVal[0].ToString();
     string str1 = moduResult.GetOutputFloat("out0").pFloatVal[0].ToString();
     string str2 = moduResult.GetOutputString("out1").astStringVal[0].strValue;

     //获取流程结果列表，str3与str2结果一致
     List<VmDynamicIODefine.IoNameInfo> ioNameInfos = VmProcess.ModuResult.GetAllOutputNameInfo();
     string str3 = VmProcess.ModuResult.GetOutputString(ioNameInfos[2].Name).astStringVal[0].strValue;
     ```
  3. 通过代码获取图像数据。输出的IMAGE类型图像数据，可通过前面的参数名称ImageD直接获取。

     ```
     ImageBaseData processImageData = VmProcess1.ModuResult.GetOutputImageV2("ImageD");
     int width = processImageData.Width;                         //宽
     int height = processImageData.Height;                       //高
     IntPtr imageByte = processImageData.ImageData;              //数据
     VMPixelFormat pixelformat = processImageData.Pixelformat;   //格式
     ```
* **通过模块输出获取数据结果**
  1. 通过如下代码获取模块的浮点型数据。

     ```
     IMVSCircleFindModuTool tool = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
     var moduResult = tool.ModuResult;
     string circleX = moduResult.OutputCircle.CenterPoint.X.ToString();
     string circleY = moduResult.OutputCircle.CenterPoint.Y.ToString();
     string circleR = moduResult.OutputCircle.Radius.ToString();
     ```
  2. 通过如下代码获取图像数据。

     ```
     SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance["流程1.输出图像1"];
     var saveImageResult=saveImage.ModuResult.OutputImage;
     byte[] imageData= saveImageResult.ImageData;
     int imagePixelformat= saveImageResult.Pixelformat;           // 17301505为MONO8灰度图，35127316为彩色图
     ```
