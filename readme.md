### 介绍
程序的功能是重命名windows系统下，visual studio中的c++的项目(The function of the program is to rename the c++ project in visual studio under windows system)；
参考https://github.com/MethodJiao/VsProjectRename 的程序，修复了若干自己在使用中遇到的问题，如修改.db文件报错、使用时间过长等；
### 用法
#### 1 
下载exe文件，直接运行；依次输入解决方案路径、原项目名、新项目名，如输入 E:\Project\TestBoostLog、TestBoostLog、newname
#### 2 
在python环境下，运行python代码；
### 问题
#### PermissionError,WindowsError: [Error 5]：
碰到过该问题，自己文件都可以重命名，但从网上下载来的一个项目不行；尝试过网上多种解决方法，无效；
后来，压缩该项目，再解压，解压后文件可以重命名；认为多次os.rename或许也有效，未尝试。
有人知道原因希望帮忙解答，谢谢好心人！