# InsufficientNetworkCapacity

The host does not have enough network capacity for running the virtual machine.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_network_capacity import InsufficientNetworkCapacity

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientNetworkCapacity from a JSON string
insufficient_network_capacity_instance = InsufficientNetworkCapacity.from_json(json)
# print the JSON string representation of the object
print InsufficientNetworkCapacity.to_json()

# convert the object into a dict
insufficient_network_capacity_dict = insufficient_network_capacity_instance.to_dict()
# create an instance of InsufficientNetworkCapacity from a dict
insufficient_network_capacity_form_dict = insufficient_network_capacity.from_dict(insufficient_network_capacity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


