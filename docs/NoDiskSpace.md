# NoDiskSpace

This fault is thrown when an operation fails because of insufficient disk space. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | **str** | The name of the datastore with insufficient disk space.  | 

## Example

```python
from vmware_vi.models.no_disk_space import NoDiskSpace

# TODO update the JSON string below
json = "{}"
# create an instance of NoDiskSpace from a JSON string
no_disk_space_instance = NoDiskSpace.from_json(json)
# print the JSON string representation of the object
print NoDiskSpace.to_json()

# convert the object into a dict
no_disk_space_dict = no_disk_space_instance.to_dict()
# create an instance of NoDiskSpace from a dict
no_disk_space_form_dict = no_disk_space.from_dict(no_disk_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


