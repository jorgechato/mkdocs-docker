from setuptools import setup

setup(
    name='mkweb',
    version='1.0.0',
    py_modules=['mkweb'],
    include_package_data=True,
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        mkweb=app.cli:cli
    ''',
)
