# HostRdmaDeviceConnectionStateEnum

Possible RDMA device connection states.  These correspond to possible link states as defined by the Infiniband (TM) specification.  Further details can be found in: - \"Infiniband (TM) Architecture Specification, Volume 1\"   section 7.2 \"Link states\"    Possible values: - `unknown`: Connection state unknown.      Indicates that the driver returned   unexpected or no connection state information. - `down`: Device down.      Indicates that both the logical link and   underlying physical link are down. Packets   are discarded. - `init`: Device initializing.      Indicates that the physical link is up, but   the logical link is still initializing.   Only subnet management and flow control link   packets can be received and transmitted. - `armed`: Device armed.      Indicates that the physical link is up, but   the logical link is not yet fully configured.   Packets can be received, but non-SMPs   (subnet management packets) to be sent are discarded. - `active`: Device active.      Indicates that both the physical and logical   link are up. Packets can be transmitted and received. - `activeDefer`: Device in active defer state.      Indicates that the logical link was active, but the   physical link has suffered a failure. If it recovers   within a timeout, the connection state will return to active,   otherwise it will move to down.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


