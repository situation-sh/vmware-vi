# HostProfileManagerAnswerFileStatusEnum

The *HostProfileManagerAnswerFileStatus_enum* enum defines possible values for answer file status.  Possible values: - `valid`: Answer file is valid. - `invalid`: Answer file is not valid.      The file is either missing or incomplete.   - To produce an answer file, pass host-specific data (user input) to the     *HostProfileManager*.*HostProfileManager.ApplyHostConfig_Task*     method.   - To produce a complete answer file, call the     *HostProfile*.*HostProfile.ExecuteHostProfile*     method and fill in any missing parameters in the returned     *ProfileExecuteResult*.*ProfileExecuteResult.requireInput*     list. After you execute the profile successfully, you can pass the complete required     input list to the apply method. - `unknown`: Answer file status is not known.    ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


