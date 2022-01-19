
from datetime import date, datetime

#Las primeras 2 letras del nombre
#Las ultimas 2 letras del apellido materno
#La edad

class GeneratePassword:

  def __init__(self, nm, lnm, bth, t=3):
    self.__name = nm
    self.__lastname = lnm
    self.__age = self._convertdate2age(bth)
    self.__t = t

  def generatePassword(self):
    nm = self.__name
    lnm = self.__lastname
    t = self.__t
    age = self.__age
    if nm and lnm and t and age:
      name = nm.lower()
      lastname = lnm.lower()
      passw = name[:2]+lastname[-2:]
      rpassw = self._rotatePassword(passw,t)
      result = rpassw.upper()+str(age)
      #JOEZ27 > GMBW27
    return result

  def _convertdate2age(self, birthdatestr):
    b = datetime.strptime(birthdatestr, "%d/%m/%Y")
    today = date.today()
    diff = (today.month, today.day) < (b.month, b.day)
    #print(diff)
    res = today.year - b.year - diff
    return res

  def _rotatePassword(self, st, n):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    if st:
      res = []
      for c in st:
        i = abc.index(c)
        res.append(abc[i-(n)])
      rst = ''.join([str(x) for x in res]).upper()
    return rst

'''
age = convertdate2age("11/01/1995")
print(generatePassword("Jose","Lopez",age))

print(rotatePassword('joez'))

a = GeneratePassword("Jose", "Lopez")
print(a)
'''