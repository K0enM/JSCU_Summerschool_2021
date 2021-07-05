# Firmware encryptie challenge

## Omschrijving: 	

Dit is de ruwe bytecode van de check in de firmware updater. De updater vereist een juist wachtwoord, nog verder uitzoeken.

## Oplossing:

Niet gevonden

## Writeup:

Dit is de enige challenge die ik niet heb kunnen oplossen. Dat komt door een combinatie van een aantal factoren. Ten eerste had ik voordat ik hieraan begon maar een paar Youtube video's gekeken over reverse engineering & assembly. Daarnaast had ik er ook weinig tijd voor doordat ik druk bezig was voor mijn studie.

Ik heb toch geprobeerd om het op te lossen en heb daarvoor de bytecode gedecompileerd met Ghidra en RetDec, waar RetDec duidelijk beter was. Daaruit kon ik opmaken dat er over een array van 25 integers geloopt wordt en dat elke integer in ieder geval geXOR'd wordt met 0x1337. Verder dan dit ben ik niet gekomen. 