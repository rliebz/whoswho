from setuptools import setup, find_packages

REQUIREMENTS = ['nameparser', 'fuzzywuzzy']
TEST_REQUIREMENTS = ['nose']

setup(
    name='whoswho',
    packages=find_packages(),
    version='0.1.1',
    description='A simple python library for determining whether '
                'two names describe the same person.',
    author='Robert Liebowitz',
    author_email='rliebz@gmail.com',
    url='https://www.github.com/rliebz/whoswho',
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    )
)