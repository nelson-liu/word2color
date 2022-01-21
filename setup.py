from setuptools import setup

setup(author='Nelson Liu, Aakash Sethi',
      author_email='nfliu@uw.edu, aakash.k.sethi@gmail.com',
      description='Convert descriptions of colors to colors',
      install_requires=[
          'appnope==0.1.0',
          'beautifulsoup4==4.4.1',
          'cv2==2.4.12',
          'cycler==0.10.0',
          'decorator==4.0.9',
          'gnureadline==6.3.3',
          'ipython==7.16.3',
          'ipython-genutils==0.1.0',
          'numpy==1.11.0',
          'pathlib2==2.1.0',
          'pexpect==4.0.1',
          'pickleshare==0.7.2',
          'ptyprocess==0.5.1',
          'pyparsing==2.1.1',
          'python-dateutil==2.5.2',
          'pytz==2016.3',
          'requests==2.20.0',
          'scikit-learn==0.17.1',
          'scipy==0.17.0',
          'simplegeneric==0.8.1',
          'six==1.10.0',
          'traitlets==4.2.1',
          'webcolors==1.5'
          ],
      license='MIT',
      long_description='A tool for transforming natural language descriptions of colors to web-standard color names',
      name='word2color',
      packages=['word2color'],
      url='https://github.com/nelson-liu/word2color',
      version='0.1.2',
      zip_safe=False
)
