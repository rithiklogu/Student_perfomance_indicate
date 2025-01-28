from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file and returns a list of dependencies.
    Removes '-e .' if present in the requirements file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='student_performance_analysis',
    version='0.0.1',
    author='Rithik',
    author_email='rithiklogu.bh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
