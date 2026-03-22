import pandas as pd

def generate_mermaid_from_csv(csv_path):
    # Load the ETL Lineage Sheet
    df = pd.read_csv(csv_path)
    
    # Initialize Mermaid string with Left-to-Right orientation
    mermaid = ["graph LR"]
    
    # Define styling for different node types
    mermaid.append("    classDef job fill:#f9f,stroke:#333,stroke-width:2px;")
    mermaid.append("    classDef source fill:#e1f5fe,stroke:#01579b;")
    mermaid.append("    classDef target fill:#e8f5e9,stroke:#2e7d32;")

    for _, row in df.iterrows():
        job_id = row['Job_ID']
        job_name = row['Job_Name']
        sources = row['Source_Tables'].split(',') # Handles multiple source tables
        targets = row['Target_Tables'].split(',')
        dependency = row['Dependency']

        # 1. Create Source to Job connections
        for src in sources:
            src_clean = src.strip()
            mermaid.append(f"    {src_clean}[({src_clean})]:::source --> {job_id}[[ {job_name} ]]:::job")

        # 2. Create Job to Target connections
        for tgt in targets:
            tgt_clean = tgt.strip()
            mermaid.append(f"    {job_id} --> {tgt_clean}[({tgt_clean})]:::target")

        # 3. Create Job Dependencies (Dotted lines)
        if pd.notna(dependency) and dependency != "None":
            mermaid.append(f"    {dependency} -.-> {job_id}")

    return "\n".join(mermaid)

# --- Usage ---
# Assuming you have a 'lineage.csv' with columns: 
# Job_ID, Job_Name, Source_Tables, Target_Tables, Dependency
# mermaid_code = generate_mermaid_from_csv('lineage.csv')
# print(mermaid_code)
