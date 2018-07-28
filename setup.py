import setuptools

setuptools.setup(
    name='snakeye',
    version='0.1',
    description='Python Packaging for Humans',
    url='https://github.com/valutac/snakeye',
    author='Valutac',
    author_email='research@valutac.com',
    license='MIT',
    packages=setuptools.find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['snakeye=snakeye.cli:main'],
    }
)
