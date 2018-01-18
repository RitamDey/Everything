#include <stdio.h>


typedef struct Vector {
    float x;
    float y;
    float z;
} Vector;


typedef struct Color {
    unsigned short int red;
    unsigned short int green;
    unsigned short int blue;
} Color;


typedef struct Vertex {
    Vector position;
    Color color;
} Vertex;


int main(int argc, char **argv) {
    Vertex vertices[] = {
        {.position = {3323.176, 6562.231, 9351.231},
         .color = {3040, 34420, 54321}},
        {.position = {7623.982, 2542.231, 9823.121},
         .color = {32736, 5342, 2321}},
        {.position = {6352.121, 3432.111, 9763.232},
         .color = {56222, 36612, 11214}},
        {.position = {6729.862, 2347.212, 3421.322},
         .color = {45263, 36291, 36701}}
    };

    FILE *file = fopen("colors.bin", "wb");

    if (file == NULL)
        return -1;

    fwrite(vertices, sizeof(Vertex), 4, file);
    fclose(file);

    return 0;
}
