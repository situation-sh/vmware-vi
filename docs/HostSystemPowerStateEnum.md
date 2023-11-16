# HostSystemPowerStateEnum

Defines a host's power state.  Possible values: - `poweredOn`: The host is powered on.      A host that is entering standby mode   *entering* is also in this state. - `poweredOff`: The host was specifically powered off by the user through   VirtualCenter.      This state is not a cetain state, because   after VirtualCenter issues the command to power off the host,   the host might crash, or kill all the processes but fail to   power off. - `standBy`: The host was specifically put in standby mode, either   explicitly by the user, or automatically by DPM.      This state   is not a cetain state, because after VirtualCenter issues the   command to put the host in standby state, the host might   crash, or kill all the processes but fail to power off. A host   that is exiting standby mode *exiting*   is also in this state. - `unknown`: If the host is disconnected, or notResponding, we cannot   possibly have knowledge of its power state.      Hence, the host   is marked as unknown.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


