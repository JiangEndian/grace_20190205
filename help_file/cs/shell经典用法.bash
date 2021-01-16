
#测试两变量不相等，双引号弱引用，单引号强引用
if [ "$var1" -ne "$var2" ];then#测试字符串应引起来
fi
#[是链接到test[test]的一个符号链接，要封闭
#[[ ... ]]更能防止逻辑错误，如&&,||,<,>只能在这通过
if [[ "$var1" < "$var2" ]];then
elif test xxx;then
else #[els] 别的, 否则, 不然
fi

[ -eq等于/-lt小于/-gt大于/-ge大于等于/-le小于等于 ]

[ -a逻辑与/-o逻辑或/ ]
#上面的-a/-o和下面的双方括号里的他们很像
[[ && / || ]]
#(())C风格，可能用过C，因此更顺手...
((</<=/>/>=))
[[ =/==/!=/</> ]] #在这里使用模式匹配

#if的其他用法
if cd $dir 2>/dev/null;then #隐藏错误信息
else
fi
[ $var1 -ne $var2 ] && cmd  #不用if完成if功能
if [ test1 ] && [ test2 ];then  #单的里面只能用字母的
if [[ test1 && test2 ]];then    #双的可以里面用&&||...
if [ test1 -a test2 ];then      #单的里面用-a/-o
fi
fi
fi

let "var += 5"  #计算，C类似行为
let a=16+5
let "z=5**3"    #求幂操作
let "n=$n+1"    #let "n = n + 1"也可以
((n=n+1))       #C风格计算，更顺手～
let "n++"
((n++))/((++n)) #C风格的计算
$((n++))        #C风格的计算并表值
let "otc = 032" #八进制，以零为前缀
let "hex = 0x32"    #十六进制，以0x/0X为前缀
let "bin = 2#101"   #其他进制，基数#数，基数为2-64进制


#测试参数1存在，$1只是${1}的简写形式，某些场合必须全
if [ -n $1 ];then #-n字符串不为NULL
fi
until [ -z $1 ];do  #直到没有这个参数（取完了） #-z字符串为NULL
    shift   #参数前推直至推完
done # [dʌn]完成了的

archive=${1:-$BackupFile}   #如果没有$1则用后面的

case 变量 in
    value1)
    cmd
    ;;  #双分号结束一个子判断
    value2)
    cmd
    ;;
    *)  #除了上面的外的其他值
    cmd
    ;;
esac


#测试文件存在/不存在
if [ -x ${filename} ];then
    #测试文件存在
else
    #文件不存在
fi
[ -ot比其旧/ ]
[ -d $home ] || cmd #测试目录存在


#循环break退一层break N退N层。continue开始下轮循环
while :;do  #死循环
done
while true;do   #死循环
done
while [ $var -lt $var ];do
done
while [ $var != "end" ];do
done
while ((a!=3));do   #C风格的，不顺眼，顺手～
done
while read && [[ $REPLY != 's' ]];do #输入不为s则循环
done
for a in 1 2 3 4;do #遍历
done
for f in $(ls -a);do    #遍历文件，有空格可不行。。。
done
for((i=0;i<10;i++));do
    echo $i # [ˈekoʊ]回声, 回音【计】 回显;
done
for((i=0, j=0; i<10; i++,j++));do
    echo $i$j
done
for file in *;do
done
for file in [jx]*;do
    rm -f $file #删除当前目录下以j或x开头的文件
    echo "Removed file \"$file\""
done
for a;do    #循环将遍历$@，参数列表
done
NUMBERS="9 7 3 8 0" #命令替换产生list的for循环 # [lɪst]目录, 名单, 列出, 列表, 序列
for number in `echo $NUMBERS`;do
done


######[sɔːrt]种类, 分类, 排序 # [juˈniːk] 独一无二的
cat *.lst | sort | uniq #合并且排序.lst文件再删除多余相同行


#位置参数$0,$1,$2,$3......
$#  #所有参数的总数，为0代表没有参数
$0  #脚本名字，$1开始第一个参数，以此类推，$9,${10}
$* $@   #表示所有位置参数,$@会保存shift后除掉$1的剩余
$?  #保存了最后一个命令执行后的退出状态
$_  #保存前一个命令最后一个参数的变量值
\$$var  #引用var变量值为变量名的变量值

$RANDOM #返回伪随机整数（0-32767）,取模得某范围。不平均
rnumber=$(($RANDOM%25+6))   #6-30之间的随机数。0-24，+6
RANDOM=1    #为随机数设定种子，同样种子同样序列。。。


#重定向
cmd > filename  #重定向标准输出 至文件
cmd &> filename #重定向标准输出和标准错误 至文件
cmd >&2         #重定向标准输出 至标准错误
>>  #追加
cmd 2>&1        #重定向标准错误 至标准输出
cmd < filename  #从文件中接受输入
ls -yz >> log 2>&1  #所有到log中，因为stderr被重定向 
ls -yz 2>&1 >> log  #错误信息只输出，不入文件了。。。


#字处理-替换字符
tr 'a-z' 'A-Z'  #把输入字符改为大写
tr '_' ' '      #把输入串中的_换为空格


#函数（方法）
funname()   #调用时:funname 1 2或funname() 1 2，内部获得参数用$1,$2
{
    cmd
}


#输入
read    #读入到REPLY变量中
read fruit  #读入到fruit变量中 # [fruːt]水果
read -p "showmessage:" x/y  #提示，并读入到x或y中
read -t $TimeLimit var  #定时限输入


#批量更改文件后缀.bash 旧后缀 新后缀
#!/bin/bash
old=".$1"
new=".$2"
for filename in *.$1;do
    mv $filename ${filename%$old}$new   #剥去.$1加上.$2
done

filename=test111
echo ${filename%'111'}  #test。只能剥最后的111不能剥test
#格式：${原字串变量名%'欲剥的末字串'}

echo -e "\n" #可识别转义字符哦哦～得加双引号


#常用命令法
cut -d ' ' -f1,2 /etc/mtab  #获得mount上的文件系统列表
uname -a |cut -d" " -f1,3,11,12 #获得OS和kernel版本 # [ˈkɜːrnl]核心【计】 内核
cut -d: -f1 /etc/passwd #列出所有用户，f要加-，为"-fn"~ # [ˈpæswɜːrd]密码
head -8 file | tail -1  #列出文件第8行 # [hed]头 # [teɪl]尾
ls *.txt | wc -l    #统计当前目录有多少个txt文件
cmd | grep foo | wc -l  #统计含有foo的有多少行
cmd | grep -c foo       #同上，用grep的-c选项也能统计
nl file #与cat -n file相似，但默认空行不计数。。。
factor 27417    #将一个正数分解为多个素数 # [ˈfæktər]因素, 因数
echo "2+3" | bc #类C语法的计算器
notify-send #bash提醒，GUI，alert是他的一个alias # [ˈnoʊtɪfaɪ]通知 # [ˈeɪliəs]别名
free	#查看内存使用情况-m-g以M/G为单位打印，-h人性化显示 # [friː]自由的,免费的

date -d "-/+n day/month/year"   #打印n天/月/年 前/后 
    #%Y:yyyy  %y:yy  %m:mm  %d:dd  %H:hh  %M:mm  %S:ss %w:星期
NOW=`date +%s`  #当前时间的秒数
TO=`date -d "+1day05:30" +%s`   #明天5：30的时间的秒数

seq m n #m到n的一个序列如1,2,3 / 2,3,4,5,这样的。
grep -v '#' fname #v打印不符合要求的行，本例为不显示注释行
    -n加行号
    -An打印符合要求的行及后面n行
    -Bn打印符合要求的行及前面n行
    -Cn要求的及上下n行
    --color=auto #在脚本中加上，才能出彩色(bash已经alias了)
    '[^a-z\.!^ -]' #表示没有小写字母，没有. 没有!, 没有空格，没有- 的 串，注意[]里面有个小空格。

jobs    #查看shell中后台执行的任务
    fg n   #调到前台，不加编号为最近的
    ctrl + z    #暂停，输入bg可以进入后台执行，等于加个&
df -h   #以合适的单位显示已挂载磁盘的使用情况
find /home/ed -name filename*    #按名字查找
    -type f文件 b块设备 d目录 l连接 s套接字
    -size +1000K/-1000K #按大小找，大于/小于1M的 # [saɪz]
    -size +50k -a -size -60k -exec ls -l {}\; #exec是find的一个选项
    #找出size大于50K，且size小于60K的文件，并用ls处理
locate filename*    #从数据库查找，更快，但新文件找不到 # [ˈloʊkeɪt]找出,定居
ifconfig eth0 ip    #修改IP，然后 # configure [kənˈfɪɡjər] 装配
service network restart #重启网络服务 # [ˈsɜːrvɪs] 服务 # [ˈnetwɜːrk]网络 # [ˌriːˈstɑːrt] 重启
ls *.txt | xargs -n1 -i{} mv {} {}_bak  #批量改后缀 # argument [ˈɑːrɡjumənt] 参数

############cman xargs得到的一些东西################
xargs [选项] cmd #从标准输入读入参数，以此多次执行command
    #-n1    每次执行命令最多可以有1个参数（遍历）
    #-i{}   把前面的参数用{}取代
    #mv {} {}_bak   重命名命令
####################################################

cvlc -R --no-repeat --play-and-exit 2.mp3 >/dev/null 2>&1 &
#后台放一遍退出，不输出任何信息

printf %04d 33 #0033...我还用py写了个，用的时候才发现～ #  [prɪnt] 打印



#vim相关
#:e!    #还原成最原始状态
#:w othername    #编辑后的文档另存为 # [ˈʌðər]其他的
#:n1,n2 w othername #将n1到n2的内容另存为
#vim file1 file2    #打开两个文件
#:e filename/:n filename    #转到指定文件
#:n #转到下一文件
#:12 #跳到12行

#ftp相关
ftp ip #连接目标ftp服务，进入后
    输入username
    输入password
    help #显示可用命令
    ls #列出远程目录
    cd #切换远程目录
    bin #切换到使用二进制传输方式
    lcd #指定下载到本机的哪个目录
    get #下载单个文件
    put /home/ed/本地文件 远程文件名 #上传本地文件为远程文件名
    prompt #关闭交互模式
    mput #批量上传（先关闭交互模式，多个文件用空格分隔）
    mget #批量下载
    bye #再见，退出ftp
###############ftp自动化文件auto.ftp###############
open 192.168.191.222
user jed jed
bin
prompt
lcd /home/ed/Downloads/
mget * #下载当前目录所有文件
bye
###然后，用-n关闭交互模式调用文件
ftp -n < auto.ftp
####################################################
#vsftpd可查看bash_help

ifconfig eth0 down/up #停用/启用网络适配器。

################
ssh相关命令：
1、从服务器上下载文件
scp username@servername:/path/filename /var/www/local_dir（本地目录）

3、从服务器下载整个目录
scp -r username@servername:/var/www/remote_dir/（远程目录） /var/www/local_dir（本地目录）
例如:scp -r root@192.168.0.101:/var/www/test  /var/www/  

2、上传本地文件到服务器
scp /path/filename username@servername:/path   

4、上传目录到服务器
scp  -r local_dir username@servername:remote_dir
例如：scp -r test  root@192.168.0.101:/var/www/   把当前目录下的test目录上传到服务器的/var/www/ 目录
注：目标服务器要开启写入权限。

获取文件名：resFile=`basename /tmp/csdn/zhengyi/test/adb.log`
获取目录名：dirPath=`dirname /tmp/csdn/zhengyi/test/adb.log`
获得当前目录：basename $(pwd)
