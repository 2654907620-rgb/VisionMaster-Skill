<!-- src:struct_procedure_run_policy.html -->
<!-- path:接口函数 > 公共模块 > 模块结果基类 > ProcedureRunPolicy -->
# ProcedureRunPolicy结构体 参考 公共模块 » 模块结果基类

用户自定义流程运行策略信息结构
更多...

|  |  |
| --- | --- |
| Public 属性 | |
| int | nThreadNum |
|  | 指定流程其执行线程数目 更多... |
|  | |
| byte [] | chCpuCore |
|  | 指定流程运行的CPU核心 CPU核数组，0-无效，1-有效。byCpuCore[0]表示cpu0、byCpuCore[1]表示cpu1，byCpuCore[2]表示cpu2... 更多... |
|  | |
| uint [] | nReserved |
|  | 保留字段 更多... |
|  | |

## 详细描述

用户自定义流程运行策略信息结构

## 类成员变量说明

## ◆ nThreadNum

|  |
| --- |
| int nThreadNum |

指定流程其执行线程数目

## ◆ chCpuCore

|  |
| --- |
| byte [] chCpuCore |

指定流程运行的CPU核心 CPU核数组，0-无效，1-有效。byCpuCore[0]表示cpu0、byCpuCore[1]表示cpu1，byCpuCore[2]表示cpu2...

## ◆ nReserved

|  |
| --- |
| uint [] nReserved |

保留字段
