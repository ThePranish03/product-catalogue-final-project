# CI/CD Final Project Submission Evidence

Repository: https://github.com/ThePranish03/product-catalogue-final-project

## GitHub source links

1. Project README: https://github.com/ThePranish03/product-catalogue-final-project/blob/main/README.md
2. GitHub Actions workflow: https://github.com/ThePranish03/product-catalogue-final-project/blob/main/.github/workflows/workflow.yml
3. Tekton tasks: https://github.com/ThePranish03/product-catalogue-final-project/blob/main/.tekton/tasks.yml

## GitHub Actions verification

After pushing the workflow, open https://github.com/ThePranish03/product-catalogue-final-project/actions
Select **Product Catalogue CI**, open the newest run, and verify these steps are green:
- Checkout repository
- Set up Python
- Install dependencies
- Lint with flake8
- Run unit tests with pytest

Preserve the actual run log from the Actions run for the terminal-output item. Do not submit fabricated success output. A workflow run is only successful when GitHub reports its conclusion as `success`.

## OpenShift evidence still to capture from the target cluster

Save genuine screenshots using these exact filenames (PNG format is recommended):
- `oc-pipelines-console-pvc-details.png`: OpenShift console → Storage → PersistentVolumeClaims → select the pipeline workspace PVC. Include name, namespace, status, capacity, access mode, and storage class.
- `oc-pipelines-oc-final.png`: OpenShift Pipelines page showing the pipeline named `oc-pipelines-oc-final` and its Tasks/definition.
- `oc-pipelines-oc-green.png`: PipelineRuns page showing a completed successful run (Succeeded) for `oc-pipelines-oc-final`.

## OpenShift terminal evidence

Use the project/namespace that contains the OpenShift Pipeline. Capture actual command output, for example:

```bash
oc project
oc get pvc
oc get pipeline oc-pipelines-oc-final -o yaml
oc get pipelineruns
oc describe pipelinerun <successful-pipelinerun-name>
oc logs -f pipelinerun/<successful-pipelinerun-name> -n <namespace>
```

For the application logs item, use the real application pod selected by the deployment:

```bash
oc get pods
oc logs deployment/<application-deployment-name> --all-containers=true --tail=200
```

Paste the unedited output into the submission. Replace placeholders with names returned by your cluster. Do not claim an OpenShift run succeeded until the PipelineRun status is `Succeeded`.

## Pipeline integration note

The Tekton task file supplies the requested `cleanup` and test tasks. A cluster administrator or project user must apply these task definitions and create/configure the Pipeline, PVC/workspace, Git credentials (if required), and PipelineRun in the OpenShift cluster. This GitHub connection cannot access your OpenShift console or cluster credentials, so it cannot capture genuine PVC, Pipeline, PipelineRun, or application-log evidence.