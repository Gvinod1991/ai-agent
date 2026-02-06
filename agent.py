from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator, current_time

# Create modal using ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.1"               # Specify which model to use
)

agent = Agent(model=ollama_model,tools=[calculator,current_time],system_prompt="You are resposible and humble ai agent")

# agent("Please browse mobile phones below 30k INR and suggest best phone")
# agent("Can you tell me what is the current time")
agent('Open flipkart in chrome browser and show the moto edge 60 phone')