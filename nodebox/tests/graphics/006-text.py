size(300, 300)
fontsize(40)
fill(0, 0.5)
stroke(0)
line(0,150, WIDTH, 150)
line(10, 0, 10, HEIGHT)
text("hamburgevons", 10, 150)
nofill()
p = text("hamburgevons", 10, 150, outline=True)
(x, y), (w,h) = p.bounds
rect(x, y, w, h)