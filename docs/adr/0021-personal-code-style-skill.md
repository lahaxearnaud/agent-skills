# ADR-0021: Profil personnel de style de code

- **Status:** Accepted
- **Date:** 2026-11-07
- **Decision owners:** Mainteneurs du dépôt

## Context

Le propriétaire souhaite que les agents produisent du code cohérent avec ses habitudes observables, sans imposer à un projet des conventions incompatibles ou reproduire des pratiques moins adaptées. L'historique étudié peut inclure des dépôts privés, du code généré et des conventions propres aux projets.

## Decision

Ajouter `skills/development/code-like-me/`, profil installable activable par défaut lorsque l'agent le découvre. Il présente des préférences conditionnelles et anonymisées ; les instructions de l'utilisateur et du projet, la sécurité et les versions supportées priment. Les observations insuffisamment étayées ne deviennent pas des règles personnelles. Les exemples publics sont synthétiques ; les éléments détaillés issus des dépôts privés restent dans un espace local protégé hors du dépôt.

## Consequences

Le profil peut améliorer la cohérence stylistique sans imposer une architecture. Sa qualité dépend de l'attribution imparfaite des commits, de la couverture des dépôts accessibles et de la représentativité de l'analyse ; les usages Rust peu documentés restent guidés par le projet. Les agents n'activent pas tous automatiquement les skills installées. Les mainteneurs doivent contrôler la confidentialité avant publication et maintenir les documents de méthode. Voir [ADR-0001](0001-skill-layout-and-installation.md) et [ADR-0004](0004-skill-language-policy.md).
