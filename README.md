# Prompt Engineering

This is a repository for the prompt engineering project. The goal of this project is to create a tool that can be used to generate prompts for a variety of different tasks. The prompts are generated using a ChatGPT-3.5 turbo model. The model is then used to generate prompts for a given task.

This is a course from **Deeplearning.AI** and **OpenAI.**

## Installation

To install the project, you will need to clone the repository and install the dependencies. The dependencies are:

- Python 3.11+
- Anaconda
- Jupyter Notebook
- OpenAI API key (get it in the OpenAI official website)

Since the API key is not included in the repository, you will need to create a file called `.env` in the root directory of the project. The file should contain the following:

```bash
OPENAI_API_KEY=<your key here>
```

## File Structure

```bash
./root
├── .gitignore
├── principles-of-prompting.ipynb
├── ...
├── .env => create
```

## Usage

To use the project, you will need to run the Jupyter Notebook. There are various topics covered in this project. The topics are:

- [Principles of Prompting](./principles-of-prompting.ipynb)
- [Inference](./inference.ipynb)
- [Transformation](./transformation.ipynb)
