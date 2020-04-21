#!/usr/bin/env python3

import os
import sys
import json
import pandas as pd

class CurrencyExchangeFunction:
    def __init__(self):
        tmpdir = "historicrates"
        self.exfile = os.path.join(tmpdir, "exchange_data_auto.txt")
        self.df_buy = None

    def analyse(self):
        snapshotfiles = os.listdir(os.path.dirname(self.exfile))
        snapshotfiles = [sf for sf in snapshotfiles if sf.startswith(os.path.basename(self.exfile) + ".")]
        snapshotfiles.sort()

        curidx = {}
        df_buy = pd.DataFrame({"Currency": []})
        for snapshotfile in snapshotfiles:
            date = snapshotfile.split(".")[-1]
            f = open(os.path.join(os.path.dirname(self.exfile), snapshotfile))
            c = json.load(f)
            for k, v in c.items():
                buy = v[1]
                rowpos = curidx.setdefault(k, df_buy.shape[0])
                df_buy.loc[rowpos, "Currency"] = k
                df_buy.loc[rowpos, date] = buy
        df_buy = df_buy.set_index(["Currency"])
        self.df_buy = df_buy

    def daterange(self):
        dr = {"start": self.df_buy.columns[0], "end": self.df_buy.columns[-1]}
        print(dr)
        return json.dumps(dr)

    def evolution(self, fromdate=None, todate=None, withtop=True):
        evolution = {}
        fromidx = 0
        toidx = -1
        if fromdate:
            fromidx = self.df_buy.columns.get_loc(fromdate)
        if todate:
            toidx = self.df_buy.columns.get_loc(todate)
        for row in self.df_buy.iterrows():
            evolution[row[0]] = 100 * (row[1][toidx] - row[1][fromidx]) / row[1][fromidx]
        if withtop:
            self.evolution_top(evolution, fromidx, toidx)
        return self.evolution_all(evolution, fromidx, toidx)

    def evolution_all(self, evolution, fromidx, toidx):
        evolution = {k: round(evolution[k], 2) for k in sorted(evolution)}
        print(evolution)
        return json.dumps(evolution)

    def evolution_top(self, evolution, fromidx, toidx):
        evolution = {k: evolution[k] for k in sorted(evolution, key=lambda k: evolution[k], reverse=True)}
        for idx, (k, v) in enumerate(evolution.items()):
            if idx < 5 or idx >= len(evolution) - 5:
                print(f"#{idx:2} {k} {round(v,3):+6.2f}%")
            elif idx == 5:
                print("...")

def gfunc(request):
    #req = request.get_json()
    req = request.args
    cef = CurrencyExchangeFunction()
    cef.analyse()
    if "dates" in req:
        return cef.daterange()
    else:
        fromdate = None
        todate = None

        if "fromdate" in req:
            fromdate = req["fromdate"]
        if "todate" in req:
            todate = req["todate"]
        return cef.evolution(fromdate, todate, False)

if __name__ == "__main__":
    fromdate = None
    todate = None

    if len(sys.argv) >= 2:
        fromdate = sys.argv[1]
    if len(sys.argv) == 3:
        todate = sys.argv[2]

    cef = CurrencyExchangeFunction()
    cef.analyse()
    cef.daterange()
    cef.evolution(fromdate, todate, True)
