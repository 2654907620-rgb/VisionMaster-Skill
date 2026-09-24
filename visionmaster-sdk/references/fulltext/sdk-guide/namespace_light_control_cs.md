<!-- src:namespace_light_control_cs.html -->
# LightControlCs 命名空间参考

|  |  |
| --- | --- |
| 类 | |
| struct | GlobalLightParam |
|  | 各通道光源控制信息结构 更多... |
|  | |
| struct | LightChannelInfo |
|  | 光源控制信息结构 更多... |
|  | |
| struct | LightConfigInfo |
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
