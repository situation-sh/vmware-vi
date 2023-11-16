# SelectionSet

Base class for selecting entities  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.selection_set import SelectionSet

# TODO update the JSON string below
json = "{}"
# create an instance of SelectionSet from a JSON string
selection_set_instance = SelectionSet.from_json(json)
# print the JSON string representation of the object
print SelectionSet.to_json()

# convert the object into a dict
selection_set_dict = selection_set_instance.to_dict()
# create an instance of SelectionSet from a dict
selection_set_form_dict = selection_set.from_dict(selection_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


