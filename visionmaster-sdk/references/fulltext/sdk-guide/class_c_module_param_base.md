<!-- src:class_c_module_param_base.html -->
<!-- path:接口函数 > 公共模块 > 模块参数基类 > CModuleParamBase -->
# CModuleParamBase类 参考 公共模块 » 模块参数基类

模块参数基类
更多...

被 AndParam, BranchParam, BranchStringParam, CalculatorParam, CameraIOParam, CoordinateParam, CoordinateTransformParam, DataAnalysisParam, DataAssembleParam, DataClassificationParam, DataFilterParam, DataQueueParam, DataRecordParam, DataSetParam, DataSortParam, FormatParam, GeometryCreateParam, GlobalCameraParam, GraphicsSetParam, IfBranchParam, IfParam, ImageAcquisitionParam, ImageBufferParam, ImageSourceParam, Array2dCorrectParam, Bcr2dParam, AffineTransformParam, AngleBisectorFindParam, BcrParam, ImageBinaryParam, BlobFindLabelsParam, BlobFindParam, BoxFilterParam, BoxMergeParam, BoxOverlapCalculationParam, C2CMeasureParam, CalibBoardCalibParam, CalibTransformParam, CaliperCornerParam, CaliperEdgeParam, CaliperParam, CameraMapParam, CircleEdgeInspParam, CircleEdgePairInspParam, CircleFindParam, CircleFitParam, CnnCharDetectCParam, CnnCharDetectParam, CnnClassifyCParam, CnnClassifyParam, CnnCodeRecgCParam, CnnCodeRecgParam, CnnDetectCParam, CnnDetectParam, CnnFastFlawParam, CnnFlawCParam, CnnFlawParam, CnnHPRegisterDetectCParam, CnnHPRegisterDetectParam, CnnInspectCParam, CnnInspectParam, CnnInstanceSegmentCParam, CnnInstanceSegmentParam, CnnRegisterAnomalyClassificationCParam, CnnRegisterAnomalyClassificationParam, CnnRegisterClassifyCParam, CnnRegisterClassifyParam, CnnRegisterDetectCParam, CnnRegisterDetectParam, CnnRegisterMulticlassClassificationCParam, CnnRegisterMulticlassClassificationParam, CnnRegisterObjectCountCParam, CnnRegisterObjectCountParam, CnnRegisterPresenceDetectCParam, CnnRegisterPresenceDetectParam, CnnRegisterSegmentCParam, CnnRegisterSegmentParam, CnnRetrievalCParam, CnnRetrievalParam, CnnSingleCharDetectCParam, CnnSingleCharDetectParam, CnnUnSupervisedClassifyParam, CnnUnSupervisedParam, ColorExtractParam, ColorImageGenerationParam, ColorMeasureParam, ColorRecognitionParam, ColorSegmentParam, ColorTransformParam, ContourMatchParam, DivideImageParam, EdgeFlawInspParam, EdgeInspGroupParam, EdgePairFlawInspParam, EdgePairInspGroupParam, EdgePairPosTrendAnalyParam, EdgePosTrendAnalyParam, EdgeWidthFindParam, EllipseFindParam, EllipseFitParam, FastFeatureMatchParam, FixtureParam, FrameMeanParam, GeometricTransformParam, GluePathConductParam, GrayMatchParam, GrayMatchVAParam, GroupParam, HistToolParam, HPFeatureMatchParam, ImageCalibParam, ImageCombineProcessParam, ImageCorrectCalibParam, ImageCorrectManualParam, ImageEnhanceParam, ImageFilterParam, ImageFixtureParam, ImageMathParam, ImageMorphParam, ImageNormlizeParam, ImageResizeParam, ImageSharpnessParam, ImgStitchCalibParam, InspectParam, IntensityMeasureParam, InverseAffineTransformParam, L2CMeasureParam, L2LMeasureParam, LineAlignParam, LineEdgeInspParam, LineEdgePairInspParam, LineFindGroupParam, LineFindParam, LineFitParam, MachineLearningClassifierParam, MapCalibParam, MarkFindParam, MarkInspParam, MarkInspVAParam, MaskToolParam, MatrixCircleFindParam, MedianLineFindParam, MultiImageFusionParam, MultiLabelFilterParam, MultiLineFindParam, MultiPointAlignParam, NImageCalibParam, NPointCalibParam, OcrDlCParam, OcrDlParam, OcrParam, P2CMeasureParam, P2LMeasureParam, P2PMeasureParam, PairLineParam, ParallelCalculateParam, PeakFindParam, PixelCountParam, PixelCountVAParam, PolarUnwarpParam, QuadrangleFindParam, RectFindParam, RegionCopyParam, RotateCalculateParam, ScaleTransformParam, ShadeCorrectParam, SinglePointAlignParam, SurfaceDefectFilterParam, TargetTrackParam, VerticalLineFindParam, LightParam, PointSetParam, ProcedureParam, PyShellParam, ReadCalibFileParam, ReadDatasParam, RotateCalibParam, SaveImageParam, SaveTextParam, SendDatasParam, ShellParam, SinglePointGrabParam, SinglePointMapAlignParam, SinglePointRectifyParam, StringCompareParam, TimeStatisticParam, TranslationCalibParam , 以及 TriggerParam 继承.

|  |  |
| --- | --- |
| Public 成员函数 | |
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

模块参数基类

## 成员函数说明

## ◆ GetParamValue()

|  |  |  |  |
| --- | --- | --- | --- |
| int GetParamValue | ( | String | *strName*, |
|  |  | ref String | *strValue* |
|  | ) |  |  |

获取参数值

## ◆ SetParamValue()

|  |  |  |  |
| --- | --- | --- | --- |
| int SetParamValue | ( | String | *strName*, |
|  |  | String | *strValue* |
|  | ) |  |  |

设置参数值

## ◆ GetBinaryData()

|  |  |  |  |
| --- | --- | --- | --- |
| int GetBinaryData | ( | String | *strName*, |
|  |  | IntPtr | *pBinData*, |
|  |  | uint | *nMemSize*, |
|  |  | ref uint | *nDataLen* |
|  | ) |  |  |

获取二进制数据

## ◆ SetBinaryData()

|  |  |  |  |
| --- | --- | --- | --- |
| int SetBinaryData | ( | String | *strName*, |
|  |  | IntPtr | *pBinData*, |
|  |  | uint | *nDataLen* |
|  | ) |  |  |

设置二进制数据

## ◆ SetInputInt()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputInt | ( | String | *strName*, |
|  |  | int [] | *anIntVal* |
|  | ) |  |  |

设置整型输入

## ◆ SetInputFloat()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputFloat | ( | String | *strName*, |
|  |  | float [] | *anFloatVal* |
|  | ) |  |  |

设置浮点型输入

## ◆ SetInputString()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputString | ( | String | *strName*, |
|  |  | InputStringData [] | *astStrData* |
|  | ) |  |  |

设置字符串型输入

## ◆ SetInputImage()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetInputImage | ( | InputImageData | *stImageData* | ) |  |

设置图像型输入

## ◆ SetInputBytes()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInputBytes | ( | String | *strName*, |
|  |  | BytesData | *stBytesData* |
|  | ) |  |  |

设置二进制数据型输入
