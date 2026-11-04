# ADR-0015: Skill de rédaction des tests avec la pyramide

- **Status:** Accepted
- **Date:** 2026-11-04
- **Decision owners:** Mainteneurs du dépôt

## Context

Le dépôt publie des skills réutilisables pour agents de code. Une méthode cohérente de rédaction des tests doit aider les agents à choisir un niveau proportionné, éviter une suite dominée par des tests E2E lents et fragiles, et utiliser le test-first lorsque la tâche s'y prête. La skill doit rester autonome et installable avec la CLI `skills`.

## Decision

Créer `skills/testing/test-pyramid/` comme skill du domaine `testing`, installable sous le nom `test-pyramid`. Elle définit une méthode fonctionnelle et de non-régression fondée sur la pyramide : tester une règle au niveau unitaire, les contrats UI au niveau composant, les collaborations réelles au niveau intégration/fonctionnel, et réserver l'E2E à quelques parcours dont la composition apporte une confiance distincte.

La pyramide est une règle de répartition et de choix du niveau le plus bas fidèle, sans ratio chiffré ni quota de couverture. La skill recommande le test-first par défaut, vérifie que le premier échec vient du comportement attendu et prévoit les tests de caractérisation ou les tâches de couverture seule. Elle utilise les frameworks et commandes existants et n'impose pas de nouvelle dépendance.

Le package contient des résumés attribués des sources officielles pour l'usage hors ligne, un guide de sélection et des exemples PHP/Symfony, JavaScript, Vue et navigateur. Des scénarios synthétiques et un bilan d'évaluation sont conservés dans `maintenance/testing/`; ils ne constituent pas un corpus de vulnérabilités.

## Consequences

Les agents disposent d'une méthode et d'exemples consultables hors ligne. Le dépôt doit maintenir les résumés de sources, les scénarios d'évaluation, les liens d'installation et l'index d'ADR lorsque la skill évolue. L'évaluation initiale reste qualitative : les scénarios de base choisissaient déjà des couches adaptées, et une comparaison répétée avec la skill reste à effectuer. La skill ne prescrit pas de méthode aux tests de performance, de charge, d'accessibilité ou de sécurité.

Voir aussi [ADR-0001](0001-skill-layout-and-installation.md) sur le packaging des skills et [ADR-0009](0009-offline-skill-references.md) sur les références locales.
