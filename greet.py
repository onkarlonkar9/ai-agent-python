from strands import Agent, tool

@tool
def greet(name) -> str:
    return f"hello desto, kya haal chaal hai {onkar}"

agent = Agent(tools=[greet])
agent("Greet onkar with some josh!")