import plotter
plotter.parce('noise.txt')
plotter.plot_2d_time('noise','EMF.xlsx','noise')
plotter.get_offset_std('noise','EMF.xlsx')
plotter.parce('real..txt')
plotter.plot_2d_time('real','EMF.xlsx','real')