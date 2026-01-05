import nplot
import BSDT

def launch():
    for i in BSDT.target:
        name = i.split('/')[-1]
        nplot.data(name)
    
def MakeAll():
    for i in nplot.datalist:
        i.make()

def ProcessAll():
    for i in nplot.datalist:
        i.process()


if __name__ == "__main__":
    launch()
    MakeAll()
    ProcessAll()
    print('시팔 살려주세요') 
