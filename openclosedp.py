"""
A class/function should be open for extension and closed for modification

"""
from abc import ABC, abstractmethod
from typing import Any

class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class Uploader(ABC):
    @abstractmethod
    def upload_file(self):
        pass


class Aws(Auth, Uploader):
    def authenticate(self) -> Any:
        auth_client = None
        return auth_client
    
    def upload_file(self) -> Any:
        return super().upload_file()
    

class Azure(Auth, Uploader):
    def authenticate(self) -> Any:
        auth_client = None
        return auth_client
     
    def upload_file(self) -> Any:
        return super().upload_file()