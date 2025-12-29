import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def parce(filename,save = 'EMF'):
    delay = 1
    global results
    timelines = []
    voltage_list = []
    dat = os.path.join('storage',filename)
    linenum = 0
    with open(dat, "r", encoding='utf-8')as f:
        for line in f:
            linenum+=delay
            timeline = linenum
            raw = line.strip()
            voltage_list.append(raw)
            timelines.append(timeline)
    df = pd.DataFrame({
        "Time": timelines,
        "voltage":voltage_list
    })
    name = filename.split('.')[0]
    if os.path.isdir(os.path.join('storage',name)): pass
    else: os.makedirs(os.path.join('storage',name))
    df.to_excel(os.path.join('storage',name,f"{save}.xlsx"), index=False)

def get_offset_std(foldername,filename,save='noise'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    voltage = df.voltage
    voltage_arr = voltage.to_numpy()
    print(np.mean(voltage_arr))
    print(np.std(voltage_arr))
    


def plot_2d_time(foldername,filename,save='EMF'):
    df = pd.read_excel(os.path.join('storage',foldername,filename), engine='openpyxl', header=0)
    timelines = df.Time
    voltage = df.voltage
    plt.plot(timelines, voltage, label = "Electromotive Force", color = (0.0, 0.0, 1.0, 1.0), linestyle="-", marker="")

    plt.title(f"Induced Electromotive Force")
    plt.xticks([])
    plt.grid(axis='x', visible=False)
    plt.xlabel("Time                 [   ms  ]")
    plt.ylabel("Electromotive Force  [   V   ]")
    plt.grid(True)
    plt.legend(
        loc       = "lower right",
        frameon   =  True,
        edgecolor = "black",
        facecolor = "white",
        )

    plt.savefig(f"{save}_Graph.jpg", dpi=3000, bbox_inches='tight')
    plt.close()
