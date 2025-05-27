from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings


def get_rag_chain():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(persist_directory="vectorstore", embedding_function=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True
    )
    return qa_chain
