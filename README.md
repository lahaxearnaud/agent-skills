# Agent Skills

Un catalogue de skills pour agents de code, organisé par domaine. Il comprend des skills de revue statique XSS et injection SQL, une skill de rédaction d’ADR et une méthode pour construire des skills fondées sur un corpus.

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

# Installer la skill de rédaction et d'indexation des ADR
npx skills add lahaxearnaud/agent-skills --skill adr-authoring --agent codex opencode --yes

# Installer pour son utilisateur plutôt que pour le projet courant
npx skills add lahaxearnaud/agent-skills --skill xss-static-review --global
```

La commande est **`npx skills add`** : elle exécute la CLI `skills` et installe des fichiers de skill, pas une dépendance npm de l'application auditée. La prise en charge d'un agent et ses chemins d'installation dépendent de la version de la CLI et de l'agent ; consulter leur documentation. Chaque skill installe ses propres références avec elle ; la revue XSS ne nécessite pas le corpus au moment de l’audit.

## Catalogue

| Domaine | Skill | Utilisation |
|---|---|---|
| Security | [xss-static-review](skills/security/xss-static-review/SKILL.md) | Revue statique de XSS Web : PHP, Symfony, Twig, JavaScript, Vue et autres technologies. |
| Security | [sql-injection-static-review](skills/security/sql-injection-static-review/SKILL.md) | Revue statique des injections SQL : PHP, Doctrine et autres technologies Web. |
| Documentation | [adr-authoring](skills/documentation/adr-authoring/SKILL.md) | Rédige, met à jour et indexe les ADR en respectant les conventions du dépôt. |
| Meta | [research-backed-skill-builder](skills/meta/research-backed-skill-builder/SKILL.md) | Création de skills documentées à partir de sources et de corpus traçables. |

Exemple : « Utilise `xss-static-review` pour examiner les sources de ce dépôt et identifier les flux XSS potentiels. » La skill interdit de lancer l'application, un navigateur, des payloads ou un scanner actif. Elle distingue les flux établis statiquement des candidats dont un élément reste inconnu.

## Corpus et maintenance

- [Corpus injection SQL](corpus/security/sql-injection/README.md) : 61 résumés de rapports publiés, 20 pistes à qualifier et 30 scénarios synthétiques ; voir aussi le [prompt de maintenance SQL](maintenance/security/sql-injection/update-prompt.md) et l’[évaluation SQL](maintenance/security/sql-injection/evaluation.md).
- [Corpus XSS complet](corpus/security/xss/README.md) : avis et rapports, scénarios, sondes de référence, bonnes pratiques, normes, notes et résultats bruts de recherche.
- [Guide de maintenance](maintenance/security/README.md) et [prompt de mise à jour](maintenance/security/prompt-maj-xss.md) : ajouter des sources et améliorer la skill sans confondre preuve statique et exécution observée.
- [Évaluation initiale de la skill](maintenance/security/evaluation-xss-static-review.md) : essais sur extraits synthétiques et limites de validation.
- [Évaluation de la skill de création](maintenance/meta/evaluation-research-backed-skill-builder.md) : scénarios sécurité et PostgreSQL, avec et sans la skill.
- [Évaluation de adr-authoring](maintenance/documentation/adr-authoring/evaluation.md) : scénario de référence et critères pour vérifier le respect des conventions ADR.

Les références externes et résultats de recherche ont des niveaux de preuve différents ; un index GHSA dédupliqué ne garantit pas un ensemble d'incidents distincts ou entièrement analysés. Le corpus conserve des exemples de charges à des fins de recherche et d'analyse, mais la skill n'exécute aucune sonde.

## Licence et attribution

Les contributions originales de ce dépôt sont distribuées sous [licence MIT](LICENSE). Les sources tierces, extraits, références et résultats bruts conservent leurs droits et licences propres ; leur inclusion ne les place pas sous MIT. Voir [PROVENANCE.md](PROVENANCE.md).
