'''
10. Hospital Appointment Scheduling
A hospital receives appointment requests represented by starting and ending times.
Some appointments overlap with each other. The scheduling system needs to combine
overlapping appointment periods so that the final schedule contains only non-overlapping time ranges.

'''

appoint=[[1,3],[2,6],[8,10],[15,18]]
appoint.sort()
res=[appoint[0]]
for i in range(1,len(appoint)):
    if appoint[i][0]<=res[-1][1]:
        res[-1][1]=max(res[-1][1],appoint[i][1])
    else:
        res.append(appoint[i])
print(res)