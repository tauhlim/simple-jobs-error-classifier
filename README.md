# simple-jobs-error-classifier
Classify your Databricks Job failures (or anything really) with AI Functions

# Introduction

Sometimes, our batch jobs fail. It sucks, but it happens. What matters is whether we can streamline the process to triage, troubleshoot, and fix the batch jobs.

[Databricks Assistant](https://www.databricks.com/product/databricks-assistant) provides a good out-of-the-box experience for individual job task failures, but
1. You have to be in the product, at the specific failed tasks to get insights from Databricks Assistant
1. There isn't an Assistant API to pass detailed error messages and ask for a fix.

_Sidenote: Databricks Team - Assistant API? 🥺_

# Simple Solution Overview

1. Databricks System Tables (`system.lakeflow.job_task_run_timeline`) has data on each job run, and the status of the run.
1. Detailed error messages can be retrieved from the Databricks Jobs REST API / Databricks SDK
1. Combine the 2 sources and save as Delta Table
1. Run pre-built [AI functions](https://learn.microsoft.com/en-us/azure/databricks/large-language-models/ai-functions) on the detailed error message.

# Disclaimer
This code is experimental that is not yet supported by Databricks. It should not be used in production environments and is provided strictly for educational and experimental purposes.