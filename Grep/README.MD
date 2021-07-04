# Grep challenge

## Omschrijving: 	

Grep, dé tool voor zoeken naar teksten in bestanden. De normale versie heeft dependencies, maar deze is statisch gecompileerd! Super handig!

## Oplossing:

JSCU{y0u_can_gRep_wHat3v3r_y0u_l1k3}

## Writeup:

Deze Grep binary gedownload op mijn laptop op mijn Linux distributie die draait via [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10). De hint dat deze binary statisch gecompileerd was leidde me direct naar om de binary via `strings` te onderzoeken, en dan via `grep JSCU` te zoeken naar de flag. Dat leverde direct de oplossing op.