# HostPatchManagerIntegrityStatusEnum

The integrity validation status.  Possible values: - `validated`: The update is successfully validated. - `keyNotFound`: The integrity can not be verified since a public key to   verify the update cannot be found. - `keyRevoked`: A public key to verify the update has been revoked. - `keyExpired`: A public key to verify the update is expired. - `digestMismatch`: A digital signature of the update does not match. - `notEnoughSignatures`: Not enough signed signatures on the update. - `validationError`: The integrity validation failed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


