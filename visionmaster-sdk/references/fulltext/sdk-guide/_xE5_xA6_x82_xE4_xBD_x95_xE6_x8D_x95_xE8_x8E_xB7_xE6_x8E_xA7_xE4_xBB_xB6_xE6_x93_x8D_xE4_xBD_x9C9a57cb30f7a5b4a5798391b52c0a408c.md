<!-- src:_xE5_xA6_x82_xE4_xBD_x95_xE6_x8D_x95_xE8_x8E_xB7_xE6_x8E_xA7_xE4_xBB_xB6_xE6_x93_x8D_xE4_xBD_x9C9a57cb30f7a5b4a5798391b52c0a408c.html -->
<!-- path:常见问题 > 如何捕获控件操作过程中抛出的异常？ -->
# 如何捕获控件操作过程中抛出的异常

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**二次开发程序操作控件的过程中，一般异常会在内部进行捕获，并以弹窗、日志等方式进行提示，部分特殊异常会抛出到外部，例如加密狗断开等。若未妥善捕获该类异常，可能会导致程序闪退。

## 解决方法

建议在程序中增加全局捕获异常逻辑，可参考如下代码。

* **对于Winform程序：**

  ```
  // 指示应用程序如何响应未经处理的异常
  Application.SetUnhandledExceptionMode(UnhandledExceptionMode.CatchException);
  // 处理UI线程异常
  Application.ThreadException += Application_ThreadException;
  // 处理非UI线程异常
  AppDomain.CurrentDomain.UnhandledException += CurrentDomain_UnhandledException;

  Application.EnableVisualStyles();
  Application.SetCompatibleTextRenderingDefault(false);
  Application.Run(new Form1());
  ```
* **对于WPF程序：**

  ```
  // 处理UI线程异常
  this.DispatcherUnhandledException += App_DispatcherUnhandledException;
  // 处理非UI线程异常
  AppDomain.CurrentDomain.UnhandledException += CurrentDomain_UnhandledException;
  ```
