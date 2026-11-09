# openpay
Open Payment Host is a free, open-source, self-hosted, minimalist payments

## Publishing to GitHub Packages

Maven is configured to publish this project to GitHub Packages. Before deploying,
add a GitHub Personal Access Token (classic) with the `write:packages` scope to
your local Maven settings file at `~/.m2/settings.xml`:

```xml
<settings>
    <servers>
        <server>
            <id>github</id>
            <username>YOUR_GITHUB_USERNAME</username>
            <password>YOUR_PERSONAL_ACCESS_TOKEN</password>
        </server>
    </servers>
</settings>
```

Keep the token in this local file; do not commit it. Once the project has Maven
source files, deploy the package with:

```sh
mvn deploy
```
