# BaseConfigInfoDiskFileBackingInfoProvisioningTypeEnum

Provisioning type constants.  Possible values: - `thin`: Space required for thin-provisioned virtual disk is allocated   and zeroed on demand as the space is used. - `eagerZeroedThick`: An eager zeroed thick virtual disk has all space allocated and   wiped clean of any previous contents on the physical media at   creation time.      Such virtual disk may take longer time   during creation compared to other provisioning formats. - `lazyZeroedThick`: A thick virtual disk has all space allocated at creation time.      This space may contain stale data on the physical media.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


