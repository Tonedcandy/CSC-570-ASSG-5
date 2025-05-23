import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Load the Excel file
file_path = '/Users/monish/Documents/Webgazer/source.xlsx'
df = pd.read_excel(file_path)

# Define point groups and their corresponding columns
points = {
    'Left Hand': ['leftHand.x', 'leftHand.y', 'leftHand.z'],
    'Right Hand': ['rightHand.x', 'rightHand.y', 'rightHand.z'],
    'Left Eye': ['leftEye.x', 'leftEye.y', 'leftEye.z'],
    'Right Eye': ['rightEye.x', 'rightEye.y', 'rightEye.z'],
    'Cube': ['cube.x', 'cube.y', 'cube.z']
}

# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)

# Compute global axis limits
all_x = pd.concat([df[col[0]] for col in points.values()])
all_y = pd.concat([df[col[1]] for col in points.values()])
all_z = pd.concat([df[col[2]] for col in points.values()])
ax.set_xlim(all_x.min(), all_x.max())
ax.set_ylim(all_y.min(), all_y.max())
ax.set_zlim(all_z.min(), all_z.max())
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("3D Point Animation with Slider")

# Initialize scatter plots
scatters = {}
colors = ['red', 'blue', 'green', 'orange', 'purple']
for i, (label, cols) in enumerate(points.items()):
    scatters[label] = ax.scatter([], [], [], color=colors[i], label=label)
ax.legend()

# Create slider
ax_slider = plt.axes([0.2, 0.1, 0.65, 0.03])
frame_slider = Slider(ax_slider, 'Frame', 0, len(df) - 1, valinit=0, valstep=1)

# Update function
def update(frame):
    for label, cols in points.items():
        x, y, z = df[cols[0]].iloc[frame], df[cols[1]].iloc[frame], df[cols[2]].iloc[frame]
        scatters[label]._offsets3d = ([x], [y], [z])
    fig.canvas.draw_idle()

# Link slider to update function
frame_slider.on_changed(update)
update(0)
plt.show()