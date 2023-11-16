# ArrayOfFilterInUse

A boxed array of *FilterInUse*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FilterInUse]**](FilterInUse.md) |  | 

## Example

```python
from vmware_vi.models.array_of_filter_in_use import ArrayOfFilterInUse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFilterInUse from a JSON string
array_of_filter_in_use_instance = ArrayOfFilterInUse.from_json(json)
# print the JSON string representation of the object
print ArrayOfFilterInUse.to_json()

# convert the object into a dict
array_of_filter_in_use_dict = array_of_filter_in_use_instance.to_dict()
# create an instance of ArrayOfFilterInUse from a dict
array_of_filter_in_use_form_dict = array_of_filter_in_use.from_dict(array_of_filter_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


