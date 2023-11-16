# VirtualMachineTicketTypeEnum

The virtual machine ticket type.  Possible values: - `mks`:       Deprecated as of vSphere API 8.0. Use *webmks* instead.      Remote mouse-keyboard-screen ticket. - `device`:       Deprecated as of vSphere 8.0 API. Use *webRemoteDevice*   instead.      Remote device ticket. - `guestControl`:       Deprecated as of vSphere 6.6.3 API. Use   *GuestOperationsManager* instead.      Guest operation ticket. - `dnd`: Drag and drop ticket.      ***Since:*** vim dnd version - `webmks`: Mouse-keyboard-screen over WebSocket ticket.      MKS protocol is VNC (a.k.a. RFB) protocol with   VMware extensions; the protocol gracefully degrades   to standard VNC if extensions are not available.   wss://{Ticket.host}/ticket/{Ticket.ticket}      ***Since:*** vSphere API 6.0 - `guestIntegrity`: Guest Integrity over WebSocket ticket.      This ticket grants the client read-only access to guest integrity   messages and alerts.      ***Since:*** vSphere API 6.7 - `webRemoteDevice`: Remote device over WebSocket ticket.      ***Since:*** vSphere API 7.0  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


