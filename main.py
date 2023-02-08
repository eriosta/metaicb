from pytrials.client import ClinicalTrials
import pprint as pp
import pandas as pd
# https://pytrials.readthedocs.io/en/latest/_modules/pytrials/client.html#ClinicalTrials.get_study_fields

ct = ClinicalTrials()

# Get 50 full studies related to Coronavirus and COVID in json format.
# response = ct.get_full_studies(search_expr="Immune-checkpoint inhibitor+PD-L1+PD-1", max_studies=50)

# for k,v in response.items():
#     for a,b in v.items():
#         pp.pprint(b)
#     break

# for field in ct.study_fields:
#     print(field)

for i in list(ct.study_fields):
    print(i)

# Get the NCTId, Condition and Brief title fields from 500 studies related to Coronavirus and Covid, in csv format.
tmp = ct.get_study_fields(
    search_expr="(Immune-checkpoint inhibitor+PD-L1+PD-1)",
    fields=["NCTId", "Condition", "BriefTitle", "OfficialTitle","Keyword","Phase",
            "WhyStopped","PrimaryOutcomeDescription","PrimaryOutcomeMeasure","IsFDARegulatedDrug",
            "InterventionDescription","InterventionName","InterventionOtherName","InterventionType",
            "EligibilityCriteria","EnrollmentCount","StartDate",'LastKnownStatus',"LastUpdatePostDate","ReferenceCitation"],
    max_studies=500,
    fmt="csv",
)
# Get the count of studies related to Coronavirus and COVID.
# ClinicalTrials limits API queries to 1000 records
# Count of studies may be useful to build loops when you want to retrieve more than 1000 records

search="immune checkpoint inhibitor"
# ct.get_study_count(search_expr=search)

pd.DataFrame.from_records(tmp[1:], columns=tmp[0]).to_csv("ClinicalTrials_ICB_PDL1_PD1_N_246.csv")

import re

keywords = "nivolumab|opdivo|ono-4538|MDX-1106|BMS-936558|nivo|pembrolizumab|lambrolizumab|keytruda|SCH900475|MK-3475|atezolizumab|tecentriq|RO5541267|RG7446|MPDL3280A|durvalumab|imfinzi|MEDI-4736|MEDI4736|avelumab|barvencik|MSB0010718C|cemiplimab|libtayo|REGN2810"
pattern = re.compile(r"\b(" + keywords + ")\b")


ct.get_study_count(search_expr=search)


keywords = "Programmed death-1|PD-1|PD1|Programmed death ligand-1|PD-L1|PDL1|checkpoint inhibitor|checkpoint blockade"
pattern = re.compile(r"\b(" + keywords + ")\b")
