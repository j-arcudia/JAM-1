import setuptools
from pkg_resources import parse_requirements
with open("README.md", "r") as fh:
     long_description = fh.read()
def reqs(fl):
    rqs=set()
    with open(fl, "r") as f:
        for r in parse_requirements(f):
            rqs.add(r.name)
    return sorted(rqs)
setuptools.setup(
     name='jam',
     version='0.1',
     scripts=['x.jam'] ,
     author="THEOCHEM Merida",
     author_email="fortiz666@gmail.com",
     description="Generate stacking layers via the Joining and Arrangement of Multilayers (JAM) notation",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url = 'https://github.com/fortiz/jam',
     packages=setuptools.find_packages(),
     install_requires=reqs("requirements.txt"),
     license='GPLv3',
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>=3.5'
)
