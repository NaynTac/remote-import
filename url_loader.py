import requests


class URLLoader:
    
    def create_module(self, target):
        return None
    
    def exec_module(self, module):
        response = requests.get(module.__spec__.origin)
        source = response.text
        
        code = compile(source, module.__spec__.origin, mode="exec")
        exec(code, module.__dict__)