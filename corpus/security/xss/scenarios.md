# Scénarios hypothétiques pour revue de code

Ces scénarios sont des hypothèses de test, **pas des incidents publiés**. Les familles de syntaxe et de transformations sont inspirées notamment de [PayloadsAllTheThings — XSS](https://swisskyrepo.github.io/PayloadsAllTheThings/XSS%20Injection/) et de sa [rubrique sur les filtres](https://swisskyrepo.github.io/PayloadsAllTheThings/XSS%20Injection/1%20-%20XSS%20Filter%20Bypass/). Leur exploitabilité dépend du parseur, des versions, des transformations, du contrôle effectif de l'entrée et de la politique du document. Chaque ligne décrit un chemin possible : vérifier toutes les conditions ; la présence d'un mot-clé seul ne prouve rien. Sauf mention contraire, une CSP permissive ou un chemin d'exécution autorisé est également nécessaire pour obtenir l'exécution JS.

Colonnes : **source → destination / condition / remède**. L'impact potentiel commun, si exécution confirmée dans l'origine de l'application, est l'usage des droits de la victime et l'accès aux données accessibles au script, sous réserve des restrictions du navigateur.

## Twig et Symfony

| ID | Chemin et condition de déclenchement | Correction ou piste de revue |
|---|---|---|
| S01 | Paramètre de recherche → `{{ q\|raw }}` dans le corps HTML ; contrôle de q. | Retirer `raw`, conserver l'auto-échappement HTML. |
| S02 | Nom de produit stocké → macro de fil d'Ariane avec `raw` ; page vue par un autre utilisateur. | Échapper chaque libellé au rendu, pas au stockage. |
| S03 | Nom de compte → `{% autoescape false %}` sur un bloc HTML. | Réactiver l'auto-échappement et limiter tout bloc d'exception. |
| S04 | Objet provenant de la base → conversion en `Twig\Markup` ; contenu non fiable déclaré déjà sûr. | Réserver `Markup` à du HTML réellement assaini et au contexte HTML. |
| S05 | Filtre Twig personnalisé → `is_safe => ['all']` pour un résultat HTML ; réutilisation dans JS ou URL. | Déclarer uniquement le contexte garanti ; encoder pour le contexte final. |
| S06 | Fonction Twig → `is_safe => ['html']` mais concaténation d'un nom non échappé. | Échapper les parties textuelles avant d'assembler le HTML. |
| S07 | Texte utilisateur → HTML assaini → `html_entity_decode()` → `raw`. | Éviter toute transformation qui recrée du balisage après assainissement. |
| S08 | Message traduit paramétré → rendu `raw` ; un paramètre de traduction est contrôlable. | Échapper les paramètres selon leur contexte ; éviter `raw` global. |
| S09 | Valeur de formulaire → attribut HTML sans guillemets ; séparateurs autorisés. | Toujours citer les valeurs et utiliser l'échappement adapté. |
| S10 | URL fournie → `href` cité et échappé HTML, mais schéma dangereux autorisé. | Analyser l'URL et autoriser les schémas attendus, puis encoder l'attribut. |
| S11 | Chemin utilisateur → `src` d'une iframe ; contenu actif du même domaine. | Héberger le contenu non fiable sur une origine isolée ; sandbox adaptée. |
| S12 | Nom JSON contrôlé → nom de balise dynamique d'un composant HTML. | Liste fermée de noms de balises et construction DOM structurée. |
| S13 | SVG distant ou téléversé → `ux_icon()` / SVG inline ; fournisseur ou fichier contrôlable. | Mise à jour et assainissement SVG robuste ; privilégier fichiers de confiance. |
| S14 | Fichier de log ou source non PHP contrôlable → profiler développeur rendu en HTML. | Échapper chaque ligne ; restreindre l'accès au profiler et corriger la dépendance. |
| S15 | Requête HTTP → page d'erreur concaténant le message d'exception en HTML. | Échapper les messages ; désactiver les pages de debug en production. |
| S16 | Paramètre utilisateur → réponse HTML manuelle `new Response(...)` via concaténation. | Utiliser Twig auto-échappé et définir explicitement Content-Type/charset. |
| S17 | Nom de fichier téléversé → attribut `download`, titre ou tableau admin via `raw`. | Encoder à chaque sortie ; traiter le nom de fichier comme non fiable. |
| S18 | Valeur `data-*` initialement échappée → lecture via `dataset` → `innerHTML`. | La lecture DOM restitue du texte décodé : utiliser `textContent` ensuite. |
| S19 | Entrée → `json_encode` injecté dans `<script>` sans protection HTML des délimiteurs. | Sérialiser de manière sûre pour un script HTML ou sortir le JSON via un endpoint séparé. |
| S20 | URL de retour stockée → attribut de bouton/action ; validation ne vérifie que l'hôte avant normalisation finale. | Parser une fois, valider schéma/hôte après canonicalisation et encoder la sortie. |

## Contextes HTML, JS, DOM et URL

| ID | Chemin et condition de déclenchement | Correction ou piste de revue |
|---|---|---|
| S21 | Paramètre URL → texte HTML par concaténation serveur sans échappement. | Échapper comme texte HTML. |
| S22 | Paramètre → attribut HTML cité ; guillemet de fermeture non encodé. | Encoder l'attribut et conserver les guillemets. |
| S23 | Paramètre → commentaire HTML ; possibilité de fermer le commentaire et créer des éléments. | Ne pas insérer de données non fiables dans les commentaires HTML. |
| S24 | Entrée → bloc `<script>` dans une chaîne JS ; fermeture du script interprétée par le parseur HTML. | Sérialisation sûre pour HTML et JS ; préférer JSON séparé. |
| S25 | Entrée → chaîne JS encodée pour HTML seulement. | Éviter la génération JS ; sinon sérialiser pour JS puis protéger le contexte HTML englobant. |
| S26 | Entrée → littéral de gabarit JS ; interpolation ou délimiteur contrôlable. | Éviter l'insertion de code ; utiliser une valeur JSON sérialisée sûre. |
| S27 | `location.search` → `innerHTML`. | `URLSearchParams` pour lire, `textContent` pour afficher. |
| S28 | `location.hash` → `insertAdjacentHTML`. | Construire des nœuds et affecter `textContent`. |
| S29 | `document.referrer` → `document.write`. | Éviter `document.write` et traiter le Referer comme non fiable. |
| S30 | `postMessage` depuis une origine non vérifiée → HTML dynamique. | Vérifier précisément `event.origin` et le schéma des données ; éviter `innerHTML`. |
| S31 | Réponse API contrôlable → `outerHTML`. | Construire le DOM ou assainir le HTML nécessaire avec une politique stricte. |
| S32 | Paramètre → jQuery `.html()` / `.append()` avec chaîne de HTML. | Utiliser `.text()` pour le texte et revoir les versions des dépendances. |
| S33 | Paramètre → `Range.createContextualFragment()` puis insertion. | Traiter ce parseur comme un puits HTML ; utiliser des nœuds textuels. |
| S34 | Message d'erreur API → notification dont le moteur autorise HTML. | Afficher le texte avec une API sans HTML. |
| S35 | Données sérialisées dans `data-*` → décodage JS → rendu via template HTML. | Suivre la donnée à travers les décodages et encoder au dernier puits. |
| S36 | Valeur → `setAttribute('onclick', valeur)` ou attribut d'événement équivalent. | Ne jamais affecter de code depuis une donnée ; utiliser des gestionnaires fixes. |
| S37 | URL utilisateur → `href` avec schéma script après décodage ou normalisation. | Autoriser explicitement les schémas et vérifier la valeur interprétée. |
| S38 | URL utilisateur → `iframe.srcdoc` sans sandbox stricte ; HTML contrôlable. | Éviter `srcdoc` non fiable ; isoler origine et privilèges. |
| S39 | Paramètre → nom de callback JSONP renvoyé comme code JavaScript. | Supprimer JSONP ; sinon validation très stricte d'identifiant et retour JSON ordinaire. |
| S40 | Fragment d'URL → `eval`, `Function` ou minuteur à chaîne. | Supprimer l'évaluation de chaînes ; CSP sans `unsafe-eval` en défense additionnelle. |

## Sanitisation, formats et transformations

| ID | Chemin et condition de déclenchement | Correction ou piste de revue |
|---|---|---|
| S41 | Éditeur riche → assainissement par regex ne comprenant pas le parseur HTML. | Employer un assainisseur maintenu et configuré par liste autorisée. |
| S42 | HTML assaini → transformation Markdown → nouveau rendu HTML. | Assainir après la dernière transformation générant du HTML. |
| S43 | Markdown non fiable → moteur autorisant HTML brut → insertion directe. | Désactiver le HTML brut ou assainir la sortie produite. |
| S44 | HTML filtré → `innerHTML` → sérialisation/reparsing modifiant l'arbre ; mutation XSS. | Tester avec les parseurs cibles et une version corrigée de l'assainisseur. |
| S45 | HTML apparemment filtré → SVG/MathML autorisé avec attributs ou espaces de noms dangereux. | Désactiver ces espaces de noms si inutiles ; assainisseur à jour. |
| S46 | URL assainie → décodage d'entités ou percent-encoding ultérieur reconstituant un schéma interdit. | Normaliser avant validation, éviter tout décodage après validation. |
| S47 | Unicode de largeur complète → normalisation NFKC après filtre transformant des caractères en syntaxe HTML. | Canonicaliser avant les contrôles ; encoder au rendu. Cela dépend d'une normalisation effective. |
| S48 | Entrée multipart → double décodage entre proxy et application. | Documenter les transformations et valider/encoder après la dernière pertinente. |
| S49 | Filtre limité à `script` → attribut événement, SVG ou autre contexte actif autorisé. | Ne pas utiliser de blacklist de mots ; appliquer les défenses contextuelles. |
| S50 | Filtre sur casse fixe → conversion de casse en aval donnant une syntaxe reconnue. | Éviter les blacklists ; modéliser la transformation effectivement utilisée. |
| S51 | HTML assaini côté serveur → bibliothèque cliente le modifie et insère des attributs dangereux. | Assainir après la dernière mutation ou construire le DOM de façon sûre. |
| S52 | Tableur importé → export HTML contenant données ou styles non échappés. | Mettre à jour le générateur, traiter le document importé comme non fiable. |
| S53 | Fichier HTML/SVG téléversé → service en ligne sous l'origine de l'application. | Origine sans cookies séparée, `Content-Disposition: attachment` si possible et type correct. |
| S54 | Type MIME incorrect + navigateur effectuant du sniffing → document actif. | Définir type correct et `X-Content-Type-Options: nosniff` ; isoler l'origine. |
| S55 | XML/XSLT ou aperçu de documents interprété dans une origine privilégiée. | Désactiver les fonctions actives inutiles, isoler l'aperçu et ses ressources. |
| S56 | Message de suppression d'une règle d'analyse statique → rapport HTML ouvert par un développeur. | Échapper les données issues des projets analysés dans les rapports. |
| S57 | Information issue de SNMP, d'un webhook ou d'un journal → page d'administration. | Modéliser ces systèmes externes comme sources non fiables. |
| S58 | CSS généré depuis une entrée → propriété ou URL non contrôlée ; comportement dépendant du navigateur. | Éviter l'injection dans CSS ; liste fermée de propriétés et de valeurs. Ne pas conclure à une XSS sans preuve. |
| S59 | Traduction ou configuration supposée fiable modifiable par un rôle inférieur → panneau d'un administrateur. | Documenter la frontière de confiance ; encoder même les données de configuration modifiables. |
| S60 | Contenu utilisateur → attribut `formaction` ou autre URL omise de l'assainisseur. | Mettre à jour l'assainisseur et limiter balises, attributs et schémas. |
