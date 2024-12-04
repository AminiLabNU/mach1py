from setuptools import setup, find_packages


setup(
    name="mach1py",
    version="1.0.0",
    description="Python parser for converting Biomomentum Mach-1 data files",
    author="Turner Jennings",
    author_email="turner.jennings@outlook.com",
    url="https://github.com/AminiLabNU/mach1py",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pandas"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
    ],
)
