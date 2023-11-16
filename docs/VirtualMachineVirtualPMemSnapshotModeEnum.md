# VirtualMachineVirtualPMemSnapshotModeEnum

The set of supported snapshot modes for VMs configured with NVDIMMs.  Possible values: - `independent_persistent`: The data on virtual NVDIMMs are not affected by snapshot reverts.      Writes to virtual NVDIMMs after a snapshot is taken cannot be   reverted to the snapshotted state. - `independent_eraseonrevert`: Virtual NVDIMMs are erased and recreated upon snapshot reverts.    ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


