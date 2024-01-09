def chuong8_bai1():
 print("Bài toán tìm số lớn nhất và nhỏ nhất.")
 a=eval(input("Nhập số a:"))
 b=eval(input("Nhập số b:"))
 c=eval(input("Nhập số c:"))
 d=eval(input("Nhập số d:"))
 g=0
 h=0
 while(g<a)or(g<b)or(g<c)or(g<d):
    g+=1
 h=g
 while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
 print("max =",g)
 print("min =",h)   

def chuong8_bai2():
  a = float(input("Nhap gia tri a:"))
  if a > 0:
    print("|x| = ", a)
  else:
    print("|x| = ", -a)

def chuong8_bai3():
 print("Giải phương trình ax+b=0")
 a = int(input("Nhập số a:"))
 b = int(input("Nhập số b:"))
 if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else: print("Phương trình vô nghiệm.") 
 else: 
    print('Nghiệm của phương trình là: x = ', -b/a)

def chuong8_bai4():
 a = eval(input("nhap do dai canh a: "))
 b = eval(input("nhap do dai canh b: "))
 c = eval(input("nhap do dai canh c: "))
 if a+b<c and b+c<b:
    print("day khong phai la tam giac")
 else:
    print("day la mot tam giac")
    import math
    p=(a+b+c)/2
    S= math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Dien tich tam giac tren la: ",S)

def chuong8_bai5():
 a = int(input("Nhập năm: "))
 if ((a%4==0) and (a%100!=0) or (a%400==0)):
    print("năm", a, "là năm nhuận")
 else:
    print("năm", a, "không phải là năm nhuận")

def chuong8_bai6():
 loai_xe=int(input("Cho biết loại xe là 4/7 ? :"))
 so_km=float(input("Nhập số km chạy bằng = "))
 time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
 tien_cuoc=float(0)
 tien_di_chuyen=float(0)
 if time_cho >=5:
    tien_cho=(time_cho-5)*0.8
 else:
    tien_cho=0
 if loai_xe==4:
     if so_km <=0.8:
         tien_di_chuyen=0.8*11000
     elif so_km <=20:
         tien_di_chuyen=0.8*11000+(20-so_km)*12100
     else:
         tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
     tien_cuoc=tien_cho+tien_di_chuyen
     print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
 if loai_xe==7:
     if so_km <=0.8:
         tien_cuoc+tien_cho+0.8*13000
     elif so_km <=30:
         tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
     else:
         tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
     tien_cuoc=tien_cho+tien_di_chuyen
     print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)

def chuong8_bai7():
  a=float(input("Nhập số KWh tiêu thụ:"))
  if a>=0:
      if a<=50:
         print("Tổng số tiền phải trả là:",a*1678,"đồng.")
      elif a<=100:
        print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
      elif a<=200:
        print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
      elif a<=300:
        print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
      elif a<=400:
        print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
      else:
        print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
  else:
    print("Số KWh không hợp lệ.")
   
def chuong8_bai8():
  print("Các mã loại phòng cho bạn:")
  print("1-Standard")
  print("2-Superior Garden View")
  print("3-Superior Ocean View")
  print("4-Garden View Bungalow")
  print("5-Pool View Bungalow")
  print("6-Family Room")
  print("7-Beach Front Bungalow")
  print("8-VIP sea View")
  a=int(input("Nhập mã loại phòng:"))
  b=int(input("Nhập số đêm:"))
  if a>0&a<=8:
      if a==1: c=1260000
      elif a==2: c=1550000
      elif a==3: c=1830000
      elif a==4: c=1830000
      elif a==5: c=2120000
      elif a==6: c=2120000
      elif a==7: c=2540000
      elif a==8: c=4800000
      else: 
          print("Vui lòng chọn lại mã loại phòng.")
  else: print("Vui lòng chọn lại mã loại phòng.") 
  if b==1:
     print("Giá  tiền phải trả là:",c,"đồng.")
  elif b==2:
      print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
  elif b==3:
      print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
  elif b>=4:
      print("Giá  tiền phải trả là:",c*b*0.7,"đồng.")       
  else:
      print("Vui lòng nhập lại số đêm.")

def chuong8_bai9():
 n = 10
 while n > -1:
    print(n)
    n = n - 1
 else:
    print("Start!!")

def chuong8_bai10():
  n = int(input("Nhap so nguyen n: "))
  x = float(input("Nhap so thuc x: "))
  s = (x**2 + 1)**n
  print(f"S = ({x}^2 + 1)^{n} = {s}")

def chuong8_bai11():
  n = int(input("Nhap so nguyen n: "))
  x = float(input("Nhap so thuc x: "))
  a = (x**2 + x + 1)**n + (x**2 - x + 1)**n
  print(f"A = ({x}^2 + {x} + 1)^{n} + ({x}^2- {x} + 1)^{n} = {a}")

def chuong8_bai12(): 
  x = int(input("Nhap vao so nguyen duong x: "))
  if x < 2:
      print(x, " khong phai so nguyen to")
  else:
      for i in range(2,x):
         if x%i == 0:
              print(x, "khong phai so nguyen to")
              break
      else:
          print(x, " la so nguyen to")

def chuong8_bai13():
   #A = tổng các số lẻ nhỏ hơn hay bằng n
  n = int(input("Nhap vao so nguyen duong n: "))
  tong = 0
  for i in range(0, n+1):
      if i%2!=0:
          tong = tong + i
  print(f"A = {tong}")

  #B = tổng các số chẵn nhỏ hơn hay bằng n
  n = int(input("Nhap vao so nguyen duong n: "))
  tong = 0
  for i in range(0, n+1):
      if i%2==0:
          tong = tong + i
  print(f"B = {tong}")

  #C = tích các số từ 1 đến n
  n = int(input("Nhap vao so nguyen duong n: "))
  tich = 1
  for i in range(1, n+1):
      tich = tich*i
  print(f"C = {tich}")

  #D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
  n = int(input("Nhap vao so nguyen duong n: "))
  tich = 1
  for i in range(1, n+1):
      if i%3==0:
          tich = tich*i
  print(f"D = {tich}")

  #E = tổng các số nguyên tố nhỏ hơn hay bằng n
  n = int(input("Nhap vao so nguyen duong n: "))
  tong = 0
  for i in range(2, n+1):
      for j in range(2,i):
          if i%j == 0:
              break
      else:
          tong = tong + i
  print(f"E = {tong}")

  #F = tổng chuỗi đan dấu
  n = int(input("Nhap vao so nguyen duong n: "))
  tong = 0.0
  flag = True
  for i in range(1, n+1):
      if flag == True:
          tong = tong + 1.0/i
          flag = False
      else:
          tong = tong - 1.0/i
          flag = True
  print(f"F = {tong}")

def chuong8_bai14():
  n = int(input("Nhap so cac so nguyen: "))
  if n < 0:
      print("n khong hop le")
  else:
      tong = 0
      for i in range(1,n+1):
          a = int(input(f"Nhap so nguyen thu {i}:", ))
          tong = tong + a
      print("Tong cac so vua nhap:", tong)

def chuong8_bai15():
  a = True
  S = 0
  while a:
      print("nhập số nguyên N: ")
      b = int(input())
      S = S + b
      if b ==0:
          a = False
          break
  print("tổng số hạng vừa nhập là: ",S) 
  
def chuong8_bai16():
  a = int(input("Nhập số a: "))
  b = int(input("Nhập số b: "))
  while(a*b!=0):
      if a>b:
          a%=b
      else:
          b%=a
  print(a+b) 

def chuong8_bai17():
  a = int(input("Nhập số a: "))
  b = int(input("Nhập số b: "))
  c = a*b
  for i in range (b, c+1):
      if i%a == 0 and i%b == 0:
          d = i
          break
  print(i)

def chuong8_bai18():
  x = int(input("Nhap vao so nguyen duong x: "))
  if x < 0:
     print("x phai la so nguyen duong")
  else:
     if x == 0:
         print("0 khong phai la so hoan hao")
     tong = 0
     for i in range(1, x):
        if x%i==0:
            tong = tong + i
     if tong == x:
        print(x, "la so hoan hao")
     else:
        print(x, "khong phai so hoan hao")

def chuong8_bai19():
  day_so = input("Nhap vao mot day so bat ky, moi so cach nhau boi dau cach: ")
  if day_so[0] != "1":
     print("Day so phai bat dau tu so 1")
  else:
      day_so_nguoc = day_so[::-1]
      pos = 0
      count = 0
      day_so_moi = ""
      for i in day_so_nguoc:
         if i == " ":
             k = day_so_nguoc[pos - count : pos]
             k = k[::-1]
             if int(k) % 2 != 0:
                 day_so_moi = day_so_moi + k + " "
             count = 0
         else:
             count = count + 1
         pos = pos + 1
      day_so_moi = day_so_moi + "1"
      print(day_so_moi)

def chuong8_bai20():
  n = int(input("Nhap so nguyen duong n: "))
  x = int(input("Nhap so nguyen x: "))
  if n < 0:
      print("n khong hop le")
  else:
      tong = 0
      for i in range(1,n+1):
          giai_thua = 1
          for j in range(1,i+1):
              giai_thua = giai_thua*i
          tong = tong + (x**i)/giai_thua
      print(f"e^{x} = {tong}")