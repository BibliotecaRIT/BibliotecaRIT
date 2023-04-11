from setuptools import setup, find_packages
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='Biblioteca RIT',
    version='2.0.0',
    url='https://github.com/BibliotecaRIT/BibliotecaRIT',
    license='MIT License',
    author='NuPESSC',
    author_email='nupessc@ufv.br',
    keywords='relevância temática, issue tracking, similaridade de cossenos',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy","scikit-learn"],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
