import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images.append(file_name)
        
#print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width,height)
#print(size)


out = cv2.VideoWriter('project.mp4v',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

while(True):
    ret,frame=vid.read()
    cv2.imshow('camara Web',frame)
    out.write(frame)
    if cv2.waitKey(25)==32:
        break
# Para Atardecer
#for i in range(0,count-1):

# Para Amanecer
for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release() # Liberando el video generado
print("Listo")

