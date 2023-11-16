# ArrayOfHostSpecification

A boxed array of *HostSpecification*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSpecification]**](HostSpecification.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_specification import ArrayOfHostSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSpecification from a JSON string
array_of_host_specification_instance = ArrayOfHostSpecification.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSpecification.to_json()

# convert the object into a dict
array_of_host_specification_dict = array_of_host_specification_instance.to_dict()
# create an instance of ArrayOfHostSpecification from a dict
array_of_host_specification_form_dict = array_of_host_specification.from_dict(array_of_host_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


