from setuptools import setup, find_packages

setup(
    name="pycps",
    version="0.1.0",
    description="A python library to apply Cyclone Phase-Space (CPS) methodology proposed by Hart (2003)",
    author="Vitor Hugo de Almeida Marrafon",
    author_email="vitorhmarrafon@gmail.com",
    url="https://github.com/vhmarrafon/pycps",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)