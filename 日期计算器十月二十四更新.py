nianfenshu = [366,365,365,365]

meiyuerishu = [0,31,28,31,30,31,30,31,31,30,31,30,31,0]



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


d = int(input('请输入结束年份:'))





e = int(input('请输入结束月份:'))
#录取结束月份
while e<1 or e>12:
    e = int(input('您输入的结束月份有误，请重新输入结束月份:'))
    if e>=1 and e<=12:
        break


f = int(input('请输入结束日份:'))
#录取结束日份
while d == 1582 and e == 10 and f >4 and f <15:
    f = int(input('您输入的结束日份有误(这一天不存在！)，请重新输入结束日份:'))
    if  f <5 or f >14:
        break


genghuan = 0
if a > d or (a==d and b >e) or (a==d and b==e and c >f):
    genghuan = a
    a = d
    d = genghuan
    genghuan = b
    b = e
    e = genghuan
    genghuan = c
    c = f
    f = genghuan
    genghuan = '已更换'



one = 0

aa = a

bb = b

ee = e



while aa<d-1:
    aa += 1
    one = one + nianfenshu[aa%4]

    if aa==d-1:
        break


two = 0
while bb<13:
    two = two + meiyuerishu[bb]
    bb += 1
    if bb==13:
        break



three =0
while ee>0:
    ee-=1
    three=three+meiyuerishu[ee]
    if ee==0:
        break




four = 0


if a%4 ==0:
    if b<=2:
        four +=1

if d%4==0:
    if e>=3:
        four +=1


five = 0
if a<=1582 and b<=10 and c<=5 and d>=1582 and e>=10 and f>=14:
    five-=10


two = two -c

three = three +f



if a!=d:
    jieguo = one + two +three +four + five

elif a==d:
    jieguo = (one + two + three + four + five)-nianfenshu[a%4]


if genghuan == '已更换':
    jieguo *=-1
    print(f'您计算的{d}年{e}月{f}日至{a}年{b}月{c}日相隔天数结果为{jieguo}天，感谢您的使用')
elif genghuan != '已更换':
    print(f'您计算的{a}年{b}月{c}日至{d}年{e}月{f}日相隔天数结果为{jieguo}天，感谢您的使用')

manyi=input('您满意吗？有问题请反馈QQ944311671（Y/N）')