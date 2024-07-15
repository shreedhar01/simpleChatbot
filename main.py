from audio import get_audio_input
from result import response

def chat():
  try:
    print(f"Lets chat")
    perference = input("Type your perferance (text/audio)")

    if perference.lower() == "audio":
      while True:
          sentence = get_audio_input()

          if sentence.lower() == "quit":
              break         
          response(sentence)

    elif perference.lower() == "text":
      while True:
        sentence = input("You: ")
        if sentence.lower() == "quit":
            break
        response(sentence)

    else:
       print(f"{perference} not we offer")

  except Exception as e:
    print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
  chat()
  print("Chat ended. Goodbye!")