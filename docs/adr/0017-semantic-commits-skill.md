# ADR-0017: Skill de rédaction des commits sémantiques

- **Status:** Accepted
- **Date:** 2026-11-05
- **Decision owners:** Mainteneurs du dépôt

## Context

Les messages de commit peuvent alimenter semantic-release, dont le résultat dépend du parseur, des règles et de la configuration du projet. Un agent doit décrire fidèlement les modifications et signaler les incompatibilités sans supposer que toutes les installations interprètent les mêmes conventions.

## Decision

Créer le domaine `skills/development/` et la skill installable `semantic-commits`. Elle guide l'inspection des changements et de la configuration effective, la rédaction de messages structurés, les indications de rupture et la vérification avant commit. Elle fournit des références attribuées consultables hors ligne. Elle respecte les autorisations Git du projet et ne configure pas semantic-release à la place de l'utilisateur.

## Consequences

Les mainteneurs doivent tenir à jour les exemples et les résumés des sources. Les prévisions de version restent conditionnelles aux règles, branches et plugins réellement configurés ; la syntaxe seule ne garantit pas une publication. Voir [ADR-0001](0001-skill-layout-and-installation.md) et [ADR-0009](0009-offline-skill-references.md).
