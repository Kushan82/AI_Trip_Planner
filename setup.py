from typing import List
from setuptools import setup, find_packages
def get_requirements() -> List[str]:
    """
    Returns a list of package requirements.
    """
    requirement_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()
            for line in lines: 
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the current directory.")

    return requirement_list
print(get_requirements())
 
setup(
    name="AI_Trip_Planner",
    version="0.1.0",
    description="A Python package for planning AI-assisted trips.",
    author="KD",
    author_email="KD@hotmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)