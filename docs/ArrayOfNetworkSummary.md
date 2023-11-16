# ArrayOfNetworkSummary

A boxed array of *NetworkSummary*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NetworkSummary]**](NetworkSummary.md) |  | 

## Example

```python
from vmware_vi.models.array_of_network_summary import ArrayOfNetworkSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNetworkSummary from a JSON string
array_of_network_summary_instance = ArrayOfNetworkSummary.from_json(json)
# print the JSON string representation of the object
print ArrayOfNetworkSummary.to_json()

# convert the object into a dict
array_of_network_summary_dict = array_of_network_summary_instance.to_dict()
# create an instance of ArrayOfNetworkSummary from a dict
array_of_network_summary_form_dict = array_of_network_summary.from_dict(array_of_network_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


