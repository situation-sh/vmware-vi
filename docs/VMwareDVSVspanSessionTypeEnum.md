# VMwareDVSVspanSessionTypeEnum

Distributed Port Mirroring session types.  Possible values: - `mixedDestMirror`:       Deprecated as of vSphere API 5.1.      In mixedDestMirror session, Distributed Ports can be used as source entities,   and both Distributed Ports and Uplink Ports Name can be used as destination entities. - `dvPortMirror`: In dvPortMirror session, Distributed Ports can be used as both source   and destination entities. - `remoteMirrorSource`: In remoteMirrorSource session, Distributed Ports can be used as source entities,   and uplink ports name can be used as destination entities. - `remoteMirrorDest`: In remoteMirrorDest session, vlan Ids can be used as source entities,   and Distributed Ports can be used as destination entities. - `encapsulatedRemoteMirrorSource`: In encapsulatedRemoteMirrorSource session, Distributed Ports can be used as source entities,   and Ip address can be used as destination entities.    ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


