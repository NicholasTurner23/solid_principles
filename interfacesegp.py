"""
Interfaces should be granularly split and be as small as possible

"""
from abc import ABC, abstractmethod

class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass

class Text(ABC):
    @abstractmethod
    def text_message(self):
        pass

class Canera(ABC):
    @abstractmethod
    def photo(self):
        pass


class BestMobilePhoneDevice(Phone, Text, Canera):
    def voice(self):
        return super().voice()
    
    def text_message(self):
        return super().text_message()
    
    def photo(self):
        return super().photo()
    

class OldSchoolMobilePhone(Phone, Text):
    def voice(self):
        return super().voice()
    
    def text_message(self):
        return super().text_message()
    

class Pager(Text):
    def text_message(self):
        return super().text_message()
