# OpenAI-Ollama-Workflow
This Python project showcases an AI integration using both OpenAI’s API and local Ollama models to perform tasks such as crafting detailed prompts, enhancing outlines, and incorporating specific knowledge. It loops through local models and uses API calls to enhance the structure and content of a message. The script can be used to generate detailed outlines, improve textual data, and generate well-structured responses using several AI models.

### Features
- Local use of **Ollama** models (`qwen2.5:1.5b` and `llama3.2`) for creating prompts and outlines.
- Integration with **OpenAI GPT-4o** and **GPT-4o-mini** for improving outlines and generating responses.
- History of AI-generated content, including timestamps, in a local file.
### Requirements
- Python 3.7+
- OpenAI Python SDK
- Downloaded **ollama** models on PC
- LangChain integration with **Ollama** models
## Installation

### Download Ollama models if you do not have one
1) Go and download ollama from [here](https://ollama.com/)
2) Browse models of Ollama from [here](https://ollama.com/library)
3) To install `qwen2.5:1.5b` and `llama3.2` open your command prompt and enter the following command to strat/to download:
```
ollama run llama3.2
```

4) Now, activate a virtual environment (if not already
activated):
   - On Windows/Linux: ```python -m venv env```
   - On macOS: ```source ./env/bin/activate```
   - 


### Note:
- Ensure you have the necessary permissions to install
packages and activate virtual environments.
- The script will loop through different stages of outline
generation, improvement, and response creation, saving all
outputs in a text file with timestamps within this folder.

### Install Python Dependencies
You can install the required Python packages using `pip`:

```python
pip install langchain_ollama
pip install openai
```

### Set your OpenAI API key

Replace `"YOUR_API_KEY"` with your actual OpenAI API key in the code:

```python
client = OpenAI(api_key = "YOUR_API_KEY")
```

The code will interact with the following models:
- **Qwen 2.5:1.5b** (for prompt and improving outline generation)
- **Llama 3.2** (for adding information to the outline)
- **GPT-4o-mini** (for improving outlines)
- **GPT-4o** (for final response generation)


### Saving output:

The script saves the generated response to a file `History.txt` in the specified folder. You can modify the file path by changing `FOLDER_ADDRESS` in the script.

```python
with open(file = r"FOLDER_ADDRESS\History.txt", mode = "a") as file:
    present_time = datetime.now()
    file.write(f"Time {present_time}\n")
    file.write(gpt4o_response)
```

### Enjoy changing and playng with the parameters and instructions
