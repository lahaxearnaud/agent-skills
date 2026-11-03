# ADR-0012: Reproduction isolée et minimale de vulnérabilités

- **Statut :** Acceptée
- **Date :** 2026-11-03
- **Responsables de la décision :** Mainteneurs du dépôt

## Contexte

Les skills de revue de sécurité du dépôt analysent le code sans exécuter l'application. Une revue peut cependant identifier un doute précis dont la validation par un très petit POC local réduirait l'incertitude. Exécuter le projet complet, restaurer toutes ses dépendances ou monter le dépôt dans un conteneur élargirait inutilement la surface et le coût d'une expérience qui doit rester jetable.

## Décision

Ajouter une skill installable distincte, `isolated-vulnerability-reproduction`, destinée à reproduire une hypothèse de vulnérabilité issue d'une revue de code, pour toute famille de vulnérabilités, uniquement dans un harnais local minimal.

Le POC doit conserver seulement le code qui détermine le comportement observé, les auxiliaires indispensables et des données synthétiques. Il ne faut jamais restaurer ou réinstaller le graphe complet de dépendances du projet. Si une fonction d'une dépendance est la seule partie pertinente et que son code source local est disponible, l'agent peut copier cette fonction exacte et seulement ses auxiliaires indispensables, en consignant son origine et sa version.

L'exécution est limitée à un moteur Docker local Linux et à une image officielle préalablement récupérée, explicitement approuvée et épinglée par digest. Aucun runtime hôte, endpoint réel, application complète, scanner actif, réseau sortant ou effet persistant n'est permis. Le runner refuse les chemins non temporaires, les secrets, les symlinks, les arbres de dépendances volumineux et les manifestes qui modifieraient le profil de sécurité. Il ne monte aucun chemin hôte : il transmet une archive vérifiée du petit espace de travail par entrée standard et l'extrait dans un `tmpfs` du conteneur éphémère. Les limites de temps, ressources et sortie restent fixes.

Les résultats distinguent reproduction positive, non-reproduction dans les conditions testées et blocage ou impossibilité de reproduire sans risque. Une absence de marqueur n'est jamais une preuve d'absence de vulnérabilité. Une évaluation statique et les règles source-only des autres skills restent distinctes de cette reproduction, conformément à [ADR-0003](0003-static-security-review-scope.md).

## Conséquences

Les agents peuvent vérifier rapidement une fonction ciblée sans lancer le projet ni créer un environnement applicatif complet. La reproduction peut néanmoins omettre l'appelant, la configuration, l'état de la dépendance ou le comportement d'intégration; chaque résultat doit donc énoncer ces limites. Copier une fonction depuis sa dépendance peut aussi perdre un comportement de packaging ou d'état implicite; si les auxiliaires nécessaires ne peuvent pas être isolés fidèlement, le résultat reste non reproductible.

Le runner requiert un hôte POSIX pour construire son archive à travers des descripteurs de répertoire sans suivre les symlinks. Un conteneur partage le noyau Linux du moteur Docker; les restrictions réduisent l'exposition sans promettre un confinement parfait. Le runner refuse les preuves qui nécessiteraient un effet hôte, une évasion ou un affaiblissement des restrictions. Cette skill est séparée des skills de revue statique : elle ne change pas leur périmètre.
