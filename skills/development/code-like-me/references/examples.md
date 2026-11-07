# Synthetic examples

These examples illustrate the profile; they are not copied from a project.

## PHP: explicit contract in a compatible project

If the surrounding code uses PHP 8.2 or later and an immutable, non-extendable class is appropriate, keep the contract visible and the change focused:

```php
final readonly class Eligibility
{
    public function isEligible(int $quantity): bool
    {
        return $quantity > 0;
    }
}
```

For example, test both positive and zero quantities. Prefer `final` and `readonly` for suitable new classes when the PHP version, behavior and project conventions allow it; do not retrofit unrelated files or prevent required extension or mutation. Extract a service when its complexity, reuse or testability justifies it. Cover each reachable new or modified branch with behavior tests at the lowest faithful layer.

## JavaScript: match the project module system

```js
const isEligible = (quantity) => quantity > 0;
```

Use `let` for a binding that actually changes. If the repository uses CommonJS or a different style, preserve it instead of converting it to ES modules.

## Rust: follow the repository

Use the existing toolchain, error strategy and local conventions. The available personal history is too sparse to prefer a particular style of `Result`, `unwrap`, or abstraction.
