# VAppAutoStartActionEnum

Possible values: - `none`: No action is taken for this virtual machine.      This virtual machine is   not a part of the auto-start sequence. This can be used for both auto-start   and auto-start settings. - `powerOn`: This virtual machine is powered on when it is next in the auto-start order. - `powerOff`: This virtual machine is powered off when it is next in the auto-stop order.      This is the default stopAction. - `guestShutdown`: The guest operating system for a virtual machine is shut down when that   virtual machine in next in the auto-stop order. - `suspend`: This virtual machine is suspended when it is next in the auto-stop order.    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


