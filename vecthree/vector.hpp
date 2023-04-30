#pragma once

struct Vector
{
    Vector() : x(0), y(0) {}
    Vector(double _1, double _2) : x(_1), y(_2) {}

    friend bool operator==(const Vector& first, const Vector& second)
    {
        return first.x == second.x && first.y == second.y;
    }

    double x;
    double y;
};

#define PI 3.141592653589793238462643383

constexpr double radians_to_degrees(double r)
{
    return r * 180/PI;
}

constexpr double degrees_to_radians(double r)
{
    return r * PI/180;
}

Vector add(const Vector& vecone, const Vector& vectwo){
    Vector vec;

    vec.x = vecone.x + vectwo.x;
    vec.y = vecone.y + vectwo.y;

    return vec;
}

Vector sub(const Vector& vecone, const Vector& vectwo){
    Vector vec;

    vec.x = vecone.x - vectwo.x;
    vec.y = vecone.y - vectwo.y;

    return vec;
}

Vector scale(Vector mvec, const int val){
    mvec.x = mvec.x * val;
    mvec.y = mvec.y * val;

    return mvec;
}

double magnitude(const Vector& vec){
	double tot = 0;

	tot += vec.x * vec.x;
    tot += vec.y * vec.y;
	
	return round(sqrt(tot));
}

Vector normalize(Vector vec){
    const auto magvec = magnitude(vec);

    vec.x = vec.x / magvec;
    vec.y = vec.y / magvec;
    
	return vec;
}

double dot(const Vector& vecone, const Vector& vectwo){
	double h = 0;

	auto prod = vecone.x * vectwo.x;
	h += prod;

	prod = vecone.y * vectwo.y;
	h += prod;

	return h;
}

double get_angle(const Vector& vecone, const Vector& vectwo){
    double ang = 0.;

    if (vecone == vectwo)
        return ang;

    const auto mdot = dot(vecone, vectwo);
    const auto mag1 = magnitude(vecone);
    const auto mag2 = magnitude(vectwo);

    const auto acos_res = radians_to_degrees(acos(mdot/(mag1*mag2)));

    ang = static_cast<double>(acos_res);

    return ang;
}
