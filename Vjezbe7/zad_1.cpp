#include <iostream>
#include <math.h>
#define _USE_MATH_DEFINES
#include <vector>
using namespace std;

class Particle        
{
  public:                 
    double v0, alpha0, x0, y0, dt;    
    double alpha; 
    double vx, vy;
    vector< double > xx;
    vector< double > yy;
    double r0, t0;

    Particle(double v0_, double alpha0_, double x0_, double y0_, double dt_)
    {
      alpha = (alpha0_ * M_PI) / 180;
      vx = v0_ * cos(alpha);    
      vy = v0_ * sin(alpha);
      dt = dt_;
      r0 = x0_;
      t0 = 0.0;
      x0 = x0_;
      y0 = y0_;
    }
    
  private: 
    void move() 
    { 
      for(int i; i <= 10000; i++)
      { 
        x0 = x0 + vx * dt;
        vy = vy - 9.81 * dt;
        y0 = y0 + vy * dt;
        xx.push_back(x0);
        yy.push_back(y0);
        t0 = t0 + dt;
        if(y0 <= 0)
        {
          break;
        }
      }
    }

  public:    
    void range()
    {
      move();  
      double r = x0 - r0;
      cout << "Range of projectile: " << r << " m" << endl;  
    }

      void totalTime()
      {        
        move();
        double t = t0;
        cout << "Total time: " << t << " s" << endl;
      }
};


int main()
{
  Particle p1(100.0, 45.0, 0.0, 0.0, 0.01);
  p1.range();
  p1.totalTime();

  Particle p2(15.0, 40.0, 3.0, 3.0, 0.01);
  p2.range();
  p2.totalTime();

  return 0;
}