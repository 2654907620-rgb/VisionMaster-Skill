<!-- src:class_light_module_cs_1_1_light_param.html -->
<!-- path:接口函数 > 采集 > 光源 > LightParam -->
# LightParam类 参考 采集 » 光源

光源参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | OutputTypeEnum {     OK = 1,     NG = 2   } |
|  | 输出类型 更多... |
|  | |
| enum | Channel1LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道1光源状态 更多... |
|  | |
| enum | Channel1LightStateVBEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道1光源状态 更多... |
|  | |
| enum | Channel1EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道1沿定义 更多... |
|  | |
| enum | Channel2LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道2光源状态 更多... |
|  | |
| enum | Channel2LightStateVBEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道2光源状态 更多... |
|  | |
| enum | Channel2EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道2沿定义 更多... |
|  | |
| enum | Channel3LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道3光源状态 更多... |
|  | |
| enum | Channel3EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道3沿定义 更多... |
|  | |
| enum | Channel4LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道4光源状态 更多... |
|  | |
| enum | Channel4EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道4沿定义 更多... |
|  | |
| enum | Channel5LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道5光源状态 更多... |
|  | |
| enum | Channel5EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道5沿定义 更多... |
|  | |
| enum | Channel6LightStateEnum {     LightStateOn = 1,     LightStateOff = 2   } |
|  | 通道6光源状态 更多... |
|  | |
| enum | Channel6EdgeTypeEnum {     EdgeTypeRising = 1,     EdgeTypeFalling = 2   } |
|  | 通道6沿定义 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< int > | InputChannel1Brightness `[set]` |
|  | 通道1亮度 更多... |
|  | |
| List< int > | InputChannel2Brightness `[set]` |
|  | 通道2亮度 更多... |
|  | |
| List< int > | InputChannel3Brightness `[set]` |
|  | 通道3亮度 更多... |
|  | |
| List< int > | InputChannel4Brightness `[set]` |
|  | 通道4亮度 更多... |
|  | |
| List< int > | InputChannel5Brightness `[set]` |
|  | 通道5亮度 更多... |
|  | |
| List< int > | InputChannel6Brightness `[set]` |
|  | 通道6亮度 更多... |
|  | |
| List< string > | InputString `[set]` |
|  | 输入字符 更多... |
|  | |
| OutputTypeEnum | OutputType `[get, set]` |
|  | 输出类型 更多... |
|  | |
| int | TriggerTime `[get, set]` |
|  | 触发时间(ms)，范围：[-1,65535] 更多... |
|  | |
| bool | Channel1Enable `[get, set]` |
|  | 通道1使能 更多... |
|  | |
| int | Channel1Brightness `[get, set]` |
|  | 通道1亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel1LightStateEnum | Channel1LightState `[get, set]` |
|  | 通道1光源状态 更多... |
|  | |
| Channel1LightStateVBEnum | Channel1LightStateVB `[get, set]` |
|  | 通道1光源状态 更多... |
|  | |
| Channel1EdgeTypeEnum | Channel1EdgeType `[get, set]` |
|  | 通道1沿定义 更多... |
|  | |
| int | Channel1DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel2Enable `[get, set]` |
|  | 通道2使能 更多... |
|  | |
| int | Channel2Brightness `[get, set]` |
|  | 通道2亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel2LightStateEnum | Channel2LightState `[get, set]` |
|  | 通道2光源状态 更多... |
|  | |
| Channel2LightStateVBEnum | Channel2LightStateVB `[get, set]` |
|  | 通道2光源状态 更多... |
|  | |
| Channel2EdgeTypeEnum | Channel2EdgeType `[get, set]` |
|  | 通道2沿定义 更多... |
|  | |
| int | Channel2DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel3Enable `[get, set]` |
|  | 通道3使能 更多... |
|  | |
| int | Channel3Brightness `[get, set]` |
|  | 通道3亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel3LightStateEnum | Channel3LightState `[get, set]` |
|  | 通道3光源状态 更多... |
|  | |
| Channel3EdgeTypeEnum | Channel3EdgeType `[get, set]` |
|  | 通道3沿定义 更多... |
|  | |
| int | Channel3DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel4Enable `[get, set]` |
|  | 通道4使能 更多... |
|  | |
| int | Channel4Brightness `[get, set]` |
|  | 通道4亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel4LightStateEnum | Channel4LightState `[get, set]` |
|  | 通道4光源状态 更多... |
|  | |
| Channel4EdgeTypeEnum | Channel4EdgeType `[get, set]` |
|  | 通道4沿定义 更多... |
|  | |
| int | Channel4DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel5Enable `[get, set]` |
|  | 通道5使能 更多... |
|  | |
| int | Channel5Brightness `[get, set]` |
|  | 通道5亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel5LightStateEnum | Channel5LightState `[get, set]` |
|  | 通道5光源状态 更多... |
|  | |
| Channel5EdgeTypeEnum | Channel5EdgeType `[get, set]` |
|  | 通道5沿定义 更多... |
|  | |
| int | Channel5DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel6Enable `[get, set]` |
|  | 通道6使能 更多... |
|  | |
| int | Channel6Brightness `[get, set]` |
|  | 通道6亮度，光源控制器：0~255；视觉控制器：0~100 更多... |
|  | |
| Channel6LightStateEnum | Channel6LightState `[get, set]` |
|  | 通道6光源状态 更多... |
|  | |
| Channel6EdgeTypeEnum | Channel6EdgeType `[get, set]` |
|  | 通道6沿定义 更多... |
|  | |
| int | Channel6DurationTime `[get, set]` |
|  | 持续时间(ms)，范围：[0,30000] 更多... |
|  | |
| bool | Channel7Enable `[get, set]` |
|  | 通道7使能 更多... |
|  | |
| int | Channel7Brightness `[get, set]` |
|  | 通道7亮度，光源控制器:0~255; 视觉控制器:0~100 更多... |
|  | |
| bool | Channel8Enable `[get, set]` |
|  | 通道8使能 更多... |
|  | |
| int | Channel8Brightness `[get, set]` |
|  | 通道8亮度，光源控制器:0~255; 视觉控制器:0~100 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 成员函数 继承自 CModuleParamBase | |
| int | GetParamValue (String strName, ref String strValue) |
|  | 获取参数值 更多... |
|  | |
| int | SetParamValue (String strName, String strValue) |
|  | 设置参数值 更多... |
|  | |
| int | GetBinaryData (String strName, IntPtr pBinData, uint nMemSize, ref uint nDataLen) |
|  | 获取二进制数据 更多... |
|  | |
| int | SetBinaryData (String strName, IntPtr pBinData, uint nDataLen) |
|  | 设置二进制数据 更多... |
|  | |
| void | SetInputInt (String strName, int[] anIntVal) |
|  | 设置整型输入 更多... |
|  | |
| void | SetInputFloat (String strName, float[] anFloatVal) |
|  | 设置浮点型输入 更多... |
|  | |
| void | SetInputString (String strName, InputStringData[] astStrData) |
|  | 设置字符串型输入 更多... |
|  | |
| void | SetInputImage (InputImageData stImageData) |
|  | 设置图像型输入 更多... |
|  | |
| void | SetInputBytes (String strName, BytesData stBytesData) |
|  | 设置二进制数据型输入 更多... |
|  | |

## 详细描述

光源参数

## 成员枚举类型说明

## ◆ OutputTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum OutputTypeEnum | | strong |

输出类型

| 枚举值 | |
| --- | --- |
| OK | OK时输出 |
| NG | NG时输出 |

## ◆ Channel1LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel1LightStateEnum | | strong |

通道1光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel1LightStateVBEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel1LightStateVBEnum | | strong |

通道1光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 常亮 |
| LightStateOff | 常灭 |

## ◆ Channel1EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel1EdgeTypeEnum | | strong |

通道1沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## ◆ Channel2LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel2LightStateEnum | | strong |

通道2光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel2LightStateVBEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel2LightStateVBEnum | | strong |

通道2光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 常亮 |
| LightStateOff | 常灭 |

## ◆ Channel2EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel2EdgeTypeEnum | | strong |

通道2沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## ◆ Channel3LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel3LightStateEnum | | strong |

通道3光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel3EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel3EdgeTypeEnum | | strong |

通道3沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## ◆ Channel4LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel4LightStateEnum | | strong |

通道4光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel4EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel4EdgeTypeEnum | | strong |

通道4沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## ◆ Channel5LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel5LightStateEnum | | strong |

通道5光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel5EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel5EdgeTypeEnum | | strong |

通道5沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## ◆ Channel6LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel6LightStateEnum | | strong |

通道6光源状态

| 枚举值 | |
| --- | --- |
| LightStateOn | 触发后亮（常灭） |
| LightStateOff | 触发后灭（常亮） |

## ◆ Channel6EdgeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum Channel6EdgeTypeEnum | | strong |

通道6沿定义

| 枚举值 | |
| --- | --- |
| EdgeTypeRising | 上升沿 |
| EdgeTypeFalling | 下降沿 |

## 属性说明

## ◆ InputChannel1Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel1Brightness | | set |

通道1亮度

**备注**

仅当次执行起效

## ◆ InputChannel2Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel2Brightness | | set |

通道2亮度

**备注**

仅当次执行起效

## ◆ InputChannel3Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel3Brightness | | set |

通道3亮度

**备注**

仅当次执行起效

## ◆ InputChannel4Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel4Brightness | | set |

通道4亮度

**备注**

仅当次执行起效

## ◆ InputChannel5Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel5Brightness | | set |

通道5亮度

**备注**

仅当次执行起效

## ◆ InputChannel6Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<int> InputChannel6Brightness | | set |

通道6亮度

**备注**

仅当次执行起效

## ◆ InputString

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> InputString | | set |

输入字符

**备注**

仅当次执行起效

## ◆ OutputType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | OutputTypeEnum OutputType | | getset |

输出类型

## ◆ TriggerTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TriggerTime | | getset |

触发时间(ms)，范围：[-1,65535]

## ◆ Channel1Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel1Enable | | getset |

通道1使能

## ◆ Channel1Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel1Brightness | | getset |

通道1亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel1LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel1LightStateEnum Channel1LightState | | getset |

通道1光源状态

## ◆ Channel1LightStateVB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel1LightStateVBEnum Channel1LightStateVB | | getset |

通道1光源状态

## ◆ Channel1EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel1EdgeTypeEnum Channel1EdgeType | | getset |

通道1沿定义

## ◆ Channel1DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel1DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel2Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel2Enable | | getset |

通道2使能

## ◆ Channel2Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel2Brightness | | getset |

通道2亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel2LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel2LightStateEnum Channel2LightState | | getset |

通道2光源状态

## ◆ Channel2LightStateVB

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel2LightStateVBEnum Channel2LightStateVB | | getset |

通道2光源状态

## ◆ Channel2EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel2EdgeTypeEnum Channel2EdgeType | | getset |

通道2沿定义

## ◆ Channel2DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel2DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel3Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel3Enable | | getset |

通道3使能

## ◆ Channel3Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel3Brightness | | getset |

通道3亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel3LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel3LightStateEnum Channel3LightState | | getset |

通道3光源状态

## ◆ Channel3EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel3EdgeTypeEnum Channel3EdgeType | | getset |

通道3沿定义

## ◆ Channel3DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel3DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel4Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel4Enable | | getset |

通道4使能

## ◆ Channel4Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel4Brightness | | getset |

通道4亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel4LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel4LightStateEnum Channel4LightState | | getset |

通道4光源状态

## ◆ Channel4EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel4EdgeTypeEnum Channel4EdgeType | | getset |

通道4沿定义

## ◆ Channel4DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel4DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel5Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel5Enable | | getset |

通道5使能

## ◆ Channel5Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel5Brightness | | getset |

通道5亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel5LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel5LightStateEnum Channel5LightState | | getset |

通道5光源状态

## ◆ Channel5EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel5EdgeTypeEnum Channel5EdgeType | | getset |

通道5沿定义

## ◆ Channel5DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel5DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel6Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel6Enable | | getset |

通道6使能

## ◆ Channel6Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel6Brightness | | getset |

通道6亮度，光源控制器：0~255；视觉控制器：0~100

## ◆ Channel6LightState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel6LightStateEnum Channel6LightState | | getset |

通道6光源状态

## ◆ Channel6EdgeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | Channel6EdgeTypeEnum Channel6EdgeType | | getset |

通道6沿定义

## ◆ Channel6DurationTime

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel6DurationTime | | getset |

持续时间(ms)，范围：[0,30000]

## ◆ Channel7Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel7Enable | | getset |

通道7使能

## ◆ Channel7Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel7Brightness | | getset |

通道7亮度，光源控制器:0~255; 视觉控制器:0~100

## ◆ Channel8Enable

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool Channel8Enable | | getset |

通道8使能

## ◆ Channel8Brightness

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int Channel8Brightness | | getset |

通道8亮度，光源控制器:0~255; 视觉控制器:0~100
