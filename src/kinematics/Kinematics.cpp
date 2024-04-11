#include <iostream>
#include <math.h>

// robot geometry
const float e = 41;     // end effector
const float f = 105;     // base
const float re = 210;
const float rf = 100;

// trigonometric constants
const float sqrt3 = sqrt(3.0);
const float pi = 3.141592653;    // PI
const float sin120 = sqrt3 / 2.0;
const float cos120 = -0.5;
const float tan60 = sqrt3;
const float sin30 = 0.5;
const float tan30 = 1 / sqrt3;

// forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
// returned status: 0=OK, -1=non-existing position
// Forward Kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
int delta_calcForward(float theta1, float theta2, float theta3, float *x0, float *y0, float *z0) {
    float t = (f - e) * tan30 / 2;
    float dtr = pi / 180.0;

    theta1 *= dtr;
    theta2 *= dtr;
    theta3 *= dtr;

    float y1 = -(t + rf * cos(theta1));
    float z1 = -rf * sin(theta1);

    float y2 = (t + rf * cos(theta2)) * sin30;
    float x2 = y2 * tan60;
    float z2 = -rf * sin(theta2);

    float y3 = (t + rf * cos(theta3)) * sin30;
    float x3 = -y3 * tan60;
    float z3 = -rf * sin(theta3);

    float dnm = (y2 - y1) * x3 - (y3 - y1) * x2;

    float w1 = y1 * y1 + z1 * z1;
    float w2 = x2 * x2 + y2 * y2 + z2 * z2;
    float w3 = x3 * x3 + y3 * y3 + z3 * z3;

    // x = (a1*z + b1)/dnm
    float a1 = (z2 - z1) * (y3 - y1) - (z3 - z1) * (y2 - y1);
    float b1 = -((w2 - w1) * (y3 - y1) - (w3 - w1) * (y2 - y1)) / 2.0;

    // y = (a2*z + b2)/dnm;
    float a2 = -(z2 - z1) * x3 + (z3 - z1) * x2;
    float b2 = ((w2 - w1) * x3 - (w3 - w1) * x2) / 2.0;

    // a*z^2 + b*z + c = 0
    float a_val = a1 * a1 + a2 * a2 + dnm * dnm;
    float b_val = 2 * (a1 * b1 + a2 * (b2 - y1 * dnm) - z1 * dnm * dnm);
    float c = (b2 - y1 * dnm) * (b2 - y1 * dnm) + b1 * b1 + dnm * dnm * (z1 * z1 - re * re);

    // discriminant
    float d = b_val * b_val - 4.0 * a_val * c;
    if (d < 0)
        return -1; // non-existing point

    *z0 = -0.5 * (b_val + sqrt(d)) / a_val;
    *x0 = (a1 * (*z0) + b1) / dnm;
    *y0 = (a2 * (*z0) + b2) / dnm;
    return 0;
}
// Inverse Kinematics : (x0, y0, z0) -> (theta1, theta2, theta3)
// helper functions, calculates angle theta1 (for YZ-pane)
int delta_calcAngleYZ(float x0, float y0, float z0, float *theta) {
    float y1 = -0.5 * 0.57735 * f; // f/2 * tg 30
    y0 -= 0.5 * 0.57735 * e;       // shift center to edge
    // z = a + b*y
    float a = (x0 * x0 + y0 * y0 + z0 * z0 + rf * rf - re * re - y1 * y1) / (2 * z0);
    float b = (y1 - y0) / z0;
    // discriminant
    float disc = -(a + b * y1) * (a + b * y1) + rf * (b * b * rf + rf);
    if (disc < 0)
        return -1; // non-existing point

    float yj = (y1 - a * b - sqrt(disc)) / (b * b + 1); // choosing outer point
    float zj = a + b * yj;
    *theta = 180.0 * atan(-zj / (y1 - yj)) / pi + ((yj > y1) ? 180.0 : 0.0);
    return 0;
}

// inverse kinematics
// returned status: 0=OK, -1=non-existing position
int delta_calcInverse(float x0, float y0, float z0, float *theta1, float *theta2, float *theta3) {
    *theta1 = *theta2 = *theta3 = 0;
    int status = delta_calcAngleYZ(x0, y0, z0, theta1);
    if (status == 0)
        status = delta_calcAngleYZ(x0 * cos120 + y0 * sin120, y0 * cos120 - x0 * sin120, z0, theta2); // rotate coords to +120 deg
    if (status == 0)
        status = delta_calcAngleYZ(x0 * cos120 - y0 * sin120, y0 * cos120 + x0 * sin120, z0, theta3); // rotate coords to -120 deg
    return status;
}

int main() {
    // Forward Kinematics
    // Örnek açı değerleri(degree)
    float theta1 = 30;  
    float theta2 = 45;
    float theta3 = 60;
    // Output: Positions: (23, -37, -223) 

    float x_forward, y_forward, z_forward;

    int status_forward = delta_calcForward(theta1, theta2, theta3, &x_forward, &y_forward, &z_forward);

    if (status_forward == 0) {
        std::cout << "Positions: (" << roundf(x_forward) << ", " << roundf(y_forward) << ", " << roundf(z_forward) << ")" << std::endl;
    } else {
        std::cerr << "Hesaplama hatasi: Geçersiz konum!" << std::endl;
    }

    // Inverse Kinematics
    // Örnek Konum
    float x = 3.82;    
    float y = 68.19;
    float z = -240.5;
    //Output: Theta1 = 60deg, Theta2 = 45deg, Theta3 = 60deg

    float theta1_inverse, theta2_inverse, theta3_inverse;

    int status_inverse = delta_calcInverse(x, y, z, &theta1_inverse, &theta2_inverse, &theta3_inverse);

    if (status_inverse == 0) {
        std::cout << "Motor Angles:\nTheta1 = " << roundf(theta1_inverse) <<"deg" << "\nTheta2 = " << roundf(theta2_inverse) <<"deg" << "\nTheta3 = " << roundf(theta3_inverse) <<"deg" << std::endl;
    } else {
        std::cerr << "Hesaplama hatasi: Geçersiz konum!" << std::endl;
    }

    return 0;
}