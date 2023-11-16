# SharesLevelEnum

Simplified shares notation.  These designations have different meanings for different resources.  Possible values: - `low`: For CPU: Shares = 500 \\* number of virtual CPUs     For Memory: Shares = 5 \\* virtual machine memory size in megabytes     For Disk: Shares = 500     For Network: Shares = 0.25 \\* *DVSFeatureCapability.networkResourcePoolHighShareValue* - `normal`: For CPU: Shares = 1000 \\* number of virtual CPUs     For Memory: Shares = 10 \\* virtual machine memory size in megabytes     For Disk: Shares = 1000     For Network: Shares = 0.5 \\* *DVSFeatureCapability.networkResourcePoolHighShareValue* - `high`: For CPU: Shares = 2000 \\* number of virtual CPUs     For Memory: Shares = 20 \\* virtual machine memory size in megabytes     For Disk: Shares = 2000     For Network: Shares = *DVSFeatureCapability.networkResourcePoolHighShareValue* - `custom`: If you specify <code>custom</code> for the *SharesInfo.level* property, when there is resource contention the Server uses the *SharesInfo.shares* value to determine resource allocation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


