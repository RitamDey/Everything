#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace std;


int main(int argc, char **argv) {
    String imageName("/home/stux/Images/78A265wPiO4.jpeg");  // by default

    if (argc > 1)
        imageName = argv[1];

    Mat image;

    image = imread(imageName, IMREAD_COLOR); // Read the image file

    if (image.empty()) {
        cout << "Couldn't open image" << std::endl;
        return -1;
    }

    namedWindow("Display Window", WINDOW_AUTOSIZE);  // Create a display
    imshow("Display window", image);  // Show our image inside it

    waitKey(0);  // Wait for a keystroke on the window
    return 0;
}
