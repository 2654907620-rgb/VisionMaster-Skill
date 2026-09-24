<!-- src:group___xE6_x8E_xA7_xE5_x88_xB6_xE5_x99_xA8_xE7_xAE_xA1_xE7_x90_x86.html -->
<!-- path:接口函数 > 全局模块 > 控制器管理 -->
# 控制器管理 全局模块

控制器管理可管理所有光源以及IO模块。
更多...

|  |  |
| --- | --- |
| 类 | |
| struct | LightChannelInfo |
|  | 光源控制信息结构 更多... |
|  | |
| struct | LightConfigInfo |
|  | 各通道光源控制信息结构 更多... |
|  | |
| struct | GlobalLightParam |
|  | 各通道光源控制信息结构 更多... |
|  | |
| class | LightControlTool |
|  | 全局光源 更多... |
|  | |

|  |  |
| --- | --- |
| 枚举 | |
| enum | DeviceTypeEnum {     TYPE\_NONE = 0x00000000,     TYPE\_LIGHT\_CONTROLLER = 0x00001004,     TYPE\_VB2200 = 0x00440101,     TYPE\_VB2230 = 0x00440102,     TYPE\_VC4000 = 0x00880204,     TYPE\_VC3000\_LIGHT = 0x00000204,     TYPE\_VC3000\_IO = 0x00880000,     TYPE\_VC3000\_GPIO = 0x00380000,     TYPE\_VC2000 = 0x01880204,     TYPE\_IN\_COMM\_LIGHT\_4C = 101,     TYPE\_IN\_COMM\_LIGHT\_6C = 102,     TYPE\_IN\_COMM\_VB2200 = 103,     TYPE\_IN\_COMM\_VB2230 = 104,     TYPE\_IN\_COMM\_VC2000 = 105,     TYPE\_IN\_COMM\_VC3000\_IO = 106,     TYPE\_IN\_COMM\_VC3000\_LIGHT = 107,     TYPE\_IN\_COMM\_GPIO = 108,     TYPE\_IN\_COMM\_VC3000H = 109,     TYPE\_IN\_COMM\_VC4000 = 110   } |
|  | 设备类型 更多... |
|  | |
| enum | TriggerEdgeEnum {     MV\_IO\_EDGE\_UNKNOW = 0x00,     MV\_IO\_EDGE\_RISING = 0x01,     MV\_IO\_EDGE\_FALLING = 0x02   } |
|  | 沿定义，用户表示输入信号的触发 更多... |
|  | |
| enum | LightStateEnum {     MV\_IO\_LIGHTSTATE\_ON = 0x0001,     MV\_IO\_LIGHTSTATE\_OFF = 0x0002   } |
|  | 光源常亮常灭 更多... |
|  | |

## 详细描述

控制器管理可管理所有光源以及IO模块。

## 枚举类型说明

## ◆ DeviceTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum DeviceTypeEnum | | strong |

设备类型

**备注**

            V4.3之前版本原有控制器管理使用TYPE\_开头部分

            V4.4版本新增通信管理-控制器管理使用TYPE\_IN\_COMM\_开头部分

| 枚举值 | |
| --- | --- |
| TYPE\_NONE |  |
| TYPE\_LIGHT\_CONTROLLER | 光源控制器 |
| TYPE\_VB2200 | VB2200 |
| TYPE\_VB2230 | VB2230 |
| TYPE\_VC4000 | VC4000 |
| TYPE\_VC3000\_LIGHT | VC3000\_LIGHT |
| TYPE\_VC3000\_IO | VC3000\_IO |
| TYPE\_VC3000\_GPIO | VC3000\_GPIO |
| TYPE\_VC2000 | VC2000 |
| TYPE\_IN\_COMM\_LIGHT\_4C | LIGHT\_4C |
| TYPE\_IN\_COMM\_LIGHT\_6C | LIGHT\_6C |
| TYPE\_IN\_COMM\_VB2200 | VB2200 |
| TYPE\_IN\_COMM\_VB2230 | VB2230 |
| TYPE\_IN\_COMM\_VC2000 | VC2000 |
| TYPE\_IN\_COMM\_VC3000\_IO | VC3000\_IO |
| TYPE\_IN\_COMM\_VC3000\_LIGHT | VC3000\_LIGHT |
| TYPE\_IN\_COMM\_GPIO | VC3000\_GPIO |
| TYPE\_IN\_COMM\_VC3000H | VC3000H |
| TYPE\_IN\_COMM\_VC4000 | VC4000 |

## ◆ TriggerEdgeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum TriggerEdgeEnum | | strong |

沿定义，用户表示输入信号的触发

| 枚举值 | |
| --- | --- |
| MV\_IO\_EDGE\_UNKNOW |  |
| MV\_IO\_EDGE\_RISING | 上升沿 |
| MV\_IO\_EDGE\_FALLING | 下降沿 |

## ◆ LightStateEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum LightStateEnum | | strong |

光源常亮常灭

| 枚举值 | |
| --- | --- |
| MV\_IO\_LIGHTSTATE\_ON | 触发后常亮 |
| MV\_IO\_LIGHTSTATE\_OFF | 触发后常灭 |
