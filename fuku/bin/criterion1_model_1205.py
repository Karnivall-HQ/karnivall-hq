# M-001 criterion 1 path model for the 12/05 deadline (Fuku, 2026-11-14 11:02 WIB).
# Judged window: 7d 11/28-12/04 (12/05 07:00 readout). Base = 7d 11/07-11/13 rates (tracker 11/14 row).
# A lever live by 11/27 eve counts all 7 days; live later -> fewer days. BC flat. Run: python3 fuku/bin/criterion1_model_1205.py
# Daily use (07:00 readout): pass the fresh 7d base + today's date, e.g.
#   python3 fuku/bin/criterion1_model_1205.py --peik 2016453 14 --bc 313500 6 --p2 924806 8 --today 2026-11-15
# --budget = PEIKIRA daily SPEND for the window (re-base, added 2026-11-15): expected actual spend, not the CBO setting.
#   CPLs stay the 7d CPLs (INFERRED: flat with spend under the bid cap). Default = PEIKIRA 7d spend / 7.
# Added 2026-11-16 (lesson: two-part criterion): prints the assumed account spend/day next to the LWD
#   and a criterion-2 line (account at Rp 1M/day, PEIKIRA fills the gap at the same CPLs; INFERRED: flat CPL).
#   --cap-throttled flags that the bid cap currently holds PEIKIRA below that spend.
# Defaults = 7d 11/07-11/13. Prints the last workable date (both asks live by eve of that date -> <= 95k).
import argparse, datetime as dt
ap=argparse.ArgumentParser()
ap.add_argument('--peik',nargs=2,type=float,default=[2016453,14],metavar=('SPEND','LEADS'))
ap.add_argument('--bc',nargs=2,type=float,default=[313500,6],metavar=('SPEND','LEADS'))
ap.add_argument('--p2',nargs=2,type=float,default=[924806,8],metavar=('SPEND','LEADS'))
ap.add_argument('--today',default=None)
ap.add_argument('--budget',type=float,default=None,metavar='PEIKIRA_DAILY_SPEND')
ap.add_argument('--cap-throttled',action='store_true',help='bid cap holds PEIKIRA spend below the 1M leg need')
A=ap.parse_args()
P_S,P_L=A.peik; BC_S,BC_L=A.bc
P2_CPL=A.p2[0]/A.p2[1]         # freed spend runs at PEIKIRA2's 7d CPL
P_DAY=A.budget if A.budget else P_S/7; P_CPL=P_S/P_L; BC_DAY=BC_S/7; BC_CPL=BC_S/BC_L
SITE={'none':1.0,'+0.5pt':4.4/3.9,'+1pt':4.9/3.9}
def week(days_on=7, rest=P_CPL, site=1.0, a3_share=0.0, a3_cpl=95000, p_day=None):
    P_DAY_=P_DAY if p_day is None else p_day
    s=l=0.0
    for d in range(7):
        on = d >= 7-days_on
        r = rest if on else P_CPL
        sh = a3_share if on else 0.0
        leads = P_DAY_*(1-sh)/r + (P_DAY_*sh/a3_cpl if sh else 0)
        m = site if on else 1.0
        s += P_DAY_ + BC_DAY; l += (leads + BC_DAY/BC_CPL)*m
    return s/l
def f(x): return f"{x/1000:.1f}k"
rows=[("A  nothing changes", week(0)),
      ("F  Ad015 paused (freed at 115.6k)", week(rest=P2_CPL)),
      ("F' Ad015 paused (freed at 130k)", week(rest=130000)),
      ("C  site +0.5pt", week(site=SITE['+0.5pt'])),
      ("C  site +1pt", week(site=SITE['+1pt'])),
      ("F+C site +0.5pt", week(rest=P2_CPL, site=SITE['+0.5pt'])),
      ("F'+C site +0.5pt (freed at 130k)", week(rest=130000, site=SITE['+0.5pt'])),
      ("E  ADSET-3 1/3 @70k (Ad015 on)", week(a3_share=1/3, a3_cpl=70000)),
      ("F+E ADSET-3 1/3 @70k", week(rest=P2_CPL, a3_share=1/3, a3_cpl=70000)),
      ("F+E ADSET-3 1/3 @95k", week(rest=P2_CPL, a3_share=1/3, a3_cpl=95000)),
      ("F+C+E ADSET-3 1/3 @95k, +0.5pt", week(rest=P2_CPL, site=SITE['+0.5pt'], a3_share=1/3, a3_cpl=95000)),
      ("F+C+E ADSET-3 1/3 @130k, +0.5pt", week(rest=P2_CPL, site=SITE['+0.5pt'], a3_share=1/3, a3_cpl=130000))]
print(f"PEIKIRA {f(P_DAY)}/day{' (--budget)' if A.budget else ''} at {f(P_CPL)}, BC {f(BC_DAY)}/day at {f(BC_CPL)}")
print("Full window (all levers live by 11/27 eve):")
for n,v in rows: print(f"  {n:38s} {f(v):>7s} {'OK' if v<=95000 else 'MISS'}")
print("Late starts (days of 7 the lever is live):")
for days,lbl in [(7,'11/27'),(5,'11/29'),(3,'12/01'),(1,'12/03')]:
    print(f"  live {lbl} eve ({days}d): F+C+0.5pt {f(week(days,P2_CPL,SITE['+0.5pt']))}  F alone {f(week(days,P2_CPL))}  C+0.5 alone {f(week(days,site=SITE['+0.5pt']))}")
# break-even: PEIKIRA-rest CPL needed with no site fix / with +0.5pt, Ad015 question aside
def be_rest(site):
    lo,hi=30000,300000
    for _ in range(60):
        m=(lo+hi)/2
        if week(rest=m,site=site)<=95000: lo=m
        else: hi=m
    return lo
print("Break-even PEIKIRA CPL (full window): no site", f(be_rest(1.0)), "| site +0.5pt", f(be_rest(SITE['+0.5pt'])), "| +1pt", f(be_rest(SITE['+1pt'])))

# Last workable date: latest eve (11/27..12/03) where F+C(+0.5pt) live still gives <= 95k.
start=dt.date(2026,11,27); last=None
for k in range(7):
    if week(7-k,P2_CPL,SITE['+0.5pt'])<=95000: last=start+dt.timedelta(days=k)
line = f"LAST WORKABLE DATE (asks #1+#2 live by eve): {last.strftime('%m/%d') if last else 'NONE: criterion 1 needs more than asks #1+#2'}"
if A.today and last:
    line += f" | days left {(last-dt.date.fromisoformat(A.today)).days} *(calc)*"
print(line)

ACCT_DAY=P_DAY+BC_DAY
print(f"  assumes account spend {f(ACCT_DAY)}/day (PEIKIRA {f(P_DAY)} + BC {f(BC_DAY)}) = {ACCT_DAY/1e6*100:.0f}% of the Rp 1M/day leg *(calc)*")
# Criterion 2: account at Rp 1M/day. PEIKIRA must carry 1M - BC/day.
need=1_000_000-BC_DAY
c2_A=week(0,p_day=need); c2_FC=week(7,P2_CPL,SITE['+0.5pt'],p_day=need)
ok=lambda v:'OK' if v<=95000 else 'MISS'
line2=(f"CRITERION 2 (Rp 1M/day leg): PEIKIRA needs {f(need)}/day ({need/P_DAY:.1f}x assumed) | "
       f"CPL at 1M/day: nothing changes {f(c2_A)} {ok(c2_A)}, F+C+0.5pt {f(c2_FC)} {ok(c2_FC)} *(calc)*")
if A.cap_throttled: line2+=" | BLOCKED: bid cap holds PEIKIRA below this spend"
print(line2)
