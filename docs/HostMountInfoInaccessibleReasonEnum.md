# HostMountInfoInaccessibleReasonEnum

A datastore can become inaccessible due to a number of reasons as defined in this enum *HostMountInfoInaccessibleReason_enum*.  The reason for a datastore being inaccessible is reported in *HostMountInfo.inaccessibleReason*. APD (\"All Paths Down\") is a condition where a SAN or NFS storage has become inaccessible for unknown reasons. It only indicates loss of connectivity and does not indicate storage device failure or LUN removal (Permanent Device Loss or PDL) A difference between APD and PDL is that APD may recover in which case all use cases will start to work as before. In case of PDL the failed datastore/device is unlikely to recover and hence the device path information and data cache will be emptied. If the PDL condition recovers, the failed datastores have to be added back to the host. Once in PDL a datastore cannot be added back until there are no longer any open files on the datastore. PDL is not linked to the APD and can happen at any time with or without APD preceding. If APD and PDL occur at the same time, APD will be reported first. Once (and if) the APD condition clears, PermanentDataLoss will be reported if PDL condition still exists.  Possible values: - `AllPathsDown_Start`: AllPathsDown\\_Start value is reported when all paths down state is detected - `AllPathsDown_Timeout`: After a wait for a system default time (which is user modifiable)   to ascertain the state is indeed an APD, AllPathsDown\\_Timeout property   is reported.      The host advanced option used to set timeout period   is \"/Misc/APDTimeout\"   After the datastore property is set to AllPathsDown\\_Timeout, all data i/o   to the datastore will be fast-failed (failed immediately). - `PermanentDeviceLoss`: A PDL condition is reported as PermanentDeviceLoss.    ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


