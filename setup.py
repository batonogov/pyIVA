import setuptools
import pyIVA


with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

with open('requirements.txt', 'r', encoding='utf-8') as file:
    requirements = [c for c in file.read().split('\n') if c]

setuptools.setup(
    name='pyIVA',
    version=pyIVA.__version__,
    author='Fedor Batonogov',
    author_email='batonogov@icloud.com',
    description='IVA MCU Clients API (2.13.3)',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/batonogov/pyIVA',
    packages=setuptools.find_packages(),
    # install_requires=requirements,
    classifiers=[
      "Programming Language :: Python :: 3.10",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
