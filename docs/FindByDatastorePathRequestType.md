# FindByDatastorePathRequestType

The parameters of *SearchIndex.FindByDatastorePath*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**path** | **str** | A datastore path to the .vmx file for the virtual machine.  | 

## Example

```python
from vmware_vi.models.find_by_datastore_path_request_type import FindByDatastorePathRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of FindByDatastorePathRequestType from a JSON string
find_by_datastore_path_request_type_instance = FindByDatastorePathRequestType.from_json(json)
# print the JSON string representation of the object
print FindByDatastorePathRequestType.to_json()

# convert the object into a dict
find_by_datastore_path_request_type_dict = find_by_datastore_path_request_type_instance.to_dict()
# create an instance of FindByDatastorePathRequestType from a dict
find_by_datastore_path_request_type_form_dict = find_by_datastore_path_request_type.from_dict(find_by_datastore_path_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


