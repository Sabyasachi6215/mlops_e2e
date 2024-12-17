''' The Setup.py file defines the configuration of the project like metadata, dependencies etc.

Summary:
-e .: Tells pip to install the current project in editable mode.
setup.py: Describes your project (name, dependencies, etc.) and makes it installable.
Why setup.py is necessary: It standardizes project packaging and makes installation and distribution easier.
'''

from setuptools import find_packages,setup # wheever __init__.py file is there, that foldfer will be considered as a package
from typing import List


def get_requirements() -> List[str]:
    '''
    This function returns a list of requirements
    '''
    requirement_lst:List[str] = []
    

    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                #Ignore empty lines and e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
   
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_lst

# print(get_requirements())

setup(
    name="NetwrokSecurity",
    version="0.0.1",
    author="Sabyasachi Ghosh",
    author_email="sabyarjit.ghosh@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()  # Dependencies
)