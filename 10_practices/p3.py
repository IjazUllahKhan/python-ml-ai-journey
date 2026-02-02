# import libraries
from youtube_transcript_api import YouTubeTranscriptApi,YouTubeTranscriptApiException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()
import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import FAISS



# document ingestion

yttapi = YouTubeTranscriptApi()

ytvedioData = yttapi.fetch("q4YBbyyu9mk")

result1 = " ".join(snippet.text for snippet in ytvedioData)

# print(result)


# text splitting

splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200 )


result2 = splitter.create_documents([result1])

# print(result2[0])


# embedding generation and vector store

embeddingModel = HuggingFaceEndpointEmbeddings(huggingfacehub_api_token=os.getenv("HF_TOKEN"),model="sentence-transformers/all-MiniLM-L6-v2")

# vectorStore = FAISS.from_documents(result2,embeddingModel)

# vectorStore.save_local("my_faiss_store")

loadedStore = FAISS.load_local(
    folder_path="my_faiss_store",
    embeddings= embeddingModel,
    allow_dangerous_deserialization= True
)

# secret mapping dictionary created by langchain
# print(vectorStore.index_to_docstore_id)

# print(vectorStore.get_by_ids(["c934822d-6d72-474a-87b9-38feb50b7c0a"]))


# Retriever



retriever = loadedStore.as_retriever(search_type = "similarity",search_kwargs = {"k": 2})

print(retriever.invoke("Computer SCience"))






# result3 = embeddingModel.embed_query("hello")

# print(len(result3))