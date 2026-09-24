<!-- src:class_save_text_module_cs_1_1_save_text_param.html -->
<!-- path:接口函数 > 逻辑工具 > 文本保存 > SaveTextParam -->
# SaveTextParam类 参考 逻辑工具 » 文本保存

文本保存参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | OutputTypeEnum {     TXT = 0x0,     CSV = 0x1   } |
|  | 数据源 更多... |
|  | |
| enum | SaveConditionEnum {     ALL = 0x0,     OK = 0x1,     NG = 0x2,     NONE = 0x3   } |
|  | 保存条件 更多... |
|  | |
| enum | SaveTypeEnum {     OverWrite = 0x0,     NoSave = 0x1   } |
|  | 存储方式 更多... |
|  | |
| enum | NameTypeEnum {     Index = 0x0,     Time = 0x1,     None = 0x2   } |
|  | 文件命名 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| OutputTypeEnum | OutputType `[get, set]` |
|  | 数据源 更多... |
|  | |
| bool | SaveColumnNames `[get, set]` |
|  | 保存列名 更多... |
|  | |
| bool | SaveTrigger `[get, set]` |
|  | 触发保存 更多... |
|  | |
| SaveConditionEnum | SaveCondition `[get, set]` |
|  | 保存条件 更多... |
|  | |
| string | Path `[get, set]` |
|  | 保存路径 更多... |
|  | |
| int | FileCount `[get, set]` |
|  | 文件保存数量，范围：[1,65530] 更多... |
|  | |
| int | FileLen `[get, set]` |
|  | 文件容量(K)，范围：[100,10240] , Range:[100,10240] 更多... |
|  | |
| SaveTypeEnum | SaveType `[get, set]` |
|  | 存储方式 更多... |
|  | |
| string | TimeStamp `[get, set]` |
|  | 时间戳设置 更多... |
|  | |
| bool | SaveByDateTrigger `[get, set]` |
|  | 生成日期目录 更多... |
|  | |
| int | MaxDayCount `[get, set]` |
|  | 文件保存天数，范围：[1,500] 更多... |
|  | |
| NameTypeEnum | NameType `[get, set]` |
|  | 文件命名 更多... |
|  | |
| bool | RealTimeSave `[get, set]` |
|  | 实时存储 更多... |
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

文本保存参数

## 成员枚举类型说明

## ◆ OutputTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum OutputTypeEnum | | strong |

数据源

| 枚举值 | |
| --- | --- |
| TXT | TXT |
| CSV | CSV |

## ◆ SaveConditionEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SaveConditionEnum | | strong |

保存条件

| 枚举值 | |
| --- | --- |
| ALL | 全部保存 |
| OK | OK时保存 |
| NG | NG时保存 |
| NONE | 不保存 |

## ◆ SaveTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SaveTypeEnum | | strong |

存储方式

| 枚举值 | |
| --- | --- |
| OverWrite | 覆盖存储 |
| NoSave | 停止存储 |

## ◆ NameTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum NameTypeEnum | | strong |

文件命名

| 枚举值 | |
| --- | --- |
| Index | 序号 |
| Time | 时间 |
| None | 无 |

## 属性说明

## ◆ OutputType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | OutputTypeEnum OutputType | | getset |

数据源

## ◆ SaveColumnNames

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveColumnNames | | getset |

保存列名

## ◆ SaveTrigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveTrigger | | getset |

触发保存

## ◆ SaveCondition

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SaveConditionEnum SaveCondition | | getset |

保存条件

## ◆ Path

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string Path | | getset |

保存路径

## ◆ FileCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FileCount | | getset |

文件保存数量，范围：[1,65530]

## ◆ FileLen

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int FileLen | | getset |

文件容量(K)，范围：[100,10240] , Range:[100,10240]

## ◆ SaveType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SaveTypeEnum SaveType | | getset |

存储方式

## ◆ TimeStamp

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string TimeStamp | | getset |

时间戳设置

## ◆ SaveByDateTrigger

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SaveByDateTrigger | | getset |

生成日期目录

## ◆ MaxDayCount

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int MaxDayCount | | getset |

文件保存天数，范围：[1,500]

## ◆ NameType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | NameTypeEnum NameType | | getset |

文件命名

## ◆ RealTimeSave

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool RealTimeSave | | getset |

实时存储
