# FBFBBFF RLR gives row 44 - F = 0, B = 1
# 0101100 = 44

#RLR gives col 5 - R = 1, L = 0

# Every seat also has a unique seat ID: multiply the row by 8, then add the column.

from data import data


maxSid = 0
sids = []
seats = [] # ordered pair row, column
for item in data:
    idx = 0
    val = 0
    rowVal = 0
    colVal = 0
    sid = 0
    # print("item: %s" % item)
    # item = "FBBBFBBLRR"
    for bit in item:
        # for bits 0 - 6 - exponent = 6 - idx

        # print("bit: %s" % bit)
        # print("idx: %d" % idx)
        if idx in range(0,7):
            exp = 6 - idx
        # for bits 7,8,9 exponent = 9 - idx
        elif idx in range(7,10):
            exp = 9 - idx
        
        # print("exp: %d" % exp)
        
        if bit is 'B' or bit is 'R':
            # print("power: %d" % pow(2,exp))
            val += pow(2,exp)

        if idx == 6:
            rowVal = val
            # print("row val: %d" % rowVal)
            val = 0

        if idx == 9:
            colVal = val
            # print("col val: %d" % colVal)
            sid = rowVal * 8 + colVal
            sids.append(sid)
            seats.append([rowVal,colVal])
            # print("sid: %d" % sid)
            
            if sid > maxSid:
                maxSid = sid
                # print("maxSid: %d" % maxSid)
        
        idx += 1

# print(maxSid)
# print(sids)

seatMap = [[0 for col in range(8)] for row in range(128)]

# print(seatMap)

for sid in sids:
    # for a given sid  - if sid -1 doesnt exist 
    # check if sid - 2 exists
    # if it does missing sid is sid - 1
    if sid - 1 not in sids:
        if sid - 2 in sids:
            print("my sid is: %d" % (sid - 1))


    col = sid % 8
    row = (sid - col)/8
   
   

# print(seatMap)