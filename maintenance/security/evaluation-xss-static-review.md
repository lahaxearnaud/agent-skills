# Évaluation initiale de xss-static-review

Évaluation sans exécution d'application, navigateur ni scanner actif.

- Deux scénarios de référence ont été soumis à un agent sans la skill : flux PHP → Twig `data-*` → `dataset` → `innerHTML` ; puis concaténation après assainissement, `:href` et script nonce. L'agent a correctement distingué les conditions et limites. Ils ne constituent donc pas une preuve que la skill améliore le rappel ou réduit les faux positifs par rapport à un agent sans skill.
- Un agent distinct a appliqué la skill aux mêmes familles d'extraits : il a distingué trois candidats, les conditions inconnues et `textContent` avec élément non identifié. L'évaluation a signalé une ambiguïté sur la preuve que le script client est chargé ; le texte a été précisé pour la lever.
- Une revue indépendante du dossier a identifié deux ambiguïtés : statut des consignes locales applicables et exclusions implicites de `rg`. Le texte a été corrigé sur ces deux points.
- Aucune mesure de rappel, précision, robustesse sur dépôts réels ou compatibilité effective avec les versions installées de Codex/OpenCode n'a été réalisée. La skill est un premier livrable à évaluer sur des projets et jeux de cas statiques représentatifs avant de lui attribuer une performance.
