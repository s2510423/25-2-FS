def plot_2d(name,offset,height):
    delay = 10
    global results
    timelines = []
    voltage_list = []
    constant_list = []
    dat = os.path.join(name)
    linenum = 0
    with open(dat, "r")as f:
        for line in f:
            linenum+=delay
            timeline = linenum
            raw = line.strip()
            voltage_list.append(raw)
            timelines.append(timeline)
    voltage_arr = np.array(voltage_list)
    timelines_arr = np.array(timelines)
    df = pd.DataFrame({
        "Time": timelines_arr,
        "voltage":voltage_arr
    })

    df.to_excel(f"EMF {height}cm.xlsx", index=False)

    plt.plot(timelines_arr, voltage_arr, label = "Electromotive Force", color = (0.0, 0.0, 1.0, 1.0), linestyle="-", marker="")

    plt.title(f"Induced Electromotive Force [height: {height}cm]")
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

    plt.savefig(f"EMF in {height}cm.jpg", dpi=300, bbox_inches='tight')
    timelines.clear()
    lift_list.clear()
    drag_list.clear()
    plt.close()
