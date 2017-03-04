# Jonathan Halverson
# Sunday, February 26, 2017
# This script extracts facebook ids from json

with open('posts_ManchesterByTheSeaMovie.jsonl', 'r') as f:
  txt = f.readlines()
txt = ''.join(txt).replace('_', '9')

import re
numbers = re.sub("\D", " ", txt)
numbers = numbers.split()

from collections import Counter
c = Counter(map(len, numbers))
print sorted(c.items())

fbids = [number for number in numbers if len(number) > 11 and len(number) < 18]
print len(fbids), len(set(fbids))

with open('fbids_MbtS.txt', 'w') as f:
  for fbid in set(fbids):
    f.write(str(fbid) + '\n')

#12-17
"""
12345678901234567890
467107603470866
10203738716251473
1401583446804067
1454274154842107
1055170377830951
10152125494822659
10152243507851884
1599477866976872
746265652119758
10104656977985669
952553364758225
1811096509213322
740358822721704
10204167022993707
415603461920990
10201840990448671
759392517470890
377927852592706
673759866075186
10152592197199367
4436004393792
164925227175686
10201910908600302
10205193506183424
1142731515751476
10202849780598874
898383376874332
613772698744290
467107603470866
10203738716251473
122375558256646
10203542998196124
10202744403064470
10152170533099823
10201735021249398
337767189715191
637589509657789
10203121306098401
10203770809696423
308586752645997
10203965610924976
10203302418579758
770289572981967
10203104800196603
10205568676966322
748479078612939
10203043271475358
10152443862421759
10201787312549455
10202944810801397
10153490763832388
10202849780598874
10152578424394860
613772698744290
10152460008349159
467107603470866
10203738716251473
10152838793207999
721440437916577
122375558256646
10202744403064470
538102969643025
971041972918383
10201735021249398
637589509657789
10201976213902912
10202627013505102
10203121306098401
1006866809340358
10206633444858378
1539003202993060
10153284318869576
885795548109030
10203302418579758
10152952825896667
"""
