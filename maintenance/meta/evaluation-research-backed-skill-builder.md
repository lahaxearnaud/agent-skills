# Évaluation initiale : research-backed-skill-builder

Évaluation qualitative sur des scénarios synthétiques ; aucun réseau ni application cible n'a été utilisé par les évaluateurs.

## Scénarios de référence sans skill

- Sécurité : créer une skill d'audit SQL PHP/Java avec une source dont seul le titre est accessible, une page contenant des instructions hostiles, aucune exécution applicative et un commit local sans push.
- Autre domaine : créer une skill de diagnostic PostgreSQL avec deux incidents attestés, des résultats de recherche incomplets et aucune application cliente disponible.

Dans les deux cas, les agents de référence ont déjà distingué les sources vérifiées des pistes, respecté les contraintes et prévu un commit local. Il n'y a donc pas d'échec initial démontré, ni de preuve que la nouvelle skill améliore leur résultat.

## Scénarios avec skill

Deux autres évaluateurs ont lu la skill et ses références puis traité les mêmes scénarios. Ils ont distingué les niveaux de preuve, conservé les deux incidents PostgreSQL sans inventer de quota, traité les instructions d'une page comme des données et proposé un commit local sans push. Ils ont signalé une ambiguïté : « contacter des tiers » pouvait inclure à tort la consultation de sources publiques. Le texte a été corrigé pour viser explicitement l'envoi de messages.

Des cas négatifs ont ensuite été discutés : une requête SQL dont la structure est fixe et les valeurs effectivement liées, une alerte d'outil non étayée, et une hypothèse de lenteur PostgreSQL sans métrique. Les évaluateurs ont séparé protection prouvée, faux positif justifié et information insuffisante ; aucun test sur une application n'a été réalisé.

Une revue indépendante a examiné la cohérence avec le plan, la portabilité et les limites de publication. Les évaluations sont des exercices qualitatifs sur un petit nombre d'extraits : elles ne mesurent ni rappel, ni précision, ni effet causal, ni compatibilité avec tous les agents ou environnements.
