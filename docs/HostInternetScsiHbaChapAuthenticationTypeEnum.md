# HostInternetScsiHbaChapAuthenticationTypeEnum

The type of CHAP authentication setting to use.  prohibited : do not use CHAP. preferred : use CHAP if successfully negotiated, but allow non-CHAP connections as fallback discouraged : use non-CHAP, but allow CHAP connectsion as fallback required : use CHAP for connection strictly, and fail if CHAP negotiation fails. Defaults to preferred on first configuration if unspecified.  Possible values: - `chapProhibited` - `chapDiscouraged` - `chapPreferred` - `chapRequired`  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


