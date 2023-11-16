# HostCryptoStateEnum

Defines a host's encryption state  Possible values: - `incapable`: The host is not safe for receiving sensitive material. - `prepared`: The host is prepared for receiving sensitive material   but does not have a host key set yet. - `safe`: The host is crypto safe and has a host key set. - `pendingIncapable`: The host is explicitly crypto disabled and pending reboot to be   applied.      When host is in this state, creating encrypted virtual   machines is not allowed, but still need a reboot to totally clean   up and enter incapable state.      ***Since:*** vSphere API 7.0  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


