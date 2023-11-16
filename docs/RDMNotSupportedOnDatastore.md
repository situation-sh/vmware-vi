# RDMNotSupportedOnDatastore

The virtual machine is configured with a Raw Disk Mapping.  This is not supported on the datastore.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the RDM device that would have its backing placed on the datastore.  This is not guaranteed to be the only such device.  ***Since:*** VI API 2.5  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**datastore_name** | **str** | The name of the datastore.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.rdm_not_supported_on_datastore import RDMNotSupportedOnDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of RDMNotSupportedOnDatastore from a JSON string
rdm_not_supported_on_datastore_instance = RDMNotSupportedOnDatastore.from_json(json)
# print the JSON string representation of the object
print RDMNotSupportedOnDatastore.to_json()

# convert the object into a dict
rdm_not_supported_on_datastore_dict = rdm_not_supported_on_datastore_instance.to_dict()
# create an instance of RDMNotSupportedOnDatastore from a dict
rdm_not_supported_on_datastore_form_dict = rdm_not_supported_on_datastore.from_dict(rdm_not_supported_on_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


