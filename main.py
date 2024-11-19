import numpy as np
from projection import Projection
from rotation import rotate_vertices
import matplotlib.pyplot as plt

# Parameters
n, f, D, d = 40, 100, 80, 60
vertices = np.array([
    [0, 0, 50],  # Bottom face
    [1, 0, 50],
    [1, 1, 50],
    [0, 1, 50],
    [0, 0, 51],  # Top face
    [1, 0, 51],
    [1, 1, 51],
    [0, 1, 51],
])

faces = [
    [vertices[i] for i in [0, 1, 2, 3]],  # Bottom face
    [vertices[i] for i in [4, 5, 6, 7]],  # Top face
    [vertices[i] for i in [0, 1, 5, 4]],  # Side face
    [vertices[i] for i in [1, 2, 6, 5]],  # Side face
    [vertices[i] for i in [2, 3, 7, 6]],  # Side face
    [vertices[i] for i in [3, 0, 4, 7]],  # Side face
]

# Rotating the vertices
rot_v = rotate_vertices(vertices, angle_x=0, angle_y=0, angle_z=np.pi/4)
print("rot_v", "_"*10,rot_v)

# Projection
p1 = Projection(near=n, far=f, D=D, d=d)
rot_v_proj = np.array([p1.GL_projection(v) for v in rot_v])
print("rot_v_pr", "_"*10,rot_v_proj)

#faces that are projected
faces_pr = [
    [rot_v_proj[i] for i in [0, 1, 2, 3]],  # Bottom face
    [rot_v_proj[i] for i in [4, 5, 6, 7]],  # Top face
    [rot_v_proj[i] for i in [0, 1, 5, 4]],  # Side face
    [rot_v_proj[i] for i in [1, 2, 6, 5]],  # Side face
    [rot_v_proj[i] for i in [2, 3, 7, 6]],  # Side face
    [rot_v_proj[i] for i in [3, 0, 4, 7]],  # Side face
]

def plot_face(points):
    
    polygon = np.vstack([points, points[0]])

    plt.fill(polygon[:, 0], polygon[:, 1], color='skyblue', alpha=0.5)  

    
    plt.plot(polygon[:, 0], polygon[:, 1], 'b-', marker='o')  
fig, ax = plt.subplots()
ax.set_aspect('equal')

for face in faces:
    for v in faces_pr:
        plot_face(v)

plt.show()