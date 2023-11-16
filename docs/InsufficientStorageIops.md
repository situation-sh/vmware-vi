# InsufficientStorageIops

The datastore does not have enough IOPs capacity for running the virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unreserved_iops** | **int** | The IOPs available on the datastore  ***Since:*** vSphere API 6.0  | 
**requested_iops** | **int** | The IOPs resource amount requested in the failed operation  ***Since:*** vSphere API 6.0  | 
**datastore_name** | **str** | Name of the datastore with insufficient capacity  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.insufficient_storage_iops import InsufficientStorageIops

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientStorageIops from a JSON string
insufficient_storage_iops_instance = InsufficientStorageIops.from_json(json)
# print the JSON string representation of the object
print InsufficientStorageIops.to_json()

# convert the object into a dict
insufficient_storage_iops_dict = insufficient_storage_iops_instance.to_dict()
# create an instance of InsufficientStorageIops from a dict
insufficient_storage_iops_form_dict = insufficient_storage_iops.from_dict(insufficient_storage_iops_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


