## Farmaan
import numpy as np
import matplotlib.pyplot as plt
import imageio.v3 as iio
import csv, os

def video(filename: str):
    """
    Take CSV data and generate plots at time t (frames),
    and compile them into a video
    """
    file_path = "Two body sim.mp4"

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' does not exist.")

    frames = []
    with open(filename, 'r') as myfile:
        myfile = csv.DictReader(myfile)
        for row in myfile:
            
            x1, y1 = float(row['x1']), float(row['y1'])
            x2, y2 = float(row['x2']), float(row['y2'])
            
            # Create the figure
            fig, ax = plt.subplots(figsize=(20, 20), dpi=100)
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
            ax.axis('off')
            ax.scatter(x1, y1, color='blue', s=1000, label='Mass 1')
            ax.scatter(x2, y2, color='red', s=1000, label='Mass 2')
            ax.set_xlim(-6,6)
            ax.set_ylim(-6,6)
            ax.set_title("Two Body Simulation")
        
            # Convert the Matplotlib figure to a NumPy image array
            fig.canvas.draw()
            frame = np.array(fig.canvas.renderer.buffer_rgba())

            # Append to the list of frames
            frames.append(frame)

            plt.close(fig)  # close the figure to save memory

        # Write the video (using FFmpeg backend)
    iio.imwrite("Two body sim.mp4", frames, fps=60)