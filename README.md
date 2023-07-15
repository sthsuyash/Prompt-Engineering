# ChatGPT Prompt Engineering for Developers

This is a repository for the ChatGPT prompt engineering project. The goal of this project is to create a tool that can be used to generate prompts for a variety of different tasks. The prompts are generated using a `ChatGPT-3.5 turbo` model. The model is then used to generate prompts for a given task.

This is from [course](https://learn.deeplearning.ai/?_gl=1*ggepyo*_ga*MTk5MjU1NDY1NS4xNjgzMzg2OTM2*_ga_PZF1GBS1R1*MTY4NTQ3NzMzNi4zLjAuMTY4NTQ3NzM0Ny40OS4wLjA.) by **DeepLearning.AI** and **OpenAI.**

I have made own modifications to the project and is not the same as the original project code in the course.

## Description

LLM (Large Language Model) is a model that can be used to generate text in a variety of different languages. The model is trained on a large corpus of text.

There are two types of language models(LLM):

1. ### Base LLM

   Predicts the next word in a sequence of words based on text training data.

   Gives what is the next most likely word to be followed.

   Eg.

   1. <span style="color:red">Once there lived two</span> <span style="color:green">person in a village who were very poor.</span>

   2. <p style="color:red">What is the tallest mountain in the world?</p>
      <p style="color:green">How tall is the tallest mountain in the world?</p>

2. ### Instruction Tuned LLM

   Fine-tunes on instructions and good attempts at following those instructions.

   used RLHF (Reinforcement Learning from Human Feedback) to fine-tune the model.

   Helpful, Honest, Harmless

   1. <p style="color:red">What is the tallest mountain in the world?</p>
      <p style="color:green">Mount Everest is the tallest mountain in the world.</p>

## Installation

To install the project, you will need to clone the repository and install the following requirements:

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

To use the project, you will need to run the Jupyter Notebook. There are various topics covered in this project. Each topic is covered in a separate notebook. The notebooks are located in the root directory of the project.

## Projects

- [Principles of Prompting](./principles_of_prompting.ipynb)
- [Summarization](./summarization.ipynb)
- [Inference](./inference.ipynb)
- [Transformation](./transformation.ipynb)
- [Expanding](./expanding.ipynb)
- [Chatbot](./chatbot.ipynb)

## Iterative Prompt Development

The process of prompt development is iterative. The process is as follows:

- Idea
- Implementation(Code/Data) Prompt
- Experimental result
- Error Analysis
  and repeat
