from setuptools import setup, find_packages

HYPHON_E_DOT = '-e .'

def get_requirements(file_path):
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    
    if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]


setup(
    name="ml_project", 
    version="0.0.1",
    author="Harsh Parihar",
    author_email="happywwe2k@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"))
