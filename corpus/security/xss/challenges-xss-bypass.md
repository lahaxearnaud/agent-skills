# Challenges et recherches : combinaisons XSS, filtres et technologies

Recherche du 3 novembre 2026. Les cas ci-dessous sont des **laboratoires intentionnellement vulnérables** et des recherches publiées, pas des vulnérabilités découvertes par nous dans une application. Les liens de labs contiennent les solutions originales ; les résumés servent à construire des règles d'analyse et des tests de régression. Les versions de framework, navigateur, CSP, interaction et configuration propres au challenge conditionnent le résultat. Aucun challenge n'a été exécuté pendant cette recherche.

## 15 challenges et recherches à intégrer

### L01 — Échappement JS insuffisant : antislash

[PortSwigger — chaîne JS, guillemets et antislash](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-double-quotes-encoded-single-quotes-escaped). **Chaîne :** entrée réfléchie → chaîne JavaScript → échappement des apostrophes mais pas des antislashs → rupture possible. **Préconditions :** contexte JS précis, logique d'échappement incomplète et exécution du script. **Revue :** chercher les `replace` artisanaux et suivre l'ordre d'encodage ; préférer une sérialisation adaptée au contexte HTML + JS.

### L02 — Les protections JS ne protègent pas forcément le HTML englobant

[PortSwigger — apostrophe et antislash échappés](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped). **Chaîne :** donnée dans une chaîne JS au sein d'une balise script → fermeture de la balise par le parseur HTML avant l'interprétation JS. **Préconditions :** insertion dans HTML, séquence de fermeture admise et CSP compatible. **Revue :** sécurité de la sérialisation pour les deux parseurs ; ne pas déclarer sûr un encodage JavaScript isolé sans examiner l'HTML.

### L03 — Littéral de gabarit et interpolation

[PortSwigger — template literal](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-template-literal-angle-brackets-single-double-quotes-backslash-backticks-escaped). **Chaîne :** entrée reflétée dans un template literal JS → expression d'interpolation encore interprétable. **Préconditions :** contenu placé dans un littéral JS exécutable et caractères d'interpolation pertinents conservés. **Revue :** ne pas concaténer des données non fiables dans du code JavaScript ; valider un exemple de régression contenant une interpolation non exécutée.

### L04 — JSON réfléchi puis évalué

[PortSwigger — reflected DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-reflected). **Chaîne :** serveur → réponse ressemblant à du JSON avec échappement incomplet → client utilisant `eval`. **Préconditions :** contrôle de la donnée et usage du code client concerné. **Revue :** utiliser un parseur JSON, traiter le résultat comme donnée non fiable et suivre tous les puits DOM ultérieurs.

### L05 — Remplacement partiel de caractères

[PortSwigger — stored DOM XSS](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored). **Chaîne :** commentaire stocké → remplacement de la première occurrence seulement → HTML réinjecté. **Préconditions :** plusieurs occurrences et rendu interprété. **Revue :** repérer les filtrages bricolés à base de `replace` ; ne pas considérer un remplacement global comme un assainisseur HTML complet.

### L06 — Attribut URL valide en HTML, dangereux comme navigation

[PortSwigger — lien stocké](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded). **Chaîne :** valeur fournie → `href` cité → schéma exécutable → clic. **Préconditions :** absence de validation du schéma, interaction et CSP/navigation compatibles. **Revue :** vérifier le parseur et les schémas, puis encoder l'attribut ; l'échappement des guillemets ne valide pas la destination.

### L07 — Attribut d'événement : HTML puis JavaScript

[PortSwigger — `onclick` stocké](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-onclick-event-angle-brackets-double-quotes-html-encoded-single-quotes-backslash-escaped). **Chaîne :** entités HTML → décodage d'attribut → interprétation JS au clic. **Préconditions :** valeur dans un événement inline, données et navigation propres au lab. **Revue :** éviter d'insérer des données dans le code d'un événement ; la protection doit couvrir les deux grammaires.

### L08 — Message inter-fenêtres vers HTML

[PortSwigger — web messages](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages). **Chaîne :** `postMessage` → écouteur → `innerHTML`. **Préconditions :** message accepté, page ouverte, contenu interprété et CSP compatible. **Revue :** contrôler `event.origin` et éventuellement `event.source`, valider la structure et utiliser `textContent` pour le texte.

### L09 — Message vers URL et contrôle par sous-chaîne

[PortSwigger — message et URL JavaScript](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-a-javascript-url). **Chaîne :** message → recherche de `http:` quelque part dans la chaîne → affectation à une URL. **Préconditions :** message acceptée et schéma dangereux réellement navigable. **Revue :** parser et comparer le protocole et l'origine, au lieu de tester une sous-chaîne.

### L10 — Message JSON vers iframe

[PortSwigger — message et JSON.parse](https://portswigger.net/web-security/dom-based/controlling-the-web-message-source/lab-dom-xss-using-web-messages-and-json-parse). **Chaîne :** message externe → `JSON.parse` → champ URL → `iframe.src`. **Préconditions :** message accepté et navigation dangereuse admise. **Revue :** JSON valide ne signifie pas URL sûre ; suivre les champs du message jusqu'au puits.

### L11 — Vue et données textuelles recompilées

[PortSwigger Research — Vue script gadgets](https://portswigger.net/research/evading-defences-using-vuejs-script-gadgets). **Chaîne :** texte inséré par une API initialement textuelle → zone ensuite utilisée comme template Vue → expressions interprétées. **Préconditions :** version et mode de compilation/montage du framework décrits dans la recherche ; ne pas généraliser à toute interpolation Vue. **Revue :** ne pas compiler de contenu non fiable ni monter sur un DOM contenant du contenu utilisateur ; vérifier l'ordre des opérations.

### L12 — AngularJS, expressions et CSP

[PortSwigger — AngularJS sandbox et CSP](https://portswigger.net/web-security/cross-site-scripting/contexts/client-side-template-injection/lab-angular-sandbox-escape-and-csp). **Chaîne :** injection de directives → évaluation par un framework déjà présent → particularités sandbox/CSP. **Préconditions :** version AngularJS, directives et navigateur du lab ; une CSP et un framework ne garantissent pas la sécurité d'un template non fiable. **Revue :** différencier la technologie AngularJS du projet Vue/Twig audité et rechercher les interpréteurs de templates présents.

### L13 — HTML filtré : élément personnalisé et focus

[PortSwigger — balises standards bloquées](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked). **Chaîne :** filtre autorisant des balises personnalisées → événement/focus interprété. **Préconditions :** injection HTML, éléments et attributs non bloqués, comportement du navigateur et CSP. **Revue :** blacklist de balises insuffisante ; employer l'encodage de sortie ou un assainisseur adapté.

### L14 — SVG, animation et URL

[PortSwigger — événements et `href` bloqués](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-event-handlers-and-href-attributes-blocked). **Chaîne :** SVG autorisé → mécanisme d'animation qui affecte une URL → clic. **Préconditions :** éléments SVG et attributs du lab autorisés, interaction et navigateur compatibles. **Revue :** traiter SVG comme contenu actif et limiter les éléments, attributs et schémas ; supprimer seulement `on*` ou `href` ne prouve pas la sûreté.

### L15 — Injection dans la politique CSP elle-même

[PortSwigger — CSP bypass](https://portswigger.net/web-security/cross-site-scripting/content-security-policy/lab-csp-bypass). **Chaîne :** paramètre contrôlé → partie d'un en-tête CSP → directive injectée qui modifie la politique → script exécutable. **Préconditions :** construction vulnérable de l'en-tête et navigateur supportant la directive ; le lab précise des contraintes propres à Chrome. **Revue :** ne pas concaténer d'entrées non fiables dans la politique, inspecter tous les en-têtes effectifs et les directives plus spécifiques.

## Scénarios de test à reprendre

Les mécanismes décrits sont associés aux labs ci-dessus, pas à Cloudflare ou HAProxy automatiquement :

- **SCT-01 :** texte PHP/Twig → élément HTML → compilation ultérieure par Vue ; vérifier que la donnée ne devient jamais une source de template.
- **SCT-02 :** JSON valide → JS client → HTML ; distinguer sérialisation, parsing JSON et encodage du puits final.
- **SCT-03 :** filtre/assainisseur → ajout d'un wrapper → nouveau parse ; vérifier les garanties après la dernière transformation.
- **SCT-04 :** URL fournie → contrôle de chaîne → `href`/`src` ; remplacer par validation d'URL structurée et test des schémas.
- **SCT-05 :** `postMessage` → JSON → iframe ou DOM ; l'origine du message et les champs ont chacun une validation propre.
- **SCT-06 :** entrée → en-tête CSP construit dynamiquement ; vérifier que la valeur ne peut pas créer de directive.
- **SCT-07 :** application Vue SSR + CSP → état sérialisé dans HTML → lecture client ; vérifier les frontières HTML/JS et la cohérence des chemins client/serveur.

Pour chaque scénario, conserver les tests positifs et négatifs, versions, navigateur, CSP effective, prérequis et chemin source → transformation → puits. Les règles candidates ne sont pas des détections validées sans analyse réelle du projet.
