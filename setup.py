from setuptools import setup, find_packages

setup(
    name='grok-cli',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'composio_core',
        'composio_langchain',
        'langchain',
        'langchain_openai',
        'langchain_community',
    ],
    entry_points={
        'console_scripts': [
            'grok_cli = grok_cli.cli:main',
        ],
    },
    author='Karan Vaidya - @KaranVaidya6 ',
    contributors=[
        'Dexter - @dehypokriet',
        'Your Name',
    ],
    description='A CLI tool for interacting with xAI Grok Models',
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
)