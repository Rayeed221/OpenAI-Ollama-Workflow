from openai import OpenAI
from langchain_ollama import OllamaLLM
from datetime import datetime

# Set your OpenAI API key
client = OpenAI(api_key = "YOUR_API_KEY")

# Function to call qwen2.5:1.5b model locally from your PC - (for making/modifying prompts)
def qwen_prompt_maker(msg):
    engine = OllamaLLM(model="qwen2.5:1.5b")  
    print("qwen2.5:1.5b | Generating prompt --------------------")
    response = engine.invoke(input = f"Create detailed prompt by being me. The message is [{msg}]. 
                            \nUnderstand the context and key-points and wants of the message. 
                            Then create a prompt withit within 200 words")
    # print(response.strip())                      
    return response

# Function to call qwen2.5:1.5b model locally from your PC - (for creating/improving outline)
def qwen_outline_maker(msg):
    engine = OllamaLLM(model="qwen2.5:1.5b")  
    print("qwen2.5:1.5b | Generating Outline -------------------")
    response = engine.invoke(input = f"Create detailed outline/ Add details on the outline.       
                             If there is an existing outline, add more details, information 
                             and  data which is not mentioned in the prompt and add 
                             (relavent/necessary/good to have) topics into the outline. 
                             Mention every key-terms and add more if have any. 
                             prompt/outline is: \n[{msg}]")
    # print(response.strip())
    return response


# Function to call llama3.2 model locally from your PC
def llama_model(data):
    engine = OllamaLLM(model="llama3.2")  
    print("llama3.2 | Adding Information -------------------")
    response = engine.invoke(input = f"Add more specific important terms/knowledge which 
                             is not mentioned into the outline in brackets.\n[{data}]"
    )
    # print(response.strip())
    return response


# Function to call API of GPT4o-mini  
def gpt4o_mini(msg, data):

    # Create a chat completion request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system",
                   "content": """Improve outline of the outline_data by understanding the context, requirements, 
                   reasonal thinking and improvements considering the prompt of the user_message. Be precise and 
                   consice based on the wants/requirements of meesage or prompt."""},
                    {"role" : "user",
                     "content": f"The user_message is :[{msg}]. \n \n The outline_data is :[{data}]"}],
        max_tokens= 600
    )
    print("GPT4o-mini | Improving Outline --------------------",)
    response_message = response.choices[0].message.content
    # print(response_message)
    
    return response_message


# Function to call API of GPT4o    
def gpt4o(msg, data):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages = [{"role" : "system", "content": """Within 300 words and using plain text format explain every topics 
                     and the sub-topics of the outline in brackets step-by-step by understanding the wants of user_message.
                     Only use newline when You will be explaining each topic within 2-10 sentenses depending on the 
                     needs (musts, wants, good to have)."""},
                {"role" : "user",
                 "content": f"The user_message is :[{msg}]. \n The outline_data is :[{data}]"}],
        max_tokens= 800
    )
    print("GPT4o | Generating Response -----------------------")
    response_message = response.choices[0].message.content
    return response_message.strip()

# Input message of yours
msg = """ USER_MESSAGE """


# Generating a detailed prompt using qwen
qwen_prompt = qwen_prompt_maker(msg) 

# Generating and improving outline in 3x (qwen2.5 and llama3.2) loop after getting qwen_outline when i == 0
for i in range(3):
    if i == 0:
        qwen_outline = qwen_outline_maker(qwen_prompt)                   
    else:
        qwen_outline = qwen_outline_maker(llama_outline)
    llama_outline = llama_model(qwen_outline)  

# Add more details on the outline by gpt4o-mini model based on the user message
gpt4o_mini_outline = gpt4o_mini(msg, llama_outline)
 
#Generating the whole response by gp4o model based on the user message
gpt4o_response = gpt4o(msg, gpt4o_mini_outline)

# Display final output
print("Final Output: -------------------------------------")
print(gpt4o_response)


# Save the written data history into a Notepad in this directory with date and time
with open(file = r"FOLDER_ADDRESS\History.txt", mode = "a") as file:
    present_time = datetime.now()
    file.write(f"Time {present_time}\n")
    file.write(gpt4o_response)
    
    
