from setuptools import setup

setup(
    name='.lumache',
    version='0.1.0',    
    description='asdf',
    url='',
    author='svb',
    # authors = [
    #     {name='Giulio Tesei', email='giulio.tesei@bio.ku.dk'},
    #     {name='Sören von Bülow', email='soren.bulow@bio.ku.dk'},
    #     {name='Kresten Lindorff-Larsen', email='lindorff@bio.ku.dk'}
    # ]
    license='GNU GPL3',
    packages=['lumache'],

    # include_package_data=True,
    package_data={},# '' : ['data/*.csv', 'data/*.yaml', 'data/templates/*']},

    classifiers=[
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3>=3.7,<3.11',
    ],
)
