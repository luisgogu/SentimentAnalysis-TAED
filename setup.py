from setuptools import find_packages, setup

setup(
    name='sentiment_analysis',
    packages=find_packages(),
    version='0.1.0',
    description='Sentiment Analysis project on IMDB Movie reviews dataset',
    install_requires=['torch', 'keras', 'tensorflow', 'pyngrok',
                      'sklearn', 'IPython', 'pytorch-pretrained-bert', 'pandas', 'numpy'],
    author='HeartTeam',
    license=''
)