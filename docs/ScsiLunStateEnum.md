# ScsiLunStateEnum

The Operational state of the LUN  Possible values: - `unknownState`: The LUN state is unknown. - `ok`: The LUN is on and available. - `error`: The LUN is dead and/or not reachable. - `off`: The LUN is off.      ***Since:*** vSphere API 4.0 - `quiesced`: The LUN is inactive.      ***Since:*** vSphere API 4.0 - `degraded`: One or more paths to the LUN are down, but I/O   is still possible.      Further path failures may   result in lost connectivity. - `lostCommunication`: No more paths are available to the LUN. - `timeout`: All Paths have been down for the timeout condition   determined by a user-configurable host advanced option.      ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


