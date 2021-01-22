# Bresenham's line algorithm
>Bresenham's line algorithm is a line drawing algorithm that determines the points of an n-dimensional raster that should be selected in order to form a close approximation to a straight line between two points. It is commonly used to draw line primitives in a bitmap image (e.g. on a computer screen), as it uses only integer addition, subtraction and bit shifting, all of which are very cheap operations in standard computer architectures. It is an incremental error algorithm. It is one of the earliest algorithms developed in the field of computer graphics. [More on Wikipedia](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm)


# Objective
Program a method `drawLine(p1,p2,color)` that draws a line in the image from point `p1` to point `p2` with `color`. The points `p1` and `p2` are expressed as matrices (x , y)<sup>T</sup> (column vectors). The color is a tuple of the form `(r,g,b)`, where r,g,b are values between 0 and 255.