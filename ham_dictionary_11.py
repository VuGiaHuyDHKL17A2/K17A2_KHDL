def chuong11_bai15():
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