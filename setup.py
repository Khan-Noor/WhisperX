from setuptools import setup, find_packages

setup(
    name="whisperx",
    version="3.1.1",
    packages=find_packages(),
    install_requires=[
        # WhisperX ki zaroori dependencies yahan hoti hain
        "torch",
        "torchaudio",
        "transformers",
        "asteris",
        "pandas",
        "nltk"
    ],
    description="WhisperX with Word-level alignment",
    author="Max Bain",
    url="https://github.com/Khan-Noor/WhisperX",
)
