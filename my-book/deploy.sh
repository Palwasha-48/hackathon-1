#!/bin/bash

# Build the site
npm run build

# Navigate to the build output
cd build

# Initialize a new git repository
git init
git add .
git commit -m "Deploy website to GitHub Pages"

# Push to the gh-pages branch (replace with your repo URL)
git remote add origin https://github.com/Palwasha-48/h-3.git
git push -f origin main:gh-pages

echo "Deployment completed! Your site will be available at https://Palwasha-48.github.io/h-3/"