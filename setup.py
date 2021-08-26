from setuptools import setup, find_packages

setup(
    name='django-bulstyle',
    version='1.7',
    description='Theme for Brown University Library Django Projects',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'django-bootstrap3',
        'requests',
    ],
)
