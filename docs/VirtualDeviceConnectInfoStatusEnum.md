# VirtualDeviceConnectInfoStatusEnum

Specifies the connectable virtual device status.  Possible values: - `ok`: The device is working correctly. - `recoverableError`: The device has reported a recoverable error.      For example,   attempting to connect to floppy device that is being used by   another virtual machine or some other program would result in   this status. - `unrecoverableError`: The device cannot be used.      For example, attempting to connect to   a floppy device that does not exist would result in this status. - `untried`: The device status is unknown, or it has not been requested to   connect when the VM is powered on.    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


