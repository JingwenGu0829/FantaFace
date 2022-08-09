//neutral mouth
void neutral_mouth(float open_cred){
  //Sine Wave by Daniel Shiffman. 
  float period = 500.0;
  w = width+16;
  dx = (TWO_PI / period) * xspacing;
  yvalues = new float[w/xspacing];
  neutral_calcWave(open_cred);
  neutral_renderWave();
}

void neutral_calcWave(float open_cred) {
  theta += 0.02;
  float x = theta;
  float amplitude = map(open_cred, 0, 100, 25.0, 50); //amplitude change with the opening of the mouth
  for (int i = 0; i < yvalues.length; i++) {
    yvalues[i] = sin(x)*amplitude;
    x+=dx;
  }
}
void neutral_renderWave() {
  pushMatrix();
  noStroke();
  fill(255);
  translate(0, 150);
  for (int x = 0; x < yvalues.length; x++) {
    ellipse(x*xspacing, height/2+yvalues[x], 16, 16);
  }
  popMatrix();
}

//disgust mouth:
void disgust_mouth(float open_cred){
  randomSeed(10);
  int w;  
  w = width + 16;
  dis_yvalues = new float[w/dis_xspacing];
  maxwaves = round(map(open_cred, 0, 100, 2, 10));//map the opening of the mouth to the amplitudud of the waves
  theta += 0.2;

  for (int i = 0; i < maxwaves; i++) {
    amplitude_dis[i] = random(10,30);
    float period = random(100,150); 
    dis_dx[i] = (TWO_PI / period) * dis_xspacing;
  }

  for (int i = 0; i < dis_yvalues.length; i++) {
    dis_yvalues[i] = 0;
  }
  for (int j = 0; j < maxwaves; j++) {
    float x = theta;
    for (int i = 0; i < dis_yvalues.length; i++) {
      if (j % 2 == 0)  dis_yvalues[i] += sin(x)*amplitude_dis[j];
      else dis_yvalues[i] += cos(x)*amplitude_dis[j];
      x+=dis_dx[j];
    }
  }
  disgust_renderWave();
}

void disgust_renderWave() {
  pushMatrix();
  noStroke();
  fill(54,129,12);
  translate(0, 100, 2);
  ellipseMode(CENTER);
  for (int x = 0; x < dis_yvalues.length; x++) {
    ellipse(x*dis_xspacing,height/2+dis_yvalues[x],16,16);
  }
  popMatrix();
}

//Angery Mouth:
void anger_mouth(float open_cred){
  randomSeed(10);
  int w;  
  w = width + 16;
  dis_yvalues = new float[w/dis_xspacing];
  maxwaves = round(map(open_cred, 0, 100, 2, 10));//map the opening of the mouth to the amplitudud of the waves
  theta += 0.2;

  for (int i = 0; i < maxwaves; i++) {
    amplitude_dis[i] = random(10,30);
    float period = random(100,150); 
    dis_dx[i] = (TWO_PI / period) * dis_xspacing;
  }

  for (int i = 0; i < dis_yvalues.length; i++) {
    dis_yvalues[i] = 0;
  }
  for (int j = 0; j < maxwaves; j++) {
    float x = theta;
    for (int i = 0; i < dis_yvalues.length; i++) {
      if (j % 2 == 0)  dis_yvalues[i] += sin(x)*amplitude_dis[j];
      else dis_yvalues[i] += cos(x)*amplitude_dis[j];
      x+=dis_dx[j];
    }
  }
  anger_renderWave();
}

void anger_renderWave() {
  pushMatrix();
  noStroke();
  fill(253,91,79);
  translate(0, 100, 2);
  ellipseMode(CENTER);
  for (int x = 0; x < dis_yvalues.length; x++) {
    ellipse(x*dis_xspacing,height/2+dis_yvalues[x],16,16);
  }
  popMatrix();
}

//Sad mouth:
void sad_mouth(float open_cred, float left_mouth_corner_y, float right_mouth_corner_y, float mid_y,
               float lip_top_y, float lip_bottom_y){
  pushMatrix();
  fill(156,192,248);
  noStroke();
  translate(0, 180, 2);
  float leftY = map(left_mouth_corner_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float rightY = map(right_mouth_corner_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float midY = map(mid_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float open = map(open_cred, 0, 100, 2, 40);
  
  beginShape();
  strokeWeight(2);
  curveVertex(0, leftY);
  curveVertex(0, leftY);
  curveVertex(350, midY);
  curveVertex(800, rightY);
  curveVertex(800, rightY-10);
  curveVertex(350, midY-open);
  curveVertex(0, leftY-14);
  curveVertex(0, leftY-14);
  endShape();
  popMatrix();
}

//Happy Mouth:
void happy_mouth(float open_cred, float left_mouth_corner_y, float right_mouth_corner_y, float mid_y,
               float lip_top_y, float lip_bottom_y){
  pushMatrix();
  fill(245,225,164);
  noStroke();
  translate(0, 140, 2);
  float leftY = map(left_mouth_corner_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float rightY = map(right_mouth_corner_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float midY = map(mid_y, lip_top_y-10, lip_bottom_y+10, 300, 400);
  float open = map(open_cred, 0, 100, 2, 40);
  
  beginShape();
  strokeWeight(2);
  curveVertex(0, leftY+18);
  curveVertex(0, leftY+18);
  curveVertex(350, midY+open);
  curveVertex(800, rightY+8);
  curveVertex(800, rightY);
  curveVertex(350, midY);
  curveVertex(0, leftY);
  curveVertex(0, leftY);
  endShape();
  popMatrix();
}

//Surprise_Mouth:
void surprise_mouth(float open_cred){
  for(int i=0; i<pos.length; i++){
    radiusF[i] += radiusFIncre[i];
    float theta = map(i, 0, pos.length, 0, TWO_PI);
    float r = map(noise(radiusF[i]*5), 0, 1, 60, 65);
    float open = map(open_cred, 0, 100, 1,1.5);
    pos[i].set(cos(theta)*r+width*.5, sin(theta)*r*open+width*.5);
  }
  pushMatrix();
  noStroke();
  beginShape();
  translate(-30, 100, 2);
  fill(255,202,56);
  for(int i=0; i<pos.length+3; i++){
    int idx = i%pos.length;
    curveVertex(pos[idx].x, pos[idx].y);
  }
  endShape();
  popMatrix();
}

//Fear mouth
void fear_mouth(float open_cred){
  for(int i=0; i<pos.length; i++){
    radiusF[i] += radiusFIncre[i];
    float theta = map(i, 0, pos.length, 0, TWO_PI);
    float r = map(noise(radiusF[i]*5), 0, 1, 60, 65);
    float open = map(open_cred, 0, 100, 1,1.5);
    pos[i].set(cos(theta)*r+width*.5, sin(theta)*r*open+width*.5);
  }
  pushMatrix();
  noStroke();
  beginShape();
  translate(-30, 100, 2);
  fill(89,5,95);
  for(int i=0; i<pos.length+3; i++){
    int idx = i%pos.length;
    curveVertex(pos[idx].x, pos[idx].y);
  }
  endShape();
  popMatrix();
}
