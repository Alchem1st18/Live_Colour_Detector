In this mini project, i've used Opencv and Pillow to do live video feed colour detection.
There are 2 observations made,
1. By just using pillow and the getbbox function, we get only one large dimension box from our frame and this includes all the images of a particular color we have specified.
2. In order to modify it and ensure that if the objects of same color are some distance apart, we dont get one box but instead separate boxes for the objects, we use CONTOURS.
   The same concept in [1] has been used but once the mask is obtained, we make contours for the mask, and then make rectangles for the contours detected.
   This ensures we get separate boxes for every object detected.
