def chunk_documents(documents,chunk_size=1000,chunk_overlap=200):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        seperators=["\n\n","\n"," ",""] #splits according to the seperators

    )

    split_docs=text_splitter.split_documents(documents) #returns document objects of chunks with metadata ,page_content source etc
    print(f"Split {len(documents)} documents into {len(split_docs)} chunks")

    if split_docs:
        print(f"\nExample chunk:")
        print(f"Content:{split_docs[0].page_content[:200]}...")
        print(f"Metadata:{split_docs[0].metadata}")
    
    return split_docs
