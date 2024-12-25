from utils import load_input
a = load_input(__file__)

from time import perf_counter
t0 = perf_counter()

total = 0
line_no = 0
while line_no < len(a):
    btna = a[line_no]
    btnb = a[line_no+1]
    prize = a[line_no+2]
    line_no += 4
    
    ax = int(btna.split("X")[1].split(",")[0])
    ay = int(btna.split(", Y")[1])
    bx = int(btnb.split("X")[1].split(",")[0])
    by = int(btnb.split(", Y")[1])
    px = int(prize.split("X=")[1].split(",")[0])
    py = int(prize.split("Y=")[1])
    
    # Pre-computed solutions to the following simultaneous equations:
    #   c*ax + d*bx = px
    #   c*ay + d*by = py
    #
    # Where c is number of button A presses and d is number of button B presses
    #
    # Also, check that denominator divides numerator to ensure a whole number of presses
    
    if (py*ax-px*ay) % (by*ax-bx*ay) != 0:
        continue
    
    d = (py*ax-px*ay) // (by*ax-bx*ay)
    
    if (px-d*bx) % ax != 0:
        continue
    
    c = (px-d*bx) // ax

    total += 3*c + d

print(total)
print(f'Time: {(perf_counter()-t0) * 1000:.3f}ms')