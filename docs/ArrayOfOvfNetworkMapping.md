# ArrayOfOvfNetworkMapping

A boxed array of *OvfNetworkMapping*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfNetworkMapping]**](OvfNetworkMapping.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_network_mapping import ArrayOfOvfNetworkMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfNetworkMapping from a JSON string
array_of_ovf_network_mapping_instance = ArrayOfOvfNetworkMapping.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfNetworkMapping.to_json()

# convert the object into a dict
array_of_ovf_network_mapping_dict = array_of_ovf_network_mapping_instance.to_dict()
# create an instance of ArrayOfOvfNetworkMapping from a dict
array_of_ovf_network_mapping_form_dict = array_of_ovf_network_mapping.from_dict(array_of_ovf_network_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


