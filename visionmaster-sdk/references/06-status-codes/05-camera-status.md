<!-- src:_xE7_x9B_xB8_xE6_x9C_xBA_xE7_x9B_xB8_xE5_x85_xB3_xE7_x8A_xB6_xE6_x80_x81_xE7_xA0_x81.html | path:状态码 > 算子状态码（C#） > 相机相关状态码 -->
<!-- src:_xE7_x9B_xB8_xE6_x9C_xBA_xE7_x9B_xB8_xE5_x85_xB3_xE7_x8A_xB6_xE6_x80_x81_xE7_xA0_x81.html -->
<!-- path:状态码 > 算子状态码（C#） > 相机相关状态码 -->
# 相机相关状态码

| 通用错误码定义:范围0x80000000-0x800000FF | | |
| --- | --- | --- |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_HANDLE | 0x80000000 | 错误或无效的句柄 |
| MVD\_CAM\_E\_SUPPORT | 0x80000001 | 不支持的功能 |
| MVD\_CAM\_E\_BUFOVER | 0x80000002 | 缓存已满 |
| MVD\_CAM\_E\_CALLORDER | 0x80000003 | 函数调用顺序错误 |
| MVD\_CAM\_E\_PARAMETER | 0x80000004 | 错误的参数 |
| MVD\_CAM\_E\_RESOURCE | 0x80000006 | 资源申请失败 |
| MVD\_CAM\_E\_NODATA | 0x80000007 | 无数据 |
| MVD\_CAM\_E\_PRECONDITION | 0x80000008 | 前置条件有误，或运行环境已发生变化 |
| MVD\_CAM\_E\_VERSION | 0x80000009 | 版本不匹配 |
| MVD\_CAM\_E\_NOENOUGH\_BUF | 0x8000000A | 传入的内存空间不足 |
| MVD\_CAM\_E\_ABNORMAL\_IMAGE | 0x8000000B | 异常图像，可能是丢包导致图像不完整 |
| MVD\_CAM\_E\_LOAD\_LIBRARY | 0x8000000C | 动态导入DLL失败 |
| MVD\_CAM\_E\_NOOUTBUF | 0x8000000D | 没有可输出的缓存 |
| MVD\_CAM\_E\_UNKNOW | 0x800000FF | 未知的错误 |
| GenICam系列错误:范围0x80000100-0x800001FF | | |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_GC\_GENERIC | 0x80000100 | 通用错误 |
| MVD\_CAM\_E\_GC\_ARGUMENT | 0x80000101 | 参数非法 |
| MVD\_CAM\_E\_GC\_RANGE | 0x80000102 | 值超出范围 |
| MVD\_CAM\_E\_GC\_PROPERTY | 0x80000103 | 属性 |
| MVD\_CAM\_E\_GC\_RUNTIME | 0x80000104 | 运行环境有问题 |
| MVD\_CAM\_E\_GC\_LOGICAL | 0x80000105 | 逻辑错误 |
| MVD\_CAM\_E\_GC\_ACCESS | 0x80000106 | 节点访问条件有误 |
| MVD\_CAM\_E\_GC\_TIMEOUT | 0x80000107 | 超时 |
| MVD\_CAM\_E\_GC\_DYNAMICCAST | 0x80000108 | 转换异常 |
| MVD\_CAM\_E\_GC\_UNKNOW | 0x800001FF | GenICam未知错误 |
| GigE\_STATUS对应的错误码:范围0x80000200-0x800002FF | | |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_NOT\_IMPLEMENTED | 0x80000200 | 命令不被设备支持 |
| MVD\_CAM\_E\_INVALID\_ADDRESS | 0x80000201 | 访问的目标地址不存在 |
| MVD\_CAM\_E\_WRITE\_PROTECT | 0x80000202 | 目标地址不可写 |
| MVD\_CAM\_E\_ACCESS\_DENIED | 0x80000203 | 设备无访问权限 |
| MVD\_CAM\_E\_BUSY | 0x80000204 | 设备忙，或网络断开 |
| MVD\_CAM\_E\_PACKET | 0x80000205 | 网络包数据错误 |
| MVD\_CAM\_E\_NETER | 0x80000206 | 网络相关错误 |
| GigE相机特有的错误码 | | |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_IP\_CONFLICT | 0x80000221 | 设备IP冲突 |
| USB\_STATUS对应的错误码:范围0x80000300-0x800003FF | | |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_USB\_READ | 0x80000300 | 读usb出错 |
| MVD\_CAM\_E\_USB\_WRITE | 0x80000301 | 写usb出错 |
| MVD\_CAM\_E\_USB\_DEVICE | 0x80000302 | 设备异常 |
| MVD\_CAM\_E\_USB\_GENICAM | 0x80000303 | GenICam相关错误 |
| MVD\_CAM\_E\_USB\_BANDWIDTH | 0x80000304 | 带宽不足 该错误码新增 |
| MVD\_CAM\_E\_USB\_DRIVER | 0x80000305 | 驱动不匹配或者未装驱动 |
| MVD\_CAM\_E\_USB\_UNKNOW | 0x800003FF | USB未知的错误 |
| 升级时对应的错误码:范围0x80000400-0x800004FF | | |
| 名称 | 值 | 说明 |
| MVD\_CAM\_E\_UPG\_FILE\_MISMATCH | 0x80000400 | 升级固件不匹配 |
| MVD\_CAM\_E\_UPG\_LANGUSGE\_MISMATCH | 0x80000401 | 升级固件语言不匹配 |
| MVD\_CAM\_E\_UPG\_CONFLICT | 0x80000402 | 升级冲突（设备已经在升级了再次请求升级即返回此错误） |
| MVD\_CAM\_E\_UPG\_INNER\_ERR | 0x80000403 | 升级时相机内部出现错误 |
| MVD\_CAM\_E\_UPG\_UNKNOW | 0x800004FF | 升级时未知错误 |
