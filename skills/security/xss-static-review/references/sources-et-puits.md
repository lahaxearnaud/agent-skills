# Sources, transformations et puits pour la revue XSS

Ces listes orientent la recherche. Pour chaque occurrence, déterminer le type de donnée, l'acteur qui la contrôle, le chemin et le contexte : aucun mot-clé ne suffit à lui seul.

## Sources à inventorier

- HTTP : query, chemin, corps, formulaires, JSON, cookies, en-têtes, paramètres multiples et URL de redirection ; données venant d'une authentification SAML/OIDC et messages d'exception associés.
- Données persistées : profils, commentaires, noms de produits, traductions modifiables, configurations éditables, CMS, titres, fichiers, résultats de recherche, tickets et publications. Distinguer contrôle d'écriture et lecteurs.
- Fournisseurs externes : API, flux webhook, messages WebSocket, imports, fichiers, noms de fichier, métadonnées de base de données, certificats, logs, DNS et métriques. Une API interne ou une base ne confère pas automatiquement la confiance.
- Navigateur : `location.search`, `location.hash`, `location.href`, `document.referrer`, `document.cookie`, `localStorage`, IndexedDB, réponses `fetch`/XHR, `postMessage`, attributs `data-*` et état DOM. Pour les messages, relever contrôle de `event.origin`, `event.source` et structure.
- Vue : props et slots, router query/params/hash, données API, stores, computed/watchers, traductions, bindings, clés d'objets, état SSR et hydratation. Une prop n'est pas automatiquement contrôlée par un attaquant : remonter aux parents et à leurs sources.
- Twig/PHP : paramètres de `render`, entités et getters, macros, inclusions, héritage, globals, traductions, fonctions/filtres et `Twig\Markup`. Suivre les valeurs à travers les différents fichiers.

## Propagation et changements de grammaire

Suivre affectations, interpolations, callbacks, appels, tableaux/objets et leurs **clés**, closures, événements, promesses, API, base de données, stockage, sérialisation et noms de champs. Noter explicitement les étapes inconnues.

Repérer `decodeURIComponent`, `html_entity_decode`, `htmlspecialchars_decode`, parsing et sérialisation HTML/DOM, Markdown, XML, SVG, URL, JSON, charset et normalisation Unicode. Un décodage ne signifie pas automatiquement vulnérabilité : déterminer l'entrée, l'ordre et le puits final. Lire un attribut HTML via `dataset` peut restituer les caractères décodés après un encodage initial.

Ne jamais traiter `JSON.parse`, `json_encode`, une validation de format, un stockage en base ou un retour d'API comme une désinfection HTML universelle. Les transformations après un assainissement peuvent modifier ou invalider sa garantie.

## Puits par contexte

| Contexte | Candidats |
|---|---|
| HTML serveur | Twig `raw`, `autoescape false`, `Markup`, fonctions/filters `is_safe`, concaténation dans une réponse PHP, vues d'erreur ou debug, génération HTML dans des bibliothèques. |
| HTML DOM | `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, jQuery `.html`/`.append` avec HTML, `Range.createContextualFragment`, parseurs HTML suivis d'une insertion ; `v-html`, `h(...,{innerHTML})`, JSX `innerHTML`, autres mécanismes de HTML brut. |
| URL/navigation | `href`, `src`, `action`, `formaction`, redirections et paramètres de retour, navigation JS, URL de scripts ou iframe. Vérifier schéma et destination ; un attribut échappé ne valide pas le protocole. |
| Code JS | Donnée dans une balise `<script>`, gestionnaire inline, `eval`, `Function`, minuteurs à chaîne, création de script et compilation de template client. Tenir compte du parseur HTML englobant. |
| Document actif | Téléversement, aperçu ou conversion HTML/SVG/XML, `iframe.srcdoc`, réponse webhook et fichier servi inline. Examiner média, origine, sandbox et navigation directe. |
| CSS et UI | Valeurs de style ou HTML libre pouvant modifier l'interface ; qualifier séparément la tromperie UI et ne pas affirmer XSS sans chaîne d'exécution. |

`textContent` sur un élément de présentation ordinaire crée du texte, pas du HTML. Sur un élément `script`, la valeur peut être du code : vérifier le type et le cycle de vie de l'élément. Les attributs fixes non exécutables, valeurs constantes et constructions DOM structurées peuvent être sûrs ; ne pas confondre symbole et preuve.

## Recherche dirigée

Commencer par les dossiers source, templates et configuration réellement présents. Chercher aussi les appels indirects et les bibliothèques générant du HTML ; ajuster les exclusions `vendor`, `node_modules` et bundles si une dépendance ou un artefact est pertinent. Utiliser les outils SAST présents seulement s'ils peuvent analyser localement et statiquement les fichiers ; documenter leurs limites de langage, de fichiers et d'interprocéduralité. Ne pas installer ou lancer un outil qui exécute l'application.
