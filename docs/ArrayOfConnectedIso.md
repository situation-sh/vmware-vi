# ArrayOfConnectedIso

A boxed array of *ConnectedIso*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ConnectedIso]**](ConnectedIso.md) |  | 

## Example

```python
from vmware_vi.models.array_of_connected_iso import ArrayOfConnectedIso

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfConnectedIso from a JSON string
array_of_connected_iso_instance = ArrayOfConnectedIso.from_json(json)
# print the JSON string representation of the object
print ArrayOfConnectedIso.to_json()

# convert the object into a dict
array_of_connected_iso_dict = array_of_connected_iso_instance.to_dict()
# create an instance of ArrayOfConnectedIso from a dict
array_of_connected_iso_form_dict = array_of_connected_iso.from_dict(array_of_connected_iso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


