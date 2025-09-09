import chromadb #type: ignore
import json
from LLM_model import AIAnalyst
from chromadb.config import Settings #type: ignore
from System import SmartStudentDataSystem
from Restrict import DataLoader
from pathlib import Path


# Connect to ChromaDB (defaults to local in-memory DB)

def collect_data(path, role, assign):
    ai = SmartStudentDataSystem()
    loader = DataLoader(path, silent=False)
    file_path = loader.load_data(role=role, assign=assign)
    ai.retrieve_metadata(file_path)
    return ai.collections, file_path

if __name__ == "__main__":

    data_dir = Path(__name__).resolve().parent / 'database' / 'chroma_store'
    role = "Admin"
    assign = ["Department_CCS"]

    collections = collect_data(data_dir, role, assign)
    api_mode = 'online'
    
    print(f"\n\n\n{collections}\n\n\n")
    
    try:
        with open("../config/config.json", "r", encoding="utf-8") as f:
            full_config = json.load(f)
    except FileNotFoundError:
        print("❌ config.json not found! Cannot start AI Analyst.")
    
    ai = AIAnalyst(collections=collections, llm_config=full_config, execution_mode=api_mode)
    

