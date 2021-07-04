# Password dump challenge

## Omschrijving: 	

Password dump die op verschillende underground websites gedeeld wordt. Komt één van onze wachtwoorden er ook in voor?

## Oplossing:

JSCU{PASS_M3_TH3_HASH}

## Writeup:

Het pwdump bestand gedownload op mijn computer en mijn eerste idee was om de hashes te identificeren. Dit via meerdere websites gedaan, waaruit kwam dat dit hoogstwaarschijnlijk een salted MD5 hashes waren. Omdat ik voor HackTheBox en TryHackMe al hashcat had gebruikt om hashes mee te kraken, probeerde ik dat eerst.

Dat lukte totaal niet, een heleboel dictionary attacks geprobeerd met verschillende lijsten wachtwoorden, maar niks lukte. Toen heb ik wat onderzoek gedaan naar het bestand wat ik gekregen had, en op een gegeven moment googled ik op de bestandsnaam: 127.0.0.1.pwdump, omdat het me toch vaag bekend voorkwam. 

Dat bracht me op [deze blogpost](https://gracefulsecurity.com/cracking-windows-domain-passwords-for-password-analysis/), die liet zien dat dit om hashes ging voor windows domain accounts uit een domain controller. De blogpost liet ook zien hoe dit makkelijk via JohnTheRipper te kraken was. De commands uit de blogpost gerund, waar [deze output](john.output) uitkwam, waar na elke USER 1 letter stond die samen de oplossing vormde.