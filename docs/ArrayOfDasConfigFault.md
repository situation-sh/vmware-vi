# ArrayOfDasConfigFault

A boxed array of *DasConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DasConfigFault]**](DasConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_das_config_fault import ArrayOfDasConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDasConfigFault from a JSON string
array_of_das_config_fault_instance = ArrayOfDasConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfDasConfigFault.to_json()

# convert the object into a dict
array_of_das_config_fault_dict = array_of_das_config_fault_instance.to_dict()
# create an instance of ArrayOfDasConfigFault from a dict
array_of_das_config_fault_form_dict = array_of_das_config_fault.from_dict(array_of_das_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


