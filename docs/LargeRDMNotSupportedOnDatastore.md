# LargeRDMNotSupportedOnDatastore

The virtual machine is configured with a 2TB+ Raw Disk Mapping.  This is not supported on the datastore.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the 2TB+ RDM device that would have its backing placed on the datastore.  This is not guaranteed to be the only such device.  ***Since:*** vSphere API 5.0  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**datastore_name** | **str** | The name of the datastore.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.large_rdm_not_supported_on_datastore import LargeRDMNotSupportedOnDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of LargeRDMNotSupportedOnDatastore from a JSON string
large_rdm_not_supported_on_datastore_instance = LargeRDMNotSupportedOnDatastore.from_json(json)
# print the JSON string representation of the object
print LargeRDMNotSupportedOnDatastore.to_json()

# convert the object into a dict
large_rdm_not_supported_on_datastore_dict = large_rdm_not_supported_on_datastore_instance.to_dict()
# create an instance of LargeRDMNotSupportedOnDatastore from a dict
large_rdm_not_supported_on_datastore_form_dict = large_rdm_not_supported_on_datastore.from_dict(large_rdm_not_supported_on_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


