<!-- src:GUID-5CC017AA-BB74-4EBC-AF38-165CE79CE7DB.html -->
<!-- path:产品概述 > 运行环境 -->
# 运行环境

# 运行环境

为确保软件能正常安装及运行，对安装软件的工控机配置有所要求。

## 推荐配置

* 操作系统：Windows7/10/11（64位操作系统）

  说明

  如需使用深度学习模块，建议使用Windows 10或Windows 11 64位操作系统。
* CPU：Intel Core i7-6700 3.4GHz 及以上

  说明

  如需使用CPU相关深度学习模块，建议配备i7-8代及以上。
* 内存：8 GB及以上
* 显卡：显存1 GB及以上

  说明

  如需使用GPU相关深度学习模块，需确保显存6 GB及以上，具体参见推荐硬件。
* .NET FrameWork：4.6.1及以上
* 网卡：Intel i210系列及以上千兆网卡
* USB接口：USB3.0

## 最低配置

* 操作系统：Windows7/10/11（64位操作系统）
* CPU：Intel 3845
* 内存：4 GB
* 显卡：显存1 GB

  说明

  如需使用GPU相关深度学习模块，需确保显存6 GB及以上，具体参见推荐硬件。
* .NET FrameWork：4.6.1
* 网卡：千兆网卡
* USB接口：USB3.0

## 推荐硬件

软件中的深度学习功能，需搭配如下设备或显卡使用。

* AI推理终端：海康机器人自主研发的AI推理终端设备，其内部搭载VM专用AI推理加速卡，支持运行部分深度学习和缺陷检测模块，包括DL字符定位、DL字符识别、DL分类、DL读码、DL目标检测、DL实例分割、DL图像检索、DL图像分割、DL快速图像分割、DL无监督分割和异常检测。

  说明

  使用AI推理终端运行上述模块前，请确保您的工控机内存不低于16 GB，并安装Windows 10或Windows 11
  64位操作系统。此外，操作系统内部版本号需不低于10.0.19041。
* NVIDIA独立显卡：支持运行所有深度学习类和边缘学习类模块。可考虑使用以下显卡型号。

  + NVIDIA® GeForce® RTX™
    50系列：RTX5060、RTX5060Ti、RTX5070、RTX5070Ti、RTX5080、RTX5090 D v2。
  + NVIDIA® GeForce® RTX™
    40系列：RTX4060、RTX4060Ti、RTX4070、RTX4070Ti、RTX4080、RTX4090。
  + NVIDIA® GeForce® RTX™
    30系列：RTX3050、RTX3060、RTX3060Ti、RTX3070、RTX3080、RTX3090。
  + NVIDIA® GeForce® RTX™
    20系列：RTX2060、RTX2060S、RTX2070、RTX2070S、RTX2080、RTX2080S、RTX2080Ti。
  + NVIDIA® GeForce® GTX
    10系列：GTX1060、GTX1660、GTX1660S、GTX1070、GTX1070Ti、GTX1080、GTX1080Ti。
  + NVIDIA® Tesla®系列：Tesla L2。

  说明
  + NVIDIA® GeForce®
    RTX™
    50系列显卡的驱动版本应不低于572.61，以上其他系列显卡的驱动版本应不低于528.33。
  + 安装深度学习安装包时，支持选择AI推理终端和NVIDIA显卡。软件运行时，将根据设置的显卡或设备运行深度学习相关模块。更多配置详情，请参见深度学习安装包中的安装指南。
