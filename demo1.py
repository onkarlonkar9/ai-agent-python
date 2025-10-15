from strands import Agent

agent = Agent(model="amazon.titan-text")  # Replace with a model you have access to
response = agent("What is the current time?")
print(response)
