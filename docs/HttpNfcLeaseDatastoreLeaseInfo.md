# HttpNfcLeaseDatastoreLeaseInfo

For a given datastore, represented by datastoreKey, contains a list of leased multi-POST-capable hosts connected to it.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_key** | **str** | Datastore key.  ***Since:*** vSphere API 4.1  | 
**hosts** | [**List[HttpNfcLeaseHostInfo]**](HttpNfcLeaseHostInfo.md) | List of hosts connected to this datastore and covered by this lease.  The hosts in this list are multi-POST-capable, and any one of them can be used to transfer disks on this datastore.  ***Since:*** vSphere API 4.1  | 

## Example

```python
from vmware_vi.models.http_nfc_lease_datastore_lease_info import HttpNfcLeaseDatastoreLeaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HttpNfcLeaseDatastoreLeaseInfo from a JSON string
http_nfc_lease_datastore_lease_info_instance = HttpNfcLeaseDatastoreLeaseInfo.from_json(json)
# print the JSON string representation of the object
print HttpNfcLeaseDatastoreLeaseInfo.to_json()

# convert the object into a dict
http_nfc_lease_datastore_lease_info_dict = http_nfc_lease_datastore_lease_info_instance.to_dict()
# create an instance of HttpNfcLeaseDatastoreLeaseInfo from a dict
http_nfc_lease_datastore_lease_info_form_dict = http_nfc_lease_datastore_lease_info.from_dict(http_nfc_lease_datastore_lease_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


