# ArrayOfInsufficientDisks

A boxed array of *InsufficientDisks*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientDisks]**](InsufficientDisks.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_disks import ArrayOfInsufficientDisks

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientDisks from a JSON string
array_of_insufficient_disks_instance = ArrayOfInsufficientDisks.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientDisks.to_json()

# convert the object into a dict
array_of_insufficient_disks_dict = array_of_insufficient_disks_instance.to_dict()
# create an instance of ArrayOfInsufficientDisks from a dict
array_of_insufficient_disks_form_dict = array_of_insufficient_disks.from_dict(array_of_insufficient_disks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


