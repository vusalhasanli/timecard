import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="westvalley-timecard", 
    version="0.0.1",
    author="author",
    author_email="mail@vhasanov.com",
    description="This is a tool to fill out weekly timecard for westvalley staffing group employees",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vusalhasanli/timecard",
    packages=['commands'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3+",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['chromedriver', 'click', 'selenium'],
    entry_points='''
            [console_scripts]
            westvalley=commands.westvalley:westvalley
    ''',
)