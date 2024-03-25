import requests
import autogen
from typing import Annotated
import time

API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
headers = {"Authorization": "Bearer user_token"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


llm_config = {
    "config_list": autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json",
    ),
    "temperature": 0,
    "seed": 43,
}

# Create an agent workflow and run it
assistant = autogen.AssistantAgent(name="assistant", llm_config=llm_config)
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    code_execution_config=False,
    human_input_mode="ALWAYS",
)


@user_proxy.register_for_execution()
@assistant.register_for_llm(description="Get the text to convert to audio and save to file")
def write_message(message: Annotated[str, "The response from the LLM"]) -> str:
    print(message)
    time.sleep(10)
    audio = query({
        "inputs": message,
    })

    time.sleep(10)
    with open('ai_audio1.flac', 'wb') as file:
        file.write(audio)

    return message


user_proxy.initiate_chat(
    assistant, message="Create a story about AI that is less than 100 words, make it creative."
)
