# ProfileExecuteResultStatusEnum

Defines the result status values for a *HostProfile*.*HostProfile.ExecuteHostProfile* operation.  The result data is contained in the *ProfileExecuteResult* data object.  Possible values: - `success`: Profile execution was successful.      You can use the output configuration data   to apply the profile to a host. - `needInput`: Additional data is required to complete the operation.      The data requirements are defined in the list of policy options for the profile   (*ApplyProfile*.*ApplyProfile.policy*\\[\\]). - `error`: Profile execution generated an error.      See *ProfileExecuteResult*.*ProfileExecuteResult.error*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


