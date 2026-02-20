## Farmaan
import numpy as np
import matplotlib.pyplot as plt
import imageio as iio
import csv, os

def video(filename: str):
    """
    Take CSV data and generate plots at time t (frames),
    and compile them into a video
    """
    # Get directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine directory with filename
    Video_path = os.path.join(script_dir, "twobody.mp4")

    if os.path.exists(Video_path):
        os.remove(Video_path)
        print(f"File '{Video_path}' deleted successfully.")
    else:
        print(f"File '{Video_path}' does not exist.")
    
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')
    ax.axis('off')
    ax.set_xlim(-6,6)
    ax.set_ylim(-6,6)
    ax.set_title("Two Body Simulation", color="white")

    mass_1 = ax.scatter([], [], color="blue", s=300)
    mass_2 = ax.scatter([], [], color="red", s=300)

    with iio.get_writer(Video_path, fps=60, codec="libx264") as writer:
        with open(filename, 'r') as myfile:
            myfile = csv.DictReader(myfile)
            for row in myfile:

                x1, y1 = float(row['x1']), float(row['y1'])
                x2, y2 = float(row['x2']), float(row['y2'])

                mass_1.set_offsets([[x1, y1]])
                mass_2.set_offsets([[x2, y2]])

                # Convert the Matplotlib figure to a NumPy image array
                fig.canvas.draw()
                frame = np.asarray(fig.canvas.buffer_rgba())
                writer.append_data(frame)

    plt.close(fig)  # close the figure to save memory