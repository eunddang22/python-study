h,m = map(int,input().split())
mm = h*60 + m
alarm = mm-45
h = alarm // 60
m = alarm % 60
if h <0 :
    h = 24 + h
alarm1 = [h,m]
print(h,m)

