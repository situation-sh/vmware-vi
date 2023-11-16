# VsanHostDiskResultStateEnum

Values used for indicating a disk's status for use by the VSAN service.  See also *VsanHostDiskResult.state*.  Possible values: - `inUse`: Disk is currently in use by the VSAN service.      A disk may be considered in use by the VSAN service regardless of   whether the VSAN service is enabled. As long as a disk is in use   by VSAN, it is reserved exclusively for VSAN and may not be used   for other purposes.      See also *VsanHostDiskResult.error*. - `eligible`: Disk is considered eligible for use by the VSAN service,   but is not currently in use. - `ineligible`: Disk is considered ineligible for use by the VSAN service,   and is not currently in use.      See also *VsanHostDiskResult.error*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


