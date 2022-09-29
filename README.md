# PathDrawer Coding Challenge
<img src="answer.png" alt="drawing" width="500" />

### Methodology
The algorithm first started by looking for BGR values between the lower[0,0,139] and upper[35,30,188] bounds of BGR. The coordinates of these spots were then stored in an array. The array was split into two arrays with one of them having x-values less than the middle x-value and the other having x-values greater than the middle x-values. Afterwards, a linear regression line was calculated for both arrays to create two best fit lines: one for each side of the track. These lines were then plotted on the screen.

### What I Tried That Didn't Work

My first attempt included trying to use one specific orange-red color that the cones all had. However, the variations in lighting drastically changed the color of the cones near the top compared to the ones near the bottom. I also tried using a middle value using a median value, however, the model had more difficulty recognizing points on the right side compared to the left side. I also considered ony using one coordinate per cone, but issues arised when the exit sign was registered as an orange-red color.

### What Libraries Are Used

* NumPy
* Math
* OpenCV
