from distutils.log import debug
from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List


#Declaring variables for setup function
PROJECT_NAME="housing predictor"
VERSION="0.0.1"
AUTHOR="LALITA"
DESCRIPTION="This is first Machine leaning project"
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    '''
    Description: this function is going to return list of requirement 
    mention in requirements.txt file

    return : This function is going to return to list which contain 
    name of libraries mentioned in requirements.txt file 
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)

