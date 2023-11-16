# ArrayOfDVSSelection

A boxed array of *DVSSelection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DVSSelection]**](DVSSelection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_selection import ArrayOfDVSSelection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDVSSelection from a JSON string
array_of_dvs_selection_instance = ArrayOfDVSSelection.from_json(json)
# print the JSON string representation of the object
print ArrayOfDVSSelection.to_json()

# convert the object into a dict
array_of_dvs_selection_dict = array_of_dvs_selection_instance.to_dict()
# create an instance of ArrayOfDVSSelection from a dict
array_of_dvs_selection_form_dict = array_of_dvs_selection.from_dict(array_of_dvs_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


