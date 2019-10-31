a = int(input('请输入起始年份:'))
b = int(input('请输入起始月份:'))

while b<1 or b>12:
    b = int(input('您输入的起始月份有误，请重新输入起始月份:'))
    if b>=1 and b<=12:
        break

c = int(input('请输入起始日份:'))
#录取起始日份
while a == 1582 and b == 10 and c >4 and c <15:
    c = int(input('您输入的起始日份有误(这一天不存在！)，请重新输入起始日份:'))
    if  c <5 or c >14:
        break


d = int(input('要延后多久？'))
while d <=0:
    d = int(input('只能向后计算，请重新输入要延后多久:'))
    if d >0:
        break
aa = a
bb = b
cc = c+d

meiyourishu = [0,31,29,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31,31,28,31,30,31,30,31,31,30,31,30,31]




while cc > meiyourishu[aa%4*12+bb]:

    cc-=meiyourishu[aa%4*12+bb]
    bb+=1
    while bb > 12:
        aa += 1
        bb -= 12
        if bb <= 12:
            break
    if cc<=meiyourishu[aa%4*12+bb]:
        break
aaa =aa
bbb = bb
ccc = cc
if a <1852 or (a == 1852 and b <10 ) or (a == 1852 and b==10 and c <=4):
    if aa >1852 or (aa == 1852 and bb >10 ) or (bb == 1852 and bb==10 and cc >=4):
        cc -=10
    if cc <=0:
        bb-=1
        cc += meiyourishu[aa%4*12+bb]
    if bb ==0:
        aa-=1
        bb =12

print (f"{a}年{b}月{c}日延后{d}天的结果是{aa}年{bb}月{cc}日")
manyi=input('您满意吗？（Y/N）')