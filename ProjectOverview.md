For a project overview, current as of 9/20/2008, see [ProjectOverview(pdf)](http://code.google.com/p/imageanalysis/source/browse/trunk/projectOverview.pdf).


  * Database and server information
    * SensorBase:
    * Server
  * Files you need:
    * snake (folder) --- incomplete
    * medFilter
    * findXY (file)
    * gvfmain (file)
    * checkGrad
    * calibrate
    * orient
    * findRegionDimensions (file)
    * findMode (file)
    * checkRes (file)
    * brightness-intensityGradients-checkGrad-calibrate.py (file) --- incomplete
    * getPollution (file)
    * matchBright (file) --- incomplete
    * Any SMS files
    * Any slogging code
    * Code that uploads results
    * imageGrayscale

## Implementation ##
  * Architectural overview, and notes on the status of individual components
    * Photo taken on phone and sent to SensorBase
      * Automatically uploaded to SensorBase if there is internet access
      * If there is no internet access: We have adapted Saro’s SMS code so that results can be sent via SMS, however, we still need a program on the phone that will call SMS only when internet isn’t found
    * The server queries SensorBase for new images every 3 hours
      * The three hour period is adjustable
      * The server accepts no more than 15 images during each query period—see “Methods and Design”, delta
    * Images are checked for quality
      * Checks to make sure the image meets the minimum resolution, see “methods and design” and “evaluation” for current value
      * Images converted to grayscale
      * Median filter applied
      * The image is segmented
        * We have not been able to successfully segment our test images. One problem is not iterating the GVF and snake deformation enough. Resolution may also have an effect, but we didn’t officially test this. We’re also unsure of how to parse the output from the segmentation to find which points in the output correspond to which objects within the image (see comments in “snakeinterp1.py”). We were looking into using a segmentation method that is similar to the one we are currently trying to use but consistently works with multiple images with precedent est., we think , on how to parse the output. This new method is detailed at: http://www.i3s.unice.fr/~debreuve/acontour.htm
        * You might want to just use the matlab code. Unfortunately, Matlab code takes a ridiculous amount of memory to run the segmentation code (we frequently got the error “System out of memory”). There was a project a few years ago with dietsense that integrated matlab and python. This might be useful for writing the segmentation code and also have the added bonus of being easily integrated with our python code. E-mail Nicolai Munk Petersen at nmp@webcore.eu for more info. He worked on the python-matlab integration project
        * **NOTE**:  Once we have the output from the segmentation figured out, we should be able to fill in the gaps in the matchBright program we have right now
      * Light intensity gradient check
        * Bad images:
        * If zero across the entire image, the image is bad, because it’s either totally wash-out, totally yellowed, or totally dark
        * If not zero within a 50 pixel radius of the filter and color chart (see “Methods and Design”, pre-processing)
        * Bad images are not analyzed—we want have a program that sends a notice of the bad image and unsuccessful analysis to sensorbase and back to the phone; ideally, this program will also tell about the type of error, so that Surya and the people taking the pictures will know what is being done wrong, but we haven’t added this feature yet.
        * Good images:
        * If zero with a 50 pixel radius of the filter and the color chart
        * Good images are calibrated (see “Methods and Design”, pre-processing)
    * The images are matched to the color chart
      * The color chart is oriented in the frame(see “methods and design”)
      * We have a program to do this right now but it assumes that the color chart is to the left of the filter. We would like a more flexible program that doesn’t assume this. I would like to work on this part if you like (oh, and I’m also cool with helping with any segmentation stuff….like I told Nithya, I can commit a max of 4 hours a week to work on CENS stuff until I see how busy everything else will be, but I will have some time to help you if you want/need, and am still very interested in continuing work on the project)
      * The filter is matched to a bar on the  color chart
      * Results are uploaded on SensorBase and sent to the phone with less detail via SMS. More tests are needed to determine how well SMS works
    * Order to run the files in—already called in order on server:
      * Slogging code
      * checkRes
      * imageGrayscale
      * medFilter
      * GVFmain (make sure you’ve imported all the files from the ‘snake’ folder, since this program calls all those files)
      * checkGrad (calls ‘calibrate’ if images are good)
      * orient
      * matchBright
      * getPollution
    * upload result code (name?)
  * libraries you need to download for all the code to run:
    * pylab (this is optional once the program is totally working because it just displays different things, but while we were coding, esp. when coding the snake, we found it really useful to display the result along the way)
    * python imaging library (PIL)
    * scipy
    * numpy