# Synthetic examples

These examples illustrate the profile; they are not copied from a project.

## PHP: explicit contract in a compatible project

If the surrounding code uses modern typed PHP, keep the contract visible and the change focused:

```php
function isEligible(int $quantity): bool
{
    return $quantity > 0;
}
```

Do not add `strict_types`, `final`, `readonly` or new service layers to unrelated files merely to imitate the profile. Respect the existing PHP version and project conventions.

## JavaScript: match the project module system

```js
const isEligible = (quantity) => quantity > 0;
```

Use `let` for a binding that actually changes. If the repository uses CommonJS or a different style, preserve it instead of converting it to ES modules.

## Rust: follow the repository

Use the existing toolchain, error strategy and local conventions. The available personal history is too sparse to prefer a particular style of `Result`, `unwrap`, or abstraction.
