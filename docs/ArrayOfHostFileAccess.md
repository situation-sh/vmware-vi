# ArrayOfHostFileAccess

A boxed array of *HostFileAccess*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostFileAccess]**](HostFileAccess.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_file_access import ArrayOfHostFileAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostFileAccess from a JSON string
array_of_host_file_access_instance = ArrayOfHostFileAccess.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostFileAccess.to_json()

# convert the object into a dict
array_of_host_file_access_dict = array_of_host_file_access_instance.to_dict()
# create an instance of ArrayOfHostFileAccess from a dict
array_of_host_file_access_form_dict = array_of_host_file_access.from_dict(array_of_host_file_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


