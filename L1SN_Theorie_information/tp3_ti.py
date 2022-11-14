def add_mod2(o,k):
    return (o+k)%2

def deg(poly):
    if poly==[]:
        return []
    i = -1
    long = len(poly)
    while poly[i]!=1 and i>=-long:
        i-=1
    return long+i

def coeff(poly):
    if 1 in poly:
        return 1
    else:
        return 0

def is_null_poly(poly):
    return coeff(poly)==0

def add_poly(poly1,poly2):
    poly = []
    s,o = 0,0
    long1 = len(poly1)
    long2 = len(poly2)
    while s!=long1 and o!=long2:
        poly.append(add_mod2(poly1[s],poly2[o]))
        s+=1
        o+=1
    if s==long1:
        poly += poly2[o:]
    else:
        poly += poly1[s:]
    return poly

def add_poly_recurs(poly):
    if len(poly)==2:
        return add_poly(poly[0],poly[1])
    elif len(poly)==1:
        return poly
    else:
        poly[1]=add_poly(poly[0],poly[1])
        return add_poly_recurs(poly[1:])

def diff_poly(poly1,poly2):
    return add_poly(poly1,poly2)

def mult_poly(poly1,poly2):
    if is_null_poly(poly1) or deg(poly1)==0:
        return poly2
    elif is_null_poly(poly2) or deg(poly2)==0:
        return poly1
    i = 0
    long1 = len(poly1)
    new_poly = [[]]*long1
    for i in range(long1):
        if poly1[i]==1:
            new_poly[i]= [0]*i + poly2
    new_poly = add_poly_recurs(new_poly)
    return new_poly

def eucl_poly(poly1,poly2):
    Q = []
    R = poly1
    d = deg(poly2)
    c = coeff(poly2)
    while not is_null_poly(R) and deg(R) >= d:
        S = [0] * (deg(R)-d)
        S.append((coeff(R)//c))
        Q = add_poly(Q,S)
        R = add_poly(R,mult_poly(S,poly2))
    return Q,R

def div_poly(poly1,poly2):
    return eucl_poly(poly1,poly2)[0]

def mod_poly(poly1,poly2):
    return eucl_poly(poly1,poly2)[1]

def pad(poly,nombre):
  long=len(poly)
  if long>nombre:
    for i in range (nombre,long):
      del poly[0]
  else:
    for i in range (long,nombre):
        poly.append(0)
  return poly

def monome(n):
  tab = []
  for i in range (0,n):
    tab.append(0)
  tab.append(1)
  return tab

def cod(mess,poly,taille):
  c=mult_poly(mess,(monome(deg(poly))))
  o=mod_poly(c,poly)
  d=add_poly(c,o)
  e=pad(d,taille)
  return e

def decod(mess,poly,taille):
  b = True
  i = mod_poly(mess,poly)
  if (not is_null_poly(i)):
    b = False
    m = mess
  else:
    m = div_poly(mess,monome(deg(poly)))
  pad(m,taille)
  return m,b