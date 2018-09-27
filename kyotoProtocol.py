#Kyoto Protocol

import datetime, random

def dates(year):
    kyotoMessage = ""
    if year == 2012:
        kyotoMessage = "Kyoto Protocol Expires December 13, 2012"
    elif year == 2005:
        kyotoMessage = "The Kyoto Protocol officially goes into force February \
16, 2005"
    elif year == 2001:
        kyotoMessage = "The united states fails to ratify the Kyoto Protocol"
    elif year == 1997:
        kyotoMessage = {"House Message" : "The Kyoto Protocol mandates a reduct\
ion of reported 1990 emissions levels by 6-8 percent by 2008"}
        carMessage = {"Car Message" : "The first consumer hybrid electric autom\
obile is marketed in Japan" }
        return kyotoMessage, carMessage
    return kyotoMessage
    pass

def whatIsKyotoProtocol():
    kyotoDict = {'JI':'Joint Implementation','CDM':'Clean Development Mechanism'
    ,'IET':'International Emission Trading'}
    return kyotoDict

def keyFind():
    message = "List of keys/Acromnymns I would like to find again someday"
    acronym = ['RMU(carbon)','CER','UNFCC(COP22)','LULUCF(reforestion)','REDD+']
    secretList = ['carbonSinks','NDC']
    return acronym

def funFact():
    heading4 = """"""
    ugh = "Doha Amendents"
    wowMessage = "138MT or something like that C02 stuffy by 2030"
    urlList = ["http://www.env.go.jp/en/earth/cc/kptap.pdf","watch?v=IZgBPL17a6M&t=0s"]
    chapter = "To Promote Global Warming Countermeasures in a Sustained Manner"
    return wowMessage

def main():
    importantDates = [1997,2001,2005,2012]
    randomDate = random.choice(importantDates)
    print("What happened in the following year %s?" % randomDate)
    message = dates(randomDate)
    print("Year %s:\nmessage:" % randomDate, message)
    print("What is the kyoto protocol in simple?")
    print(whatIsKyotoProtocol().values())
    print(funFact())
    pass

if __name__ == '__main__':
    main()
