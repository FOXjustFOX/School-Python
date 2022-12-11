#working, 100% on szkopuł

import decimal

n = int(input())

suma = 0

for i in range(n):
    x = input().replace(",", ".")
    decimal.getcontext().prec = 200

    suma = decimal.Decimal(suma) + decimal.Decimal(x)

if suma - int(suma) == 0:
    print(str(int(suma)).replace(".", ","))
elif 'E' in [x for x in str(suma)]:
    g = str(suma)
    g = g[-2:]
    print(f'{suma:.{g}f}'.replace(".", ","))
elif suma * 10 == 9:
    print(str(f'{suma:.1f}').replace(".", ","))

else:
    print(str(suma).replace(".", ","))
