<!-- src:class_i_m_v_s_cnn_register_anomaly_classification_modu_c_cs_1_1_result_filter_item_param.html -->
<!-- path:接口函数 > 边缘学习 > 异常分类CPU > ResultFilterItemParam -->
# ResultFilterItemParam类 参考 边缘学习 » 异常分类CPU

结果判断动态参数项
更多...

|  |  |
| --- | --- |
| Public 成员函数 | |
|  | ResultFilterItemParam () |
|  | CH: 构造函数 | EN: Constructor 更多... |
|  | |
|  | ResultFilterItemParam (ParamItem similarityLimitEnableItem, ParamItem similarityLimitLowItem, ParamItem similarityLimitHighItem, ParamItem categoryNameLimitEnableItem, ParamItem categoryNameLimitItem) |
|  | CH: 构造函数 | EN: Constructor 更多... |
|  | |

|  |  |
| --- | --- |
| 属性 | |
| bool | SimilarityLimitEnableValue `[get, set]` |
|  | 相似度判断 更多... |
|  | |
| double | SimilarityLimitLowValue `[get, set]` |
|  | 相似度范围下限 更多... |
|  | |
| double | SimilarityLimitHighValue `[get, set]` |
|  | 相似度范围上限 更多... |
|  | |
| bool | CategoryNameLimitEnableValue `[get, set]` |
|  | 类别名称判断 更多... |
|  | |
| string | CategoryNameLimitValue `[get, set]` |
|  | 类别名称 更多... |
|  | |

## 详细描述

结果判断动态参数项

## 构造及析构函数说明

## ◆ ResultFilterItemParam() [1/2]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ResultFilterItemParam | ( |  | ) |  |

CH: 构造函数 | EN: Constructor

## ◆ ResultFilterItemParam() [2/2]

|  |  |  |  |
| --- | --- | --- | --- |
| ResultFilterItemParam | ( | ParamItem | *similarityLimitEnableItem*, |
|  |  | ParamItem | *similarityLimitLowItem*, |
|  |  | ParamItem | *similarityLimitHighItem*, |
|  |  | ParamItem | *categoryNameLimitEnableItem*, |
|  |  | ParamItem | *categoryNameLimitItem* |
|  | ) |  |  |

CH: 构造函数 | EN: Constructor

## 属性说明

## ◆ SimilarityLimitEnableValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool SimilarityLimitEnableValue | | getset |

相似度判断

## ◆ SimilarityLimitLowValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SimilarityLimitLowValue | | getset |

相似度范围下限

## ◆ SimilarityLimitHighValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | double SimilarityLimitHighValue | | getset |

相似度范围上限

## ◆ CategoryNameLimitEnableValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | bool CategoryNameLimitEnableValue | | getset |

类别名称判断

## ◆ CategoryNameLimitValue

|  |  |  |
| --- | --- | --- |
| |  | | --- | | string CategoryNameLimitValue | | getset |

类别名称
