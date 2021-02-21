#!/usr/bin/env python3

import hgtk

자음 = 'ㅇ ㄱ ㄴ ㄷ ㄹ ㅁ ㅍ ㅅ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ ㄲ ㄸ ㅃ ㅆ ㅉ'.split()
모음 = 'ㅏ ㅑ ㅓ ㅕ ㅗ ㅛ ㅜ ㅠ ㅡ ㅣ ㅐ ㅔ ㅟ ㅘ ㅢ ㅚ ㅙ ㅝ ㅞ ㅒ ㅖ'.split()
받침 = 'ㅇ ㄱ ㄴ ㄷ ㄹ ㅁ ㅂ ㅅ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ ㄲ ㅆ ㄳ ㄵ ㄶ ㄺ ㄻ ㄼ ㄽ ㄾ ㄾ ㅀ ㅄ'.split()

#print(hgtk.letter.decompose('감')) #분해
#print(hgtk.letter.compose('ㄱ', 'ㅏ', 'ㅁ'))#조합
#print(hgtk.text.decompose('강은혜는 강비! hello world 1234567890 ㅋㅋ!'))
#print(hgtk.text.compose('ㅎㅏㄱᴥㄱㅛᴥㅈㅗ.....hello world 1234567890 ㅋㅋ!'))

for i in 자음:
    line = []
    for j in 모음:
        line.append(hgtk.letter.compose(i, j))
    print(' '.join(line))
for i in 자음:
    for j in 모음:
        line = []
        for k in 받침:
            line.append(hgtk.letter.compose(i, j, k))
        print(' '.join(line))
