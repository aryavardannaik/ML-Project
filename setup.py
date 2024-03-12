from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file:str)->List[str]:
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return


setup(
    name= "ML Projecet",
    author= "Aryavardan Naik",
    version= "0.0.01",
    packages=find_packages(),
    install_requires = get_requirements("requirement.txt")
)