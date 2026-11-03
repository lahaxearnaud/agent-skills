# Rapport statique et critères de preuve

## Classement des preuves

- **Flux établi statiquement** : l'acteur et la source contrôlable, les transformations et le puits sont reliés dans le code ; l'atteignabilité et les conditions sont justifiées par les éléments visibles, notamment le chargement du script client par la page et la liaison effective entre source et puits. Cela reste une conclusion statique, pas une exécution navigateur observée.
- **Candidat à confirmer par lecture** : puits ou chemin plausible mais source, liaison, protection, configuration ou portée manquante. Indiquer précisément quoi rechercher ; ne pas le présenter comme vulnérabilité confirmée.
- **Écarté avec raison** : constante, accès inatteignable, sortie texte ordinaire ou protection adaptée démontrée à ce contexte. Ne pas présenter comme fausse alerte si un maillon reste inconnu.

La présence d'une source et d'un puits dans le même fichier ne prouve pas leur liaison. Une analyse statique ne prouve pas un déclenchement, une exécution navigateur, un vol de données ou un contournement de CSP. Ne pas appeler « confirmé en exploitation » un résultat purement statique.

## Fiche de constat

Pour chaque constat pertinent, fournir :

1. **Titre et statut** : flux établi statiquement ou candidat ; gravité seulement si les éléments la justifient et en précisant les hypothèses.
2. **Source et acteur** : fichier:ligne, contrôle réellement prouvé ou supposé, droits nécessaires.
3. **Chemin** : fichier:ligne de chaque transformation et jonction inter-fichiers ; persistance et lecteur si applicable.
4. **Puits et contexte final** : fichier:ligne, HTML/attribut/URL/script/SVG/DOM, mécanisme et protection absente, mal adaptée ou inconnue.
5. **Portée** : réfléchie ou stockée si établi ; mécanisme DOM si applicable ; self/tiers/indéterminée séparément, rôle victime, interaction.
6. **Conditions et impact** : navigateur, origine, CSP/Trusted Types et cookies **si visibles**, comportement non établi et conséquences conditionnelles. Ne pas promettre RCE, vol de cookie ou prise de compte sans chaîne documentée.
7. **Correction** : choix concret au dernier puits, validation URL, assainissement contextualisé, isolation de document ou mise à jour, selon le cas. Ne pas affaiblir une CSP.
8. **Validation statique après correction** : quoi relire dans le code et quels chemins alternatifs doivent être inspectés. Ne pas proposer des tests d'application ou sondes runtime ; si l'incertitude ne peut être levée par le code disponible, la maintenir.

## Vue d'ensemble

À la fin, indiquer périmètre et fichiers effectivement examinés, technologie, contexte de configuration et dépendances disponibles, éventuels outils statiques réellement utilisés, surfaces non couvertes et limites. Si rien n'est démontré, écrire « aucun flux XSS établi dans le périmètre examiné » plutôt que « aucune XSS ». Grouper les occurrences d'une même cause commune tout en référençant chaque puits pertinent.

## Mini-grille de vérification

- Un lien vers `javascript:` échappé HTML : candidat si le schéma et le contrôle ne sont pas validés ; l'interaction est un prérequis possible.
- `v-html` sur constante de confiance : pas un flux XSS contrôlable sans autre preuve.
- `sanitize(x) + userInput` envoyé à `innerHTML` : la seconde partie n'est pas couverte ; retracer aussi l'acteur et l'accès à la page.
- Texte depuis `location.hash` vers `textContent` d'un élément ordinaire : ne pas signaler comme injection HTML, tant qu'aucune réutilisation dangereuse n'est démontrée.
- Réflexion d'un marqueur dans du texte encodé : pas une preuve d'exécution.
- Valeur issue d'un script nonce ou d'une page avec CSP inconnue : ne pas conclure que la CSP bloque ou autorise le vecteur sans la politique effective.
- Une valeur éditable uniquement par son propriétaire : la qualifier self ou portée inconnue seulement après avoir cherché partage, lecteurs privilégiés, import et écriture par un tiers ; ne pas supposer une chaîne CSRF.
