# ArrayOfHostSubSpecification

A boxed array of *HostSubSpecification*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSubSpecification]**](HostSubSpecification.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sub_specification import ArrayOfHostSubSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSubSpecification from a JSON string
array_of_host_sub_specification_instance = ArrayOfHostSubSpecification.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSubSpecification.to_json()

# convert the object into a dict
array_of_host_sub_specification_dict = array_of_host_sub_specification_instance.to_dict()
# create an instance of ArrayOfHostSubSpecification from a dict
array_of_host_sub_specification_form_dict = array_of_host_sub_specification.from_dict(array_of_host_sub_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


