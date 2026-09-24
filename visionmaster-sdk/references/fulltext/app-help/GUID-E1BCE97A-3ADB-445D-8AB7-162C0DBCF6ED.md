<!-- src:GUID-E1BCE97A-3ADB-445D-8AB7-162C0DBCF6ED.html -->
<!-- path:模块使用参考 > 逻辑工具 > Python脚本 -->
# Python脚本

# Python脚本

Python脚本模块功能和脚本模块大同小异，差别主要为编程语言的不同。Python脚本基于Python开发语言，脚本基于C#开发语言。

说明

Python脚本模块只能对流程内的数据进行处理。如需对方案下所有流程的批量执行逻辑进行控制，可通过全局脚本实现。

本节内容包含：

* 界面概览
* 编程指引
* 脚本接口
* 结构体
* 模块结果

## 界面概览

将Python脚本模块拖入流程编辑区后，双击该模块打开Python脚本编辑窗口。

![](GUID-3CDFD590-1A8A-4358-A5C0-7AAFB6A7C1BE-high.png)

图 1 Python脚本

该窗口各区域说明如下：

表 1 脚本编辑窗口介绍

| 窗口区域 | 描述 |
| --- | --- |
| 输入/输出变量编辑区 | 设置输入输出的变量，可自定义变量名称。变量支持多种数据类型，主要为int（整型）、float（浮点型）、string（字符串）、byte（字节）、image（图像）、ROIBOX（ROI内的识别框）、ANNULUS（圆环）、POLYGON（多边形）、POINT（点）、LINE（线）、FIXTURE（修正信息）、RECT（矩形）、ELLIPSE（椭圆）、pointset（点集）。  说明 不带“[]”的变量为一个值，带“[]”的变量为数组。   * 输入设置：可通过初始值订阅Python脚本前序模块的结果或全局/局部变量。 * 输出设置：可作为Python脚本后序模块的输入。 |
| 控制栏 | * 导入：导入脚本程序（格式：.py）。 * 导出：导出脚本程序（格式：.py）。 * 导出工程：将脚本程序导出，导出后可使用Visual   Studio进行调试。 * ：单击后可设置密码以启用加密权限。启用加密后，实时生效，未验证密码只能修改输入变量的值或订阅，以及执行预编译、执行和确定功能；验证密码成功后可进行查看、编辑代码等其他操作；再次单击并输入密码可取消加密。 |
| Python编程区 | 可在此处通过调用脚本接口等方式自定义开发脚本。  该区域提供脚本的默认代码及相关说明。  说明 在C#编程区自定义脚本代码之前，需先在输入/输出变量编辑区定义输入变量（例如int型的in0）和输出变量（例如int型的out0）。完成定义后，可在C#编程区中直接编写代码，获取或设置变量的值。 |
| 结果显示 | 显示该模块编译后的打印和保存信息。 |
| 其他功能 | * 预编译：可对脚本程序进行预编译，单击该按钮即调用Init方法。 * 执行：单击该按钮即调用Process方法。 * 确定：   保存修改后的代码并退出脚本编辑界面。 |

## 编程指引

可在Python编程区可自定义编写脚本代码，其核心接口Process。

可在Process方法中实现变量计算和逻辑处理等自定义逻辑，相关功能在流程执行时生效。在Process方法内自定义代码逻辑时，成功返回0，否则返回其他值。

注意

* 自定义代码逻辑需写入`try...except...`中，方便定位异常，同时避免内存泄漏。
* Python代码严格要求按照4个空格缩进，不支持tab缩进。

进入Process方法后，需先初始化变量，否则无法访问输入/输出变量、全局/局部变量。具体代码如下：

```
  moduleVar = IoHelper(data, INIT_MODULE_VAR)
  globalVar = IoHelper(data, INIT_GLOBAL_VAR)
  localVar = IoHelper(data, INIT_LOCAL_VAR)
```

说明

* 其中moduleVar表示该模块中设置的输入和输出变量，globalVar表示方案中的全局变量，localVar表示模块所处流程或Group模块中的局部变量。
* 所有变量都需严格根据变量类型使用。若需转换类型转换，应在用户代码内通过显示转换代码进行类型转换。
* 默认代码中已有初始化变量的相关逻辑，不需要手动额外添加。

读写输入输出变量的方式如下：

* 输入变量为只读，无法修改。假设输入变量名为in0，类型为int，可通过`tmp =
  moduleVar.in0`读取该变量的值。
* 输出变量为只写，无法读取。
  假设输出变量名为out0，类型为int，可通过`moduleVar.out
  = 9`设置该变量的值。

说明

全局变量和局部变量支持读取和修改，操作方法类似，但需将moduleVar对应更换为globalVar或localVar。

## 使用方法

Python脚本模块支持自定义代码逻辑处理输入数据，实现基本算法模块无法实现的数据处理逻辑，帮助您提高开发效率和灵活适应各种应用场景。

### 使用场景

Python脚本模块适用于在实现一些复杂或基本模块无法实现的逻辑时使用，通过自定义代码实现这些数据处理逻辑。

### 调用模块

Python脚本模块支持绝大部分数据类型的处理，无针对前置或后置模块的特定要求，在流程中可搭配各类模块使用，根据脚本自定义的代码逻辑处理输入数据，将结果数据输出给后置模块。即只要脚本逻辑与流程逻辑匹配，模块可在流程中的任意环节调用。

在流程中调用Python脚本模块后，可在`Process()`方法中实现变量计算和逻辑处理等具体的功能。

### 应用示例

假设在某视觉业务场景中需要将定位目标匹配点的X、Y坐标按照X坐标值从小到大排列输出。基于此场景，方案流程如下。

![](GUID-878DDFCF-519C-4062-8AA4-D2BA9BC36EF0-high.png)

图 2 方案流程

该示例通过图像源模块输入目标图像；通过快速匹配模块对目标进行定位；再通过Python脚本模块对匹配点的X、Y坐标进行排序输出。下文只对Python脚本模块配置进行介绍，图像源和快速匹配模块详细说明请参见图像源和快速匹配。

1. 双击Python脚本模块。
2. 在Python脚本对话框，配置输入和输出变量。

   输入变量订阅快速匹配模块的float型数组；输出变量也设置为float型数组供后续使用，如下图所示。

   ![](GUID-19E6E346-B1E8-4CD0-B371-9D4655351F1F-high.png)

   图 3 配置变量
3. 在Python编程区，输入如下示例代码。

   说明

   示例代码仅供参考，使用过程中请根据实际需求编写代码。

   ```
   # coding: utf-8
   import sys
   from ioHelper import *

   def Process(data) -> int:
       """Write custom logic code inside the Process method. Return 0 for success or any other value for failure."""
       """在Process方法内编写自定义逻辑代码, 成功返回0, 返回其他值表示失败"""

       """Do not delete this code block."""
       """请勿删除此处代码"""
       moduleVar = IoHelper(data, INIT_MODULE_VAR)
       globalVar = IoHelper(data, INIT_GLOBAL_VAR)
       localVar = IoHelper(data, INIT_LOCAL_VAR)

       #创建空列表
       matchPointX = []
       matchPointY = []
       #输入变量赋值到列表
       matchPointX = moduleVar.in0
       matchPointY = moduleVar.in1
       try:
           #组装为字典
           matchDict = dict(zip(matchPointX,matchPointY))
           matchPointX.clear()
           matchPointY.clear()
           #按字典键（X坐标）值进行排序
           sortedList = sorted(matchDict.items())
           PrintMsg(str(sortedList))
           for item in sortedList:
               #字典拆分
               matchPointX.append(item[0])
               matchPointY.append(item[1])
           #赋值到输出变量
           moduleVar.out0 = matchPointX
           moduleVar.out1 = matchPointY
       except BaseException as e:
           PrintMsg(e)
       return 0
   ```
4. 进行预编译和执行操作。

代码执行完毕后可对比查看快速匹配模块图像和Python脚本模块输出变量，验证执行结果，如下图所示。

![](GUID-15171E7A-CC38-4202-8700-CF270644C0DB-high.png)

图 4 验证执行结果

## 脚本接口

Python脚本提供个别开放接口，方便您通过代码控制变量。

* globalVar.GetValue：获取全局变量
* globalVar.SetValue：设置全局变量
* localVar.GetValue：获取局部变量
* localVar.SetValue：设置局部变量

### globalVar.GetValue

接口原型
:   `globalVar.GetValue(paramName)`

功能描述
:   获取全局变量

输入参数
:   `paramName`：string类型，全局变量名称。

返回值
:   成功返回全局变量的值，失败返回None。

### globalVar.SetValue

接口原型
:   `globalVar.SetValue(paramName，paramValue)`

功能描述
:   设置全局变量

输入参数
:   `paramName`：string类型，全局变量名称。

    `paramValue`：全局变量的值。

返回值
:   成功返回0，失败返回非0。

### localVar.GetValue

接口原型
:   `localVar.GetValue(paramName)`

功能描述
:   获取局部变量

输入参数
:   `paramName`：string类型，局部变量名称

返回值
:   成功返回全局变量的值，失败返回None。

### localVar.SetValue

接口原型
:   `localVar.SetValue(paramName，paramValue)`

功能描述
:   设置局部变量

输入参数
:   `paramName`：string类型，局部变量名称

    `paramValue`：局部变量的值

返回值
:   成功返回0，失败返回非0。

## 结构体

使用Python脚本编写代码时，会使用到一些结构体。

具体包含如下结构体：

* RoiAnnulus
* Circle
* ELLIPSE
* Fixture
* ImageData
* Line
* Point
* PointSet
* Rect
* RoiBox
* RoiPolygon
* Annulus

### RoiAnnulus

对应ROI圆环。相关参数如下：

center\_x
:   ROI圆环中心点X

center\_y
:   ROI圆环中心点Y

inner\_radius
:   ROI圆环内径

outer\_radius
:   ROI圆环外径

start\_angle
:   ROI圆环起始角度

angle\_extend
:   ROI圆环展开角度

### Circle

对应圆。相关参数如下：

radius
:   半径

center\_x
:   圆心X

center\_y
:   圆心Y

### ELLIPSE

对应椭圆。相关参数如下：

center\_x
:   椭圆中心点X

center\_y
:   椭圆中心点Y

major\_radius
:   椭圆长轴

minor\_radius
:   椭圆短轴

angle
:   椭圆角度

### Fixture

对应位置修正信息。相关参数如下：

init\_point\_x
:   基准点X

init\_point\_y
:   基准点Y

init\_angle
:   基准角度

init\_scale\_x
:   基准尺度X

init\_scale\_y
:   基准尺度Y

run\_point\_x
:   运行点X

run\_point\_y
:   运行点Y

run\_angle
:   运行角度

run\_scale\_x
:   运行尺度X

run\_scale\_y
:   运行尺度Y

### ImageData

对应图像数据。相关参数如下：

width
:   图像宽度

height
:   图像高度

pixel\_format
:   像素格式

buffer
:   图像数据

dataLen
:   数据长度

### Line

对应直线。相关参数如下：

start\_point\_x
:   直线起点X

start\_point\_y
:   直线起点Y

end\_point\_x
:   直线终点X

end\_point\_y
:   直线终点Y

### Point

对应点。相关参数如下：

point\_x
:   点X

point\_y
:   点Y

### PointSet

对应点集。相关参数如下：

buffer
:   点集数据

dataLen
:   数据长度

### Rect

对应矩形。相关参数如下：

rect\_x
:   矩形起点X

rect\_y
:   矩形起点Y

width
:   矩形宽度

height
:   矩形高度

### RoiBox

对应Box。相关参数如下：

center\_x
:   Box中心点X

center\_y
:   Box中心点Y

width
:   Box宽度

height
:   Box高度

angle
:   Box角度

### RoiPolygon

对应多边形。相关参数如下：

point\_num
:   多边形点数

point\_x
:   多边形顶点X

point\_y
:   多边形顶点Y

### Annulus

对应圆环。相关参数如下：

center\_x
:   圆环中心点X

center\_y
:   圆环中心点Y

inner\_radius
:   圆环内径

outer\_radius
:   圆环外径

start\_angle
:   圆环起始角度

angle\_extend
:   圆环展开角度

## 模块结果

Python脚本模块的模块结果具体如下：

耗时（ms）
:   float型，代表该模块运行时耗费的时间。

模块状态
:   int型，0代表NG，此时模块呈现红色；1代表OK，此时模块呈现绿色。
