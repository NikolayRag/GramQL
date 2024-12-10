from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='GramQL',
  version='0.0.1',
  author='@ki-privet',
  author_email='thenickra@gmail.com',
  description='GraphQL library which uses Telegram as a storage engine',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/NikolayRag/GramQL',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'https://github.com/NikolayRag/GramQL'
  },
  python_requires='>=3.6'
)
