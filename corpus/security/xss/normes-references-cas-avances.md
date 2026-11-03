# Normes, documentations et cas avancés pour l'analyse XSS

Recherche documentaire du 3 novembre 2026. Ce complément relie les mécanismes des navigateurs aux cas du corpus et aux éléments à vérifier dans une future skill d'analyse de code. Les normes et documentations décrivent des comportements attendus ; elles ne remplacent pas un test dans les navigateurs et versions effectivement visés.

## 1. Normes et spécifications pertinentes

| Référence et statut | Ce qu'elle apporte | Application à l'analyse XSS |
|---|---|---|
| [WHATWG HTML — parsing](https://html.spec.whatwg.org/multipage/parsing.html), standard vivant | Décodage des octets, états du tokenizer, construction et correction de l'arbre, références de caractères. | Identifier le contexte avant et après chaque parse ; l'analyse d'une chaîne ne se réduit pas à chercher `<script>`. Suivre la valeur décodée d'un attribut lue par le DOM. |
| [WHATWG HTML — syntaxe](https://html.spec.whatwg.org/multipage/syntax.html), standard vivant | Syntaxe et contraintes des éléments, attributs et textes spéciaux. | Distinguer élément de texte ordinaire, attribut cité/non cité et contenu d'un élément `script`. |
| [WHATWG HTML — origine](https://html.spec.whatwg.org/multipage/origin.html), standard vivant | Concepts d'origine et d'origine opaque utilisés par le navigateur. | Identifier l'origine réelle du document exécutant le code ; une iframe isolée, un document `srcdoc` et un fichier sur le domaine principal n'ont pas automatiquement les mêmes droits. Vérifier également sandbox et héritage. |
| [WHATWG URL](https://url.spec.whatwg.org/), standard vivant | Parsing, normalisation, résolution d'URL relatives et traitement des caractères de contrôle. | Parser avant de comparer schéma et origine ; tester la valeur finalement utilisée. Une erreur de validation indiquée par la norme n'implique pas toujours un échec du parseur. |
| [RFC 3986 — URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html), RFC IETF | Syntaxe générique des URI et références relatives. | Utile pour le modèle général ; ne pas assimiler mécaniquement son interprétation à celle du parseur WHATWG utilisé par le navigateur. |
| [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259.html), RFC IETF | Grammaire JSON et média `application/json`. | Un JSON syntaxiquement valide n'est pas automatiquement sûr lorsqu'il est intégré à un document HTML ou injecté ensuite via `innerHTML` ; analyser aussi la grammaire englobante. |
| [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html), RFC IETF | Sémantique de HTTP et métadonnées de représentation, notamment `Content-Type`. | Vérifier le média réellement servi par chaque réponse. Ne pas attribuer à cette RFC la spécification complète du `nosniff` ou du parsing HTML. |
| [WHATWG MIME Sniffing](https://mimesniff.spec.whatwg.org/), standard vivant | Algorithmes de détermination du type de contenu par les navigateurs. | Contrôler `Content-Type`, `X-Content-Type-Options: nosniff`, le type de destination et le navigateur ; `nosniff` n'empêche pas qu'un HTML explicitement servi comme tel soit actif. |
| [W3C CSP Level 3](https://www.w3.org/TR/CSP3/), spécification en évolution | Directives, nonces, hash, règles inline et comportement de plusieurs politiques. | Évaluer la directive effective pour la destination : éléments script, attributs, URL, chargements et rapports. Une politique en mode rapport seul ne bloque pas. |
| [W3C Trusted Types](https://w3c.github.io/trusted-types/dist/spec/), spécification en évolution | Types et politiques pour certains puits d'injection DOM. | Vérifier enforcement, navigateurs cibles, puits couverts et implémentation des politiques. Un type créé par une politique permissive ne démontre pas que le contenu est sûr. |
| [RFC 6265 — HTTP State Management](https://www.rfc-editor.org/rfc/rfc6265.html), RFC IETF | Sémantique de base des cookies, dont `HttpOnly` et `Secure`. | `HttpOnly` limite l'accès par des API non HTTP ; il n'empêche pas par lui-même un script exécuté dans l'origine d'effectuer des requêtes auxquelles le navigateur joint le cookie. Pour SameSite, consulter la documentation navigateur à jour plutôt que cette RFC historique seule. |
| [WHATWG Fetch](https://fetch.spec.whatwg.org/), standard vivant | Requêtes, réponses, CORS, modes et traitement des ressources. | Analyser séparément l'envoi d'une requête, ses identifiants et l'accès à sa réponse ; une restriction de lecture CORS ne signifie pas toujours absence d'envoi ou d'effet. |

Les standards WHATWG évoluent ; les RFC sont des publications versionnées ; les spécifications W3C mentionnées peuvent évoluer. Conserver la date de consultation, la version de navigateur et la configuration du test lorsqu'un résultat dépend de leur interprétation.

## 2. Documentation de test et jeux de référence

- **[OWASP WSTG 4.2 — XSS réfléchie](https://wstg.owasp.org/v4.2/4-Web_Application_Security_Testing/07-Input_Validation_Testing/01-Testing_for_Reflected_Cross_Site_Scripting/)** : inventorier les points d'entrée, repérer la réflexion puis examiner le contexte et l'impact réel. Les versions figées ont des identifiants stables ; ne pas confondre avec les identifiants des versions en développement.
- **[OWASP WSTG 4.2 — XSS stockée](https://wstg.owasp.org/stable/4-Web_Application_Security_Testing/07-Input_Validation_Testing/02-Testing_for_Stored_Cross_Site_Scripting/)** : documenter séparément la phase d'écriture, le stockage et la consultation par le rôle victime.
- **[OWASP WSTG 4.2 — XSS DOM](https://wstg.owasp.org/stable/4-Web_Application_Security_Testing/11-Client-side_Testing/01-Testing_for_DOM-based_Cross_Site_Scripting/)** : partir des sources et puits côté client ; les fragments d'URL et flux purement navigateur peuvent ne pas apparaître dans la réponse serveur analysée par un scanner HTTP. Les exemples historiques du guide ne garantissent pas le comportement des navigateurs actuels.
- **[OWASP — DOM Clobbering Prevention](https://cheatsheetseries.owasp.org/cheatsheets/DOM_Clobbering_Prevention_Cheat_Sheet.html)** : examiner les collisions de noms/id DOM avec des propriétés utilisées par du code de confiance et les gadgets en aval.
- **[DOMPurify — modèle de sécurité](https://github.com/cure53/DOMPurify/wiki/Security-Goals-%26-Threat-Model)** et **[historique des classes de contournement](https://github.com/cure53/DOMPurify/wiki/Attack-Classes-%26-Bypass-History)** : mXSS, différences de parsing, espaces de noms, configuration et modification après assainissement. Ces pages évoluent ; comparer avec la version déployée et ses avis.
- **[Web Platform Tests](https://github.com/web-platform-tests/wpt)** : suite inter-navigateurs utile pour vérifier des hypothèses de parsing, URL, CSP et DOM. C'est une source de tests de conformité ; un test WPT réussi ne démontre pas la sûreté d'une application.
- **[CodeQL — flux JS/TS](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-javascript-and-typescript/)** : propagation des données et adaptation des modèles ; vérifier la couverture des `.vue` et des jonctions PHP/Twig/JS dans la version utilisée.
- **[Semgrep — glossaire analyse de flux](https://semgrep.dev/docs/writing-rules/glossary)** : sources, puits, assainisseurs et portée d'analyse ; vérifier les fonctionnalités et l'édition réellement utilisées.

## 3. Cas publiés additionnels et limites de confiance

[Index CSV des dix cas](cas-avances.csv).

Les huit premiers avis ci-dessous sont **de nouveaux identifiants GHSA par rapport aux deux index existants**. Le neuvième est un avis de discussion supplémentaire : les mainteneurs contestent son caractère de vulnérabilité dans leur modèle de menace. Le dixième, Twig, figurait déjà dans le corpus et est approfondi ici. Les versions et correctifs indiqués sont ceux des avis consultés : reconsulter leurs mises à jour et les plages complètes avant d'agir.

### A01 — mXSS après changement de contexte : DOMPurify

[GHSA-h8r8-wccr-v5f2](https://github.com/cure53/DOMPurify/security/advisories/GHSA-h8r8-wccr-v5f2) : une sortie assainie est concaténée dans un élément spécial puis reparsée ; le changement de contexte peut modifier l'arbre et créer un gestionnaire actif. L'avis du dépôt indique 3.3.1 tandis que l'[avis GitHub agrégé](https://github.com/advisories/GHSA-h8r8-wccr-v5f2) indique les versions antérieures à 3.3.2 ; les deux mentionnent une correction en 3.3.2. Cette divergence de plage reste à vérifier auprès de l'éditeur. **Conditions :** entrée contrôlée, réinsertion dans un contexte concerné et navigateur/CSP permettant l'effet. **Détection :** remonter la chaîne après `sanitize`, notamment concaténations et nouvel `innerHTML`. Les identifiants CVE mentionnés dans le texte historique de l'avis et dans ses métadonnées diffèrent ; se référer au GHSA et vérifier l'état actuel.

### A02 — Prototype pollution affaiblissant l'assainisseur

[GHSA-v9jr-rg53-9pgp](https://github.com/cure53/DOMPurify/security/advisories/GHSA-v9jr-rg53-9pgp) : une pollution préalable de prototype peut rendre permissifs des paramètres de contrôle d'éléments personnalisés dans DOMPurify 3.0.1–3.3.3 ; correctif indiqué en 3.4.0. **Conditions :** primitive de pollution effective avant l'appel, configuration et entrée concernées. **Détection :** joindre la revue des fusions d'objets à celle des paramètres de l'assainisseur ; ne pas conclure à partir du seul numéro de version.

### A03 — Imbrication et contrôle de profondeur

[GHSA-mmhx-hmjr-r674](https://github.com/cure53/DOMPurify/security/advisories/GHSA-mmhx-hmjr-r674) : l'avis décrit un contournement du contrôle de profondeur par du HTML spécialement imbriqué, éventuellement affaibli par pollution de prototype. Correctifs indiqués : 2.5.4 et 3.1.3 selon la branche. **Détection :** versions effectivement installées, dépendances transitives et tests de contenu riche ; une entrée imbriquée ne prouve pas à elle seule le comportement d'un navigateur donné.

### A04 — Mutation pendant la visite de `selectedcontent`

[GHSA-87xg-pxx2-7hvx](https://github.com/cure53/DOMPurify/security/advisories/GHSA-87xg-pxx2-7hvx) : le navigateur peut reconstruire un sous-arbre déjà parcouru par l'assainisseur. L'avis vise DOMPurify 3.4.4 et indique un correctif en 3.4.5. **Conditions :** version, élément et comportement du moteur de navigateur concernés. **Détection :** options et versions, puis validation du DOM final après la mutation, pas uniquement comparaison de chaînes.

### A05 — `IN_PLACE` et racine formulaire perturbée

[GHSA-r47g-fvhr-h676](https://github.com/cure53/DOMPurify/security/advisories/GHSA-r47g-fvhr-h676) : en mode `IN_PLACE`, un formulaire racine influençable et des descendants aux noms particuliers pouvaient préserver des attributs dangereux. L'avis indique les versions jusqu'à 3.4.5 et un correctif en 3.4.6. **Conditions :** mode, type de racine et contrôle du DOM décrits dans l'avis ; l'avis distingue les entrées chaînes et d'autres racines. **Détection :** suivre les nœuds transmis à `sanitize`, et pas uniquement les chaînes.

### A06 — Vite et code généré sensible au DOM clobbering

[GHSA-64vr-g452-qvp3](https://github.com/vitejs/vite/security/advisories/GHSA-64vr-g452-qvp3) : dans les configurations et formats de sortie mentionnés, du HTML contrôlé sans script peut perturber une résolution d'URL utilisée par du code généré. **Conditions :** version et format concernés, gadget produit et possibilité d'injecter les éléments appropriés. **Détection :** vérifier le lockfile, les options de build, les assets générés et le chemin de chargement. Ne pas supposer que toute application Vite est exploitable.

### A07 — Rollup et URL de script générée

[GHSA-gcx4-mw62-g8wm](https://github.com/rollup/rollup/security/advisories/GHSA-gcx4-mw62-g8wm) : le code généré pour certains formats et usages d'`import.meta.url` peut utiliser une propriété DOM perturbée comme base d'URL. Les branches et versions corrigées figurent dans l'avis. **Conditions :** bundle correspondant, gadget atteignable et HTML contrôlable. **Détection :** examiner aussi les dépendances de build et reconstruire les assets après correction, pas seulement les bibliothèques chargées à l'exécution.

### A08 — Webpack et chemin public automatique

[GHSA-4vvj-4cpr-p986](https://github.com/webpack/webpack/security/advisories/GHSA-4vvj-4cpr-p986) : l'avis décrit une collision avec `document.currentScript` dans le code généré pour la résolution automatique du chemin public. **Conditions :** version, configuration `publicPath`, possibilité d'injecter du HTML et chargement ultérieur d'un script concerné. L'avis distingue les plages affectées et corrigées : consulter les métadonnées actuelles pour les versions exactes. **Détection :** sources applicatives, configuration Encore/Webpack et code réellement construit.

### A09 — DOM inter-fenêtres et `IN_PLACE` : avis contesté

[GHSA-4w3q-35jp-p934](https://github.com/cure53/DOMPurify/security/advisories/GHSA-4w3q-35jp-p934) : le rapport décrit un élément d'une autre fenêtre passé au mode `IN_PLACE`. Les mainteneurs indiquent dans l'avis ne pas considérer le cas comme une vulnérabilité entrant dans leur modèle de menace et évoquent une publication pour discussion. **À retenir pour revue :** vérifier le document propriétaire du nœud, le contrat d'API et la valeur retournée ; ne pas présenter cet avis comme un bug confirmé indépendamment de cette réserve. Les métadonnées et le commentaire des mainteneurs doivent être relus ensemble.

### A10 — Twig HtmlDumper : nom de template dans le profiler

[GHSA-2g2g-8p8h-fgwm](https://github.com/twigphp/Twig/security/advisories/GHSA-2g2g-8p8h-fgwm), déjà indexé : l'avis concerne le rendu de noms de templates et de profils dans le dumper HTML. **À vérifier :** accès au profiler, possibilité d'influencer les noms, version et correctif ; ne pas extrapoler à un serveur de production n'exposant pas cette interface. Il complète le cas distinct du profiler Symfony et de ses extraits de fichiers.

## 4. Nouvelles hypothèses pour futurs tests de régression

Ces hypothèses sont **synthétiques** : elles ne sont pas des incidents supplémentaires.

1. Un paramètre PHP échappé dans un attribut `data-*` est relu par `dataset` puis inséré par Vue dans `v-html` : vérifier les deux étapes et un contrôle négatif en interpolation texte.
2. Un JSON valide est inclus dans une balise de données HTML, puis lu par JavaScript : comparer le document servi, l'arbre créé et l'utilisation ultérieure. Le type JSON ne supprime pas la nécessité d'examiner le parseur HTML englobant.
3. Un champ de traduction modifiable par un rôle limité est interpolé dans un template de confiance, puis envoyé à `v-html` : vérifier séparément contrôle du message et contrôle du paramètre, ainsi que l'assainissement final.
4. Une entrée HTML assainie est reconstruite via un wrapper spécial puis reparsée : observer l'arbre final et les modifications liées au navigateur ; comparer avec un rendu en texte et avec une insertion dans le contexte effectivement pris en charge par l'assainisseur.
5. Une URL relative, absolue ou contenant des caractères normalisés est validée côté PHP puis utilisée dans le navigateur : comparer les parseurs, la base d'URL et la valeur finale ; ne pas déduire un bypass sans divergence effective.
6. Un champ `id` ou `name` dans du HTML contrôlable coexiste avec un bundle affecté : inspecter le code généré, les règles CSP et le chargement dynamique avant de conclure à une XSS.
7. Une dépendance de build est mise à jour sans reconstruction du bundle servi : vérifier séparément lockfile, build et contenu réellement déployé.
8. Un nœud transmis à `DOMPurify` en mode `IN_PLACE` provient d'une autre fenêtre ou constitue une racine détachée : vérifier contrat de la version, nœud retourné et arbre final ; distinguer le cas contesté A09 de la vulnérabilité décrite en A05.
9. Un résultat apparemment sûr est réinjecté dans `iframe.srcdoc` : tester le sous-document, son origine et sa sandbox plutôt que de se limiter au document parent.
10. Une CSP en `Report-Only` et une autre politique appliquée coexistent : examiner tous les en-têtes effectifs, les directives pertinentes et les résultats navigateur.

## 5. Champs supplémentaires à prévoir dans la future skill

Ajouter aux fiches d'analyse : `standard_ou_grammaire`, `ordre_des_parseurs`, `type_document`, `origine_finale`, `etat_sandbox`, `version_navigateur`, `version_dependance`, `code_source_ou_bundle`, `date_build`, `configuration_assainisseur`, `transformations_apres_assainissement`, `statut_avis`, `contexte_CSP` et `preuve_statique_ou_dynamique`. Toute valeur non visible doit rester « inconnue » ; une version vulnérable est un signal d'inventaire, tandis qu'un constat applicatif nécessite aussi le chemin d'utilisation et ses préconditions.
