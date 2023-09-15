# import setuptools

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()


# __version__ = "0.0.0"

# REPO_NAME = "Resume_Screener"
# AUTHOR_USER_NAME = "Shantanu"
# SRC_REPO = "Resume_Screener"
# AUTHOR_EMAIL = "shantanujain1507@gmail.com"


# setuptools.setup(
#     name=SRC_REPO,
#     version=__version__,
#     author=AUTHOR_USER_NAME,
#     author_email=AUTHOR_EMAIL,
#     description="APP for Resume Screener",
#     long_description=long_description,
#     url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
#     project_urls={
#         "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
#     },
#     package_dir={"": "src/Resume_Screener"},
#     packages=setuptools.find_packages(where="src/Resume_Screener")
# )

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name="Resume_Screener",
version='0.0.1',
author='Shantanu',
author_email='shantanujain1507@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)