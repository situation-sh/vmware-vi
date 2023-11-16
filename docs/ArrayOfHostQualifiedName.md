# ArrayOfHostQualifiedName

A boxed array of *HostQualifiedName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostQualifiedName]**](HostQualifiedName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_qualified_name import ArrayOfHostQualifiedName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostQualifiedName from a JSON string
array_of_host_qualified_name_instance = ArrayOfHostQualifiedName.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostQualifiedName.to_json()

# convert the object into a dict
array_of_host_qualified_name_dict = array_of_host_qualified_name_instance.to_dict()
# create an instance of ArrayOfHostQualifiedName from a dict
array_of_host_qualified_name_form_dict = array_of_host_qualified_name.from_dict(array_of_host_qualified_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


