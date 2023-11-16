# HostMountInfoMountFailedReasonEnum

NFS mount request can be failed due to a number of reasons as defined in this enum *HostMountInfoMountFailedReason_enum*.  The reason for the mount failure is reported in *HostMountInfo.mountFailedReason*. This is applicable only for those datastores to which mount retry is configured.  Possible values: - `CONNECT_FAILURE`: Failed to get port or connect.      Or MOUNT/FSINFO RPC failed. - `MOUNT_NOT_SUPPORTED`: Server doesn't support MOUNT\\_PROGRAM/MOUNT\\_PROGRAM\\_VERSION. - `NFS_NOT_SUPPORTED`: Server doesn't support NFS\\_PROGRAM/NFS\\_PROGRAM\\_VERSION. - `MOUNT_DENIED`: No permission to mount the remote volume or it doesn't exist. - `MOUNT_NOT_DIR`: Remote path not a directory. - `VOLUME_LIMIT_EXCEEDED`: Maximum NFS volumes have been mounted. - `CONN_LIMIT_EXCEEDED`: Maximum connections for NFS has been reached. - `MOUNT_EXISTS`: Volume already mounted or a different mount exists with same label. - `OTHERS`: Any other reason which is not present in above list. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


