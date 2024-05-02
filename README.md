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



Great, let's craft the installation instructions for the README file based on the provided prerequisites and steps:

### Installation Instructions

#### Prerequisites
Before getting started, ensure you have the following prerequisites installed on your system:
- Git
- Python
- PIP
- Docker & Docker Compose
- venv (Python virtual environment)

#### Steps to Install vPrompt

1. **Clone the Repository**: 
   - Create a parent folder to hold everything related to vPrompt.
   - Clone the vPrompt Git repository into the parent folder using the following command:
     ```
     git clone https://github.com/reenphygeorge/vPrompt.git
     ```

2. **Setup Python Virtual Environment (venv)**:
   - Navigate to the parent folder where the vPrompt repository was cloned.
   - Install the `venv` module (if not already installed) by executing:
     ```
     python -m venv env
     ```
     or
     ```
     python3 -m venv env
     ```

3. **Activate the Virtual Environment**:
   - Activate the virtual environment. Use the appropriate command based on your operating system:
     - For Unix/Linux/macOS:
       ```
       source env/bin/activate
       ```
     - For Windows (PowerShell):
       ```
       .\env\Scripts\Activate.ps1
       ```
     - For Windows (Command Prompt):
       ```
       .\env\Scripts\activate.bat
       ```

4. **Install Requirements**:
   - With the virtual environment activated, install the required packages and dependencies by running:
     ```
     pip install -r api/requirements.txt
     ```
     This will install all the necessary packages listed in the `requirements.txt` file, including `ultralytics` and others.

5. **Start Using vPrompt**:
   - Once all dependencies are installed successfully, you can start using vPrompt.

### Additional Notes
- Make sure to activate the virtual environment (`env`) before running any commands related to vPrompt to ensure that the correct dependencies are used.
- If you encounter any issues during the installation process, refer to the troubleshooting section or seek assistance from the vPrompt community or developers.

Feel free to let me know if you need further clarification or if there are any additional details you'd like to include!
