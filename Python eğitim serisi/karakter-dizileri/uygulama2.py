kursAdi = "python ilE proGramlAma"
webSite = "https://www.btkakademi.gov.tr/"

msj = " btk akademi  ".strip()
msj = kursAdi.lower()
msj = webSite.count(".")
msj = webSite.startswith("https")
msj = webSite.endswith("tr")
msj = webSite.isalpha()
msj = kursAdi.replace(" ","-")
msj = kursAdi.replace("python","java")
msj = kursAdi.split()
msj = webSite.find("www")

print(msj)