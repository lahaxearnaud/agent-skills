# ADR-0019: Revue statique des téléversements de fichiers

- **Status:** Accepted
- **Date:** 2026-11-05
- **Decision owners:** Mainteneurs du dépôt

## Context

Les fichiers téléversés et leurs métadonnées peuvent traverser plusieurs validations, stockages et traitements avant d'être servis ou interprétés. Les conséquences dépendent notamment des permissions, des processeurs et de la configuration du serveur, qui ne figurent pas toujours dans le code examiné.

## Decision

Ajouter la skill installable `file-upload-static-review` et un corpus d'au moins trente avis publics. La skill suit les octets et métadonnées depuis l'entrée jusqu'au stockage, aux traitements et à la restitution. Elle distingue les chemins établis, les candidats et les contrôles démontrés, et reste source-only sans téléversement ni exécution de l'application. Ses références attribuées sont incluses pour une utilisation hors ligne.

## Consequences

Les mainteneurs doivent garder les sources, limites et références à jour. Un fichier accepté ou un stockage public ne démontre pas à lui seul l'exécution serveur ou une XSS ; les configurations absentes restent des inconnues. Les recoupements avec XSS, path traversal et RCE doivent rester explicités. Voir [ADR-0002](0002-corpus-evidence-and-provenance.md) et [ADR-0009](0009-offline-skill-references.md).
