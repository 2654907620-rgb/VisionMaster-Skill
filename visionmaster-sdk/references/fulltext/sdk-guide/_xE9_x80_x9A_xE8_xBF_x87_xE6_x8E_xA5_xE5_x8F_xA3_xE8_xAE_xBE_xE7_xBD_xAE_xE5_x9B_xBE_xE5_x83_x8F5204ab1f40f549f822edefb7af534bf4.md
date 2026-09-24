<!-- src:_xE9_x80_x9A_xE8_xBF_x87_xE6_x8E_xA5_xE5_x8F_xA3_xE8_xAE_xBE_xE7_xBD_xAE_xE5_x9B_xBE_xE5_x83_x8F5204ab1f40f549f822edefb7af534bf4.html -->
<!-- path:常见问题 > 如何通过图像源模块接口设置输入图像？ -->
# 图像源：通过接口设置图像输入的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何通过图像源模块接口设置输入图像？

## 知识点

图像源模块的图像分为8位灰度图和24位彩色图，可输出两层图像，分别为【图像源.图像】和【图像源.灰度图像】。其他模块基本只能处理8位图。

* 图像源类型为SDK且接口传入的图像为灰度图时：
  + 若未开启输出Mono8使能，图像源的【图像源.图像】有图像数据且为灰度图，【图像源.灰度图像】无图像数据；
  + 若开启输出Mono8使能，则图像源的【图像源.图像】和【图像源.灰度图像】都有图像数据，且均为灰度图。
* 图像源类型为SDK且接口传入的图像为彩色图时：
  + 若未开启输出Mono8使能，图像源的【图像源.图像】有图像数据且为彩色图，【图像源.灰度图像】无图像数据；
  + 若开启输出Mono8使能，则图像源的【图像源.图像】和【图像源.灰度图像】都有图像数据，前者是彩色图，后者是灰度图。

图像源后续连接模块的图像输入源默认为【图像源.图像】。若【图像源.图像】为灰度图，则无需调整，可直接使用；若【图像源.图像】为彩色图，则需将输入源设为【图像源.灰度图像】，否则后续模块将运行失败。

## 解决方法

图像源选择不同的类型，操作方法有所差别。

* 图像源选择SDK时，使用**SetImagePath接口**或**SetImageData接口**。其中SetImageData接口的参数图像类型为ImageBaseData，像素格式Pixelformat使用枚举类VMPixelFormat。

  ```
  imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.SDK;
  imageSourcTool.SetImagePath("E:\\VSVM4.0\\1.bmp");
  imageSourcTool.SetImageData(imageBaseData);             //参数类型为ImageBaseData
  ```
* 图像源选择本地（LocalImage）时，此功能可实现添加单个图像。若需要添加图像文件夹，则使用**SetParamValue接口**遍历文件夹中所有图像。

  ```
  ImageSourceModuleTool imageSourcTool = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
  imageSourcTool.ModuParams.ImageSourceType = ImageSourceParam.ImageSourceTypeEnum.LocalImage;

  //添加图片，添加同路径下的图片无效，添加效果查看：保存方案或切换流程Tab页
  imageSourceTool.AddInputImageByPath("D:\\3.ProjectCode\\VM4.3\\1.bmp");

  //删除图片
  imageSourceTool.DeleteInputImageByPath("D:\\1.bmp");

  //清空图片
  imageSourceTool.ClearAllInputImage();

  //加载文件夹中所有图片
  DirectoryInfo dir = new DirectoryInfo("E:\\VSVM4.2\\图像\\新建文件夹");
  FileInfo[] dirinfo = dir.GetFiles();
  for (int i = 0; i < dirinfo.Length; i++)
  {
   string str = dirinfo[i].FullName;
       imageSourceTool.AddInputImageByPath(str);
  }
  ```
