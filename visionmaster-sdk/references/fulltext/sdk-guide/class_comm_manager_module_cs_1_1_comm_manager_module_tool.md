<!-- src:class_comm_manager_module_cs_1_1_comm_manager_module_tool.html -->
<!-- path:接口函数 > 全局模块 > 通信管理 > CommManagerModuleTool -->
# CommManagerModuleTool类 参考 全局模块 » 通信管理

全局通信
更多...

继承自 VmModule .

|  |  |
| --- | --- |
| Public 成员函数 | |
| void | SetString (int nDeviceId, string strValue, int nAddressId=-1) |
|  | 设置字符串型数据 更多... |
|  | |
| void | SetInt (int nDeviceId, int[] nValue, int nAddressId=-1) |
|  | 设置整型数据 更多... |
|  | |
| void | SetFloat (int nDeviceId, float[] fValue, int nAddressId=-1) |
|  | 设置浮点型数据 更多... |
|  | |
| void | SetBytes (int nDeviceId, byte[] btValue, int nAddressId=-1) |
|  | 设置二进制型数据 更多... |
|  | |
| void | GetReadData (int nDeviceId, ref byte[] pData, int nDataSize=1024, int nAddressId=-1) |
|  | 获取读取数据 更多... |
|  | |
| bool | bIsDeviceConnect (int nDeviceId) |
|  | 通信设备是否处于连接状态 更多... |
|  | |
| string | GetParamValue (int nDeviceId, string strParamName, int nAddressId=-1) |
|  | 获取指定参数的参数值 更多... |
|  | |
| void | SetParamValue (int nDeviceId, string strParamName, string strValue, int nAddressId=-1) |
|  | 设置指定参数的参数值 更多... |
|  | |
| void | SetGlobalLightParam (GlobalLightParam stLightParam) |
|  | 设置全局光源参数信息 更多... |
|  | |
| Public 成员函数 继承自 VmModule | |
| void | EnableResultCallback () |
|  | 二次开发使用，开启模块结果回调 更多... |
|  | |

|  |  |
| --- | --- |
| 额外继承的成员函数 | |
| Public 属性 继承自 VmModule | |
| ModuResultMemoryTypeEnum | ModuResultMemType |
|  | 模块结果内存管理类型 更多... |
|  | |

## 详细描述

全局通信

## 成员函数说明

## ◆ SetString()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetString | ( | int | *nDeviceId*, |
|  |  | string | *strValue*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

设置字符串型数据

## ◆ SetInt()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetInt | ( | int | *nDeviceId*, |
|  |  | int [] | *nValue*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

设置整型数据

## ◆ SetFloat()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetFloat | ( | int | *nDeviceId*, |
|  |  | float [] | *fValue*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

设置浮点型数据

## ◆ SetBytes()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetBytes | ( | int | *nDeviceId*, |
|  |  | byte [] | *btValue*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

设置二进制型数据

## ◆ GetReadData()

|  |  |  |  |
| --- | --- | --- | --- |
| void GetReadData | ( | int | *nDeviceId*, |
|  |  | ref byte [] | *pData*, |
|  |  | int | *nDataSize* = `1024`, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

获取读取数据

## ◆ bIsDeviceConnect()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| bool bIsDeviceConnect | ( | int | *nDeviceId* | ) |  |

通信设备是否处于连接状态

## ◆ GetParamValue()

|  |  |  |  |
| --- | --- | --- | --- |
| string GetParamValue | ( | int | *nDeviceId*, |
|  |  | string | *strParamName*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

获取指定参数的参数值

## ◆ SetParamValue()

|  |  |  |  |
| --- | --- | --- | --- |
| void SetParamValue | ( | int | *nDeviceId*, |
|  |  | string | *strParamName*, |
|  |  | string | *strValue*, |
|  |  | int | *nAddressId* = `-1` |
|  | ) |  |  |

设置指定参数的参数值

## ◆ SetGlobalLightParam()

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| void SetGlobalLightParam | ( | GlobalLightParam | *stLightParam* | ) |  |

设置全局光源参数信息

**备注**

            异步接口，部分异常设置不返回错误
