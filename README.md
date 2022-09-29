# PathDrawer Coding Challenge
<img src="answer.png" alt="drawing" width="500" />

### Methodology
The algorithm first started by looking for BGR values between the lower[0,0,139] and upper[35,30,188] bounds of BGR. The coordinates of these spots were then stored in an array. The array was split into two arrays with one of them having x-values less than the middle x-value and the other having x-values greater than the middle x-values. Afterwards, a linear regression line was calculated for both arrays to create two best fit lines: one for each side of the track.

### What I Tried That Didn't Work
