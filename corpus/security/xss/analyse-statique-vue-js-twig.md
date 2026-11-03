# XSS : méthodes de validation par analyse statique — JavaScript, Vue et Twig

Recherche du 3 novembre 2026. Ce document décrit des méthodes de revue statique et des hypothèses vérifiables, pas une analyse d'un dépôt particulier. Les extraits ci-dessous sont des exemples de laboratoire synthétiques ; leurs données d'entrée sont supposées contrôlables. L'exécution effective d'une XSS dépend aussi du contexte navigateur, de l'usage de la page et de la CSP.

## Nouveaux cas publiés particulièrement utiles

1. **Vue I18n : attributs dans une traduction HTML** — [GHSA-x8qp-wqqm-57ph / CVE-2025-53892](https://github.com/intlify/vue-i18n/security/advisories/GHSA-x8qp-wqqm-57ph). Un paramètre interpolé dans une traduction rendue via `v-html` pouvait produire une XSS malgré `escapeParameterHtml`. **À suivre :** origine des paramètres → traduction → directive `v-html` ; vérifier versions et configuration. Ne pas supposer que l'option protège tous les contextes HTML.
2. **Vue I18n : sous-document `srcdoc`** — [GHSA-83rm-6c8r-g728 / CVE-2026-118257](https://github.com/advisories/GHSA-83rm-6c8r-g728). Les caractères neutralisés dans le document parent peuvent être décodés puis réinterprétés dans le sous-document iframe. **À suivre :** traduction → assainisseur → `v-html` → iframe avec `srcdoc` ; si iframe et attribut sont possibles. Le correctif cité par l'avis précédent ne suffisait pas à ce cas.
3. **Chamilo : publication stockée** — [GHSA-ppw9-gf4r-5c39](https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-ppw9-gf4r-5c39). Le rapport identifie le traitement PHP d'un message et un composant `SocialWallPost.vue` affichant du HTML ; la combinaison API et `v-html` sans assainissement approprié constitue le chemin à examiner. Il faut pouvoir injecter un message et qu'un autre utilisateur le consulte.
4. **Policy Reporter : chaîne considérée sans risque car non URL** — [GHSA-q98m-7w8c-w388 / CVE-2026-44245](https://github.com/advisories/GHSA-q98m-7w8c-w388). Le composant Vue `PropertyCard` envoie à `v-html` des valeurs qui ne correspondent pas à son test d'URL. **À suivre :** valeur de propriété → branche conditionnelle → `v-html`. Un test d'URL n'assainit pas le HTML de la branche alternative.
5. **Vue SSR : noms d'attributs d'un objet** — [GHSA-g2v6-rqmx-r4w6](https://github.com/vuejs/core/security/advisories/GHSA-g2v6-rqmx-r4w6). L'avis décrit un problème de validation des noms d'attributs dans le rendu SSR avec liaison d'objet ; cela concerne des **clés**, pas seulement les valeurs. Préconditions : rendu SSR, liaison d'un objet et contrôle pertinent de ses clés. L'avis consulté ne renseignait aucune version corrigée ; vérifier son état actuel avant décision.
6. **Vue 2 compiler et pollution de prototype** — [GHSA-g3ch-rx76-35fx / CVE-2024-6783](https://github.com/advisories/GHSA-g3ch-rx76-35fx). L'avis relie une pollution de prototype à des propriétés exploitées par le compilateur. Il faut établir séparément l'existence d'une primitive de pollution et l'utilisation du composant affecté. La présence de Vue 2 seule ne prouve pas une XSS exploitable.
7. **ComfyUI : clés JSON dans `innerHTML`** — [GHSA-j6xv-rx8r-mh6j](https://github.com/Comfy-Org/ComfyUI_frontend/security/advisories/GHSA-j6xv-rx8r-mh6j). Un nom de propriété issu d'un fichier de workflow est interpolé dans du HTML et transmis à `innerHTML`. **À suivre :** import JSON → clés de propriétés → dialogue de propriétés → puits HTML ; la victime doit ouvrir un fichier et la vue concernée. Vérifier les noms de propriétés autant que les valeurs.
8. **AVideo : transport JSON puis interprétation HTML** — [GHSA-wfq5-qgqp-hvhv](https://github.com/WWBN/AVideo/security/advisories/GHSA-wfq5-qgqp-hvhv). Une entrée URL traverse `json_encode`, puis atteint `innerHTML` côté client. La sérialisation JSON ne garantit pas la sécurité du puits HTML ultérieur.
9. **NocoDB : cellules de texte riche** — [GHSA-wwp2-x4rj-j8rm](https://github.com/nocodb/nocodb/security/advisories/GHSA-wwp2-x4rj-j8rm). L'avis rapporte une XSS stockée dans les cellules de texte riche. **À suivre :** droits d'édition d'une cellule, transformations du contenu et rendu au lecteur ; voir l'avis et le correctif pour la chaîne exacte.

Les huit premiers cas décrivent des mécanismes précis tirés d'avis ; le neuvième sert de piste de revue, avec une chaîne détaillée encore à confirmer. La CSP de l'application n'est pas systématiquement documentée dans ces avis : elle doit être relevée séparément.

## Étape 1 — Construire une carte des frontières de confiance

Pour chaque page, relever : contrôleur et route PHP, variables passées à `render`, template Twig parent et inclusions, données `data-*` et JSON exposées, point de montage Vue, composants, requêtes API et puits navigateur. Enregistrer les droits requis pour modifier chaque source. Un champ stocké, un fichier importé, un webhook, une traduction modifiable, une réponse API ou un nom de clé JSON peut être contrôlable même s'il ne provient pas directement de la requête de la victime.

Le parcours peut traverser PHP → Twig → DOM initial → JavaScript → composant Vue. Ne jamais considérer automatiquement une sortie Twig échappée, une base de données, une réponse interne ou une API comme une source de confiance pour les étapes suivantes. Noter les frontières non modélisées par l'outil et les relier manuellement par les noms de variables, champs JSON, attributs DOM et points d'appel.

## Étape 2 — Inventaire des sources, transformations et puits

| Couche | Sources et points d'entrée à considérer | Transformations et puits à examiner |
|---|---|---|
| JS natif | `location.search/hash`, URL, `document.referrer`, cookies accessibles, `postMessage`, réponses réseau, stockage local, fichiers importés, données DOM | `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `Range.createContextualFragment`, `DOMParser` si le résultat est inséré, `srcdoc`, URL et gestionnaires, évaluateurs de chaînes. |
| Vue | `props`, stores, `route.query/params/hash`, données d'API, paramètres d'i18n, contenu de slots, clés d'objets liés, état SSR hydraté | `v-html`, `innerHTML` dans `h()`/JSX, templates compilés à l'exécution, `:href`, `:src`, `v-bind="objet"`, composants d'aperçu, sérialisation SSR. |
| Symfony/Twig | Requête, entités, journaux, traductions modifiables, propriétés d'objets, résultat de `render` et fonctions/filters Twig personnalisés | `raw`, `autoescape false`, `Twig\Markup`, `is_safe`, `pre_escape`, réponse HTML, filtres, macros, inclusions, attributs dynamiques, interpolation dans JS ou URL. |

Un puits est sensible seulement dans le contexte approprié : `textContent` sur un élément de texte ordinaire n'interprète pas du HTML ; ne pas l’utiliser pour insérer du contenu non fiable dans un élément script exécutable. De son côté, `:href` ou `setAttribute('href', ...)` demande une validation de schéma ; `innerHTML` n'exécute pas nécessairement tous les types de balises script insérées, mais d'autres formes de contenu actif peuvent rester pertinentes. Ne pas traiter l'ensemble des `setAttribute`, `.html` ou des `props` comme des vulnérabilités sans résolution du contexte.

## Étape 3 — Analyse statique des flux

Pour chaque candidat, documenter : **source contrôlable → affectations / appels / champs → transformations → puits → contexte final**, avec fichiers et lignes. Utiliser l'AST et une analyse de propagation (« taint ») lorsque disponibles ; une simple recherche textuelle repère des points d'entrée mais ne démontre pas la continuité du flux.

- Propager au travers des concaténations, fonctions utilitaires, objets, tableaux, promesses, magasins Vue, champs d'API et valeurs retournées ; suivre aussi les clés dynamiques. Les résolutions dynamiques, appels indirects et alias peuvent nécessiter une revue manuelle.
- Modéliser `decodeURIComponent`, décodages HTML, parsers Markdown, JSON, sérialisation et conversions DOM comme des transformations, **pas** comme des assainisseurs universels.
- Les contrôles conditionnels ne sont protecteurs que si l'on prouve qu'ils couvrent tous les chemins vers le puits et qu'ils valident la valeur effectivement utilisée après ses transformations.
- Un assainisseur n'efface la propagation que pour un **contexte et une configuration** vérifiés. Par exemple, du HTML assaini ne garantit ni une URL sûre ni un template Vue sûr ; une mutation ou un décodage en aval peut invalider la garantie.
- Distinguer donnée contrôlée, texte échappé HTML, HTML assaini sous politique donnée, URL validée et valeur JS sérialisée. L'idéal est un suivi de plusieurs états ou des règles distinctes par contexte ; sinon, garder des alertes à confirmer et documenter les limites.
- Une CSP inconnue ne valide ni n'invalide le flux. L'évaluer après identification du contexte : le défaut de code et l'exploitabilité à l'exécution sont deux conclusions distinctes.

## Étape 4 — Vue : liaison entre templates et code

1. Parser chaque fichier `.vue` comme composant à trois zones : template, script et styles ; identifier bindings, alias, `props`, valeurs calculées, fonctions, hooks et stores.
2. Pour `v-html="expression"`, remonter l'expression jusqu'à ses sources dans le script, les props du parent et les réponses API. Vérifier si une sanitisation HTML adaptée est bien appliquée **au résultat final** et si une transformation ultérieure modifie celui-ci.
3. Pour `:href` / `:src`, suivre la construction de l'URL, sa normalisation, la liste des schémas et la destination effective. L'échappement d'attribut par Vue empêche l'injection de délimiteurs mais ne valide pas le schéma de l'URL.
4. Pour `v-bind="object"` et les noms dynamiques, examiner les clés contrôlables, les différences SSR/client et la version de Vue. Pour `h()`/JSX, rechercher les propriétés `innerHTML` et les fonctions de rendu personnalisées.
5. Vérifier toute compilation de templates ou montage sur du DOM préexistant contenant potentiellement une contribution non fiable. Une chaîne contrôlée utilisée comme **template** est une catégorie différente d'une interpolation de texte.
6. Tracer le SSR et l'hydratation : origine de l'état, sérialisation sûre dans le HTML et lectures ultérieures. Les templates Vue sont compilés différemment en SSR et côté client ; les deux chemins méritent examen.

Sources : [sécurité Vue](https://vuejs.org/guide/best-practices/security), [directives intégrées](https://vuejs.org/api/built-in-directives), [rendu SSR](https://vuejs.org/guide/scaling-up/ssr).

## Étape 5 — Twig et frontières PHP → navigateur

1. Inspecter la configuration d'auto-échappement effective, le type de template et les blocs `{% autoescape %}`. L'auto-échappement HTML n'analyse pas automatiquement toutes les grammaires imbriquées dans un document.
2. Remonter chaque `|raw`, `Markup`, fonction ou filtre déclaré `is_safe` jusqu'à la donnée et à la garantie réelle ; une constante connue ou un fragment HTML correctement assaini ne prouve pas une faille. Vérifier inclusions, macros, héritage et filtres propres au projet.
3. Distinguer contenu texte, attribut cité, URL, JS, CSS, noms d'attributs et imbrications. Un résultat échappé pour HTML peut être dangereux dans une URL ou un script. Les stratégies disponibles sont décrites par [Twig](https://twig.symfony.com/doc/3.x/filters/escape.html) ; la configuration et l'extension de filtres sont documentées dans [l'API](https://twig.symfony.com/doc/3.x/api.html) et [les extensions](https://twig.symfony.com/doc/3.x/advanced.html).
4. Suivre les données rendues en `data-*` jusqu'au code client : le navigateur décode les entités à la lecture. Si la valeur est réutilisée dans `innerHTML` ou `v-html`, la garantie initiale ne suffit pas.
5. Suivre toute donnée PHP sérialisée en JSON jusqu'à son placement HTML puis son utilisation : vérifier à la fois le contexte `<script>` et le puits final. Préférer un transport de données séparé lorsque possible.
6. Examiner filtres personnalisés `is_safe => ['all']` et `['html']` en fonction du contenu réellement produit, de `pre_escape`, des versions et de la stratégie active. Une déclaration est une affirmation du code, pas une preuve de sûreté.

## Exemples synthétiques : paires à valider

### JavaScript : source URL → DOM

```js
const name = new URLSearchParams(location.search).get('name') ?? '';
// Candidat : la donnée est interprétée comme HTML.
output.innerHTML = name;
// Variante texte : aucune interprétation HTML au puits.
output.textContent = name;
```

Constat fort si `output` désigne bien un élément de page et si la donnée URL atteint la première affectation. Une CSP stricte peut limiter l'exécution de certains vecteurs ; l'injection HTML demeure à qualifier.

### Vue : une même prop, deux contextes

```vue
<template>
  <div v-html="message"></div> <!-- candidat si message n'est pas du HTML fiabilisé -->
  <div>{{ message }}</div>      <!-- texte : interpolation échappée par Vue -->
</template>
<script setup>
defineProps({ message: String })
</script>
```

Remonter `message` au parent ; `v-html` sur une constante contrôlée par les développeurs ne prouve pas une XSS. Une donnée déjà assainie demande vérification de sa politique et de toute mutation.

### Twig → DOM : perte de la garantie HTML initiale

```twig
<div id="welcome" data-name="{{ name }}"></div>
```
```js
const name = document.querySelector('#welcome').dataset.name;
output.innerHTML = name; // candidat si name est contrôlable
// output.textContent = name; // option sûre pour du texte
```

La première sortie est échappée dans l'attribut cité ; la lecture `dataset` fournit la valeur décodée. Il faut suivre le second puits au lieu de conclure à partir du seul template.

### Vue : URL et HTML sont deux contextes différents

```vue
<a :href="target">Ouvrir</a>
```

Ce seul extrait est un **candidat** si `target` est contrôlable : vérifier la validation du schéma et les usages. L'interpolation d'attribut ne suffit pas à garantir une URL de navigation sûre. Un `https:` fixé et contrôlé peut être légitime.

## Outils et validation des résultats

- **Recherche ciblée :** `rg -n 'innerHTML|outerHTML|insertAdjacentHTML|document\.write|createContextualFragment|srcdoc|v-html|is_safe|Twig\\\\Markup|autoescape|\|\s*raw' assets src templates` ; adapter les répertoires. Cette étape ne couvre pas les alias, constructions calculées ou tous les puits.
- **CodeQL JS/TS :** utiliser les requêtes XSS existantes puis ajuster les modèles de sources, puits et appels propres au projet ; la [documentation du flux de données JS/TS](https://codeql.github.com/docs/codeql-language-guides/analyzing-data-flow-in-javascript-and-typescript/) et la [requête XSS côté client](https://codeql.github.com/codeql-query-help/javascript/js-xss/) expliquent le principe. Confirmer que la version et l'extracteur analysent effectivement les fichiers et expressions du projet, notamment `.vue` ; ne pas présumer une couverture inter-langages PHP/Twig/JS.
- **Semgrep :** utiliser le mode taint pour des règles source/puits et, au besoin, propagateurs et assainisseurs spécifiques. La portée inter-fonctions/inter-fichiers dépend du moteur et de l'édition ; voir [la documentation Semgrep](https://semgrep.dev/docs/writing-rules/glossary). Vérifier le support des templates `.vue` et Twig dans l'installation employée avant de revendiquer une couverture.
- **Twig/PHP :** en l'absence d'un moteur prouvé capable de suivre PHP → Twig → JS, combiner analyse PHP, analyse syntaxique des templates et revue manuelle des points de jonction. Ne pas promettre qu'une recherche regex résout les macros, héritages ou déclarations `is_safe`.
- **Triage :** classer chaque résultat en flux confirmé statiquement, candidat avec chaînon manquant, ou faux positif justifié. Un flux confirmé statiquement n'est pas nécessairement une XSS reproduite : préciser les contrôles d'accès, le navigateur, la CSP et l'interaction victime encore inconnus.
- **Tests locaux facultatifs après revue :** si le dépôt et un environnement isolé sont disponibles, ajouter un test positif et un contrôle négatif pour chaque règle, puis un test navigateur ciblé pour confirmer le contexte et la CSP. Les exemples ci-dessus n'ont pas été exécutés.

## Format conseillé pour la future skill

`identifiant ; technologie/version ; fichier:ligne source ; contrôle attaquant ; étapes du flux ; fichier:ligne puits ; contexte de parsing ; protections et transformations ; prérequis ; preuve ; CSP connue/inconnue ; impact conditionnel ; correctif ; test de non-régression ; limites/faux positifs`. Conserver séparément les avis publiés, les variantes synthétiques et les constats réels d'un dépôt.
