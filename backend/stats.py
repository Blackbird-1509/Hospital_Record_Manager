import backend.sqlconnect as sqlconnect
import matplotlib.pyplot as mpl
import matplotlib

matplotlib.use("Agg")

#Gender Ratio in Different Age Groups
def stats_calculate():
    connector, cur = sqlconnect.connect('admin', 'hospital123')
    gx,gm,gf=[],[],[]
    for i in range(20,60,10):
        cur.execute("select count(*) from patient_records where gender='M' and age between %s and %s",(i,i+9))
        g1=cur.fetchall()
        gm.append(g1[0][0])
        cur.execute("select count(*) from patient_records where gender='F' and age between %s and %s",(i,i+9))
        g2=cur.fetchall()
        gf.append(g2[0][0])
        gx.append(f"{i}-{i+9}")
    mpl.bar([x-0.25 for x in range(len(gx))],gm,width=0.25,label="Male",color='b')
    mpl.bar([x for x in range(len(gx))],gf,width=0.25,label="Female",color='r')
    mpl.xlabel("Age Group")
    mpl.ylabel("Count")
    mpl.title("Gender Ratio in Different Age Groups")
    mpl.xticks(range(len(gx)),gx)
    mpl.legend()
    mpl.savefig("output1.jpg")
    mpl.close()

#blood group distribution
    cur.execute("select blood_type,count(*) from patient_records group by blood_type")
    b=cur.fetchall()
    bt=[]
    btc=[]
    for i in b:
        bt.append(i[0])
        btc.append(i[1])
    mpl.pie(btc,autopct=lambda pct: f"{pct/100*sum(btc):.2f}%",labels=bt,wedgeprops={'linewidth': 1, 'edgecolor': "black"})
    mpl.savefig("output2.jpg")
    mpl.close()

#bmi vs age
    cur.execute("select age,weight,height*height from patient_records")
    bmi=[]
    age=[]
    for i in sorted(cur.fetchall()):
        age.append(i[0])
        bmi.append(i[1]/i[2]*10000)
    mpl.plot(age,bmi)
    mpl.xlabel("BMI")
    mpl.ylabel("Age")
    mpl.title("BMI vs Age")
    mpl.savefig("output3.jpg")
    mpl.close()