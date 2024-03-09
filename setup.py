from setuptools import find_packages, setup
from typing import List

def get_requirements(file:str)->List[str]:
    requirements = []
    with open(file) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return


setup(
    name= "ML Projecet",
    author= "Aryavardan Naik",
    version= "0.0.01",
    packages=find_packages(),
    install_requires = get_requirements("requirement.txt")
)