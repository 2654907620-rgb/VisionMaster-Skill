<!-- source: 02-ch1-software-usage.md  pages 8-217 -->
# VM 软件使用 FAQ（第1章）

> 适用软件：海康机器人 VisionMaster（VM）4.0 系列为主，部分条目覆盖 VM3.X。
> 本章聚焦四类问题：环境配置（1.1）、工具使用（1.2）、全局模块（1.3）、通讯（1.4）。
> 所有代码块均按原文保留，路径、注册表项、DLL 名、API 名、版本号、阈值原样引用。

## 本章速览

- VM 启动/进程失败多为系统环境变量缺失：补 `C:\Windows\system32`、或补 `C:\Program Files (x86)\MVDAlgorithmSDK\Runtime\Win32`、`...Runtime\x64`。
- 模块加载报“找不到引用库”：VM3.X 缺 `.NET Framework 3.5`，VM4.0 需安装 `.NET Framework 4.6.1`。
- 显卡驱动与 VM 界面控件冲突会导致“图像后台切换但前端不变”，需回退显卡驱动到上一版本。
- 试用版限制：最多 2 流程、2 全局相机，移除 Modbus/PLC 通信、图像组合/四边形/多直线查找模块，无深度学习。
- 最大模块数默认 256，改 `VisionMaster.cfg` 与 `ServerConfiguration.ini` 中的“软件最大模块数”。
- 导出程序开机自启动需 `.bat`（ANSI 编码）+ 注册表 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`，因依赖 VM 服务先拉起。
- 循环模块本质是单组工具多次运行，靠 `LoopIndex` 循环标记做位置修正；循环输出须用脚本缓存，否则只拿到最后一次结果。
- 彩色图像几何查找失败：默认灰度转换（各通道取平均）会丢失信息，应先用“颜色转换”提取 B 通道再查找。
- 深度学习图像分割的缺陷面积：在分割模块后接 **BLOB 标签分析**模块获取。
- TCP 通讯无法直接发“数据点集合”，须用脚本将点集转字符串后再用“发送数据”模块订阅。
- 32 位寄存器解析按 ABCD / BADC / CDAB / DCBA 四种字节序；脚本中 `GetBytesValue` 取 byte 数组再重组。
- 多个不连续 ROI 检测：脚本用 `SetFloatValueByIndex` 一次性输出 X/Y/Height/Width/Rotation 点位。
- 脚本调试：导出工程 → VS“附加到进程” → 选 `ShellModuleManager` 进程（多脚本时按任务管理器“命令行”列区分脚本编号 0/1/4）。
- 全局触发 + 通讯接收事件实现“外部发 T1/T2 执行流程1/2”（仅与逻辑，多条件需多个事件）。
- 心跳功能：类型选“多数据”、间隔 1000ms，客户端收不到变化即判定通讯异常。
- 全局脚本 `UserGlobalMethods_OnReceiveCommunicateDataEvent` 可接收通讯数据，执行流程（`IMVS_PF_ExecuteOnce_V30_CS`）、加载本地图像、动态导入模板（换型）。
- VM4.0 全局脚本 `DeviceID` 改为每次分配唯一 ID，不再按设备列表顺序从 0 递增。
- Modbus TCP 目标端口固定 **502**；可发 Int 与 Float（Float 一般 ×1000 转 Int）；写寄存器注意大端/小端字节序与轮询使能。
- Group 嵌套循环渲染不显示：调大 `VisionMaster.cfg` 的“流程缓存队列丢弃阈值数量”（默认 128），原则 ≥ 循环次数 × Group 内模块数。
- 普通用户权限运行 VM4.0：需管理员安装维护版、改 `StartServerByExe=1`、授权 Users 完全控制，并视情况删 `AwakenGpuTool.exe`、关组策略 UAC 批准模式。

---

## 1.1 环境配置类

### 1.1.1 驱动配置：图像后台切换但前端界面不变的解决方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：图像源模块触发设置为自动切换，执行流程后图像后台实时切换，但前端界面图像不变，始终只显示同一张图像。

**原因 / 原理**
- 电脑显卡驱动程序与 VM 界面控件冲突。

**解决步骤**
1. 右键“此电脑”→ 管理 → 设备管理器 → 显示适配器。
2. 选中显示适配器并右键“属性”，查看当前显卡驱动程序版本。
3. 点击“回退驱动程序”，选择上一版本；成功回退后驱动版本变化。
4. 打开 VM 运行流程，界面图像即可自动切换。

**注意事项 / 坑**
- 该问题为显卡驱动与 VM 控件冲突，回退驱动是官方推荐做法。

### 1.1.2 驱动缺失：格式化工具打开后消失的解决方法
**问题现象 / 适用场景**
- 环境：VM3.XX、VM4.0.0
- 现象：拖拽出格式化模块后，格式化模块变灰色，直接消失。

**原因 / 原理**
- 缺少 .Net Framework 库。VM3.XX 依赖 3.5，VM4.0 依赖 4.6。

**解决步骤**
- VM3.X：安装 `.NET Framework 3.5`。
- VM4.0：直接安装 `.NET Framework 4.6.1` 即可，目录与 3.XX 一致。

### 1.1.3 环境配置：VM 试用版本激活报错的解决方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：激活时报“更新失败：应用程序与本地 LM 通讯出错”。

**解决步骤**
1. 进入 `VisionMaster4.0.0\Applications\EncRuntime`，运行 `haspdinst_33582.exe`，按弹框提示完成安装。
2. 安装完成弹框点 OK。
3. 再运行 `VM_6600_S_V400_Unlock30d.exe` 即可成功激活。

**关键路径 / 文件**
- `VisionMaster4.0.0\Applications\EncRuntime\haspdinst_33582.exe`
- `VM_6600_S_V400_Unlock30d.exe`

**注意事项 / 坑（试用版软件端限制）**
1. 最多只支持 2 个流程。
2. 最大只支持建 2 个全局相机。
3. 通信管理移除 Modbus 和 PLC 功能。
4. 去除图像组合模块。
5. 去除四边形查找模块。
6. 去除多直线查找模块。
7. 不支持深度学习功能。

### 1.1.4 模块数限制：修改 VM 最大模块数量
**问题现象 / 适用场景**
- 环境：VM3.3.1、VM3.4.0
- 现象：VM 默认最大模块数量为 256，方案模块数量超过限制。

**解决步骤**
- 3.3.1 及 4.0.0 版本：
  1. 在 `VisionMaster3.3.1\Applications` 中找到 `VisionMaster.cfg`。
  2. 在 `VisionMaster3.3.1\Applications\Server` 中找到 `ServerConfiguration.ini`。
  3. 在这两个文件中找到“软件最大模块数”，修改为需要的值。
- 3.4.0 版本：
  1. 在 `Applications\Server` 中找到 `ServerConfiguration.ini`。
  2. 找到“软件最大模块数”，修改为需要的值。

**关键文件 / 配置项**
- `VisionMaster.cfg`（Applications 目录）
- `ServerConfiguration.ini`（Applications\Server 目录）
- 配置项：“软件最大模块数”

### 1.1.5 开机自启动：VM 运行界面导出物开机运行的设置方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：VM 运行界面导出的程序注册 Windows 开机自启动后，开机时程序启动异常报错。

**原因 / 原理**
- 程序的执行依赖 VM 相关服务，自启动时相关服务未拉起造成启动失败。

**解决步骤**
1. 创建脚本：新建一个 `.bat` 文件，输入以下格式代码：
   ```
   start /d "C:\Users\xxx\Desktop\导出程序\daochu\Public_Release" daochu.exe
   ```
   引号内为导出程序所在路径，引号后接 `空格 + 导出程序 exe 的带后缀名称`。**必须以 ANSI 格式编码**，否则中文乱码（可用 Notepad++ 转换编码）。
2. 注册脚本：Win+R 输入 `regedit`，打开目录
   `\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
   右键 → 新建 → 字符串值，自定义名称后双击，输入 `.bat` 脚本的文件路径，确定。
3. 验证：Win10 打开任务管理器→启动页查看；Win7 用 `msconfig`→启动页查看。开机后自动调用脚本拉起导出程序。

**关键 API / 参数 / 路径 / 注册表项**
- 注册表：`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`
- 示例路径：`C:\Users\xxx\Desktop\导出程序\daochu\Public_Release\daochu.exe`

**注意事项 / 坑**
- `.bat` 必须用 ANSI 编码，否则中文路径乱码导致启动失败。

### 1.1.6 锁定模式：开启锁定模式提示信息的方法
**问题现象 / 适用场景**
- 环境：VM3.4.0、VM4.0.0
- 现象：VM 方案每次加载都提示是否开启锁定模式，或自动锁定。

**解决步骤**
- VisionMaster4.x 版本：在 `VisionMaster4.0.0\Applications\VisionMaster.cfg` 中修改：
  - `NumOfDefLockModeModulesCount`（默认开启锁定模式模块数量）
  - `PromptNumOfLockModeModulesCount`（提示开启锁定模式模块数量）
  使之大于方案模块数量。
- VisionMaster3.x 版本：在 `VisionMaster3.4.0\Applications\VisionMaster.cfg` 中修改：
  - “默认开启锁定模式模块数量”
  - “提示开启锁定模式模块数量”
  使之大于方案参数。

**关键配置项**
- `NumOfDefLockModeModulesCount`
- `PromptNumOfLockModeModulesCount`

### 1.1.7 环境配置：格式化模块报错解决方法
**问题现象 / 适用场景**
- 环境：VisionMaster3.2，Windows10
- 现象：在拉取模块工具中拖出格式化、变量计算等模块时报错“找不到引用库”。

**原因 / 原理**
- 未安装 .NET Framework 3.5。

**解决步骤**
1. 下载 .NET Framework 3.5 SP1 脱机安装程序：`https://dotnet.microsoft.com/download/dotnet-framework/net35-sp1`。
2. 安装 .NET Framework 3.5（弹出配置对话框选“安装此功能”，需联网）。
3. 若遇到错误 `0x800f0906`、`0x800f0907`、`0x800f081f` 或 `0x800F0922`，参考：
   `https://docs.microsoft.com/zh-CN/troubleshoot/windows-client/application-management/dotnet-framework-35-installation-error`

### 1.1.8 环境配置：VM3.4 启动失败解决办法
**问题现象 / 适用场景**
- 环境：VM3.4
- 现象：VM3.4 启动弹窗“启动失败”。

**原因 / 原理**
- 系统环境变量缺失。

**解决步骤**
- 环境变量 `Path` 添加：`C:\Windows\system32`

### 1.1.9 环境配置：VM 进程启动失败解决办法
**问题现象 / 适用场景**
- 环境：VM4.0
- 现象：VM4.0 启动弹窗“进程启动失败”。

**原因 / 原理**
- 系统环境变量缺失。

**解决步骤**
- 环境变量 `Path` 添加：
  - `C:\Program Files (x86)\MVDAlgorithmSDK\Runtime\Win32`
  - `C:\Program Files (x86)\MVDAlgorithmSDK\Runtime\x64`

**关键路径 / 配置项**
- `C:\Program Files (x86)\MVDAlgorithmSDK\Runtime\Win32`
- `C:\Program Files (x86)\MVDAlgorithmSDK\Runtime\x64`

### 1.1.10 内存管理：开启虚拟内存的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：使用内存需求较大的应用，物理内存不能满足需求。

**解决步骤**
1. 打开电脑“属性”→“高级系统设置”。
2. 选择“高级”选项卡。
3. 点击“性能”下方的“设置”按钮。
4. 进入“高级”界面，点击虚拟内存下面的“更改”。
5. 在虚拟内存设置界面点击“自定义”，设置合适大小。

**注意事项 / 坑**
- 开启虚拟内存可弥补物理内存不足，加快程序运行。

### 1.1.11 运行间隔：设置流程运行间隔的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何有效设置流程运行间隔。

**原因 / 原理**
- 流程运行间隔 = 流程执行完后间隔多久再次执行。0ms 表示执行完立刻执行下一次；1000ms 表示等待 1s 再执行。
- 间隔适当增大，流程耗时更稳定、多个流程执行次数才会相同；否则耗时波动变大、多流程执行次数不同。多流程连续运行场景更明显。

**示例**
- 一个方案四个同样的流程，单流程运行约 200ms：
  - 间隔 10ms：连续运行时各流程执行次数差异大、波动大。
  - 间隔 600ms：各流程执行次数一致、耗时稳定。

### 1.1.12 静默执行：禁止 VM 静默执行的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何禁止 VM 加载方案后的静默执行。

**解决步骤**
1. 在 `\VisionMaster4.0.0\Applications\VisionMaster.cfg` 中将控制是否静默执行的参数修改为 `0`。
2. 在 `\VisionMaster4.0.0\Applications\VisionMaster.exe.Config` 中将控制是否静默执行的参数设置为 `0`。

**关键文件**
- `VisionMaster4.0.0\Applications\VisionMaster.cfg`
- `VisionMaster4.0.0\Applications\VisionMaster.exe.Config`

### 1.1.13 用户权限：普通用户权限使用 VM 的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：普通用户权限下启动 VM400，报错 `E0000109 消息格式错误`。

**解决步骤**
1. 管理员权限下安装 VM4.0 维护 20220415 安装包（截止 20220505 最新补丁为 20220505，建议打最新补丁；2022 年 5 月之后有完整包可直接用）。
2. 修改 `VisionMaster.cfg` 和 `VisionMaster.exe.cfg`，将 `StartServerByExe` 节点 `Value` 改为 `1`，路径 `..\VisionMaster4.0.0\Applications`。
3. 管理员权限在 `..\VisionMaster4.0.0\Applications\Server` 下运行 `ServerUninstall.bat`。
4. 管理员权限手动杀掉所有 VM 相关进程：`VisionMaster.exe`、`VisionMasterServerApp.exe`。
5. 管理员权限在 VM 安装路径配置普通用户（如 Users 用户）的“完全控制”权限（不配可能导致加载资源失败）。
6. 管理员权限关闭防火墙和杀毒软件（不配有时软件打不开）。
7. （非必要）有的电脑会报 `cudart64_110.dll` 丢失，需删除 `AwakenGpuTool.exe`；如不发生此报错无需删除。该工具用于深度学习模块，不影响 2D 算法模块；需使用深度学习模块则不要执行此步。
8. （非必要）有的电脑打开 VM 提示需输入管理员密码，需在管理员账户下改组策略：搜索 `gpedit.msc` → 计算机配置 → Windows 设置 → 安全设置 → 本地策略 → 安全选项 → “用户帐户控制：以管理员批准模式运行所有管理员”改为“已禁用”。

**关键文件 / 配置项**
- `VisionMaster.cfg` / `VisionMaster.exe.cfg`：`StartServerByExe` = 1
- `..\VisionMaster4.0.0\Applications\Server\ServerUninstall.bat`
- 进程：`VisionMaster.exe`、`VisionMasterServerApp.exe`
- DLL：`cudart64_110.dll`、`AwakenGpuTool.exe`
- 组策略项：`用户帐户控制：以管理员批准模式运行所有管理员`

### 1.1.14 图标隐藏：电脑右下角 VM 图标不显示的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上
- 现象：VM SDK 开发时，右下角 VM 图标是否可以隐藏。

**解决步骤**
- 打开 `VisionMaster4.0.0\Applications\Tools` 下的工具 `VM.CustomHelper.exe`，运行后取消“显示托盘图标”前面的勾。

**关键路径 / 文件**
- `VisionMaster4.0.0\Applications\Tools\VM.CustomHelper.exe`

---

## 1.2 工具类

### 1.2.1 文本保存：逐行保存格式化模块输出的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 以上
- 现象：文本保存模块无法逐行获取格式化模块输出，只能订阅整个结果，不能通过分隔符按行分割单独获取某一行。

**解决步骤**
- 使用“协议解析”模块根据分隔符获取格式化模块每行数据，再用“文本保存”模块订阅协议解析模块的输出。

**注意事项 / 坑**
- 需多个模块配合使用（格式化 → 协议解析 → 文本保存）。

### 1.2.2 脚本模块：循环模块搭配脚本使用的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：使用 VM 模块搭配脚本模块，如何实现获取所有数据一次性全部输出（如每个试剂盒试纸检测，一次性输出四个结果）。

**原因 / 原理**
- 循环模块本质是单组工具多次运行，与编程 for/while 性质一样，按前置输入循环次数执行。VM 引入循环标记 `LoopIndex`，循环内模块可订阅该值实现位置修正。
- 位置关系两种输入：①继承（直接继承前序定位模块检测区域）；②通过位置修正（将位置修正作为循环内首模块，在位置修正信息内配置循环标记引导后续模块相对修正）。
- VM 机制是“执行一次输出一次”的顺序结构；用格式化模块只能拿到循环内最后一次结果，需用脚本缓存每次结果，达循环次数时汇总输出。

**关键代码（C#）**
```csharp
using System;
using System.Text;
using System.Windows.Forms;
using Hik.Script.Methods;
class UserScript:ScriptMethods,IProcessMethods
{
    int processCount ;
    int var0,var1;
    int[] num=new System.Int32[5];
    /// <summary>
    /// 预编译时变量初始化
    /// </summary>
    public void Init()
    {
        processCount = 0;
    }
    public bool Process()
    {
        //每次执行将进入该函数，此处添加所需的逻辑流程处理
       // MessageBox.Show("Process Success");
        GetIntValue("var0",ref var0);
        GetIntValue("var1",ref var1);
        num[processCount]=var1;
        processCount++;
        if(processCount==var0)
        {
            for(int i=0;i<var0;i++)
            {
                SetIntValueByIndex("EveryStatus",num[i],i,var0);
            }
            SetIntValue("InspeNum",processCount);
            Array.Clear(num,0,num.Length);
            processCount=0;
        }
        return true;
    }
}
```

**关键 API / 参数**
- 循环标记：`LoopIndex`
- 脚本接口：`GetIntValue`、`SetIntValueByIndex`、`SetIntValue`、`Array.Clear`

**注意事项 / 坑**
1. 方案设计需权衡配置与性能，重点看流程时间是否满足现场需求，再决定是否采用循环。
2. 脚本内需做数据次数缓存、次数判断和数据清理；若仅获取点坐标可用“点集工具”开启循环使能实现。
3. 位置修正：①先保证前序定位模块仅匹配到一个工件；②基于该工件建立位置修正；③基于位置修正调整后续工具相对 ROI；④确保单组工具检测正常后，再将前序定位模块数量设为理想数量，单击运行查看整体效果。

### 1.2.3 几何查找：彩色图像的几何查找方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何对彩色图像进行几何查找（圆查找、直线查找等），如查找隔膜边缘直线，直接直线查找定位失败。

**原因 / 原理**
- 算法处理灰度图，图像源对彩色图转灰度默认“各通道取平均值”，该转换下隔膜下边缘灰度及纹理信息与背景几乎相同，导致查找失败。

**解决步骤**
1. 使用“颜色转换”工具将彩色图像通道分离（本案例提取 RGB 中的 B 通道）。
2. 对转换得到的 B 通道灰度图像使用“直线查找”工具，定位成功。

**注意事项 / 坑**
- 不熟悉 VM 对彩色图转灰度图的转换方法会导致几何查找失败。

### 1.2.4 深度学习：图像分割的面积的获取方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：利用深度学习图像分割获取的缺陷面积尺寸如何获取。

**解决步骤**
- 在“图像分割”模块后面接“BLOB 标签分析”模块。

**注意事项 / 坑**
- 需熟悉 VM 相关工具的组合使用。

### 1.2.5 颜色识别：使用颜色识别工具做分类检测的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何使用颜色识别工具做极耳阳极/阴极的分类检测。

**解决步骤**
1. 图像源模块基本参数中，像素格式选择 `RGB24`。
2. 颜色识别模块创建模型，图像列表加载当前彩色图像，截取图像样本并添加至标签。
3. 待检测区域绘制 ROI，运行颜色识别模块，输出参数“最佳匹配名称”为分类结果。

**关键参数**
- 像素格式：`RGB24`
- 输出参数：“最佳匹配名称”（极耳阳极→铜；极耳阴极→铁）

### 1.2.6 数据分析：使用脚本模块解析 32 位寄存器数据的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上
- 现象：接收数据模块接收的数据是 16 进制 byte 数组，无法获取 10 进制数据，需再次解析。

**关键代码（C#）**
```csharp
public bool Process()
{
    int datatype=4;//数据格式，ABCD、CDAB、BADC、DCBA 四种
    byte[] _registervalue = new System.Byte[1];//初始化字节数组，GetBytesValue函数中会根据实际情况再初始化字节长度。
    GetBytesValue("recdata",ref _registervalue);//获取数据
    string hexdata=string.Empty;
    int[] registervalue = new System.Int32[_registervalue.Length /2];//数据列表，结果是32位的数据

    for(int j=0;j<_registervalue.Length;j=j+4 )
    {
        if(datatype==1) //ABCD
            hexdata=string.Format("{0:x2}", Convert.ToInt32(_registervalue[j])) //A
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+1])) //B
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+2])) //C
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+3])); //D
        else if(datatype==2) //BADC
            hexdata=string.Format("{0:x2}",Convert.ToInt32(_registervalue[j+1])) //B
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j])) //A
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+3])) //D
            + string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+2])); //C
        else if(datatype==3)//CDAB
            hexdata =string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+2])) //C
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+3])) //D
            +  string.Format("{0:x2}", Convert.ToInt32(_registervalue[j])) //A
            + string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+1])); //B
        else //DCBA
            hexdata=string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+3])) //C
            + string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+2])) //D
            + string.Format("{0:x2}", Convert.ToInt32(_registervalue[j+1])) //A
            + string.Format("{0:x2}", Convert.ToInt32(_registervalue[j])); //B

        registervalue[j/4] =  Convert.ToInt32(hexdata, 16); //16进制字符串转为10进制整形
    }

    for(int i=0;i<registervalue.Length;i++)//将32位寄存器数据设置到脚本输出变量
    {
        SetIntValueByIndex("out0",registervalue[i],i,registervalue.Length);
    }
    return true;
}
```

**关键 API / 参数**
- `datatype`：1=ABCD，2=BADC，3=CDAB，4=DCBA
- 接口：`GetBytesValue("recdata",...)`、`SetIntValueByIndex("out0",...)`
- 每 4 字节组为一个 32 位数据；`hexdata` 为 16 进制串，转 10 进制整形。

**注意事项 / 坑**
- 不熟悉 32 位寄存器数据解析方法时易出错，务必按 PLC/设备字节序选对 datatype。

### 1.2.7 定位功能：使用位置修正模块实现 ROI 自动修正
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：粗定位的实现方法。

**解决步骤**
- 使用“位置修正”模块，订阅前项任意具有定位识别功能的模块输出的目标点，对后置模块中的 ROI 进行自动修正（订阅前项匹配点、订阅位置修正信息）。

**注意事项 / 坑**
- 功能不熟悉会导致 ROI 无法跟随定位结果修正。

### 1.2.8 读码功能：设置读码参数方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：读码模块使用介绍。

**解决步骤**
- 不同 DM 码以及 QR 码尺寸不一样，需设置合适的“降采样倍数”和“码宽”参数。默认一般无法读到码内容，需调节降采样倍数及码宽。
- 设置读码宽度：根据码的实际宽度设定范围。

**注意事项 / 坑**
- 功能不熟悉时直接读码会失败，必须先调降采样倍数和码宽。

### 1.2.9 图像采集：运行 VP 后 VM 流程中相机取图失败的解决方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：运行 VisionPro 后，再运行 VM 触发流程，第一次触发能正常取图，再次触发后流程卡死，最后超时报取图失败。

**原因 / 原理**
- VisionPro 会把相机设置为单帧模式，而 VM 暂时不支持单帧模式。

**解决步骤**
- 用 MVS 将相机采集模式设为“连续模式”。

**注意事项 / 坑**
- VisionPro 修改了相机采图模式，需手动在 MVS 切回连续模式。

### 1.2.10 多图融合：使用多图融合工具实现光度立体法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何使用多图融合工具实现光度立体法。

**解决步骤**
1. 将通过相机和光源拍摄的多张不同角度不同亮度的图像放到同一个文件夹中。
2. 将“多图采集”模块拖到流程编辑区，双击配置参数，导入文件夹；取图数量为 3-8（与拍摄图像的角度和亮度的数目有关）；**分布角**为光源与正方向的夹角，**照射角**为光源中线与相机中线的夹角。
3. 将“多图融合”模块拖到流程编辑区，设定相应参数，得到合成后的图像。

**关键参数**
- 取图数量：3-8
- 分布角：光源与正方向夹角
- 照射角：光源中线与相机中线夹角

### 1.2.11 仿射变换：使用仿射变换进行抠图的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何使用仿射变换进行抠图。

**解决步骤**
1. 拖动图像源模块到流程编辑区，添加本地图像。
2. 拖动仿射变换模块到流程编辑区，创建希望抠图的 ROI，设置运行参数，其中**尺度**和**宽高比**均设置为 `1`，执行后可得抠出的图像。

**关键参数**
- 尺度 = 1
- 宽高比 = 1

### 1.2.12 中线测量：测量中线之间距离的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何测量物体中线之间的距离。

**解决步骤**
1. 使用“四边形查找”模块以及“平行线查找”模块查找与中心线相关的边缘。
2. 使用“线线测量”模块进行中线距离测量，在线输入中订阅四边形查找的中点线和平行线查找的边缘中线，输出中线之间的距离。

**注意事项 / 坑**
- 不熟悉四边形查找及平行线查找工具的输出参数会导致订阅错误。

### 1.2.13 图像增强：使用图像增强工具凸显目标方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何使用图像增强工具凸显目标，改善视觉效果（如电池底部脏污检测，底部粗糙成像差，直接 blob 分析达不到好效果）。

**解决步骤**
1. 设置图像增强的相关参数。
2. 显示增强结果。

**注意事项 / 坑**
- 不熟悉图像增强工具的使用会导致效果不好。

### 1.2.14 字符串显示：使用脚本显示字符串的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何使用脚本在图像显示窗口显示自定义的字符串。

**解决步骤**
1. 在脚本模块中设置输入变量和想要的输出变量。
2. 编写脚本逻辑。
3. 输出显示结果。

**关键代码（C#）**
```csharp
public bool Process()
{
    GetFloatValue("isShield", ref isShield);
    GetStringValue("isPop", ref isPop);
    if(isShield > 10000)
    {
        shieldInfo = "中心孔被遮挡";
    }
    else
    {
        shieldInfo = "中心孔未被遮挡";
    }
    if(isPop == "OK")
    {
        PopInfo = "隔膜正常";
    }
    else if(isPop == "NG")
    {
        PopInfo = "隔膜弹起";
    }
    string resultInfo = shieldInfo + "," + PopInfo;
    SetStringValue("resultInfo", resultInfo);
    return true;
}
```

**关键 API / 参数**
- 输入：`isShield`(float)、`isPop`(string)
- 输出：`shieldInfo`、`PopInfo`、`resultInfo`(string)
- 接口：`GetFloatValue`、`GetStringValue`、`SetStringValue`

### 1.2.15 路径提取：使用 VM 路径提取工具查找边缘点的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何使用 VisionMaster 软件的路径提取工具查找边缘点。

**解决步骤**
1. 在工具栏中拖入“路径提取”工具，“运行参数”中的“提取方式”选择“查找边缘点”。
2. 然后在“模板匹配”中创建大致轨迹和训练参数（阈值、卡尺、路径点数量等）。
3. 点击完成后执行，即可查询边缘点。

**关键参数**
- 提取方式：查找边缘点
- 训练参数：阈值、卡尺、路径点数量

### 1.2.16 标定板生成：使用 VM 自研标定板 Demo 生产标定板的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何使用 VisionMaster 软件的自研标定板 Demo 生成标定板。

**解决步骤**
1. 在 VisionMaster 软件“工具”中打开“标定板生成工具”，或在安装目录
   `VisionMaster\VisionMaster4.0.0\Applications\Tools\自研标定板生成Demo`
   下打开 `DemoGenCalBoard_ch.exe`。
2. 根据提示进行标定板文件生成步骤。
3. 按任意键退出，标定文件生成在
   `VisionMaster\VisionMaster4.0.0\Applications\Tools\自研标定板生成Demo` 下查看。

**关键路径 / 文件**
- `VisionMaster\VisionMaster4.0.0\Applications\Tools\自研标定板生成Demo\DemoGenCalBoard_ch.exe`

### 1.2.17 脚本模块：编写脚本处理点集合的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何对数据点集合通过脚本模块进行处理并输出结果。

**解决步骤**
1. 首先在脚本里手动添加输入、输出变量（定义变量名、数据类型以及订阅来源）。
2. 脚本代码中首先必须实例化数组用来获取点集合。
3. 在 `Process()` 中编写输入变量、处理过程、输出变量等操作；4.0 版本输出点集合只支持通过 Index 输出结果。

**关键代码（C#）— 定义数组**
```csharp
class UserScript:ScriptMethods,IProcessMethods
{
    //先定义存放坐标数组,数量大于输入点个数，这里假设512个
    float[] X = new float[512];
    float[] Y = new float[512];
    float[] X1 = new float[512];
    float[] Y1 = new float[512];
    ...
}
```

**关键代码（C#）— Process()**
```csharp
/// <summary>
/// Enter the process function when running code once
/// 流程执行一次进入Process 函数
/// </summary>
/// <returns></returns>
public bool Process()
{
    //获得输入变量numX、numY
    int lenX = 0;
    int lenY = 0;
    GetFloatArrayValue("inx",ref X,out lenX);
    GetFloatArrayValue("iny",ref Y,out lenY);

    ///处理方法放在这里
    ///...

    //通过Index输出变量outx、outy
    for(int i = 0; i < lenX;i++)
    {
        SetFloatValueByIndex("outx",X1[i],i,lenX);
        SetFloatValueByIndex("outy",Y1[i],i,lenY);
    }
    return true;
}
```

**关键 API / 参数**
- 接口：`GetFloatArrayValue("inx"/"iny",...)`、`SetFloatValueByIndex("outx"/"outy",...)`
- 输出点集合只支持通过 Index 输出。

### 1.2.18 脚本模块：添加自定义程序集的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何在脚本模块中添加自定义的程序集。

**解决步骤**
1. 打开一个脚本模块，找到“编辑程序集”。
2. 引用程序集中点击“添加”，找到自定义的程序集。
3. 在脚本中引用添加的程序集，调用其中的接口函数。

**关键代码（C#）**
```csharp
using MathNet.Numerics;//引用程序集
```

### 1.2.19 N 点标定：模块 N 点标定的使用方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何使用 N 点标定模块。

**解决步骤**
- N 点标定常用九点标定和十二点标定（如九点标定：获取 9 组像素点及对应 9 组物理点，生成标定文件）。
1. 当图像源为本地图片（九张）时，首先获取一个像素点来标记运动轨迹（如边缘交点）；然后 N 点标定模块参数配置，注意**平移次数、物理坐标系参数以及自由度**的配置。
2. 执行九次，图片自动切换，形成九点标定的运动轨迹；N 点标定模块可查看相应标定点，也可导出/导入。

**关键参数**
- 平移次数、物理坐标系参数、自由度
- 标定文件可导出/导入

### 1.2.20 字符识别：使用字符识别模块训练的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：使用字符识别模块时，不知道是否需要训练及如何训练。

**解决步骤**
1. 字符识别模块使用需要进行训练，训练得到字符库可保存到本地，下次直接导入。
2. 打开字库训练窗口，先选择 ROI 区域，然后提取字符，接着训练字符，最后添加至字符库。

**注意事项 / 坑**
- 不熟悉字符识别模块使用时会漏掉训练步骤。

### 1.2.21 渲染保存：将多个模块的渲染结果在原彩色图片中保存的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何将多个模块的结果同时渲染在原彩色图像中保存。

**解决步骤**
1. 图像源模块，更改图像素格式为 `RGB24`。
2. 处理模块输入源改为灰度图像数据。
3. 使用“输出图像源”模块保存图像，并绑定输入图像源和需要渲染的处理模块。
4. 保存结果。

**关键参数**
- 图像素格式：`RGB24`
- 保存模块：输出图像源模块（绑定输入图像源 + 需渲染的处理模块）

### 1.2.22 分支字符：使用分支字符调试不同分支的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：如何对分支字符下的不同分支进行调试。

**解决步骤**
1. 拖拽分支字符模块到流程区，设置不同分支的字符。
2. 打开想要调试的分支的调试按钮，即可进行调试。

**注意事项 / 坑**
- 不熟悉分支字符工具的使用。

### 1.2.23 调试脚本：对脚本进行调试的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上
- 现象：如何对 VM 脚本模块中的代码进行调试。

**解决步骤**
1. 在脚本模块中使用“导出工程”功能，将代码导出。
2. 找到导出的工程并打开。
3. 生成解决方案，设置断点，点击 VS 菜单“调试”中的“附加到进程”，选择 `ShellModuleManager` 进程，点击附加。
4. 在 VM 中点击执行，自动进入 VS 开始调试。

**多脚本区分（脚本编号 0/1/4）**
- 若方案有多个脚本，在任务管理器找到 `ShellModule` 进程（不知对应哪个脚本）。
- 右键 → “转到详细信息”。
- 将鼠标放在第一行右键 → “选择列”，勾选“命令行”。
- 查看脚本编号对应的进程号，附加时选择对应进程。

**关键进程**
- `ShellModuleManager`（每个脚本对应一个）

### 1.2.24 区域设置：多个不连续 ROI 同时检测的使用方法
**问题现象 / 适用场景**
- 环境：VM4.0.0 + VS2015 及以上
- 现象：VM 中 Blob、模板匹配等工具查找区域不连续、重复性强，希望用脚本工具一次性设置，减少工作量。

**解决步骤**
1. 在工具中加入“脚本”工具，将输出端链接在需要使用 ROI 的工具上。
2. 打开脚本工具，添加 5 个 float 输出端，输入端按需要添加。
3. 关键算子使用、配置 ROI。
4. 编写代码详细输出各 ROI 的 X/Y/Height/Width/Rotation。

**关键代码（C#）**
```csharp
public bool Process()
{
    //以float类型在输出端"X"的第一位输入200
    SetFloatValueByIndex("X",200,0,2);
    //以float类型在输出端"X"的第二位输入500
    SetFloatValueByIndex("X",500,1,2);
    //以float类型在输出端"Y"的第一位输入200
    SetFloatValueByIndex("Y",200,0,2);
    //以float类型在输出端"Y"的第二位输入500
    SetFloatValueByIndex("Y",500,1,2);
    //以float类型在输出端"Height"的第一位输入200
    SetFloatValueByIndex("Height",200,0,2);
    //以float类型在输出端"Height"的第二位输入300
    SetFloatValueByIndex("Height",300,1,2);
    //以float类型在输出端"Width"的第一位输入200
    SetFloatValueByIndex("Width",200,0,2);
    //以float类型在输出端"Width"的第二位输入300
    SetFloatValueByIndex("Width",300,1,2);
    //以float类型在输出端"Rotation"的第一位输入0
    SetFloatValueByIndex("Rotation",0,0,2);
    //以float类型在输出端"Rotation"的第二位输入0
    SetFloatValueByIndex("Rotation",0,1,2);
    return true;
}
```

**关键 API / 参数**
- 接口：`SetFloatValueByIndex("X"/"Y"/"Height"/"Width"/"Rotation", 值, 索引, 总数)`
- 末位参数 `2` 表示每组 2 个元素。

### 1.2.25 通讯模块：通讯模块发送数据点集合的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：发送数据模块中，TCP 通讯直接订阅数据点集合只能发送第一组数据，无法将集合都发送。

**原因 / 原理**
- TCP 通讯无法发送数据点集合，需要将点集合通过脚本转换为字符串形式，再用“发送数据”模块订阅传输。

**解决步骤**
1. 在脚本中订阅输入变量及输出变量。
2. 编写脚本代码进行格式转换（点集 → 以 `,` 间隔的字符串）。
3. 发送数据模块订阅转换后的字符串变量。

**关键代码（C#）**
```csharp
//获得输入变量numX、numY
int lenX = 0;
int lenY = 0;
GetFloatArrayValue("numX",ref X,out lenX);
GetFloatArrayValue("numY",ref Y,out lenY);
//将格式转换为字符串，间隔符为","
string Str = "";
for(int i = 0; i < lenX;i++)
{
    Str += X[i].ToString("f3")+",";
}
string Str1 = "";
for(int i = 0; i < lenY;i++)
{
    Str1 += Y [i].ToString("f3")+",";
}
//结果输出
SetStringValue("strX",Str);
SetStringValue("strY",Str1);
```

**关键 API / 参数**
- 输入：`numX`、`numY`（float 数组）
- 输出：`strX`、`strY`（string）
- 接口：`GetFloatArrayValue`、`SetStringValue`
- 间隔符：`,`

### 1.2.26 模板保存：导入及导出匹配模板的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何将本次模板匹配所创建的模板进行导出，以便下次使用。

**解决步骤**
1. 点击高精度匹配模块，创建模板。
2. 编辑模板，点击“导出”按钮，选择保存路径和命名。
3. 点击“载入”按钮，载入之前保存的模板。

**注意事项 / 坑**
- 不熟悉高精度匹配模块使用时会找不到导出/载入入口。

### 1.2.27 标定片标定：使用标定板标定激光振镜的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何使用标定板标定激光振镜。

**解决步骤**
- 首先使用激光在平面上打一个十字并指明坐标系方向（十字中心为坐标系原点），然后选择一个透明标定片将十字线与标定片任意直角对齐，最后调整运行参数中的原点坐标与标定片坐标系方向并选择物理尺寸，使标定片坐标系与十字线坐标系重合并生成标定文件。

### 1.2.28 Group 显示：Group 嵌套循环使能渲染显示的方法
**问题现象 / 适用场景**
- 环境：VM3.4.0
- 现象：方案流程中使用多个 Group 模块嵌套，并启用“循环使能”，执行流程时 Group 模块图像源和图形源都不能正常显示。

**原因 / 原理**
- Group 循环超出了配置的缓存数量，需要调大缓存。

**解决步骤**
1. 打开 Vm3.4.0 安装目录下的 `VisionMaster.cfg` 文件。
2. 修改“流程缓存队列丢弃阈值数量”，默认 `128`。修改原则：**缓存数量 ≥ 循环次数 × Group 内模块数量**。
3. 保存修改，重启 Vm 生效。

**关键配置项**
- `VisionMaster.cfg` → “流程缓存队列丢弃阈值数量”（默认 128）

### 1.2.29 脚本模块：脚本模块图像数据转换的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：VM 算法平台软件如何转换图像数据（Bitmap → VM 图像）。

**关键代码（C#）**
```csharp
BitmapData bmpData = _NewBitmap.LockBits(new System.Drawing.Rectangle(0, 0, _NewBitmap.Width, _NewBitmap.Height), ImageLockMode.ReadOnly, System.Drawing.Imaging.PixelFormat.Format8bppIndexed);
int stride = bmpData.Stride;  // 扫描线的宽度
int offset = stride - _NewBitmap.Width;  // 显示宽度与扫描线宽度的间隙
IntPtr iptr = bmpData.Scan0;  // 获取bmpData的内存起始位置
int scanBytes = stride * _NewBitmap.Height;// 用stride宽度，表示这是内存区域的大小
byte[]mapdata = new byte[scanBytes];  //为目标数组分配内存
System.Runtime.InteropServices.Marshal.Copy(iptr, mapdata, 0, scanBytes); //copy内存中数据到数组中
OutImage.Buffer=mapdata;
OutImage.Width=_NewBitmap.Width;
OutImage.Heigth=_NewBitmap.Height;
OutImage.PixelFormat=ImagePixelFormate.MONO8;
SetImageValue("out1",OutImage);
```

**关键 API / 参数**
- 输出图像对象：`OutImage`（含 `Buffer`/`Width`/`Heigth`/`PixelFormat`）
- `PixelFormat = ImagePixelFormate.MONO8`
- 接口：`SetImageValue("out1", OutImage)`

**注意事项 / 坑**
- 原文 `Heigth`、`ImagePixelFormate` 为 VM 脚本环境内的拼写，照原文使用。

### 1.2.30 Group 循环：使用 Group 循环处理 ROI 的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何遍历 ROI 区域，并实现对 ROI 区域循环处理。

**解决步骤**
1. 创建 Group 模块，配置输入设置及循环设置，即订阅需要传入的图像及 ROI 集合。
2. 订阅图像和 ROI：在 Group 中的图像处理模块中订阅传入的图像，并采用“继承”方式订阅 ROI 区域。
3. 订阅索引：订阅 ROI 集合后需指定每次循环处理的 ROI 下标，通过点击方括号中间弹出订阅索引选项。
4. 输出设置：Group 模块配置循环中的输出参数。

**注意事项 / 坑**
- 不熟悉 Group 模块循环的使用及索引订阅方法会导致 ROI 不随循环切换。

---

## 1.3 全局模块类

### 1.3.1 通讯管理：通讯管理的心跳管理功能的使用方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 问题：外部设备与视觉保持连接过程中，因网线被拔、网口松动、视觉程序意外退出等，如何让外部设备的程序知道与视觉的通讯已中断。

**解决步骤**
1. 打开通讯管理：点工具栏通讯管理图标进入。
2. 找到“心跳管理”模块，设置心跳：心跳类型选择“多数据”，时间间隔设置 `1000ms`。

**原理说明**
- 心跳类型“多数据”、间隔 1000ms 时，客户端每隔 1s 收到不同字符串（如当前 `HeartBeat0`，过 1s 收到 `HeartBeat1`，再过 1s 又 `HeartBeat0`，如此循环）。
- 当客户端不再收到来自视觉的字符，或视觉发送的字符不再变化，都说明通讯发生异常。

**注意事项 / 坑**
- 需了解心跳功能用法，以及心跳类型“单数据”和“多数据”的区别。

### 1.3.2 全局触发：使用全局触发功能执行流程的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：以 TCP 通讯为例，视觉作为 TCP 服务端，第三方设备作为 TCP 客户端。客户端发 `T1` 视觉执行流程1；发 `T2` 视觉执行流程2。

**解决步骤**
**方法一（通用，接收类型可为 int/float/string/byte）**
1. 打开 VM，快捷菜单点“通信”按钮；通信界面点设备列表后的加号，协议类型选“TCP 服务端”，设置本机 IP 和本机端口，点创建。
2. 点“接收事件”，进入接收事件窗口，点事件列表后加号，选“字节匹配处理方式”→“协议组装事件类型”，点创建；绑定设备选对应设备；规则列表加号添加规则（如接收 `T1`，类型 `string`，比较规则“等号”）。
   - 注意：规则列表目前只支持“与”逻辑，必须全部满足才触发。本例 T1/T2 为“或”逻辑，需建两个接收事件（一个收 T1，一个收 T2）。
3. 快捷菜单点“全局触发”按钮；点触发序号下加号，按项目添加触发事件。
4. 分别建立两个一模一样的流程；执行后给客户端发送“流程已执行”。

**方法二（简单，接收类型仅 string）**
1. 同方法一步骤一，创建 TCP 服务端。
2. 借助全局触发中的“字符串触发”；如希望客户端发 `T3` 执行流程3，按图配置。
3. 添加流程3，客户端发 T3 执行。

**注意事项 / 坑**
- 接收事件规则仅支持“与”逻辑，多条件“或”需拆成多个事件。
- 方法一为通用型（int/float/string/byte 均可），方法二仅适用于 string。

### 1.3.3 全局变量：全局变量关联流程中具体模块结果的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 问题：将视觉流程中模板匹配算法模块运行的结果数据“特征匹配点 X”关联全局变量 `MatchResultX`。

**解决步骤**
- 在流程运行主界面中按 1、2、3、4 操作：①选中算法模块；②选择“模块结果”Tab 页；③点击“订阅数据”图标；④选择全局变量。

**关键参数**
- 示例全局变量名：`MatchResultX`

**注意事项 / 坑**
- 不了解全局变量绑定操作会导致无法把模块结果暴露给外部。

### 1.3.4 全局脚本：方案加载完成信号发给通信设备的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：需要在方案加载完成后，发送加载完成信号到全局变量，再发送给通信设备。

**解决步骤**
- 通过全局脚本实现，打开示例完成常用基本功能开发；打开全局通信代码后，在脚本中添加代码发送加载完成信号。

**注意事项 / 坑**
- 全局脚本和通信接口不熟悉会导致无法实现。

### 1.3.5 全局脚本：通信设备 ID 获取方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：4.0 版本之前，全局脚本中通信数据接收函数的 `DeviceID` 是按设备管理列表至上而下、从 0 开始依次增 1；现在这种方法行不通。

**解决步骤 / 原理**
- VM4.0 版本每次增加设备列表都会分配唯一的 ID 号，后续全局脚本中判断设备 ID 通过这个唯一 ID 识别，不再从上到下默认排序。

**注意事项 / 坑**
- 版本更新导致 DeviceID 语义变化，老代码需改写。

### 1.3.6 全局脚本：PLC 通讯字符触发流程执行的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：PLC 通讯字符改变时，触发流程执行一次的方法。

**解决步骤**
- 打开全局通信脚本，在 `UserGlobalMethods_OnReceiveCommunicateDataEvent` 里面修改。

**关键代码（C#）**
```csharp
string strTemp="0000";
public override void UserGlobalMethods_OnReceiveCommunicateDataEvent(ReceiveDataInfo dataInfo)
{
    if(dataInfo == null || dataInfo.DeviceData==null)
    {return;}

    //接收到的数据转成字符串
    string str = System.Text.Encoding.Default.GetString(dataInfo.DeviceData);

    if(dataInfo.DeviceID==1)
    {
        //解析收到的数据
        if(str=="0100"&&strTemp=="0000")
        {
            ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle,10000,null);
        }

        if(str=="0400"&&strTemp=="0000")
        {
            //执行流程2一次
            ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle,10001,null);
        }
        strTemp=str;
    }
}
```

**关键 API / 参数**
- 回调：`UserGlobalMethods_OnReceiveCommunicateDataEvent(ReceiveDataInfo dataInfo)`
- `dataInfo.DeviceID == 1`
- `ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10000/10001, null)`
- 边沿判定：`strTemp` 记录上一帧，实现“字符改变才触发一次”

### 1.3.7 全局脚本：通过全局脚本加载本地图像的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：VM 通过全局脚本加载本地图像。

**解决步骤**
1. 打开全局脚本，选择需要的示例。
2. 在运行函数中插入如下代码。

**关键代码（C#）**
```csharp
public int Process()
{
    //m_operateHandle 二次开发SDK操作句柄
    if (m_operateHandle == IntPtr.Zero)
    { return ImvsSdkPFDefine.IMVS_EC_NULL_PTR; }

    ImvsSdkPFDefine.IMVS_PF_INPUT_IMAGE_INFO stImageInfo = new ImvsSdkPFDefine.IMVS_PF_INPUT_IMAGE_INFO();
    stImageInfo.nDataType = 1;
    stImageInfo.nModuleID = 16;//图像源模块序号
    stImageInfo.strImagePath = "E:\\VSproject\\Demo\\12.jpg";

    ImvsPlatformSDK_API.IMVS_PF_SetImageData_CS(m_operateHandle, stImageInfo);

    //System.Threading.Thread.Sleep(200);

    //自定义执行逻辑
    //流程1运行一次
    int nRet = ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10002, null);
    return nRet;
}
```

**关键 API / 参数**
- `ImvsSdkPFDefine.IMVS_PF_INPUT_IMAGE_INFO`：`nDataType=1`、`nModuleID=16`（图像源模块序号）、`strImagePath`
- `ImvsPlatformSDK_API.IMVS_PF_SetImageData_CS`
- `ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10002, null)`

### 1.3.8 全局脚本：通过全局脚本获取通讯输入的参数并赋值给全局变量
**问题现象 / 适用场景**
- 环境：VM4.0.0 及以上
- 现象：全局脚本根据外部通讯输入的数值赋值给全局变量，实现输入与全局变量之间的数值绑定（一般应用于定位、标定等需要外界物理值的场景）。

**解决步骤**
1. 在 VM 通讯管理中设置好通讯设备，连接。
2. 根据通讯设备、接收的信息格式设置接收事件。
3. 在全局变量中设置对应的变量。
4. 在全局脚本中根据输入的字符串进行分割设置对应的全局变量。

**成果**
- 实现模块直接绑定通讯输入的点位信息。

**注意事项 / 坑**
- 不熟悉模块之间的业务关系会导致通讯输入与全局变量无法对应。

### 1.3.9 全局脚本：VM 加载方案后自动执行的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：如何让 VM 在方案加载后自动执行流程。

**解决步骤**
- 通过全局脚本控制方案加载之后希望执行的操作，将如下代码添加到全局脚本中。

**关键代码（C#）**
```csharp
public override int InitAfterLoadSol()
{
    //加载方案完成信号，在方案加载回调函数中获取信号
    Sleep(500);
    //控制流程1执行一次
    ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10000, null);
    return 0;
}
```

**关键 API / 参数**
- 重写：`InitAfterLoadSol()`
- `Sleep(500)`
- `ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10000, null)`

### 1.3.10 全局脚本：多流程协作控制的方法
**问题现象 / 适用场景**
- 环境：VM4.0 及以上
- 现象：如何实现多流程间的协作控制，如：流程 A、B 执行完毕执行流程 C。

**解决步骤**
- 使用全局脚本实现多流程协作控制，主要在流程运行状态回调中判断流程执行状态来控制流程执行。

**关键代码（C#）**
```csharp
using System;
using VM.GlobalScript.Methods;
using System.Linq;
using System.Windows.Forms;
using iMVS_6000PlatformSDKCS;
using System.Runtime.InteropServices;
using System.Threading;
using System.Collections.Generic;
using System.Threading.Tasks;

/*****************************************
 * 示例说明:该示例用于检测流程的运行状态来执行剩余的逻辑
 *         例如:流程0 和流程1 执行完之后需要执行流程2
 * ***************************************/
public class UserGlobalScript : UserGlobalMethods, IScriptMethods
{
    /// <summary>
    /// 初始化函数
    /// </summary>
    /// <returns>成功:返回0</returns>
    public int Init()
    {
        //二次开发SDK初始化
        InitSDK();
        //需要等待多少个流程就添加多少个
        objProcessStatusDict.Add(10000, new ProcessWorkStatus() { });
        objProcessStatusDict.Add(10001, new ProcessWorkStatus() { });
        return 0;
    }

    private Dictionary<uint, ProcessWorkStatus> objProcessStatusDict = new Dictionary<uint, ProcessWorkStatus>();

    /// <summary>
    /// 运行函数
    /// 单次执行:该函数执行一次
    /// 连续执行:以一定时间间隔重复执行该函数
    /// </summary>
    /// <returns>成功:返回0</returns>
    public int Process()
    {
        //m_operateHandle 二次开发SDK操作句柄
        if (m_operateHandle == IntPtr.Zero)
        { return ImvsSdkPFDefine.IMVS_EC_NULL_PTR; }

        //自定义执行逻辑
        //默认执行全部流程，如果自定义流程执行逻辑，请移除DefaultExecuteProcess方法
        int nRet = DefaultExecuteProcess();

        return 0;
    }

    /// <summary>
    ///流程运行状态空闲回调
    /// </summary>
    /// <param name="workStatus"></param>
    public void ExecuteProcessWorkStatus(ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS workStatus)
    {
        try
        {
            //1为忙碌状态，0为空闲状态，为0时说明流程执行完毕
            if (objProcessStatusDict.ContainsKey(workStatus.nProcessID))
            {
                objProcessStatusDict[workStatus.nProcessID].Status = workStatus.nWorkStatus;
            }

            //如果都为true说明已经执行过一次
            if (objProcessStatusDict.All(x => x.Value.IsExecute))
            {
                //全部置位
                foreach (var item in objProcessStatusDict)
                {
                    item.Value.IsExecute = false;
                }
                Task.Run(() =>
                {
                    //执行后续逻辑动作
                    ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10002, null);
                });
            }
        }
        catch (Exception ex)
        {
            //MessageBox.Show(ex.ToString());
        }
    }

    /// <summary>
    /// SDK回调函数
    /// </summary>
    public override void ResultDataCallBack(IntPtr outputPlatformInfo, IntPtr puser)
    {
        base.ResultDataCallBack(outputPlatformInfo, puser);
        ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO struInfo = (ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO)Marshal.PtrToStructure(outputPlatformInfo, typeof(ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO));
        switch (struInfo.nInfoType)
        {
            //获取模块结果数据
            case (uint)ImvsSdkPFDefine.IMVS_CTRLC_OUTPUT_PlATFORM_INFO_TYPE.IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_MODULE_RESULT:
                {
                    ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P resultInfo = (ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P)Marshal.PtrToStructure(struInfo.pData, typeof(ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P));
                    break;
                }
            ///获取流程运行状态
            case (uint)ImvsSdkPFDefine.IMVS_CTRLC_OUTPUT_PlATFORM_INFO_TYPE.IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_WORK_STATE:
                {
                    ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS stWorkStatus = (ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS)Marshal.PtrToStructure(struInfo.pData, typeof(ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS));
                    //处理流程运行状态
                    ExecuteProcessWorkStatus(stWorkStatus);
                    break;
                }
            default:
                break;
        }
    }
}

public class ProcessWorkStatus
{
    public ProcessWorkStatus()
    {
        IsExecute = false;
    }
    public bool IsExecute { get; set; }
    private uint _status;
    public uint Status
    {
        get { return _status; }
        set
        {
            if (_status != value)
            {
                IsExecute = (value == 0 && _status == 1);
                _status = value;
            }
        }
    }
}
```

**关键 API / 参数**
- 命名空间：`VM.GlobalScript.Methods`、`iMVS_6000PlatformSDKCS`
- 流程 ID 字典：`objProcessStatusDict`（key 如 10000、10001）
- 回调：`ExecuteProcessWorkStatus`、`ResultDataCallBack`、`DefaultExecuteProcess`
- 流程状态：`IMVS_PF_MODULE_WORK_STAUS.nWorkStatus`（1=忙碌，0=空闲）
- 触发后续：`IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10002, null)`
- 类：`ProcessWorkStatus`（含 `IsExecute`、`Status`）

**注意事项 / 坑**
- 需熟悉全局脚本控制多流程的写法，状态回调中 `Status` 由 1→0 时才置 `IsExecute=true`。

### 1.3.11 全局脚本：通过通讯触发快速匹配模块换型的方法
**问题现象 / 适用场景**
- 环境：VM4.0 及以上
- 现象：如何实现根据通讯信号切换快速匹配的模型文件并触发流程执行。

**解决步骤**
- 动态切换模板需在全局脚本中调用相关接口实现，可在全局脚本的通讯数据接收回调中实现代码逻辑。

**关键代码（C#）**
```csharp
using System;
using VM.GlobalScript.Methods;
using System.Windows.Forms;
using iMVS_6000PlatformSDKCS;
using System.Runtime.InteropServices;

/**************************************
 * 示例说明: 接收全局通信模块数据示例
 *     前提: 全局通信模块中开启有通信设备
 * 控制逻辑: 1.接收来自全局通信模块接收到的数据
 *           2.如果接收到数据字符T1/T2，则加载对应模型文件并执行流程1一次
 * ***************************************/
public class UserGlobalScript : UserGlobalMethods, IScriptMethods
{
    /// <summary>
    /// 初始化函数
    /// </summary>
    /// <returns>成功:返回0</returns>
    public int Init()
    {
        //二次开发SDK初始化
        InitSDK();
        //设置与全局通信模块的通信端口
        StartGlobalCommunicate();
        //注册通信数据接收事件
        RegesiterReceiveCommunicateDataEvent();
        return 0;
    }

    /// <summary>
    /// 运行函数
    /// 单次执行:该函数执行一次
    /// 连续执行:以一定时间间隔重复执行该函数
    /// </summary>
    /// <returns>成功:返回0</returns>
    public int Process()
    {
        //m_operateHandle 二次开发SDK操作句柄
        if (m_operateHandle == IntPtr.Zero)
        { return ImvsSdkPFDefine.IMVS_EC_NULL_PTR; }
        //默认执行全部流程，如果自定义流程执行逻辑，请移除DefaultExecuteProcess方法
        int nRet = DefaultExecuteProcess();
        return nRet;
    }

    /// <summary>
    /// 通信数据接收函数
    /// </summary>
    public override void UserGlobalMethods_OnReceiveCommunicateDataEvent(ReceiveDataInfo dataInfo)
    {
        if (dataInfo == null || dataInfo.DeviceData == null)
        { return; }
        //接收到的数据转成字符串
        string str = System.Text.Encoding.Default.GetString(dataInfo.DeviceData);
        //创建导入模型结构体
        ImvsSdkPFDefine.IMVS_PF_IMPORT_MODULE_DATA_INPUT stImportData = new ImvsSdkPFDefine.IMVS_PF_IMPORT_MODULE_DATA_INPUT();
        stImportData.stImportModuData = new ImvsSdkPFDefine.IMVS_PF_IMPORT_MODULE_DATA[ImvsSdkPFDefine.IMVS_PF_MAX_IMPORT_NUM];
        //这里的deviceIndex和全局通信模块中的一致
        if (dataInfo.DeviceID == 1)
        {
            //解析收到的数据
            if (str == "T1")
            {
                //导入一个模板
                string strImportFilePath = "E:\\Project\\VMProject\\模板切换\\3.fmxml";
                stImportData.stImportModuData = new ImvsSdkPFDefine.IMVS_PF_IMPORT_MODULE_DATA[ImvsSdkPFDefine.IMVS_PF_MAX_IMPORT_NUM];
                stImportData.nDataNum = 1;
                stImportData.nDataType = 1;
                //操作模块ID
                stImportData.nModuleID = 1;
                stImportData.stImportModuData[0].pData = Marshal.StringToHGlobalAnsi(strImportFilePath);
                int iDataLen = System.Text.Encoding.Default.GetBytes(strImportFilePath).Length;
                stImportData.stImportModuData[0].nDataLen = (uint)iDataLen;
            }
            if (str == "T2")
            {
                //创建模型文件字符串数组,同时导入两个模板
                string[] strImportFilePath = new System.String[] { "E:\\Project\\VMProject\\模板切换\\1.fmxml", "E:\\Project\\VMProject\\模板切换\\2.fmxml" };
                stImportData.nDataNum = 2;
                stImportData.nDataType = 1;
                stImportData.nModuleID = 1;
                int count = 0;
                foreach (var iter in strImportFilePath)
                {
                    stImportData.stImportModuData[count].pData = Marshal.StringToHGlobalAnsi(iter);
                    int iDataLen = System.Text.Encoding.Default.GetBytes(iter).Length;
                    stImportData.stImportModuData[count].nDataLen = (uint)iDataLen;
                    count++;
                }
            }
            //导入模型
            ImvsPlatformSDK_API.IMVS_PF_ImportModuleData_CS(m_operateHandle, stImportData);
            //执行流程1
            ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10000, null);
        }
    }

    /// <summary>
    /// SDK回调函数
    /// </summary>
    public override void ResultDataCallBack(IntPtr outputPlatformInfo, IntPtr puser)
    {
        base.ResultDataCallBack(outputPlatformInfo, puser);
        ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO struInfo = (ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO)Marshal.PtrToStructure(outputPlatformInfo, typeof(ImvsSdkPFDefine.IMVS_PF_OUTPUT_PLATFORM_INFO));
        switch (struInfo.nInfoType)
        {
            //获取模块结果数据
            case (uint)ImvsSdkPFDefine.IMVS_CTRLC_OUTPUT_PlATFORM_INFO_TYPE.IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_MODULE_RESULT:
                {
                    ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P resultInfo = (ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P)Marshal.PtrToStructure(struInfo.pData, typeof(ImvsSdkPFDefine.IMVS_PF_MODULE_RESULT_INFO_LIST_P));
                    break;
                }
            ///获取流程运行状态
            case (uint)ImvsSdkPFDefine.IMVS_CTRLC_OUTPUT_PlATFORM_INFO_TYPE.IMVS_ENUM_CTRLC_OUTPUT_PLATFORM_INFO_WORK_STATE:
                {
                    ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS stWorkStatus = (ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS)Marshal.PtrToStructure(struInfo.pData, typeof(ImvsSdkPFDefine.IMVS_PF_MODULE_WORK_STAUS));
                    break;
                }
            default:
                break;
        }
    }
}
```

**关键 API / 参数**
- 初始化：`InitSDK()`、`StartGlobalCommunicate()`、`RegesiterReceiveCommunicateDataEvent()`
- 数据接收：`UserGlobalMethods_OnReceiveCommunicateDataEvent(ReceiveDataInfo dataInfo)`
- `dataInfo.DeviceID == 1`
- 导入结构体：`IMVS_PF_IMPORT_MODULE_DATA_INPUT`、`IMVS_PF_IMPORT_MODULE_DATA`
  - `nDataNum`、`nDataType=1`、`nModuleID=1`、`stImportModuData[].pData`、`stImportModuData[].nDataLen`
- `IMVS_PF_MAX_IMPORT_NUM`
- `ImvsPlatformSDK_API.IMVS_PF_ImportModuleData_CS(m_operateHandle, stImportData)`
- `ImvsPlatformSDK_API.IMVS_PF_ExecuteOnce_V30_CS(m_operateHandle, 10000, null)`
- 模板文件路径示例：`E:\Project\VMProject\模板切换\3.fmxml`、`1.fmxml`、`2.fmxml`

**注意事项 / 坑**
- 不熟悉全局脚本通讯回调及模板导入相关接口时极易出错；`DeviceID` 须与全局通信模块中一致。

---

## 1.4 通讯类

### 1.4.1 通讯管理：ModBus 通信发送非整型数据的方法
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 现象：Modbus 通信发送数据只能为 Int 类型（界面显示误导）。

**解决步骤**
- 实际可以发送 Int 和 Float 数据：
  1. 发送数据支持 Int 和 Float。
  2. 通信设备配置。
  3. 发送事件配置。

**关键参数**
- 可发送类型：Int、Float
- 一般 Float 类型乘以 1000 后都可转化为 Int 类型发送。

**注意事项 / 坑**
- 通信管理界面显示有问题，显示为 Int 类型存在一定误导；实际可发送 Int 与 Float。

### 1.4.2 通讯管理：使用 Modbus TCP 通讯协议与流程交互
**问题现象 / 适用场景**
- 环境：VM4.0.0
- 问题：使用 Modbus TCP 通讯协议与视觉通讯，当地址为 0000 的保持型寄存器（4x 寄存器）变为 1 时，触发视觉流程执行一次，同时视觉将地址为 0000 的寄存器复位（写为 0）；视觉流程执行完成后，将结果数据（特征匹配状态、特征匹配点 X、特征匹配点 Y、特征角度）分别写入地址 0001、0002、0004、0006 的保持型寄存器。

**解决步骤 / 原理**
- VM4.0 相比 VM3.X 最大改进是新增**网关功能**，能满足视觉与绝大多数上位机、机器人、PLC 通过用户自定义协议通讯。涉及 4 个知识点：
  1. 全局模块中通讯设备的创建
  2. 通讯接收事件与全局触发的关系
  3. 通讯发送事件的使用
  4. 发送整数和浮点数到 Modbus 寄存器

**第一步：创建通讯设备**
- 工具栏点“通讯管理”图标进入（黄色箭头所示）。
- 创建一个 Modbus 通讯设备。
- 目标 IP 填 PLC 的 IP 地址（本例用 Modbus 仿真设备模拟，填 `127.0.0.1`）；目标端口填 `502`（Modbus TCP 协议默认端口）。

**第二步：添加寄存器地址**
- 添加触发流程运行一次的寄存器地址，**轮询使能要打开**。（注意地址的数据类型、寄存器个数、发送顺序；发送顺序与 PLC 类型有关，大端模式数据高字节存低地址、低字节存高地址，小端模式相反。）
- 添加特征匹配模块状态寄存器地址（写入寄存器，轮询不必打开）。
- 添加特征匹配坐标 X 存放地址（写入寄存器，轮询不必打开）。
- 添加特征匹配坐标 Y 存放地址（写入寄存器，轮询不必打开）。
- 添加特征匹配角度存放地址（写入寄存器，轮询不必打开）。

**第三步：定义接收事件**
- 绑定地址下拉选择之前添加的触发寄存器地址。
- 在规则列表中定义规则。

**第四步：配置全局触发**
- 工具栏点“全局触发”图标（黄色箭头所示）。
- 进入全局触发设置，选“事件触发”Tab 页，触发事件中下拉选择上一步配置好的接收事件；触发命令类型选“执行流程”，触发配置选“流程1”，触发字符无需填写。

**第五步：定义发送事件**
- （原文为图示，文字缺失）

**关键参数**
- Modbus TCP 默认端口：`502`
- 触发寄存器：4x 地址 `0000`（保持型，轮询使能开）
- 写回寄存器：`0001`（特征匹配状态）、`0002`（特征匹配点 X）、`0004`（特征匹配点 Y）、`0006`（特征匹配角度）
- 字节序：大端 / 小端（依 PLC 型号）

**注意事项 / 坑**
- 写入结果的寄存器轮询不必打开；触发寄存器需打开轮询。
- 注意 PLC 的字节序（大端/小端）与发送顺序配置一致。

---

## 条目索引

1.1.1 驱动配置：图像后台切换但前端界面不变的解决方法
1.1.2 驱动缺失：格式化工具打开后消失的解决方法
1.1.3 环境配置：VM 试用版本激活报错的解决方法
1.1.4 模块数限制：修改 VM 最大模块数量
1.1.5 开机自启动：VM 运行界面导出物开机运行的设置方法
1.1.6 锁定模式：开启锁定模式提示信息的方法
1.1.7 环境配置：格式化模块报错解决方法
1.1.8 环境配置：VM3.4 启动失败解决办法
1.1.9 环境配置：VM 进程启动失败解决办法
1.1.10 内存管理：开启虚拟内存的方法
1.1.11 运行间隔：设置流程运行间隔的方法
1.1.12 静默执行：禁止 VM 静默执行的方法
1.1.13 用户权限：普通用户权限使用 VM 的方法
1.1.14 图标隐藏：电脑右下角 VM 图标不显示的方法
1.2.1 文本保存：逐行保存格式化模块输出的方法
1.2.2 脚本模块：循环模块搭配脚本使用的方法
1.2.3 几何查找：彩色图像的几何查找方法
1.2.4 深度学习：图像分割的面积的获取方法
1.2.5 颜色识别：使用颜色识别工具做分类检测的方法
1.2.6 数据分析：使用脚本模块解析 32 位寄存器数据的方法
1.2.7 定位功能：使用位置修正模块实现 ROI 自动修正
1.2.8 读码功能：设置读码参数方法
1.2.9 图像采集：运行 VP 后 VM 流程中相机取图失败的解决方法
1.2.10 多图融合：使用多图融合工具实现光度立体法
1.2.11 仿射变换：使用仿射变换进行抠图的方法
1.2.12 中线测量：测量中线之间距离的方法
1.2.13 图像增强：使用图像增强工具凸显目标方法
1.2.14 字符串显示：使用脚本显示字符串的方法
1.2.15 路径提取：使用 VM 路径提取工具查找边缘点的方法
1.2.16 标定板生成：使用 VM 自研标定板 Demo 生产标定板的方法
1.2.17 脚本模块：编写脚本处理点集合的方法
1.2.18 脚本模块：添加自定义程序集的方法
1.2.19 N 点标定：模块 N 点标定的使用方法
1.2.20 字符识别：使用字符识别模块训练的方法
1.2.21 渲染保存：将多个模块的渲染结果在原彩色图片中保存的方法
1.2.22 分支字符：使用分支字符调试不同分支的方法
1.2.23 调试脚本：对脚本进行调试的方法
1.2.24 区域设置：多个不连续 ROI 同时检测的使用方法
1.2.25 通讯模块：通讯模块发送数据点集合的方法
1.2.26 模板保存：导入及导出匹配模板的方法
1.2.27 标定片标定：使用标定板标定激光振镜的方法
1.2.28 Group 显示：Group 嵌套循环使能渲染显示的方法
1.2.29 脚本模块：脚本模块图像数据转换的方法
1.2.30 Group 循环：使用 Group 循环处理 ROI 的方法
1.3.1 通讯管理：通讯管理的心跳管理功能的使用方法
1.3.2 全局触发：使用全局触发功能执行流程的方法
1.3.3 全局变量：全局变量关联流程中具体模块结果的方法
1.3.4 全局脚本：方案加载完成信号发给通信设备的方法
1.3.5 全局脚本：通信设备 ID 获取方法
1.3.6 全局脚本：PLC 通讯字符触发流程执行的方法
1.3.7 全局脚本：通过全局脚本加载本地图像的方法
1.3.8 全局脚本：通过全局脚本获取通讯输入的参数并赋值给全局变量
1.3.9 全局脚本：VM 加载方案后自动执行的方法
1.3.10 全局脚本：多流程协作控制的方法
1.3.11 全局脚本：通过通讯触发快速匹配模块换型的方法
1.4.1 通讯管理：ModBus 通信发送非整型数据的方法
1.4.2 通讯管理：使用 Modbus TCP 通讯协议与流程交互
