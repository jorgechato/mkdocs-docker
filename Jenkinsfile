//!groovy

// docker
def customImage
def registry = "quay.io/orggue"
def registry_credential = "quay_credential"


// potentially you will import here the libraries and wrappers you develop
// @ library('<library-name@version>') _
node {
    try {
        stage("Checkout") {
            checkout scm
            // Notification if the pipeline is currently running should be here
        }

        stage("Dependencies") {
            sh "pip install mkdocs"
        }

        stage("Integration Test") {
            // If we wanted we could run some tests before building the image
            sh "python src/mkweb/app/handler_test.py"
        }

        stage("Build") {
            customImage = docker.build("mkdocs:${env.BUILD_ID}", "-f build/Dockerfile .")
        }

        stage("Test") {
            // let's check if the container generate the correct output
            sh "./mkdockerize.sh produce ./tmp"
            if (!fileExists('./tmp.tar.gz')) {throw new Exception("File wasn't created.")}
        }

        stage("Publish") {
            docker.withRegistry(registry, registry_credential) {
                customImage.push()
            }
        }

        // Notification of a successful pipeline
    } catch(def e) {
        currentBuild.result = 'FAILURE'
        echo e.getMessage()

        // Here you can notify to git if the commit has failed the execution
    }
}
