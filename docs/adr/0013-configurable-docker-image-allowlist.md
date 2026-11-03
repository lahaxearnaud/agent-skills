# ADR-0013: Liste d'autorisation configurable des images Docker

- **Statut :** Acceptée
- **Date :** 2026-11-03
- **Responsables de la décision :** Mainteneurs du dépôt

## Contexte

La skill de reproduction isolée doit permettre des PoC jetables dans des environnements et langages différents, tout en empêchant l'agent de lancer une image Docker arbitraire. La restriction précédente aux dépôts officiels était trop large pour être une liste finie et ne permettait pas l'usage explicite d'un registre privé.

## Décision

Le runner utilise une liste intégrée limitée à ces dépôts, avec tout tag concret sauf `latest` :

- `docker.io/library/node:*`
- `docker.io/library/php:8.*`
- `docker.io/library/python:*`
- `mcr.microsoft.com/playwright:*`

La version PHP 7 n'est pas autorisée par la liste intégrée. La variable d'environnement `ISOLATED_POC_ALLOWED_IMAGES`, si elle est définie, remplace entièrement cette liste. Elle contient une liste séparée par des virgules. Chaque entrée nomme exactement le registre et le chemin du dépôt; le registre doit être non ambigu pour Docker (hôte avec point, hôte avec port ou `localhost`), car un hôte simple tel que `registry/team/php` peut être interprété comme un espace de noms Docker Hub. Le seul joker autorisé est `*` dans le tag, par exemple `registry.example.test/security/php:8.*`. Une valeur vide ou mal formée bloque la validation. Cette règle permet d'autoriser explicitement des images de registres privés sans republier la skill à chaque nouvelle version de tag.

Le manifeste doit conserver une référence complète et concrète `registre/namespace/image:tag@sha256:<digest>`. Le runner compare la partie `registre/namespace/image:tag` à la liste active, refuse `latest`, exige que l'image soit déjà présente localement et vérifie le digest avant de la lancer. La variable d'autorisation est lue par le runner hôte et n'est pas transmise au conteneur.

Cette décision remplace uniquement la restriction de provenance des images définie par [ADR-0012](0012-isolated-poc-reproduction.md). Ses autres limites restent en vigueur : Docker local Linux, aucune connexion réseau du conteneur, aucun montage hôte, ressources bornées et aucun lancement du projet audité.

## Conséquences

Les versions futures d'un même dépôt peuvent être permises par un motif de tag sans mise à jour de la skill. Un utilisateur peut sélectionner des registres et dépôts privés, mais leur ajout constitue une décision de confiance explicite. Un motif large tel que `repo:*` autorise toutes les versions correspondant à ce dépôt; le digest vérifié identifie le contenu effectivement exécuté sans rendre ce contenu digne de confiance par lui-même. Les motifs globaux sur le registre ou le nom du dépôt restent interdits.
