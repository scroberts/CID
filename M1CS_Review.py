#!/usr/bin/env python3

import CID

######## CID Specific Information ##############

### M1CS Reliability Analysis
dirpath = r'/Users/sroberts/Box Sync/Python/CID/M1CS review/'
CID_coll = ['Collection-10863']
htmlfile = 'M1CS Reliability Analysis - REL04 for Signatures_MC_MS.html'
outroot = 'M1CSReliability_'

CID.make_cid(dirpath, CID_coll, htmlfile, outroot)

### M1CS Design Description Document
dirpath = r'/Users/sroberts/Box Sync/Python/CID/M1CS review/'
CID_coll = ['Collection-10864']
htmlfile = 'ddd_04 - REL06 for Signatures_MC_MS.html'
outroot = 'M1CSDDesc_'

CID.make_cid(dirpath, CID_coll, htmlfile, outroot)

### References for M1CS ACTUATOR AND SENSOR TEST, ANALYSIS, AND MODELING REPORTS
dirpath = r'/Users/sroberts/Box Sync/Python/CID/M1CS review/'
CID_coll = ['Collection-10865']
htmlfile = 'Actuator_and_sensor_reports - REL06 for signatures_MC_MS.html'
outroot = 'M1CSActSen_'

CID.make_cid(dirpath, CID_coll, htmlfile, outroot)

### References for Operational Concept Design Document
dirpath = r'/Users/sroberts/Box Sync/Python/CID/M1CS review/'
CID_coll = ['Collection-10866']
htmlfile = 'M1CS_Ops_Concept_REL04 - Approvals_MC_MS.html'
outroot = 'M1CSAOpCon_'

CID.make_cid(dirpath, CID_coll, htmlfile, outroot)



