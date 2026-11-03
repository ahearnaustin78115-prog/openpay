pluginManagement {
    repositories {
        gradlePluginPortal()
        google()
        mavenCentral()
    }
}

plugins {
    id("com.gradle.develocity") version "4.6.1"
    id("com.gradle.common-custom-user-data-gradle-plugin") version "2.8.0"
}

val isCI = providers.environmentVariable("CI").isPresent
providers.environmentVariable("DEVELOCITY_URL").orNull?.let {
    develocity.server = it
}

develocity {
    buildScan {
        uploadInBackground = !isCI
        publishing.onlyIf { it.isAuthenticated }
        obfuscation {
            ipAddresses { addresses -> addresses.map { "0.0.0.0" } }
        }
    }
}

dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.name = "openpay"
include(":app")
