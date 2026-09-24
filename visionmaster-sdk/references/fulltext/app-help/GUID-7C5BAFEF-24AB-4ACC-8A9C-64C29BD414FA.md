<!-- src:GUID-7C5BAFEF-24AB-4ACC-8A9C-64C29BD414FA.html -->
<!-- path:模块使用参考 > 逻辑工具 > 脚本 -->
# 脚本

# 脚本

可在流程中调用脚本模块，并通过自定义脚本代码控制流程数据处理。

## 使用限制

* 脚本模块仅支持使用标准C#语言（Windows版本）进行编写。
* 脚本模块只能对流程内的数据进行处理。如需对方案下所有流程的批量执行逻辑进行控制，可通过全局脚本实现。

## 界面概览

将脚本模块拖入流程编辑区后，双击该模块打开脚本编辑窗口。

![](GUID-A76FEF39-E075-405E-8FEB-8B7716D894D1-high.png)

图 1 脚本编辑窗口

该窗口各区域说明如下：

表 1 脚本编辑窗口介绍

| 窗口区域 | 描述 |
| --- | --- |
| 相关设置 | 对设置输入输出的变量，可自定义变量名称。变量支持多种数据类型，主要为int（整型）、int[]、float（浮点型）、float[]、string（字符串）、string[]、byte（字节）、image（图像）、ROIBOX（ROI内的识别框）、ROIBOX[]、ANNULUS（圆环）、POLYGON（多边形）、POINT（点）、LINE（线）、FIXTURE（修正信息）、RECT（矩形）、ELLIPSE（椭圆）、pointset（点集）。  说明 不带“[]”的变量为一个值，带“[]”的变量为数组。   * 输入设置：可通过初始值绑定脚本前序模块的结果或全局/局部变量。 * 输出设置：输出变量可作为脚本需显示的内容或后序模块的输入。部分类型（请以实际为准）的输出变量勾选后，将在显示设置中显示，作为该模块的信息输出，并可在该模块的图像上显示。 * 显示设置：显示输出设置中勾选的输出变量。其中参数名称可自定义修改，除image类型外的数据还可单击进行显示相关设置。 |
| 控制栏 | * 导入：导入脚本程序（格式：.cs）。 * 导出：导出脚本程序（格式：.cs）。 * 编辑程序集：添加程序集，与全局脚本添加程序集相同，详情参见程序集添加。 * 导出工程：将脚本程序导出，导出后可使用Visual   Studio进行调试。 * 查询接口：查询设置或获取不同数据类型参数的接口以及其他常用接口。 * ：单击后可设置密码以启用加密权限。启用加密后，实时生效，未验证密码只能修改输入变量的值或订阅，以及执行预编译、执行和确定功能；验证密码成功后可进行查看、编辑代码等其他操作；再次单击并输入密码可取消加密。 |
| C#编程区 | 可在此处通过调用脚本接口等方式自定义开发脚本。  该区域提供脚本的默认代码，默认代码的简要解读参见下文的默认代码导读。  说明 在C#编程区自定义脚本代码之前，需先在输入/输出变量编辑区定义输入变量（例如int型的in0）和输出变量（例如int型的out0）。完成定义后，可在C#编程区中直接编写代码，获取或设置数组类型以外类型的变量的取值。示例如下：   ``` public bool Process() {   int a = in0;   out0 = 32;   return true; } ``` |
| 编译结果显示 | 显示该模块编译后的结果信息。 |
| 其他功能 | * 预编译：对脚本程序进行预编译，单击该按钮即调用Init方法（该方法详情见下文的使用方法）。 * 执行：单击该按钮即调用Process方法（该方法详情见下文的使用方法）。 * 确定： 保存修改后的代码并退出脚本编辑界面。 |

## 使用方法

* 调用脚本模块

  在流程中调用脚本模块时，无针对前序/后序模块的特定要求。只要脚本逻辑与流程逻辑匹配，脚本模块可在流程中的任意环节调用。
* 自定义脚本代码

  在流程中调用脚本模块后，可在C#编程区调用脚本开放接口自定义脚本代码。其中的核心接口为Init和Process。

  + 可在Init方法中实现变量初始化和句柄创建等初始化逻辑，相关工作会在加载方案时完成。
  + 可在Process方法中实现变量计算和逻辑处理等具体的功能，具体的功能在流程执行时执行。

    ![](GUID-4760D199-0F73-486C-8625-B4CE148015B4-high.png)

    图 2 Init与Process方法的执行顺序

  说明

  脚本模块还支持调用C#程序集和非托管库，具体调用方法与全局脚本的第三方库调用相同，详情参见第三方库调用方法。

## 应用示例

脚本的具体应用示例，请参见应用示例：通信数据收发控制。

## 默认代码导读

脚本模块在C#编程区提供的默认代码如下。其中Init方法只有在加载方案或者修改代码后预编译时才会运行，Process方法在流程执行的时候运行。

可在`public partial class
UserScript:ScriptMethods,IProcessMethods`中自行实现代码逻辑。

```
using System;
using System.Text;
using System.Windows.Forms;
using Script.Methods;
/************************************
Shell Module default code: using .NET Framwwork 4.6.1
*************************************/
public partial class UserScript:ScriptMethods,IProcessMethods
{
    //the count of process
    //执行次数计数
    int processCount ;

    /// <summary>
    /// Initialize the field's value when compiling
    /// 预编译时变量初始化
    /// </summary>
    public void Init()
    {
        //You can add other global fields here
	//变量初始化，其余变量可在该函数中添加
        processCount = 0;

    }

    /// <summary>
    /// Enter the process function when running code once
    /// 流程执行一次进入Process函数
    /// </summary>
    /// <returns></returns>
    public bool Process()
    {
        //You can add your codes here, for realizing your desired function
	//每次执行将进入该函数，此处添加所需的逻辑流程处理

        return true;
    }
}
```

## 脚本Demo源码

以下为脚本Demo文件ScriptDemo.cs的源码。该文件可从VM安装路径下获取，相对路径为：.\Applications\Module(sp)\x64\Logic\ShellModule。

```
using System;
using System.Text;
using System.Windows.Forms;
using Script.Methods;
public partial class UserScript:ScriptMethods,IProcessMethods
{
    //the count of process
    //执行次数计数
    int processCount ;

    /// <summary>
    /// Initialize the field's value when compiling
    /// 预编译时变量初始化
    /// </summary>
    public void Init()
    {
        //You can add other global fields here
	//变量初始化，其余变量可在该函数中添加
        processCount = 0;

    }

    /// <summary>
    /// Enter the process function when running code once
    /// 流程执行一次进入Process函数
    /// </summary>
    /// <returns></returns>
    public bool Process()
    {
        //You can add your codes here, for realizing your desired function
	//每次执行将进入该函数，此处添加所需的逻辑流程处理

	//获取设置int
        int a = 0;
        GetIntValue("in0",ref a);
        SetIntValue("out0", a);

        //获取设置float
        float f=0f;
        GetFloatValue("in1",ref f);
        SetFloatValue("out1", f);

        //获取设置string
        string s="";
        GetStringValue("in2",ref s);
        SetStringValue("out2", s);

        //获取设置二进制数据
        byte[] by = new byte[]{};
        GetBytesValue("in8",ref by);
        SetBytesValue("out8", by);

        int count=0;
        //获取设置int数组
        int[] narry = new int[3];
        GetIntArrayValue("in3",ref narry,out count);
        SetIntArrayValue("out3",narry,0,narry.Length);

        //获取设置float数组
        float[] farry = new float[3];
        GetFloatArrayValue("in4",ref farry,out count);
        SetFloatArrayValue("out4",farry,0,farry.Length);

        //获取设置strig数组
        string[] sarry = new string[3];
        GetStringArrayValue("in5",ref sarry,out count);
        SetStringArrayValue("out5",sarry,0,sarry.Length);

	//设置/获取16进制数据
        byte[] tempBytes = new byte[] { };
        GetBytesValue("in1", ref tempBytes);
        SetBytesValue("out1", new byte[]{0x00,0x02});

        //设置/获取图像数据
        ImageData imagedata = new ImageData();
        GetImageValue("in6", ref imagedata);
        SetImageValue("out6", imagedata);

	//设置/获取ROIBOX数据
	RoiboxData roidata = new RoiboxData();
        GetRoiboxValue("in7", ref roidata);
        SetRoiboxValue("out7", roidata);

        //设置全局变量
        GlobalVariableModule.SetValue("var1", "323");
        //2.获取全局变量
        object paramValue = GlobalVariableModule.GetValue("var1");

        //获取模块结果数据
        //GetModule传入模块的名称，如果存在group中，需要加上group的名称
        //GetValue() 传入的是模块的输出参数名称
        object result = CurrentProcess.GetModule("图像源1").GetValue("Height");
        object result1 = CurrentProcess.GetModule("组合模块1.图像源1").GetValue("Height");

        //设置模块运行参数
        //如果该模块在group内部，需要加上group模块的参数名称
        //SetValue(),key值为具体的参数名称，
        CurrentProcess.GetModule("BLOB分析1").SetValue("FindNum", "4");
        CurrentProcess.GetModule("组合模块1.BLOB分析1").SetValue("FindNum", "4");

        //5.通信发送数据
        //GetDevice(int index), index为通信设备的ID
        //tcp,udp,串口发送数据调用函数
        GlobalCommunicateModule.GetDevice(1).SendData("msg",DataType.StringType);

        //plc设备发送数据
        //GetAddress(int index),index为address的ID
        GlobalCommunicateModule.GetDevice(2).GetAddress(1).SendData("100",DataType.IntType);
        GlobalCommunicateModule.GetDevice(2).GetAddress(1).SendData("100",DataType.StringType);
        GlobalCommunicateModule.GetDevice(2).GetAddress(1).SendData("100",DataType.FloatType);

        //modbus发送设备数据
        GlobalCommunicateModule.GetDevice(3).GetAddress(1).SendData("100",DataType.IntType);
        GlobalCommunicateModule.GetDevice(3).GetAddress(1).SendData("100",DataType.StringType);
        GlobalCommunicateModule.GetDevice(3).GetAddress(1).SendData("100",DataType.FloatType);

        return true;
    }
}
```

## 模块结果

脚本模块的模块结果具体如下：

耗时（ms）
:   float型，代表该模块运行时耗费的时间。

模块状态
:   int型，0代表NG，此时模块呈现红色；1代表OK，此时模块呈现绿色。

out\*
:   类型由输出变量设置时决定，显示输出变量的信息。
