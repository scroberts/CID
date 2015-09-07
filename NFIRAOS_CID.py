#!/usr/bin/env python3

import CID

######## CID Specific Information ##############

### NFIRAOS CID Information
dirpath = r'/Users/sroberts/Box Sync/Python/CID/CID NFIRAOS/'
CID_coll = ['Collection-10610']
htmlfile = 'NFIRAOS_CID.htm'
outroot = 'NFIRAOS_'

### STR CID Information
# dirpath = r'/Users/sroberts/Box Sync/Python/CID/CID STR/'
# CID_coll = ['Collection-10610']
# htmlfile = 'STR_CID.htm'
# outroot = 'STR_'

######## End of Specific CID Information

CID.make_cid(dirpath, CID_coll, htmlfile, outroot)



