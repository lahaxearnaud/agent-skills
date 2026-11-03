# Installation et usage

Cette skill portable suit le format Agent Skills : `SKILL.md` et références relatives. Elle est préparée pour être copiée dans le répertoire de skills reconnu par votre installation de Codex ou OpenCode ; l'emplacement et le mécanisme de découverte dépendent de leur configuration et version. Ce dossier est un livrable dans le workspace ; il n'a pas été installé globalement ni activé automatiquement.

Exemple de demande : « Utilise la skill xss-static-review pour auditer statiquement les routes, templates Twig et composants Vue de ce dépôt. » L'agent lit le `SKILL.md`, puis les références pertinentes. La skill ne lance pas l'application ni de tests dynamiques ; ses recherches de code restent locales et en lecture seule.

Les références sont intégrées au dossier pour rester utilisables après copie. Elles synthétisent le corpus de ce dépôt sous `corpus/security/xss/` et pointent vers des avis et documentations publiques ; elles ne dépendent pas de l'accès à ce corpus ou à Internet pendant l'audit. Les versions et liens de sécurité peuvent évoluer.

Pour une installation locale à un projet, recopier tout le dossier sous `.agents/skills/xss-static-review/` dans le projet cible, si cet emplacement est pris en charge par la version utilisée. OpenCode documente aussi `.opencode/skills/xss-static-review/` : [documentation officielle](https://opencode.ai/docs/skills). Vérifier la découverte dans l’outil après copie ; aucun emplacement global n’a été modifié.
