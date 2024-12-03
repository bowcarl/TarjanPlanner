from setuptools import setup, find_packages

setup(
    name="ACIT4420-TarjanPlanner",
    version="0.1",
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in (if any)
    description="A planning tool to calculate the shortest path and based on transportation mode, calculate cost and time.",
    author="Carl Petter Mørch-Reiersen",
    author_email="camor2778@oslomet.no",
    install_requires=[
       "geopy",
       "networkx",
       "matplotlib"
    ],
    entry_points={
        'console_scripts': [
            'TarjanPlanner=TarjanPlanner.__main__:main',  # Points directly to the main function in main.py
        ],
    },
)
