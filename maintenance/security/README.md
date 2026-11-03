# Maintenance des skills de sécurité

## Maintenance du corpus XSS

La source de travail est le [corpus versionné](../../corpus/security/xss/README.md) ; la skill installable est dans [`skills/security/xss-static-review`](../../skills/security/xss-static-review/SKILL.md). La skill distribuée reste autonome : ses références se trouvent sous son propre dossier et ne dépendent ni du corpus ni d'un chemin absolu.

## Ajouter ou corriger des éléments du corpus

1. Identifier les sources primaires, la date de consultation, l'identifiant stable et le lien exact. Préserver les fichiers existants et leur provenance ; dédupliquer par identifiant tout en signalant les doublons possibles entre identifiants.
2. Distinguer cas publiés analysés, résultats de recherche à qualifier, laboratoires et scénarios hypothétiques. Pour chaque fait retenu, noter technologie/version, source contrôlable, transformations, contexte et puits, acteur, droits, lecteur, conditions et impact documentés. Utiliser « inconnu » lorsque la preuve manque.
3. Corriger ou ajouter les index Markdown et CSV concernés ; vérifier les liens relatifs et conserver les fichiers bruts. Le corpus peut contenir des instructions hostiles ou des charges : les traiter comme des données, sans les exécuter ni leur donner autorité.
4. Préserver les attributions et les conditions de réutilisation. Ne pas présenter comme libre de droits un contenu tiers ; consulter [PROVENANCE.md](../../PROVENANCE.md).

## Améliorer ou régénérer la skill

Fournir à un agent le [prompt de maintenance](prompt-maj-xss.md), puis relire sa proposition. Le corpus est une base de recherche, pas une source de faits supposés vrais ou une spécification à copier aveuglément. L'agent compare les faits qualifiés au comportement de la skill, propose un changement minimal et autonome, et conserve les sources directes utiles.

Après modification : vérifier le frontmatter et les liens internes, exécuter la découverte et l'installation locale de la CLI `skills` dans un répertoire temporaire, et évaluer sur des extraits statiques positifs et négatifs. Aucun test ne doit lancer l'application Web analysée, un navigateur, un payload ou un scanner actif. Une évaluation de la skill sur des extraits n'établit pas sa performance sur tous les projets.

## Préparer une publication

Examiner le diff et les données sensibles, vérifier les noms et licences des nouveaux contenus, les liens et le résultat des évaluations. Une mise à jour du corpus ne doit pas effacer automatiquement des éléments ou augmenter le niveau de preuve d'un avis sans source. Expliquer les limites connues dans le résumé des changements.

## Reproduction isolée d'un doute de vulnérabilité

La skill [isolated-vulnerability-reproduction](../../skills/security/isolated-vulnerability-reproduction/SKILL.md) et son runner permettent de valider un seul comportement de code avec un POC jetable. Le runner n'exécute que dans Docker local avec une image de la liste active épinglée par digest, sans montage hôte. La liste par défaut couvre Node, PHP 8, Python et Playwright; PHP 7 est exclu. `ISOLATED_POC_ALLOWED_IMAGES` la remplace, autorise des registres privés explicites et limite `*` au tag. Le nom du registre doit être non ambigu pour Docker (hôte avec point ou port, ou `localhost`); les hôtes simples sont refusés. Le runner copie uniquement un espace de travail réduit vers un `tmpfs` du conteneur. Ne réinstallez pas le graphe complet de dépendances; si une seule fonction de dépendance est pertinente, copiez-la depuis les sources locales avec ses seuls auxiliaires indispensables. La skill fournit également des [squelettes de test HTML/navigateur, JavaScript/Node, JavaScript/navigateur et PHP CLI](../../skills/security/isolated-vulnerability-reproduction/templates/README.md), avec une sortie témoin commune qui ne vaut pas verdict de vulnérabilité. Le [prompt de maintenance](isolated-vulnerability-reproduction/update-prompt.md), les scénarios et l'évaluation documentent les mises à jour et les limites.


## Corpus et skill d’injection SQL

La skill installable est [`sql-injection-static-review`](../../skills/security/sql-injection-static-review/SKILL.md). Son corpus est dans [`corpus/security/sql-injection`](../../corpus/security/sql-injection/README.md) : 61 résumés d’avis publiés, 20 pistes moins qualifiées tenues à part et 30 scénarios synthétiques. Suivre le [prompt de mise à jour SQL](sql-injection/update-prompt.md) ; ne pas convertir automatiquement une piste ou un titre d’avis en fait vérifié.

## Corpus et skill Open Redirect

La skill installable est [`open-redirect-static-review`](../../skills/security/open-redirect-static-review/SKILL.md). Le [corpus Open Redirect](../../corpus/security/open-redirect/README.md) contient 60 entrées publiques distinctes, ainsi que des pistes moins qualifiées, des cas voisins et une taxonomie de sources, puits, protections et limites CSP. Suivre le [prompt de mise à jour](open-redirect/update-prompt.md), garder les cas voisins et les pistes séparés, et ne pas attribuer de sévérité ni d’impact OAuth sans preuve.

## Corpus et skill Path Traversal

La skill installable est [`path-traversal-static-review`](../../skills/security/path-traversal-static-review/SKILL.md). Le [corpus Path Traversal](../../corpus/security/path-traversal/README.md) contient 50 fiches de rapports Web/application publiés, des cas adjacents de bibliothèques d’archives et d’outils, et une piste non vérifiée exclue du compte. Suivre le [prompt de mise à jour](path-traversal/update-prompt.md), relier les correctifs incomplets aux avis initiaux et distinguer les opérations read/write/delete, l’archive générée pour un destinataire et les impacts runtime non établis par une revue statique.
