void fear_background(){
  
  int amt = 10000, cols = 100, rows=100;
  float cellSize;
  
  cellSize = width*1.0/cols; 
  bgColorT = color(85,23,89);
  
  for(int i = 0;i<amt;i++){
    int col= i%cols;
    int row= i/cols;
    float x = map(col, 0, cols-2, cellSize*.5, width-cellSize*.5);
    float y = map(row, 0, rows-2, cellSize*.5, height-cellSize*.5);
    float rtt = map(noise(col*.05, row*.05, 0.01), 0,1,-PI*1.5, PI*1.5);
    
    pushMatrix();
    translate(x,y);
    rotate(rtt+frameCount*0.1);
    strokeWeight(60);
    stroke(156,31,164,40);
    line(0, 0, 20, 0);
    popMatrix();
  }
}

void anger_background(){
  int amt = 10000, cols = 100, rows=100;
  float cellSize;
  
  cellSize = width*1.0/cols; 
  bgColorT = color(120);
  
  for(int i = 0;i<amt;i++){
    int col= i%cols;
    int row= i/cols;
    float x = map(col, 0, cols-2, cellSize*.5, width-cellSize*.5);
    float y = map(row, 0, rows-2, cellSize*.5, height-cellSize*.5);
    float rtt = map(noise(col*.05, row*.05, 0.01), 0,1,-PI*1.5, PI*1.5);
    
    pushMatrix();
    translate(x,y);
    rotate(rtt+frameCount*0.1);
    strokeWeight(60);
    stroke(255,141,133,40);
    line(0, 0, 20, 0);
    popMatrix();
  }
}

void disgust_background(){
  int cols = 10, rows = 10;
  int amt = cols*rows;
  float cellSize;
  
  noFill();
  stroke(0);
  strokeWeight(5);
  bgColorT = #549C78;
  cellSize = width*1.0/cols;
  thetaMax = new float[amt];
  
  for(int i=0; i<amt; i++){
    int col = i%cols;
    int row = i/cols;
    float ctrX = map(col, 0, cols-1, cellSize*.5, width-cellSize*.5);
    float ctrY = map(row, 0, rows-1, cellSize*.5, height-cellSize*.5);
    drawSpiral(120, i, ctrX, ctrY, PI*.25*i, cellSize*.5);
  }
}

void drawSpiral(int res, int idx, float ctrX, float ctrY, float thetaOfst, float rMax){
  float d = dist(cos(60), sin(60), ctrX, ctrY); //前两个的角度是眼球角度
  d = constrain(d, 0, width*.7);
  thetaMax[idx] = lerp(thetaMax[idx], map(d, 0, width*.5, TWO_PI*4, 0), .0625);
  
  beginShape();
  for(int i=0; i<res; i++){
    float theta = map(i, 0, res-1, 0, thetaMax[idx]*6)+thetaOfst;
    float r = map(i, 0, res-1, rMax, 0);
    float x = cos(theta)*r+ctrX;
    float y = sin(theta)*r+ctrY;
    vertex(x, y);
  }
  endShape();
}
