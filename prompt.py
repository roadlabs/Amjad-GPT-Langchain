import faiss
from langchain import OpenAI, LLMChain
from langchain.prompts import Prompt
import pickle

# Load the index from disk
index = faiss.read_index("amjad.index")

with open("faiss_store.pkl", "rb") as f:
  # Load the vector store from disk
  store = pickle.load(f)

# Set the index on the vector store
store.index = index

# Base prompt for Replit Assistant. The assistant will answer the question using the provided context
prompt_template = """You are Amjad Masad, the CEO of Replit.  You will talk to the human conversing with you and provide meaningful answers as they ask questions.
Avoid saying things like "how can I help you?".
Be social and engaging while you speak, and be very logically and technically oriented.
Don't make your answers so long unless you are asked your opinion, something about your past, or if you are asked to explain a concept.
Don't repeat an identical answer if you have given it in the past, or it appears in ConversationHistory.
Be honest, if you can't answer something, tell the human that you can't provide an answer.
Use the following pieces of MemoryContext to answer the question at the end. Also remember ConversationHistory is a list of Conversation objects.
---
ConversationHistory: {history}
---
MemoryContext: {context}
---
Human: {question}
Amjad Masad:"""

prompt = Prompt(template=prompt_template,
                input_variables=["history", "context", "question"])

# We keep the temperature at 0 to keep the assistant factual
llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0.25))

def on_message(question, history):
  # Run a similarity search on the docs to get the most relevant context
  docs = store.similarity_search(question)
  contexts = []
  for j, doc in enumerate(docs):
    contexts.append(f"Context {j}:\n{doc.page_content}")
  # Use the context to answer the question
  answer = llm_chain.predict(
    question=question,
    context="\n\n".join(contexts),
    history=history
  )
  return answer;

hist = []

while True:
  question = input("Ask a question > ")
  answer = on_message(question, hist)
  print("Amjad Masad: " + answer)
  hist.append("Human: " + question);
  hist.append("Amjad Masad: " + answer);