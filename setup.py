from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='Timestack',
    version='0.1.0',
    description='Stack based time management tool',
    long_description=readme(),
    url='https://github.com/limeburst/timestack',
    author='Jihyeok Seo',
    author_email='me@limeburst.net',
    py_modules=['timestack'],
    scripts=['timestack.py'],
    app=['timestack.py'],
)
