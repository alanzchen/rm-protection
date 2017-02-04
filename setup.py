import codecs
from setuptools import setup


with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rm_protection",
    version="0.0.3",
    license='MIT',
    description="A safe alternative for \"rm\" with minimum difference.",
    author='Alan Chen',
    author_email='me@zenan.ch',
    url='https://github.com/alanzchen/rm-protection',
    packages=['rm_protection'],
    package_data={
        'rm_protection': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    entry_points={
        'console_scripts': [
            'rm-p=rm_protection.rm_p:protected_rm',
            'protect=rm_protection.protect:protect_file',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: System',
    ],
    long_description=long_description,
)