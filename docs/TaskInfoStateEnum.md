# TaskInfoStateEnum

List of possible states of a task.  Possible values: - `queued`: When there are too many tasks for threads to handle. - `running`: When the busy thread is freed from its current task by   finishing the task, it picks a queued task to run.      Then the queued tasks are marked as running. - `success`: When a running task has completed. - `error`: When a running task has encountered an error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


