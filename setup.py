from setuptools import setup

setup(name='fs_ds_util',
      version='0.3',
      description='FSteppich Data Science Utilities',
      packages=['fs_ds_util', 'fs_ds_util/tests'],
      url="https://github.com/fsteppich/fsteppich-datascience-utilities",
      author="Florian Steppich",
      author_email="fsteppich+pypi@gmail.com",
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
      zip_safe=False)
