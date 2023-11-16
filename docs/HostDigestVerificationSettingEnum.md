# HostDigestVerificationSettingEnum

This enum specifies the supported digest verification settings.  For NVMe over TCP connections, both header and data digests may be requested during the process of establishing the connection. For details, see: - NVM Express Technical Proposal 8000 - NVMe/TCP Transport,   Section 7.4.6, \"PDU Header and Data Digests\"    Possible values: - `digestDisabled`: Both header and data digest verification are disabled. - `headerOnly`: Only header digest verification is enabled. - `dataOnly`: Only data digest verification is enabled. - `headerAndData`: Both header and data digest verification are enabled.    ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


