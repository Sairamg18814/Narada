from setuptools import setup, find_packages

setup(
    name='agenticSeek',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': ['agentic-seek=agentic_seek.cli:main']
    },
)

