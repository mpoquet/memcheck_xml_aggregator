from setuptools import setup, find_packages

readme = open('README.md').read()
requirements = []
version = '0.1.0'

setup(
    name='memcheck_xml_aggregator',
    author="Millian Poquet",
    author_email='millian.poquet@gmail.com',
    version=version,
    url='https://github.com/mpoquet/memcheck_xml_aggregator',
    packages=find_packages(),
    install_requires=requirements,
    zip_safe=False,
    description="Aggregate information from Valgrind's Memcheck XML output.",
    long_description=readme,
    keywords=['parsing', 'test', 'valgrind', 'memcheck'],
    license='GPL3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
