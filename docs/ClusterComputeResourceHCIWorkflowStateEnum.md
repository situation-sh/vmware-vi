# ClusterComputeResourceHCIWorkflowStateEnum

HCIWorkflowState identifies the state of the cluser from the perspective of HCI workflow.  The workflow begins with in\\_progress mode and can transition to 'done' or 'invalid', both of which are terminal states.  Possible values: - `in_progress`: Indicates cluster is getting configured or will be configured. - `done`: Indicates cluster configuration is complete. - `invalid`: Indicates the workflow was abandoned on the cluster before the   configuration could complete.    ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


