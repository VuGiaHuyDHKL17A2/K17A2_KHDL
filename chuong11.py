# BT 11.1
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
print('Độ dài list a:',len(a))
print('Độ dài list b:',len(b))
print('Độ dài list c:',len(c))
print('Độ dài list d:',len(d))



# BT 11.2
teams = [['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'], ['David', 'Jack', 'Bill', 'Tom', 'Mike'], ['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
print(teams[2][1])



# BT 11.3
List_of_animals =  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo'] 
n = input(" I want to find")
print("List of animals :  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']")
print("Number of animals",len(List_of_animals))
if n in List_of_animals:
    print("There is ",n,"list of animals")
else:
    print("There isn't ",n,"list of animals")
  
#11.4
    mylist=[]
while True:
    val=int(input("Nhập giá trị : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    mylist.append(val)
    if a==0:
        x=int(input("Nhập giá trị cần tìm x:"))
        break
print('List:',mylist) 
print('Tổng các giá trị trong list:',sum(mylist))
print(x,'xuất hiện',mylist.count(x),'trong list')
if max(mylist)==x:
    print(x,'lớn hơn tất cả các số trong list')
else:
    print(x,'không lớn hơn tất cả các số trong list')
newlist=[int(i) for i in mylist if int(i)>x]
print('Các số lớn hơn',x,'trong list',newlist)


#  11.5
list=[]
x=int(input("Nhập giá trị:"))
list.append(x)
i=1
while i==1:
          y=int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không"))
          if y==1:
                  x=int(input("Nhập giá trị:"))
                  list.append(x)
          elif y==0:
                  break
print("list:",list)
sum=0
for num in list:
        sum+=num
print("Tổng các giá trị trong list:",sum)
x=int(input("Nhập giá trị cần tìm:"))
find = x in list
if find=="True":
        print(x,"xuất hiện",list.count(x),"lần trong list")
for i in list:
        if i>x:
          print(x,"không lớn hơn tất cả các số trong list")
          break
new_list=[]
for i in list:
        if i>x:
               new_list.append(i)
print("Các số lớn hơn",x,"trong list:",new_list)   
# 11.6
chieu_cao=[74,74,72,72,73,69,69,71,76,71]
def doi(x):
    return x*0.0254
ccmoi = [doi(x) for x in chieu_cao]
print('Đổi inch sang m:',ccmoi)
print('In 3 chiều cao đầu tiên:',ccmoi[0:3])
print('In 3 chiều cao cuối cùng:',ccmoi[-3:])
print("Chiều cao max:",max(ccmoi))
print("Chiều cao min:",min(ccmoi))
print("Chiều cao trung bình:",sum(ccmoi)/len(ccmoi))
ccmoi.sort()
print('Chiều cao tăng dần:',ccmoi)
ccmoi.sort()
ccmoi.reverse()
print('Chiều cao giảm dần:',ccmoi)

# 11.8   
def has_lucky_number(nums):
  for num in nums:
    if num % 7 == 0:
      return True
  return False
nums = [2, 6, 7, 9]
print(has_lucky_number(nums))
 #11.9
arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
def party_late(arrivals,name):
    if name==arrivals[-1]:
        return False
    elif name==arrivals[0]:
        return False
    elif name==arrivals[1]:
        return False
    elif name==arrivals[2]:
        return False
    elif name==arrivals[3]:
        return False
    else:
        return True
print(party_late(arrivals,name='Gilber'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))
#11.10
def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))
#11.11
a=['red','green','yellow','blue','black','white','pink','orange','red','blue']
print("Tuple :",a)
x=int(input('Nhập số từ 0 đến 9: '))
y=int(input('Nhập số từ -1 đến -9: '))
z=input('Nhập chuỗi cần tìm: ')
print("Tuple[",x,"] =",a[x])
print("Tuple[",y,"] =",a[y])
print(z,"xuất hiện trong tuple",a.count(z),"lần")
#11.12
a=(3,1,2,4)
print("Tuple a: ",a)
b=(5,7,6,8)
print("Tuple b: ",b)
x=list(a+b)
c=tuple(x)
print("Tuple c: ",c)
x.sort()
d=tuple(x)
print("Tuple d: ",d)
print("Tuple[3]=",d[3])
print("3 phần tử cuối cùng của tuple d :",d[-3:])

#11.13
set1=set()
while True:
    val=int(input("Nhập giá trị cho set 1 : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    set1.add(val)
    if a==0:
        break
set2=set()
while True:
    val=int(input("Nhập giá trị cho set 2 : "))
    a=int(input("Tiếp tục nhập giá trị ? 1:Có,0:Không "))
    set2.add(val)
    if a==0:
        break
print("Set 1:",set1)
print("Set 2:",set2)
print("Set 1 có số phần tử là:",len(set1))
print("Set 2 có số phần tử là:",len(set2))
print("Tổng các giá trị của set 1 là:",sum(set1))
print("Tổng các giá trị của set 2 là:",sum(set2))
print("Min set 1:",min(set1))
print("Max set 1:",max(set1))
print("Min set 2:",min(set2))
print("Max set 2:",max(set2))
a=set1.pop()
print("Phần tử bị lấy ra ở set 1:",a)
print("Set 1 sau khi pop:",set1)
setb=set1|set2
print("Set 1 union set 2:",setb)
setc=set1&set2
print("Set 1 interection set 2:",setc)
setd=set1-set2
print("Set 1 difference set 2:",setd)
sete=set1^set2
print("Set 1, set 2 symmetric difference:",sete)
print("Set 1 sắp tăng dần: ",sorted(set1))
print("Set 2 sắp giảm dần: ",sorted(set2,reverse=True))

#11.14
danh_ba={'Minh':'0989741258','Hạnh':'0903852147','Bình':'0913753951','An':'0933753654','Linh':'0813138951'}
while True:
    a=int(input("Bạn muốn làm gì ? 1: Tìm thông tin trong danh bạ; 2: Thêm liên hệ mới "))
    if a==1:
        a=input("Nhập tên cần tìm: ")
        if a in danh_ba:
            print('Thông tin của',a,'trong danh bạ là:\n',a,":",danh_ba[a])   
        else:
            print("Người này không nằm trong danh bạ")
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break
    elif a==2:
        b=input("Tên liên hệ mới :")
        c=input("Số điện thoại liên hệ mới:")
        danh_ba[b]=c
        print('Danh bạ điện thoại :')
        for i in danh_ba:
            print(i,':',danh_ba[i])
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break
#11.15
tudien={'cat':'con mèo','dog':'con chó','ant':'con kiến','bear':'con gấu'}
while True:
    a=int(input("Bạn muốn làm gì ? 1: Xem từ điển; 2: Tra từ điển; 3: Thêm từ; 4:Xoá từ "))
    if a==1:
        print("Dictionary :")
        for i in tudien:
            print(i,":",tudien[i])
        x=int(input("Bạn muốn tiếp tục không ? số bất kì: có, 0: không ")) 
        if x==0:
            break   
    elif a==2:
        b=input("Nhập từ cần tra: ")
        if b in tudien:
            print('Từ này có trong từ điển :\n',b,":",tudien[b])   
        else:
            print("Từ này không có trong từ điển !")
        x=int(input("Bạn muốn tiếp tục không ? số bất kì: có, 0: không ")) 
        if x==0:
            break
    elif a==3:
        d=input("Nhập từ tiếng anh cần thêm :")
        e=input("Nhập nghĩa tiếng việt của từ cần thêm:")
        tudien[d]=e
        print('Dictionary :')
        for i in tudien:
            print(i,':',tudien[i])
        print("Từ điện đang có",len(tudien),"từ")
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break
    elif a==4:
        f=input("Nhập từ cần xoá : ")
        g=int(input("Bạn có thật sự muốn xoá không ? số bất kì: có, 0: không ")) 
        del tudien[f]
        print("Đã xoá từ",f,'trong từ điển')
        print("Dictionary :")
        for i in tudien:
            print(i,":",tudien[i])
        x=int(input("Bạn có muốn tiếp tục không ? Số bất kì:Có,0:Không "))
        if x==0:
            break










