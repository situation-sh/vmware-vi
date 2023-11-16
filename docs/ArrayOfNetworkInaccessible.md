# ArrayOfNetworkInaccessible

A boxed array of *NetworkInaccessible*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetworkInaccessible]**](NetworkInaccessible.md) |  | 

## Example

```python
from vmware_vi.models.array_of_network_inaccessible import ArrayOfNetworkInaccessible

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetworkInaccessible from a JSON string
array_of_network_inaccessible_instance = ArrayOfNetworkInaccessible.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetworkInaccessible.to_json()

# convert the object into a dict
array_of_network_inaccessible_dict = array_of_network_inaccessible_instance.to_dict()
# create an instance of ArrayOfNetworkInaccessible from a dict
array_of_network_inaccessible_form_dict = array_of_network_inaccessible.from_dict(array_of_network_inaccessible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


