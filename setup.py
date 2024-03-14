from setuptools import setup, find_packages

setup(
    name='Aetherize',
    version='1.0.0',
    author='Brandon G. Merritt',
    author_email='brandongmerritt@gmail.com',
    description='An image compression software',
    long_description='A Python package for compressing images losslessly.',
    url='https://https://github.com/brandon-merritt/Aetherize',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'Pillow>=8.3.1',  # Pillow is a popular Python imaging library
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
