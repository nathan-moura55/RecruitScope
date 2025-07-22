from setuptools import setup, find_packages

setup(
    name="recruitscope",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "recruitscope = github_user.main:main"
        ]
    },
    author="Nathan de Moura",
    description="CLI tool to analyze GitHub user activity for recruitment",
    url="https://github.com/nathan-moura55/RecruitScope",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)