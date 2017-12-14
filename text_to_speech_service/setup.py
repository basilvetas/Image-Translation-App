from setuptools import setup

setup(name='translation_service',
      version='0.1',
      description="Translation service that uses Google Translate API.",
      author='Jerome Kafrouni',
      author_email='j.kafrouni@columbia.edu',
      url='https://github.com/basilvetas/Image-Translation-App',
      packages=['translation_service'],
      install_requires=[
          # add here any tool that you need to install via pip 
          # to have this package working
      ],
      entry_points={
          'console_scripts': [
              'run = translation_service.__main__:main'
          ]
      },
)