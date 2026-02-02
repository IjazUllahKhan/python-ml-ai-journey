from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
import os


llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    max_new_tokens=512,
    do_sample=False,
    repetition_penalty=1.03,
    provider="auto",  # let Hugging Face choose the best provider for you
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("capital of pakistan")

print(result)