# IscsiPortInfoPathStatusEnum

Possible values: - `notUsed`: There are no paths on this Virtual NIC - `active`: All paths on this Virtual NIC are standby paths from SCSI stack   perspective. - `standBy`: One or more paths on the Virtual NIC are active paths to   storage.      Unbinding this Virtual NIC will cause storage path   transitions. - `lastActive`: One or more paths on the Virtual NIC is the last active   path to a particular storage device.    ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


