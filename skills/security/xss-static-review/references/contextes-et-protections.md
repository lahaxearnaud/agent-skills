# Contextes, assainissement et protections

## Décision par destination

| Destination finale | Vérification et correction indicative |
|---|---|
| Texte HTML / attribut ordinaire cité | Auto-échappement HTML effectif ou encodeur HTML correct, guillemets maintenus ; ne pas utiliser `raw` sur une donnée non fiable. |
| Attribut URL / redirection | Parser, valider les schémas et, si nécessaire, origine/hôte/chemin, puis encoder pour l'attribut ; distinguer URL relatives, destination de navigation et chargement de script. |
| JavaScript dans HTML | Éviter la génération de code ; préférer un transport JSON séparé. Sinon vérifier la sérialisation JS **et** l'imbrication dans le document HTML, notamment les délimiteurs de script. Un simple échappement HTML ne suffit pas. |
| HTML riche / SVG | Déterminer l'assainisseur, sa version, sa configuration, le contexte accepté et toutes les transformations après assainissement. Favoriser la politique minimale, ou l'isolement si du contenu actif est nécessaire. |
| Vue | Interpolation texte normalement échappée ; `v-html` et render functions HTML sont des puits. `:href` demande validation URL. Ne pas compiler un template contrôlé ni monter sur du DOM préexistant non fiable. |
| Document autonome / `srcdoc` | Déterminer origine, type MIME, disposition, sandbox, CSP et navigation. Un SVG comme image et un SVG ouvert comme document ne sont pas équivalents. |

## Garanties conditionnelles

- **Twig :** confirmer stratégie d'autoescape du template, blocs d'exception, macros/includes, `raw`, `Markup`, déclarations `is_safe` et `pre_escape` des filtres personnalisés. `is_safe` est une déclaration à vérifier, non une preuve. L'auto-échappement HTML ne valide pas le schéma URL.
- **PHP :** `htmlspecialchars` avec drapeaux et charset appropriés protège certains contextes HTML, pas tous les contextes JS, URL, CSS ou HTML non cité. Prendre en compte la version PHP et le contexte ; ne pas recommander une concaténation de code.
- **Assainisseurs :** pour `DOMPurify`, Symfony HtmlSanitizer ou équivalent, vérifier version, options, allowlist, hooks, type d'entrée et sortie. Évaluer `sanitize` après la dernière transformation qui produit du HTML ; une concaténation non fiable après assainissement n'est pas couverte. Ne pas supposer qu'une configuration permissive est sûre. Pour un avis CVE, vérifier la plage, l'utilisation et le correctif ; la présence de la dépendance seule ne prouve pas le flux.
- **URL :** une recherche de sous-chaîne `http` ou un encodage HTML n'est pas une validation de schéma. Comparer la valeur réellement utilisée après parsing ; une URL HTTPS valide peut conduire à un site non fiable.
- **CSP :** inspecter headers/config et valeur réellement applicable si visible ; distinguer `Report-Only`, `script-src`, `script-src-elem`, `script-src-attr`, nonce/hash, `unsafe-inline`, `unsafe-eval` et `strict-dynamic`. Plusieurs politiques sont cumulatives. Une CSP peut bloquer des vecteurs sans corriger l'injection ; du code injecté dans un script légitime doté d'un nonce peut être autorisé. Si l'en-tête final est inconnu, ne pas le deviner.
- **Trusted Types :** examiner la directive effective, les navigateurs et les politiques `createPolicy`/default. Une politique qui renvoie la chaîne telle quelle ne démontre pas la sûreté ; les puits couverts et le support sont limités.
- **Cookies et session :** `HttpOnly` limite l'accès direct à certains cookies, sans empêcher automatiquement une action authentifiée. La portée dépend de l'origine et des contrôles réels. Ne pas affirmer un vol de cookie si les propriétés sont inconnues.
- **WAF/proxy :** ne prouve ni sécurité ni vulnérabilité. Les règles, normalisations, exceptions, chemins d'origine et limites de corps sont souvent hors dépôt. Documenter l'incertitude sans suggérer de sonder l'application.

Sources : [Twig escape](https://twig.symfony.com/doc/3.x/filters/escape.html), [sécurité Vue](https://vuejs.org/guide/best-practices/security), [Symfony HtmlSanitizer](https://symfony.com/doc/current/html_sanitizer.html), [OWASP XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [MDN CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP).
