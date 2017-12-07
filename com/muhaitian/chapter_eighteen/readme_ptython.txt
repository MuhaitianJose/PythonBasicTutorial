程序打包：Distutils
python setup.py build(创建了叫做build的子目录，其中包含名为lib的子目录，并且把hello.py的一个副本放置在build/lib内。build子目录
是Distutils组装包（以及编译扩展库等）的工作区。在安转的时候不需要运行build命令--如果需要的话，在运行install命令的时候它就自动运行)
python setup.py install：install命令会将hello.py模块复制到PYTHONPATH变量内一些系统特定的目录内。
打包：建立存档文件
python setup.py sdist：用于源代码发布
python setup.py bdist_wininst：打包Windows下的安装文件
python setup.py bdist_rpm：打包linux下的执行程序
需要详细了解