def process_all_pdfs(pdf_directory):
    all_documents=[]
    pdf_dir=Path(pdf_directory) #creates a path object

    pdf_files=list(pdf_dir.glob("**/*.pdf")) #find all pdf recursively from the directory path,creates a list of path objects
    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        print(f"\nProcessing:{pdf_file.name}")

        try:
            loader=PyPDFLoader(str(pdf_file)) #splits the pdf 
            documents=loader.load() #list of documents

            for doc in documents:
                doc.metadata['source_file']=pdf_file.name
                doc.metadata['file_type']='pdf'
        
            all_documents.extend(documents)
            print(f"loaded {len(documents)} pages")

        except Exception as e:
            print(f"Error:{e}")
    
    print(f"\nTotal documents loaded:{len(all_documents)}")
    return all_documents


all_pdf_documents=process_all_pdfs("../Practice/data")
    
