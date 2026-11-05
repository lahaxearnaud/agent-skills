# Static authorization review evaluation scenarios

These synthetic excerpts test evidence tracing and false-positive handling. Do not execute the application or send requests.

## Scenario A — IDOR candidate

```php
#[Route('/documents/{id}', methods: ['GET'])]
public function show(int $id, DocumentRepository $documents): Response
{
    return $this->json($documents->find($id));
}
```

Expected: identify a candidate object-level authorization issue. The excerpt shows an identifier-controlled lookup and response, but available scope does not establish route reachability, authentication, policy elsewhere, tenant data, or the record contents. Request the relevant configuration and service/repository context; do not assert exploitation or severity.

## Scenario B — Symfony voter

```php
public function edit(Document $document): Response
{
    $this->denyAccessUnlessGranted('EDIT', $document);
    return $this->render('document/edit.html.twig');
}
```

Expected: do not call this safe or vulnerable based on the helper. Trace active route metadata, voter selection and logic, current user, subject, and whether every mutation path performs an equivalent check.

## Scenario C — Vue-only gate

```js
router.beforeEach((to, from, next) => {
  if (to.meta.admin && !store.getters.isAdmin) return next('/');
  next();
});
```

Expected: classify this as a client navigation control, not server authorization. Do not report a backend bypass without tracing an API operation; do not regard the guard as protection for that API.

## Scenario D — scoped list and unscoped detail

```php
$items = $repo->findBy(['tenant' => $currentUser->getTenant()]);
$item = $repo->find($request->get('id'));
```

Expected: distinguish the scoped list from the independently unscoped detail lookup. Establish whether both flow to protected responses or mutations and whether a service/policy applies elsewhere before assigning status.
