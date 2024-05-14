
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

fig, ax = plt.subplots(figsize=(12, 12))

x_axis = []
y_axis = []

with open("data.txt", "r") as input_data:
    data = [float(i) for i in input_data.read().split("\n")]
with open("settings_for_programm.txt", "r") as input_data:
    settings = [float(i) for i in input_data.read().split("\n")]

y_axis = [i * settings[1] for i in data]

for i in range (0,  len(data)):
    x_axis.append (i / settings[0])

new_x_axis = [x_axis[i] for i in range (0, len(x_axis), 4)]
new_y_axis = [y_axis[i] for i in range (0, len(y_axis), 4)]


ax.plot(new_x_axis, new_y_axis, marker = '*', color = 'blue', label = 'Experemental dots', linewidth = 2.0)



plt.title ('Plot of voltage dendence from time')
plt.xlabel ('time, sec')
plt.ylabel ('U, B')

ax.text (54, 2.0 ,r'$Discharge time = 6.37, sec$')
ax.text (54, 1.8, r'$Charge time = 1.97, sec$')

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(AutoMinorLocator(5))

ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

#ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

ax.grid (which = 'major')
ax.grid (which = 'minor', linestyle=':')

ax.set_xlim([0, 65])
ax.set_ylim([0, 3])

ax.legend ()
plt.savefig('Voltage_plot', format = 'png')
#plt.show()