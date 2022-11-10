import os
from typing import List

from setuptools import find_packages, setup

def find_stub_files(name: str) -> List[str]:
    result = []
    for root, _dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
            
    return result

readme = ""
with open("README.md") as file:
    readme = file.read()
    
requirements = []
with open("requirements.txt") as file:
    requirements = file.read()
    
extra_requirements = []
with open("requirements-test.txt") as file:
    extra_requirements = file.read()

setup(
    name="discord-ext-commands-types",
    version="0.1.0",
    description="Mypy stubs for `discord.ext.commands` @ discord.py",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/japandotorg/discord-ext-commands-types",
    author="Lemon Rose",
    python_requires=">=3.7",
    install_requires=requirements,
    extra_requires=extra_requirements,
    packages=["discord.ext.commands-types", *find_packages(exclude=["scripts", "tests"])],
    package_data={
        "discord.ext.commands-types": find_stub_files("discord.ext.commands-types"),
        "mypy_commands_types_plugin": ["py.typed"]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ],
    project_urls={
        "Release notes": "https://github.com/japandotorg/discord-ext-commands-types/releases",
    }
)
