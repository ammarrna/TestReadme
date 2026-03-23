```mermaid
graph LR
    subgraph "Source Columns"
    CRM_Portal_CLM_HDR_CLAIM_ID[CLM_HDR.CLAIM_ID]
    CRM_Portal_CLM_HDR_SUBMIT_DT[CLM_HDR.SUBMIT_DT]
    ERP_System_PART_MST_PART_NO[PART_MST.PART_NO]
    IoT_Hub_SENS_DATA_ERR_CODE[SENS_DATA.ERR_CODE]
    CRM_Portal_CLM_DTL_LABOR_HRS[CLM_DTL.LABOR_HRS]
    Manual_Entry_ADJ_NOTES_REASON[ADJ_NOTES.REASON]
    end

    subgraph "Target Columns"
    FACT_WARRANTY_Claim_Key[Claim_Key (Integer)]
    FACT_WARRANTY_Submission_Date[Submission_Date (Date)]
    DIM_PARTS_Part_SKU[Part_SKU (Varchar)]
    FACT_WARRANTY_Diagnostic_Code[Diagnostic_Code (Varchar)]
    FACT_WARRANTY_Labor_Cost[Labor_Cost (Decimal)]
    FACT_WARRANTY_Adjustment_Reason[Adjustment_Reason (String)]
    end

    CRM_Portal_CLM_HDR_CLAIM_ID -- "Hash of Claim_ID and Dealer_ID" --> FACT_WARRANTY_Claim_Key
    CRM_Portal_CLM_HDR_SUBMIT_DT -- "Convert to UTC ISO-8601" --> FACT_WARRANTY_Submission_Date
    ERP_System_PART_MST_PART_NO -- "Direct Mapping" --> DIM_PARTS_Part_SKU
    IoT_Hub_SENS_DATA_ERR_CODE -- "Map to Standard Error Catalog" --> FACT_WARRANTY_Diagnostic_Code
    CRM_Portal_CLM_DTL_LABOR_HRS -- "Labor_Hours * Standard_Rate" --> FACT_WARRANTY_Labor_Cost
    Manual_Entry_ADJ_NOTES_REASON -- "Clean special characters" --> FACT_WARRANTY_Adjustment_Reason
```
