import time

if(__name__ == "__main__"):
    print('Selamat datang di 24-Solver')
    inp = [int(i) for i in input('Masukan 4 angka (dipisah spasi) : ').split(' ')]
    start = time.time()
    permutasiAngka = [[inp[a], inp[b], inp[c], inp[d]] for a in range(
        4) for b in range(4) for c in range(4) for d in range(4) 
        if a!=b!=c!=d!=a!=c!=b!=d]
    #Hapus duplikat dengan mengubahnya menjadi set/himpunan lalu menjadi list lagi
    permutasiAngka = set(tuple(tup) for tup in permutasiAngka)
    permutasiAngka = [list(li) for li in permutasiAngka]
    #Generate kemungkinan operator
    op = ['+','-','*','/']
    permutasiOperator = [[op[a],op[b],op[c]] for a in range(4) for b in range(4) 
        for c in range(4)]
    #Generate kemungkinan ekspresi beserta kurungnya
    cnt = 0
    epsilon = abs(24-(8/(3-(8/3))))
    for pA in permutasiAngka:
        a,b,c,d = pA
        for pO in permutasiOperator:
            op1,op2,op3 = pO
            tupleFormatString = (a,op1,b,op2,c,op3,d)
            #Kemungkinan kurung
            '''
            ((a b) c) d
            (a b) (c d)
            (a (b c)) d
            a ((b c) d)
            a (b (c d))
            '''
            ekspresi = []
            ekspresi.append("((%d%c%d)%c%d)%c%d" % tupleFormatString)
            ekspresi.append("(%d%c%d)%c(%d%c%d)" % tupleFormatString)
            ekspresi.append("(%d%c(%d%c%d))%c%d" % tupleFormatString)
            ekspresi.append("%d%c((%d%c%d)%c%d)" % tupleFormatString)
            ekspresi.append("%d%c(%d%c(%d%c%d))" % tupleFormatString)
            for e in ekspresi:
                try:
                    hasil = eval(e)
                    if(abs(hasil-24)<=epsilon):
                        print(e+" = 24")
                        cnt += 1
                except ZeroDivisionError:
                    pass
    print('Banyak Solusi : %d' % cnt)
    end = time.time()
    print('Program dijalankan selama %.5f detik' % (end-start))
    
