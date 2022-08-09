class Particle {
  PVector position;
  PVector velocity;
  PVector acceleration;
  float lifespan;

  Particle(PVector l) {
    acceleration = new PVector(0, 0.05);
    velocity = new PVector(random(-.5, .5), random(-2, 0));
    position = l.copy();
    lifespan = 255.0;
  }

  void run() {
    update();
    display();
  }

  void update() {
    velocity.add(acceleration);
    position.add(velocity);
    lifespan -= 1.0;
  }

  void display() {
    stroke(255, lifespan);
    fill(color(139,223,255), lifespan);
    ellipse(position.x, position.y, 15, 15);
  }

  boolean isDead() {
    if (lifespan < 0.0) {
      return true;
    } else {
      return false;
    }
  }
}

// A class to describe a group of Particles
// An ArrayList is used to manage the list of Particles 

class ParticleSystem {
  ArrayList<Particle> particles;
  PVector origin;

  ParticleSystem(PVector position) {
    origin = position.copy();
    particles = new ArrayList<Particle>();
  }

  void addParticle() {
    particles.add(new Particle(origin));
  }

  void run() {
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      if (p.isDead()) {
        particles.remove(i);
      }
    }
  }
}


class Particle2 {
  PVector position2;
  PVector velocity2;
  PVector acceleration2;
  float lifespan2;

  Particle2(PVector l) {
    acceleration2 = new PVector(0, 0.05);
    velocity2 = new PVector(random(-.5, .5), random(-2, 0));
    position2 = l.copy();
    lifespan2 = 255.0;
  }

  void run2() {
    update2();
    display2();
  }

  // Method to update position
  void update2() {
    velocity2.add(acceleration2);
    position2.add(velocity2);
    lifespan2 -= 1.0;
  }

  // Method to display
  void display2() {
    stroke(255, lifespan2);
    fill(color(139,223,255), lifespan2);
    ellipse(position2.x, position2.y, 15, 15);
  }

  // Is the particle still useful?
  boolean isDead2() {
    if (lifespan2 < 0.0) {
      return true;
    } else {
      return false;
    }
  }
}

class ParticleSystem2 {
  ArrayList<Particle2> particles2;
  PVector origin2;

  ParticleSystem2(PVector position2) {
    origin2 = position2.copy();
    particles2 = new ArrayList<Particle2>();
  }

  void addParticle2() {
    particles2.add(new Particle2(origin2));
  }

  void run2() {
    for (int i = particles2.size()-1; i >= 0; i--) {
      Particle2 p = particles2.get(i);
      p.run2();
      if (p.isDead2()) {
        particles2.remove(i);
      }
    }
  }
}
