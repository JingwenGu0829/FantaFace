class Eye {
  int x, y;
  int size;
  float angle = 0.0;
  PVector v1, v2, v3, v4, v5, v6;
  
  Eye(int tx, int ty, int ts) {
    x = tx;
    y = ty;
    size = ts;
 }
 
 /* Actual Parameters:

  void update(float [] right_corner, float [] left_corner,
  float [] top, float [] bottom, float [] pupil,){
    //map the actual pupil position to the cartoon eye
    x_pupil = map(pupil[0],left_corner[0],right_corner[0], x-size+size/1.4, x+size-size/1.4);
    y_pupil = map(pupil[1],top[1], bottom[1], y-size+size/1.4, y+size-size/1.4);
  }
  
  //neutral eye
  void display(){
    fill(255);
    ellipse(x, y, size, size);
    fill(0);
    ellipse(x_pupil, y_pupil, size/1.4, size/1.4);
  }
*/


  void update(float mx, float my) {
    angle = atan2(my-y, mx-x);
  }
  
//left eye:
  void display1(String type){
    if (type.equals( "Neutral")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size);
      rotate(angle);
      fill(0);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Happy")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      
      float r = size/2.0;
      v1 = new PVector(0, -r);
      v2 = new PVector(r, 0);
      v3 = new PVector(0.6*r, 2.5/4*r);
      v4 = new PVector(0, 0.57*r);
      v5 = new PVector(-0.6*r, 2.5/4*r);
      v6 = new PVector(-r, 0);
      beginShape();
      vertex(v1.x, v1.y);
      bezierVertex(v1.x+40, v1.y, v2.x-10, v2.y-50, v2.x, v2.y);
      bezierVertex(v2.x+10, v2.y+50, v3.x+15, v3.y-5, v3.x, v3.y);
      bezierVertex(v3.x-15, v3.y, v4.x+40, v4.y, v4.x, v4.y);
      bezierVertex(v4.x-40, v4.y, v5.x+20, v5.y, v5.x, v5.y);
      bezierVertex(v5.x-20, v5.y-5, v6.x-10, v6.y+50, v6.x, v6.y);
      bezierVertex(v6.x+10, v6.y-50, v1.x-40, v1.y, v1.x, v1.y);
      endShape();
    
      rotate(angle);
      fill(214,172,2);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Disgust")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size*1.3);
      rotate(angle);
      fill(54,129,12);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Anger")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      beginShape();
      float r = size/2;
      v1 = new PVector(-0.707*r*1.1, -0.707*r*1.1);
      v2 = new PVector(0, -0.707*r*1.27);
      v3 = new PVector(2/2.236*r*1.1, -1/2.236*r*1.1);
      v4 = new PVector(0.6*r*1.1, 2.5/4*r*1.1);
      v5 = new PVector(-0.707*2/3*r*1.1, 0.707*2/3*r*1.1);
      vertex(v1.x, v1.y);
      bezierVertex(v1.x+10, v1.y-10, v2.x-30, v2.y-5, v2.x, v2.y);
      bezierVertex(v2.x+30, v2.y+5, v3.x-10, v3.y-20, v3.x, v3.y);
      bezierVertex(v3.x+10, v3.y+20, v4.x+20, v4.y-20, v4.x, v4.y);
      bezierVertex(v4.x-20, v4.y+20, v5.x+50, v5.y+50, v5.x, v5.y);
      bezierVertex(v5.x-50, v5.y-50, v1.x-10, v1.y+10, v1.x, v1.y);
      endShape();
    
      rotate(angle);
      fill(147,20,0);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Fear")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size*1.3);
      rotate(angle);
      fill(89,5,95);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Sadness")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      
      beginShape();
      float r = size/2;
      v1 = new PVector(-0.707*r*1.1, 0.707*r*1.1);
      v2 = new PVector(0, 0.707*r*1.27);
      v3 = new PVector(2/2.236*r*1.1, 1/2.236*r*1.1);
      v4 = new PVector(0.6*r*1.1, -2.5/4*r*1.3);
      v5 = new PVector(-0.707*2/3*r*1.1, -0.707*2/3*r*1.1);
      vertex(v1.x, v1.y);
      bezierVertex(v1.x+10, v1.y+10, v2.x-30, v2.y+5, v2.x, v2.y);
      bezierVertex(v2.x+30, v2.y-5, v3.x-10, v3.y+20, v3.x, v3.y);
      bezierVertex(v3.x+10, v3.y-20, v4.x+20, v4.y+20, v4.x, v4.y);
      bezierVertex(v4.x-20, v4.y-20, v5.x+50, v5.y-50, v5.x, v5.y);
      bezierVertex(v5.x-50, v5.y+50, v1.x-10, v1.y-10, v1.x, v1.y);
      endShape();
      
      rotate(angle);
      fill(5,7,95);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals( "Surprise")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size*1.3);
      rotate(angle);
      fill(209,202,78);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }  
  }
  
//right eye:
  void display2(String type){
    if (type.equals( "Neutral")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size);
      rotate(angle);
      fill(0);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals( "Happy")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      
      float r = size/2.0;
      v1 = new PVector(0, -r);
      v2 = new PVector(r, 0);
      v3 = new PVector(0.6*r, 2.5/4*r);
      v4 = new PVector(0, 0.57*r);
      v5 = new PVector(-0.6*r, 2.5/4*r);
      v6 = new PVector(-r, 0);
      beginShape();
      vertex(v1.x, v1.y);
      bezierVertex(v1.x+40, v1.y, v2.x-10, v2.y-50, v2.x, v2.y);
      bezierVertex(v2.x+10, v2.y+50, v3.x+15, v3.y-5, v3.x, v3.y);
      bezierVertex(v3.x-15, v3.y, v4.x+40, v4.y, v4.x, v4.y);
      bezierVertex(v4.x-40, v4.y, v5.x+20, v5.y, v5.x, v5.y);
      bezierVertex(v5.x-20, v5.y-5, v6.x-10, v6.y+50, v6.x, v6.y);
      bezierVertex(v6.x+10, v6.y-50, v1.x-40, v1.y, v1.x, v1.y);
      endShape();
    
      rotate(angle);
      fill(214,172,2);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals( "Disgust")){
      pushMatrix();
      translate(x, y);
      rotate(45);
      fill(255);
      ellipse(0, 0, size, size);
      rotate(angle);
      fill(54,129,12);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals( "Anger")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      beginShape();
      float r = size/2;
      v1 = new PVector(0.707*r*1.1, -0.707*r*1.1);
      v2 = new PVector(0, -0.707*r*1.27);
      v3 = new PVector(-2/2.236*r*1.1, -1/2.236*r*1.1);
      v4 = new PVector(-0.6*r*1.1, 2.5/4*r*1.1);
      v5 = new PVector(0.707*2/3*r*1.1, 0.707*2/3*r*1.1);
      vertex(v1.x, v1.y);
      bezierVertex(v1.x-10, v1.y-10, v2.x+30, v2.y-5, v2.x, v2.y);
      bezierVertex(v2.x-30, v2.y+5, v3.x+10, v3.y-20, v3.x, v3.y);
      bezierVertex(v3.x-10, v3.y+20, v4.x-20, v4.y-20, v4.x, v4.y);
      bezierVertex(v4.x+20, v4.y+20, v5.x-50, v5.y+50, v5.x, v5.y);
      bezierVertex(v5.x+50, v5.y-50, v1.x+10, v1.y+10, v1.x, v1.y);
      endShape();
    
      rotate(angle);
      fill(147,20,0);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals( "Fear")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size*1.3);
      rotate(angle);
      fill(89,5,95);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }
    if (type.equals("Sadness")){
      pushMatrix();
      translate(x, y);
      fill(255);
      //ellipse(0, 0, size, size*0.8);
      beginShape();
      float r = size/2;
      v1 = new PVector(0.707*r*1.1, 0.707*r*1.1);
      v2 = new PVector(0, 0.707*r*1.27);
      v3 = new PVector(-2/2.236*r*1.1, 1/2.236*r*1.1);
      v4 = new PVector(-0.6*r*1.1, -2.5/4*r*1.3);
      v5 = new PVector(0.707*2/3*r*1.1, -0.707*2/3*r*1.1);
      vertex(v1.x, v1.y);
      bezierVertex(v1.x-10, v1.y+10, v2.x+30, v2.y+5, v2.x, v2.y);
      bezierVertex(v2.x-30, v2.y-5, v3.x+10, v3.y+20, v3.x, v3.y);
      bezierVertex(v3.x-10, v3.y-20, v4.x-20, v4.y+20, v4.x, v4.y);
      bezierVertex(v4.x+20, v4.y-20, v5.x-50, v5.y-50, v5.x, v5.y);
      bezierVertex(v5.x+50, v5.y+50, v1.x+10, v1.y-10, v1.x, v1.y);
      endShape();
      
      rotate(angle);
      fill(5,7,95);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
      ps.addParticle();
      ps2.addParticle2();
      ps.run();
      ps2.run2();
    }
    if (type.equals( "Surprise")){
      pushMatrix();
      translate(x, y);
      fill(255);
      ellipse(0, 0, size, size*1.3);
      rotate(angle);
      fill(209,202,78);
      ellipse(size/8, 0, size/1.4, size/1.4);
      popMatrix();
    }  
  }
}
