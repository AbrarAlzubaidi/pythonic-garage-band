from abc import ABC, abstractmethod


class Band():
    Allmembers=[]
    def __init__(self,name,members=[]):
        self.name=name
        self.members=members
        # Band.Allmembersll.append(self.members)

    def play_solos(self):
        return ["face melting guitar solo","bom bom buh bom","rattle boom crash"]

    def __str__(self):
        return f"Band name: {self.name}"

    def __repr__(self):
        return f"Band name: {self.name}"

    @classmethod
    def to_list(cls):
        return cls.Allmembers



class Musician():
    
    def __init__(self,name):
        self.name=name
        Band.Allmembers.append(name)

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    @abstractmethod
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    @staticmethod
    def play_solo():
        return "face melting guitar solo"

class Bassist(Musician):
   def __str__(self):
        return f"My name is {self.name} and I play bass"

   def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

   def get_instrument(self):
        return "bass"

   @staticmethod
   def play_solo():
        return "bom bom buh bom"

class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    @staticmethod
    def play_solo():
        return "rattle boom crash"



if __name__ == "__main__":
    smoother = Band("Smoother") 
    print("Band name: ",smoother.name)
  

    joan = Guitarist("Joan Jett")
    print("Guitarist name: ",joan.name)
    print(joan.get_instrument())

    sheila = Drummer("Sheila E.")
    print("Drummer name: ",sheila.name)
    print(sheila.get_instrument())

    meshell = Bassist("Meshell Ndegeocello")
    print("Bassist name: ",meshell.name)
    print(meshell.get_instrument())

    print("\n members: ", smoother.members)
