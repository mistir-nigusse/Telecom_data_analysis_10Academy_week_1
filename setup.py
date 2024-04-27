from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TELECOM_DATA_ANALYSIS",
    version="0.1",
    author="mistir",
    author_email="mistirnigusse00@gmail.com.com",
    description="Description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mistir-nigusse/Telecom_data_analysis_10Academy_week_1",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "matplotlib==3.8.4",
        "nltk==3.8.1",
        "numpy==1.26.4",
        "pandas==2.2.1",
        "pick==2.2.0",
        "psycopg2==2.9.9",
        "scipy==1.13.0",
        "seaborn==0.13.2",
        "SQLAlchemy==2.0.29",
        "streamlit==1.33.0",
        "python-dotenv==1.0.1",
        "scikit-learn==1.4.2"
    ],
)
