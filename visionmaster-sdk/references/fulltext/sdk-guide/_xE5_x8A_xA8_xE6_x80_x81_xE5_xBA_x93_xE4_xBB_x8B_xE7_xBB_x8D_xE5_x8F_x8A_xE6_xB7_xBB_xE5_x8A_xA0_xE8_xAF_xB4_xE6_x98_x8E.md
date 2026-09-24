<!-- src:_xE5_x8A_xA8_xE6_x80_x81_xE5_xBA_x93_xE4_xBB_x8B_xE7_xBB_x8D_xE5_x8F_x8A_xE6_xB7_xBB_xE5_x8A_xA0_xE8_xAF_xB4_xE6_x98_x8E.html -->
<!-- path:编程引导 > 配置流程 > 动态库介绍及添加说明 -->
# 动态库介绍及添加说明

本章节主要介绍配置流程中涉及的动态库及其添加说明。

## dll动态库功能

* VM.Core.dll：包含所有方案、流程的对外接口。
* VM.PlatformSDKCS.dll：提供对外接口的底层实现，是所有对外接口的基础库。
* VMControls.Interface.dll、VMControls.BaseInterface.dll：控件对外接口的基础库。
* VMControls.RenderInterface.dll：带渲染功能控件的基础库，如ROI、图形显示等。
* VMControls.Winform.Release.dll：Winform控件的基础库，包含Winform控件的对外接口。
* VMControls.WPF.Release.dll：包含WPF控件的对外接口。

## 开发方式说明

以下开发方式说明不包含具体模块，如使用到模块，在以下基础上导入使用到的对应模块dll即可。

* 纯调接口方式（无控件）需导入以下2个dll：

  + VM.Core.dll
  + VM.PlatformSDKCS.dll
* Winform控件需导入以下6个dll：

  + VM.Core.dll
  + VM.PlatformSDKCS.dll
  + VMControls.Interface.dll
  + VMControls.BaseInterface.dll
  + VMControls.RenderInterface.dll
  + VMControls.Winform.Release.dll
* WPF控件需导入以下6个dll：
  + VM.Core.dll
  + VM.PlatformSDKCS.dll
  + VMControls.Interface.dll
  + VMControls.BaseInterface.dll
  + VMControls.RenderInterface.dll
  + VMControls.WPF.Release.dll
