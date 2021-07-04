# Yara challenge

## Omschrijving: 	

Met deze Yara regel kun je een groot deel van alle malware samples die in het wild voorkomen detecteren :)

## Oplossing:

JSCU{hEx_eNc0d1nG_rULeSSS}

## Writeup:

Ik had nog nooit van Yara gehoord, dus eerst wat onderzoek gedaan. Uiteindelijk gevonden dat het een tool was om malware the detecteren en classificeren, wat ook al in de hint stond. 

Toen ik dus eenmaal een idee had wat Yara deed en hoe Yara regels werkte, ben ik maar eens naar de regel gaan kijken. Daar zag ik een aantal bestandsnamen staan die veelvoorkomend lijken binnen malware, maar ik zag ook een aantal Hexadecimale variabelen staan. Deze variabelen 1 voor 1 gedecodeerd in [CyberChef](https://gchq.github.io/CyberChef/) via `From Hex` en toen kwam bij de $key2 variable de oplossing eruit. 