#Photovoltaic cells
import webbrowser

key1 = """Kyoto Protocol expires December 13, 2012."""
key2 = """Negotiations on the transfer of clean energy technologies to developing nations
continue at the Conference of the Parties (COP16) to the United Nations Framework
Convention on Climate Change in Cancun, Mexico"""
key3 = 'Fukushima Daiichi'
key4 = "Electron cyclotron resonance plasma enhanced sputtering system glows -Semiconductor"

def photovoltaicDef():
    PHOTOVOLTAIC = """A device or material capable of producing an electric current
    when exposed to electromagnetic energy most often sunlight"""
    photoVoltaicCellImgUrl = "https://www.bing.com/images/search?q=photovoltaic+cells&FORM=HDRSC2"
    #webbrowser.open(photoVoltaicCellImgUrl)
    return PHOTOVOLTAIC

def photovoltaicSolarPowerDef():
    PHOTOVOLATICSOLARPOWER = """Electricity produced by photovoltaic cells which are semiconductor
    devices that produce electricity when exposed to light. Depending on the cell design between
    6% and 42% of energy falling on the photovoltaic cell is turned into electricity"""
    return PHOTOVOLATICSOLARPOWER


def photoVoltaicCells(date):
    subHeading = "The promise of solar energy: As cheap as fossil fuels?"
    costUnits = ["USD"]
    keyNames = ["SunShot Initiative", "U.S Department of Energy"]
    usTotalRenewableEnergy2010 = 1
    totalEnergySavedPVPerWatt = 0
    yearsMention = [2010,2006,2000,2011]
    title = "The promise of solar energy: As cheap as fossil fuels?"
    names = ['WalterVarhur','MikeCross']
    solarPower = .01 * usTotalRenewableEnergy2010
    electricityGrowthSolarPower20062010 = .12
    costToInstallSolarPowerPerWatt = 4.5
    for i in range(5):
        windBioMass = i * electricityGrowthSolarPower20062010
    print(subHeading)
    for i in range(11):
        totalEnergySavedPVPerWatt = totalEnergySavedPVPerWatt + costToInstallSolarPowerPerWatt


    print("Despite the failure of solar power to generate more than about", solarPower, "\
 of the US total energy")
    print("The total growth of wind bio mass energy From 2006 - 2010 over a 4 year\
 period", windBioMass)
    print("Each year that was about", electricityGrowthSolarPower20062010, "avg growth per year")
    print("By", yearsMention[3], "improvements in commerical PV Cell led to a steady\
 decline in solar cell prices to", costToInstallSolarPowerPerWatt, costUnits[0])
    print("Created in", date, keyNames[0], "seeks PV cell prices 1", costUnits[0], "\
 per watt" )
    print("A reasonable pay-back timeframe is 10-12 years. If you bought it in\
 2011 for",costToInstallSolarPowerPerWatt,"per watt the total engery spent would be\
 ",totalEnergySavedPVPerWatt,"per watts before you would have decreased utility bills" )




def main():
    print("What is photovoltaic?")
    p = photovoltaicDef()
    print(p)
    print("What is photovoltaic solar power?")
    pv = photovoltaicSolarPowerDef()
    print(pv)
    photoVoltaicCells(2011)
    pass

if __name__ == '__main__':
    main()
