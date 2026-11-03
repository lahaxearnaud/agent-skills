# Maintenance de la skill XSS

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
