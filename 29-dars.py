# XUSUSIYATLARGA STANDART QIYMAT BERISH
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi

# STANDART QIYMATNI O'ZGARTIRISH

# talaba1.bosqich= 2
# print(talaba1.bosqich)
# Natija: 2

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich talabasi

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 2-bosqich talabasi

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich talabasi

# OBYEKTLAR O'RTASIDA MUNOSABAT
# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# # Natija: 3

# print(matematika.talabalar)
# Natija: [<__main__.Talaba object at 0x000001AB08939588>, <__main__.Talaba object at 0x000001AB089397C8>, <__main__.Talaba object at 0x000001AB087D9F08>]

# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]

# [talaba.get_info() for talaba in self.talabalar]

# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# ['Alijon Valiyev. 1-bosqich talabasi ', 'Hasan Alimov. 1-bosqich talabasi ', 'Akrom Boriyev. 1-bosqich talabasi ']

# NUQTA YOKI METOD?
# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
      
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1    
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil

# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni

# OBYEKTNING XUSUSIYATLARI VA METODLARINI KO'RISH
# dir() funksiyasi
# >>> dir(Talaba)
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'get_age',
#  'get_fullname',
#  'get_info',
#  'get_lastname',
#  'get_name',
#  'set_bosqich',
#  'update_bosqich']

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
# # Natija: ['get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'set_bosqich', 'update_bosqich']
# print(see_methods(talaba1))
# Natija: ['bosqich', 'familiya', 'get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'ism', 'set_bosqich', 'tyil', 'update_bosqich']

# __dict__ METODI
# print(talaba1.__dict__)
# Natija: {'ism': 'Alijon', 'familiya': 'Valiyev', 'tyil': 2000, 'bosqich': 1}
# print(talaba1.__dict__.keys())
# Natija: dict_keys(['ism', 'familiya', 'tyil', 'bosqich'])
