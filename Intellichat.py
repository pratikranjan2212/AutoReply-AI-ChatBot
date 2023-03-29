import openai
from dotenv import load_dotenv

openai.api_key = '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'
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question,chat_log = None):
    chat_log_path = "Database\\chat_log.txt"
    FileLog = open(chat_log_path,"r")
    chat_log_template = FileLog.read()
    FileLog.close()

    if chat_log is None:
        chat_log = chat_log_template

        prompt = (f'{chat_log}You : {question}\nJarvis : ')
        response = completion.create(
            model = "text-davinci-002",
            prompt = prompt,
            temperature = 0.5,
            max_tokens = 60,
            top_p = 0.3,
            frequency_penalty = 0.5,
            presence_penalty = 0)
        answer = response.choices[0].text.strip()

        chat_log_template_update = chat_log_template + f"\nYou : {question} \nJarvis : {answer}"
        chat_log_path = "Database\\chat_log.txt"
        FileLog = open(chat_log_path,"w")
        FileLog.write(chat_log_template_update)
        FileLog.close()
        return answer

while True:
    print(ReplyBrain(input('Enter :')))