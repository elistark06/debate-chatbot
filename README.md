# debate-chatbot
---


## GETTING STARTED

> this app requires an anthropic API key,
> 
> you can get your anthropic api key here: https://console.anthropic.com


### Heres a guide to setting up your anthropic API key:

REFERENCE THE ACCESSING THE API SECTION AND MOVE TO THE CONSOLE TO SETUP YOUR ACCOUNT AND KEY

https://docs.anthropic.com/en/api/overview#accessing-the-api


### After setting up your API key:

#### initialize a virtual machine:

> in your terminal while in the project directory input:
>
> `py -m venv .venv`
>
> this adds a new directory for your vm
> 
> now activate it by inputting:
>
> `./.venv/scripts/activate`

#### install requirements.txt:

> in your terminal while in the project directory input:
> 
> `py -m pip install -r requirements.txt`

#### add .env file and api key:

> in the project directory add a file named .env
> 
> in this file add a new environment variable like this
>
> `ANTHROPIC_API_KEY=your-api-key`
>
> this is adding an environment variable that lets you address the anthropic api using your key

#### FINALLY:
> run the program using a python debugger,
> 
> in the console a response from the llm should be printed
