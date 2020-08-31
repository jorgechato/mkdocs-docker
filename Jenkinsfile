//!groovy
node {
    try {
        stage("Checkout") {
            checkout scm
        }

        stage("Build") {
        }

        stage("Checkout") {
        }
    } catch(def e) {
        currentBuild.result = 'FAILURE'
        echo e.getMessage()

        // Here you can notify to git if the commit has failed the execution
    }
}
