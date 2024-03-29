# AutoStartWaitHeartbeatSettingEnum

Determines if the virtual machine should start after receiving a heartbeat, ignore heartbeats and start after the startDelay has elapsed, or follow the system default before powering on.  When a virtual machine is next in the start order, the system either waits a specified period of time for a virtual machine to power on or it waits until it receives a successful heartbeat from a powered on virtual machine. By default, this is set to no.  Possible values: - `yes`: The system waits until receiving a heartbeat before powering on the next   machine in the order. - `no`: The system does not wait to receive a heartbeat before powering on the next   machine in the order.      This is the default setting. - `systemDefault`: The system uses the default value to determine whether or not to wait to   receive a heartbeat before powering on the next machine in the order. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


