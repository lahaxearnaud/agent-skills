# Analyse et exploitation défensive du corpus

## Six cas publiés examinés

### 1. Symfony WebProfiler : journal vers HTML — CVE-2026-45072

[GHSA-hmr5-2xcr-v8pp](https://github.com/symfony/symfony/security/advisories/GHSA-hmr5-2xcr-v8pp). Dans le profiler de développement, `file_excerpt` traitait les fichiers PHP avec coloration échappante, mais insérait directement les lignes de fichiers non PHP dans des éléments `code`. Il fallait pouvoir écrire dans un fichier du projet, par exemple un log de développement, puis qu'un développeur ouvre cet extrait dans le profiler. Le correctif échappe les lignes non PHP. Indice de revue : branches de rendu de fichiers, provenance des logs, déclarations de sortie HTML sûre. Le rapport qualifie le profiler d'interface de développement ; ne pas extrapoler à toute installation de production.

### 2. Sylius : mêmes données, plusieurs puits — CVE-2026-31823

[GHSA-mx4q-xxc9-pf5q](https://github.com/Sylius/Sylius/security/advisories/GHSA-mx4q-xxc9-pf5q). Des noms d'entités contrôlés par un administrateur sont affichés via `|raw` dans les fils d'Ariane et par interpolation HTML dans les composants d'administration et d'autocomplétion. L'impact nécessite le droit d'écrire les noms et la consultation des pages affectées. Il s'agit de plusieurs puits associés à un même avis, pas de trois vulnérabilités indépendantes automatiquement. Le correctif supprime l'insertion brute ou échappe les valeurs à l'endroit approprié.

### 3. Twig extras : déclaration de confiance trop large — CVE-2026-46637

[GHSA-jv8m-2544-3pg3](https://github.com/twigphp/Twig/security/advisories/GHSA-jv8m-2544-3pg3). Des filtres de packages extras étaient déclarés sûrs dans tous les contextes, alors que leurs sorties ne garantissaient pas cette propriété ; l'avis décrit notamment des interactions entre conversion HTML/Markdown et décodage d'entités. Pour une application donnée, il faut vérifier version, filtre utilisé, donnée contrôlée et contexte final. Une chaîne sûre comme fragment HTML n'est pas nécessairement sûre dans un script, une URL ou un attribut.

### 4. Symfony HtmlSanitizer : attributs URL oubliés — CVE-2026-45753

[GHSA-hhg7-c65m-h7ff](https://github.com/symfony/symfony/security/advisories/GHSA-hhg7-c65m-h7ff). Certains attributs contenant des URL ne passaient pas par le contrôle d'URL. Une exploitation exige une configuration qui autorise le couple balise/attribut concerné, une donnée contrôlée, puis une utilisation permettant au navigateur d'interpréter l'URL. La présence d'un assainisseur ne démontre donc pas sa couverture de tous les attributs ni qu'une URL échappée HTML est sans danger. Vérifier correctif et configuration réellement déployée.

### 5. AVideo : JSON valide, puis injection DOM — CVE-2026-33035

[GHSA-wfq5-qgqp-hvhv](https://github.com/WWBN/AVideo/security/advisories/GHSA-wfq5-qgqp-hvhv). L'avis décrit une entrée de paramètre URL passée par `json_encode()` puis utilisée dans une fonction JS qui produit du HTML via `innerHTML`. La sérialisation a une fonction de transport ; elle ne rend pas le contenu sûr pour un futur puits HTML. Vérifier la chaîne complète PHP → JavaScript → DOM. `textContent` convient lorsque seul du texte est nécessaire.

### 6. Symfony UX Icons : SVG déclaré sûr — CVE-2026-55877

[GHSA-6v8j-33hc-mv84](https://github.com/advisories/GHSA-6v8j-33hc-mv84) et [avis Symfony](https://symfony.com/blog/cve-2026-55877-xss-in-symfony-ux-icons-via-unsanitized-svg-content-in-local-files-and-iconify-on-demand-responses). Le contenu SVG issu de fichiers locaux ou de réponses Iconify pouvait être intégré comme HTML sûr sans assainissement suffisant. L'attaque suppose le contrôle d'une de ces sources ou une compromission correspondante, ainsi que le rendu du SVG vulnérable. Vérifier les versions et l'origine effective des icônes, pas seulement la présence de `ux_icon()`.

## CSP : impact dépendant de la politique effective

La référence utilisée ici est la [documentation CSP de MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) ; voir aussi [`script-src-elem`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src-elem) et [`script-src-attr`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src-attr).

| Politique ou condition | Conséquence à examiner |
|---|---|
| Pas de politique effective limitant les scripts | Balisage actif, gestionnaires et URL script peuvent s'exécuter selon le contexte et le navigateur. |
| `script-src` restrictif, sans autorisation inline | Les scripts inline, gestionnaires inline et URL `javascript:` sont généralement bloqués, sous réserve des directives plus spécifiques et du navigateur. L'injection HTML reste un défaut. |
| `'unsafe-inline'` | Peut autoriser le code inline ; son effet dépend notamment de la présence de nonce/hash et du support du navigateur. Ne pas conclure à partir de ce seul mot. |
| Nonce ou hash correctement appliqué | Bloque de nombreux scripts injectés sans autorisation correspondante ; ne protège pas une donnée injectée dans le corps d'un script déjà autorisé. |
| `'strict-dynamic'` | La confiance peut se propager à des scripts chargés par un script autorisé ; auditer les chargeurs et les URL qu'ils construisent. |
| `'unsafe-eval'` | Autorise certaines évaluations de chaînes lorsque les autres conditions CSP le permettent ; un puits `eval` reste dangereux. |
| `script-src-elem` / `script-src-attr` | Les règles peuvent différer entre balises script et gestionnaires d'événement ; examiner les directives effectives et leur repli. |
| CSP en `Report-Only` | Émet des rapports sans appliquer cette politique ; vérifier s'il existe aussi une politique appliquée séparée. |
| `connect-src`, `img-src`, `form-action` | Restreignent respectivement certaines communications, chargements d'images ou destinations de formulaires ; aucune directive unique n'empêche tous les impacts d'une XSS. |
| Plusieurs politiques CSP | Elles s'appliquent conjointement ; examiner les en-têtes de la réponse finale, du document et les politiques héritées pertinentes. |
| `frame-ancestors` / sandbox | Agissent sur l'encadrement ou les privilèges du document ; ne constituent pas une protection générale contre toute XSS dans la page principale. |

Même lorsque JavaScript est bloqué, l'injection HTML peut modifier l'interface, des liens ou des formulaires ; l'impact exact dépend des contrôles actifs. Une CSP stricte est une défense en profondeur, pas une preuve que l'injection est corrigée. `HttpOnly` empêche la lecture directe d'un cookie par JavaScript, mais n'empêche pas automatiquement les requêtes authentifiées effectuées dans la session ; SameSite, CORS et CSRF doivent être évalués séparément. Trusted Types peut réduire certains puits DOM dans les navigateurs et configurations qui l'imposent, mais la sûreté dépend des politiques Trusted Types elles-mêmes.

## Procédure pour la future skill

1. Identifier les entrées : query, chemin, corps, cookie, en-têtes, messages, base, fichiers, traductions modifiables, flux distants et logs. Prouver qui les contrôle, même indirectement.
2. Suivre les transformations et changements de confiance : décodages, normalisation Unicode, traduction, Markdown, JSON, concaténation, HTML assaini puis modifié. L'échappement peut être défait ou devenir inadapté au contexte suivant.
3. Identifier le puits final et son contexte réel : texte HTML, attribut cité ou non, URL, script inline, chaîne JS, CSS, HTML DOM, SVG, `srcdoc`, réponse ou fichier autonome.
4. Vérifier les protections pertinentes à **chaque** frontière de parseur : autoescape Twig, `raw`/`Markup`/`is_safe`, validation de schéma URL, assainisseur et configuration, sérialisation JS, API DOM, version des bibliothèques. Une expression repérée par recherche est un candidat, pas une preuve.
5. Déterminer prérequis et impact : acteur, droits, interaction victime, origine, version, CSP appliquée, navigateur, cookies et privilèges. Ne pas inférer que toute injection de HTML exécute du JS.
6. Proposer la correction minimale adaptée au puits : `textContent`, échappement contextuel, suppression de `raw`, validation d'URL, assainissement après dernière transformation, isolement des fichiers actifs ou mise à jour. Ajouter des tests ciblés de non-régression et au moins un cas légitime.
7. Produire des constats avec chemin source → transformations → puits, preuve de contrôle, contexte et limites ; distinguer constat vérifié, hypothèse et faux positif.

### Recherches initiales dans un dépôt PHP/Twig

Rechercher `|raw`, `autoescape false`, `Twig\\Markup`, `is_safe`, `htmlspecialchars_decode`, `html_entity_decode`, `new Response`, `innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`, `srcdoc`, `eval`, les noms de paramètres JSONP et les constructions d'URL. Ces termes servent à orienter la lecture, pas à classer automatiquement comme vulnérable. Examiner aussi les paramètres de sanitisation, le code tiers, les vues d'erreur, les pages d'administration, les résultats de recherche et les rapports.

### Évaluation de la future skill

Constituer des jeux positifs et négatifs isolés, y compris `raw` appliqué à une constante sûre, URL HTTPS validée, `textContent`, sortie assainie non modifiée, CSP stricte avec injection dans un script nonce, et sérialisation JSON suivie de `innerHTML`. Mesurer rappel et faux positifs par contexte, et vérifier que chaque constat cite une source contrôlable et un puits atteignable. Les scénarios sont des plans de test, pas des tests exécutés.

## Sources générales

- [PayloadsAllTheThings — XSS](https://swisskyrepo.github.io/PayloadsAllTheThings/XSS%20Injection/), [contournement de filtres](https://swisskyrepo.github.io/PayloadsAllTheThings/XSS%20Injection/1%20-%20XSS%20Filter%20Bypass/) et [CSP](https://swisskyrepo.github.io/PayloadsAllTheThings/XSS%20Injection/4%20-%20CSP%20Bypass/). Certains exemples sont historiques ou dépendent de versions et de transformations particulières ; ne pas supposer leur fonctionnement sur un navigateur actuel.
- [Twig : stratégies d'échappement](https://twig.symfony.com/doc/3.x/filters/escape.html).
- [OWASP : prévention des XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
- [MDN : mise en place d'une CSP](https://developer.mozilla.org/en-US/docs/Web/Security/Practical_implementation_guides/CSP).
