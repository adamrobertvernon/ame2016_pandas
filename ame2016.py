import pandas as pd
from fortranformat import FortranRecordReader
fline=FortranRecordReader('(a1,i3,i5,i5,i5,1x,a3,a4,1x,f13.5,f11.5,f11.3,f9.3,1x,a2,f11.3,f9.3,1x,i3,1x,f12.5,f11.5)')
from collections import namedtuple

filename="mass16.txt"
# filename="mass.mas12"

df_cols=["NZ", "N", "Z", "A", "el","o", "massexcess", "uncmassex", "binding", "uncbind","B", "beta", "uncbeta", "am_int", "am_float", "uncatmass"]

record=namedtuple('nucleo','cc NZ  N  Z  A    el  o     massexcess  uncmassex binding uncbind     B  beta  uncbeta    am_int am_float   uncatmass')

df = pd.DataFrame(columns=df_cols)

f=open(filename,'r')
print("converting...")
for line_i, line in enumerate(f):
    nucl=record._make(fline.read(line))
    df2 = pd.DataFrame([[nucl.NZ, nucl.N, nucl.Z, nucl.A, nucl.el, nucl.o, nucl.massexcess, nucl.uncmassex, nucl.binding,
    nucl.uncbind, nucl.B, nucl.beta, nucl.uncbeta, nucl.am_int ,nucl.am_float, nucl.uncatmass]], columns=df_cols)
    df= df.append(df2, ignore_index=True)


print(df)
df.to_csv("ame2016.csv")
