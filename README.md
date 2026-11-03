# OpenPay

Open Payment Host is a free, open-source, self-hosted, minimalist payments project.

## Android app

The Android application is in `app/`. It currently contains a minimal launcher screen and uses
`com.example.myapp` as its application ID.

Build it with JDK 17 and Android SDK platform 37:

```shell
./gradlew :app:assembleDebug
```

The Gradle settings apply the Develocity Gradle plugin and its common custom user data plugin.
Set `DEVELOCITY_URL` to your Develocity server URL to configure the destination for Build Scans.
Publishing is skipped unless the build is authenticated.

## Maven example

`maven-example/` is a standalone Maven project demonstrating the Common Custom User Data Maven
extension referenced above. Its `.mvn/extensions.xml` applies both the Develocity Maven extension
and the common custom user data extension. The custom Groovy script adds the project name and
parallel-build status to Build Scans.

Build it with JDK 17 and Maven:

```shell
cd maven-example
mvn verify
```

To publish Maven Build Scans, configure the Develocity server URL using the Maven extension's
supported configuration, for example `-Ddevelocity.url="$DEVELOCITY_URL"`, authenticate with that
server, and explicitly request a scan with `-Dscan`. The sample disables automatic scan publishing.
