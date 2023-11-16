# OvfCreateImportSpecParamsDiskProvisioningTypeEnum

Types of disk provisioning that can be set for the disk in the deployed OVF package.  Possible values: - `monolithicSparse`: A sparse (allocate on demand) monolithic disk.      Disks in this format can   be used with other VMware products. - `monolithicFlat`: A preallocated monolithic disk.      Disks in this format can be used with   other VMware products. - `twoGbMaxExtentSparse`: A sparse (allocate on demand) disk with 2GB maximum extent size.      Disks in this format can be used with other VMware products. The 2GB   extent size makes these disks easier to burn to dvd or use on   filesystems that don't support large files. - `twoGbMaxExtentFlat`: A preallocated disk with 2GB maximum extent size.      Disks in this format   can be used with other VMware products. The 2GB extent size   makes these disks easier to burn to dvd or use on filesystems that   don't support large files. - `thin`: Space required for thin-provisioned virtual disk is allocated and   zeroed on demand as the space is used. - `thick`: A thick disk has all space allocated at creation time   and the space is zeroed on demand as the space is used. - `seSparse`: A sparse (allocate on demand) format with additional space   optimizations.      ***Since:*** vSphere API 5.1 - `eagerZeroedThick`: An eager zeroed thick disk has all space allocated and wiped clean   of any previous contents on the physical media at creation time.      Such disks may take longer time during creation compared to other   disk formats.      ***Since:*** vSphere API 5.0 - `sparse`: Depending on the host type, Sparse is mapped to either   MonolithicSparse or Thin. - `flat`: Depending on the host type, Flat is mapped to either   MonolithicFlat or Thick.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


