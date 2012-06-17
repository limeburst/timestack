from setuptools import setup
try:
    import py2exe
except ImportError:
    pass

setup(
        name='Timestack',
        version="0.1",
        description="Stack based time management tool.",
        long_description=open("README").read(),
        author="Jihyeok Seo",
        author_email="me@limeburst.net",
        url="http://github.com/limeburst/timestack",
        py_modules=["timestack"],
        scripts=["timestack.py"],
        app=['timestack.py'],
        windows=['timestack.py'],
        )
