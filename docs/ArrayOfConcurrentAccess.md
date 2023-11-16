# ArrayOfConcurrentAccess

A boxed array of *ConcurrentAccess*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ConcurrentAccess]**](ConcurrentAccess.md) |  | 

## Example

```python
from vmware_vi.models.array_of_concurrent_access import ArrayOfConcurrentAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfConcurrentAccess from a JSON string
array_of_concurrent_access_instance = ArrayOfConcurrentAccess.from_json(json)
# print the JSON string representation of the object
print ArrayOfConcurrentAccess.to_json()

# convert the object into a dict
array_of_concurrent_access_dict = array_of_concurrent_access_instance.to_dict()
# create an instance of ArrayOfConcurrentAccess from a dict
array_of_concurrent_access_form_dict = array_of_concurrent_access.from_dict(array_of_concurrent_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


