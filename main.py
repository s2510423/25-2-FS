import nplot
import BSDT

def launch():
    for i in BSDT.dirscanner.target:
        name = i.split('/')[-1]
        nplot.data(name[:-4])
    
def MakeAll():
    for i in nplot.datalst:
        i.make()

def ProcessAll():
    for i in nplot.datalst:
        i.process()


if __name__ == "__main__":
    launch()
    MakeAll()
    ProcessAll()
    print('** 살려주세요') 
