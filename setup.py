from setuptools import setup

from distutils.core import setup
setup(
  name = 'pip_install_assistant',
  packages = ['pip_install_assistant'],
  version = '0.1.0',
  license='MIT',
  description = 'Installs pip packages at runtime',
  author = 'Jake Gadaleta',
  author_email = 'jake.gads@gmail.com',
  url = 'https://github.com/gadzygadz/pip_install_assistant',
  keywords = ['pip', 'installer'],
  
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 2 - Beta',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
  ],
)