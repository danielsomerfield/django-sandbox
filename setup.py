from setuptools import setup

setup(
    name='petapp',
    packages=['petapp'],
    include_package_data=False,
    install_requires=[
        'Django',
        'requests',
        'requests_oauthlib'
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
