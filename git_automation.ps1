param (
    [string]$Commit = "Intial Commit"
)

git add .
git commit -m "$Commit"
git push -u origin main