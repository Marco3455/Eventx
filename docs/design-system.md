# Design System — EventX (Plateforme de billetterie)

> Projet en **Tailwind CSS v4** : pas de `tailwind.config.ts`, le thème est défini directement dans `app/globals.css` via `@theme`.

## Couleurs

| Rôle | Usage | Variable CSS |
|---|---|---|
| `primary` (violet) | Marque, navigation, éléments premium | `--primary` |
| `accent` (corail) | Boutons d'action forte (Acheter, Réserver) | `--accent` |
| `secondary` | Fonds secondaires, badges | `--secondary` |
| `muted` | Texte discret, placeholders | `--muted-foreground` |
| `success` / `destructive` | États (paiement validé / erreur) | `--success` / `--destructive` |

Valeurs définies dans `:root` (clair) et `.dark` (sombre) dans `app/globals.css`, puis exposées à Tailwind via le bloc `@theme inline`. Ne jamais coder une couleur en dur — toujours les classes Tailwind (`bg-primary`, `text-accent`...).

## Typographie

| Police | Rôle | Classe Tailwind |
|---|---|---|
| **Space Grotesk** | Titres, hero, chiffres clés | `font-display` |
| **Inter** | Texte courant | `font-body` (par défaut sur `body`) |
| **IBM Plex Mono** | Codes billets, prix, références | `font-mono-ui` (ou classe utilitaire `.ticket-code`) |

Chargées via `next/font/google` dans `app/layout.tsx`, exposées comme variables CSS puis mappées dans `@theme`.

## Espacements

Tokens sémantiques définis dans `@theme` (`app/globals.css`) :

| Token | Valeur | Usage |
|---|---|---|
| `gutter` | 24px | Padding latéral standard (mobile) |
| `gutter-lg` | 48px | Padding latéral (desktop) |
| `card-padding` | 24px | Padding interne des `Card` |
| `stack` | 16px | Espacement entre éléments empilés |
| `section-gap` | 80px | Espace vertical entre sections (mobile) |
| `section-gap-lg` | 120px | Espace vertical entre sections (desktop) |

Exemple : `className="py-section-gap lg:py-section-gap-lg px-gutter lg:px-gutter-lg"`.

## Breakpoints

`sm` 480px · `md` 768px · `lg` 1024px · `xl` 1280px · `2xl` 1440px — définis dans `@theme`. Convention mobile-first.

## Composants de base

- `Button` — variantes `default` (violet), `accent` (corail, CTA fort), `secondary`, `outline`, `ghost`, `destructive`, `link`.
- `Input` — champ de formulaire standard.
- `Card` — `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, `CardFooter`.

## Conventions

1. Jamais de couleurs Tailwind brutes (`bg-purple-600`) — toujours les tokens sémantiques.
2. Montants et codes de billets → `.ticket-code` / `font-mono-ui`.
3. `accent` (corail) réservé aux actions à fort enjeu — un seul par écran.
4. Nouveaux composants → `components/ui/`, pattern `forwardRef` + `cn()`.

## Installation (le projet utilise pnpm)

```bash
pnpm add class-variance-authority clsx tailwind-merge tw-animate-css @radix-ui/react-slot
pnpm dev
```

### shadcn/ui

`components.json`, `Button`, `Input`, `Card` sont déjà écrits dans le style shadcn/ui. Pour ajouter un composant supplémentaire :

```bash
pnpm dlx shadcn@latest add <nom-du-composant>
```
