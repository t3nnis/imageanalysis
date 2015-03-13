A project by Kelsey Whitesell and Brendan Kutler

##########################################################################################

Automated programs requiring no human input have become more popular for tedious and sensitive tasks that require a high degree of objectivity and/or technical knowledge, especially over long distances. Our project, analyzing the air quality of rural homes in India based off of air filter data, is one such example. Instead of paying the high cost of sending trained officials to a work site, researchers can instead teach the native people of an area to work an mostly automated program. Thus they have the benefit of working from their own lab, with the best equipment, while also providing feedback to the very people the data is supposed to help, instead of leaving them inside an isolated box.

This project, however, differs from many that have preceded it, starting from our very method of data collection that both expands and limits the project: a cellular phone. Although it provides the ability to transmit data without the internet or wifi connection required by a laptop, it also has a lower resolution camera and less memory space for our third-party code. Therefore the decision of a certain type of a image analysis algorithm, and its implementation is very important: it must be completely compatible with this new platform's limitations, while still utilizing its strengths effectively.

The structure of the project is also different. Since the research is going to be detailed over large lengths of time, the speed of transmitting data can take a back seat to quality control. Also, because of the phone's limited memory space, most of the heavy duty analysis will take place on a home server, thus freeing up processor speed for other applications.

It is very important to make these automated programs accurate, efficient, and robust, with an output that can be easily understood. This explores the issues of analyzing the quality of grayscale images, finding and segmenting objects within those images, and matching two grayscale images, and provides a survey of previously developed algorithms for these tasks.



############################################################################################
> further details to be added later