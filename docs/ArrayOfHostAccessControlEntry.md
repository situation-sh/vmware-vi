# ArrayOfHostAccessControlEntry

A boxed array of *HostAccessControlEntry*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAccessControlEntry]**](HostAccessControlEntry.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_access_control_entry import ArrayOfHostAccessControlEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAccessControlEntry from a JSON string
array_of_host_access_control_entry_instance = ArrayOfHostAccessControlEntry.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAccessControlEntry.to_json()

# convert the object into a dict
array_of_host_access_control_entry_dict = array_of_host_access_control_entry_instance.to_dict()
# create an instance of ArrayOfHostAccessControlEntry from a dict
array_of_host_access_control_entry_form_dict = array_of_host_access_control_entry.from_dict(array_of_host_access_control_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


