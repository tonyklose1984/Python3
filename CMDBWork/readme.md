## CMDB运维系统。
1. 运行环境：**python2.7.13 Linux : Centos7 Django == 1.8.16**

2. 功能：
    * 实现对服务器上的应用具有远程管理的能力
    * CMDB资产管理
        1. 服务器端具有同步能力
        2. 用户端具有采集功能(服务器指标检测)
        3. 用户管理功能
        4. 日志检测功能
        5. api访问接口

3. 文件结构
    * CMDBWork ---- 项目主目录
    * Api      ---- Api apps (接口模块)
    * Service  ---- Service apps (服务器展示)
    * User     ---- User apps (用户管理模块)
    * Log      ---- Log apps (日志模块)
    * static   ---- 所有静态配置文件
    * template ---- HTML模板文件
    * readme.md---- 说明文档

