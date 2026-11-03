# Organiser un corpus réutilisable

Adapter aux conventions du dépôt ; à défaut, utiliser `corpus/<domaine>/<sujet>/` pour le corpus et `maintenance/<domaine>/` pour sa méthode d'entretien. Éviter les chemins absolus dans les livrables. Le corpus reste disponible aux mainteneurs mais la skill installée doit embarquer les références nécessaires à son usage, sauf demande contraire.

## Structure minimale

- Un index ou README indique sujet, date, périmètre, méthode de recherche, nombre d'entrées par statut, sources, doublons possibles, exclusions, lacunes et liens relatifs vers les fichiers de détail.
- Des fiches ou lignes structurées regroupent les cas et exemples ; utiliser Markdown, CSV ou JSON selon les besoins. Une collection de titres identifie des pistes, pas un ensemble d'analyses confirmées.
- Une section décrit les technologies et mécanismes récurrents, protections ou pratiques et leurs limites ; lier les conclusions aux sources ou marquer les inférences.
- Un plan de maintenance explique comment enrichir le corpus, vérifier les sources, retrouver les changements liés à la skill et préserver les données préexistantes.

## Champs d'une fiche

Renseigner lorsque c'est pertinent : `id`, `titre`, `categorie`, `source_url`, `auteur`, `date_publication`, `date_consultation`, `nature_source`, `statut_verification`, `technologie`, `versions`, `acteurs`, `conditions`, `entree`, `transformations`, `destination`, `mecanisme`, `impact_attribue`, `correction`, `preuve`, `limites` et `relations_doublons`. Les valeurs non connues restent explicitement inconnues ; ne pas inventer de schéma complet lorsqu'un champ est sans objet.

Pour la sécurité, distinguer vulnérabilité, prérequis, acteurs, surfaces, exploitation observée ou alléguée, impact conditionnel, protection et limites ; si des attaques ou outils sont documentés, ajouter contexte et portée des résultats. Pour les autres domaines, adapter ces champs aux symptômes, conditions, effets, diagnostics et correctifs.

## Mettre à jour un corpus existant

Lire les index et conventions, conserver le contenu et les sources ; ajouter ou corriger de façon traçable. Dédupliquer par identifiant, indiquer les entrées liées et la possibilité de doublons non établis. Garder les scénarios hypothétiques, les labs et les incidents indépendants clairement séparés. Une correction doit expliciter son origine et ne pas effacer silencieusement des informations antérieures ou des limitations.
