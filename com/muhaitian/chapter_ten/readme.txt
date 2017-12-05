通配符：点号（.）可以匹配任何字符（除了换行符）
对特殊字符进行转义：比如‘python\\.org’才能匹配‘python.org’
字符集：可以匹配它所包括的任意字符（‘[pj]ython’能够匹配‘python’和‘jython’）
10.2
dir：查看模块包含的内容可以使用dir。
help：查看函数的文档注释
10.3
sys：这个模块让你能够访问与Python解释器联系紧密的变量和函数
sys.argv：命令行参数，包含脚本名称
sys.exit：退出当前的程序，可选参数为给定的返回值或者错误信息
sys.modules：映射模块的名字到载入模块的字典
sys.path：查找模块所在目录的目录名列表
sys.platform：类似sunos5或者win32的平台标识符
sys.stdin：标准输入流----一个类文件对象
sys.stdout：标准输出流--一个类文件对象
sys.stderr：标准错误流--一个类文件对象
os：os模块为你提供了访问多个操作系统服务的功能。
os.environ：对环境变量进行映射
os.system：在子shell中执行操作系统的命令
os.sep：路径中的分隔符
os.linesep：行分隔符（‘\n’,'\r','\r\n'）
os.urandom：返回n字节的加密强随机数据

fileinput:fileinput 模块让你能够轻松遍历文本文件的所有行。

fileinput.input([files[,inplace[,backup]]])：便于遍历多个输入流中的行
fileinput.filename()：返回当前文件的名称
fileinput.lineno()：返回当前（累计）的行数
fileinput.isfirstline()：检查当前是否是文件的第一行
fileinput.isstdin()：检查最后一行是否来自sys.stdin
fileinput.nextfile()：关闭当前文件，移动到下一个文件
fileinput.close()：关闭序列
集合（Set）：
堆（heap）
heappush(heap,x)：将x入堆
heappop(heap)：将堆中最小的元素弹出
heapify(heap)：将heap属性强制应用到任意一个列表
heapreplace(heap,x)：将堆中最小的元素弹出，同时将x入堆
nlargest(n,iter)：返回iter中第n大的元素
nsmallest(n,iter)：返回iter中第n小的元素

time：获取当前时间、操作时间和日期、从字符串读取时间以及格式化时间为字符串
asctime([tuple])：将时间元组转换为字符串
localtime([secs])：将秒数转换为本地时间
sleep(secs)：休眠（不做任何事情）secs秒
strptime(String[,format])：将字符串解析为时间元组
time()：当前时间（新纪元开始后的秒数，以UTC为准）

random模块包含返回随机数的函数（0<=n<1之间的随机数n,其中0<n<=1）
getrandbits(n)：以长整型形式返回n个随机数
uniform(a,b)：返回随机实数n,其中a<=n<b
randrange([start],stop,[step])：返回range（start,stop,step）中的随机数
choice（seq）：从序列seq中返回随意元素
shuffle(seq[,random])：原地指定序列seq
sample(seq,n)：从序列seq中选择n个随机且独立的元素

re模块包含对正则表达式的支持



