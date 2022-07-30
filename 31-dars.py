# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id

# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.__km
# # Natija: AttributeError: 'Avto' object has no attribute '__km'

# print(f"ID: {avto1.get_id()}")
# # Natija: ID: 1d4f39a4-3222-4682-9231-6275ca5e1bff

#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")

# avto1.add_km(1500)
# print(avto1.get_km())

# Natija: 101500

# class Avto:
#     """Avtomobil klassi"""
#     num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.num_avto += 1

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# print(avto1.num_avto)

# # Natija: 2

# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.num_avto)
# # Natija: 3

# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0 # klassga oid xususiyat
#     def __init__(self,make,model,rang,yil,narh):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         Avto.__num_avto += 1

# class Avto:
#     """Avtomobil klassi"""
#     __num_avto = 0
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
    
#     @classmethod
#     def get_num_avto(cls):
#         return cls.__num_avto

# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.get_num_avto())
# # Natija: 3


# from odamlar import Talaba
# from transport import Avto

# talaba = Talaba("Alijon","Valiyev","FA010101","N00022")
# avto = Avto("GM","Malibu","Qora",2020,40000)

# from odamlar import Talab, Shaxs

# talaba = Talaba("Alijon","Valiyev","FA010101","N00022")
# shaxs = Shaxs("Hasan","Husanov","FB0011223")

# import odamlar
# talaba = odamlar.Talaba("Alijon","Valiyev","FA010101","N00022")
# shaxs = odamlar.Shaxs("Hasan","Husanov","FB0011223")

# from odamlar import *
# talaba = Talaba("Alijon","Valiyev","FA010101","N00022")
# shaxs = Shaxs("Hasan","Husanov","FB0011223")

