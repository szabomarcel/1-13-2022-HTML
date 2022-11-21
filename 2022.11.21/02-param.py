def hányados(osztandó, osztó):
    osztandó = 66
    osztó = 55

    print("A fv-ben:", osztandó, ",", osztó)
    res = osztandó / osztó
    return res 

osztandó = 100
osztó = 10

print("A fv-elött:", osztandó, ",", osztó)
eredm = hányados(osztandó,osztó)
print("A fv-után:", osztandó, ",", osztó)

print(eredm)