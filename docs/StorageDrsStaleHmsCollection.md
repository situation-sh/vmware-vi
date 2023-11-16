# StorageDrsStaleHmsCollection

This fault is thrown when Storage DRS action for relocating HMS collection of replica disks does not correspond to current HMS inventory configuration and hence, is rejected by HMS service.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_stale_hms_collection import StorageDrsStaleHmsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsStaleHmsCollection from a JSON string
storage_drs_stale_hms_collection_instance = StorageDrsStaleHmsCollection.from_json(json)
# print the JSON string representation of the object
print StorageDrsStaleHmsCollection.to_json()

# convert the object into a dict
storage_drs_stale_hms_collection_dict = storage_drs_stale_hms_collection_instance.to_dict()
# create an instance of StorageDrsStaleHmsCollection from a dict
storage_drs_stale_hms_collection_form_dict = storage_drs_stale_hms_collection.from_dict(storage_drs_stale_hms_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


