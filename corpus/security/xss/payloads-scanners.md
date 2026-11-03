# Payloads et marqueurs observés dans les scanners XSS

Recherche du 3 novembre 2026. Extraits limités et adaptés pour comprendre les tests : consulter les sources pour les jeux complets, leurs versions et licences. **Les entrées synthétiques sont identifiées ; les gabarits et fragments ont besoin de leur contexte.** Une charge qui se reflète ne prouve pas qu’elle est exécutable. Aucune sonde n’a été envoyée à une application.

Le tableau inclut **28 entrées** : sondes de réflexion, charges de confirmation et variantes pédagogiques. Chaque ligne contient les prérequis, les limites et la provenance ; le [CSV](payloads-scanners.csv) fournit les chaînes séparées pour exploitation locale. `{{first}}` est un placeholder de Nuclei, pas une chaîne à confondre avec du Twig. Les exemples `alert`/`prompt` nécessitent un observateur navigateur ; une recherche textuelle dans la réponse n’établit pas leur exécution.

### P01 — marqueur non exécutable

- Charge : `v3dm0s`
- Origine : XSStrike ; exact ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : réflexion brute. Aucune exécution JavaScript ; plusieurs paramètres peuvent renvoyer le marqueur.

### P02 — caractères et marqueur

- Charge : `'"><{{first}}>`
- Origine : Nuclei ; gabarit exact ; [source](https://github.com/projectdiscovery/nuclei-templates/blob/main/dast/vulnerabilities/xss/reflected-xss.yaml).
- Contexte : réflexion dans HTML. Le modèle remplace {{first}} par un entier aléatoire ; test de réflexion, pas preuve de XSS.

### P03 — script inline

- Charge : `<scrIpt>alert(1);</scRipt>`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : contenu HTML. Le navigateur doit interpréter la balise et la CSP doit autoriser son exécution.

### P04 — gestionnaire erreur

- Charge : `<img src=x onerror=prompt()>`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : contenu HTML. Chargement image en échec et gestionnaire inline permis par CSP.

### P05 — événement / console

- Charge : `<img src=x onerror=console.log(1);>`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : contenu HTML. Événement déclenché et console observée ; utile sans boîte de dialogue.

### P06 — SVG inline

- Charge : `<svg onload=alert(1)>`
- Origine : ZAP / Dalfox ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : contenu HTML. Élément SVG interprété et gestionnaire autorisé ; dépend du contexte et de la CSP.

### P07 — événement au survol

- Charge : `<b onMouseOver=alert(1);>test</b>`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : contenu HTML. Survol nécessaire et gestionnaire autorisé.

### P08 — attributs et interaction

- Charge : `accesskey='x' onclick='alert(1)' b`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : injection dans une balise. Nécessite un contexte permettant d’ajouter ces attributs et une interaction valide.

### P09 — nom de balise / attribut

- Charge : `button onclick='alert(1)'/`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : injection dans une balise. Fragment incomplet ; dépend du contenu qui entoure la donnée.

### P10 — instruction JS

- Charge : `;alert(1)`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : attribut événement existant. Fragment dépendant du code encadrant et de l’autorisation CSP.

### P11 — schéma URL

- Charge : `javascript:alert(1);`
- Origine : ZAP ; exact ; [source](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java).
- Contexte : attribut URL. Dépend du type d’élément, de la navigation/interaction et de la CSP.

### P12 — sortie attribut

- Charge : `'><img src=x onerror=alert(1)>`
- Origine : Dalfox ; exact ; [source](https://dalfox.hahwul.com/guide/payloads/).
- Contexte : attribut cité par apostrophes. Fermeture d’attribut et de balise nécessaire ; erreur image et CSP permissive.

### P13 — sortie de chaîne JS

- Charge : `";alert(1);//`
- Origine : Dalfox ; exact ; [source](https://dalfox.hahwul.com/guide/payloads/).
- Contexte : script inline. Dépend de la chaîne englobante et de la syntaxe générée ; CSP pertinente.

### P14 — gestionnaire événement

- Charge : `onmouseover=alert(1)`
- Origine : Dalfox ; exact ; [source](https://dalfox.hahwul.com/guide/payloads/).
- Contexte : attribut ou balise. Fragment ; une insertion syntaxiquement valide et le survol sont nécessaires.

### P15 — DOM clobbering

- Charge : `<img id=x>`
- Origine : Dalfox ; exact ; [source](https://dalfox.hahwul.com/guide/payloads/).
- Contexte : injection HTML. Ce marqueur ne démontre pas une XSS : il faut prouver une collision et un gadget de code.

### P16 — sonde de filtre

- Charge : `<test`
- Origine : XSStrike ; exact ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : réflexion HTML. Fragment syntaxique incomplet ; sa réflexion ne prouve pas une injection exécutable.

### P17 — sonde de filtre

- Charge : `<test x=y`
- Origine : XSStrike ; exact ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : réflexion HTML. Fragment incomplet visant la transformation/filtrage des caractères.

### P18 — sonde attribut

- Charge : `<test sRc=xxx`
- Origine : XSStrike ; exact ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : réflexion HTML. Sonde de filtre non associée à une preuve d’exécution.

### P19 — sonde balise SVG

- Charge : `<svg x=y>`
- Origine : XSStrike ; exact ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : réflexion HTML. Détecte éventuellement une balise conservée ; pas de code JavaScript dans cette sonde.

### P20 — événement details

- Charge : `<details open oNToggle=confi\u0072m()>`
- Origine : XSStrike ; exact code source ; [source](https://github.com/s0md3v/XSStrike/blob/master/core/config.py).
- Contexte : HTML interprété. Chaîne telle que présentée dans le code source Python ; vérifier la valeur après évaluation et le navigateur.

### P21 — marqueur unique

- Charge : `XSSCANARY7Q2`
- Origine : Synthétique ; créé pour corpus.
- Contexte : tous contextes. Varier le marqueur par test ; seul le retour observable est établi.

### P22 — caractères et échappement

- Charge : `XSSCANARY7Q2<>&'"`
- Origine : Synthétique ; créé pour corpus.
- Contexte : HTML ou attribut. Comparer caractères envoyés, réponse et DOM ; une réflexion brute n’établit pas l’exécution.

### P23 — événement erreur

- Charge : `<img src=x onerror=alert(1)>`
- Origine : Synthétique ; variante pédagogique.
- Contexte : HTML interprété. Doit produire un événement dans un document où la CSP l’autorise ; innerHTML ne se réduit pas aux balises script.

### P24 — fermeture script

- Charge : `</script><script>alert(1)</script>`
- Origine : Synthétique ; variante pédagogique.
- Contexte : script dans HTML. Suppose que la séquence atteigne littéralement le parseur HTML ; CSP et insertion comptent.

### P25 — schéma URL

- Charge : `javascript:alert(1)`
- Origine : Synthétique ; variante pédagogique.
- Contexte : lien ou navigation. Schéma doit être autorisé et action de navigation pertinente ; blocage possible par CSP.

### P26 — entités HTML

- Charge : `&lt;img src=x onerror=alert(1)&gt;`
- Origine : Synthétique ; variante pédagogique.
- Contexte : pipeline avec décodage. Devient pertinent seulement si une transformation ultérieure recrée du HTML actif.

### P27 — Unicode / normalisation

- Charge : `＜svg onload=alert(1)＞`
- Origine : Synthétique ; variante pédagogique.
- Contexte : pipeline normalisant NFKC. Les signes pleine chasse ne sont pas des délimiteurs HTML standard sans transformation effective.

### P28 — encodage URL

- Charge : `XSSCANARY7Q2%3C%3E`
- Origine : Synthétique ; variante pédagogique.
- Contexte : paramètre URL. Résultat dépend des couches et du nombre de décodages ; attention à un encodage additionnel par le client.

