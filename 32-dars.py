# >>> dir(Avto)
# ['_Avto__num_avto',
#  '__class__',
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
#  'make',
#  'model',
#  'narh',
#  'rang',
#  'yil']

#  class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# print(avto1) # obyekt haqida ma'lumot
# # Natija: <__main__.Avto object at 0x00000238A6DAE0C8>

# class Avto:
#     __num_avto = 0
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1
    
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto: {self.rang} {self.make} {self.model}"

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# print(avto1)
# # Natija: Avto: Qora GM Malibu

# x,y = 5,10
# print(x>y)

# # Natija: False

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto1>avto2

# # Natija: TypeError: '>' not supported between instances of 'Avto' and 'Avto'

#     def __eq__(self,boshqa_avto):
#         """Tenglik"""
#         return self.narh == boshqa_avto.narh
    
#     def __lt__(self,boshqa_avto):
#         """Kichik"""
#         return self.narh<boshqa_avto.narh
    
#     def __le__(self,boshqa_avto):
#         """Kichik yoki teng"""
#         return self.narh<=boshqa_avto.narh

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1>avto2)

# # Natija: False

# avto3 = Avto("Honda","Accord","Oq",2017,40000)
# print(avto1==avto3)

# # Natija: True

# matn = 'hello world'
# print(len(matn))
# # Natija: 11
# sonlar = [12, 34, 56, 66]
# print(len(sonlar))
# # Natija: 4

# len(avto1)
# # Natija: TypeError: object of type 'Avto' has no len()

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"

# salon1 = AvtoSalon("MaxAvto")
# print(salon1)

# # Natija: MaxAvto avtosaloni

# >>> isinstance("salom",str)
# True # "salom" bu str
# >>> isinstance(9.5,int)
# False # 9.5 int (butun son) emas
# >>> isinstance(avto1,Avto)
# True # avto1 Avto klassiga tegishli

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def add_avto(self,avto):
#         if isinstance(avto,Avto): # agar avto Avto klassidan bo'lsa
#             self.avtolar.append(avto)
#         else:
#             print("Avto obyketini kiriting")

# # Avto obyektlarini yaratamiz
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)

# # Yuqoridagi obyektlarni salon1 ga qo'shamiz
# for avto in [avto1, avto2, avto3]: 
#     salon1.add_avto(avto)

#     def __len__(self):
#         return len(self.avtolar)

# >>> print(len(salon1))
# 3 # Salonimizda 3 ta moshina bor

# >>> mevalar = ['olma','anor','uzum']
# >>> mevalar[0]
# 'olma'
# salon1[0]

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)
    
#     def __getitem__(self,index):
#         return self.avtolar[index]

# >>> salon1[0]
# Avto: Qora GM Malibu
# >>> salon1[1]
# Avto: Oq GM Lacetti
# >>> salon1[2]
# Avto: Silver Toyota Carolla
# >>> salon1[:] # barcha elementlarni ko'rish
# [Avto: Qora GM Malibu, Avto: Oq GM Lacetti, Avto: Silver Toyota Carolla]

# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# salon1[0]=avto4
# # Natija: TypeError: 'AvtoSalon' object does not support item assignment

#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value

# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# salon1[0]=avto4
# print(salon1[0])

# # Natija: Avto: Qizil Mazda 6

# >>> x,y=10,20
# >>> x+y
# 30
# >>> x*5
# 50

# >>> t1 = "hello"
# >>> t2 = "world"
# >>> t1+t2
# 'helloworld'
# >>> t1*5
# 'hellohellohellohellohello'

# >>> l1 = [1, 2, 3]
# >>> l2 = [4, 5, 6]
# >>> l1+l2
# [1, 2, 3, 4, 5, 6]
# >>> l1*2
# [1, 2, 3, 1, 2, 3]

# class AvtoSalon:
#     """Avtosalon klassi"""
#     def __init__(self,name):
#         self.name = name
#         self.avtolar = []

#     def __repr__(self):
#         return f"{self.name} avtosaloni"
    
#     def __len__(self):
#         return len(self.avtolar)

#     def __getitem__(self,index):
#         return self.avtolar[index]
    
#     def __setitem__(self,index,value):
#         if isinstance(value,Avto):
#             self.avtolar[index]=value
    
#     def add_avto(self,*qiymat):
#         for avto in qiymat: 
#             if isinstance(avto,Avto):
#                 self.avtolar.append(avto)
#             else:
#                 print("Avto obyketini kiriting")

# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)

# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)

# salon1+salon2
# # Natija: TypeError: unsupported operand type(s) for +: 'AvtoSalon' and 'AvtoSalon'

#     def __add__(self,qiymat):
#         if isinstance(qiymat,AvtoSalon):
#             yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon

# >>> salon3 = salon1+salon2
# >>> print(salon3)
# MaxAvto Avto Lider avtosaloni
# >>> salon3[:]
# [Avto: Qora GM Malibu,
#  Avto: Oq GM Lacetti,
#  Avto: Silver Toyota Carolla,
#  Avto: Qizil Mazda 6,
#  Avto: Qora Volkswagen Polo,
#  Avto: Oq Honda Accord]

#      def __add__(self,qiymat):
#         if isinstance(qiymat,AvtoSalon):
#             yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
#             yangi_salon.avtolar = self.avtolar + qiymat.avtolar
#             return yangi_salon
#         elif isinstance(qiymat,Avto):
#             self.add_avto(qiymat)
#         else:
#             print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")

# avto7 = Avto("BMW", 'X7','Qora',2015,75000)
# salon1 + avto7
# print(salon1[:])

# >>> print(10)
# 10
# >>> len("salom")
# 5

#     def __call__(self):
#         return [avto for avto in self.avtolar]
# salon1()

#     def __call__(self,*param):
#         if param: # agar parametr bo'lsa
#             for avto in param:
#                 self.add_avto(avto)
#         else: # agar parametr bo'lmasa
#             return [avto for avto in self.avtolar]

# avto_new = Avto("Mercedes-Benz", 'E200','Silver',2015,80000)
# salon1(avto_new) # Yangi avto qo'shamiz
# salon1() # salondagi mashinalarni ko'ramiz

# # Natija: [Avto: GM Malibu. 40000$, Avto: GM Lacetti. 20000$, Avto: Toyota Carolla. 45000$, Avto: Mercedes-Benz E200. 80000$]

