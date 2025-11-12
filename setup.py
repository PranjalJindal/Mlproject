from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_parh:str)->List[str]:


    requirements=[]
    with open(file_parh) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name='Mlproject',
    version='0.0.1',
    author='Pranjal Jindal',
    author_email='pranjaljindal06@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)