# Commented out IPython magic to ensure Python compatibility.
# %pip install matplotlib

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import os
#import cv2
import math
#from google.colab.patches import cv2_imshow
from time import sleep

df = pd.read_csv("Demand_History.csv")

years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']

f = []
for i, _ in enumerate(years):
  f.append(plt.figure(f"Demand in year {years[i]}"))
  plt.figure(figsize=(12,12))
  colors = cm.rainbow(df[years[i]])
  plt.scatter(df.x_coordinate, df.y_coordinate, color=colors, linewidth=7.5)
  plt.axis([0, 65, 0, 65])
  #plt.savefig(f"Demand in year {years[i]}")
  sleep(2)

"""The code below created the demand video. Basically the saved plots are being added to the video"""

"""image_folder = "."
video_name = "Demand Evolution.mp4"

images = [img for img in os.listdir(image_folder)
            if img.endswith(".jpg") or
                img.endswith(".jpeg") or
                img.endswith("png")]

frame = cv2.imread(os.path.join(image_folder, images[0]))

height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0x7634706d, 1, (width, height)) 

# Appending the images to the video one by one
for image in images: 
  frame = cv2.imread(os.path.join(image_folder, image))
  #cv2_imshow(frame)
  video.write(frame) 
  
video.release()  # releasing the video generated"""

coordinates = (df.x_coordinate[0], df.y_coordinate[0])
plt.figure(figsize=(17,17))
colors = cm.rainbow(df['2011'])
plt.scatter(df.x_coordinate, df.y_coordinate, color=colors, linewidth=7.5)
plt.axis([0, 65, 0, 65])
plt.show()

x_coord = 63.5
y_coord = 0.5
demand_point_index = (math.floor(y_coord) * 64) + math.floor(x_coord) 

demand = [df[y][demand_point_index]  for y in years]
print(demand)

plt.stem(years, demand)

demand_point_index = range(64*64)

y = '2010'
demand = df[y]
print(demand)

plt.plot(demand_point_index, demand)
#hi this is sanaka
