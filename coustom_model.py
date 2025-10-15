from strands import Agent
from strands.models.ollama import OllamaModel

ollama_model = OllamaModel(
    model_id="llama3",
    host="http://localhost:11434"
)

agent = Agent(model=ollama_model)

agent("hi")