
import cv2
# Function for stereo vision and depth estimation
import triangulation as tri
import calibration
import nanocamera as nano

# Stereo vision setup parameters
B = 6               #Distance between the cameras [cm]
alpha = 50        #Camera field of view in the horisontal plane [degrees]



def findDis(centerRight, centerLeft, frameRight, frameLeft):
    # Function to calculate depth of object. Outputs vector of all depths in case of several balls.
    # All formulas used to find depth is in video presentaion
    depth = tri.find_depth(centerRight, centerLeft, frameRight, frameLeft, B, alpha)
    # cv2.putText(frameRight, "Distance: " + str(round(depth,1)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0),3)
    # cv2.putText(frameLeft, "Distance: " + str(round(depth,1)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0),3)
    # Multiply computer value with 205.8 to get real-life depth in [cm]. The factor was found manually.
    print("  => Depth: ", str(round(depth,1)))
    return round(depth,1)


if __name__ == "__main__":
    pass