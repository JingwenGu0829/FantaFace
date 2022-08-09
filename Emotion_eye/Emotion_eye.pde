import com.hamoid.*;
float t1=0;

Eye e1, e2, e3;
JSONObject json;
color bgColorTL, bgColorTR, bgColorBR, bgColorBL, bgColorT,bgColorTt;
String emotion_now, emotion_before;
boolean change = false;
float [] thetaMax;
ParticleSystem ps;
ParticleSystem2 ps2;
//float soundDuration = 10.03;
int index=1;
import java.io.File;
//variables for mouth

float theta = 0.0;
//neutral:
int w; 
float[] yvalues; 
float dx; 
int xspacing = 5; 
//disgust mouth:
int dis_xspacing = 1;   
int maxwaves = 10;  
float[] amplitude_dis = new float[maxwaves];  
float[] dis_dx = new float[maxwaves];       
float[] dis_yvalues;     

//surprise, fear mouth:
PVector [] pos;
float [] radiusF, radiusFIncre;



void setup() {
  size(800, 800);
  smooth(8);
  noStroke();
  bgColorTL = bgColorTR = bgColorBR = bgColorBL = bgColorT = bgColorTt = color(#E7C5CC); //neutral background
   
  e1 = new Eye(270, 280, 170);
  e2 = new Eye(470, 290, 170);
 
  ps = new ParticleSystem(new PVector(3*width/4-70,height/2-25));
  ps2 = new ParticleSystem2(new PVector(width/3-30,height/2-25));
  
    //fear, surprise mouth initiation
  pos = new PVector[40];
  radiusF = new float[40];
  radiusFIncre = new float[40];
  for(int i=0; i<pos.length; i++){
    pos[i] = new PVector();
    radiusF[i] = random(100);
    radiusFIncre[i] = random(.005, .015);
  }
  //videoExport = new VideoExport(this, "myVideo.mp4");
  //videoExport.setFrameRate(30);  
  //videoExport.startMovie();
}

void draw() {  
  background();
  String path="C:\\Users\\19051\\Desktop\\Capstoneproject\\json\\result"+str(index)+"json";
  String get_emo="";
  File f=new File(path);
  if(!f.exists()){
      print("file "+str(index)+"not exist");
     //videoExport.endMovie();
      exit();
  }else{
    json=loadJSONObject(path);
    get_emo=json.getString("emotion");
    get_emo=get_emo.substring(0,1).toUpperCase()+get_emo.substring(1,get_emo.length());
    }
  
  //Begin to start the video and end the video
  //if(mousePressed){
  //  if(mouseButton == LEFT){
  //    videoExport.startMovie();
  //  }

  //for(int i=0;i<1000; i++){  //iteration
  //    emotion_before = emotion_now;  //The animation will display emotion_before
      emotion_before = get_emo;//情绪的参数
      print(emotion_before+"\n");
      if (emotion_now == emotion_before){  //if not change, continue
        change = false;
        //continue;
      }
  
   // save the frame
  //}
  
  emotion(emotion_before);
  e1.update(cos(60), sin(60));//左眼球的参数(cos(角度),sin(角度))
  e2.update(cos(60),sin(60));//右眼球的参数
  e1.display1(emotion_before);
  e2.display2(emotion_before);
  saveFrame(str(index)+".jpg");
  index+=1;
}

//background colors
void background(){
  bgColorTL = lerpColor(bgColorTL, bgColorT, .25);
  bgColorTR = lerpColor(bgColorTR, bgColorT, .125);
  bgColorBR = lerpColor(bgColorBR, bgColorT, .625);
  bgColorBL = lerpColor(bgColorBL, bgColorT, .3125);

  noStroke();
  beginShape(QUADS);
  fill(bgColorTL);
  vertex(0, 0);//TL
  fill(bgColorTR);
  vertex(width, 0);//TR
  fill(bgColorBR);
  vertex(width, height);//BR
  fill(bgColorBL);
  vertex(0, height);//BL
  endShape();
}

//Different emotions
void emotion (String type){
  if (type.equals( "Neutral")){
    bgColorT = #E7C5CC;
    neutral_mouth(0);
  }
  if (type.equals( "Happy")){
    bgColorT = #F6C762;
    fill(225,136,57);
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    star(0, 0, 220, 280, 20); 
    popMatrix();
    happy_mouth(80, 300, 310, 320, 270, 325);
    //float open_cred(0~100), float left_mouth_corner_y, float right_mouth_corner_y, float mid_y,float lip_top_y, float lip_bottom_y
  }
  if (type.equals("Disgust")){
    bgColorT = #549C78;
    disgust_background();
    noStroke();
    fill(124,120,14);
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    flower(0, 0, 260, 280, 10); 
    popMatrix();
    disgust_mouth(100);//mouth open_cred(0~100)
  }
  if (type.equals("Anger")){
    bgColorT = #DA4D5B;
    fill(180,20,0);
    anger_background();
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    star(0, 0, 200, 280, 35); 
    popMatrix();
    anger_mouth(80);//mouth open_cred(0~100)
  }
  if (type.equals("Fear")){
    bgColorT = #9B1EA3;
    fear_background();
    fill(110,0,160);
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    flower(0, 0, 230, 270, 17); 
    popMatrix();
    fear_mouth(80);//mouth open_cred(0~100)
  }
  if (type.equals("Sadness")){
    bgColorT = #3A76C8;
    fill(14,65,201);
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    flower(0, 0, 230, 280, 7); 
    popMatrix();
     sad_mouth(80, 300, 320, 290, 270, 325);
    //float mouth open_cred(0~100), float left_mouth_corner_y, float right_mouth_corner_y, float mid_y,float lip_top_y, float lip_bottom_y
    
    
  }
  if (type.equals("Surprise")){
    bgColorT = #EE8833;
    surprise_mouth(80);//mouth open_cred(0~100)
    fill(255,245,46);
    pushMatrix();
    translate(width*0.5, height*0.5);
    rotate(frameCount / 400.0);
    star2(0, 0, 210, 280, 65); 
    popMatrix();
  }
}

//Shape:
//(1) Happy
void star(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a+halfAngle) * radius1;
    sy = y + sin(a+halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}

void star2(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = lerp(x + cos(a+halfAngle-angle) * radius1,x + cos(a+halfAngle) * radius1,0.0125);
    sy = lerp(y + sin(a+halfAngle-angle) * radius1,y + sin(a+halfAngle) * radius1,0.0125);
    vertex(sx, sy);
  }
  endShape(CLOSE);
}

void flower(float x, float y, float radius1, float radius2, int npoints) {
  float angle = TWO_PI / npoints;
  float halfAngle = angle/2.0;
  beginShape();
  for (float a = 0; a < TWO_PI+1; a += angle) {
    float sx = x + cos(a) * radius2;
    float sy = y + sin(a) * radius2;
    curveVertex(sx, sy);
    sx = lerp(x + cos(a+halfAngle-angle) * radius1,x + cos(a+halfAngle) * radius1,0.825);
    sy = lerp(y + sin(a+halfAngle-angle) * radius1,y + sin(a+halfAngle) * radius1,0.825);
    curveVertex(sx, sy);
  }
  endShape(CLOSE);
}   
