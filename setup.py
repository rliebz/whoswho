from setuptools import setup, find_packages

REQUIREMENTS = ['nameparser']
TEST_REQUIREMENTS = ['nose']

setup(
    name='whoswho',
    packages=find_packages(),
    version='0.2.1',
    description='A simple python library for determining whether '
                'two names describe the same person.',
    author='Robert Liebowitz',
    author_email='rliebz@gmail.com',
    url='https://www.github.com/rliebz/whoswho',
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
    ),
    keywords=['whoswho', 'name', 'match', 'parser']
)
