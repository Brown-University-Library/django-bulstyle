from setuptools import setup

setup(
    name='django-bulstyle',
    version='1.4a',
    description='Theme for Brown University Library Django Projects',
    packages=['bulstyle'],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'django-bootstrap3',
        'requests',
    ],
)
