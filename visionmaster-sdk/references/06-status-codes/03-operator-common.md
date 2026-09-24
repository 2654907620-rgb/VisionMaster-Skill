<!-- src:_xE9_x80_x9A_xE7_x94_xA8_xE7_x8A_xB6_xE6_x80_x81_xE7_xA0_x81.html | path:状态码 > 算子状态码（C#） > 通用状态码 -->
<!-- src:_xE9_x80_x9A_xE7_x94_xA8_xE7_x8A_xB6_xE6_x80_x81_xE7_xA0_x81.html -->
<!-- path:状态码 > 算子状态码（C#） > 通用状态码 -->
# 通用状态码

| 通用状态码定义：范围 0x80100000-0x801000FF。 | | |
| --- | --- | --- |
| 名称 | 值 | 说明 |
| MVD\_E\_HANDLE | 0x80100000 | 错误或无效的句柄 |
| MVD\_E\_SUPPORT | 0x80100001 | 不支持的功能 |
| MVD\_E\_OVER\_ABILITY | 0x80100002 | 超出限制的能力范围 |
| MVD\_E\_CALLORDER | 0x80100003 | 函数调用顺序错误 |
| MVD\_E\_PRECONDITION | 0x80100004 | 前置条件有误 |
| MVD\_E\_PARAMETER\_RANGE | 0x80100005 | 参数超出范围限制 |
| MVD\_E\_PARAMETER\_ILLEGAL | 0x80100006 | 参数非法 |
| MVD\_E\_PARAMETER\_MATCH | 0x80100007 | 参数互相不匹配 |
| MVD\_E\_PARAMETER\_GENERIC | 0x80100008 | 通用参数错误 |
| MVD\_E\_RESOURCE | 0x80100009 | 资源申请失败 |
| MVD\_E\_BUFOVER | 0x8010000A | 缓存已满 |
| MVD\_E\_NOOUTBUF | 0x8010000B | 没有可输出的缓存 |
| MVD\_E\_NOENOUGH\_BUF | 0x8010000C | 传入的内存空间不足 |
| MVD\_E\_FILE\_PATH | 0x8010000D | 不支持的文件路径 |
| MVD\_E\_FILE\_FORMAT | 0x8010000E | 不支持的文件格式 |
| MVD\_E\_FILE\_CORRUPTED | 0x8010000F | 文件损坏 |
| MVD\_E\_FILE\_GENERIC | 0x80100010 | 通用文件错误 |
| MVD\_E\_NODATA | 0x80100011 | 无数据 |
| MVD\_E\_ABNORMAL\_IMAGE | 0x80100012 | 异常图像 |
| MVD\_E\_VERSION | 0x80100013 | 版本不匹配 |
| MVD\_E\_LOAD\_LIBRARY | 0x80100014 | 动态导入DLL失败 |
| MVD\_E\_RUNTIME | 0x80100015 | 运行环境错误 |
| MVD\_E\_NO\_AVAILABLE\_DEVICE | 0x80100016 | 没有可用设备，不存在可用的显卡或者显卡驱动未更新 |
| MVD\_E\_MODEL\_TYPE | 0x80100017 | 模型类型错误 |
| MVD\_E\_MODEL\_VERSION | 0x80100018 | 模型版本错误 |
| MVD\_E\_MODEL\_ANALYSIS | 0x80100019 | 模型解析错误 |
| MVD\_E\_OUTOF\_MEMORY | 0x8010001A | 申请CPU内存失败 |
| MVD\_E\_OUTOF\_GPUMEMORY | 0x8010001B | 申请GPU内存失败 |
| MVD\_E\_ROI\_TYPE\_ERROR | 0x8010001C | ROI类型不支持 |
| MVD\_E\_ROI\_ANGLE\_ERROR | 0x8010001D | 不支持带角度的ROI |
| MVD\_E\_PARAM\_KEYNAME | 0x8010001E | 运行参数名有误 |
| MVD\_E\_MVDALGO\_DEV\_ENV | 0x8010001F | 环境变量配置不正确 |
| MVD\_E\_GET\_LOCK\_KEY | 0x80100020 | 获取加密狗Key失败 |
| MVD\_E\_DATA\_ENCRYPTION | 0x80100021 | 数据加密失败 |
| MVD\_E\_DATA\_DECRYPTION | 0x80100022 | 数据解密失败 |
| MVD\_E\_DATA\_PARSE | 0x80100023 | 数据解析失败 |
| MVD\_E\_GPU\_DEVICE | 0x80100024 | GPU设备操作错误 |
| MVD\_E\_ROI\_RANGE | 0x80100025 | ROI超出范围 |
| MVD\_E\_GPU\_COMPUTE\_CAPABILITY | 0x80100026 | GPU算力不足 |
| MVD\_E\_GPU\_DRIVER | 0x80100027 | GPU驱动版本不足或不支持 |
| MVD\_E\_MODEL\_DATA | 0x80100028 | 模型数据异常 |
| MVD\_E\_NO\_PRO\_LICENSE | 0x80100029 | 没有PRO授权许可 |
| MVD\_E\_UNKNOW | 0x801000FF | 未知的错误 |
| 算法处理流程相关:范围0x80100200-0x801002FF | | |
| 名称 | 值 | 说明 |
| MVALGORITHM\_E\_ALGORITHM | 0x80100201 | 算法版本错误 |
| MVALGORITHM\_E\_CONFIG | 0x80100202 | 算法配置错误 |
| MVALGORITHM\_E\_UNKNOW | 0x80100203 | 算法未知错误 |
| 字符缺陷检测算法相关 | | |
| 名称 | 值 | 说明 |
| MVALGORITHM\_E\_MKINSP\_ROUGH\_MATCH\_FAILED | 0x80100204 | 字符缺陷检测粗定位失败 |
| MVALGORITHM\_E\_MKINSP\_MODEL\_VERSION\_NOT\_SUPPORT | 0x80100205 | 字符缺陷检测模板版本号不支持 |
| 单点算子相关 标定转换失败错误码 | | |
| 名称 | 值 | 说明 |
| MVD\_E\_CALIBRATION\_DATA\_ERROR | 0x80100206 | 标定数据错误 |
| 渲染控件相关错误码 | | |
| 名称 | 值 | 说明 |
| MVD\_E\_RENDER\_IMG\_FORMAT | 0x80100301 | 图像像素格式不正确或者不支持 |
| MVD\_E\_RENDER\_IMG\_TYPE | 0x80100302 | 图像类型不支持或不正确 |
| MVD\_E\_RENDER\_IMG\_SIZE | 0x80100303 | 图像宽高不正确或者超出范围 |
| MVD\_E\_RENDER\_IMG\_ENCOD | 0x80100304 | 图像编解码失败 |
| MVD\_E\_RENDER\_CANVAS\_ZOOM | 0x80100305 | 画布缩放超出限制 |
| MVD\_E\_RENDER\_CANVAS\_PARAM | 0x80100306 | 画布大小范围非法 |
| MVD\_E\_RENDER\_GENERIC | 0x80100307 | 渲染引擎通用错误 |
| MVD\_E\_RENDER\_ILLEGAL\_SHAPE | 0x80100308 | 渲染引擎绘制范围有误的图形 |
| MVD\_E\_RENDER\_MEMORY | 0x80100309 | 渲染引擎画布拷贝错误 |
| MVD\_E\_RENDER\_HANDLD\_NOTFIND | 0x8010030A | 图像或图形句柄不存在或无效 |
