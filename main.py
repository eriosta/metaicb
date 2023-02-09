from pytrials.client import ClinicalTrials
import re
import pandas as pd
# https://pytrials.readthedocs.io/en/latest/_modules/pytrials/client.html#ClinicalTrials.get_study_fields

ct = ClinicalTrials()

fields = ["NCTId", "Condition", "BriefTitle", "OfficialTitle","Keyword","Phase",
            "WhyStopped","PrimaryOutcomeDescription","PrimaryOutcomeMeasure","IsFDARegulatedDrug",
            "InterventionDescription","InterventionName","InterventionOtherName","InterventionType",
            "EligibilityCriteria","EnrollmentCount","StartDate",'LastKnownStatus',"LastUpdatePostDate","ReferenceCitation"]

search="(Immune-checkpoint inhibitor+PD-L1+PD-1)"

# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
tmp = ct.get_study_fields(
    search_expr=search,
    fields=fields,
    max_studies=1000,
    fmt="csv")
# Get the count of studies related to Coronavirus and COVID.
# ClinicalTrials limits API queries to 1000 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records

tmp = pd.DataFrame.from_records(tmp[1:], columns=tmp[0])#.to_csv("ClinicalTrials_ICB_PDL1_PD1_N_246.csv")

#pd1
r'PD-1|PD1|Programmed death-1|Programmed death 1|nivolumab|opdivo|ono-4538|MDX-1106|BMS-936558|nivo|pembrolizumab|keytruda|SCH900475|MK-3475|lambrolizumab'
# pdl1
r'Programmed death ligand-1|Programmed death ligand 1|PD-L1|PDL1|atezolizumab|tecentriq|RO5541267|MPDL3280A|RG7446|durvalumab|imfinzi|MED 4736|MED-4736|avelumab|MSB0010718C|cemiplimab|libtayo|REGN2810'

pd1_pattern = re.compile(r'PD-1|PD1|Programmed death-1|nivolumab|opdivo|ono-4538|MDX-1106|BMS-936558|nivo|pembrolizumab|keytruda|SCH900475|MK-3475|lambrolizumab', re.IGNORECASE)
pdl1_pattern = re.compile(r'Programmed death ligand-1|PD-L1|PDL1|atezolizumab|tecentriq|RO5541267|MPDL3280A|RG7446|durvalumab|imfinzi|MED 4736|MED-4736|avelumab|MSB0010718C|cemiplimab|libtayo|REGN2810', re.IGNORECASE)

regex_list = [pd1_pattern,pdl1_pattern]

# create list of regular expressions
# regex_list = [re.compile(r'hello|hi', re.IGNORECASE), re.compile(r'goodbye|goodnight', re.IGNORECASE)]

# create function to check for match with regex




def check_match(text, regex_list):
    istrueforregex1 = False
    istrueforregex2 = False
    if regex_list[0].search(text):
        istrueforregex1 = True
    if regex_list[1].search(text):
        istrueforregex2 = True
    if istrueforregex1 and istrueforregex2:
        return "Both"
    elif istrueforregex1:
        return "AntiPD1"
    elif istrueforregex2:
        return "AntiPDL1"
    else:
        return "None"

def match_regex(df, columns, regex_list):
    # Compile the regular expressions for faster matching
    regex1 = regex_list[0]
    regex2 = regex_list[1]

    for column in columns:
        df[column + "_result"] = "None"
        for index, row in df.iterrows():
            text = row[column]
            result = check_match(text, [regex1, regex2])
            df.at[index, column + "_result"] = result

    return df

regex_list = [pd1_pattern,pdl1_pattern]
columns = [col for col in tmp.columns if col.startswith("Intervention")]
result = match_regex(tmp, columns, regex_list)
print(result)
result.to_csv("ClinicalTrials_ICB_PDL1_PD1_N_246.csv")


# tmp.to_csv("ClinicalTrials_ICB_PDL1_PD1_N_246.csv")

