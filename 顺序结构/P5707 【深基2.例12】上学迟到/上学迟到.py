#给s和v分别赋值int类型
s,v=map(int,input().split())
#将走路总时间向上取整
t=(s+v-1)//v+10
#如果今天出发，则用8小时计减去总时间
start=8*60-t
#如果时间提前一天，则要加一天的时间(分钟)
if start < 0:
    start+=24*60
h=start//60
mn=start%60
#02d表示位置用0补足，总共两位数字，用十进制输出
print(f"{h:02d}:{mn:02d}")