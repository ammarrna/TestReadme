import pandas as pd

def generate_mermaid_from_csv(csv_path):
    # Load the ETL Lineage Sheet
    df = pd.read_csv(csv_path)
    
    # Initialize Mermaid string
    mermaid = ["graph LR"]
    
    # Styling
    mermaid.append("    classDef job fill:#f9f,stroke:#333,stroke-width:2px;")
    mermaid.append("    classDef source fill:#e1f5fe,stroke:#01579b;")
    mermaid.append("    classDef target fill:#e8f5e9,stroke:#2e7d32;")

    for _, row in df.iterrows():
        job_id = row['Job_ID'].strip()
        job_name = row['Job_Name'].strip()
        sources = str(row['Source_Tables']).split(',')
        targets = str(row['Target_Tables']).split(',')
        dependencies = str(row['Dependency']).split(',') # Split multiple dependencies

        # 1. Source to Job
        for src in sources:
            src_clean = src.strip()
            if src_clean and src_clean != 'nan':
                mermaid.append(f"    {src_clean}[({src_clean})]:::source --> {job_id}[[ {job_name} ]]:::job")

        # 2. Job to Target
        for tgt in targets:
            tgt_clean = tgt.strip()
            if tgt_clean and tgt_clean != 'nan':
                mermaid.append(f"    {job_id} --> {tgt_clean}[({tgt_clean})]:::target")

        # 3. Handle MULTIPLE Job Dependencies (Dotted lines)
        for dep in dependencies:
            dep_clean = dep.strip()
            if dep_clean and dep_clean not in ["None", "nan", "none"]:
                mermaid.append(f"    {dep_clean} -.-> {job_id}")

    return "\n".join(mermaid)

# Example Usage:
# print(generate_mermaid_from_csv('retail_lineage.csv'))
