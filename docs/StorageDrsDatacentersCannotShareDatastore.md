# StorageDrsDatacentersCannotShareDatastore

This fault is thrown when one datastore using Storage DRS is added to two different datacenters.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_datacenters_cannot_share_datastore import StorageDrsDatacentersCannotShareDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsDatacentersCannotShareDatastore from a JSON string
storage_drs_datacenters_cannot_share_datastore_instance = StorageDrsDatacentersCannotShareDatastore.from_json(json)
# print the JSON string representation of the object
print StorageDrsDatacentersCannotShareDatastore.to_json()

# convert the object into a dict
storage_drs_datacenters_cannot_share_datastore_dict = storage_drs_datacenters_cannot_share_datastore_instance.to_dict()
# create an instance of StorageDrsDatacentersCannotShareDatastore from a dict
storage_drs_datacenters_cannot_share_datastore_form_dict = storage_drs_datacenters_cannot_share_datastore.from_dict(storage_drs_datacenters_cannot_share_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


