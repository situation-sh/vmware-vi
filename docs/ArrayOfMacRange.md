# ArrayOfMacRange

A boxed array of *MacRange*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MacRange]**](MacRange.md) |  | 

## Example

```python
from vmware_vi.models.array_of_mac_range import ArrayOfMacRange

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMacRange from a JSON string
array_of_mac_range_instance = ArrayOfMacRange.from_json(json)
# print the JSON string representation of the object
print ArrayOfMacRange.to_json()

# convert the object into a dict
array_of_mac_range_dict = array_of_mac_range_instance.to_dict()
# create an instance of ArrayOfMacRange from a dict
array_of_mac_range_form_dict = array_of_mac_range.from_dict(array_of_mac_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


