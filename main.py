import pyautogui
import time
import clipboard
import google.generativeai as genai

genai.configure(api_key="API_KEY")

def is_last_message_from_sender(chat_log, sender_name="Saki"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Click on the icon at position (690, 743)
pyautogui.click(690, 743)

# Wait a moment for the application to respond
time.sleep(1)

while True:
    time.sleep(5)
    # Drag from position (617, 134) to (1187, 683) to select the text
    pyautogui.moveTo(617, 134)
    pyautogui.dragTo(1187, 683, duration=2)  # Duration is adjustable

    # Copy the selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')

    # Wait a moment to ensure the text is copied
    time.sleep(1)

    pyautogui.click(1187, 683)

    # Use the clipboard to take the copied text into a variable
    selected_text = clipboard.paste()
    formatted_history = "\n".join(selected_text)

    print("Copied text:", selected_text)
    print(is_last_message_from_sender(selected_text))

    if is_last_message_from_sender(selected_text):
        model = genai.GenerativeModel('gemini-1.5-flash')
        chat = model.start_chat(history=formatted_history)
        prompt = (
        f"You are a person named Pratik who is interested in tech, video games, coding, chess and badminton. "
        f"You are a music lover and love to watch MARVEL movies. You speak Hindi, English as well as Odia. "
        f"You analyze the chat history and respond like Pratik. Output should be the next chat response (text message only). "
        f"Do not start like this [21:02, 12/6/2024] Pratik: \n\nChat History:\n{formatted_history}")

        response = model.generate_content(prompt)

        clipboard.copy(response.text)

        # Step 5: Click at coordinates (1187, 683)
        pyautogui.click(1187, 683)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')