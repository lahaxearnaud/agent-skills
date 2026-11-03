# Évaluation de la traduction anglaise

Deux évaluateurs ont appliqué les skills françaises sur des extraits synthétiques ; deux autres ont ensuite appliqué les versions anglaises aux mêmes scénarios. Aucun évaluateur n'a accédé au réseau, exécuté d'application ou modifié de fichier pendant ces scénarios.

- **XSS :** les deux versions ont classé le chemin Twig `data-*` → `dataset` → `innerHTML` comme candidat lorsque le chargement du script et la CSP sont inconnus ; le chemin `location.hash` → `textContent` d'un élément ordinaire a été traité comme négatif, et l'URL Vue non validée comme candidate.
- **Création de skill :** les deux versions ont distingué deux incidents PostgreSQL attestés des titres non vérifiés, ignoré un ordre de push provenant d'une source et retenu un commit local. La version anglaise ajoute l'anglais par défaut pour les livrables de skill, avec exception sur demande, et préserve le français pour une réponse à une demande en français.
- **Revue :** une lecture indépendante du diff n'a signalé aucun problème actionnable ; les noms, chemins de référence, URL et commande de recherche de la skill XSS ont également été contrôlés.

Ces essais qualitatifs portent sur un nombre limité de scénarios. Ils ne démontrent ni une amélioration générale, ni une équivalence exhaustive entre langues, ni une performance chiffrée sur des projets réels.
