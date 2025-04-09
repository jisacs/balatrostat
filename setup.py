from setuptools import setup, find_packages

setup(
    name='pokerstat',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A poker statistics analysis tool',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)