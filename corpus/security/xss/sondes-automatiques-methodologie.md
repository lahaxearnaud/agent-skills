# Scanners XSS : fonctionnement et interprétation des sondes

Recherche documentaire du 3 novembre 2026. Ces outils réalisent des tests dynamiques ; ils complètent l'analyse statique et ne remplacent pas la revue des flux PHP → Twig → Vue → DOM. Aucun scan d'application n'a été réalisé pour ce corpus.

## Sources primaires examinées

| Outil | Source et méthode observée | Limite de l'affirmation |
|---|---|---|
| OWASP ZAP | [Règle XSS réfléchie 40012](https://github.com/zaproxy/zap-extensions/blob/main/addOns/ascanrules/src/main/java/org/zaproxy/zap/extension/ascanrules/CrossSiteScriptingScanRule.java) : chaînes de test, analyseur de contexte HTML, sondes ciblées selon la position, certaines mutations. | C'est la règle réfléchie examinée, pas un inventaire de toutes les règles ZAP. Le fait que la règle émette une alerte ne signifie pas qu'un navigateur a effectivement exécuté du JavaScript. |
| XSStrike | [Configuration](https://github.com/s0md3v/XSStrike/blob/master/core/config.py) : marqueur `v3dm0s`, fragments de fuzz, familles de balises et événements. [Documentation d'utilisation](https://github.com/s0md3v/XSStrike/wiki/Usage) : fuzzing et modes de crawl. | Les chaînes fixes et celles générées ont des rôles différents ; leur application dépend de la version et des options. Ne pas reprendre comme garantie indépendante l'affirmation commerciale d'un payload « garanti ». |
| Dalfox | [Documentation des payloads](https://dalfox.hahwul.com/guide/payloads/) : sélection par contexte, familles HTML, JS, URL, et marqueurs de vérification ; [modèle de détection](https://dalfox.hahwul.com/getting-started/quick-start/). | Les catégories et niveaux de preuve sont ceux décrits par l'outil. Un placement considéré exécutable par son parseur ou un callback n'est pas automatiquement une observation directe d'exécution JS dans le navigateur de la victime. |
| Nuclei | [Template DAST XSS réfléchie](https://github.com/projectdiscovery/nuclei-templates/blob/main/dast/vulnerabilities/xss/reflected-xss.yaml) : motif avec entier aléatoire, fuzzing en postfixe des parties corps, query et chemin ; recherche de réflexion en réponse HTML. | Ce template cherche une réflexion de caractères, pas l'exécution effective. Tous les formats, paramètres cachés et parcours authentifiés ne sont pas nécessairement couverts. Les templates et moteurs évoluent. |

Ces liens pointent vers des branches/documentations évolutives ; ils ne sont pas des références à un commit figé. Pour une future étude reproductible, relever les versions et commits au moment d'exécuter les outils.

## Signaux et niveau de preuve

1. **Marqueur réfléchi** : une chaîne unique réapparaît dans une réponse ou dans le DOM. Cela établit un flux observable mais peut être normal, même si la chaîne contient des caractères spéciaux correctement échappés.
2. **Caractères non neutralisés ou modifiés** : comparer entrée, corps HTTP et DOM ; identifier si les délimiteurs sont actifs dans le contexte. La présence brute de caractères ne démontre pas leur interprétation en code.
3. **Contexte atteignable** : préciser corps HTML, attribut cité, URL, script, commentaire, CSS, `srcdoc`, ou réinsertion DOM. Un analyseur approximatif peut mal interpréter les imbrications ou réparations du navigateur.
4. **Élément ou attribut actif interprété par le navigateur** : enregistrer le DOM, l'origine, le type de document, le chargement et les violations CSP. La présence d'un attribut ne démontre pas que son événement s'est déclenché.
5. **Exécution observée** : observer dans un navigateur de test un effet local inoffensif et reproductible, puis expliquer la source et le chemin. Documenter le contexte, le rôle requis, la CSP effective, les interactions et le navigateur. La réussite d'une sonde ne prouve pas que toutes ses variantes fonctionnent.
6. **XSS stockée ou aveugle** : relier précisément l'écriture et la lecture ultérieure. Un rappel réseau démontre une requête reçue mais doit être corrélé à la source et au contexte ; certaines charges, préchargements ou outils d'inspection peuvent générer des requêtes sans exécution JavaScript. Distinguer réception HTTP, exécution effective et utilisateur affecté.

## Méthode de validation adaptée au propre code

- Dresser l'inventaire des paramètres réellement atteignables : query, corps de formulaire/JSON, chemin, données enregistrées, champs de composants, données API, fichiers et messages. Les scanners n'ont connaissance que des routes, sessions et actions qu'ils ont pu découvrir ou qui leur ont été fournies.
- Préparer des tests contrôlés et reproductibles, avec données et comptes de test, et comparer une réponse de référence à la réponse contenant un marqueur unique. Mesurer les effets des encodages, des reconstructions côté client et des droits de lecture.
- Commencer par les marqueurs non exécutables, puis choisir des cas adaptés au contexte identifié. Les entrées [P01–P28](payloads-scanners.md) ne sont pas interchangeables : par exemple, une charge HTML ne prouve rien si elle est affichée dans un nœud texte ou dans un JSON non interprété.
- Pour Vue, tester la lecture de `route`, d'une API et des props jusqu'à `v-html` ; pour Twig, suivre le rendu initial et la réutilisation des données échappées par JS. Vérifier le cas de données stockées puis affichées à un autre rôle.
- Pour chaque candidat, joindre requête et réponse expurgées de secrets, emplacement de la réflexion, transformations, contexte de parsing, preuve d'exécution éventuelle, CSP appliquée et provenance de la sonde. Une absence de marqueur n'exclut pas un chemin asynchrone, stocké ou inaccessible au robot.
- Associer au constat dynamique le flux statique et un correctif adapté, puis créer un test de non-régression positif et un cas négatif légitime. Ne pas concevoir une protection en production comme une liste noire des seuls payloads connus : vérifier la sûreté du contexte final.

## Relations avec le corpus existant

- [Sondes et charges documentées](payloads-scanners.md), [CSV](payloads-scanners.csv).
- [Scénarios hypothétiques](scenarios.md) : situations de code et conditions de déclenchement.
- [Analyse statique JS, Vue et Twig](analyse-statique-vue-js-twig.md) : propagation, frontières de confiance et faux positifs.
- [Bonnes pratiques](bonnes-pratiques-securite.md) : remédiations et limites de la CSP.
