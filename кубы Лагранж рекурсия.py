from math import floor, sqrt
n = int(input())


def tlan(n, kol, st, sst):
    kol += 1
    bo = 1
    if kol > 7:
        return 0
    ch1 = floor(n ** (1 / 3))

    if st == '':
        ch1 += sst
        if ch1 == 0:
            print('0')
            return 3
    else:
        nubla = st.rfind(' ', 0, -1)
        if nubla < 0:
            nubla = 0
        ol_st = st[nubla: -1:]
        old_nu = int(ol_st) ** (1 / 3)
        if ch1 > old_nu:
            ch1 = int(old_nu)

    st += str(ch1 ** 3)
    if ch1 ** 3 == n:
        print(st)
        return 2
    else:
        st += ' '
        bo = tlan(n - ch1 ** 3, kol, st, sst)
        if bo == 0:
            if kol != 1:
                return 0
            else:
                st = ''
                sst -= 1
                tlan(n, 0, st, sst)
tlan(n, 0, '', 0)
