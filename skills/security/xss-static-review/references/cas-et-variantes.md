# Cas du corpus et recherche de variantes

Les références ci-dessous illustrent des mécanismes confirmés par leurs auteurs. Elles ne démontrent pas qu'un projet audité est vulnérable. Comparer version, configuration, source, chemin, rôle et puits ; si un avis ou correctif n'est pas disponible localement, ne pas inventer ses détails.

| Motif | Cas source | Question de revue |
|---|---|---|
| Échappement HTML puis décodage DOM puis HTML | [AVideo — GHSA-wfq5-qgqp-hvhv](https://github.com/WWBN/AVideo/security/advisories/GHSA-wfq5-qgqp-hvhv) | Une donnée JSON ou HTML échappée arrive-t-elle ensuite dans `innerHTML` ? |
| `raw` et mêmes valeurs dans plusieurs interfaces | [Sylius — GHSA-mx4q-xxc9-pf5q](https://github.com/Sylius/Sylius/security/advisories/GHSA-mx4q-xxc9-pf5q) | Les données d'entité traversent-elles macros, fil d'Ariane et composants admin ? |
| Logs ou fichiers rendus dans l'interface de debug | [Symfony — GHSA-hmr5-2xcr-v8pp](https://github.com/symfony/symfony/security/advisories/GHSA-hmr5-2xcr-v8pp) | Toutes les branches de rendu échappent-elles les données et qui peut écrire/lire le fichier ? |
| Filtre déclaré sûr pour trop de contextes | [Twig — GHSA-jv8m-2544-3pg3](https://github.com/twigphp/Twig/security/advisories/GHSA-jv8m-2544-3pg3) | La garantie `is_safe` correspond-elle à l'entrée et au contexte final ? |
| Sécurité d'un attribut URL non couverte | [Symfony HtmlSanitizer — GHSA-hhg7-c65m-h7ff](https://github.com/symfony/symfony/security/advisories/GHSA-hhg7-c65m-h7ff) | La configuration autorise-t-elle des balises/attributs et schémas concernés ? |
| Objet SVG provenant d'une source externe | [Symfony UX Icons — GHSA-6v8j-33hc-mv84](https://github.com/advisories/GHSA-6v8j-33hc-mv84) | Qui contrôle les icônes et comment le SVG est-il rendu ? |
| Donnée en script déjà autorisé par nonce | [Adminer — GHSA-h6jr-7pr6-grgj](https://github.com/vrana/adminer/security/advisories/GHSA-h6jr-7pr6-grgj) | Métadonnée externe insérée dans JS ? La branche d'échec de validation laisse-t-elle passer l'entrée ? |
| Message stocké dans Vue | [Chamilo — GHSA-ppw9-gf4r-5c39](https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-ppw9-gf4r-5c39) | L'écriture par un rôle atteint-elle `v-html` vu par un autre ? |
| Rendu intermédiaire avant assainissement | [Grafana — GHSA-7rqg-hjwc-6mjf](https://github.com/advisories/GHSA-7rqg-hjwc-6mjf) | Un état de rendu ou aperçu utilise-t-il la valeur avant sa transformation ? |
| HTML riche ou SVG servi comme document | [Open WebUI — GHSA-v2qm-5wxj-qhj7](https://github.com/advisories/GHSA-v2qm-5wxj-qhj7) | Un endpoint voisin d'un correctif sert-il encore un document actif sur l'origine applicative ? |
| SVG et repli en cas d'échec du sanitizer | [FreeScout — GHSA-cvr8-cw5c-5pfw](https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-cvr8-cw5c-5pfw) | Une erreur entraîne-t-elle l'acceptation d'une sortie moins sûre ? |
| Markdown/diagramme et calcul intermédiaire | [Mermaid — GHSA-7rqq-prvp-x9jh](https://github.com/mermaid-js/mermaid/security/advisories/GHSA-7rqq-prvp-x9jh) | La mesure d'un libellé ou la génération SVG crée-t-elle un puits avant le rendu final ? |
| Branches JSON ou WebSocket non couvertes | [AVideo — GHSA-2fhx-q92v-5fhv](https://github.com/advisories/GHSA-2fhx-q92v-5fhv) | Une clé alternative contourne-t-elle la validation appliquée à une seule branche ? |
| État de confiance après mutation | [Rails — GHSA-89vf-4333-qx8v](https://github.com/rails/rails/security/advisories/GHSA-89vf-4333-qx8v) | Une transformation préserve-t-elle à tort une marque de sûreté ? |
| Données d'infrastructure vers tableau admin | [Froxlor — GHSA-43gm-9rr3-cx7g](https://github.com/advisories/GHSA-43gm-9rr3-cx7g) | Le format métier valide-t-il par erreur du texte HTML brut dans un écran privilégié ? |
| Self-XSS à portée limitée | [Nextcloud Deck — GHSA-mg7w-x9fm-9wwc](https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mg7w-x9fm-9wwc) | L'autre compte peut-il réellement recevoir la valeur, ou la portée est-elle inconnue / limitée ? |

## Recherche de variantes autour d'un constat

1. Chercher les autres champs et composants utilisant le même helper, renderer, filtre ou endpoint ; inclure les pages d'admin, aperçu, erreur et export.
2. Chercher les voies alternatives de la donnée : JSON/formulaire, clés de message concurrentes, stockage puis lecture, appel SSR et client.
3. Vérifier les contextes différents d'une même sortie : texte, attribut URL, script, SVG, document autonome.
4. Inspecter les branches d'erreur, repli, versioning, encodage et pré/post-traitement du sanitizer.
5. Distinguer chaque variante confirmée statiquement d'une piste dont un maillon manque ; ne pas multiplier les constats pour un même chemin racine sans expliquer les surfaces.
