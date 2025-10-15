from strands import Agent
from strands_tools import http_request

agent = Agent(tools=[http_request])

agent("what is current time ?")