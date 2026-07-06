# RiskMaverick

Jekyll site (magazine) deployed via GitHub Pages to riskmaverick.com.

## Local development
Requires Ruby 3.3+ with DevKit.
```powershell
bundle install
bundle exec jekyll serve --livereload
```
Open http://localhost:4000. Production builds automatically on GitHub Pages from the default branch.

## Adding an article
Create `_posts/YYYY-MM-DD-slug.md` with front-matter: `title`, `kind` (basics|analysis|wire), `markets: []`, `concepts: []`, `excerpt`, and `sources: [{title, publisher, url}]`. It appears automatically on matching hubs and in Insights.
