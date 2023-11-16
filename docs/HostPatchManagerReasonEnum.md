# HostPatchManagerReasonEnum

Reasons why an update is not applicable to the ESX host.  Possible values: - `obsoleted`: The update is made obsolete by other patches installed on the host. - `missingPatch`: The update depends on another update that is neither installed   nor in the scanned list of updates. - `missingLib`: The update depends on certain libraries or RPMs that are not   available. - `hasDependentPatch`: The update depends on an update that is not installed but is   in the scanned list of updates. - `conflictPatch`: The update conflicts with certain updates that are already   installed on the host. - `conflictLib`: The update conflicts with RPMs or libraries installed on the   host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


