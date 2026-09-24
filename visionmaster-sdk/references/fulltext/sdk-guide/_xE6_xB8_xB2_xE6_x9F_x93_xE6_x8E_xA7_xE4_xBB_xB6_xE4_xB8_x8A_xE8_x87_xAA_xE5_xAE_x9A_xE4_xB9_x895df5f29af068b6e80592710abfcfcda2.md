<!-- src:_xE6_xB8_xB2_xE6_x9F_x93_xE6_x8E_xA7_xE4_xBB_xB6_xE4_xB8_x8A_xE8_x87_xAA_xE5_xAE_x9A_xE4_xB9_x895df5f29af068b6e80592710abfcfcda2.html -->
<!-- path:常见问题 > 如何在渲染控件上自定义图形？ -->
# 输出图像：渲染控件上自定义图形的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何在渲染控件上自定义图形？

## 解决方法

1. 手动添加引用VMControls.WPF.dll、WindowsBase.dll。添加后，引用属性【复制本地】改为false。
2. 渲染控件绑定图像再绘制图形。
3. 流程运行结束后，在回调函数中调用渲染控件的AddShape绘图接口，支持绘制直线、圆形、矩形、文本等图形元素。以绘制直线和文本为例，相关代码如下：

   ```
   //绘制直线
   VMControls.WPF.LineEx line = new VMControls.WPF.LineEx(new System.Windows.Point(100, 100), new System.Windows.Point(600, 600), stroke: "#FF0000", strokeThickness: 10);
   vmRenderControl1.AddShape(line);

   //绘制文本
   VMControls.WPF.TextEx text = new VMControls.WPF.TextEx("欢迎使用VM4.2二次开发！", new System.Windows.Point(1000, 1000), fontSize: 20, stroke: "#FF0000");
   vmRenderControl1.AddShape(text);
   ```
