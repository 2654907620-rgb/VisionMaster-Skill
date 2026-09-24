<!-- src:_xE7_xA8_x8B_xE5_xBA_x8F_xE5_x90_xAF_xE5_x8A_xA8_xE5_x90_x8E_xE6_x8A_xA5_xE9_x94_x99_xE7_x9A_x8439b445d04d97f919174b2dbcabb4a034.html -->
<!-- path:常见问题 > 如何排查程序启动后报错的原因？ -->
# 环境配置：程序启动后报错的排查方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**VM4.3 SDK程序启动后，出现 Vm.Core.Solution 或 VM.PlatformSDKCS 等相关内容，如下图所示。

## 解决方法

1. 确保VM软件能正常运行，且能打开和运行方案。
2. 确认环境已完成配置。主要为：是否插好加密狗，是否以管理员身份运行VS再打开项目，框架是否选择.NET Framework4.6.1且取消勾选【首选32位】，二次开发程序启动前是否已关闭VM软件。
3. （可选步骤）若VM版本为4.0或4.1，SDK开发时重新拷贝Development\V4.0.0\ComControls\bin\x64下所有的文件到二次开发exe所在目录下。
4. 若PC存在多个版本的VM，请确认方案和程序升级后，是否适配当前的VM版本。
5. 如以上操作仍无法解决，可使用try{ }catch(VmException ex){ }捕获异常码，并在手册中查找异常码对应的内容。
