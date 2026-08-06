source "https://rubygems.org"

# We build the site with our own Actions workflow (.github/workflows/pages.yml),
# so Jekyll is ours to pin. The github-pages gem used to do this for us, but it
# forces Jekyll 3.10 and a frozen dependency set that no longer resolved against
# a modern Bundler — the source of the "can't satisfy your Gemfile's
# dependencies" build warning.
gem "jekyll", "~> 4.4"

group :jekyll_plugins do
  gem "jekyll-sitemap", "~> 1.4"
end

# Ruby 3+ no longer bundles webrick, and only `jekyll serve` needs it — keeping
# it out of the default group means CI never installs it.
group :development do
  gem "webrick", "~> 1.8"
end
