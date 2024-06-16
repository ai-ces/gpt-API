import openai 

openai.api_key = "" # api key here

while True:

    model_engine = "" # model engine here

    prompt = input(":")

    if 'exit' in prompt or 'quit' in prompt: 
        break


    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n=1,
        stop = None,
    )

    response = completion.choice[0].text

    print(response)