# 11/20 gate scenario model (Fuku, 2026-11-14). Edit the base numbers at the top with each readout, lock known window days, run: python3 fuku/bin/gate_model_1120.py
# Window 11/13-11/19. Day 11/13 actual PEIKIRA 293,851/0. BC flat at 7d rate all 7 days.
P_DAY=2016453/7; P_CPL=2016453/14
BC_S=313500; BC_L=6
D13_S=293851; D13_L=0
P2_CPL=924806/8
def run(days_changed, peik_cpl_after, site=1.0, a3_share=0, a3_cpl=None):
    # 11/14..11/19 = 6 days; last `days_changed` days changed
    s=D13_S; l=D13_L
    for d in range(6):
        ch = d >= 6-days_changed
        if not ch:
            s+=P_DAY; l+=P_DAY/P_CPL
        else:
            base=peik_cpl_after
            if a3_share:
                cpl=(1-a3_share)*base + 0  # spend-weighted leads
                leads=P_DAY*(1-a3_share)/base + P_DAY*a3_share/a3_cpl
            else:
                leads=P_DAY/base
            s+=P_DAY; l+=leads*site
    # BC: site multiplier only on changed days
    bc_day_s=BC_S/7; bc_day_l=BC_L/7
    for d in range(7):
        ch = d >= 7-days_changed
        s+=bc_day_s; l+=bc_day_l*(site if ch else 1)
    return s/l, l
print("A nothing:", [round(x,1) for x in run(0,P_CPL)])
for days,lbl in [(5,'live 11/14 eve'),(4,'11/15 eve'),(3,'11/16 eve')]:
    print(lbl)
    print("  Ad015 paused, freed->P2 115.6k:", round(run(days,P2_CPL)[0]))
    print("  Ad015 paused, freed at 130k:", round(run(days,130000)[0]))
    print("  Site +0.5pt:", round(run(days,P_CPL,site=4.4/3.9)[0]), " +1pt:", round(run(days,P_CPL,site=4.9/3.9)[0]))
    print("  Ad015+site0.5 (115.6k):", round(run(days,P2_CPL,site=4.4/3.9)[0]), " +1pt:", round(run(days,P2_CPL,site=4.9/3.9)[0]))
    for sh in (1/3,0.6):
        print(f"  A3 share {sh:.2f} @70/95/130 (rest 144k):", [round(run(days,P_CPL,a3_share=sh,a3_cpl=c)[0]) for c in (70000,95000,130000)])
        print(f"  Ad015 paused + A3 {sh:.2f} @70/95/130 (rest 115.6k):", [round(run(days,P2_CPL,a3_share=sh,a3_cpl=c)[0]) for c in (70000,95000,130000)])
        print(f"  ALL (Ad015+site .5+A3 {sh:.2f}) @70/95/130:", [round(run(days,P2_CPL,site=4.4/3.9,a3_share=sh,a3_cpl=c)[0]) for c in (70000,95000,130000)])
# break-even A3 CPL, share 1/3 and 0.6, with/without Ad015 pause, live 11/14 eve
def be(share, rest, site=1.0, days=5):
    lo,hi=10000,300000
    for _ in range(60):
        m=(lo+hi)/2
        if run(days,rest,site=site,a3_share=share,a3_cpl=m)[0]<=95000: lo=m
        else: hi=m
    return round(lo)
print("BE A3 (5d):", {f"{sh:.2f}/{n}":be(sh,r) for sh in (1/3,0.6,0.8) for n,r in (("144k",P_CPL),("Ad015off",P2_CPL))})
print("BE A3 + site .5:", {f"{sh:.2f}":be(sh,P2_CPL,site=4.4/3.9) for sh in (1/3,0.6)})
print("Ad015off+site+1pt 5d:", round(run(5,P2_CPL,site=4.9/3.9)[0]))
