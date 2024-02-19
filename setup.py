from setuptools import setup, find_packages

setup(
    name='test-automation-libraries',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'paramiko',
    ],
    author='Kuldip Mehta',
    author_email='kulsmehta13@gmail.com',
    description='Basic libraries for test autoamtion',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kulsmehta13/test-automation-libraries',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
