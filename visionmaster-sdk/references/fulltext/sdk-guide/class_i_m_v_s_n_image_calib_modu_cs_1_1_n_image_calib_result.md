<!-- src:class_i_m_v_s_n_image_calib_modu_cs_1_1_n_image_calib_result.html -->
<!-- path:接口函数 > 标定 > N图像标定 > NImageCalibResult -->
# NImageCalibResult类 参考 标定 » N图像标定

N图像标定结果
更多...

继承自 CModuleResultBase .

|  |  |
| --- | --- |
| 属性 | |
| int | ModuStatus `[get]` |
|  | 模块状态 更多... |
|  | |
| int | CalibStatus `[get]` |
|  | 标定状态 更多... |
|  | |
| int | CalibErrStatus `[get]` |
|  | 评估标定误差状态 更多... |
|  | |
| int | RotDirectState `[get]` |
|  | 旋转方向 更多... |
|  | |
| int | CornerPairsNum `[get]` |
|  | 信息数量 更多... |
|  | |
| List< PointF > | CalibImagePoint `[get]` |
|  | 标定图像点 更多... |
|  | |
| float | TransError `[get]` |
|  | 平移像素平均误差 更多... |
|  | |
| float | TransEstMax `[get]` |
|  | 平移像素最大误差 更多... |
|  | |
| int | TransErrMaxPtsNum `[get]` |
|  | 平移像素最大误差对应点数 更多... |
|  | |
| float | TransWorldError `[get]` |
|  | 平移估计真实误差 更多... |
|  | |
| float | TransErrWorldMax `[get]` |
|  | 平移像素真实最大误差 更多... |
|  | |
| float | RotError `[get]` |
|  | 旋转像素平均误差 更多... |
|  | |
| float | RotErrMax `[get]` |
|  | 旋转像素最大误差 更多... |
|  | |
| int | RotErrMaxPtsNum `[get]` |
|  | 旋转像素最大误差对应点数 更多... |
|  | |
| float | RotWorldError `[get]` |
|  | 旋转真实平均误差 更多... |
|  | |
| float | RotErrWorldMax `[get]` |
|  | 旋转真实最大误差 更多... |
|  | |
| int | TransMotionErrPicIndex `[get]` |
|  | 机构平移最大误差所在图片索引 更多... |
|  | |
| float | TransMotionErrAvgTrans `[get]` |
|  | 机构平移图像移动量与机构移动量偏差 更多... |
|  | |
| float | TransMotionErrAvgScale `[get]` |
|  | 机构平移图像尺度变化 更多... |
|  | |
| float | TransMotionErrAvgRotate `[get]` |
|  | 机构平移图像之间旋转变化量 更多... |
|  | |
| float | TransMotionErrMaxTrans `[get]` |
|  | 机构平移最大误差距离误差 更多... |
|  | |
| float | TransMotionErrMaxScale `[get]` |
|  | 机构平移最大误差图像尺度变化 更多... |
|  | |
| float | TransMotionErrMaxRotate `[get]` |
|  | 机构平移最大误差图像之间旋转变化量 更多... |
|  | |
| float | RotMotionErrAvg `[get]` |
|  | 机构旋转平均误差 更多... |
|  | |
| float | RotMotionErrMax `[get]` |
|  | 机构旋转最大误差 更多... |
|  | |
| int | RotMotionErrPicIndex `[get]` |
|  | 机构旋转最大误差所在图片索引 更多... |
|  | |
| PointF | RotateCenterPoint `[get]` |
|  | 旋转中心坐标 更多... |
|  | |
| PointF | DirectionXVectorPoint `[get]` |
|  | x方向向量 更多... |
|  | |
| PointF | DirectionYVectorPoint `[get]` |
|  | y方向向量 更多... |
|  | |
| float | MoveDirec `[get]` |
|  | y方向和x方向移动比 更多... |
|  | |
| int | CurNum `[get]` |
|  | 当前图像个数 更多... |
|  | |
| int | TotalNum `[get]` |
|  | 图像总个数 更多... |
|  | |
| 属性 继承自 CModuleResultBase | |
| uint | ErrorCode `[get]` |
|  | 错误码 更多... |
|  | |
| float | ModuRunTime `[get]` |
|  | 模块执行耗时 更多... |
|  | |

## 详细描述

N图像标定结果

## 属性说明

## ◆ ModuStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int ModuStatus | | get |

模块状态

## ◆ CalibStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibStatus | | get |

标定状态

## ◆ CalibErrStatus

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CalibErrStatus | | get |

评估标定误差状态

## ◆ RotDirectState

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotDirectState | | get |

旋转方向

## ◆ CornerPairsNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CornerPairsNum | | get |

信息数量

## ◆ CalibImagePoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | List<PointF> CalibImagePoint | | get |

标定图像点

## ◆ TransError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransError | | get |

平移像素平均误差

## ◆ TransEstMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransEstMax | | get |

平移像素最大误差

## ◆ TransErrMaxPtsNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TransErrMaxPtsNum | | get |

平移像素最大误差对应点数

## ◆ TransWorldError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransWorldError | | get |

平移估计真实误差

## ◆ TransErrWorldMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransErrWorldMax | | get |

平移像素真实最大误差

## ◆ RotError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotError | | get |

旋转像素平均误差

## ◆ RotErrMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotErrMax | | get |

旋转像素最大误差

## ◆ RotErrMaxPtsNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotErrMaxPtsNum | | get |

旋转像素最大误差对应点数

## ◆ RotWorldError

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotWorldError | | get |

旋转真实平均误差

## ◆ RotErrWorldMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotErrWorldMax | | get |

旋转真实最大误差

## ◆ TransMotionErrPicIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TransMotionErrPicIndex | | get |

机构平移最大误差所在图片索引

## ◆ TransMotionErrAvgTrans

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrAvgTrans | | get |

机构平移图像移动量与机构移动量偏差

## ◆ TransMotionErrAvgScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrAvgScale | | get |

机构平移图像尺度变化

## ◆ TransMotionErrAvgRotate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrAvgRotate | | get |

机构平移图像之间旋转变化量

## ◆ TransMotionErrMaxTrans

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrMaxTrans | | get |

机构平移最大误差距离误差

## ◆ TransMotionErrMaxScale

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrMaxScale | | get |

机构平移最大误差图像尺度变化

## ◆ TransMotionErrMaxRotate

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float TransMotionErrMaxRotate | | get |

机构平移最大误差图像之间旋转变化量

## ◆ RotMotionErrAvg

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotMotionErrAvg | | get |

机构旋转平均误差

## ◆ RotMotionErrMax

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float RotMotionErrMax | | get |

机构旋转最大误差

## ◆ RotMotionErrPicIndex

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int RotMotionErrPicIndex | | get |

机构旋转最大误差所在图片索引

## ◆ RotateCenterPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF RotateCenterPoint | | get |

旋转中心坐标

## ◆ DirectionXVectorPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF DirectionXVectorPoint | | get |

x方向向量

## ◆ DirectionYVectorPoint

|  |  |  |
| --- | --- | --- |
| |  | | --- | | PointF DirectionYVectorPoint | | get |

y方向向量

## ◆ MoveDirec

|  |  |  |
| --- | --- | --- |
| |  | | --- | | float MoveDirec | | get |

y方向和x方向移动比

## ◆ CurNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int CurNum | | get |

当前图像个数

## ◆ TotalNum

|  |  |  |
| --- | --- | --- |
| |  | | --- | | int TotalNum | | get |

图像总个数
