from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    
    '''
    this function will return alist of requirements.
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    
    return requirements
        
        
setup(
     name="mlproject",
     version="0.0.1",
     author="Nischith Hegde",
     author_email="nischithhegde05@gmail.com",
     packages=find_packages(),
     install_requires=get_requirements('requirements.txt')
     )