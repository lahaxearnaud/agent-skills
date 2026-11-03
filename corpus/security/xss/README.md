# Corpus XSS pour préparer une future skill d'analyse de code

Recherche effectuée le 3 novembre 2026. Livrable de recherche préliminaire :

- [Index de 157 avis publiés](cas-publies.md) et [même index en CSV](cas-publies.csv) : identifiants GHSA distincts et sources directes. Ce sont des références à qualifier, **pas 157 analyses exhaustives ni nécessairement 157 vulnérabilités indépendantes**.
- [60 scénarios hypothétiques](scenarios.md) : sources, destinations, conditions et pistes de correction ; certains sont inspirés par les familles de PayloadsAllTheThings et d'autres par les mécanismes généraux de XSS. Aucun n'est présenté comme un incident réellement observé.
- [Analyses, CSP et méthode](analyse.md) : six cas étudiés, implications CSP, règles de revue et limites.

## Approfondissement JavaScript, Vue.js et Twig

- [39 références GHSA supplémentaires](nouveaux-cas-vue-js-twig.md), également disponibles en [CSV](nouveaux-cas-vue-js-twig.csv). Certaines sont connexes aux recherches et ne concernent pas directement Vue.
- [Méthodologie d’analyse statique](analyse-statique-vue-js-twig.md) : neuf cas, cartographie des flux, exemples positifs et négatifs, et limites de couverture des outils.

## Référentiel de bonnes pratiques

- [Bonnes pratiques de sécurité par technologie](bonnes-pratiques-securite.md) : recommandations sourcées, conditions, limites et correspondances pour la future analyse statique.

## Sondes utilisées par des scanners XSS

- [28 sondes et charges documentées](payloads-scanners.md) avec [CSV](payloads-scanners.csv) : provenance, contexte et conditions.
- [Méthode et niveaux de preuve](sondes-automatiques-methodologie.md) : ZAP, XSStrike, Nuclei et Dalfox ; distinction entre réflexion et exécution.

## Normes et cas avancés

- [Normes, documentation de test et dix analyses de cas](normes-references-cas-avances.md) : parsing HTML et URL, RFC, CSP, Trusted Types, assainisseurs et bundlers. Huit avis sont nouveaux ; un autre est contesté par ses mainteneurs ; un cas Twig était déjà indexé.

## Challenges et protections WAF

- [15 challenges et recherches XSS](challenges-xss-bypass.md) : mécanismes, conditions et pistes d’analyse.
- [WAF Cloudflare et HAProxy](waf-cloudflare-haproxy.md) : 12 familles de divergences, configuration et méthode de validation.

## Typologie et portée

- [XSS réfléchie, stockée et self-XSS](types-xss-reflechie-stockee-self.md) : distinctions, exemples et grille de validation inter-comptes.

## Nouveaux cas Web toutes technologies

- [20 cas et pistes de détection](cas-web-impactants.md) : identité, administration, documents actifs, frameworks et transports, dont un rapport HackerOne partiellement accessible.
- [95 références GHSA supplémentaires à qualifier](cas-web-elargis-index.md), également en [CSV](cas-web-elargis-index.csv). Il s’agit de résultats de recherche dédupliqués par identifiant, pas de 95 analyses complètes.

Les fichiers `recherche-*.json` contiennent les résultats bruts et les requêtes pour traçabilité ; leur contenu provient de l'index de recherche et peut être tronqué ou périmé. L'index est construit à partir de résultats de recherche d'avis GitHub et de listes d'avis de dépôts, en filtrant les titres explicitement XSS/cross-site scripting puis en dédupliquant par GHSA et en excluant les intitulés « Duplicate Advisory » connus. Deux GHSA différents peuvent néanmoins représenter le même incident, et une liste peut décrire une hypothèse ou un rapport incomplet. Les résultats de recherche ne prouvent ni exploitabilité actuelle ni statut de correction.

**Mode d'emploi :** commencer par `analyse.md` et `scenarios.md`, puis sélectionner dans `cas-publies.csv` les avis pertinents ; lire l'avis complet et, si possible, le correctif avant de créer une règle. Les extraits de l'index ne permettent pas à eux seuls de conclure. Ne pas confondre une source de données avec une preuve de contrôle par un attaquant. Pour chaque cas retenu, relever version, rôle, prérequis, source, transformations, puits, contexte, CSP, correctif et preuve ; marquer explicitement « inconnu » quand la source ne précise pas.

Une première skill d’analyse statique est disponible dans `../../../skills/security/xss-static-review/`. Aucune règle automatique ni exécution d’application ne fait partie de cette première version. Les sources évoluent et les pages accessibles via index ne constituent pas une recherche exhaustive du Web ou des plateformes de bug bounty.
