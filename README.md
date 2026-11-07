# Agent Skills

Un catalogue de skills pour agents de code, organisé par domaine. Il comprend des skills de revue statique XSS, injection SQL, Open Redirect, Path Traversal et RCE, une skill de rédaction d’ADR, une skill de rédaction des tests selon la pyramide et une méthode pour construire des skills fondées sur un corpus.

Les agents de code doivent commencer par lire le [guide du dépôt](AGENTS.md), qui décrit son organisation et référence les décisions d’architecture sous [`docs/adr/`](docs/adr/). Claude Code charge les mêmes consignes via [`CLAUDE.md`](CLAUDE.md).

## Installation

Avec Node.js et npm installés, utiliser la CLI open source [`skills`](https://github.com/vercel-labs/skills) :

```bash
# Voir les skills proposées par ce dépôt, sans installation
npx skills add lahaxearnaud/agent-skills --list

# Installer la skill dans le projet courant et choisir l'agent
npx skills add lahaxearnaud/agent-skills --skill xss-static-review

# Installer pour Codex et OpenCode, sans interaction
npx skills add lahaxearnaud/agent-skills --skill xss-static-review --agent codex opencode --yes

# Installer la revue statique SQL dans le projet courant
npx skills add lahaxearnaud/agent-skills --skill sql-injection-static-review --agent codex opencode --yes

# Installer le profil personnel de code pour son utilisateur
npx skills add lahaxearnaud/agent-skills --skill code-like-me --agent codex opencode --global --yes

# Installer la skill de rédaction des commits sémantiques
npx skills add lahaxearnaud/agent-skills --skill semantic-commits --agent codex opencode --yes

# Installer la skill de rédaction et d'indexation des ADR
npx skills add lahaxearnaud/agent-skills --skill adr-authoring --agent codex opencode --yes

# Installer la skill de rédaction des tests selon la pyramide
npx skills add lahaxearnaud/agent-skills --skill test-pyramid --agent codex opencode --yes

# Installer la revue statique des fichiers téléversés
npx skills add lahaxearnaud/agent-skills --skill file-upload-static-review --agent codex opencode --yes

# Installer la revue statique SSRF
npx skills add lahaxearnaud/agent-skills --skill ssrf-static-review --agent codex opencode --yes

# Installer la revue statique des autorisations
npx skills add lahaxearnaud/agent-skills --skill authorization-static-review --agent codex opencode --yes

# Installer la revue statique des Open Redirect
npx skills add lahaxearnaud/agent-skills --skill open-redirect-static-review --agent codex opencode --yes

# Installer la revue statique du Path Traversal
npx skills add lahaxearnaud/agent-skills --skill path-traversal-static-review --agent codex opencode --yes

# Installer la revue statique des RCE
npx skills add lahaxearnaud/agent-skills --skill rce-static-review --agent codex opencode --yes

# Installer pour son utilisateur plutôt que pour le projet courant
npx skills add lahaxearnaud/agent-skills --skill xss-static-review --global

# Installer la reproduction isolée de PoC jetables
npx skills add lahaxearnaud/agent-skills --skill isolated-vulnerability-reproduction --agent codex opencode --yes
```

La commande est **`npx skills add`** : elle exécute la CLI `skills` et installe des fichiers de skill, pas une dépendance npm de l'application auditée. La prise en charge d'un agent et ses chemins d'installation dépendent de la version de la CLI et de l'agent ; consulter leur documentation. Chaque skill installe ses propres références avec elle ; la revue XSS ne nécessite pas le corpus au moment de l’audit.

### Utilisation hors ligne

Les références documentaires utiles à l'analyse sont synthétisées dans chaque package et permettent une revue hors ligne. L'agent commence par ces notes; s'il a accès à une source primaire, il peut la consulter lorsqu'une nuance absente sur une version, une configuration, un comportement ou un impact change matériellement l'analyse. Cette consultation n'est jamais requise. Aucun code privé, secret ou donnée utilisateur ne doit être transmis à un service externe; sans accès à la source, l'agent indique l'incertitude. Pour une machine sans accès général à Internet, transférer à l'avance le dépôt ou le dossier complet de la skill, puis l'installer depuis cette copie locale avec une CLI déjà disponible, ou copier le dossier complet vers le répertoire de skills reconnu par l'agent. Les commandes ci-dessus qui installent depuis GitHub ou téléchargent `npx` nécessitent une connexion lors de l'installation.

## Catalogue

| Domaine | Skill | Utilisation |
|---|---|---|
| Security | [xss-static-review](skills/security/xss-static-review/SKILL.md) | Revue statique de XSS Web : PHP, Symfony, Twig, JavaScript, Vue et autres technologies. |
| Security | [sql-injection-static-review](skills/security/sql-injection-static-review/SKILL.md) | Revue statique des injections SQL : PHP, Doctrine et autres technologies Web. |
| Security | [file-upload-static-review](skills/security/file-upload-static-review/SKILL.md) | Revue statique des fichiers téléversés : validation, stockage, traitement et restitution. |
| Security | [ssrf-static-review](skills/security/ssrf-static-review/SKILL.md) | Revue statique des requêtes serveur influençables, des redirections, du DNS et des politiques de destination. |
| Security | [authorization-static-review](skills/security/authorization-static-review/SKILL.md) | Revue statique des autorisations fonctionnelles, objets, tenants et propriétés, notamment PHP/Symfony et Vue. |
| Security | [open-redirect-static-review](skills/security/open-redirect-static-review/SKILL.md) | Revue statique des redirects serveur et navigations JavaScript externes : PHP, Symfony, JavaScript, Vue, OAuth et autres technologies Web. |
| Security | [path-traversal-static-review](skills/security/path-traversal-static-review/SKILL.md) | Revue statique des traversées de chemins fichier : lectures/écritures/suppressions, fichiers statiques, templates, archives Zip Slip et symlinks. |
| Security | [rce-static-review](skills/security/rce-static-review/SKILL.md) | Revue statique des chemins RCE à partir du code : processus/commandes, évaluation dynamique, templates, désérialisation, chargement et chaînes différées. |
| Security | [isolated-vulnerability-reproduction](skills/security/isolated-vulnerability-reproduction/SKILL.md) | Reproduction jetable minimale dans Docker local; liste d'images par défaut ou remplaçable par l'utilisateur, tag optionnellement filtré par motif et digest obligatoire. |
| Development | [code-like-me](skills/development/code-like-me/SKILL.md) | Profil personnel anonymisé de rédaction du code, adaptable aux conventions du projet. |
| Development | [semantic-commits](skills/development/semantic-commits/SKILL.md) | Rédige des commits conventionnels adaptés au parseur et aux règles semantic-release du projet. |
| Documentation | [adr-authoring](skills/documentation/adr-authoring/SKILL.md) | Rédige, met à jour et indexe les ADR en respectant les conventions du dépôt. |
| Testing | [test-pyramid](skills/testing/test-pyramid/SKILL.md) | Écrit des tests fonctionnels et de non-régression en choisissant le niveau le plus bas fidèle, sans ratio imposé. |
| Meta | [research-backed-skill-builder](skills/meta/research-backed-skill-builder/SKILL.md) | Création de skills documentées à partir de sources et de corpus traçables. |

Exemple : « Utilise `xss-static-review` pour examiner les sources de ce dépôt et identifier les flux XSS potentiels. » La skill XSS interdit de lancer l'application, un navigateur, des payloads ou un scanner actif. La skill `open-redirect-static-review` suit séparément les réponses `Location` et les navigations JavaScript automatiques, en distinguant les liens cliquables et les cas incomplets. La skill `rce-static-review` reste également source-only et vérifie les chemins réseau vers les frontières d'exécution sans lancer l'application ni des scanners.

`isolated-vulnerability-reproduction` est une skill séparée, activée uniquement quand une revue a déjà identifié un doute précis et qu'une preuve minimale est faisable. Elle interdit les cibles réelles, l'exécution sur l'hôte, les montages de chemins hôte et la réinstallation du graphe de dépendances. Quand seule une fonction d'une dépendance est nécessaire, elle demande de copier cette fonction et ses seuls auxiliaires indispensables depuis les sources locales. Le runner transfère le petit espace de travail vers un `tmpfs` interne à un conteneur éphémère. Il autorise par défaut Node, toutes les versions de PHP, Python et Playwright dans les dépôts listés. `ISOLATED_POC_ALLOWED_IMAGES` remplace cette liste et accepte des références registre/dépôt exactes avec `*` uniquement dans le tag. Les hôtes ambigus à un seul label sont refusés pour éviter une résolution implicite vers Docker Hub. La skill inclut des [squelettes reproductibles](skills/security/isolated-vulnerability-reproduction/templates/README.md) pour HTML/navigateur, JavaScript avec Node, JavaScript dans un navigateur et PHP CLI; leur sortie témoin confirme le harnais uniquement, pas une vulnérabilité.

## Corpus et maintenance

- [Profil code-like-me](skills/development/code-like-me/SKILL.md) : [notes de méthode et limites](skills/development/code-like-me/references/profile.md), [prompt de maintenance](maintenance/development/code-like-me/update-prompt.md) et [scénarios comparatifs](maintenance/development/code-like-me/evaluation.md). Les preuves détaillées issues des dépôts privés restent locales et ne sont pas publiées.

- [Corpus de téléversement](corpus/security/file-upload/README.md) : 34 avis consultés ; voir le [prompt de maintenance](maintenance/security/file-upload-static-review/update-prompt.md) et les [scénarios synthétiques](maintenance/security/file-upload-static-review/evaluation.md).

- [Corpus SSRF](corpus/security/ssrf/README.md) : 24 avis consultés, avec conditions, mécanismes et limites ; voir le [prompt de maintenance](maintenance/security/ssrf-static-review/update-prompt.md) et les [scénarios synthétiques](maintenance/security/ssrf-static-review/evaluation.md).

- [Skill semantic-commits](skills/development/semantic-commits/SKILL.md) : [prompt de maintenance](maintenance/development/semantic-commits/update-prompt.md) et [scénarios d’évaluation](maintenance/development/semantic-commits/evaluation.md).

- [Corpus des autorisations](corpus/security/authorization/README.md) : 60 avis et enregistrements consultés, avec extraits attribués et pistes non vérifiées séparées ; voir le [prompt de maintenance](maintenance/security/authorization-static-review/update-prompt.md) les [scénarios synthétiques](maintenance/security/authorization-static-review/evaluation-scenarios.md) et le [bilan d’évaluation](maintenance/security/authorization-static-review/evaluation.md).

- [Corpus injection SQL](corpus/security/sql-injection/README.md) : 61 résumés de rapports publiés, 20 pistes à qualifier et 30 scénarios synthétiques ; voir aussi le [prompt de maintenance SQL](maintenance/security/sql-injection/update-prompt.md) et l’[évaluation SQL](maintenance/security/sql-injection/evaluation.md).
- [Corpus Open Redirect](corpus/security/open-redirect/README.md) : 60 fiches de CVE/avis publics dédupliquées, avec conditions, technologies, flux, impacts, protections, normes et limites ; des pistes et cas XSS/navigation adjacents sont classés à part. Voir le [prompt de mise à jour](maintenance/security/open-redirect/update-prompt.md) et l’[évaluation de la skill](maintenance/security/open-redirect-static-review/evaluation.md).
- [Corpus Path Traversal](corpus/security/path-traversal/README.md) : 50 cas publiés Web/application, plus des cas adjacents d’archives/outils et un avis non vérifié tenu à part. Les fiches distinguent les préconditions, les types d’opérations, les correctifs incomplets, les symlinks et les impacts côté serveur ou destinataire. Voir le [prompt de mise à jour](maintenance/security/path-traversal/update-prompt.md) et l’[évaluation](maintenance/security/path-traversal-static-review/evaluation.md).
- [Corpus RCE](corpus/security/remote-code-execution/README.md) : 55 cas source-checkés répartis entre processus/commandes, évaluation dynamique, templates/expressions, désérialisation et chargement/chaînes d'exécution. Les pistes non qualifiées restent à part. Voir le [prompt de mise à jour](maintenance/security/remote-code-execution/update-prompt.md), les [scénarios statiques](maintenance/security/remote-code-execution/evaluation-scenarios.md) et le [bilan d'évaluation](maintenance/security/remote-code-execution/evaluation.md).
- [Reproduction isolée de PoC](skills/security/isolated-vulnerability-reproduction/SKILL.md) : méthode et runner jetables pour valider un doute de code dans Docker local, avec ressources limitées et sans montage hôte. Voir le [prompt de maintenance](maintenance/security/isolated-vulnerability-reproduction/update-prompt.md), les [scénarios d'évaluation](maintenance/security/isolated-vulnerability-reproduction/evaluation-scenarios.md) et le [bilan d'évaluation](maintenance/security/isolated-vulnerability-reproduction/evaluation.md).
- [Squelettes de reproduction](skills/security/isolated-vulnerability-reproduction/templates/README.md) : exemples minimaux et hors ligne pour HTML/navigateur, JavaScript/Node, JavaScript/navigateur et PHP CLI, assortis d'un format commun de résultats control/trigger.
- [Corpus XSS complet](corpus/security/xss/README.md) : avis et rapports, scénarios, sondes de référence, bonnes pratiques, normes, notes et résultats bruts de recherche.
- [Guide de maintenance](maintenance/security/README.md) et [prompt de mise à jour](maintenance/security/prompt-maj-xss.md) : ajouter des sources et améliorer la skill sans confondre preuve statique et exécution observée.
- [Évaluation initiale de la skill](maintenance/security/evaluation-xss-static-review.md) : essais sur extraits synthétiques et limites de validation.
- [Évaluation de la skill de création](maintenance/meta/evaluation-research-backed-skill-builder.md) : scénarios sécurité et PostgreSQL, avec et sans la skill.
- [Évaluation de adr-authoring](maintenance/documentation/adr-authoring/evaluation.md) : scénario de référence et critères pour vérifier le respect des conventions ADR.
- [Skill test-pyramid](skills/testing/test-pyramid/SKILL.md) : méthode de rédaction des tests selon la pyramide, avec exemples PHP/Symfony, JavaScript, Vue et navigateur. Voir le [guide de sélection](skills/testing/test-pyramid/references/layer-selection.md), les [résumés de sources hors ligne](skills/testing/test-pyramid/references/offline-sources.md), les [scénarios d'évaluation](maintenance/testing/evaluation-scenarios.md) et le [bilan initial](maintenance/testing/evaluation.md).

Les références externes et résultats de recherche ont des niveaux de preuve différents ; un index GHSA dédupliqué ne garantit pas un ensemble d'incidents distincts ou entièrement analysés. Le corpus conserve des exemples de charges à des fins de recherche et d'analyse, mais la skill n'exécute aucune sonde.

## Licence et attribution

Les contributions originales de ce dépôt sont distribuées sous [licence MIT](LICENSE). Les sources tierces, extraits, références et résultats bruts conservent leurs droits et licences propres ; leur inclusion ne les place pas sous MIT. Voir [PROVENANCE.md](PROVENANCE.md).
