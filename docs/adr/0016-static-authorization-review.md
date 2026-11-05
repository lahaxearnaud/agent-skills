# ADR-0016: Revue statique des autorisations Web

- **Status:** Accepted
- **Date:** 2026-11-05
- **Decision owners:** Mainteneurs du dépôt

## Context

Les erreurs d'autorisation peuvent affecter les actions, les objets, les frontières entre organisations ou les propriétés accessibles. Une revue de code doit relier l'identité, l'opération et la ressource aux contrôles effectifs, sans conclure à une exploitation sur la seule présence d'un identifiant ou d'une interface non protégée.

## Decision

Ajouter la skill installable `authorization-static-review` et le corpus `corpus/security/authorization/`. La revue est source-only : elle examine les routes, configurations, politiques, requêtes et contrôles serveur, y compris PHP/Symfony et les limites des contrôles Vue côté client, sans lancer l'application ni sonder une cible. Elle distingue chemin établi statiquement, candidat et absence de conclusion pour le chemin examiné. Les références nécessaires sont fournies dans le package pour un usage hors ligne ; la consultation de sources primaires reste facultative pour résoudre une incertitude matérielle.

Le corpus conserve les avis consultés, les limites et les pistes non vérifiées séparément. Les scénarios synthétiques ne constituent pas des incidents publiés. Les analyses ne présument pas de l'exploitation effective ni d'une couverture exhaustive.

## Consequences

Les mainteneurs doivent garder la skill, les résumés attribués, le corpus, les évaluations et le catalogue cohérents. L'analyse dépend du code et de la configuration disponibles ; les services d'identité externes et les configurations de déploiement absentes peuvent laisser une conclusion incertaine. Voir [ADR-0002](0002-corpus-evidence-and-provenance.md) et [ADR-0009](0009-offline-skill-references.md).
