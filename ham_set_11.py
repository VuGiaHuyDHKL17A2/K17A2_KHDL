def chuong11_bai13():
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