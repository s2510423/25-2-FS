import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np
import openpyxl
from BSDT import dirscanner as dirsc

# core functions
def slicer(df, num = 4):
    voltage = df['voltage'].to_numpy()[::num]
    time = df['Time'].to_numpy()[::num]
    return pd.DataFrame({'Time':time,'voltage':voltage})

def ma(df, num = 4):
    voltage = df['voltage'].rolling(window = num).mean()
    time = df['Time']
    return pd.DataFrame({'Time':time,'voltage':voltage})

def zoom(df, milisec = 4):
    maxVal = df['voltage'].idxmax()
    voltage = df['voltage'].iloc[max(0,maxVal-1000*milisec):min(len(df['voltage']), maxVal+1000*milisec)]
    time = df['Time'].iloc[max(0,maxVal-1000*milisec):min(len(df['Time']), maxVal+1000*milisec)]
    return pd.DataFrame({'Time':time,'voltage':voltage})
def unoffset(df, offset = 505.55085039916696):
    voltage = df['voltage'] - offset
    return pd.DataFrame({'Time':df['Time'],'voltage':voltage})
funcs = {
    'ma'        :   ma,
    'zoom'      :   zoom,
    'slice'     :   slicer,
    'unoffset'  :   unoffset
}

# legacy function(REFACTORED)

def get_offset_std(foldername = 'noise',filename = 'EMF.xlsx'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    voltage = df.voltage
    print(f'offset : {df['voltage'].mean()}')
    print(f'std    : {df['voltage'].std()}')

# plot

def plot(df, path):
    plt.plot(df['Time'], df['voltage'], label = "Electromotive Force", color = (0.0, 0.0, 1.0, 1.0), linestyle="-", marker="")

    plt.title(f"Voltage by Induced Electromotive Force")
    plt.xticks([])
    plt.grid(axis='x', visible=False)
    plt.xlabel("Time     [   ms  ]")
    plt.ylabel("Voltage  [   V   ]")
    plt.grid(True)
    plt.legend(
        loc       = "lower right",
        frameon   =  True,
        edgecolor = "black",
        facecolor = "white",
        )

    plt.savefig(os.path.join(path,"Graph.jpg"), dpi=1000, bbox_inches='tight')
    plt.close()


# parce all data

def st(filename):return os.path.join('storage','__Rawdata__',f'{filename}.txt')

dirsc.bsdtfile('EMF')

datalst = []

class data: 
    def __init__(self,name):
        self.path = st(name)
        self.name = name
        self.folder = os.path.join('storage',self.name)
        datalst.append(self)

    def make(self):
        os.makedirs(os.path.join('storage',self.name))
        with open(self.path,'r') as f:
            time = 0
            timelines = []
            voltage = []
            lines = f.readlines()
            for line in lines:
                time += 1
                timelines.append(time)
                voltage.append(float(line.strip()) * 1023 / 5)
        df = pd.DataFrame({
            'Time':timelines,
            'voltage':voltage
        })
        df.to_excel(os.path.join(self.folder,'EMF.xlsx'), index=False)
    def getTask(self):
        with open (os.path.join(self.folder,'control.bsdt'), 'r') as f:
            self.tasklist = []
            lines = f.readlines()
            for line in lines:
                if line.strip() in funcs: self.tasklist.append(funcs[line.strip()])
                else: continue
    def process(self):
        self.getTask()
        df = pd.read_excel(os.path.join(self.folder, 'EMF.xlsx'), header = 0, engine = 'openpyxl') 
        for function in self.tasklist:
            df = function(df)
        df.to_excel(os.path.join(self.folder, 'result.xlsx'), index = False)
        plot(df, self.folder)


def launch:
    for i in BSDT.target:
        name = i.split('/')[-1]
        i = nplot.data(name)