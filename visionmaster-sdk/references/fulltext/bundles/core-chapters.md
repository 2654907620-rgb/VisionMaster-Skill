# VisionMaster .NET SDK 开发指南 — 核心章节全文




<!-- ===== index.html | 首页 ===== -->

<!-- src:index.html -->
<!-- path:首页 -->
# 首页

## 概述

VM算法平台SDK基于方案、流程和模块工具等进行对象级封装，可通过方案、流程和模块工具中各个对象的功能接口进行相应的数据交互与运行控制。同时提供相应的流程配置控件、参数配置控件、渲染控件、全局工具控件以及前端运行界面控件等，方便进行方案编辑、参数配置以及渲染展示，便于灵活进行开发，并扩展机器视觉应用。

|  |
| --- |
|  |
| SDK各对象功能接口调用控制 |



|  |
| --- |
|  |
| SDK控件级组合调用 |

SDK提供C++和C# 两套接口，同时分别提供两套接口的Demo，可参考Demo查看主要接口的使用方法。本文档主要介绍如何通过C# 接口调用VisionMaster算法平台SDK的外部接口。

## 注意事项

* 使用SDK前，需安装工业相机、加密狗等硬件设备的驱动。
* 杀毒软件可能将SDK识别为病毒，为方便使用，建议将VisionMaster算法平台加入杀毒软件的白名单中或关闭电脑上的杀毒软件。对于360安全卫士，建议关闭。
* 接口调用时，若接口参数涉及路径信息，必须使用绝对路径。




<!-- ===== _xE5_x8F_x91_xE7_x89_x88_xE8_xAF_xB4_xE6_x98_x8E.html | 发版说明 ===== -->

<!-- src:_xE5_x8F_x91_xE7_x89_x88_xE8_xAF_xB4_xE6_x98_x8E.html -->
<!-- path:发版说明 -->
# 发版说明

## V4.4.0维护版本（2025/11)

**【功能新增】**

* 边缘学习 类别下新增学习计数CPU 、学习计数GPU 、有无检测CPU 、有无检测GPU 、异常分类CPU 、异常分类GPU 、多类别分类CPU 和多类别分类GPU 模块，该类模块通过学习少量注册模板数据，可快速适配不同的场景下的检测需求，实现检测效率与准确率的显著提升。
* 图像处理 类别下新增掩膜工具 ，可对输入图像上的指定区域进行形态学处理和掩膜运算。该模块可适应对不规则区域的检测需求，并通过掩膜预处理，为后续的识别、定位、测量和检测等任务提供更准确的图像数据。
* 注册分类CPU 和注册分类GPU 新增结果判断动态参数项类ResultFilterItemParam，支持设置结果判断动态参数项。
* 光源 新增光源5-8的设置参数，支持调整光源5-8的状态、边缘触发类型、持续时间以及亮度参数等。
* 轮廓匹配 、快速匹配 、高精度匹配 和灰度匹配VA 新增GetModelNum()和ExportModelData()接口，可用于获取模型数量以及导出模型。
* 注册检测CPU 和注册检测GPU 的结果类CnnRegisterDetectResult新增如下模块结果属性。

  | 接口 | 描述 |
  | --- | --- |
  | LabelTypeTotalCount | 结果类别总数 |
  | LabelTypeName | 结果类别名称 |
  | LabelTypeCount | 结果类别个数 |
* 图像源 模块的结果类ImageSourceResult新增取图数量属性ImageNum。
* 方案 和流程 新增ClearHistoryResultData()，可清空流程内所有历史结果数据。此外，方案 还新增了SetLogConfig()和CloseLogConfig()接口，可实时调整日志或关闭日志配置。
* 参数配置带渲染控件 和 综合配置控件 下新增SetParamConfigUIWidth()，可用于设置参数配置窗口的宽度。

**【功能更新】**

* 高精度注册检测CPU和高精度注册检测GPU模块改名为全监督检测CPU 和全监督检测GPU ，并更新运行参数和结果参数。
* 更新注册分割CPU 、注册分割GPU 、注册检测CPU 和注册检测GPU 模块的运行参数和结果参数，支持设置批处理等级参数。
* 更新注册分割CPU 、注册分割GPU 、注册检测CPU 和注册检测GPU 模块的最大查找个数范围，由[1,1000]扩充至[1,100000]。
* 更新注册分割CPU 、注册分割GPU 、注册检测CPU 和注册检测GPU 模块的的面积范围上限及下限参数范围，由[1,16000000]扩充至[1,1600000000] 。
* 更新多直线查找 的边缘点数限制最大值参数范围，由[100,9999999]扩充至[1,9999999]。

**【功能废弃】**

* 废弃DL字符定位CPU 和DL字符定位GPU 结果类CnnCharDetectResult中的目标置信度参数ObjConf，推荐使用ObjectScore替代。
* 废弃脚本 中的结果显示属性ResultShow。
* 废弃注册分类CPU 和注册分类GPU 结果类CnnRegisterClassifyResult中所有获取缩略图相关接口。

## V4.4.0维护版本（2025/4)

**【功能新增】**

* 新增综合配置控件 功能，支持通过 VmComprehensiveConfigWithRenderControl 类中的接口显示、修改和配置“综合配置控件”。
* 全局模块控件 新增如下接口，分别用于打开各全局模块窗口。

  | 接口 | 描述 |
  | --- | --- |
  | OpenGlobalVariable | 打开全局变量窗口 |
  | OpenGlobalScript | 打开全局脚本窗口 |
  | OpenGlobalCamera | 打开全局相机窗口 |
  | OpenGlobalTrigger | 打开全局触发窗口 |
  | OpenCommunicationManager | 打开通信管理窗口 |
* 参数配置控件 新增如下接口，支持显示或隐藏特定配置项Tab页。

  | 接口 | 描述 |
  | --- | --- |
  | GetParamTabNames | 获取所有Tab页名称 |
  | SetParamTabVisible | 设置Tab页是否可见 |
* 参数配置带渲染控件 新增如下接口，支持显示/隐藏工具栏以及设置当前渲染的图像。

  | 接口 | 描述 |
  | --- | --- |
  | GetParamTabNames | 获取所有Tab页名称 |
  | SetParamTabVisible | 设置Tab页是否可见 |
  | SetRenderToolbarVisible | 设置工具栏是否可见 |
  | GetDisplayableImageNameList | 获取可显示的图像名称列表 |
  | SetSelectedImage | 选择一张图像作为显示图像 |
  | SwitchBackgroundImage | 当图像堆叠时，切换背景图像 |
  | AddStackImage | 添加一张图像进行堆叠显示，最新添加的图像堆叠在最上层 |
  | RemoveStackImage | 移除堆叠显示图像中的任意一张 |
* 渲染控件 新增如下接口，支持显示/隐藏工具栏以及设置当前渲染的图像。

  | 接口 | 描述 |
  | --- | --- |
  | SetRenderToolbarVisible | 设置工具栏是否可见 |
  | GetDisplayableImageNameList | 获取可显示的图像名称列表 |
  | SetSelectedImage | 选择一张图像作为显示图像 |
  | SwitchBackgroundImage | 当图像堆叠时，切换背景图像 |
  | AddStackImage | 添加一张图像进行堆叠显示，最新添加的图像堆叠在最上层 |
  | RemoveStackImage | 移除堆叠显示图像中的任意一张 |

**【已知问题】**

当前版本的已知问题如下。

* 通过本SDK设置模块ROI时，若先后设置多种ROI，多种ROI的生效顺序基于不同ROI的生效优先级，而非实际的设置顺序。具体优先级如下：矩形ROI>圆形ROI>多边形ROI。
* 在MFC中，若使用Tab控件管理VM控件，需要设置Tab控件的GWL\_EXSTYLE（该参数用于设置窗口扩展样式），将WS\_EX\_CONTROLPARENT添加到现有的扩展样式中；否则切换Tab页时有可能会卡死。
* 在MFC中，VM控件放在Tab中时，需要设置Tab控件的GWL\_EXSTYLE（该参数用于设置窗口扩展样式），将WS\_EX\_CONTROLPARENT添加到现有的扩展样式中；否则可能导致键盘无法输入字母和数字。
* 二次开发控件尺寸过小时，参数配置控件和参数配置带渲染控件中的滑动条尺寸可能超过控件尺寸（如下图所示），请谨慎评估和使用。
* 主界面和运行界面的参数设置类控件以及字体、颜色等基础控件，右键会出现系统默认上下文菜单，且文本跟随windows系统（例如“剪切”、“复制”、"粘贴”）。

## V4.4.0维护版本（2024/8)

**【功能新增】**

* 轮廓匹配 的参数类新增SkewXStart和SkewXEnd。
* 注册学习 类别新增高精度注册检测CPU 、高精度注册检测GPU 模块。
* 间距检测 的结果新增圆弧0 Annulus0和圆弧1 Annulus1。
* DL字符定位GPU 和DL字符定位CPU 新增文本比对参数TextComparisonEnable。
* SDK状态码 中新增1个通信相关错误码。

**【功能优化】**

* 灰度匹配VA 的参数匹配结束层EndPyramidLevel的范围由[0,10]调整为[0,8]。

**【功能废弃】**

* Blob分析 模块废弃轮廓输出使能参数BolbOutLineEnable，调整为输出轮廓类型参数BlobContourType和BlobContourTypeEnum。
* 轮廓匹配 废弃多模板排序方式参数NMSSortType，多模板重叠率参数由NMSMaxOverlap调整为MultiModelMaxOverlap。
* ML分类 废弃部分参数，已标注为“弃用”。
* 流程 废弃导入流程接口 ImportProcess() ，使用 Load() 替代；废弃导出流程接口 ExportProcess() ，使用 SaveAs() 替代。

**【文档调整】**

* 优化整个文档的架构。

## V4.4.0（2024/1）

**【功能新增】**

* 注册学习 类别新增注册检测CPU 、注册检测GPU 、注册分割CPU 、注册分割GPU 模块。
* 深度学习 类别新增DL无监督分类GPU 模块。
* 标定 类别新增坐标系 模块。
* 颜色处理 类别新增彩图生成 、颜色分割 模块。
* 逻辑工具 类别新增数据分类 、数据筛选 、数据排序 、数据记录 、Python脚本 模块。
* DL快速图像分割GPU 、DL图像分割CPU 、DL图像分割GPU 、DL分类CPU 、DL分类GPU 模块新增多ROI相关接口。
* 流程和Group增加局部变量功能。
* 流程和Group运行接口可选的响应界面操作，优化运行接口耗时波动。
* 流程和Group获取输出的所有接口增加对IO类型的判断，仅可以获取到流程和Group的输出值，不再支持获取输入的值。
* 全局变量 和脚本 模块等支持组合类型和数组类型数据。
* 结果类支持浅拷贝模式，优化图像/点集等二进制类型数据获取耗时。
* 图像/图形类型支持与算子类型互转。
* 彩色图像支持P3格式。
* 运行环境 兼容Windows 11（64位）操作系统。
* 新增环境检测工具 ，用于二次开发环境检测。
* 新增部分错误码。

**【功能更新】**

* 更新软件许可 章节，此版本使用精锐5.0系列加密狗。

**【文档调整】**

* 注册分类CPU 和 注册分类GPU 模块从 深度学习 移至 注册学习 类别。
* 灰度匹配 、像素统计 、字符缺陷检测 、DL异常检测CPU 、DL异常检测GPU 模块已移至 弃用 类别。
* 常见问题章节新增如何捕获控件操作过程中抛出的异常 、如何理解设置输入接口的“仅当次执行起效”逻辑 。

## V4.3.0维护版本（2023/5）

**【功能新增】**

* 增加ML分类 、注册分类CPU 、注册分类GPU 、DL快速图像分割GPU 、阵列圆查找 、像素统计VA等模块类封装。
* 方案模块增加相机连接状态、相机开始取图事件、相机新增和删除事件。
* 渲染控件 增加有损存图、刷新条件设置、刷新频率设置等接口。
* 控件统一增加dispose()接口，并更新控件相关调用 示例代码。
* 控件支持通过修改配置文件切换中英文显示，具体请见控件中英文切换 章节。
* 新增加密狗的网络锁功能，具体请见软件许可 章节。
* 新增清除当前版本环境按钮，具体请见版本切换和升级 章节。
* 新增相机连接状态和相机开始取图事件，具体请见事件章节。
* 新增部分错误码。

## V4.3.0（2023/1）

**【功能新增】**

* 新增椭圆拟合、逆仿射变换、轮廓匹配、椭圆查找模块。
* 新增版本切换和升级、异常信息收集工具、常见问题章节。
* 新增部分错误码。
* 新增资源释放接口，仅在退出程序前调用一次，请避免在析构函数中调用。
* 流程和Group控件的综合配置增加权限配置接口。

**【功能优化】**

* 图像类ImageBaseData\_V2功能合并至图像类ImageBaseData，后续版本逐步弃用ImageBaseData\_V2。
* 图像类ImageBaseData类内实现对图像类ImageBaseData\_V2的隐式和显示转换。
* 部分二次开发程序，升级至V4.3时需修改代码，使用ImageBaseData属性ImageDataPtr替换ImageBaseData\_V2属性ImageData。

**【文档调整】**

* 调整文档架构，涉及软件许可 、运行环境 、编程引导、示例程序介绍等章节内容。

## V4.2.0维护版本（2022/7）

**【功能新增】**

* 新增旋转标定、平移旋转标定、单点抓取、单点纠偏、单点映射对位、表面缺陷滤波模块。
* 重制灰度匹配模块。
* 图像源模块新增拼接功能相关接口，新增添加、删除、清空本地图片的接口。
* 标定相关模块增加界面按钮对应接口。
* 标定转换新增输出接口，例如生成标定接口、变量计算的重置接口。
* 分支字符模块增加设置调试模式的接口。
* 全局相机GlobalCamera新增获取相机信息列表，选择相机新增设置和获取接口。
* 方案Solution新增获取流程对象接口GetAllProcedureObjects，返回对象列表。
* 流程Procedure新增获取模块信息列表的接口，返回列表信息不将Group内模块包含进去。
* 渲染控件RenderControl和带参数的渲染控件ParamsRenderControl增加清空显示接口。
* 新增全局相机控件。

## V4.2.0（2022/4）

**【功能新增】**

* 接口函数新增拆分组合功能模块，包含划片拆分、二维阵列、多标签筛选、BoX融合、Box重叠率、Box过滤。
* 接口函数中的定位模块新增目标跟踪；深度学习模块新增DL无监督分割；运算模块新增坐标转换；图像处理模块新增图像缩放；缺陷检测模块新增边缘位置趋势分析、边缘对位置趋势分析；逻辑工具模块新增条件分支、触发模块、图形收集；全局模块新增全局相机；控件模块新增独立Group控件。

**【文档调整】**

* 修改编程引导中的相关接口流程图。
* 修改示例程序中的示例代码。
* 修改部分状态码说明。

## V4.1.0（2021/9）

**【功能新增】**

* 接口函数中的定位模块新增角平分线查找、中线查找、平行线计算、垂线查找模块接口；深度学习模块新增DL实例分割模块接口；标定模块新增标定加载模块接口；运算模块新增旋转计算模块接口；控件模块新增主界面控件模块接口。

**【文档调整】**

* 修改编程引导中的相关接口流程图。
* 调整接口函数分类，划分出图像生成模块，对位模块修改为运算模块。
* 部分接口函数新增范围说明。
* 修改示例程序中的示例代码。
* 修改部分状态码说明，删除图像融合类状态码。资源类、公共用新增部分状态码。

## V4.0.0（2021/8）

**【功能新增】**

* 提供方案、流程、Group、全局模块以及所有算法逻辑模块的功能接口。
* 提供流程配置控件、参数配置控件、带渲染功能参数配置控件、弹出式参数配置控件、渲染控件、全局工具控件以及前端运行界面控件。
* 提供示例Demo。




<!-- ===== _xE8_xBD_xAF_xE4_xBB_xB6_xE8_xAE_xB8_xE5_x8F_xAF.html | 软件许可 ===== -->

<!-- src:_xE8_xBD_xAF_xE4_xBB_xB6_xE8_xAE_xB8_xE5_x8F_xAF.html -->
<!-- path:软件许可 -->
# 软件许可

VM算法平台为收费软件，无法直接打开。需使用硬件加密狗或授权码进行激活方可使用。
VM算法平台使用需要授权，授权方式有如下3种，可在软件安装时选择使用哪种**授权方式**。

* 本机加密狗：通过精锐5.0加密狗即插即用，可更换工控机使用。仅针对接插加密狗的本机工控机有效。
* 软加密：通过授权码实现。首次使用软件前，需先完进行激活。

  注意
  :   + 若通过软加密授权后需更换使用的工控机或重装系统，则需先完成软加密的迁出，并在另一台工控机或重装系统后重新迁入。具体如何操作请联系技术支持。
      + 若工控机主板等核心硬件损坏，更换核心硬件后，本工控机的软加密将失效，需重新购买授权码。
* 远程加密狗：同样通过加密狗即插即用，但当加密狗插在局域网内服务端工控机上时，完成相关设置后，局域网内其他工控机无需再接加密狗，可直接打开算法平台。

注解
:   * 若未搭配硬件加密狗或软加密授权码，Demo可以打开，但不能实际使用。
    * 不同的授权方式具体如何激活使用，请参考《VisionMaster算法开发平台用户手册》。

## 本机加密狗

**授权方式**选择**本机加密狗**时，需提前通过工控机的USB口插入精锐5.0加密狗。

若打开软件时提示“加密狗异常”，可参考如下方法解决：

* 未插加密狗导致，插上加密狗即可；
* 加密狗驱动异常，可重装驱动解决。可进入 ..\VisionMaster+版本号\Drivers\SenseShield 路径查看驱动，双击运行install.bat脚本文件即可。

不同系列加密狗支持的功能类别有所差别，具体请见下表。

| 型号 | 定位  测量  标定  运算 | 识别 | 缺陷检测 | 边缘学习 | 深度学习 | 图像处理 | 颜色处理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| iMVS-VM-1200 | \* | √ | × | × | × | \* | \* |
| iMVS-VM-2200 | √ | × | √ | × | × | √ | \* |
| iMVS-VM-4200 | √ | × | × | × | × | \* | \* |
| iMVS-VM-6200  iMVS-VM-6210 | √ | √ | √ | × | × | √ | √ |
| iMVS-VM-6217 | √ | √ | √ | √ | × | √ | √ |
| iMVS-VM-7200 | √ | √ | √ | \* | √ | √ | √ |
| iMVS-VM-7210 | √ | √ | √ | √ | √ | √ | √ |

注解
:   * 对于上表中未提及的功能，所有型号加密狗均支持，主要为采集、拆分组合、图形生成、逻辑工具和通信等。
    * 上表中\*代表该分类部分模块可用，部分模块不可用，具体请以实际情况为准。

同时，不同型号加密狗支持的相机路数有所差别。iMVS-VM-6210和iMVS-VM-7210型号加密狗不限制相机路数，其余型号加密狗遵循以下原则：

* 不带后缀：支持4路相机
* 带SE后缀：支持2路相机
* 带PRO后缀：不限制相机路数

## 软加密

**授权方式**选择**软加密**时，需提前在本机上使用授权码进行激活。

不同型号软加密型号支持的功能类别有所差别，具体请见下表。

| 型号 | 定位  测量  标定  运算 | 识别 | 缺陷检测 | 边缘学习 | 深度学习 | 图像处理 | 颜色处理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| iMVS-VMS-1200 | \* | √ | × | × | × | \* | \* |
| iMVS-VMS-2200 | √ | × | √ | × | × | √ | \* |
| iMVS-VMS-4200 | √ | × | × | × | × | \* | \* |
| iMVS-VMS-6200  iMVS-VMS-6210 | √ | √ | √ | × | × | √ | √ |
| iMVS-VM-6217 | √ | √ | √ | √ | × | √ | √ |
| iMVS-VMS-7200 | √ | √ | √ | \* | √ | √ | √ |
| iMVS-VMS-7210 | √ | √ | √ | √ | √ | √ | √ |

注解
:   * 对于上表中未提及的功能，所有型号加密狗均支持，主要为采集、拆分组合、图形生成、逻辑工具和通信等。
    * 上表中\*代表该分类部分模块可用，部分模块不可用，具体请以实际情况为准。

软加密支持在线和离线两种方式激活，且型号后缀不同，支持的相机路数有所差别。iMVS-VMS-6210和iMVS-VMS-7210型号加密狗不限制相机路数，其余型号加密狗遵循以下原则：

* 不带后缀：支持4路相机
* 带SE后缀：支持2路相机
* 带PRO后缀：不限制相机路数

## 远程加密狗

**授权方式**选择**远程加密狗**时，需提前在局域网的服务器上插入远程加密狗并通过加密工具完成相关配置，局域网内安装软件的工控机方可使用。

不同型号软加密型号支持的功能类别有所差别，具体请见下表。

| 型号 | 定位  测量  标定  运算 | 识别 | 缺陷检测 | 边缘学习 | 深度学习 | 图像处理 | 颜色处理 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| iMVS-VMNET-6200  iMVS-VMNET-6210 | √ | √ | √ | × | × | √ | √ |
| iMVS-VM-6217 | √ | √ | √ | √ | × | √ | √ |
| iMVS-VMNET-7200 | √ | √ | √ | \* | √ | √ | √ |
| iMVS-VMNET-7210 | √ | √ | √ | √ | √ | √ | √ |

注解
:   * 对于上表中未提及的功能，所有型号加密狗均支持，主要为采集、拆分组合、图形生成、逻辑工具和通信等。
    * 上表中\*代表该分类部分模块可用，部分模块不可用，具体请以实际情况为准。

同时，不同型号加密狗支持的相机路数有所差别：

* iMVS-VMNET-6200和iMVS-VMNET-7200：支持4路相机
* iMVS-VMNET-6210和iMVS-VMNET-7210：不限制相机路数




<!-- ===== _xE8_xBF_x90_xE8_xA1_x8C_xE7_x8E_xAF_xE5_xA2_x83.html | 运行环境 ===== -->

<!-- src:_xE8_xBF_x90_xE8_xA1_x8C_xE7_x8E_xAF_xE5_xA2_x83.html -->
<!-- path:运行环境 -->
# 运行环境

使用算法平台SDK时，对PC运行环境有所要求。

注解
:   * 使用SDK前，需安装工业相机等硬件设备驱动。
    * 杀毒软件可能将SDK识别为病毒，为方便使用，建议将本软件加入该杀毒软件的白名单中或关闭电脑上的杀毒软件，对于360安全卫士建议关闭。

## 推荐配置

|  |  |
| --- | --- |
| 操作系统： | Windows 7/10/11（64位） |
| VS运行环境： | VS2015及以上版本 |
| .NET运行环境： | .NET Framework4.6.1及以上 |
| CPU： | Intel Core i7-6700 3.4GHz及以上（如需使用CPU相关深度学习功能，建议配置i7-8代及以上） |
| 内存： | 8 GB及以上 |
| 显卡： | 1 GB及以上（如需使用GPU相关深度学习模块，需确保显存6 GB及以上） |
| 网卡： | Intel i210系列以上千兆网卡 |
| USB接口： | USB3.0 |

## 最低配置

|  |  |
| --- | --- |
| 操作系统： | Windows 7/10/11（64位） |
| VS运行环境： | VS2015及以上版本 |
| .NET运行环境： | .NET Framework4.6.1及以上 |
| CPU： | Intel 3845及以上 |
| 内存： | 4 GB |
| 显卡： | 1 GB及以上（如需使用GPU相关深度学习模块，需确保显存6 GB及以上） |
| 网卡： | 千兆网卡 |
| USB接口： | USB3.0 |

## 推荐硬件

深度学习功能，需搭配如下设备或显卡使用。

* **AI推理终端**：海康机器人自主研发的AI推理终端设备，其内部搭载软件专用AI推理加速卡，支持运行部分深度学习算子和缺陷检测算子，如DL字符定位、DL字符识别、DL图像分类、DL读码、DL目标检测、DL异常检测、DL实例分割、DL图像检索、DL图像分割V2、DL快速图像分割和DL无监督分割。

  注解
  :   使用AI推理终端运行上述模块前，请确保您的工控机内存不低于16 GB，并安装Windows 10或Windows 11 64位操作系统。此外，操作系统内部版本号需不低于10.0.19041。
* **NVIDIA独立显卡**：支持全部深度学习类和边缘学习类算子，可考虑使用如下显卡型号。

  + NVIDIA GeForce RTX 50系列：RTX5060、RTX5060Ti、RTX5070、RTX5070Ti、RTX5080、RTX5090 D v2。
  + NVIDIA GeForce RTX 40系列：RTX4060、RTX4060Ti、RTX4070、RTX4070Ti、RTX4080、RTX4090。
  + NVIDIA GeForce RTX 30系列：RTX3050、RTX3060、RTX3060Ti、RTX3070、RTX3080、RTX3090。
  + NVIDIA GeForce RTX 20系列：RTX2060、RTX2060S、RTX2070、RTX2070S、RTX2080、RTX2080S、RTX2080Ti。
  + NVIDIA GeForce GTX 10系列：GTX1060、GTX1660、GTX1660S、GTX1070、GTX1070Ti、GTX1080、GTX1080Ti。
  + NVIDIA Tesla系列：Tesla L2。

    注意
    :   - NVIDIA GeForce RTX 50系列显卡的驱动版本应不低于572.61，以上其他系列显卡的驱动版本应不低于528.33。
        - 安装深度学习安装包时，支持选择**AI推理终端**和**NVIDIA显卡**。软件运行时，将根据设置的显卡或设备运行深度学习相关模块。更多配置详情，请参见深度学习安装包中的安装指南。




<!-- ===== _xE7_x89_x88_xE6_x9C_xAC_xE6_xBF_x80_xE6_xB4_xBB_xE5_x92_x8C_xE5_x8D_x87_xE7_xBA_xA7.html | 版本激活和升级 ===== -->

<!-- src:_xE7_x89_x88_xE6_x9C_xAC_xE6_xBF_x80_xE6_xB4_xBB_xE5_x92_x8C_xE5_x8D_x87_xE7_xBA_xA7.html -->
<!-- path:版本激活和升级 -->
# 版本激活和升级

本章节主要介绍如何使用激活工具自动激活当前工具所在目录对应的VisionMaster版本。

## 激活工具

当PC上同时安装该软件的多个版本时，建议使用激活工具切换对应的VisionMaster版本。该工具（即ActivationTool.exe工具）可从VisionMaster的安装路径下获取，其相对路径为：.\Applications\Tools\ActivationTool。

**前提条件：**

需确保已关闭 VisionMaster 和 Visual Studio 软件的所有相关进程。

**操作方法：**

1. 在VisionMaster的安装路径下找到ActivationTool.exe程序，并双击打开。
2. 启动后，该程序将自动激活当前版本，等待该工具提示“激活成功”即可。

## 版本升级（C# ）

完成版本切换后，若老版本的二次开发程序以及对应的方案和流程需在新版本VM上使用，则需升级。

* **升级二次开发程序**：4.0或4.1版本升级到4.2及以上版本时，需按照以下步骤操作。4.2及以上版本间升级时，无需进行以下操作，直接打开即可。
  1. 使用备份工具DevelopProcedureUpgradeTool.exe将项目中debug文件夹下的内容进行备份。避免和4.2及以上版本的文件产生冲突，导致异常。
     备份工具所在路径为：..\Applications\Tools\4.0二次开发程序升级4.2版本工具。
  2. 使用引用工具ImportRef.exe为程序添加引用。
     引用工具所在路径为：..\Development\V4.x\ComControls\Tool。
* **方案和流程升级**：使用新版本VM平台打开用老版本VM搭建的方案或流程进行升级，并将方案另存为操作。

  注解
  :   特殊情况下，部分模块、参数或全局变量需要进行检查并微调。

## 注意事项

* VM4.x版本二次开发程序启动时需确保VM4.x软件能正常打开且方案能通过VM4.x软件正常运行。确认OK后，关闭VM后台程序，再启动二次开发程序，可正常使用。
* VM4.3版本二次开发部分接口名称发生变化，基本可以兼容VM4.2二次开发接口，针对VM4.0及VM4.1二次开发接口可使用程序中提示的推荐接口。
* 在已安装V4.x某个版本的PC上，再安装另一个V4.x版本时，先安装版本的算子会被备份。
* 若PC上存在多个版本的VM4.x且需卸载其中一个版本的VM4.x时，为确保能正常使用PC上其他版本的VM，请勿勾选卸载加密狗驱动、相机SDK和算子SDK。




<!-- ===== usergroup0.html | 编程引导 ===== -->

<!-- src:usergroup0.html -->
<!-- path:编程引导 -->
# 编程引导

* 配置流程
* 方案相关操作
* 模块相关操作
* 流程相关操作
* Group相关操作
* 全局模块相关操作
* 控件相关调用
* 事件




<!-- ===== usergroup1.html | 编程引导 > 配置流程 ===== -->

<!-- src:usergroup1.html -->
<!-- path:编程引导 > 配置流程 -->
# 配置流程

* WPF框架
* WinForm框架
* 动态库介绍及添加说明
* 控件中英文切换




<!-- ===== _w_p_f_xE6_xA1_x86_xE6_x9E_xB6.html | 编程引导 > 配置流程 > WPF框架 ===== -->

<!-- src:_w_p_f_xE6_xA1_x86_xE6_x9E_xB6.html -->
<!-- path:编程引导 > 配置流程 > WPF框架 -->
# WPF框架

本章节主要介绍WPF框架的配置流程及其注意事项。

## 控件调用

1. 动态库文件 VMControls.WPF.Release.dll 内，已定义以WPF方式封装的控件类。
2. 使用自动工具/手动添加该动态库及其依赖库的引用，推荐自动工具方式，工具路径：..\Development\V4.x\ComControls\Tool\ImportRef.exe。
3. 正常安装后，默认可从WPF工具箱中拖出控件。

   注解
   :   若工具箱中无对应控件，可通过右键菜单【选择项】打开【选择工具箱项】界面，然后手动浏览打开对应版本VMControls.WPF.Release.dll动态库文件，最后勾选WPF组件以添加对应控件。
4. （可选）：若不使用WPF工具箱，也可通过xaml设计器方式直接集成其中的控件。

## 注意事项

* 支持.NET Framework，要求4.6.1版本及以上，不支持.NET Core。
* 在项目属性中的平台目标选择【Any CPU】的情况下，需去除勾选【首选32位】。
* 手动添加VM相关动态库引用后，需设置库属性中的复制本地为【False】。
* 在程序退出前，可调用接口释放VM相关资源，请避免在析构函数中调用接口。
* 参数控件和参数渲染控件暂不支持记忆参数订阅框显示的默认方式。
* 独立Group控件暂不支持执行和耗时显示功能。




<!-- ===== _win_form_xE6_xA1_x86_xE6_x9E_xB6.html | 编程引导 > 配置流程 > WinForm框架 ===== -->

<!-- src:_win_form_xE6_xA1_x86_xE6_x9E_xB6.html -->
<!-- path:编程引导 > 配置流程 > WinForm框架 -->
# WinForm框架

本章节主要介绍WinForm框架的配置流程及其注意事项。

## 控件调用

1. 动态库文件 VMControls.Winform.Release.dll 内，已定义以Winform方式封装的控件类。
2. 使用自动工具/手动添加该动态库及其依赖库的引用，推荐自动工具方式，工具路径：..\Development\V4.x\ComControls\Tool\ImportRef.exe。
3. 正常安装后，默认可从WinForm工具箱中拖出控件。

   注解
   :   若工具箱中无对应控件，可通过右键菜单【选择项】打开【选择工具箱项】界面，然后手动浏览打开对应版本VMControls.Winform.Release.dll动态库文件，最后勾选.NET Framework组件以添加对应控件。

## 注意事项

* 支持.NET Framework，要求4.6.1版本及以上，不支持.NET Core。
* 在项目属性中的平台目标选择【Any CPU】的情况下，需去除勾选【首选32位】。
* 手动添加VM相关动态库引用后，需设置库属性中的复制本地为【False】。
* 程序退出前，可调用接口释放VM相关资源，请避免在析构函数中调用接口。
* 参数控件和参数渲染控件暂不支持记忆参数订阅框显示的默认方式。
* 独立Group控件暂不支持执行和耗时显示功能。




<!-- ===== _xE5_x8A_xA8_xE6_x80_x81_xE5_xBA_x93_xE4_xBB_x8B_xE7_xBB_x8D_xE5_x8F_x8A_xE6_xB7_xBB_xE5_x8A_xA0_xE8_xAF_xB4_xE6_x98_x8E.html | 编程引导 > 配置流程 > 动态库介绍及添加说明 ===== -->

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




<!-- ===== _xE6_x8E_xA7_xE4_xBB_xB6_xE4_xB8_xAD_xE8_x8B_xB1_xE6_x96_x87_xE5_x88_x87_xE6_x8D_xA2.html | 编程引导 > 配置流程 > 控件中英文切换 ===== -->

<!-- src:_xE6_x8E_xA7_xE4_xBB_xB6_xE4_xB8_xAD_xE8_x8B_xB1_xE6_x96_x87_xE5_x88_x87_xE6_x8D_xA2.html -->
<!-- path:编程引导 > 配置流程 > 控件中英文切换 -->
# 控件中英文切换

若需切换VM二次开发控件的显示语言，则需要手动修改**..\Development\V4.x\ComControls\Assembly\LangCFG**目录下的配置文件**LanguageSet.cfg**，如下图所示。

zh-cn 表示中文，en-us 表示英文。




<!-- ===== _xE6_x96_xB9_xE6_xA1_x88_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html | 编程引导 > 方案相关操作 ===== -->

<!-- src:_xE6_x96_xB9_xE6_xA1_x88_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 方案相关操作 -->
# 方案相关操作

方案相关操作主要包括加载方案、保存方案、获取方案版本与路径信息、禁用/启用流程、方案执行一次、连续执行、停止执行等。

## 接口调用流程

方案相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

方案相关操作示例代码如下，仅供参考。

```
using System;
using System.Collections.Generic;
using VM.Core;
using VM.PlatformSDKCS;

namespace VM.Test
{
 public class SolutionTest
    {
 static void Main()
        {
 try
            {
 //获取方案版本号
 string strVersion = VmSolution.Instance.GetSolutionVersion("D:\\Test.sol", "");

 //判断方案是否加密
 bool bPassword = VmSolution.Instance.HasPassword("D:\\Test.sol");

 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //获取当前方案路径
 string strPath = VmSolution.Instance.SolutionPath;

 //使用流程名称获取流程对象
                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];

 //获取方案所有流程对象
                List<VmProcedure> procedureList = new List<VmProcedure>();
                VmSolution.Instance.GetAllProcedureObjects(ref procedureList);

 //获取方案所有流程信息
 ProcessInfoList stProcInfoList = VmSolution.Instance.GetAllProcedureList();

 //获取方案所有模块信息
 ModuleInfoList stModuInfoList = VmSolution.Instance.GetAllModuleList();

 //使用流程名称禁用流程，禁用后流程不参与方案运行
                VmSolution.Instance.DisableProcedure("流程1");

 //使用流程名称启用流程
                VmSolution.Instance.EnableProcedure("流程1");

 //使用流程名称删除流程
                VmSolution.Instance.DeleteOneProcedure("流程2");

 //禁用方案所有流程/Group/模块回调，可提高运行效率，降低CPU资源依赖
 //注意若需获取流程/Group/模块输出，还需单独启用对应流程/Group/模块的回调
                VmSolution.Instance.DisableModulesCallback();
                vmProcedure.EnableResultCallback();

 //启用方案所有流程/Group/模块回调
                VmSolution.Instance.EnableModulesCallback();

 //方案同步执行一次
                VmSolution.Instance.SyncRun();

 //设置连续执行时间间隔
                VmSolution.Instance.SetRunInterval(500);

 //方案开始连续执行
                VmSolution.Instance.ContinuousRunEnable = true;

 //方案停止连续执行
                VmSolution.Instance.ContinuousRunEnable = false;

 //保存当前方案
                VmSolution.Save();

 //方案另存为
                VmSolution.SaveAs("D:\\Test1.sol", "");

 //关闭当前方案
                VmSolution.Instance.CloseSolution();

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




<!-- ===== _xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html | 编程引导 > 模块相关操作 ===== -->

<!-- src:_xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 模块相关操作 -->
# 模块相关操作

模块相关操作主要包括加载方案、获取模块对象、设置参数、运行、获取结果等。

## 接口调用流程

模块相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

模块相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using ImageSourceModuleCs;
using IMVSFastFeatureMatchModuCs;

namespace VM.Test
{
 public class ModuleTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用模块全名称获取模块对象
                ImageSourceModuleTool imageModu = (ImageSourceModuleTool)VmSolution.Instance["流程1.图像源1"];
                IMVSFastFeatureMatchModuTool fastMatchModu = (IMVSFastFeatureMatchModuTool)VmSolution.Instance["流程1.快速匹配1"];

 //通过模块对象接口获取模块参数对象，用于设置/获取模块参数
                imageModu.ModuParams.ImageSourceType = ImageSourceTypeEnum.SDK;

 //图像源模块选择SDK模式，可使用接口设置图像数据
 //注意设置后图像数据仅当次执行有效，执行完成后清空，再次执行需再次设置
                imageModu.SetImagePath("D:\\test.jpg");

 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                imageModu.SetImageData(inputImage);

 //方案同步执行一次
                VmSolution.Instance.SyncRun();

 //通过模块对象接口获取模块结果对象，用于获取模块输出
 //注意每次方案执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                ImageSourceResult imageSourceResult = imageModu.ModuResult;
 ImageBaseData outputImage = imageSourceResult.ImageData;

 //通过模块对象接口导入模型文件，注意会替换模块当前所有模型文件
 string[] moduDataPath = new string[1] { @"D:\test.fmxml" };
                fastMatchModu.ImportModelData(moduDataPath);

 //通过模块参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
                fastMatchModu.ModuParams.InputImage = outputImage;

 //通过模块参数对象接口获取模块ROI对象，用于设置模块ROI数据
 //注意设置后ROI数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 //注意设置图形和设置掩膜功能互斥，不会同时起效
                FastFeatureMatchRoiManager nFastFeatModuRoiManager = fastMatchModu.ModuParams.ModuRoiManager;

 VM.PlatformSDKCS.PointF nPointF = new VM.PlatformSDKCS.PointF(1, 1);
 RectBox nRectBox = new RectBox(nPointF, 100, 100, 90);
                nFastFeatModuRoiManager.RoiRectangle = nRectBox;
                nFastFeatModuRoiManager.MaskImage = outputImage;

 //通过模块对象接口自执行模块，仅该模块会同步执行一次，其余模块无动作
 //注意执行前需使用流程执行、接口设置等方式填充完毕模块执行所需输入数据，不然会执行错误
                fastMatchModu.Run();

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




<!-- ===== _xE6_xB5_x81_xE7_xA8_x8B_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html | 编程引导 > 流程相关操作 ===== -->

<!-- src:_xE6_xB5_x81_xE7_xA8_x8B_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 流程相关操作 -->
# 流程相关操作

流程相关操作主要包括导入流程、获取所有模块列表、禁用/启用流程、获取输出配置结果、流程执行一次、连续执行、停止执行、删除流程实例等。

## 接口调用流程

流程相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

流程相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;

namespace VM.Test
{
 public class ProcedureTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用流程名称获取流程对象
                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];

 //获取流程所有模块信息
 ModuleInfoList stModuInfoList = vmProcedure.GetAllModuleList();

 //获取流程本层级模块信息，不包含Group内部模块
 ModuleInfoList stSomeModuInfoList = vmProcedure.GetProcedureModuleList();

 //禁用流程，禁用后流程不参与方案运行
                vmProcedure.IsEnabled = false;

 //启用流程
                vmProcedure.IsEnabled = true;

 //通过流程对象接口获取流程局部变量对象，用于设置/获取局部变量等
                IVarModule procedureVar = vmProcedure.LocalVariable;

 //通过流程对象接口获取流程参数对象，用于设置输入数据、设置/获取模块参数等
                ProcedureParam procedureParam = vmProcedure.ModuParams;

 //通过流程参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                procedureParam.SetInputImage_V2("ImageData", inputImage);

 //流程同步执行一次
                vmProcedure.Run();

 //通过流程对象接口获取流程结果对象，用于获取流程输出
 //注意每次流程执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                ProcedureResult procedureResult = vmProcedure.ModuResult;
 ImageBaseData outputImage = procedureResult.GetOutputImageV2("ImageData0");

 //加载流程，仅支持绝对路径，编码格式UTF-8
 //注意非线程安全，不支持多线程调用
                vmProcedure = VmProcedure.Load("D:\\TestPrc.prc", "");

 //设置连续执行时间间隔
                vmProcedure.SetContinousRunInterval(500);

 //流程开始连续执行
                vmProcedure.ContinuousRunEnable = true;

 //流程停止连续执行
                vmProcedure.ContinuousRunEnable = false;

 //保存流程
 //注意非线程安全，不支持多线程调用
                vmProcedure.SaveAs("D:\\TestPrc1.prc", "");

 //删除流程
                vmProcedure.Dispose();

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




<!-- ===== _group_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html | 编程引导 > Group相关操作 ===== -->

<!-- src:_group_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > Group相关操作 -->
# Group相关操作

Group相关操作主要包括导入Group、获取模块列表、禁用/启用Group、自执行、导出Group、删除Group等。

## 接口调用流程

Group相关操作接口调用流程如下图所示。其中，蓝色框内容表示必选操作，橙色框内容表示可选操作。

## 示例代码

Group相关操作示例代码如下，仅供参考。

```
using System;
using VM.Core;
using VM.PlatformSDKCS;
using IMVSGroupCs;

namespace VM.Test
{
 public class GroupTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //使用Group全名称获取方案内Group对象
                IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];

 //禁用Group，禁用后Group不参与方案运行
                groupTool.DisableGroup();

 //启用Group
                groupTool.EnableGroup();

 //加载独立Group，仅支持绝对路径，编码格式UTF-8
 //注意非线程安全，不支持多线程调用
 //注意独立Group与方案并列，并非所属关系，无法使用方案对象获取或操作
                groupTool = IMVSGroupTool.LoadIndependentGroup("D:\\TestGro.gro");

 //获取Group所有模块信息
 GroupModuInfoList stModuInfoList = groupTool.GetAllModuleList();

 //通过Group对象接口获取Group参数对象，用于设置输入数据、设置/获取模块参数等
                GroupParam groupParam = groupTool.ModuParams;

 //通过Group参数对象接口设置输入数据
 //注意设置后输入数据仅当次执行有效，执行完成后清空，再次执行需再次设置
 int nWidth = 64;
 int nHeight = 64;
 int nDataLen = nWidth * nHeight;
 ImageBaseData inputImage = new ImageBaseData(new byte[nDataLen], (uint)nDataLen, nWidth, nHeight, VMPixelFormat.VM_PIXEL_MONO_08);
                groupParam.SetInputImage_V2("ImageData", inputImage);

 //Group同步执行一次
                groupTool.Run();

 //通过Group对象接口获取Group结果对象，用于获取Group输出
 //注意每次Group执行后，通过重新获取结果对象刷新其中输出数据
 //该操作存在耗时，建议获取结果对象后，直接使用对象获取具体输出数据
                GroupResult groupResult = groupTool.ModuResult;
 ImageBaseData outputImage = groupResult.GetOutputImageV2("ImageData0");

 //保存Group
 //注意非线程安全，不支持多线程调用
                groupTool.SaveAs("D:\\TestGro1.gro");

 //删除Group
                groupTool.DestroyGroup();

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




<!-- ===== _xE5_x85_xA8_xE5_xB1_x80_xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html | 编程引导 > 全局模块相关操作 ===== -->

<!-- src:_xE5_x85_xA8_xE5_xB1_x80_xE6_xA8_xA1_xE5_x9D_x97_xE7_x9B_xB8_xE5_x85_xB3_xE6_x93_x8D_xE4_xBD_x9C.html -->
<!-- path:编程引导 > 全局模块相关操作 -->
# 全局模块相关操作

全局模块相关操作主要包括全局变量、全局通信、全局光源、数据队列等全局模块功能交互。

## 示例代码

全局模块相关操作示例代码如下，仅供参考。

```
using VM.Core;
using VM.PlatformSDKCS;
using CommManagerModuleCs;
using DataQueueModuleCs;
using GlobalVariableModuleCs;
using GlobalCameraModuleCs;
using LightControlCs;
using System;
using System.Text;

namespace VM.Test
{
 public class GlobalModuleTest
    {
 static void Main()
        {
 try
            {
 //加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

 //中文VM下搭建的方案，使用全局模块中文名称获取模块对象
                GlobalVariableModuleTool globalVar = (GlobalVariableModuleTool)VmSolution.Instance["全局变量1"];
                CommManagerModuleTool commManager = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];
                DataQueueModuleTool dataQueue = (DataQueueModuleTool)VmSolution.Instance["数据队列1"];
                GlobalCameraModuleTool globalCamera = (GlobalCameraModuleTool)VmSolution.Instance["全局相机1"];
                LightControlTool lightControl = (LightControlTool)VmSolution.Instance["全局光源1"];

 //英文VM下搭建的方案，使用全局模块英文名称获取模块对象
                GlobalVariableModuleTool eGlobalVar = (GlobalVariableModuleTool)VmSolution.Instance["Global Variable1"];
                CommManagerModuleTool eCommManager = (CommManagerModuleTool)VmSolution.Instance["CommManagerModule1"];
                DataQueueModuleTool eDataQueue = (DataQueueModuleTool)VmSolution.Instance["Data Queue1"];
                GlobalCameraModuleTool eGlobalCamera = (GlobalCameraModuleTool)VmSolution.Instance["Global Camera1"];
                LightControlTool eLightControl = (LightControlTool)VmSolution.Instance["Light Control1"];

 //模块对象进行判空后，调用接口/属性实现操作
 if (null != globalVar)
                {
 //设置全局变量
                    globalVar.SetGlobalVar("var0", "100");

 //获取全局变量
 string tmp = globalVar.GetGlobalVar("var0");
                }
 //通信管理模块设置数据和获取数据，是否连接
 if (null != commManager)
                {
 // 设置字符串型数据
                    commManager.SetString(0, "abcd");
 int[] aIntVal = new int[3];
                    aIntVal[0] = 10;
                    aIntVal[1] = 11;
                    aIntVal[2] = 12;
 // 设置整型数据
                    commManager.SetInt(1, aIntVal, 0);
 byte[] btData = null;
                    commManager.GetReadData(1, ref btData);

 string strData = Encoding.UTF8.GetString(btData).TrimEnd('\0');

 bool isDeviceConnect = commManager.bIsDeviceConnect(1);
                }
 //全局光源模块设置全局参数信息
 if (null != lightControl)
                {
                    GlobalLightParam stLight = new GlobalLightParam();
                    stLight.nDeviceIndex = 1;
                    stLight.nDeviceType = (int)DeviceTypeEnum.TYPE_VC3000_GPIO;
                    stLight.nTriggerTime = 100;
 // 设置所有通道值
                    stLight.stLightConfig.stChannel1.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel1.bChannelEnable = true;
                    stLight.stLightConfig.stChannel1.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel1.nLightState = 1;
                    stLight.stLightConfig.stChannel1.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel1.nDurationTime = 10;

                    stLight.stLightConfig.stChannel2.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel2.bChannelEnable = true;
                    stLight.stLightConfig.stChannel2.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel2.nLightState = 1;
                    stLight.stLightConfig.stChannel2.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel2.nDurationTime = 10;

                    stLight.stLightConfig.stChannel3.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel3.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel3.nLightState = 1;
                    stLight.stLightConfig.stChannel3.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel3.nDurationTime = 10;

                    stLight.stLightConfig.stChannel4.nChannelIndex = 1;
                    stLight.stLightConfig.stChannel4.bChannelEnable = true;
                    stLight.stLightConfig.stChannel4.nLightBrightness = 150;
                    stLight.stLightConfig.stChannel4.nLightState = 1;
                    stLight.stLightConfig.stChannel4.nTriggerEdge = 1;
                    stLight.stLightConfig.stChannel4.nDurationTime = 10;

                    lightControl.SetGlobalLightParam(stLight);

                }
 //数据队列模块设置数据和获取数据
 if (null != dataQueue)
                {
                    StringValue stStr = new StringValue();
                    stStr.astValue = new StringInfo[256];
                    stStr.nNum = 1;
                    stStr.nIndex = 0;
                    stStr.astValue[0].strValue = "abcd";
                    dataQueue.SetStringData(stStr);
                    VmSolution.Instance.Run();
                    StringValue stVal = dataQueue.GetStringData(0);
                    VmSolution.Instance.Run();
                    IntValue stIntVal = dataQueue.GetIntData(1);
                    VmSolution.Instance.Run();
                    FloatValue stFloatVal = dataQueue.GetFloatData(2);

                }
 //全局相机模块设置触发源，获取相机列表+设置和获取选中相机
 if (null != globalCamera)
                {
                    globalCamera.ModuParams.TriggerSource = 1;
                    CameraInfoList cameraInfoList = globalCamera.ModuParams.GetCameraInfoList();

 string sn = globalCamera.ModuParams.GetChosenCameraSN();
                    globalCamera.ModuParams.SetChosenCameraSN(sn);

                }
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




<!-- ===== _xE6_x8E_xA7_xE4_xBB_xB6_xE7_x9B_xB8_xE5_x85_xB3_xE8_xB0_x83_xE7_x94_xA8.html | 编程引导 > 控件相关调用 ===== -->

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




<!-- ===== usergroup2.html | 编程引导 > 事件 ===== -->

<!-- src:usergroup2.html -->
<!-- path:编程引导 > 事件 -->
# 事件

* 事件设置方法
* 事件类型




<!-- ===== _xE4_xBA_x8B_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE6_x96_xB9_xE6_xB3_x95.html | 编程引导 > 事件 > 事件设置方法 ===== -->

<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:编程引导 > 事件 > 事件设置方法 -->
# 事件设置方法

事件设置方法的示例代码如下，仅供参考。

```
using System;
using System.Text;
using VM.Core;
using VM.PlatformSDKCS;
using IMVSCircleFindModuCs;
using IMVSGroupCs;

namespace VM.Test
{
 public class EventTest
    {
 static void Main()
        {
 try
            {
                EventClass eventClass = new EventClass();

 // 初始化订阅方案事件
                eventClass.InitSubscribeSolutionEvent();

 // 加载方案，仅支持绝对路径，编码格式UTF-8
                VmSolution.Load("D:\\Test.sol", "");

                VmProcedure vmProcedure = (VmProcedure)VmSolution.Instance["流程1"];
                if (null == vmProcedure) return;

 // 初始化订阅流程事件
                eventClass.InitSubscribeProcedureEvent(vmProcedure);

                IMVSGroupTool groupTool = (IMVSGroupTool)VmSolution.Instance["流程1.组合模块1"];
                if (null == groupTool) return;

 // 初始化订阅Group事件
                eventClass.InitSubscribeGroupEvent(groupTool);

                IMVSCircleFindModuTool circleFindModule = (IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
                if (null == circleFindModule) return;

 // 初始化订阅模块事件
                eventClass.InitSubscribeModuleEvent(circleFindModule);

 // 退出程序前释放所有资源，注意避免在析构函数中调用
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

 public class EventClass
    {
 // 初始化订阅方案事件
 public void InitSubscribeSolutionEvent()
        {
 // 流程工作状态
            VmSolution.OnWorkStatusEvent += Handle_OnWorkStatusEvent;

 // 加密狗状态
            VmSolution.OnDongleEvent += Handle_OnDongleEvent;

 // 开始加载方案
            VmSolution.OnSolutionLoadBeginEvent += Handle_OnSolutionLoadBeginEvent;

 // 方案加载结束
            VmSolution.OnSolutionLoadEndEvent += Handle_OnSolutionLoadEndEvent;

 // 模块方案加载进度
            VmSolution.OnSolutionLoadProgressEvent += Handle_OnSolutionLoadProgressEvent;

 // 服务状态回调，VM单进程版本不触发此事件
            VmSolution.OnServerStatusEvent += Handle_OnServerStatusEvent;

 // 代理崩溃，VM单进程版本不触发此事件
            VmSolution.OnProxyCrashEvent += Handle_OnProxyCrashEvent;

 // 流程解注册状态信息
            VmSolution.OnProcedureUnRegisterEvent += Handle_OnProcedureUnRegisterEvent;

 // 方案加载时模块错误警告信息
            VmSolution.OnModelLoadWarnEvent += Handle_OnModelLoadWarnEvent;

 // 连续执行开始状态信息
            VmSolution.OnProcessStatusStartEvent += Handle_OnProcessStatusStartEvent;

 // 连续执行结束状态信息
            VmSolution.OnProcessStatusStopEvent += Handle_OnProcessStatusStopEvent;

 // 模块结果信息回调
            VmSolution.OnModuleResultCallbackEvent += Handle_OnModuleResultCallbackEvent;

 // 接收数据回调（设备ID（1字节） AddressID（1字节） 数据）
            VmSolution.OnCommunicationRecvCallBackEvent += Handle_OnCommunicationRecvCallBackEvent;

 // 通信状态回调（状态 设备ID（1字节））
            VmSolution.OnCommunicationStatusCallBackEvent += Handle_OnCommunicationStatusCallBackEvent;

 // 相机取图结束信息回调
            VmSolution.OnCameraCollectCallBackEvent += Handle_OnCameraCollectCallBackEvent;

 // 相机取图开始信息回调
            VmSolution.OnCameraCollectStartCallBackEvent += Handle_OnCameraCollectStartCallBackEvent;

 // 通信连接状态回调
            VmSolution.OnCommuConnectCallBackEvent += Handle_OnCommuConnectCallBackEvent;

 // 相机连接状态回调
            VmSolution.OnCameraConnectStatusCallBackEvent += Handle_OnCameraConnectStatusCallBackEvent;

 // 相机模块添加事件
            VmSolution.OnGlobalCameraModuleAddedEvent += Handle_OnGlobalCameraModuleAddedEvent;

 // 相机模块删除事件
            VmSolution.OnGlobalCameraModuleDeletedEvent += Handle_OnGlobalCameraModuleDeletedEvent;
        }

 // 初始化订阅流程事件
 public void InitSubscribeProcedureEvent(VmProcedure vmProcedure)
        {
 // 流程开始执行状态回调
            vmProcedure.OnWorkBeginStatusCallBack += Handle_OnWorkBeginStatusCallBack;

 // 流程执行结束状态回调
            vmProcedure.OnWorkEndStatusCallBack += Handle_OnWorkEndStatusCallBack;
        }

 // 初始化订阅Group事件
 public void InitSubscribeGroupEvent(IMVSGroupTool groupModuTool)
        {
 // IO重命名事件
            groupModuTool.OnModuleIONameChanged += Handle_OnModuleIONameChanged;

 // 显示IO重命名事件
            groupModuTool.OnModuleDisplayParamNameChanged += Handle_OnModuleDisplayParamNameChanged;
        }

 // 初始化订阅模块事件
 public void InitSubscribeModuleEvent(VmModule vmModule)
        {
 // 模块结果回调
            vmModule.ModuleResultCallBackArrived += Handle_ModuleResultCallBackArrived;
        }

 // Solution 方案回调函数
 private void Handle_OnWorkStatusEvent(ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo)
        {
 // 获取流程ID，多个流程时用于区分流程
            uint processID = workStatusInfo.nProcessID;

 // 获取流程状态，1运行开始，0运行结束
            uint workStatus = workStatusInfo.nWorkStatus;

 // 获取流程耗时，仅在运行结束时有效
 float processTime = workStatusInfo.fProcessTime;
        }
 private void Handle_OnDongleEvent(ImvsSdkDefine.IMVS_DONGLE_INFO moduleInfo)
        {
 // 获取加密狗状态，正常时为0，异常时为错误码
 int dongleStatus = moduleInfo.nDongleStatus;

 // 获取加密狗型号
 byte[] bytDongleType = moduleInfo.strDongleType;
 string str = Encoding.UTF8.GetString(bytDongleType).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadBeginEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_BEGEIN_INFO solutionLoadBeginInfo)
        {
 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadBeginInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');

        }
 private void Handle_OnSolutionLoadEndEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_END_INFO solutionLoadEndInfo)
        {
 // 获取加载方案状态，正常时为0，异常时为错误码
            uint status = solutionLoadEndInfo.nStatus;

 // 获取加载方案的路径
 byte[] strSolPath = solutionLoadEndInfo.strSolPath;
 string str = Encoding.UTF8.GetString(strSolPath).TrimEnd('\0');
        }
 private void Handle_OnSolutionLoadProgressEvent(ImvsSdkDefine.IMVS_SOLUTION_LOAD_PROCESS_INFO solutionLoadProcessInfo)
        {
 // 获取加载方案的百分比进度，取值范围0~100
            uint process = solutionLoadProcessInfo.nProcess;

        }
 private void Handle_OnServerStatusEvent(ImvsSdkDefine.IMVS_SERVER_INFO moduleInfo)
        {
 // 获取服务进程状态，单进程版本不触发
            uint serverStatus = moduleInfo.nServerStatus;

        }
 private void Handle_OnProxyCrashEvent(ImvsSdkDefine.IMVS_PROXY_CRASH_SP_INFO proxyCrashInfoo)
        {
 // 获取代理进程状态，单进程版本不触发
 int hasSolStatu = proxyCrashInfoo.nHasSolStatu;

        }
 private void Handle_OnProcedureUnRegisterEvent(ImvsSdkDefine.IMVS_PROCEDURE_UNREGISTER_INFO procedureUnregisterInfo)
        {
 // 获取删除流程ID
            uint processID = procedureUnregisterInfo.nProcessID;

 // 获取删除流程名称
 byte[] strProcessName = procedureUnregisterInfo.strProcessName;
 string str = Encoding.UTF8.GetString(strProcessName).TrimEnd('\0');
        }
 private void Handle_OnModelLoadWarnEvent(ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO_LIST loadModuleInfoList)
        {
 // 获取加载方案时，加载失败模块的信息，包括模块ID/名称等
            uint moduleNum = loadModuleInfoList.nModuleNum;
 VM.PlatformSDKCS.ImvsSdkDefine.IMVS_LOAD_MODULE_ERROR_INFO[] astLoadModuErrInfo = loadModuleInfoList.astLoadModuErrInfo;
        }
 private void Handle_OnProcessStatusStartEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_START_CONTINUOUSLY_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnProcessStatusStopEvent(ImvsSdkDefine.IMVS_STATUS_PROCESS_STOP_INFO statusInfo)
        {
 // 获取连续执行流程ID
            uint processID = statusInfo.nProcessID;
        }
 private void Handle_OnModuleResultCallbackEvent(ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data moduleResultExInfo)
        {
 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = moduleResultExInfo.nErrorCode;

 // 获取流程/Group/模块ID
            uint moduleID = moduleResultExInfo.nModuleID;

 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = moduleResultExInfo.fModuleTime;

 // 获取流程/Group/模块算法耗时
 float algorithmTime = moduleResultExInfo.fAlgorithmTime;

 // 获取流程/Group/模块运行结果数据
 int resultNum = moduleResultExInfo.nResultNum;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data[] pInfo = moduleResultExInfo.pInfo;
 if (resultNum > 0)
            {
 // 获取其中一个结果数据
                ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_EX_Data pTmpData = pInfo[0];
 // 获取结果数据名称
 string str = pTmpData.strParamName;
            }
        }
 private void Handle_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 获取接收该数据的设备的类型
 int type = reportDataInfo.nType;

 // 获取接收的数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCommunicationStatusCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
        {
 // 该事件使用较复杂，建议使用事件OnCommuConnectCallBackEvent
 // 获取通信状态变更的设备的类型
 int type = reportDataInfo.nType;

 // 获取通信状态变更数据
            IntPtr pData = reportDataInfo.pData;
 int len = reportDataInfo.nLen;
        }
 private void Handle_OnCameraConnectStatusCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_CONNECT_STATUS_INFO cameraConnectStatusInfo)
        {
 // 获取相机ID
 int cameraID = cameraConnectStatusInfo->nCameraID;

 // 获取相机连接状态
 int connectStatus = cameraConnectStatusInfo->nConnectStatus;

 // 获取相机SN
 byte[] strCameraSN = cameraConnectStatusInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnGlobalCameraModuleAddedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnGlobalCameraModuleDeletedEvent(object sender, ModuInfo cameraInfo)
        {
 // 获取模块ID
            uint moduleID = cameraInfo.nModuleID;

 // 获取界面显示名称
 string strDisplayName = cameraInfo.strDisplayName;

 // 获取模块名称
 string strModuleName = cameraInfo.strModuleName;
        }
 private void Handle_OnCameraCollectCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图结束的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图结束的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCameraCollectStartCallBackEvent(ImvsSdkDefine.IMVS_CAMERA_COLLECT_INFO cameraCollectInfo)
        {
 // 获取取图开始的全局相机ID
            uint cameraID = cameraCollectInfo.nCameraID;

 // 获取当次取图帧号
            uint frameNum = cameraCollectInfo.nFrameNum;

 // 获取取图开始的全局相机SN
 byte[] strCameraSN = cameraCollectInfo.strCameraSN;
 string str = Encoding.UTF8.GetString(strCameraSN).TrimEnd('\0');
        }
 private void Handle_OnCommuConnectCallBackEvent(ImvsSdkDefine.IMVS_COMMUNICATION_CONNECT_INFO connectCollectInfo)
        {
 // 获取通信状态变更后的状态，连接为1，断开为0
            uint deviceStatus = connectCollectInfo.nDeviceStatus;

 // 获取通信状态变更的设备ID
            uint deviceID = connectCollectInfo.nDeviceID;
        }

 // Procedure 流程回调函数
 private void Handle_OnWorkBeginStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;
        }
 private void Handle_OnWorkEndStatusCallBack(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_WORK_STAUS data = (ImvsSdkDefine.IMVS_MODULE_WORK_STAUS)eventArgs.Value;

 // 获取流程ID
            uint processID = data.nProcessID;

 // 获取流程耗时
 float processTime = data.fProcessTime;
        }

 // Group 组合模块回调函数
 private void Handle_OnModuleIONameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }
 private void Handle_OnModuleDisplayParamNameChanged(string oldName, string newName)
        {
 // 获取原名称
 string tOldName = oldName;
 // 获取新名称
 string tNewName = newName;
        }

 // Module 模块回调函数
 private void Handle_ModuleResultCallBackArrived(object sender, EventArgs e)
        {
            VMControls.Interface.ValueEventArgs eventArgs = (VMControls.Interface.ValueEventArgs)e;
            ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data data = (ImvsSdkDefine.IMVS_MODULE_RESULT_INFO_LIST_EX_Data)eventArgs.Value;

 // 获取流程/Group/模块运行的错误码，可判断是否运行异常
            uint errorCode = data.nErrorCode;
 // 获取流程/Group/模块耗时，包含算法耗时
 float moduleTime = data.fModuleTime;
 // 获取流程/Group/模块算法耗时
 float algorithmTime = data.fAlgorithmTime;

 // 获取运行结果数据
            if (data.nResultNum > 0)
            {
 // 获取其中一个结果数据的名称
 string str = data.pInfo[0].strParamName;
            }
        }
    }
}
```




<!-- ===== _xE4_xBA_x8B_xE4_xBB_xB6_xE7_xB1_xBB_xE5_x9E_x8B.html | 编程引导 > 事件 > 事件类型 ===== -->

<!-- src:_xE4_xBA_x8B_xE4_xBB_xB6_xE7_xB1_xBB_xE5_x9E_x8B.html -->
<!-- path:编程引导 > 事件 > 事件类型 -->
# 事件类型

事件类型具体请见下表。

| 接口 | 类型 | C# 事件 | 描述 |
| --- | --- | --- | --- |
| **方案** | 流程工作状态 | OnWorkStatusEvent | 反馈流程执行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 加密狗状态 | OnDongleEvent | 反馈加密狗状态，在加密狗插拔等状态变更时触发 |
| 开始加载方案 | OnSolutionLoadBeginEvent | 反馈方案加载开始，方案加载期间其他大多数接口不支持调用，可用于屏蔽其他接口的调用 |
| 方案加载结束 | OnSolutionLoadEndEvent | 反馈方案加载结束，方案加载期间其他大多数接口不支持调用，可用于恢复其他接口的调用 |
| 模块方案加载进度 | OnSolutionLoadProgressEvent | 反馈方案加载的百分比进度，可用于粗略显示加载进度条 |
| 服务状态回调（VM单进程版本不触发此事件） | OnServerStatusEvent | 反馈服务进程状态，服务断线或崩溃时触发一次，单进程版本不触发 |
| 代理崩溃（VM单进程版本不触发此事件） | OnProxyCrashEvent | 反馈代理进程状态，代理断线或崩溃时触发一次，单进程版本不触发 |
| 流程解注册状态信息 | OnProcedureUnRegisterEvent | 反馈流程删除状态，每个流程被删除时触发一次 |
| 方案加载时模块错误警告信息 | OnModelLoadWarnEvent | 反馈方案加载中的警告，每个模块若由于系统环境等因素加载失败时触发一次 |
| 连续执行开始状态信息 | OnProcessStatusStartEvent | 反馈流程连续执行状态，每个流程开始连续执行时触发一次 |
| 连续执行结束状态信息 | OnProcessStatusStopEvent | 反馈流程连续执行状态，每个流程停止连续执行时触发一次 |
| 模块结果信息回调 | OnModuleResultCallbackEvent | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |
| 接收数据回调 | OnCommunicationRecvCallBackEvent | 反馈通信接收到的数据，每个通信设备接收到数据时触发一次 |
| 通信状态回调 | OnCommunicationStatusCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| 相机取图结束信息回调 | OnCameraCollectCallBackEvent | 反馈相机取图信息，每个全局相机每次取图结束时触发一次 |
| 相机取图开始信息回调 | OnCameraCollectStartCallBackEvent | 反馈相机取图信息，每个全局相机每次取图开始时触发一次 |
| 相机连接状态信息回调 | OnCameraConnectStatusCallBackEvent | 反馈相机连接状态信息，每个相机上下线及创建链接触发一次，可在回调中拿到相机相对应状态的数值 |
| 创建相机时模块信息回调 | OnGlobalCameraModuleAddedEvent | 反馈模块信息，创建全局相机模块时触发一次 |
| 删除相机时模块信息回调 | OnGlobalCameraModuleDeletedEvent | 反馈模块信息，删除全局相机模块时触发一次 |
| 通信连接状态回调 | OnCommuConnectCallBackEvent | 反馈通信设备状态，服务端设备开启和关闭时各触发一次，客户端设备连接和断开时各触发一次 |
| **流程** | 流程开始执行状态回调 | OnWorkBeginStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| 流程执行结束状态回调 | OnWorkEndStatusCallBack | 反馈流程运行状态，每个流程开始运行和结束运行时各触发一次，可在结束中获取结果数据，但避免进行同步渲染等耗时操作，阻塞流程下次运行 |
| **Group** | IO重命名事件 | OnModuleIONameChanged | 反馈Group输入输出设置修改，每个输入/输出名称修改时触发一次 |
| 显示IO重命名事件 | OnModuleDisplayParamNameChanged | 反馈Group显示设置修改，每个显示名称修改时触发一次 |
| **模块** | 模块结果回调 | ModuleResultCallBackArrived | 反馈运行结果数据，模块/Group/流程若已开启结果回调，每次运行后触发一次，可在其中获取结果数据，但避免进行同步渲染等耗时操作，阻塞下次运行 |




<!-- ===== usergroup3.html | 示例程序介绍 ===== -->

<!-- src:usergroup3.html -->
<!-- path:示例程序介绍 -->
# 示例程序介绍

* 平台型示例程序
* 应用型示例程序




<!-- ===== usergroup4.html | 示例程序介绍 > 平台型示例程序 ===== -->

<!-- src:usergroup4.html -->
<!-- path:示例程序介绍 > 平台型示例程序 -->
# 平台型示例程序

* 方案
* 流程
* Group
* 圆查找
* 运行界面
* 获取结果




<!-- ===== _xE6_x96_xB9_xE6_xA1_x88_xE7_xA4_xBA_xE4_xBE_x8B.html | 示例程序介绍 > 平台型示例程序 > 方案 ===== -->

<!-- src:_xE6_x96_xB9_xE6_xA1_x88_xE7_xA4_xBA_xE4_xBE_x8B.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > 方案 -->
# 方案

方案示例（SolutionControl Demo）主要展示方案配合流程配置控件如何使用，以及方案对象中部分接口如何调用。

## Demo介绍

Demo启动后需先加载方案再进行其他操作，可在流程配置区编辑方案。

方案的Demo界面如下图所示，WinForm和WPF的界面有所差别。

### SolutionControl\_WinForm：

### SolutionControl\_WPF：

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | 方案操作接口 | 可对方案进行操作，主要为方案加载、保存和关闭等。 |
| 2 | 消息显示区 | 可显示Demo运行过程中的消息。 |
| 3 | 流程配置区/主界面区 | 可对方案中的流程进行配置。 |

## 操作步骤

1. 点击方案操作接口区域的【选择方案路径】，选择需打开的.sol方案文件。此时“方案路径”处显示当前打开方案的路径。
2. 在“方案密码”处输入当前选择方案的密码。

   注解
   :   若方案未设置密码，则跳过此步骤。
3. 点击【加载方案】在Demo中打开选择的方案。
4. 通过方案操作接口可获取方案相关信息，并在消息显示区显示相关消息。
   * 【获取方案路径】：可获取加载方案的路径信息。
   * 【获取方案版本】：可获取加载方案的版本信息。
   * 【检查方案密码】：可获取加载方案的密码。若方案未设置密码，则显示没有密码。
   * 【锁定工作区】：点击后流程配置区/主界面区显示“界面操作锁定”，只能对方案中的模块参数进行配置，无法对流程和模块进行添加和删除。
   * 【解锁工作区】：可对锁定的工作区进行解锁操作。

   注解
   :   WPF的Demo界面无锁定工作区和解锁工作区。
5. 通过 流程配置区/主界面区 可对加载方案的相关流程和参数进行设置。

   注解
   :   操作方法与算法平台软件一致，具体可参考软件用户手册。
6. 点击【清空信息】可删除消息显示区的的全部历史信息。
7. 操作完成后，点击【保存方案】可对加载的方案进行保存。

   注解
   :   点击【关闭方案】可将加载的方案关闭。




<!-- ===== _xE6_xB5_x81_xE7_xA8_x8B_xE7_xA4_xBA_xE4_xBE_x8B.html | 示例程序介绍 > 平台型示例程序 > 流程 ===== -->

<!-- src:_xE6_xB5_x81_xE7_xA8_x8B_xE7_xA4_xBA_xE4_xBE_x8B.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > 流程 -->
# 流程

流程示例（ProcessControl Demo）主要展示方案中流程配合流程配置控件如何使用，同时还可导入/导出流程，控制流程执行、禁用和启用。

## Demo介绍

Demo启动后可先加载方案再进行其他操作，也可直接导入流程，可在流程配置区编辑方案。

流程的Demo界面如下图所示。

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | 方案操作接口 | 可对方案进行操作，主要为方案加载和保存等。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 2 | 流程操作接口 | 可对流程进行操作，主要为导入、导出和删除流程。 |
| 3 | 流程控制接口 | 可对流程进行控制，主要为流程执行、执行的间隔时间和禁用流程。 |
| 4 | 消息显示区 | 可显示Demo运行过程中的消息。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 5 | 流程配置区 | 可对方案中的流程或导入的流程进行配置。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |

## 操作步骤

1. 在方案操作接口区域加载方案，相关介绍请见方案（SolutionControl）章节。

   注解
   :   也可不加载方案，直接导入流程。
2. 点击流程操作接口的【选择文件路径】选择需打开的.prc流程文件。
3. 点击【导入流程】，此时流程配置区显示当前导入的流程。
4. 根据流程配置区显示的流程名称，在“流程名”处输入需进行相关操作的流程名称。
5. 可对加载的流程进行相关设置。
   * 点击【单次执行】、【连续执行】和【停止执行】可对流程执行相应操作。
   * 在“连续执行时间间隔”处输入间隔时间，并点击【设置时间间隔】可设置流程连续执行时的间隔时间，单位为ms。
   * 点击【禁用流程】可将流程禁用。
6. 点击【导出流程】可将流程导出到选择的流程路径下。
7. 点击【删除流程】可将流程在流程配置区删除。




<!-- ===== _group.html | 示例程序介绍 > 平台型示例程序 > Group ===== -->

<!-- src:_group.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > Group -->
# Group

Group示例（GroupControl Demo）主要展示独立的Group如何导入/导出，绑定参数配置控件如何修改参数，绑定渲染控件如何展示渲染效果。

## Demo介绍

Group需从VM中导出，且配置完整，具备独立运行的条件。

Group的Demo界面如下图所示。

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | Group操作 | 可对Group进行导入和导出操作。 |
| 2 | Group显示区 | 可对Group中的模块以及Group自身进行相关设置。 |
| 3 | 消息显示区 | 可显示Demo运行过程中的消息。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 4 | 结果渲染区 | 可显示demo运行后的结果。 |

## 操作步骤

1. 点击【选择Group路径】，选择需打开的.gro文件。
2. 点击【导入Group】将选择的gro文件导入到demo中。
3. 可通过Group显示区对相关模块和Group进行设置。
4. 点击【执行一次】可对导入的Group以当前设置的参数执行一次。此时结果渲染区显示运行的结果。
5. 点击【导出Group】可将demo中修改后的Group导出到本机PC上。
6. 点击【清空信息】可删除消息显示区的的全部历史信息。




<!-- ===== _xE5_x9C_x86_xE6_x9F_xA5_xE6_x89_xBE.html | 示例程序介绍 > 平台型示例程序 > 圆查找 ===== -->

<!-- src:_xE5_x9C_x86_xE6_x9F_xA5_xE6_x89_xBE.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > 圆查找 -->
# 圆查找

圆查找示例（CircleFind Demo）主要展示如何加载包含圆查找模块的方案，绑定参数配置控件如何修改配置参数，以及如何展示渲染效果。其他算法平台中的算法与逻辑模块可参考此示例进行二次开发。

## Demo介绍

圆查找的Demo界面如下图所示。

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | 方案操作接口 | 可对方案进行操作，主要为加载方案和保存方案等。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 2 | 模块操作区 | 可对模块进行绑定参数、方案执行和获取结果的操作。 |
| 3 | 消息显示区 | 可显示Demo运行过程中的消息。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 4 | 参数配置区 | 可对圆查找模块的相关参数进行设置。 |
| 5 | 结果渲染区 | 可显示demo运行后的结果。 |

## 操作步骤

1. 在方案操作接口区域加载方案，相关介绍请见方案（SolutionControl）章节。

   注解
   :   加载的方案中必须至少包含1个以上圆查找模块。
2. 点击【绑定参数】，此时参数配置区显示相关参数。

   注解
   :   相关参数主要分为基本参数、运行参数和结果显示三个部分。可根据需求进行设置，操作方法与算法平台软件一致，具体可参考软件用户手册。
3. 点击【执行一次】可将该方案以当前设置的参数执行一次，此时结果渲染区显示运行的结果。
4. 点击【获取结果】，此时消息显示区显示圆查找模块的结果信息。




<!-- ===== _xE8_xBF_x90_xE8_xA1_x8C_xE7_x95_x8C_xE9_x9D_xA2.html | 示例程序介绍 > 平台型示例程序 > 运行界面 ===== -->

<!-- src:_xE8_xBF_x90_xE8_xA1_x8C_xE7_x95_x8C_xE9_x9D_xA2.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > 运行界面 -->
# 运行界面

运行界面示例（FrontendControl Demo）主要展示方案中运行界面相关操作如何进行二次开发。

## Demo介绍

运行界面的Demo界面如下图所示。

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | 方案操作接口 | 可对方案进行操作，可加载方案，加载方案已配置运行界面。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 2 | 运行界面控制区 | 可对运行界面进行相关控制。 |
| 3 | 消息显示区 | 可显示Demo运行过程中的消息。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 4 | 运行界面渲染区 | 可显示方案的运行界面。 |

## 操作步骤

1. 在方案操作接口区域加载方案，相关介绍请见方案（SolutionControl）章节。

   注解
   :   也可不加载方案，直接导入流程。
2. 点击运行界面控制区的【加载界面数据】，此时运行界面渲染区显示方案中配置的运行界面。

   注解
   :   若点击“加载界面数据”后，运行界面渲染区显示为全黑，则说明当前加载方案未配置运行界面。
3. 点击【窗口缩小】或【窗口放大】可分别对运行界面渲染区进行缩小或放大。
4. 点击【单次执行】可对加载的方案执行一次。
5. 点击【清空信息】可删除消息显示区的的全部历史信息。




<!-- ===== _xE8_x8E_xB7_xE5_x8F_x96_xE7_xBB_x93_xE6_x9E_x9C.html | 示例程序介绍 > 平台型示例程序 > 获取结果 ===== -->

<!-- src:_xE8_x8E_xB7_xE5_x8F_x96_xE7_xBB_x93_xE6_x9E_x9C.html -->
<!-- path:示例程序介绍 > 平台型示例程序 > 获取结果 -->
# 获取结果

获取结果示例（GetResultControl Demo）主要展示如何通过二次开发在回调中获取数据结果。

## Demo介绍

获取结果的Demo界面如下图所示。

Demo界面中各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | 方案操作接口 | 可选择方案路径和加载方案。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 2 | 获取结果操作接口 | 可获取方案相关结果。 |
| 3 | 渲染 | 可将方案中的图像和图像渲染区绑定显示。 |
| 4 | 消息显示区 | 可显示Demo运行过程中的消息。  相关功能和SolutionControl示例相同，具体介绍请见方案（SolutionControl）章节。 |
| 5 | 流程配置区 | 可对方案中的流程进行配置。 |
| 6 | 图像渲染区 | 可显示渲染绑定的图像数据。 |

## 操作步骤

1. 点击方案操作接口区域的【选择方案路径】，选择需打开的.sol方案文件。此时“方案路径”处显示当前打开方案的路径。
2. 在“方案密码”处输入当前选择方案的密码。

   注解
   :   若方案未设置密码，则跳过此步骤。
3. 点击【加载方案】在Demo中打开选择的方案，加载成功时进度显示为100。
4. 通过获取结果操作接口可获取方案相关结果。
   * 【获取图像源结果】：可获取图像源数据。
   * 【回调获取图像源结果】：可通过回调的方式获取图像源数据。
   * 【获取流程结果】：可获取流程输出的结果。
5. 点击【渲染绑定】可将图像与最右侧的渲染窗口绑定。

   注解
   :   点击【渲染解绑】可解除图像与渲染窗口的绑定。
6. 点击【执行一次】，流程运行一次。

   注解
   :   若已进行渲染绑定，则渲染窗口可显示执行结果。




<!-- ===== usergroup5.html | 示例程序介绍 > 应用型示例程序 ===== -->

<!-- src:usergroup5.html -->
<!-- path:示例程序介绍 > 应用型示例程序 -->
# 应用型示例程序

* 基础介绍
* OCR识别案例
* 定位引导案例
* 深度学习案例




<!-- ===== _xE5_x9F_xBA_xE7_xA1_x80_xE4_xBB_x8B_xE7_xBB_x8D.html | 示例程序介绍 > 应用型示例程序 > 基础介绍 ===== -->

<!-- src:_xE5_x9F_xBA_xE7_xA1_x80_xE4_xBB_x8B_xE7_xBB_x8D.html -->
<!-- path:示例程序介绍 > 应用型示例程序 > 基础介绍 -->
# 基础介绍

C# 提供部分应用型示例程序，分别为OCRDemoCs（字符识别示例）、LocateDemoCs（抓取定位示例）、DeepLearningDemoCs（深度学习示例）。

* OCRDemoCs：字符识别示例，用于展示字符识别相关应用方面的二次开发。
* LocateDemoCs：抓取定位示例，用于展示抓取定位相关应用方面的二次开发。
* DeepLearningDemoCs：深度学习示例，用于展示深度学习相关应用方面的二次开发。

## Demo介绍

Demo界面如下图所示。

Demo界面各个区域的具体功能介绍请见下表。

| 编号 | 名称 | 功能说明 |
| --- | --- | --- |
| 1 | VM控件区 | 可加载VM的图像显示窗口，或同时加载VM的模块编辑和图像显示区域。 |
| 2 | 结果显示区 | 显示方案运行的结果。 |
| 3 | 方案操作区 | 可选择并加载方案，进行相关设置。 |
| 4 | 消息显示区 | 可显示Demo运行过程中的消息。 |

## 操作步骤

1. 点击【选择方案】选择需打开的方案。
   各Demo文件夹下有示例方案，可直接使用。
2. 点击【加载方案】。
3. “选择流程”处根据实际需求选择需执行的方案。
4. 点击【单次运行】或【连续运行】可运行选择的流程。此时Demo界面左侧显示图像结果和运行结果。
5. （可选操作）若需要对方案中的相关参数进行设置，可点击【参数配置】在Demo左侧进行设置，相关操作与VM完全一致。
6. 点击【保存方案】可保存当前加载方案的设置。




<!-- ===== _o_c_r_xE8_xAF_x86_xE5_x88_xAB_xE6_xA1_x88_xE4_xBE_x8B.html | 示例程序介绍 > 应用型示例程序 > OCR识别案例 ===== -->

<!-- src:_o_c_r_xE8_xAF_x86_xE5_x88_xAB_xE6_xA1_x88_xE4_xBE_x8B.html -->
<!-- path:示例程序介绍 > 应用型示例程序 > OCR识别案例 -->
# OCR识别案例

## 一、应用场景

本案例作为VM二次开发的OCR识别案例，适用场景为需要使用深度学习进行OCR识别的场景。

## 二、搭建方案

示例方案路径：./PlatformSDKSampleCS/OCRDemoCs/OCRDemo.sol

### 方案思路

本演示案例为应用案例，软件和具体方案是强相关的。可加载设计好的方案，该演示方案为Demo文件夹下的OCRDemo.sol方案。若导入其他案例提供的方案，则需进行相关配置方可运行出正确结果。

方案具体流程如下：

1. 使用VisionTrain1.4.1训练平台进行深度学习模型训练得到两个训练模型，文件后缀为bin。分别为CnnCharDetect.bin（字符定位模型）和CnnOcrRecog.bin（字符识别模型）。
2. 在VisionMaster中拖拽图像源模块加载图像。
3. 使用DL字符定位模块进行字符串的定位。
4. 使用DL字符识别模块进行识别。

方案整体流程如下图所示。

### 耦合模块

方案的数据结果经过格式化模块汇总，并在流程“输出设置”中订阅，可在二次开发中拿流程输出结果，降低二次开发软件与具体模块的耦合性。

开发获取结果的是流程输出的“out”参数，开发渲染控件RenderControl绑定的渲染为图像源图像、DL字符定位输出矩形框、格式化文本，具体操作如下：

1. 点击流程图标旁边的小扳手图标进入流程配置窗口。
2. 点击【输出设置】，其中参数名称下面的“out”（区分大小写）即为开发获取的参数名，点击“订阅”，选择格式化作为绑定数据，具体如下图所示。
3. 点击【显示设置】，点击“加号”可增加需要的渲染，点击“订阅”按钮可绑定渲染内容，配置方式如下图所示。
4. 配置格式化模块内容。

   格式化模块必须配置正确。若使用时修改了案例自带的方案，特别是修改格式化模块订阅的数据，则必须参照案例自带的方案进行格式化模块配置，格式如下图所示。
   其中，主要包含：DL字符识别模块的模块状态、最优字符个数、最佳字符串信息、最优字符串置信度。

## 三、二次开发

### 运行逻辑

在Visual Studio中直接调试运行，或者在 bin 目录下双击OCRDemoCs.exe 运行。OCRDemo界面如下图所示。

**操作逻辑：**

1. 弹出软件运行界面后，在方案操作区域点击【选择方案】，选择完成后点击【加载方案】。
2. 在流程操作区域选择需要执行的流程名，点击【单次运行】或【连续运行】即可执行流程。

相关操作函数如下图所示。

先是选择方案函数和加载方案函数，然后是执行一次函数，最后是流程执行回调函数（用于获取算法执行结果）。其中，流程执行回调需要在构造函数中进行注册。

### 主要函数

本案例的主要函数包括：方案加载、单次执行、连续执行、注册方案状态回调、获取结果、方案保存和渲染界面绑定。

* 方案加载

  ```
  VmSolution.Load(strSolutionPath);           //参数为选择的方案路径
  VmSolution.Load(strSolutionPath,”***”);     //参数为选择的方案路径，方案密码
  ```
* 单次执行

  ```
  procedure = VmSolution.Instance[“流程1”] as VmProcedure;      //[]内参数填流名
  procedure.Run();//运行流程
  ```
* 连续运行

  ```
  procedure.ContinuousRunEnable = true;       //开启连续运行
  procedure.ContinuousRunEnable = false;      //停止连续运行
  ```
* 方案状态回调

  ```
  VmSolution.OnWorkStatusEvent += VmSolution_OnWorkStatusEvent;   //注册方案状态回调
  private void VmSolution_OnWorkStatusEvent(VM.PlatformSDKCS.ImvsSdkDefine.IMVS_MODULE_WORK_STAUS workStatusInfo)//回调函数实现
  {
   if (workStatusInfo.nWorkStatus == 0 && workStatusInfo.nProcessID == 10000)  //流程执行完毕，且为第一个流程
      {
   //获取结果
      }
  }
  ```
* 结果获取

  ```
  string strResult = procedure.ModuResult.GetOutputString(“out”).Value.astStringVal[0].strValue;//()内参数为流程输出的参数名
  ```
* 方案保存

  ```
  VmSolution.Save();
  ```
* 渲染界面绑定

  ```
  if(VmSolution.Instance[“流程1”]!=null)
  {
      renderControl1.ModuleSource = (VmProcedure)VmSolution.Instance[“流程1”];
  }
  ```

### 控件说明

本案例涉及3个控件，分别为VmRenderControl控件、VmMainViewConfigControl控件和VmGlobalToolControl控件。

* VmRenderControl控件：用于渲染图像数据。
* VmMainViewConfigControl控件：用于显示流程配置。
* VmGlobalToolControl控件：用于显示全局配置工具。




<!-- ===== _xE5_xAE_x9A_xE4_xBD_x8D_xE5_xBC_x95_xE5_xAF_xBC_xE6_xA1_x88_xE4_xBE_x8B.html | 示例程序介绍 > 应用型示例程序 > 定位引导案例 ===== -->

<!-- src:_xE5_xAE_x9A_xE4_xBD_x8D_xE5_xBC_x95_xE5_xAF_xBC_xE6_xA1_x88_xE4_xBE_x8B.html -->
<!-- path:示例程序介绍 > 应用型示例程序 > 定位引导案例 -->
# 定位引导案例

## 一、应用场景

本案例作为VM二次开发的定位引导案例，适用场景为单相机拍照，引导机械手抓取产品的情形。

典型场景包括：

* 相机固定安装，拍照时相机固定不动。
* 机械手旋转时旋转中心不在抓取点上，而是绕某个轴的中心旋转。如下图所示，机械手的旋转轴中心线如图中红线所示，和抓取中心并不重合。

注解
:   本案例演示重点为如何使用VM模块去实现定位抓取，并未考虑图像透视和畸变带来的抓取精度问题，因此若实际项目中照搬案例中的方法去引导机械手抓取，被抓产品可能越靠近视野边缘抓取误差越大，越靠近视野中心区域误差越小，此为正常现象。

## 二、搭建方案

示例方案路径：./PlatformSDKSampleCS/LocateDemoCs/LocateDemoCs.sol

### 方案思路

本演示案例为应用案例，软件和具体方案是强相关的。可加载设计好的方案，该演示方案为Demo文件夹下的LocateDemo.sol方案。若导入其他案例提供的方案，则需进行相关配置方可运行出正确结果。

本方案包含一个标定流程和生产流程，流程的整体框架如下图所示。

* 标定流程使用标定板，通过查找标定物中两条边缘直线的交点作为标定图像输入点。
* 生产流程通过旋转计算模块来计算运行图像点和示教图像点的偏差。偏差包含两部分：一部分是由纯平移（不考虑旋转）产生的平移偏差，另一部分是由机械手不共轴旋转产生的偏差。两者偏差加在一起便是示教点与运行点的坐标偏差。

### 耦合模块

方案的数据结果经过格式化模块汇总，并在流程“输出设置”中订阅，可在二次开发中通过流程输出结果，降低二次开发软件与具体模块的耦合性。

开发获取结果的是流程输出的“out”参数，开发渲染控件RenderControl绑定的渲染为图像源图像、DL字符定位输出矩形框、格式化文本，具体操作如下：

1. 点击流程图标旁边的“模块配置”图标进入流程配置窗口。
2. 点击【输出设置】，其中参数名称下面的“out”（区分大小写）即为开发获取的参数名，点击“订阅”按钮，选择格式化作为绑定数据，具体如下图所示。
3. 点击【显示设置】，点击“加号”可增加需要的渲染，点击“订阅”按钮可绑定渲染内容，配置方式如下图所示。
4. 配置格式化模块内容。

   格式化模块必须配置正确。若使用时修改了案例自带的方案，特别是修改格式化模块订阅的数据，则必须参照案例自带的方案进行格式化模块配置，格式为：[条件检测结果INT],[数据项1],[数据项2],[数据项3]

   * [ ]内的数据订阅流程中的模块结果输出，各个条目用英文逗号分隔，标定流程的格式化配置如下图所示。
   * 生产流程的格式化模块的配置类似，由条件检测结果、数据项组成，各条目用英文逗号分隔，在此不再赘述，请参照生产流程的格式化模块配置。

## 三、二次开发

### 运行逻辑

在Visual Studio直接调试，或者在bin目录下双击LocateDemoCs.exe运行。LocateDemo界面如下图所示。

**操作逻辑：**

1. 弹出软件运行界面后，在方案操作区域点击【选择方案】，选择完成后点击【加载方案】。
2. 在流程操作区域选择需要执行的流程名，点击【运行一次】或【连续运行】即可执行流程。

### 主要函数

本案例主要函数包括：方案加载、单次执行、连续执行、注册工作结束回调、结果获取、方案保存和渲染界面绑定。

* 方案加载

  ```
  VmSolution.Load(currentSolutionPath);
  例如：
       VmSolution.Load(“D:\\Test\\Test.sol”,“abc123”);
  ```
* 单次执行

  ```
  procedure.Run();
  ```
* 连续运行

  ```
  procedure.ContinuousRunEnable = true;       //开启连续执行
  procedure.ContinuousRunEnable = false;      //停止连续执行
  ```
* 注册工作结束回调：注册回调是基于使用事件模型，使用户获取流程运行的结果

  ```
  foreach (var vmProcedure in processList)
  {
       vmProcedure.OnWorkEndStatusCallBack += VmProcedure_OnWorkEndStatusCallBack;
  }
  ```
* 结果获取

  ```
  private void VmProcedure_OnWorkEndStatusCallBack(object sender, EventArgs e)
  {
   try
       {
           VmProcedure procedure = sender as VmProcedure;
   if (procedure != null)
          {
   //此处添加获取结果代码
           }
       }
   catch (Exception ex)
       {
         AppendLog(ex.Message);
       }
  }
  ```
* 方案保存

  ```
  VmSolution.Save();
  ```
* 渲染界面绑定

  ```
  renderControl.ModuleSource = (VmProcedure)VmSolution.Instance[“流程1”];
  ```

### 控件说明

本案例涉及3个控件，分别为VmRenderControl控件、VmMainViewConfigControl控件和VmGlobalToolControl控件。

* VmRenderControl控件：用于渲染图像数据。
* VmMainViewConfigControl控件：用于显示流程配置。
* VmGlobalToolControl控件：用于显示全局配置工具。




<!-- ===== _xE6_xB7_xB1_xE5_xBA_xA6_xE5_xAD_xA6_xE4_xB9_xA0_xE6_xA1_x88_xE4_xBE_x8B.html | 示例程序介绍 > 应用型示例程序 > 深度学习案例 ===== -->

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




<!-- ===== usergroup8.html | 工具 ===== -->

<!-- src:usergroup8.html -->
<!-- path:工具 -->
# 工具

* 异常信息收集工具
* 环境检测工具




<!-- ===== _xE5_xBC_x82_xE5_xB8_xB8_xE4_xBF_xA1_xE6_x81_xAF_xE6_x94_xB6_xE9_x9B_x86_xE5_xB7_xA5_xE5_x85_xB7.html | 工具 > 异常信息收集工具 ===== -->

<!-- src:_xE5_xBC_x82_xE5_xB8_xB8_xE4_xBF_xA1_xE6_x81_xAF_xE6_x94_xB6_xE9_x9B_x86_xE5_xB7_xA5_xE5_x85_xB7.html -->
<!-- path:工具 > 异常信息收集工具 -->
# 异常信息收集工具

异常信息收集工具可收集电脑配置信息、log文件、VM版本、算子版本信息、算子SDK日志、dump和二次开发相关日志等，主要用于程序使用出现问题时收集相关信息并提供给技术人员进行问题排查。
异常信息收集工具名称为 AbnormalInfoCollectTool.exe ，所在路径为：..\Applications\Tools\AbnormalInfoCollectTool 。

**工具使用方法：**

1. 双击打开 AbnormalInfoCollectTool.exe ，等待界面打印至收集结束。
2. 根据最后提示的文件路径可获取压缩包，如下图所示。

注解
:   * 在使用过程中，当提示有文件被占用时，打开【任务管理器】根据提示的进程名称和ID手动关闭相关进程，再点击【重试】继续收集即可。
    * 在收集VM其他版本（如VM4.0、VM4.1等）相关信息时，需拷贝 AbnormalInfoCollectTool 文件夹至对应程序路径下使用。
    * 提示是否收集二次开发相关日志时输入“y”并按“Enter”键；然后根据提示输入二次开发exe所在的路径，再按“Enter”键即可开始收集。




<!-- ===== _xE7_x8E_xAF_xE5_xA2_x83_xE6_xA3_x80_xE6_xB5_x8B_xE5_xB7_xA5_xE5_x85_xB7.html | 工具 > 环境检测工具 ===== -->

<!-- src:_xE7_x8E_xAF_xE5_xA2_x83_xE6_xA3_x80_xE6_xB5_x8B_xE5_xB7_xA5_xE5_x85_xB7.html -->
<!-- path:工具 > 环境检测工具 -->
# 环境检测工具

VisionMaster软件安装完成后，在二次开发的过程可能遇到一些典型性问题，例如：由于环境变量未生效导致未找到iMVS-6000PlatformSDK.dll，或者找到错误版本的iMVS-6000PlatformSDK.dll。
为了解决以上问题，建议使用环境检测工具，工具名称为：**VMCollector.exe**，所在路径为：..\Applications\Tools\VMCollector。

环境检测工具主要检测如下内容：

* **VisionMaster检测**
  1. 获取当前默认的VisionMaster版本：

     通过获取注册表SOFTWARE\WOW6432Node\Microsoft.NETFramework\v4.0.30319\AssemblyFoldersEx\VisionMaster的数值所包含的版本信息。该版本的语言类型通过LanguageSet.cfg文件读取获得。
  2. 获取当前运行的VisionMaster版本：

     通过获取进程中的VisionMaster程序，得到程序启动路径，然后将路径和所有版本中的信息进行对比得到当前运行版本号。该版本的语言类型通过LanguageSet.cfg文件读取获得。

     注意
     :   VisionMaster软件名称可通过中性包工具进行修改，为了获取该软件的实际名称，需要从配置文件读取软件名称。由于中性包工具没有修改注册表名称，因此不能从注册表直接获取软件名称。
  3. 判断VisionMaster系统环境变量设置是否正确：

     检测系统环境变量Path是否保存当前版本VisionMaster的路径。例如：4.2版本为当前默认版本，则需添加如下环境变量：

     D:\Program Files\VisionMaster4.2.0\Applications\PublicFile\x64
     D:\Program Files\VisionMaster4.2.0\Applications\PublicFile\x86

     注意
     :   若将以上路径添加在Path的末尾，则一些同名库的使用，会被Path列表中靠前的路径指错目录，导致运行异常。因此，需要将以上路径添加到Path的最前面。
* **二次开发依赖DLL检测**
  1. 加载当前系统环境变量中的iMVS-6000PlatformSDK.dll：

     尝试加载iMVS-6000PlatformSDK.dll，判断加载是否成功。若不成功，则提示错误信息。
  2. 使用iMVS-6000PlatformSDK.dll创建句柄：

     尝试进行初始化，判断过程是否成功。若不成功，则抛出对应错误码。如：加密狗未检测到或检测异常，可以通过检查加密狗是否插好来排查故障。




<!-- ===== usergroup9.html | 常见问题 ===== -->

<!-- src:usergroup9.html -->
<!-- path:常见问题 -->
# 常见问题

* 如何排查程序启动后报错的原因？
* 如何设置模块输入图像、参数和ROI区域？
* 如何通过图像源模块接口设置输入图像？
* 如何获取渲染图像的数据？
* 如何在渲染控件上自定义图形？
* 如何设置控件语言为英文？
* 如何通过流程输出或者模块输出获取数据结果？
* 如何通过绑定流程或模块获取渲染结果？
* 如何获取全局相机列表和设置相机参数？
* 全局模块控件中的通信管理如何接收和发送数据？
* 如何捕获控件操作过程中抛出的异常？
* 如何理解设置输入接口的“仅当次执行起效”逻辑？




<!-- ===== _xE7_xA8_x8B_xE5_xBA_x8F_xE5_x90_xAF_xE5_x8A_xA8_xE5_x90_x8E_xE6_x8A_xA5_xE9_x94_x99_xE7_x9A_x8439b445d04d97f919174b2dbcabb4a034.html | 常见问题 > 如何排查程序启动后报错的原因？ ===== -->

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




<!-- ===== _xE8_xAE_xBE_xE7_xBD_xAE_xE8_xBE_x93_xE5_x85_xA5_xE5_x9B_xBE_xE5_x83_x8F_xE3_x80_x81_xE5_x8F_x822a9f51fe6886ae7374f210fb286317fd.html | 常见问题 > 如何设置模块输入图像、参数和ROI区域？ ===== -->

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




<!-- ===== _xE9_x80_x9A_xE8_xBF_x87_xE6_x8E_xA5_xE5_x8F_xA3_xE8_xAE_xBE_xE7_xBD_xAE_xE5_x9B_xBE_xE5_x83_x8F5204ab1f40f549f822edefb7af534bf4.html | 常见问题 > 如何通过图像源模块接口设置输入图像？ ===== -->

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




<!-- ===== _xE8_x8E_xB7_xE5_x8F_x96_xE5_xB8_xA6_xE6_xB8_xB2_xE6_x9F_x93_xE7_x9A_x84_xE5_x9B_xBE_xE5_x83_x8F53eba15b49801911535d5ffd6d2d167e.html | 常见问题 > 如何获取渲染图像的数据？ ===== -->

<!-- src:_xE8_x8E_xB7_xE5_x8F_x96_xE5_xB8_xA6_xE6_xB8_xB2_xE6_x9F_x93_xE7_x9A_x84_xE5_x9B_xBE_xE5_x83_x8F53eba15b49801911535d5ffd6d2d167e.html -->
<!-- path:常见问题 > 如何获取渲染图像的数据？ -->
# 输出图像：获取带渲染的图像数据的方法

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**如何获取渲染图像的数据？

## 解决方法

1. 存图到本地。
   1. 在输出图像模块的【基本参数】中选择【像素格式】，可选RGB24或者MONO8。
   2. 通过【渲染设置】中的【前项存储设置】订阅相应模块数据，获取渲染结果。
   3. 开启【基本参数】中的【存图使能】，并在设置存图路径和文件命名。方案运行时，即可将渲染图保存到本地。
2. 获取渲染图像数据，可通过流程获取，也可通过模块输出。
   * 通过流程获取：通过流程的【输出设置】订阅输出图像模块，从而获取流程输出图像数据。可参考如何通过流程输出或者模块输出获取数据结果。
   * 通过模块输出：若【像素格式】为RGB24且【渲染设置】中的前项存储设置订阅响应模块数据，对输出图像模块进行实例化，即可获取带渲染的彩色图像数据；若【像素格式】为Mono8且【渲染设置】中的前项存储设置订阅响应模块数据，即可获取带渲染的灰度图像数据。相关代码如下。

     ```
     SaveImageTool saveImage=(SaveImageTool)VmSolution.Instance[“流程1.输出图像1”];    // 实例化输出图像模块
     Var saveImageResult=saveIamge.ModuResult.OutputImage;
     byte[] imageData= saveImageResult.ImageData;
     int imagePixelformat= saveImageResult.Pixelformat;                              // 17301505为MONO8灰度图，35127316为彩色图
     ```




<!-- ===== _xE6_xB8_xB2_xE6_x9F_x93_xE6_x8E_xA7_xE4_xBB_xB6_xE4_xB8_x8A_xE8_x87_xAA_xE5_xAE_x9A_xE4_xB9_x895df5f29af068b6e80592710abfcfcda2.html | 常见问题 > 如何在渲染控件上自定义图形？ ===== -->

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




<!-- ===== _xE6_x8E_xA7_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE4_xB8_xBA_xE8_x8B_xB1_xE6_x96_x87_xE7_x9A_x84_xE6_x96_xB9_xE6_xB3_x95.html | 常见问题 > 如何设置控件语言为英文？ ===== -->

<!-- src:_xE6_x8E_xA7_xE4_xBB_xB6_xE8_xAE_xBE_xE7_xBD_xAE_xE4_xB8_xBA_xE8_x8B_xB1_xE6_x96_x87_xE7_x9A_x84_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:常见问题 > 如何设置控件语言为英文？ -->
# 控件语言：控件设置为英文的方法

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**如何设置控件语言为英文？

## 解决方法

* 在VM4.0及VM4.1的二次开发中，控件语言设置的相关配置文件在debug路径下的LangCFG文件夹中，修改配置文件LanguageSet.cfg即可。
* 在VM4.2及VM4.3的二次开发中，因debug中未进行拷贝操作，修改配置文件的路径如下图所示。zh-cn表示中文，英文则修改为en-us。




<!-- ===== _xE9_x80_x9A_xE8_xBF_x87_xE6_xB5_x81_xE7_xA8_x8B_xE8_xBE_x93_xE5_x87_xBA_xE6_x88_x96_xE8_x80_x85f73babc98d494d79cf1981c0a0321c6d.html | 常见问题 > 如何通过流程输出或者模块输出获取数据结果？ ===== -->

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




<!-- ===== _xE9_x80_x9A_xE8_xBF_x87_xE7_xBB_x91_xE5_xAE_x9A_xE6_xB5_x81_xE7_xA8_x8B_xE6_x88_x96_xE6_xA8_xA1a402d64484deba2f1921afb46f0d4f2e.html | 常见问题 > 如何通过绑定流程或模块获取渲染结果？ ===== -->

<!-- src:_xE9_x80_x9A_xE8_xBF_x87_xE7_xBB_x91_xE5_xAE_x9A_xE6_xB5_x81_xE7_xA8_x8B_xE6_x88_x96_xE6_xA8_xA1a402d64484deba2f1921afb46f0d4f2e.html -->
<!-- path:常见问题 > 如何通过绑定流程或模块获取渲染结果？ -->
# 渲染结果：通过绑定流程或模块获取渲染结果的方法

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**如何通过绑定流程或模块获取渲染结果？

## 解决方法

渲染结果的显示可通过渲染控件绑定流程或模块的方式实现。推荐使用绑定流程的方式，更符合高内聚低耦合的思想，绑定流程可以实现单个渲染控件绑定多个算法模块渲染结果。

* 通过绑定流程显示渲染结果，一个渲染控件只能同时绑定一个流程。如需绑定多个流程，需要分时绑定或使用多个渲染控件。

  1. 完成流程配置中的显示设置，如下图所示。
  2. 通过如下代码绑定流程。

     ```
     VmProcedure VmProcess = (VmProcedure)VmSolution.Instance["流程1"];//实例化流程1
     vmRenderControl.ModuleSource=VmProcess;
     ```
* 通过绑定模块显示渲染结果，只能渲染某个模块的渲染结果。

  ```
  IMVSCircleFindModuCs.IMVSCircleFindModuTool circleTool=(IMVSCircleFindModuCs.IMVSCircleFindModuTool)VmSolution.Instance["流程1.圆查找1"];
  vmRenderControl.ModuleSource= circleTool;
  ```




<!-- ===== _xE8_x8E_xB7_xE5_x8F_x96_xE5_x85_xA8_xE5_xB1_x80_xE7_x9B_xB8_xE6_x9C_xBA_xE5_x88_x97_xE8_xA1_xA8b02deeb67251996558131b9bd4fcb156.html | 常见问题 > 如何获取全局相机列表和设置相机参数？ ===== -->

<!-- src:_xE8_x8E_xB7_xE5_x8F_x96_xE5_x85_xA8_xE5_xB1_x80_xE7_x9B_xB8_xE6_x9C_xBA_xE5_x88_x97_xE8_xA1_xA8b02deeb67251996558131b9bd4fcb156.html -->
<!-- path:常见问题 > 如何获取全局相机列表和设置相机参数？ -->
# 全局相机：获取全局相机列表和设置相机参数的方法

## 问题描述

**环境：**VM4.2及以上 + VS2013及以上
**问题：**如何获取方案中所有全局相机的连接状态，并设置全局相机的基本参数？例如：在流程运行时查看全局相机1和2的连接状态，并设置全局相机1的曝光和增益。

## 解决方法

1. **获取方案中所有全局相机的连接状态：**V4.2.1版本新增获取相机连接状态的API，通过调用 GlobalCameraTool 类中的 bIsCameraConnect( )可获取相机的连接状态。若需查看方案中所有全局相机模块的连接状态，可参考以下的代码。
   * 在程序初始化时，启动查看相机状态的线程：

     ```
     //获取流程中所有全局相机模块
     List<GlobalCameraModuleTool> glCameralist = new List<GlobalCameraModuleTool>();
     List<VmModule> vmModules = new List<VmModule>();
     VmSolution.Instance.GetAllModule(vmModules);
     foreach(VmModule module in vmModules)
     {
      if(module.GetType()==typeof(GlobalCameraModuleTool))
         {
             glCameralist.Add((GlobalCameraModuleTool)module);
         }
     }

     //启动全局相机连接状态监控线程
     Thread watchThread = new Thread(new ParameterizedThreadStart(CameraConnectionWatchDog));
     watchThread.IsBackground = true;
     watchThread.Start(glCameralist);
     ```
   * 查看相机连接状态的线程函数：

     ```
     public void CameraConnectionWatchDog(object obj)
     {
         List<GlobalCameraModuleTool> globalCameraToolList = (List<GlobalCameraModuleTool>)obj;
      bool[] isCameraConected = new bool[globalCameraToolList.Count];
      while (true)
         {
      try
             {
      //获取流程中所有已配置的连接状态
      foreach (var cameraTool in globalCameraToolList)
                 {
      if (cameraTool.bIsCameraConnect() == false)
                     {
                         MessageBox.Show(string.Format($"警告: {cameraTool.Name} 已经离线！"));
                     }
                 }
             }
      catch (VmException ex)
             {
                 MessageBox.Show("发生致命错误，错误码:" + ex.errorCode);
             }
             Thread.Sleep(2000);
         }
     }
     ```
2. **设置全局相机的参数：**通过调用 GlobalCameraParam 类的方法和属性设置。以设置全局相机1的曝光和增益为例，相关代码如下：

   ```
   GlobalCameraModuleTool cameraModuleTool = VmSolution.Instance["全局相机1"] as GlobalCameraModuleTool;
   GlobalCameraParam globalCameraParam = cameraModuleTool.ModuParams;
   globalCameraParam.ExposureTime = 5000;
   globalCameraParam.Gain = 5.0;
   ```

注意
:   全局相机使用时若没有添加引用的工具，需进行以下操作：

1. 手动添加 GlobalCameraModuleCs.dll 引用。
2. 将引用属性的“复制到本地”选项设置为False。
3. 在程序代码文件中添加命名空间的引用。

   ```
   using GlobalCameraModuleCsl;
   ```




<!-- ===== _xE6_x8E_xA5_xE6_x94_xB6_xE5_x92_x8C_xE5_x8F_x91_xE9_x80_x81_xE6_x95_xB0_xE6_x8D_xAE_xE7_x9A_x84_xE6_x96_xB9_xE6_xB3_x95.html | 常见问题 > 全局模块控件中的通信管理如何接收和发送数据？ ===== -->

<!-- src:_xE6_x8E_xA5_xE6_x94_xB6_xE5_x92_x8C_xE5_x8F_x91_xE9_x80_x81_xE6_x95_xB0_xE6_x8D_xAE_xE7_x9A_x84_xE6_x96_xB9_xE6_xB3_x95.html -->
<!-- path:常见问题 > 全局模块控件中的通信管理如何接收和发送数据？ -->
# 全局通信：接收和发送数据的方法

## 问题描述

**环境：**VM4.x + VS2013及以上
**问题：**二次开发中，全局模块控件中的通信管理如何接收和发送数据？

## 解决方法

* 通过 GetReadData() 接口接收数据，通过 SetInt() 或 SetString() 接口发送整型或字符串数据。代码如下：

  ```
  CommManagerModuleTool commTool = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];   //“通信管理1”是指当前运行的通信设备
  if(null !=null)
  {
      commTool.SetString(2, "abcd");                  //发送字符串型数据，接口函数SetString中的设备号2为通信管理中自动生成的设备序号
   int[] aIntVal = new int[3];
      aIntVal[0] = 10;
      aIntVal[1] = 11;
      aIntVal[2] = 12;
      commTool.SetInt(1, aIntVal, 0);                 //发送整型数据
   byte[] btData = null;
      commTool.GetReadData(2, ref btData);            //接收数据
  }
  ```
* 通过回调接收数据，代码如下：

  ```
  //添加HikExternalCall.dll引用，引用属性【复制到本地】改为false
  using HikExternalCall.Common;

  //注册回调函数，通讯接受事件回调
  VmSolution.OnCommunicationRecvCallBackEvent += VmSolution_OnCommunicationRecvCallBackEvent;
  private void VmSolution_OnCommunicationRecvCallBackEvent(ImvsSdkDefine.IMVS_COMMU_REPORT_DATA_INFO reportDataInfo)
  {
   string strMsg;
   try
      {
   int nType = reportDataInfo.nType;

   byte[] btarr = ExternalCallHelper.IntPtr2Bytes(reportDataInfo.pData, reportDataInfo.nLen);
   int len = btarr.Length;
   string ID = btarr[0].ToString();
   byte[] vs = new byte[len - 2];
          Array.Copy(btarr, 2, vs, 0, len - 2);
   string ReceiveData = System.Text.Encoding.Default.GetString(vs);    //数据
          strMsg = ID + "号设备接受到：" + ReceiveData;
      }
   catch (VmException ex)
      {
         strMsg = "读取通信数据失败. Error Code: " + Convert.ToString(ex.errorCode, 16);
      }
  }

  //发送字符串数据
  public void SendCommDeviceData(int Num, string SendMessage)
  {
      CommManagerModuleTool commManagerModule = (CommManagerModuleTool)VmSolution.Instance["通信管理1"];
   string strMsg;
   try
      {
   //获取通讯的连接状态
          if (commManagerModule.bIsDeviceConnect(Num))
          {
              commManagerModule.SetString(Num, SendMessage);              //给连接VM通讯的设备发送
              strMsg = "发送信号：" + SendMessage + "给" + Num + "号通讯设备";
          }
   else
          {
              strMsg = Num + "号通讯设备未打开";
          }
      }
   catch (Exception ex)
      {
          strMsg = "发送信号失败";
   return;
      }
  }
  ```




<!-- ===== _xE5_xA6_x82_xE4_xBD_x95_xE6_x8D_x95_xE8_x8E_xB7_xE6_x8E_xA7_xE4_xBB_xB6_xE6_x93_x8D_xE4_xBD_x9C9a57cb30f7a5b4a5798391b52c0a408c.html | 常见问题 > 如何捕获控件操作过程中抛出的异常？ ===== -->

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




<!-- ===== _xE5_xA6_x82_xE4_xBD_x95_xE7_x90_x86_xE8_xA7_xA3_xE8_xAE_xBE_xE7_xBD_xAE_xE8_xBE_x93_xE5_x85_xA51514c2f91c5396878be1b4a2582416b9.html | 常见问题 > 如何理解设置输入接口的“仅当次执行起效”逻辑？ ===== -->

<!-- src:_xE5_xA6_x82_xE4_xBD_x95_xE7_x90_x86_xE8_xA7_xA3_xE8_xAE_xBE_xE7_xBD_xAE_xE8_xBE_x93_xE5_x85_xA51514c2f91c5396878be1b4a2582416b9.html -->
<!-- path:常见问题 > 如何理解设置输入接口的“仅当次执行起效”逻辑？ -->
# 如何理解设置输入接口的“仅当次执行起效”逻辑？

## 问题描述

设置输入类型的接口（包括参数类的输入图像、ROI管理类的矩形/掩膜图像等接口）在配合流程执行接口或模块执行接口时，逻辑存在不一致的情况。

## 解决方法

设置输入接口的“仅当次执行起效”逻辑主要是针对流程执行。在调用设置输入接口后，对于如下两种情况，执行逻辑有所不同。

* 如果接着调用**流程执行接口**，流程使用设置数据执行一次并清空设置数据，下一次流程执行则按照流程配置执行；
* 如果接着调用**模块执行接口**，模块使用设置数据执行一次但不清空设置数据，下一次模块或流程执行则继续使用设置数据执行。




<!-- ===== _xE6_xB3_x95_xE5_xBE_x8B_xE5_xA3_xB0_xE6_x98_x8E.html | 法律声明 ===== -->

<!-- src:_xE6_xB3_x95_xE5_xBE_x8B_xE5_xA3_xB0_xE6_x98_x8E.html -->
<!-- path:法律声明 -->
# 法律声明

在法律允许的最大范围内，本文档是“按照现状”提供，可能存在瑕疵或错误。本公司不对本文档提供任何形式的明示或默示保证，包括但不限于适销性、质量满意度、适合特定目的、不侵犯第三方权利等保证；亦不对使用或是分发本文档导致的任何特殊、附带、偶然或间接的损害进行赔偿，包括但不限于商业利润损失、系统故障、数据或文档丢失产生的损失。
