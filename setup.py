from setuptools import setup, find_packages

setup(
    name="context-sanitary",
    version="0.1.0",
    description="Garbage Collector de contexto e sincronizador de memória persistente para Agentes de IA",
    author="Antigravity & OpenCode",
    url="https://github.com/wxypereira/context-sanitary",
    packages=find_packages(),
    py_modules=["sanitary_purge"],
    package_dir={"": "scripts"},
    entry_points={
        "console_scripts": [
            "context-sanitary=sanitary_purge:main",
            "sanitary-purge=sanitary_purge:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
