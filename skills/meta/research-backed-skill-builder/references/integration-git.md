# Intégration au dépôt et maintenance

## Placement portable

Inspecter les instructions et l'arborescence du dépôt. Dans un catalogue utilisant la CLI `skills`, un emplacement comme `skills/<domaine>/<nom>/SKILL.md` permet de regrouper les sujets ; confirmer la découverte avec la version réellement disponible. Ne pas créer de `SKILL.md` englobant qui masque les skills imbriquées. Chaque skill installable contient ses références nécessaires et ne dépend pas du corpus du dépôt après installation.

Ajouter la skill au catalogue existant, indiquer une commande d'installation adaptée et expliquer où se trouvent le corpus et la maintenance. Vérifier les chemins existants, noms, conflits et modifications locales ; ne pas écraser d'autres travaux ou régénérer des fichiers sans raison.

## Git et publication

- Avant de commencer, examiner `git status`, branche et consignes applicables ; choisir une branche ou un espace isolé si nécessaire. Préserver les modifications préexistantes, même non suivies.
- Préparer les seuls fichiers de la mission, inspecter leur diff et leur provenance, vérifier les données sensibles et les droits des tiers. Ne pas utiliser un ajout global qui embarquerait des changements étrangers.
- Lorsque la mission demande une livraison dans le dépôt, créer un commit local ciblé après les vérifications. Le commit local est le comportement par défaut, sauf instruction ou règle supérieure contraire. Si aucun dépôt ou identité Git n'est disponible, expliquer le blocage et conserver les livrables.
- Ne pas pousser, publier, créer un dépôt distant, ouvrir une PR ou envoyer un message à des tiers sans autorisation applicable ; si la demande autorise explicitement l'une de ces actions, suivre les règles du dépôt et vérifier son résultat. Ne jamais considérer le passage du temps comme une approbation.

## Entretien

Fournir un prompt ou une méthode de régénération : relire la skill et le corpus, qualifier les nouvelles sources, préserver les preuves précédentes, mettre à jour les références utiles, vérifier l'installation et réévaluer des scénarios. Expliquer clairement qu'un corpus peut évoluer et que les cas cités ne prouvent pas la qualité d'une future analyse. Une skill existante et son corpus ne doivent pas être écrasés par défaut.
