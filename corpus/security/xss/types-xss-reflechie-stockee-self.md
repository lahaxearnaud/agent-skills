# XSS réfléchie, stockée et self-XSS : distinction et exemples

Ajout du 3 novembre 2026. Les exemples synthétiques ne décrivent pas un incident réel ; une exécution dépend aussi du navigateur, du contexte et de la CSP. Les avis cités décrivent des cas publiés.

## Les distinctions ne portent pas toutes sur le même axe

| Notion | Question | Exemple |
|---|---|---|
| Réfléchie | Comment l'entrée est-elle restituée ? | Un paramètre d'une requête est réutilisé dans la réponse immédiate. |
| Stockée | La donnée est-elle conservée pour une lecture ultérieure ? | Un commentaire enregistré est affiché à d'autres utilisateurs. |
| Self-XSS, sens bug bounty | Qui peut provoquer l'exécution dans la session de qui ? | Un utilisateur peut injecter dans un champ qui n'est visible que par son propre compte, sans chemin établi vers une victime. |
| Self-XSS, sens ingénierie sociale | Quelle action directe la victime effectue-t-elle ? | Une personne est trompée pour coller et exécuter du code dans sa propre console. |
| DOM-based | Où se trouve le puits interprétant la donnée ? | Un script lit `location.hash` puis affecte la valeur à `innerHTML`. |

Ces catégories peuvent se recouper : une donnée stockée peut aboutir à une XSS DOM ; une réflexion dans la propre session peut être qualifiée de self-XSS si personne d'autre ne peut être atteint. Le seul fait qu'une charge ait été saisie par la personne qui teste ne prouve pas que la faille est limitée à cette personne. Sources : [MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/XSS), [PortSwigger — XSS DOM](https://portswigger.net/web-security/cross-site-scripting/dom-based), [Chrome — self-XSS console](https://developer.chrome.com/blog/self-xss?hl=en), [HackerOne — self-exploitation](https://docs.hackerone.com/en/articles/8494488-core-ineligible-findings).

## 1. XSS réfléchie

**Scénario synthétique :** un contrôleur Symfony lit un paramètre `q` et le transmet à une vue Twig. Si la vue l'insère en HTML avec `|raw`, une donnée contenue dans la requête peut être interprétée par le navigateur lors de la réponse immédiate. Un tiers peut être touché si l'attaquant peut lui faire ouvrir une requête contenant cette donnée et si l'exécution est possible dans son contexte.

```twig
{# Candidat vulnérable si q est contrôlable et restitué comme HTML. #}
<p>Recherche : {{ q|raw }}</p>
{# Pour afficher uniquement du texte, laisser l'auto-échappement actif. #}
<p>Recherche : {{ q }}</p>
```

**Cas publiés :** [AVideo — GHSA-wfq5-qgqp-hvhv](https://github.com/WWBN/AVideo/security/advisories/GHSA-wfq5-qgqp-hvhv), paramètre d'URL → JSON → `innerHTML` ; [lab PortSwigger — chaîne JavaScript](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-single-quote-backslash-escaped), exemple de parseurs HTML et JS imbriqués. Le premier est un avis produit ; le second est un environnement volontairement vulnérable.

**À vérifier :** contrôle du paramètre, transport possible vers la victime, contexte de sortie, transformations, CSP et interaction. Une réponse qui contient un marqueur reflété ne prouve pas à elle seule l'exécution.

## 2. XSS stockée

**Scénario synthétique :** un utilisateur enregistre une description ; plus tard, un administrateur consulte une page Vue qui transmet cette description à `v-html` sans assainissement approprié. La persistance et la lecture dans une autre session constituent deux étapes séparées ; le rôle d'écriture et le rôle de lecture doivent être établis.

```vue
<template>
  <!-- Candidat si description vient d'une source contrôlable sans assainissement HTML adapté. -->
  <div v-html="description"></div>
  <!-- Variante textuelle lorsque le produit n'a pas besoin de HTML riche. -->
  <div>{{ description }}</div>
</template>
```

**Cas publiés :** [Chamilo — GHSA-ppw9-gf4r-5c39](https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-ppw9-gf4r-5c39), message social et `v-html` ; [Sylius — GHSA-mx4q-xxc9-pf5q](https://github.com/Sylius/Sylius/security/advisories/GHSA-mx4q-xxc9-pf5q), noms d'entités et plusieurs rendus HTML. Les conditions d'accès et versions sont celles des avis, pas une propriété générale des frameworks.

**À vérifier :** qui écrit, où la donnée est conservée, quels écrans ou destinataires la lisent, si elle est transformée après assainissement, et si une victime disposant de droits différents peut réellement la consulter. Une XSS stockée peut ne concerner qu'un seul compte : la persistance seule ne démontre pas une attaque contre un tiers.

## 3. Self-XSS : portée limitée à son propre contexte

**Scénario synthétique :** une application stocke un champ de préférences dont l'édition et l'affichage sont strictement limités au propriétaire ; ce champ est inséré avec `innerHTML`. Si aucun autre utilisateur ou système ne peut voir ni se voir imposer cette valeur, l'exécution démontrée est limitée à la session du compte qui l'a saisie. Le puits reste une mauvaise pratique de code et devrait être corrigé, même lorsque l'impact inter-compte n'est pas démontré.

**Autre sens courant :** une personne est amenée à coller du JavaScript dans les outils développeur de son navigateur. C'est un scénario d'ingénierie sociale distinct d'une démonstration montrant qu'une entrée applicative atteint un puits. [Chrome explique ce cas](https://developer.chrome.com/blog/self-xss?hl=en).

**Attention à la classification :** documenter les hypothèses avant de conclure « self » :

1. **Lien partageable :** si une valeur reflétée dans l'URL peut être envoyée à une autre personne, vérifier son exécution dans sa session ; ce n'est pas nécessairement une self-XSS.
2. **Contenu partagé ou réutilisé :** export/import, partage, modération, support, aperçu ou compte administrateur peuvent faire passer une donnée privée vers un autre lecteur. Prouver l'existence du chemin avant de le déclarer exploitable.
3. **Écriture déclenchée par un tiers :** une autre faille, par exemple un changement d'état non autorisé, peut parfois imposer la donnée dans le compte d'une victime. Il faut démontrer cette chaîne et vérifier protections CSRF, SameSite, permissions et interaction ; leur présence ou absence ne se présume pas.
4. **Action explicite de la victime :** faire cliquer sur un lien, faire importer un fichier et faire exécuter du code manuellement dans la console sont des prérequis différents ; les noter précisément au lieu de les regrouper.
5. **Tri de bug bounty :** les politiques varient. [HackerOne](https://docs.hackerone.com/en/articles/8494488-core-ineligible-findings) exclut généralement la self-exploitation de ses critères de base sauf si une autre victime peut être attaquée ; [Mozilla](https://www.mozilla.org/en-US/security/bug-bounty/faq-webapp/) exclut les cas où l'utilisateur est amené à coller du script. Ce ne sont pas des règles universelles de sécurité applicative.

## 4. Grille à appliquer lors d'une revue

Pour chaque chemin candidat, relever :

1. **Source et contrôle :** qui choisit la donnée et quelles requêtes, API ou objets l'acheminent ?
2. **Restitution et persistance :** réponse immédiate, stockage puis lecture, donnée purement côté navigateur, ou combinaison ?
3. **Puits et contexte :** HTML, attribut, URL, script, `innerHTML`, `v-html` ou sous-document ; transformation et protections effectives.
4. **Frontière entre comptes :** qui peut déclencher l'écriture, qui peut lire et par quel moyen ? Un lecteur tiers est-il démontré, seulement possible ou exclu par une règle vérifiée ?
5. **Déclenchement et impact :** action requise, navigateur, CSP, permissions et données accessibles ; distinguer injection HTML, placement actif et exécution observée.
6. **Classement et statut :** réfléchie/stockée, DOM ou serveur comme mécanisme, puis portée self/tiers comme propriété distincte. Utiliser « indéterminé » quand l'acheminement vers un autre utilisateur n'est pas prouvé.

La skill future doit signaler le flux de code dangereux même si l'impact est limité ou inconnu, puis expliquer séparément la possibilité d'atteindre un tiers. Les scénarios ci-dessus sont des plans de test et n'ont pas été exécutés.
