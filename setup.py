from setuptools import find_packages, setup 

setup(
    name="Invoice_Extractor",
    version="0.0.2",
    author="Dhruv Pamneja",
    author_email="dpamneja@gmail.com",
    install_requires = ["google-generativeai","streamlit","python-dotenv","openai"],
    packages=find_packages()
)