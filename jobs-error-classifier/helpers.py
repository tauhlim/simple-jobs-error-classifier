from databricks.sdk import WorkspaceClient
from typing import Dict, List

def get_errors_for_task(run_id: int, w: WorkspaceClient) -> Dict[str, str]:
  task_run_output = w.jobs.get_run_output(run_id = run_id).as_dict()
  assert task_run_output.get("error") is not None, "Job run output has no errors"
  return {
    "error": task_run_output.get("error"),
    "error_trace": task_run_output.get("error_trace")
  }

