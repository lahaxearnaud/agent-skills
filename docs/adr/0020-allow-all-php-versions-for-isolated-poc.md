# ADR-0020: Autoriser toutes les versions de PHP pour les POC isolés

- **Statut :** Acceptée
- **Date :** 2026-11-06
- **Responsables de la décision :** Mainteneurs du dépôt

## Contexte

La liste intégrée définie par [ADR-0013](0013-configurable-docker-image-allowlist.md) limitait PHP à la branche 8 et excluait PHP 7. Les reproductions minimales peuvent nécessiter de représenter fidèlement le comportement d'une autre version, y compris PHP 7.

## Décision

Remplacer le motif intégré `docker.io/library/php:8.*` par `docker.io/library/php:*`, afin d'autoriser par défaut toutes les versions de PHP dans ce dépôt officiel. Cette décision remplace uniquement la restriction aux versions PHP 8 d'ADR-0013 ; le reste de cette ADR demeure applicable, notamment la liste utilisateur de remplacement, le registre et dépôt explicites, le tag concret autre que `latest`, le digest vérifié et l'usage d'une image déjà présente localement. Les contraintes d'isolation d'ADR-0012 restent applicables.

## Conséquences

Un POC peut utiliser la version PHP nécessaire sans modifier la liste d'autorisation. Un tag autorisé ne garantit ni l'existence ni la confiance de l'image : le runner vérifie toujours le digest dans le cache local et la disponibilité de l'environnement. Une liste utilisateur reste libre d'exclure certaines versions.
