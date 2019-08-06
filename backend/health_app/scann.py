from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils
from imutils import contours

def extract(image):
    '''
    A function to detect marked points
    '''
    #! reading the image for it to be consumed by the function
    imag = cv2.imread(image)
    ratio = imag.shape[0] / 500.0
    orig = imag.copy()
    imag = imutils.resize(imag, height=500)

    #! converting the image into grayscale,blur it, find the edges in the image
    gray = cv2.cvtColor(imag, cv2.COLOR_BGR2GRAY)
    gray = cv2.gaussianBlur(gray, (5,5), 0)
    edged = cv2.Canny(gray, 75, 200 )

    #! find the contours inthe edged image, keeping the largest ones and initialising the screen contour
    cnts = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

    #! loop over contours
    for c in cnts:
        peri = arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        #* if our approximated contour has four points we can assume we have found our screen
        if len(approx) == 4 :
            screenCnt = approx
            break

    #! Apply the four point transform to obtain a top down view of the original image
    paper = four_point_transform(imag, screenCnt.reshape(4,2))
    warped = four_point_transform(orig, screenCnt.reshape(4,2) * ratio) 

    warped = imutils.resize(warped, height=650)

    #! identify circles
    warped = cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY)
    warped = cv2.GaussianBlur(warped, (5, 5), 0)

    #! Read image
    #! setup simpleblob detector

    params = cv2.SimpleBlobDetector_params()

    #! Change thresholds
    #! params.minThreshold = 10
    #! params.maxThreshold = 200

    params.filterByArea = True
    params.minArea = 100

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.8 

    detector = cv2.SimpleBlobDetector_create(params)

    #! Detect blobs.
    keypoints = detector.detect(warped)

    im_with_keypoints = cv2.drawKeypoints(warped, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    pts= cv2.KeyPoint_convert(keypoints)

    #* an array to hold all the values 
    values = []
    
    dict = { '62.25076' : 'male', '225.93164' : 'first_visit'}
    for k,v in dict.items():
        for i in range(len(pts)):
            for j in range(len(pts[0])):
                ind = 0
                if int(float(pts[i][j])) == int(float(k)):
                    str = str(pts[i][j])
                    values.append(dict.get(st))
                    ind += 1
                else:
                    ind += 1
    print(values)
    return values

#* @login_required(login_url='/accounts/login/')
#* def scann(request):
#*     if request.method == 'POST':
#*         Scanform = ScannForm(request.POST,request.FILES)
#*         if form.is_valid():
#*             im = Scanform.cleaned_data['image']
#*             answers = extract(im)