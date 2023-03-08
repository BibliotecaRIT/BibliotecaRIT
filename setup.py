from setuptools import setup, find_packages
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Biblioteca RIT',
    version='1.0.8',
    url='https://github.com/BibliotecaRIT/BibliotecaRIT',
    license='MIT License',
    author='NuPESSC',
    author_email='nupessc@ufv.br',
    keywords='relevância temática, issue tracking, similaridade de cossenos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy", "sklearn"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
