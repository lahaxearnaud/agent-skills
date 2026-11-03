# ADR-0014: Squelettes de tests pour les POC isolés

- **Statut :** Acceptée
- **Date :** 2026-11-03
- **Responsables de la décision :** Mainteneurs du dépôt

## Contexte

La skill de reproduction isolée demande un POC rapide, minimal et jetable, mais un agent doit encore choisir seul la structure des cas témoin/déclencheur et la forme des résultats. Des exemples cohérents réduisent ce travail et facilitent la lecture des observations. Les langages et surfaces d'exécution ont cependant des comportements différents : une page HTML statique, du JavaScript sous Node, du JavaScript navigateur et du PHP CLI ne partagent pas le même environnement.

## Décision

La skill installable contient un dossier `templates/` avec quatre squelettes : `html-browser`, `javascript-node`, `javascript-browser` et `php-cli`. Les deux squelettes navigateur partagent un helper Chromium local documenté dans `templates/browser/`. Ils s'exécutent uniquement via le runner Docker existant, sur des fichiers locaux, avec le profil réseau et de sécurité inchangé. Le helper conserve le bac à sable Chromium par défaut; si celui-ci ne fonctionne pas sous le profil fixe, le résultat est bloqué et l'agent ne doit pas ajouter `--no-sandbox` ni affaiblir le conteneur.

Chaque exemple fournit un contrôle et un déclencheur synthétiques et émet deux lignes JSON `ISOLATED_POC_CASE=`, dans cet ordre, avec les identifiants `control` puis `trigger`. Une ligne `ISOLATED_POC_TEMPLATE_SMOKE=` signale que le squelette a fonctionné. Les exemples utilisent des placeholders sans vulnérabilité et ne constituent jamais une preuve sur le code audité. L'agent choisit le squelette selon le runtime et le comportement pertinent, remplace le placeholder par le code exact réduit et ses seuls auxiliaires indispensables, puis documente les observations, la provenance et les limites. Si aucun exemple ne reproduit fidèlement le comportement, il crée un harnais personnalisé plus petit plutôt que d'ajouter des dépendances applicatives.

Le squelette HTML observe uniquement le DOM résultant du parsing d'un fichier local; il ne reproduit pas le rendu Twig/PHP, les routes HTTP, les en-têtes ni la portée applicative. Les squelettes de navigateur ne naviguent jamais vers une cible distante.

## Conséquences

Les quatre environnements disposent d'un format de résultat prévisible et installable hors ligne avec la skill. Les images d'exemple sont épinglées par tag et digest et restent soumises à la liste active de l'utilisateur. Les images navigateur sont volumineuses et le profil fixe peut empêcher leur démarrage; ces cas restent des résultats bloqués, pas des résultats négatifs. Les scénarios spécifiques à un framework ne sont ajoutés que si un comportement de framework change matériellement le test sans réinstaller ses dépendances.
