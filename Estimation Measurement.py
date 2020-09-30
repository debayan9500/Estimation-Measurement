import numpy as np
import datetime
name = input("What is your name :").upper()
print("\nHAVE A NICE DAY", name)
print("WELCOME TO EVAPORATION CALCULATION")
print("IT IS CREATED BY DEBAYAN GHOSH")
print("your data should be in this format :"
      "\n"
      "\nDistance from     Depth   Current meter            Duration of"
      "\nLeft water edge           revolution at 0.6d       observation"
      "\n"
      "\nWe are using v = 0.51Ns + 0.03 as a velocity equation\n")
while True:
    distace_left_edge = []
    depth = []
    current_meter_rev = []
    duration = []
    w = []
    final_w = []
    rev_per_sec = []
    velocity = []
    del_q = []
    n = int(input("no of section: "))
    if n >=4 :

        for i in range(0,n):
            print("distance from edge",i+1 ,": ")
            ele1 = float(input())
            distace_left_edge.append(ele1)
        for i in range(0,n):
          print("depth",i+1 ,": ")
          ele2 = float(input())
          depth.append(ele2)
        for i in range(0,n):
            print("rev",i+1 ,": ")
            ele3 = float(input())
            current_meter_rev.append(ele3)
        for i in range(0,n):
            print("duration",i+1 ,": ")
            ele4 = float(input())
            duration.append(ele4)
        matrix1 = np.array([distace_left_edge,depth,current_meter_rev ,duration])
        transpose_matrix1= np.transpose(matrix1)
        for i in range(0,n-1):
            ele5 = distace_left_edge[i+1] - distace_left_edge[i]
            w.append(ele5)
        final_w.append(0)
        ele6 = ((w[0] + (w[1]/2))**2)/(2*w[0])
        final_w.append(ele6)
        for i in range(1,n-3):
            ele7 = (w[i]+w[i+1])/2
            final_w.append(ele7)
        ele8 = ((w[n-2] + (w[n-3]/2))**2)/(2*w[n-2])
        final_w.append(ele8)
        final_w.append(0)
        rev_per_sec = np.array(current_meter_rev)/np.array(duration)
        for i in range(0,n):
            v = (0.51 * rev_per_sec[i]) + 0.03
            velocity.append(v)
        del_q = (np.array(depth)*np.array(velocity)*np.array(final_w))
        main_matrix  = [distace_left_edge, depth, final_w, rev_per_sec, velocity, del_q]
        transpose_main_matrix = np.transpose(main_matrix)
        print("Distance from     Depth   Average Width   Revolutions     Velocity    Q")
        print("Left water edge                           per sec ")
        print(transpose_main_matrix)
        final_del_q = np.sum(del_q)
        print("The value of delta Q is ",final_del_q)
        f = open("Estimation Measurement.rtf", "a")
        dt = datetime.datetime.today()
        f.write(name)
        f.write(" %ls" %dt)
        f.write("\nDist.from   Depth   Average    Rev.      Vel.     Q")
        f.write("\nleft edge           Width      per sec ")

        f.write("\n%ls"%transpose_main_matrix)
        f.write("\nQ = %d "%final_del_q)
        f.close()

    else:

        print("Please enter the value which is greater than 3")


