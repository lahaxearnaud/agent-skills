# Nouveaux cas XSS affectant des applications Web, toutes technologies

Recherche du 3 novembre 2026. Cette sélection élargit les surfaces analysées tout en conservant le périmètre XSS Web. Les fiches synthétisent des avis ou rapports publics ; les chaînes et impacts sont ceux documentés par les sources et ne prouvent pas l'exploitabilité d'une installation actuelle. Sauf indication contraire, la CSP réellement déployée doit être relevée. Vérifier les plages de versions et les correctifs dans l'avis à jour.

## 1. Authentification et identité

### WEB-01 — ZITADEL : SAML, URL de redirection et prise de compte

**Avis :** [GHSA-pr34-2v5x-6qjq / CVE-2026-29191](https://github.com/advisories/GHSA-pr34-2v5x-6qjq). **Technologie / type :** application d'identité Go ; XSS réfléchie. **Chaîne :** paramètres de l'endpoint `/saml-post` → URL de formulaire non sûre et données reflétées sans encodage HTML → script dans l'origine d'identité. **Conditions :** une victime doit déclencher le chemin ; l'avis indique qu'une configuration SAML n'est pas nécessaire et que le vecteur précis de changement de mot de passe est limité par MFA ou authentification sans mot de passe. **Impact rapporté :** prise de compte possible sous ces conditions. **Détection :** suivre paramètres GET, redirections, action de formulaire, encodage HTML et changements de mot de passe ; le correctif supprime l'endpoint et renforce la vérification du mot de passe actuel.

### WEB-02 — Logto : RelayState dans un formulaire SAML

**Avis :** [GHSA-cpm5-w86q-w85f](https://github.com/logto-io/logto/security/advisories/GHSA-cpm5-w86q-w85f). **Technologie / type :** Node.js, SAML, XSS réfléchie dans un formulaire automatique. **Chaîne :** `RelayState` → attribut HTML interpolé sans encodage → document de l'IdP. **Conditions :** requête SAML acceptée pour une application configurée ; si les requêtes sont signées, l'attaquant doit pouvoir en produire une valide. La victime doit achever le parcours de connexion. L'avis signale une CSP autorisant l'inline. **Impact :** actions dans la session d'identité. **Détection :** chercher les générateurs HTML manuels SAML et suivre aussi `actionUrl` et les attributs cachés ; le correctif échappe les attributs au rendu.

### WEB-03 — Admidio : exception SAML affichée en HTML

**Avis :** [GHSA-7jxv-38f3-6xgf](https://github.com/Admidio/admidio/security/advisories/GHSA-7jxv-38f3-6xgf). **Technologie / type :** PHP, LightSaml ; XSS réfléchie sur un chemin d'erreur. **Chaîne :** valeurs issues de paramètres ou XML → message d'exception → sortie HTML directe. **Conditions :** atteindre le parcours SSO et provoquer une exception contenant la donnée ; le rapport décrit différentes lectures, décodages et vérifications en amont. **Impact :** exécution dans l'origine de l'application si la victime reçoit la réponse active. **Détection :** suivre les messages de bibliothèques externes jusque dans `echo`, templates et pages d'erreur ; traiter leurs contenus comme non fiables.

### WEB-04 — ZITADEL : image active ouverte comme document

**Avis :** [GHSA-hr5w-cwwq-2v4m / CVE-2024-29891](https://github.com/advisories/GHSA-hr5w-cwwq-2v4m). **Technologie / type :** Go, avatars ; XSS stockée via fichier servi. **Chaîne :** contenu HTML présenté comme image → stockage → ouverture directe en navigateur sur l'origine d'identité. **Conditions :** session active de la victime et navigation directe vers la ressource ; l'éditeur indique une reproduction dans Firefox, pas dans Chrome, Safari ou Edge dans son test de l'époque. **Impact :** prise de compte dans les circonstances rapportées. **Détection :** suivre octets réels, média déclaré, endpoint de service, `Content-Disposition`, origine et CSP du fichier ; ne pas inférer la même exécution en `<img>` et en document principal.

## 2. Administration et observabilité

### WEB-05 — Froxlor : donnée DNS vers panneau administrateur

**Avis :** [GHSA-43gm-9rr3-cx7g / CVE-2026-54347](https://github.com/advisories/GHSA-43gm-9rr3-cx7g). **Technologie / type :** PHP, Twig ; XSS stockée inter-rôles. **Chaîne :** contenu d'un enregistrement DNS TXT → callback `wordwrap` non échappant → `|raw` dans un tableau. **Conditions :** DNS et éditeur activés, compte autorisé à éditer, administrateur consultant la zone ; l'avis décrit une CSP autorisant l'inline. **Impact :** actions possibles dans la session administrateur, avec prise de contrôle indiquée par l'avis. **Détection :** suivre les données d'infrastructure, callbacks de rendu et marquage HTML sûr ; la validation d'un format DNS ne remplace pas l'encodage HTML.

### WEB-06 — Adminer : version MySQL dans un script doté d'un nonce

**Avis :** [GHSA-h6jr-7pr6-grgj](https://github.com/vrana/adminer/security/advisories/GHSA-h6jr-7pr6-grgj). **Technologie / type :** PHP, serveur MySQL contrôlé ; injection JavaScript. **Chaîne :** chaîne de version d'un serveur DB → regex retournant l'entrée intacte en cas de non-correspondance → interpolation dans un script déjà porteur d'un nonce valide. **Conditions :** la victime doit établir une connexion au serveur contrôlé ou une autre chaîne, telle que celle mentionnée dans l'avis, doit rendre cela possible. **Impact :** code dans le script autorisé par la CSP. **Détection :** suivre les métadonnées de services distants et les branches d'échec de `preg_replace`, puis inspecter le contenu de scripts nonce ; le nonce ne sécurise pas les données interpolées.

### WEB-07 — Prometheus : métriques et tooltips HTML

**Avis :** [GHSA-vffh-x6r8-xx99](https://github.com/prometheus/prometheus/security/advisories/GHSA-vffh-x6r8-xx99). **Technologie / type :** Go, interface React/Mantine ; XSS stockée DOM. **Chaîne :** noms ou labels de métriques issus de cibles de collecte, remote write ou OTLP → tooltip ou explorateur → `innerHTML`. **Conditions :** capacité d'injecter des métriques et interaction avec la vue concernée ; les chemins exacts diffèrent entre interfaces. **Impact :** accès aux capacités de la session Prometheus ; les actions d'administration dépendent des options activées. **Détection :** ne pas considérer les noms de métriques comme numériques ou sûrs par convention ; suivre aussi les labels et les outils de visualisation.

### WEB-08 — Grafana : fenêtre non assainie dans le cycle React

**Avis :** [GHSA-7rqg-hjwc-6mjf / CVE-2023-22462](https://github.com/advisories/GHSA-7rqg-hjwc-6mjf). **Technologie / type :** React, panneau de texte ; XSS stockée nécessitant plusieurs interactions. **Chaîne :** contenu du panneau → cycle de rendu qui expose temporairement du HTML non assaini → cycle suivant nettoyant le contenu. **Conditions :** rôle Editor pour modifier le panneau ; une autre personne doit éditer ce panneau et sélectionner Markdown ou HTML. **Impact :** élévation de privilèges possible selon les droits de la victime. **Détection :** examiner tous les rendus intermédiaires, états et aperçus, pas uniquement le contenu final enregistré.

## 3. Fichiers, aperçus et documents actifs

### WEB-09 — Open WebUI : correctif SVG absent d'un quatrième chemin

**Avis :** [GHSA-v2qm-5wxj-qhj7 / CVE-2026-54013](https://github.com/advisories/GHSA-v2qm-5wxj-qhj7). **Technologie / type :** Python, stockage de métadonnées ; XSS stockée via SVG. **Chaîne :** image de modèle fournie sous forme de données SVG → endpoint de service inline sur l'origine applicative → navigateur ouvrant la ressource comme document. **Conditions :** permission de créer/modifier un modèle et navigation de la victime vers l'URL directe ; l'avis précise que le chargement ordinaire dans `<img>` ne déclenche pas la même exécution. **Impact :** accès aux données de session disponibles dans l'origine, avec prise de compte décrite. **Détection :** rechercher les fonctions voisines après un correctif ; comparer les validations d'avatars utilisateur, webhook et modèle.

### WEB-10 — FreeScout : échec d'assainissement SVG suivi d'un repli regex

**Avis :** [GHSA-cvr8-cw5c-5pfw](https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-cvr8-cw5c-5pfw). **Technologie / type :** PHP, téléversement SVG ; XSS stockée. **Chaîne :** extension et média interprétés séparément → assainisseur SVG en échec → suppression partielle par regex → contenu affiché inline. **Conditions :** possibilité de fournir le fichier et consultation de la ressource dans un contexte où le navigateur interprète le contenu actif. **Impact :** exécution dans le contexte de la victime selon l'avis. **Détection :** ne pas continuer avec un nettoyage moins strict après erreur ; aligner validation des octets, média et mode de service.

### WEB-11 — django-helpdesk : pièce jointe HTML issue d'un email

**Avis :** [GHSA-q46c-8w98-fq2g](https://github.com/django-helpdesk/django-helpdesk/security/advisories/GHSA-q46c-8w98-fq2g). **Technologie / type :** Python, Django, email ; XSS stockée. **Chaîne :** corps HTML d'un email entrant ou pièce jointe → fichier sauvegardé → lien de ticket → réponse HTML servie inline. **Conditions :** un membre de l'équipe ouvre la pièce jointe ; les versions historiques ont des exceptions détaillées dans l'avis. **Impact :** script dans la session du personnel et accès aux tickets selon ses droits. **Détection :** relier ingestion email, stockage, URL de pièce jointe, type de contenu et origine ; le nom de fichier n'est pas un garant du contenu.

### WEB-12 — Jupyter Server : conversion de notebook sans sandbox CSP

**Avis :** [GHSA-fcw5-x6j4-ccmp](https://github.com/jupyter-server/jupyter_server/security/advisories/GHSA-fcw5-x6j4-ccmp). **Technologie / type :** Python, nbconvert ; XSS stockée dans l'aperçu d'un notebook. **Chaîne :** notebook avec sortie HTML contrôlée → export HTML non assaini → réponse sur l'origine Jupyter sans directive sandbox appropriée. **Conditions :** une victime authentifiée navigue vers la conversion d'un notebook influencé par un tiers. **Impact rapporté :** accès aux API Jupyter et possibilité d'exécution via le noyau lorsque les permissions le permettent. **Détection :** traiter les rendus de documents comme applications actives, examiner origine et CSP de chaque endpoint.

## 4. Frameworks, données structurées et transports

### WEB-13 — React Router : redirection issue de contenu non fiable

**Avis :** [GHSA-2w69-qvjg-hvjx / CVE-2026-22029](https://github.com/remix-run/react-router/security/advisories/GHSA-2w69-qvjg-hvjx). **Technologie / type :** React Router et Remix, navigation SPA ; XSS conditionnée par la destination. **Chaîne :** redirection provenant de données non fiables → gestion client d'URL dangereuse. **Conditions :** modes Framework, Data ou RSC indiqués dans l'avis, source de redirection contrôlable ou redirection ouverte ; le mode déclaratif seul est explicitement exclu. **Impact :** exécution côté client sous les préconditions de l'avis. **Détection :** suivre `redirect` depuis loaders/actions jusqu'au routeur et valider les destinations structurées.

### WEB-14 — React Router : en-tête Location vers HTML pré-rendu

**Avis :** [GHSA-f22v-gfqf-p8f3 / CVE-2026-33244](https://github.com/remix-run/react-router/security/advisories/GHSA-f22v-gfqf-p8f3). **Technologie / type :** React Router v7 Framework Mode ; XSS stockée dans des fichiers statiques générés. **Chaîne :** `Location` non fiable pendant le pré-rendu → HTML de redirection créé sans neutralisation correcte. **Conditions :** mode Framework et pré-rendu activés ; les modes déclaratif et Data mentionnés dans l'avis sont exclus. **Impact :** HTML actif servi depuis l'application. **Détection :** inspecter également les chemins de build et les artefacts générés ; mettre à jour puis reconstruire les fichiers.

### WEB-15 — Mermaid et KaTeX : mesure de texte via `innerHTML`

**Avis :** [GHSA-7rqq-prvp-x9jh / CVE-2025-54881](https://github.com/mermaid-js/mermaid/security/advisories/GHSA-7rqq-prvp-x9jh). **Technologie / type :** JavaScript, Mermaid et KaTeX ; XSS via rendu de diagramme. **Chaîne :** libellé de diagramme de séquence avec délimiteurs KaTeX → mesure des dimensions → `innerHTML` avec contenu complet. **Conditions :** texte de diagramme contrôlable, version concernée et branche KaTeX active. **Impact :** exécution dans la page affichant le diagramme. **Détection :** rechercher les puits de mesure hors écran et pas uniquement le rendu visible ; l'encodage de la sortie finale peut intervenir trop tard.

### WEB-16 — OneUptime : Markdown, Mermaid permissif et SVG

**Avis :** [GHSA-wvh5-6vjm-23qh / CVE-2026-32308](https://github.com/advisories/GHSA-wvh5-6vjm-23qh). **Technologie / type :** React, Markdown, Mermaid, SVG ; XSS stockée. **Chaîne :** champ Markdown → diagramme Mermaid en mode `loose` → SVG inséré dans `innerHTML`. **Conditions :** pouvoir écrire un des champs rendus et consultation par une autre personne ; les usages publics et internes dépendent des droits de chaque champ. **Impact :** code exécuté dans l'origine de la page consultée. **Détection :** inventorier les configurations de renderers, les champs qui partagent le composant et les effets des transformations SVG en aval.

### WEB-17 — Rails : indicateur de sécurité perdu après mutation

**Avis :** [GHSA-89vf-4333-qx8v / CVE-2026-33170](https://github.com/rails/rails/security/advisories/GHSA-89vf-4333-qx8v). **Technologie / type :** Ruby, Active Support/ERB ; XSS possible. **Chaîne :** `SafeBuffer` modifié en place → formatage `%` avec données non fiables → indicateur de sûreté incorrect → auto-échappement contourné. **Conditions :** version affectée et séquence précise de mutation/formatage ; l'avis ne dit pas que tout emploi de `SafeBuffer` est vulnérable. **Impact :** XSS possible selon le contexte de sortie. **Détection :** analyser les métadonnées de confiance après transformations, comme pour `Twig\Markup` ou les filtres déclarés sûrs.

### WEB-18 — AVideo : correctif WebSocket limité à une branche JSON

**Avis :** [GHSA-2fhx-q92v-5fhv / CVE-2026-49279](https://github.com/advisories/GHSA-2fhx-q92v-5fhv). **Technologie / type :** PHP, WebSocket, backend SQLite ; XSS stockée. **Chaîne :** message structuré → suppression d'un champ dans une branche → une autre clé traitée prioritairement conserve la donnée. **Conditions :** configuration WebSocket concernée et capacité d'envoyer un message ; l'impact dépend des destinataires connectés. **Détection :** suivre toutes les variantes d'un schéma, les priorités entre clés et les chemins parallèles ; ajouter des tests de non-régression au-delà du chemin initial corrigé. L'avis consulté ne renseignait pas de version corrigée dans ses métadonnées ; vérifier son état actuel.

## 5. Périmètre self-XSS et rapport bug bounty

### WEB-19 — Nextcloud Deck : avis explicitement qualifié self-XSS

**Avis :** [GHSA-mg7w-x9fm-9wwc / CVE-2024-22213](https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mg7w-x9fm-9wwc). **Technologie / type :** application Web Deck ; l'éditeur qualifie le cas de self-XSS lors de l'envoi de HTML comme commentaire. **Conditions et impact :** l'avis indique qu'un utilisateur peut être amené à exécuter du code dans son navigateur, sans détailler suffisamment ici le chemin pour affirmer une attaque inter-comptes. **Détection :** corriger le puits et noter séparément la preuve disponible sur l'acheminement vers d'autres utilisateurs. L'avis cite HackerOne ; son rapport source n'a pas été lu intégralement dans cette recherche.

### WEB-20 — Basecamp : rapport HackerOne public, détails partiellement accessibles

**Rapport :** [HackerOne #3943339](https://hackerone.com/reports/3943339). Le résultat de recherche public décrit une chaîne inter-comptes combinant pagination Turbo et HTML Active Storage, et indique que l'équipe l'a marquée résolue. La page complète n'était pas accessible au lecteur Web utilisé, qui demandait JavaScript. **Niveau de preuve :** titre et état visibles dans l'index de recherche seulement ; les étapes, prérequis exacts et correctif n'ont pas été vérifiés indépendamment. **Piste de revue :** étudier les réponses HTML de pagination, les uploads non associés et l'origine des ressources, sans présenter ce résumé comme une analyse complète du rapport.

## 6. Règles candidates pour la future analyse statique

| Piste | Source → transformations → puits | Faux positifs et vérifications indispensables |
|---|---|---|
| `WEB-R01` | Métadonnées externes (DB, DNS, métriques, certificats) → formatage → HTML/JS | Prouver le contrôle et le contexte ; un nom de champ interne n'implique pas la confiance. |
| `WEB-R02` | Exceptions SSO/XML/JSON → réponse HTML | Vérifier que le message contient une donnée contrôlable et que le chemin d'erreur est accessible. |
| `WEB-R03` | Redirection non fiable → formulaire auto-submit, routeur SPA ou HTML pré-rendu | Vérifier le schéma, l'origine, le mode du framework et si le code concerné est réellement utilisé. |
| `WEB-R04` | Email, SVG, HTML ou notebook → stockage → réponse active | Déterminer type servi, navigation directe ou intégration, origine, CSP et droits de lecture. |
| `WEB-R05` | Markdown/diagramme → renderer/mesure → HTML ou SVG | Les puits intermédiaires peuvent agir avant le nettoyage final ; vérifier version et configuration. |
| `WEB-R06` | JSON/WebSocket à branches multiples → traitement ou suppression partielle → rendu DOM | Modéliser priorités et variantes de clés ; tester tous les chemins, pas seulement le correctif original. |
| `WEB-R07` | Chaîne marquée sûre → mutation ou formatage → sortie | Vérifier la sémantique de la bibliothèque et la propagation de l'état de confiance par contexte. |
| `WEB-R08` | Entrée non fiable → script comportant un nonce valide | Le nonce autorise le script, pas automatiquement l'entrée ; suivre la sérialisation HTML/JS et les contrôles en amont. |
| `WEB-R09` | Panneau riche → état de rendu temporaire → nettoyage ultérieur | Examiner les rendus intermédiaires et les interactions ; ne pas conclure depuis le seul état final. |

Pour tous les cas : garder source, rôle attaquant, propagation, puits, victime, interaction, version, CSP, preuve, limites et correctif. Les règles candidates sont des hypothèses de conception, pas des règles SAST implémentées ni testées.
