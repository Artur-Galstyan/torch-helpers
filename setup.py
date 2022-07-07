from distutils.core import setup

setup(
    name="torch-helpers",  # How you named your package folder (MyLib)
    packages=["torch-helpers"],  # Chose the same as "name"
    version="0.1",  # Start with a small number and increase it with every change you make
    license="MIT",  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="This library is a helper to create and manage your machine learning datasets more effectively",  # Give a short description about your library
    author="Artur A. Galstyan",  # Type in your name
    author_email="mail@arturgalstyan.dev",  # Type in your E-Mail
    url="https://github.com/Artur-Galstyan/torch-helpers",  # Provide either the link to your github or to your website
    download_url="https://github.com/Artur-Galstyan/torch-helpers/archive/refs/tags/v0.1-alpha.tar.gz",  # I explain this later on
    keywords=[
        "pytorch",
        "torch",
        "dataset",
        "helper",
    ],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        "certifi==2022.6.15",
        "charset-normalizer==2.1.0",
        "click==8.1.3",
        "idna==3.3",
        "mypy-extensions==0.4.3",
        "numpy==1.23.0",
        "pathspec==0.9.0",
        "Pillow==9.2.0",
        "platformdirs==2.5.2",
        "requests==2.28.1",
        "tomli==2.0.1",
        "torch==1.12.0",
        "torchvision==0.13.0",
        "typing_extensions==4.3.0",
        "urllib3==1.26.9",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.9",  # Specify which pyhton versions that you want to support
    ],
)
