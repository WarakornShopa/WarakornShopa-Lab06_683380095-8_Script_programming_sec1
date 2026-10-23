# Activity 6.2: Discussion — Modular Programming & Standard Library

## 1. Benefits of Modular Programming

Modular programming คือการแบ่งโปรแกรมออกเป็นฟังก์ชันหรือโมดูลย่อย ๆ โดยแต่ละส่วนรับผิดชอบงานที่ชัดเจน

ประโยชน์:
1. **ลดการเขียนโค้ดซ้ำ (Reusability):** เขียนฟังก์ชันหนึ่งครั้งแล้วเรียกใช้ได้หลายจุด
2. **อ่านและดูแลรักษาง่าย (Readability/Maintainability):** โค้ดแบ่งเป็นส่วน ทำให้เข้าใจและแก้ไขได้ง่ายขึ้น
3. **แก้ไขข้อผิดพลาดง่าย (Debugging):** สามารถตรวจสอบส่วนที่มีปัญหาแยกจากส่วนอื่นได้
4. **ทดสอบได้ง่าย (Testing):** ทดสอบฟังก์ชันแต่ละตัวด้วยข้อมูลหลายกรณีได้
5. **ทำงานเป็นทีมได้สะดวก (Teamwork):** สมาชิกแบ่งกันพัฒนาคนละโมดูล แล้วนำมารวมกันได้
6. **จัดระเบียบโปรเจกต์ (Organization):** แยกโค้ดที่เกี่ยวข้องไว้ในไฟล์เดียวกัน เช่น ฟังก์ชันช่วยคำนวณไว้ใน `my_utils.py`

ตัวอย่าง: ในโปรแกรมเครื่องคิดเลข สามารถแยก `add()`, `subtract()`, `multiply()` และ `divide()` ออกจากโค้ดเมนูได้ ทำให้ทดสอบการคำนวณแต่ละแบบได้โดยไม่ต้องรันเมนูทั้งหมด

## 2. Standard Library Exploration

เอกสารทางการของ Python Standard Library:
https://docs.python.org/3/library/

### Module 1: datetime
- ใช้จัดการวันที่และเวลา
- ตัวอย่างการใช้งาน: แสดงวันที่ปัจจุบันหรือคำนวณระยะเวลาระหว่างวันสองวัน

```python
import datetime

today = datetime.date.today()
print("Today's date:", today)
```

### Module 2: os
- ใช้ทำงานที่เกี่ยวข้องกับระบบปฏิบัติการ เช่น ตรวจสอบโฟลเดอร์หรือดูไฟล์ในโฟลเดอร์
- ตัวอย่างการใช้งาน:

```python
import os

print("Current folder:", os.getcwd())
print("Files in current folder:", os.listdir())
```

### Module 3: collections
- มีโครงสร้างข้อมูลเพิ่มเติม เช่น `Counter` สำหรับนับจำนวนครั้งที่ข้อมูลปรากฏ
- ตัวอย่างการใช้งาน:

```python
from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(Counter(words))
```

## 3. Short Discussion Conclusion

การแบ่งโปรแกรมเป็นฟังก์ชันและโมดูลช่วยให้โค้ดเป็นระเบียบ นำกลับมาใช้ซ้ำได้ และทดสอบหรือแก้ไขได้ง่ายขึ้น ส่วน Standard Library ช่วยให้เราใช้ความสามารถที่ Python มีให้แล้ว โดยไม่ต้องเขียนทุกอย่างขึ้นมาใหม่
