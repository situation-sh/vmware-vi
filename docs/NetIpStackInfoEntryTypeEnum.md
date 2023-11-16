# NetIpStackInfoEntryTypeEnum

IP Stack keeps state on entries in IpNetToMedia table to perform physical address lookups for IP addresses.  Here are the standard states per @see RFC 4293 ipNetToMediaType.  Possible values: - `other`: This implementation is reporting something other than   what states are listed below. - `invalid`: The IP Stack has marked this entry as not useable. - `dynamic`: This entry has been learned using ARP or NDP. - `manual`: This entry was set manually.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


