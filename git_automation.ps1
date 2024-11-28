param (
    [string]$Commit = "Update"
)

git add .
git commit -m "$Commit"
git push -u origin main