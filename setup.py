from setuptools import setup, find_packages

setup(
    name="ai_text_pipeline",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "transformers",
        "sentence-transformers",
        "openai",
        "pinecone-client",
        "faiss-cpu",
        "langchain",
        "pypdf",
        "python-docx",
        "watchdog",
        "pydrive2",
        "google-auth",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "google-api-python-client"
    ],
    entry_points={
        'console_scripts': [
            'run-pipeline=src.text_pipeline:main',
        ]
    },
)
