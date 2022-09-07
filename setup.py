from setuptools import setup, find_packages


with open("README.md") as f:
    long_description = f.read()

setup(
    name="TSIClient",
    packages=find_packages(),
    version="3.0.1",
    license="MIT",
    description="The TSIClient is a Python SDK .",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Raa Labs",
    author_email="post@raalabs.com",
    keywords=["Time Series Insights", "TSI", "TSI SDK", "Raa Labs", "IoT"],
    install_requires=["requests", "pandas", "azure-identity"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
