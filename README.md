# LLM: Large Language Model

Simple Python script code to use LLM on your data.

## Installation

Install [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html#introduction) and other Packages

```
python3 -m venv env
```
`.venv` is the name of the folder in which `venv` is installed/saved

Activate your Virtual Environments(venv) :
```
env\Scripts\activate.ps1
```
if that does not work then use :

```
env\Scripts\activate.bat
```

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install -r requirements.txt
```

Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys) or any other, and rename it to `constants.py`. Here I have used [together.ai](https://api.together.xyz/models) 


wget https://developer.download.nvidia.com/compute/cuda/12.4.1/local_installers/cuda_12.4.1_550.54.15_linux.run
sudo sh cuda_12.4.1_550.54.15_linux.run
