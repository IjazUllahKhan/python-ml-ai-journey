import langchain_huggingface
from youtube_transcript_api import  YouTubeTranscriptApi, YouTubeTranscriptApiException
from langchain_text_splitters import RecursiveCharacterTextSplitter

from dotenv import load_dotenv
load_dotenv()
import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings


ytt_api = YouTubeTranscriptApi()


# Deprecated
# from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
# model = HuggingFaceInferenceAPIEmbeddings(
#     api_key= os.getenv("HF_TOKEN"),
#     model_name="Qwen/Qwen3-Embedding-0.6B"
# )


model = HuggingFaceEndpointEmbeddings(huggingfacehub_api_token=os.getenv("HF_TOKEN"),model="sentence-transformers/all-MiniLM-L6-v2")


print(model)

text = "hello"

embed = model.embed_query(text)

print(embed)


print("hello")

# try:
#     result =  ytt_api.fetch("q4YBbyyu9mk",languages=['ar','en'])
#     result2 = result.to_raw_data()
#     finalResult = "".join(snippet.text for  snippet in result)

   


# #  checking all available transcript for video
#     # lan = ytt_api.list("q4YBbyyu9mk")
#     # print(lan)
# except YouTubeTranscriptApiException as e:
#     print(e)

# # Text splitter
# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# chunks = splitter.create_documents([finalResult])





