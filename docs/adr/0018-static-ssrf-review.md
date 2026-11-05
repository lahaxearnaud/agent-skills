# ADR-0018: Revue statique des SSRF Web

- **Status:** Accepted
- **Date:** 2026-11-05
- **Decision owners:** Mainteneurs du dépôt

## Context

Une application Web peut déclencher des requêtes serveur à partir d'URL ou de configurations contrôlées par un acteur. L'analyse doit tenir compte des clients, des redirections, de la résolution DNS et des frontières réseau sans présumer que le code contient toute la configuration de déploiement.

## Decision

Ajouter la skill installable `ssrf-static-review` et un corpus d'au moins vingt avis publics documentés. La skill suit les données jusqu'aux opérations réseau côté serveur, directes ou indirectes, et distingue flux établi statiquement, candidat et absence de conclusion sur le chemin examiné. Elle ne lance ni application ni sondes. Elle fournit des références attribuées utilisables hors ligne et n'impose pas d'accès Internet pour la revue.

## Consequences

Les mainteneurs doivent préserver la provenance, les limites et les versions des sources et mettre à jour les références locales. Une requête serveur contrôlable ne démontre pas à elle seule l'accès à un service interne, la lecture d'une réponse ou l'exploitation. Voir [ADR-0002](0002-corpus-evidence-and-provenance.md) et [ADR-0009](0009-offline-skill-references.md).
