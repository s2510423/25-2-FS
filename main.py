import plotter
plotter.parce('noise.txt')
plotter.unoffset('noise','EMF.xlsx')
plotter.plot_2d_time('noise','unoffset.xlsx','noise')

plotter.parce('real..txt')
plotter.unoffset('real','EMF.xlsx')
plotter.plot_2d_time('real','unoffset.xlsx','real')
