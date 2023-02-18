import csv
import cv2 as cv
import os

# If we do not specify any path
# os.listdir() method will return
# the list of all files and directories
# in current working directory

dir_list = os.listdir('C:\Polygence photos 2')


with open('trophyImages.csv', 'a') as new_file:
        # create the csv writer
        csv_writer = csv.writer(new_file)

        for imageName in dir_list:
                print(imageName)
                image = cv.imread("C:\Polygence photos 2\\"+ imageName)

                #using selectROI() function to draw the bounding box around the required objects
                imagedraw = cv.selectROI(image)
                #cropping the area of the image within the bounding box using imCrop() function
                croppedimage = image[int(imagedraw[1]):int(imagedraw[1]+imagedraw[3]), int(imagedraw[0]):int(imagedraw[0]+imagedraw[2])]
                x=imagedraw[0]
                y=imagedraw[1]
                h= imagedraw[3]
                w=imagedraw[2]
                csv_writer.writerow([imageName, x, y, w, h])
                break



cv.waitKey(0)
cv.destroyAllWindows()






