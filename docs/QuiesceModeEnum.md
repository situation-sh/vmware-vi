# QuiesceModeEnum

Quiescing is a boolean flag in *ReplicationConfigSpec* and QuiesceModeType describes the supported quiesce mode for *VirtualMachine*.  If application quiescing fails, HBR would attempt filesystem quiescing and if even filesystem quiescing fails, then we would just create a crash consistent instance.  Possible values: - `application`: HBR supports application quescing for this   *VirtualMachine*. - `filesystem`: HBR supports filesystem quescing for this   *VirtualMachine*. - `none`: HBR does not support quescing for this   *VirtualMachine*.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


