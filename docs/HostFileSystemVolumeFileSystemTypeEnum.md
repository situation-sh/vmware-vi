# HostFileSystemVolumeFileSystemTypeEnum

Type of file system volume.  Possible values: - `VMFS`: VMware File System (ESX Server only).      If this is set,   the type of the file system volume is VMFS. - `NFS`: Network file system v3 linux &amp; esx servers only.      If this is   set, the type of the file system volume is NFS v3. - `NFS41`: Network file system v4.1 linux &amp; esx servers only.      If this is   set, the type of the file system volume is NFS v4.1 or later.      ***Since:*** vSphere API 6.0 - `CIFS`: Common Internet File System.      If this is set, the type of the   file system volume is Common Internet File System. - `vsan`: VSAN File System (ESX Server only).      ***Since:*** vSphere API 6.0 - `VFFS`: vFlash File System (ESX Server only).      If this is set, the type of the file system volume is VFFS.      ***Since:*** vSphere API 6.0 - `VVOL`: vvol File System (ESX Server only).      ***Since:*** vSphere API 6.0 - `PMEM`: Persistent Memory File System (ESX Server only).      ***Since:*** vSphere API 6.7 - `vsanD`: VSAN direct file system.      ***Since:*** vSphere API 7.0.1.0 - `OTHER`: Used if the file system is not one of the specified file systems.      Used mostly for reporting purposes. The other types are described   by the otherType property.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


