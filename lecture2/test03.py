#แสดงข้อมูลหลายๆประเภทใน print เดียว

#1. ใช้ , จะมี space
print("SAU",555,122.456,True,10+50)

#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช่ str ต้องแปลงเป็น str และไม่มี space ให้เหมือนกับ , 
print("SAU "+str(555)+' '+str(122.456)+' '+str(True)+' '+str(10+50))

#3. ใช้ method ชื่อ format (มี . เรียก method)
print("SAU {} {} {} {}".format(555, 123.456, True, 10+50))
print("SAU {0} {1} {2} {3}".format(555, 123.456, True, 10+50))

#4. ใช้ f-string *** 
print(f"SAU {555} {123.456} {True} {10+50} ")

#------------------------
#กรณี 1 บรรทัดมีหลาย statement
print("aaa"); print(111); print(False)