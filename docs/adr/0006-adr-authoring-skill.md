# ADR-0006 : Création de la skill de rédaction des ADR

- **Statut :** Acceptée
- **Date :** 2026-11-03
- **Responsables de la décision :** Mainteneurs du dépôt

## Contexte et problème

Le dépôt impose déjà de consigner ses décisions d’architecture dans `docs/adr/` et de les référencer dans `AGENTS.md`. Une procédure réutilisable aidera les agents de code à appliquer cette règle et à adopter les mêmes garanties dans les dépôts qui n’ont pas encore de convention ADR.

Les dépôts peuvent utiliser des modèles, des emplacements et des index différents. La skill doit donc découvrir les règles locales avant d’appliquer des valeurs par défaut. Pour ce dépôt, `AGENTS.md`, le modèle `docs/adr/0000-template.md` et le registre qu’il contient restent les références autoritatives.

## Décision

Ajouter la skill installable `adr-authoring` sous `skills/documentation/`. Elle guidera la création, la mise à jour et la succession des ADR, ainsi que la tenue d’un registre consultable par les agents. Elle suivra les conventions explicites du dépôt ; en leur absence, elle utilisera `docs/adr/`, un fichier Markdown numéroté et un registre dans `AGENTS.md`.

La skill rédigera le contenu d’un ADR dans la langue principale du `README.md`, sauf politique ADR explicite du projet, et demandera une précision si cette langue ne peut pas être déterminée. Les ADR devront présenter le contexte ou problème, la décision, la date, le statut et les conséquences. Les exemples et options ne seront ajoutés que s’ils éclairent la décision.

Les consignes de rédaction de la skill resteront en anglais, conformément à l’ADR-0004. Les consignes du dépôt rendront la skill directement découvrable pour la rédaction et l’indexation des ADR.

## Conséquences

Les agents disposeront d’une procédure installable et réutilisable. Le catalogue du `README.md` et le registre d’ADR de `AGENTS.md` devront rester à jour avec les nouvelles skills et décisions.

Les ADR historiques ne seront pas réécrits ni traduits par cette décision. Dans ce dépôt, le modèle et les règles existants prévalent sur le modèle générique de la skill.
