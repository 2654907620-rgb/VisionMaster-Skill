<!-- src:class_i_m_v_s_box_merge_modu_cs_1_1_box_merge_param.html -->
<!-- path:接口函数 > 拆分组合 > Box融合 > BoxMergeParam -->
# BoxMergeParam类 参考 拆分组合 » Box融合

Box融合参数
更多...

继承自 CModuleParamBase .

|  |  |
| --- | --- |
| Public 类型 | |
| enum | MergeMethodEnum {     Overlap = 0x1,     Distance = 0x2   } |
|  | 融合依据 更多... |
|  | |
| enum | BoxMergeTypeEnum {     MergeTypeFlawPriority = 0x1,     MergeTypeBoxLabel = 0x2,     MergeTypeNoBoxLabel = 0x3   } |
|  | Box融合类型 更多... |
|  | |
| enum | SplitCharEnum {     Dot = 0x1,     Colon = 0x2,     Semicolon = 0x3,     Underline = 0x4   } |
|  | 标签分割符 更多... |
|  | |
| enum | PrioritySortTypeEnum {     PrioritySortDescend = 0x1,     PrioritySortAscend = 0x2   } |
|  | 优先级排序 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| List< RectBox > | InputBOX `[set]` |
|  | 输入Box 更多... |
|  | |
| List< string > | BoxLabel `[set]` |
|  | Box标签 更多... |
|  | |
| List< string > | FlawPriority `[set]` |
|  | 缺陷优先级 更多... |
|  | |
| MergeMethodEnum | MergeMethod `[get, set]` |
|  | 融合依据 更多... |
|  | |
| int | OverlapThresh `[get, set]` |
|  | 重叠率，范围：[1,100] 更多... |
|  | |
| double | DxThresh `[get, set]` |
|  | X方向的距离，范围：[0,99999.9] 更多... |
|  | |
| double | DyThresh `[get, set]` |
|  | Y方向的距离，范围：[0,99999.9] 更多... |
|  | |
| BoxMergeTypeEnum | BoxMergeType `[get, set]` |
|  | Box融合类型 更多... |
|  | |
| SplitCharEnum | SplitChar `[get, set]` |
|  | 标签分割符 更多... |
|  | |
| PrioritySortTypeEnum | PrioritySortType `[get, set]` |
|  | 优先级排序 更多... |
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

Box融合参数

## 成员枚举类型说明

## ◆ MergeMethodEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum MergeMethodEnum | | strong |

融合依据

| 枚举值 | |
| --- | --- |
| Overlap | 重叠率 |
| Distance | Box中心之间的距离 |

## ◆ BoxMergeTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum BoxMergeTypeEnum | | strong |

Box融合类型

| 枚举值 | |
| --- | --- |
| MergeTypeFlawPriority | 无条件融合并按缺陷优先级输出标签 |
| MergeTypeBoxLabel | 按标签类别融合并输出标签 |
| MergeTypeNoBoxLabel | 无条件融合并随机输出标签 |

## ◆ SplitCharEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum SplitCharEnum | | strong |

标签分割符

| 枚举值 | |
| --- | --- |
| Dot | 逗号 |
| Colon | 冒号 |
| Semicolon | 分号 |
| Underline | 下划线 |

## ◆ PrioritySortTypeEnum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | enum PrioritySortTypeEnum | | strong |

优先级排序

| 枚举值 | |
| --- | --- |
| PrioritySortDescend | 降序 |
| PrioritySortAscend | 升序 |

## 属性说明

## ◆ InputBOX

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<RectBox> InputBOX | | set |

输入Box

**备注**

仅当次执行起效

## ◆ BoxLabel

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> BoxLabel | | set |

Box标签

**备注**

仅当次执行起效

## ◆ FlawPriority

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<string> FlawPriority | | set |

缺陷优先级

**备注**

仅当次执行起效

## ◆ MergeMethod

|  |  |  |
| --- | --- | --- |
| |  | | --- | | MergeMethodEnum MergeMethod | | getset |

融合依据

## ◆ OverlapThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int OverlapThresh | | getset |

重叠率，范围：[1,100]

## ◆ DxThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DxThresh | | getset |

X方向的距离，范围：[0,99999.9]

## ◆ DyThresh

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double DyThresh | | getset |

Y方向的距离，范围：[0,99999.9]

## ◆ BoxMergeType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | BoxMergeTypeEnum BoxMergeType | | getset |

Box融合类型

## ◆ SplitChar

|  |  |  |
| --- | --- | --- |
| |  | | --- | | SplitCharEnum SplitChar | | getset |

标签分割符

## ◆ PrioritySortType

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PrioritySortTypeEnum PrioritySortType | | getset |

优先级排序
