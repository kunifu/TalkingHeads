from src.talkingheads import ChatGPTClient
import time
import getpass

def execute_prompt(chathead, prompt):
    response = chathead.interact(prompt)
    # 文脈をリセット
    chathead.reset_thread()
    return response


if __name__ == "__main__":
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    chathead = ChatGPTClient(
      username=username,
      password=password,
      headless=False,
    )
    prompts = [
        "Without any explanation or extra information, just repeat the following: book.",
        "Without any explanation or extra information, type three animal names.",
        "Without any explanation or extra information, type three colors.",
        "Without any explanation or extra information, type three countries.",
        "Without any explanation or extra information, type three food items.",
    ]
    for prompt in prompts:
        print(execute_prompt(chathead, prompt))
        time.sleep(0.3)
    del chathead