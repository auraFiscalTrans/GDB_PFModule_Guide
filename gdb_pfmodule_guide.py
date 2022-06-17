#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:20:27 2022

@author: esbeidytorres
"""

import pandas as pd
pfmodule_dataframe = pd.read_csv('gdb_pfmodule.csv')

###Task 1: PF Module World Rank
pfmodule_ranking = pfmodule_dataframe[pfmodule_dataframe["hierarchy_level"] == 0]
pfmodule_ranking_sorted = pfmodule_ranking.sort_values("score", ascending=False)

###Task 2: Availability Indicator World Rank 
availability_ranking = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 2) \
                        & (pfmodule_dataframe["pillar"] == "Availability") \
                        & (pfmodule_dataframe["weight"] == 100) ] 

availability_ranking_sorted = availability_ranking.sort_values("score", ascending=False)
    
###Task 3: Governance Indicator World Rank 
governance_ranking = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 2) \
                        & (pfmodule_dataframe["pillar"] == "Governance") \
                        & (pfmodule_dataframe["weight"] == 100) ] 
governance_ranking_sorted = governance_ranking.sort_values("score", ascending=False)

    
###Task 4: Accessing the full Availability Questionnaire of a Country

full_qa_france = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 4) \
                        & (pfmodule_dataframe["pillar"] == "Availability") \
                        & (pfmodule_dataframe["country"] == "France") ] 

###Task 5: Accessing the full Governance Questionnaire of a Country
full_qg_france = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 4) \
                        & (pfmodule_dataframe["pillar"] == "Governance") \
                        & (pfmodule_dataframe["country"] == "France") ] 
    
###Task 6: Comparing countries
comparing_question = pfmodule_dataframe[(pfmodule_dataframe["hierarchy_level"] == 4) \
                        & (pfmodule_dataframe["pillar"] == "Availability") \
                        & (pfmodule_dataframe["data_type"] == "response") 
                        & (pfmodule_dataframe["variable_name"] == "A.PF.BUDGETSPEND.e.e2.CROSSCUTTING")]