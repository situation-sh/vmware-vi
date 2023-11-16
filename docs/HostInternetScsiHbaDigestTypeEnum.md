# HostInternetScsiHbaDigestTypeEnum

The type of integrity checks to use.  The digest setting for header and data traffic can be separately configured. prohibited : do not use digest. preferred : use digest if successfully negotiated, but skip the use of digest otherwise. discouraged : do not use digest if target allows, otherwise use digest. required : use digest strictly, and fail if target does not support digest. Defaults to preferred on first configuration if unspecified.  Possible values: - `digestProhibited` - `digestDiscouraged` - `digestPreferred` - `digestRequired`  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


