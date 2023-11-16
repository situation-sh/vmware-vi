# VirtualMachineWindowsQuiesceSpecVssBackupContextEnum

The VSS Snapshot Context VSS\\_SNAPSHOT\\_CONTEXT values not listed below are not implemented.  Possible values: - `ctx_auto`: The context value indicates auto selection of VSS snapshot context.      The ctx\\_backup may make Windows VSS-aware applications quiescing during   backup. The ctx\\_auto makes VMTools select ctx\\_file\\_share\\_backup context   if ctx\\_backup is not available. - `ctx_backup`: Indicate VSS\\_CTX\\_BACKUP. - `ctx_file_share_backup`: Indicate VSS\\_CTX\\_FILE\\_SHARE\\_BACKUP.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


