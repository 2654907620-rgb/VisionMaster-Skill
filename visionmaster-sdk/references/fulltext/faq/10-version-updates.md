# 专题·版本更新（多版本切换 / 4.2 / 4.3 更新说明）
<!-- pdf pages 1298-1400 -->

<!-- page 1298 -->
HIKROBOT 
 
1289 
 
 
不熟悉算法模块图像转其它类型  
4 版本更新 
4.1 多版本间切换及二次开发程序升级  
描述  
环境：VM4.2 + VS2013 及以上  
现象：电脑上安装完VM4.0 或VM4.1 之后（本篇文章主要以VM4.0 为例，VM4.1 二次
开发程序升级与VM4.0 操作相同），安装VM4.2，因此电脑上可能有两个及两个以上的
VM 版本，此时，客户则有版本间切换的需求，或者需求 VM4.0 二次开发程序升级为V
M4.2 二次开发程序。 
解答  
针对这些需求，VM4.2 开始提供了相应的工具。 
1、版本安装。例如电脑安装完VM4.0 之后，再安装VM4.2，算子路径默认在C 盘，此
时算子安装路径会自动备份VM4.0 的算子。如下图所示，VM3.4 就是备份VM4.0 的算子
的文件夹，有这个文件夹才能进行版本间切换。  



<!-- page 1299 -->
HIKROBOT 
 
1290 
 
 
 
2、版本间切换。版本切换工具是VM4.2 新增，老版本并没有对应的处理工具。  
版本切换工具路径：VisionMaster4.2.0\Applications\Tools\VersionSwitchAssistant\V
ersionSwitchAssistant.exe；启动后会根据注册表查找已安装版本，根据需要切换即可，
切换前需要关闭VM 后台程序和Visual Studio 软件。从VM4.2 切换到VM4.0 之后，算
子路径中自动会将VM4.0 的算子从V3.4 文件夹中拷贝出来，将VM4.2 的算子打包到V4.
2 文件夹中。 当安装了多版本无法定位VM 问题时，也可以使用版本切换工具，点击【清
除配置】，然后再点击相应版本。  



<!-- page 1300 -->
HIKROBOT 
 
1291 
 
 
 
3、二次开发程序升级。针对基于C#进行VM 二次开发程序，当客户需求不再使用VM4.
0 时，需要将之前VM4.0 的二次开发程序升级到VM4.2 二次开发程序时。 
首先，使用工具将项目debug 文件夹中的内容进行备份，备份工具：VisionMaster4.2.0\
Applications\Tools\4.0 二次开发程序升级4.2 版本工具\DevelopProcedureUpgradeT
ool.exe，这一步操作则是因为VM4.2 二次开发环境不需要拷贝VM 提供的二次开发dl
l，因此要清空项目生成路径debug 文件夹，将VM 提供的二次开发dll 备份到另一个文
件夹中。  



<!-- page 1301 -->
HIKROBOT 
 
1292 
 
 
 
然后，使用引用工具为程序添加引用，引用工具：VisionMaster4.2.0\Development\V4.
x\ComControls\Tool\ImportRef.exe。至此就快速的完成了VM4.0 二次开发程序到VM
4.2 二次开发程序的升级。 



<!-- page 1302 -->
HIKROBOT 
 
1293 
 
 
 
4、方案、流程升级。方案、流程升级。程序升级成功之后，用户则启动VM4.2 二次开发
程序，加载方案时会报错，此时则需要用VM4.2 去打开用VM4.0 搭建的方案或流程，进
行一个升级，升级成功会有提示窗口，并将方案另存为xxx_V4.2.sol 等，特殊情况有些模
块、有些参数或全局变量需要检查并微调。   
5、注意事项  
（1）VM4.x 二次开发程序启动的前提之一，VM4.x 能够正常打开且方案能够正常运行，
然后关闭VM 后台程序，启动二次开发程序；  



<!-- page 1303 -->
HIKROBOT 
 
1294 
 
 
（2）VM4.2 二次开发某些接口名称发生变化，基本上是兼容VM4.0 二次开发接口，但推
荐使用程序中提示的推荐接口，例如获取流程结果就需要修改一下代码；  
（3）用户将VM 控件封装到一个项目1 中，然后在项目2 中调用项目1，此时项目1 也
需要进行二次开发程序升级操作。  
（4）安装VM4.0 后再安装VM4.2 后，4.0 的算子会被备份。此时如果卸载VM4.2，算
子路径会清空VM4.2 的算子以及VM4.0 备份的算子，此时VM4.0 无法将无法使用。此
时如果想使用VM4.0，删除VM4.2 的时候，卸载项不勾选（加密狗驱动，相机sdk），
再手动安装一下VM4.0 的算子包，算子包路径VisionMaster4.x\Drivers\MVSAlgorith
mSDK_STD.exe。  
（5）针对基于C++进行VM 二次开发的程序，由于不需要拷贝DLL，所以除了更改包含
目录和库目录路径，还需要删除项目exe 生成路径下VM 相关dll。  
（6）版本切换和升级是VM4.2 新增功能。VMSDK 程序升级步骤，主要针对VM 4.0
和VM4.1 版本的二次开发程序的升级。  
问题根因  
不熟悉的多版本间切换及二次开发程序升级  
 
 



<!-- page 1304 -->
HIKROBOT 
 
1295 
 
 
4.2 VM4.2 应用更新介绍 
 
 



<!-- page 1305 -->
HIKROBOT 
 
1296 
 
 
 
 



<!-- page 1306 -->
HIKROBOT 
 
1297 
 
 
 
 



<!-- page 1307 -->
HIKROBOT 
 
1298 
 
 
 
 



<!-- page 1308 -->
HIKROBOT 
 
1299 
 
 
 
 



<!-- page 1309 -->
HIKROBOT 
 
1300 
 
 
 
 



<!-- page 1310 -->
HIKROBOT 
 
1301 
 
 
 
 



<!-- page 1311 -->
HIKROBOT 
 
1302 
 
 
 
 



<!-- page 1312 -->
HIKROBOT 
 
1303 
 
 
 
 



<!-- page 1313 -->
HIKROBOT 
 
1304 
 
 
 
 



<!-- page 1314 -->
HIKROBOT 
 
1305 
 
 
 
 



<!-- page 1315 -->
HIKROBOT 
 
1306 
 
 
 
 



<!-- page 1316 -->
HIKROBOT 
 
1307 
 
 
 
 



<!-- page 1317 -->
HIKROBOT 
 
1308 
 
 
 
 



<!-- page 1318 -->
HIKROBOT 
 
1309 
 
 
 
 



<!-- page 1319 -->
HIKROBOT 
 
1310 
 
 
 
 



<!-- page 1320 -->
HIKROBOT 
 
1311 
 
 
 
 



<!-- page 1321 -->
HIKROBOT 
 
1312 
 
 
 
 



<!-- page 1322 -->
HIKROBOT 
 
1313 
 
 
 
 



<!-- page 1323 -->
HIKROBOT 
 
1314 
 
 
 
 



<!-- page 1324 -->
HIKROBOT 
 
1315 
 
 
 
 



<!-- page 1325 -->
HIKROBOT 
 
1316 
 
 
 
 



<!-- page 1326 -->
HIKROBOT 
 
1317 
 
 
 
 



<!-- page 1327 -->
HIKROBOT 
 
1318 
 
 
 
 



<!-- page 1328 -->
HIKROBOT 
 
1319 
 
 
 
 



<!-- page 1329 -->
HIKROBOT 
 
1320 
 
 
 
 



<!-- page 1330 -->
HIKROBOT 
 
1321 
 
 
 
 



<!-- page 1331 -->
HIKROBOT 
 
1322 
 
 
 
 



<!-- page 1332 -->
HIKROBOT 
 
1323 
 
 
 
 
 
 



<!-- page 1333 -->
HIKROBOT 
 
1324 
 
 
4.3 VM4.2 平台SDK 开发更新介绍 
 
 



<!-- page 1334 -->
HIKROBOT 
 
1325 
 
 
 
 



<!-- page 1335 -->
HIKROBOT 
 
1326 
 
 
 
 



<!-- page 1336 -->
HIKROBOT 
 
1327 
 
 
 
 



<!-- page 1337 -->
HIKROBOT 
 
1328 
 
 
 
 



<!-- page 1338 -->
HIKROBOT 
 
1329 
 
 
 
 
 



<!-- page 1339 -->
HIKROBOT 
 
1330 
 
 
 
 



<!-- page 1340 -->
HIKROBOT 
 
1331 
 
 
 
 



<!-- page 1341 -->
HIKROBOT 
 
1332 
 
 
 
 



<!-- page 1342 -->
HIKROBOT 
 
1333 
 
 
 
 



<!-- page 1343 -->
HIKROBOT 
 
1334 
 
 
 
 
 



<!-- page 1344 -->
HIKROBOT 
 
1335 
 
 
4.4 VM4.2 算子SDK 开发更新介绍 
 
 



<!-- page 1345 -->
HIKROBOT 
 
1336 
 
 
 
 



<!-- page 1346 -->
HIKROBOT 
 
1337 
 
 
 
 



<!-- page 1347 -->
HIKROBOT 
 
1338 
 
 
 
 



<!-- page 1348 -->
HIKROBOT 
 
1339 
 
 
 
 



<!-- page 1349 -->
HIKROBOT 
 
1340 
 
 
 
 



<!-- page 1350 -->
HIKROBOT 
 
1341 
 
 
 
 



<!-- page 1351 -->
HIKROBOT 
 
1342 
 
 
 
 



<!-- page 1352 -->
HIKROBOT 
 
1343 
 
 
 
 



<!-- page 1353 -->
HIKROBOT 
 
1344 
 
 
 
 



<!-- page 1354 -->
HIKROBOT 
 
1345 
 
 
 
 



<!-- page 1355 -->
HIKROBOT 
 
1346 
 
 
 
 



<!-- page 1356 -->
HIKROBOT 
 
1347 
 
 
 
 



<!-- page 1357 -->
HIKROBOT 
 
1348 
 
 
 
 



<!-- page 1358 -->
HIKROBOT 
 
1349 
 
 
 
 



<!-- page 1359 -->
HIKROBOT 
 
1350 
 
 
 
 
 
 



<!-- page 1360 -->
HIKROBOT 
 
1351 
 
 
4.5 VM4.3 应用更新介绍 
 
 



<!-- page 1361 -->
HIKROBOT 
 
1352 
 
 
 
 



<!-- page 1362 -->
HIKROBOT 
 
1353 
 
 
 
 



<!-- page 1363 -->
HIKROBOT 
 
1354 
 
 
 
 



<!-- page 1364 -->
HIKROBOT 
 
1355 
 
 
 
 



<!-- page 1365 -->
HIKROBOT 
 
1356 
 
 
 
 



<!-- page 1366 -->
HIKROBOT 
 
1357 
 
 
 
 



<!-- page 1367 -->
HIKROBOT 
 
1358 
 
 
 
 



<!-- page 1368 -->
HIKROBOT 
 
1359 
 
 
 
 



<!-- page 1369 -->
HIKROBOT 
 
1360 
 
 
 
 



<!-- page 1370 -->
HIKROBOT 
 
1361 
 
 
 
 



<!-- page 1371 -->
HIKROBOT 
 
1362 
 
 
 
 



<!-- page 1372 -->
HIKROBOT 
 
1363 
 
 
 
 



<!-- page 1373 -->
HIKROBOT 
 
1364 
 
 
 
 



<!-- page 1374 -->
HIKROBOT 
 
1365 
 
 
 
 
 
 
 



<!-- page 1375 -->
HIKROBOT 
 
1366 
 
 
4.6 VM4.3 平台SDK 开发更新介绍 
 
 
 



<!-- page 1376 -->
HIKROBOT 
 
1367 
 
 
 
 



<!-- page 1377 -->
HIKROBOT 
 
1368 
 
 
 
 



<!-- page 1378 -->
HIKROBOT 
 
1369 
 
 
 
 



<!-- page 1379 -->
HIKROBOT 
 
1370 
 
 
 
 



<!-- page 1380 -->
HIKROBOT 
 
1371 
 
 
 
 



<!-- page 1381 -->
HIKROBOT 
 
1372 
 
 
 
 



<!-- page 1382 -->
HIKROBOT 
 
1373 
 
 
 
 
 
 



<!-- page 1383 -->
HIKROBOT 
 
1374 
 
 
4.7 VM4.3 算法模块开发更新介绍 
 
 



<!-- page 1384 -->
HIKROBOT 
 
1375 
 
 
 
 



<!-- page 1385 -->
HIKROBOT 
 
1376 
 
 
 
 



<!-- page 1386 -->
HIKROBOT 
 
1377 
 
 
 
 
 
 



<!-- page 1387 -->
HIKROBOT 
 
1378 
 
 
4.8 VM4.3 维护版应用更新介绍 



<!-- page 1388 -->
HIKROBOT 
 
1379 
 
 



<!-- page 1389 -->
HIKROBOT 
 
1380 
 
 
 



<!-- page 1390 -->
HIKROBOT 
 
1381 
 
 



<!-- page 1391 -->
HIKROBOT 
 
1382 
 
 



<!-- page 1392 -->
HIKROBOT 
 
1383 
 
 



<!-- page 1393 -->
HIKROBOT 
 
1384 
 
 



<!-- page 1394 -->
HIKROBOT 
 
1385 
 
 



<!-- page 1395 -->
HIKROBOT 
 
1386 
 
 



<!-- page 1396 -->
HIKROBOT 
 
1387 
 
 
 
 



<!-- page 1397 -->
HIKROBOT 
 
1388 
 
 



<!-- page 1398 -->
HIKROBOT 
 
1389 
 
 



<!-- page 1399 -->
HIKROBOT 
 
1390 
 
 



<!-- page 1400 -->
HIKROBOT 
 
1391 
 
 
 
 
 


