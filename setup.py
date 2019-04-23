import setuptools
import stackoverflow_jobs

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=stackoverflow_jobs.__name__,
    version=stackoverflow_jobs.__version__,
    author="João Eduardo Montandon",
    author_email="edu.montandon@gmail.com",
    description="Simple wrapper for crawling jobs data at Stack Overflow"
                " Jobs portal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jemaf/stackoverflow-jobs",
    license="MIT",
    keywords=["Stack Overflow", "Jobs", "crawler"],
    packages=setuptools.find_packages(exclude=["*test*"]),
    install_requires=["requests"],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
