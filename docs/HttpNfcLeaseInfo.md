# HttpNfcLeaseInfo

This class holds information about the lease, such as the entity covered by the lease, and HTTP URLs for up/downloading file backings.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lease** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**device_url** | [**List[HttpNfcLeaseDeviceUrl]**](HttpNfcLeaseDeviceUrl.md) | The deviceUrl property contains a mapping from logical device keys to URLs.  ***Since:*** vSphere API 4.0  | [optional] 
**total_disk_capacity_in_kb** | **int** | Total capacity in kilobytes of all disks in all Virtual Machines covered by this lease.  This can be used to track progress when transferring disks.  ***Since:*** vSphere API 4.0  | 
**lease_timeout** | **int** | Number of seconds before the lease times out.  The client extends the lease by calling *HttpNfcLease.HttpNfcLeaseProgress* before the timeout has expired.  ***Since:*** vSphere API 4.0  | 
**host_map** | [**List[HttpNfcLeaseDatastoreLeaseInfo]**](HttpNfcLeaseDatastoreLeaseInfo.md) | Map of URLs for leased hosts for a given datastore.  This is used to look up multi-POST-capable hosts for a datastore.  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.http_nfc_lease_info import HttpNfcLeaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseInfo from a JSON string
http_nfc_lease_info_instance = HttpNfcLeaseInfo.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseInfo.to_json()

# convert the object into a dict
http_nfc_lease_info_dict = http_nfc_lease_info_instance.to_dict()
# create an instance of HttpNfcLeaseInfo from a dict
http_nfc_lease_info_form_dict = http_nfc_lease_info.from_dict(http_nfc_lease_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


