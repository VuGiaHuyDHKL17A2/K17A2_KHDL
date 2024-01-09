def chuong11_bai11():
    a=['red','green','yellow','blue','black','white','pink','orange','red','blue']
    print("Tuple :",a)
    x=int(input('Nhập số từ 0 đến 9: '))
    y=int(input('Nhập số từ -1 đến -9: '))
    z=input('Nhập chuỗi cần tìm: ')
    print("Tuple[",x,"] =",a[x])
    print("Tuple[",y,"] =",a[y])
    print(z,"xuất hiện trong tuple",a.count(z),"lần")

def chuong11_bai12():
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